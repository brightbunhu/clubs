from django import forms
from .models import AddClub, ClubPost, UpcomingEvent, Register, AddClubLeads


class ClubForm(forms.ModelForm):
    class Meta:
        model = AddClub
        fields = ('name', 'description', 'picture')


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', widget=forms.TextInput(attrs={'class': 'form-control'}))

class ClubPostForm(forms.ModelForm):
    class Meta:
        model = ClubPost
        fields = ('name', 'event_title', 'event_description', 'event_date','event_picture')


class AddClubForm(forms.ModelForm):
    class Meta:
        model = AddClub
        fields = ['name', 'description', 'picture']

class UpcomingEventForm(forms.ModelForm):
    class Meta:
        model = UpcomingEvent
        fields = ['name', 'upcomingevent_title', 'upcomingevent_date', 'upcomingevent_poster']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'clubmembers_name', 'clubmembers_regnumber', 'clubmembers_program', 'clubmembers_phonenumber', 'clubmembers_email']

class AddClubLeadsForm(forms.ModelForm):
    class Meta:
        model = AddClubLeads
        fields = ['name', 'lead_title', 'lead_name', 'lead_regnumber', 'lead_phonenumber', 'lead_email', 'lead_program', 'lead_image']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

