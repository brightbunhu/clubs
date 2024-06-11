from django.db import models

from django.contrib.auth.models import User

    


class AddClub(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    picture = models.ImageField(upload_to='club_pictures/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', 'created']

    def __str__(self):
        return self.name

class ClubPost(models.Model):
    name = models.ForeignKey(AddClub, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=200)
    event_description = models.TextField()
    event_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    event_picture = models.ImageField(upload_to='event_pictures/')

    

    def __str__(self):
        return self.event_title
    




class AddClubLeads(models.Model):
    name = models.ForeignKey(AddClub, on_delete=models.CASCADE)
    lead_title = models.CharField(max_length=200)
    lead_name = models.CharField(max_length=200)
    lead_regnumber = models.CharField(max_length=200)
    lead_phonenumber = models.IntegerField()
    lead_email = models.EmailField()
    lead_program = models.CharField(max_length=200)
    lead_image =models.ImageField(upload_to='lead_images/')

    def __str__(self):
        return self.lead_name





class UpcomingEvent(models.Model):
    name = models.ForeignKey(AddClub, on_delete=models.CASCADE)
    upcomingevent_title = models.CharField(max_length=200)
    upcomingevent_date = models.DateField()
    upcomingevent_poster = models.ImageField(upload_to='upcoming_pictures/')

    def __str__(self):
        return self.upcomingevent_title
    



class Register(models.Model):
    name = models.ForeignKey(AddClub, on_delete=models.CASCADE)
    clubmembers_name = models.CharField(max_length=200)
    clubmembers_regnumber = models.CharField(max_length=200)
    clubmembers_program = models.CharField(max_length=200)
    clubmembers_phonenumber = models.IntegerField()
    clubmembers_email = models.EmailField()
    #dayt = created_date = models.DateField()

    def __str__(self):
        return self.clubmembers_name
    

class loginnn(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
    



