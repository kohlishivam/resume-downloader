from django.db import models

# Create your models here.
class resume_input(models.Model):
    greetings = models.CharField(max_length = 250)
    state = models.CharField(max_length = 1000)
    city = models.CharField(max_length = 1000)
    dob = models.CharField(max_length = 1000)
    LinkedIn = models.CharField(max_length = 1000)
    fbid= models.CharField(max_length = 1000 )
    name = models.CharField(max_length = 250)
    emailid = models.CharField(max_length = 1000)
    contact = models.CharField(max_length = 100)
    objective_line1 = models.CharField(max_length = 100)
    objective_achievements = models.CharField(max_length = 100)
    educational_qualifications_1 = models.CharField(max_length = 100)
    educational_qualifications_2 = models.CharField(max_length = 100)
    educational_qualifications_3 = models.CharField(max_length = 100)
    educational_qualifications_4 = models.CharField(max_length = 100)
    skills_1 = models.CharField(max_length = 100)
    skills_2 = models.CharField(max_length = 100)
    skills_3 = models.CharField(max_length = 100)
    skills_4 = models.CharField(max_length = 100)
    experience_1 = models.CharField(max_length = 100)
    experience_2 = models.CharField(max_length = 100)
    experience_3 = models.CharField(max_length = 100)
    experience_4 = models.CharField(max_length = 100)
    hobbies_1 = models.CharField(max_length = 100)
    hobbies_2 = models.CharField(max_length = 100)
    hobbies_3 = models.CharField(max_length = 100)
    hobbies_4 = models.CharField(max_length = 100)
    






    def __str__(self):
        return self.fbid