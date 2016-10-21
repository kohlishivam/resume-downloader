from django.shortcuts import render

# Create your views here.
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from django.http import HttpResponse
from reportlab.platypus import Image




PAGE_ACCESS_TOKEN = 'EAATyjn0ZCjToBAOgI9PDxTmeC7hmZCtinfMQcmRZCapf9jt2nDhkFKZBOVHA2W9j0RYthJhHrtSZBh33ido0QLPZC2hmTwCmTP1NRS63Egq4WfrLn0EhSZAH9x9GkwwboYWUdKTFOuFIklMiXuxttlmQ3INk9uZCZAIZBUwxOD6zH0bwZDZD'






def try_test(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="my cv.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    #print dir(p)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setFont("Helvetica", 20)
    p.drawString(230,820, "SHIVAM KOHLI")
    p.setFont("Helvetica", 8)
    p.drawString(230,810,"kohlishivam5522@gmail.com")
    p.drawString(230,800,"9868074022")
    p.setFont("Helvetica", 13)
    
    p.drawString(0,790,"Objective")
    p.setStrokeColor(colors.red)    
    p.line(0,785,500,785)
    p.setFont("Helvetica", 9)
    p.drawString(20,775,"To pursue a dynamic and challenging career in a growth oriented company.")

    p.setFont("Helvetica", 13)
    p.drawString(0,755,"Professional Summary")
    p.setStrokeColor(colors.red)    
    p.line(0,750,500,750)
    p.setFont("Helvetica", 9)
    p.drawString(20,740,"Guru Tegh Bahadur Institute Of Technology Student , 2nd year , B.Tech Computer Science")
    p.drawString(20,730,"Fast and interested learner")
    p.drawString(20,720,"In depth knowledge of Data Structures , Web development and Android development")
    p.drawString(20,710,"Knowledge of various programming languages like C++ , Python , Javascript , php , etc")
    
    p.drawString(0,690,"Skills")
    p.setStrokeColor(colors.red)    
    p.line(0,685,500,685)
    p.setFont("Helvetica", 9)
    p.drawString(20,675,"Data Structures : Well versed with data structures")
    p.drawString(20,665,"Front-End Web Development : In depth knowledge of html,css,javascript,jquery etc")
    p.drawString(20,655,"Backend-End Web Devepolment : Good knowedge of Django , Python ,php")
    p.drawString(20,645,"Android Development (created basic apps revoloving around the use of various apis)")

    p.setFont("Helvetica", 13)
    p.drawString(0,625,"Education")
    p.setStrokeColor(colors.red)    
    p.line(0,620,500,620)
    p.setFont("Helvetica", 9)
    p.drawString(20,610,"2015   High School Diploma from    Indraprastha International School,Dwarka New Delhi")
    p.drawString(20,600,"2019   Bachelors of Technology:Computer Science from Guru Tegh Bahadur Institute of School,Rajouri Garden,New Delhi")
    
    p.setFont("Helvetica", 13)
    p.drawString(0,580,"Hobbies")
    p.setStrokeColor(colors.red)    
    p.line(0,575,500,575)
    p.setFont("Helvetica", 9)
    p.drawString(20,565,"Learning Latest Web and Android Technologies")
    p.drawString(20,555,"Currently working on chatbots")
    p.drawString(20,545,"Surfing net")
    p.drawString(20,535,"Playing badminton , cycling , Swimmng , Basketball")



    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


def userdeatils(fbid):
    url = 'https://graph.facebook.com/v2.6/' + fbid + '?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=' + PAGE_ACCESS_TOKEN
    resp = requests.get(url=url)
    data =json.loads(resp.text)
    return data         




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

                    

                    if 'hey' in message_text:
                        data = userdeatils(sender_id)
                        post_facebook_message(sender_id, 'hey'+ data +'!  Here is the link of your resume https://shrouded-reaches-29290.herokuapp.com/resume/'+data)


                    else:
                        post_facebook_message(sender_id,'please say hey to talk')

                except Exception as e:
                    print e
                    pass

        return HttpResponse()  

def index(request):
    return HttpResponse('Hello world')



















