#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from django.http import HttpResponse
from reportlab.platypus import Image
from django.shortcuts import render
from django.http import HttpResponse
import urllib2
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests
from main.models import resume_input


PAGE_ACCESS_TOKEN = 'EAATyjn0ZCjToBAI8vGomXbBh1Uk2kHH37E62fjAkcuxhH2bW4rBZCKHftgrIiS72DILFlQVUlk6FO4Ut6k1zquTXnaZCkMLhYf2K6E7ZBt3wLHQilZCZBMfRsV3fQCilng7jfeMRoilcKsywlwnXemRbvF8KKf5kPAvR1BYPLiQwZDZD'


def resume(request,id):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mycv.pdf"'
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    pp = resume_input.objects.get_or_create(fbid=id)[0]
    #print dir(p)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setFont("Helvetica", 20)
    p.drawString(230,820, pp.name)
    p.setFont("Helvetica", 8)
    p.drawString(230,810,pp.emailid)
    p.drawString(230,800,pp.contact)
    p.drawString(230,790,pp.dob)
    p.drawString(230,780,pp.LinkedIn)
    p.drawString(230,770,pp.city)
    p.setFont("Helvetica", 13)
    
    p.drawString(0,750,"Objective")
    p.setStrokeColor(colors.red)    
    p.line(0,745,500,745)
    p.setFont("Helvetica", 9)
    p.drawString(20,735,pp.objective_line1)
    p.drawString(20,725,pp.objective_achievements)

    p.setFont("Helvetica", 13)
    p.drawString(0,705,"Educational Qualifications ")
    p.setStrokeColor(colors.red)    
    p.line(0,700,500,700)
    p.setFont("Helvetica", 9)
    p.drawString(20,690,pp.educational_qualifications_1)
    p.drawString(20,680,pp.educational_qualifications_2)
    p.drawString(20,670,pp.educational_qualifications_3)
    p.drawString(20,660,pp.educational_qualifications_4)
    
    p.drawString(0,640,"Experience")
    p.setStrokeColor(colors.red)    
    p.line(0,635,500,635)
    p.setFont("Helvetica", 9)
    p.drawString(20,625,pp.experience_1)
    p.drawString(20,625,pp.experience_1)
    p.drawString(20,605,pp.experience_1)
    p.drawString(20,595,pp.experience_1)

    p.setFont("Helvetica", 13)
    p.drawString(0,575,"Skills")
    p.setStrokeColor(colors.red)    
    p.line(0,570,500,570)
    p.setFont("Helvetica", 9)
    p.drawString(20,560,pp.skills_1)
    p.drawString(20,550,pp.skills_2)
    p.drawString(20,540,pp.skills_3)
    p.drawString(20,530,pp.skills_4)
    
    p.setFont("Helvetica", 13)
    p.drawString(0,510,"Hobbies")
    p.setStrokeColor(colors.red)    
    p.line(0,505,500,505)
    p.setFont("Helvetica", 9)
    p.drawString(20,495,pp.hobbies_1)
    p.drawString(20,485,pp.hobbies_2)
    p.drawString(20,475,pp.hobbies_3)
    p.drawString(20,465,pp.hobbies_4)

    p.showPage()
    p.save()
    return response


def cards(fbid):
    
    response_object = {
      "recipient": {
        "id": fbid
      },
      "message": {
        "attachment": {
          "type": "template",
          "payload": {
            "template_type": "generic",
            "elements": [{
              "title": "RESUME",
              "subtitle": "Don,t wait just click",
              "item_url": "https://resume-pdf.herokuapp.com/try/%s"%(fbid),               
              "image_url": "",
              "buttons": [{
                "type": "web_url",
                "url": "https://resume-pdf.herokuapp.com/try/%s"%(fbid),  
                "title": "DOWNLOAD"
              }, {
                "type": "element_share"
              }]
              
            }]
          }
        }
      }
    }

    return json.dumps(response_object)


def post_facebook_message(fbid,message_text):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    # response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})
    # status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    # print status.json()
    if message_text == 'templates':
        response_msg = cards(fbid)

    else:
        response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})

    requests.post(post_message_url, 
                    headers={"Content-Type": "application/json"},
                    data=response_msg)



def name_generator(fbid):
    url = 'https://graph.facebook.com/v2.6/%s?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=%s'%(fbid,PAGE_ACCESS_TOKEN)    
    resp = requests.get(url)
    data = json.loads(resp.text)
    name = '%s '%(data['first_name'])
    return name



class MyChatBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'resume maker':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Oops invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message= json.loads(self.request.body.decode('utf-8'))
        print incoming_message

        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                print message
                try:
                    sender_id = message['sender']['id']
                    message_text = message['message']['text']
                    pp = resume_input.objects.get_or_create(fbid =sender_id)[0]
                    data = name_generator(sender_id)

                    if message_text.lower() in 'hi,hello,hey,supp'.split(','):
                        pp.greetings = 'TRUE'
                        pp.state='1'
                        pp.save()
                        post_facebook_message(sender_id,'Hey , ' + data +', Now , please provide me with your personal details,  Your EMAILID')

                    elif pp.state =='1':
                        pp.emailid = message_text
                        pp.state='3'
                        pp.save()
                        post_facebook_message(sender_id,'Your date of birth')
                       
                        
                    elif pp.state =='3':
                        pp.dob = message_text
                        pp.state='4'
                        pp.save()
                        post_facebook_message(sender_id,'Great ,Now  Please tell me your contact PHONE NUMBER to be displayed on the resume ')
                    
                    elif pp.state =='4':
                        pp.contact = message_text
                        pp.state='5'
                        pp.save()
                        post_facebook_message(sender_id,'Great ,Now  Please provide me your LinkedIn id')

                    elif pp.state =='5':
                        pp.LinkedIn = message_text
                        pp.state='6'
                        pp.save()
                        post_facebook_message(sender_id,'Now your city of residence')
         

                    elif pp.state =='6':
                        pp.city = message_text
                        pp.state='7'
                        pp.save()
                        post_facebook_message(sender_id,'okay, now your Summary or Objective.   KEY POINTS to be included are     1)Start with your professional title     2)Add two or three achievements    , Your professional tittle and a line describing you  ')
                    
                    elif pp.state =='7':
                        pp.objective_line1 = message_text
                        pp.state='8'
                        pp.save()
                        post_facebook_message(sender_id,'Okay, your achievements if any')



 



                    elif pp.state =='8':
                        pp.objective_achievements = message_text
                        pp.state='9'
                        pp.save()
                        post_facebook_message(sender_id,'Great , now tell me your educational qualification  include your year of passing , institute name,first')

                    elif pp.state =='9':
                        pp.educational_qualifications_1 = message_text
                        pp.state ='10'
                        pp.save()
                        post_facebook_message(sender_id,'Any more? if no simply type no')

                    elif pp.state=='10':
                        for i in range(1):
                            if message_text == 'no':
                                pp.state = '12'
                                pp.save()
                                post_facebook_message(sender_id,'COOL,type no to continue')

                            else :
                                pp.educational_qualifications_2 = message_text
                                pp.state = '11'
                                pp.save()
                                post_facebook_message(sender_id,'Any more? if no simply type no')

                    elif pp.state=='11':
                        for i in range(1):
                            if message_text == 'no':
                                pp.state = '12'
                                pp.save()
                                post_facebook_message(sender_id,'COOL,type no to continue')


                            else :
                                pp.educational_qualifications_3 = message_text
                                pp.state = '12'
                                pp.save()
                                post_facebook_message(sender_id,'Any more? if no simply type no')

                    elif pp.state =='12':
                        if message_text=='no' :
                            pp.state ='13'
                            pp.save()
                            post_facebook_message(sender_id,'Great , now tell me your skills in your field,first')
                        
                        else:
                            pp.educational_qualifications_4 = message_text
                            pp.state ='13'
                            pp.save()
                            post_facebook_message(sender_id,'Great , now tell me your skills in your field,first')






                
                    elif pp.state =='13':
                        pp.skills_1 = message_text
                        pp.state ='15'
                        pp.save()
                        post_facebook_message(sender_id,'Any more? if no simply type no')

                    elif pp.state=='15':
                        for i in range(1):
                            if message_text == 'no':
                                pp.state = '17'
                                pp.save()
                                post_facebook_message(sender_id,'COOL,type no to continue')


                            else :
                                pp.skills_2 = message_text
                                pp.state = '16'
                                pp.save()
                                post_facebook_message(sender_id,'Any more? if no simply type no')

                    elif pp.state=='16':
                        for i in range(1):
                            if message_text == 'no':
                                pp.state = '17'
                                pp.save()
                                post_facebook_message(sender_id,'COOL,type no to continue')


                            else :
                                pp.skills_3 = message_text
                                pp.state = '17'
                                pp.save()
                                post_facebook_message(sender_id,'Any more? if no simply type no')

                    elif pp.state =='17':
                        if message_text=='no':
                            pp.state ='18'
                            pp.save()
                            post_facebook_message(sender_id,'Great , now tell me your experience,first')

                        else:
                            pp.skills_4 = message_text
                            pp.state ='18'
                            pp.save()
                            post_facebook_message(sender_id,'Great , now tell me your experience,first')





                   
                    elif pp.state =='18':
                        pp.experience_1 = message_text
                        pp.state ='20'
                        pp.save()
                        post_facebook_message(sender_id,'Any more? if no simply type no')

                    elif pp.state=='20':
                        for i in range(1):
                            if message_text == 'no':
                                pp.state = '22'
                                pp.save()
                                post_facebook_message(sender_id,'COOL,type no to continue')


                            else :
                                pp.experience_2 = message_text
                                pp.state = '21'
                                pp.save()
                                post_facebook_message(sender_id,'Any more? if no simply type no')

                    elif pp.state=='21':
                        for i in range(1):
                            if message_text == 'no':
                                pp.state = '22'
                                pp.save()
                                post_facebook_message(sender_id,'COOL,type no to continue')


                            else :
                                pp.experience_3 = message_text
                                pp.state = '22'
                                pp.save()
                                post_facebook_message(sender_id,'Any more? if no simply type no')

                    elif pp.state =='22':
                        if message_text == 'no':
                            pp.state ='23'
                            pp.save()
                            post_facebook_message(sender_id,'Great , now tell me your hobbies,first')

                        else:
                            pp.experience_4 = message_text
                            pp.state ='23'
                            pp.save()
                            post_facebook_message(sender_id,'Great , now tell me your hobbies,first')







                    

                    elif pp.state =='23':
                        pp.hobbies_1 = message_text
                        pp.state ='25'
                        pp.save()
                        post_facebook_message(sender_id,'Any more? if no simply type no')

                    elif pp.state=='25':
                        for i in range(1):
                            if message_text == 'no':
                                pp.state = '28'
                                pp.save()
                                post_facebook_message(sender_id,'COOL,type no to continue')


                            else :
                                pp.hobbies_2 = message_text
                                pp.state = '26'
                                pp.save()
                                post_facebook_message(sender_id,'Any more? if no simply type no')

                    elif pp.state=='26':
                        for i in range(1):
                            if message_text == 'no':
                                pp.state = '28'
                                pp.save()
                                post_facebook_message(sender_id,'COOL,type no to continue')


                            else :
                                pp.hobbies_3 = message_text
                                pp.state = '27'
                                pp.save()
                                post_facebook_message(sender_id,'Any more? if no simply type no')

                    elif pp.state =='27':
                        pp.hobbies_4 = message_text
                        pp.state ='28'
                        pp.save()
                        post_facebook_message(sender_id,'name')















                    

                    











                    elif pp.state =='28':
                        pp.name = message_text
                        pp.save()
                        post_facebook_message(sender_id,' you are done with providing the detail, now click the link that will automatically download a pdf name mycv.pdf') 
                        post_facebook_message(sender_id,'templates')

                    else:
                        post_facebook_message(sender_id,'please, say ,hey ,hi ,hello ,supp to start a conversation')

                except Exception as e:
                    print e
                    pass

        return HttpResponse()  

def index(request):
    return HttpResponse('Hello world')


















