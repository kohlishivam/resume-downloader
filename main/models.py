from django.db import models

# Create your models here.
class resume_input(models.Model):
    greetings = models.CharField(max_length = 250 ,  null=True)
    state= models.CharField(max_length = 1000 ,  null=True)
    fbid= models.CharField(max_length = 1000 ,  null=True)
    name = models.CharField(max_length = 250)
    emailid = models.EmailField(max_length = 1000)
    contact = models.IntegerField(max_length = 100 ,  null=True)
    details_sub11 = models.CharField(max_length = 100)
    details_sub21 = models.CharField(max_length = 100)
    details_sub22 = models.CharField(max_length = 250)
    details_sub23 = models.CharField(max_length = 250)
    details_sub24 = models.CharField(max_length = 250)
    details_sub31 = models.CharField(max_length = 250)
    details_sub32 = models.CharField(max_length = 250)
    details_sub33 = models.CharField(max_length = 250)
    details_sub34 = models.CharField(max_length = 250)
    details_sub41 = models.CharField(max_length = 250)
    details_sub42 = models.CharField(max_length = 250)
    details_sub51 = models.CharField(max_length = 250)
    details_sub52 = models.CharField(max_length = 250)
    details_sub53 = models.CharField(max_length = 250)
    details_sub54 = models.CharField(max_length = 250)



    def __str__(self):
        return self.fbid