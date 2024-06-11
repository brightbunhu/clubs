from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import AddClub, AddClubLeads, Register, ClubPost, UpcomingEvent
from .forms import (
    AddClubForm,
    ClubPostForm, 
    UpcomingEventForm,
    RegisterForm,
    AddClubLeadsForm,
    SearchForm,
    LoginForm,
    ClubForm,

)
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib import messages


def delete_club(request, pk):
    club = AddClub.objects.get(id=pk)
    club.delete()
    messages.success(request, "Club deleted successfully!")
    return redirect('club_list')




def update_club(request, pk):
    club = AddClub.objects.get(id=pk)
    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            messages.success(request, "Club updated successfully!")
            return redirect('club_list')
    else:
        form = ClubForm(instance=club)
    return render(request, 'update_club.html', {'form': form})



def search(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    results = AddClub.objects.filter(name__icontains=q)

    context = {"results": results}
    return render(request, "search.html", context)


# Home views
def leadshome(request):
    lists = AddClub.objects.all()  # get all AddClub objects from the database
    context = {"lists": lists}

    return render(request, "b/leadshome.html", context)

def home(request):
    lists = AddClub.objects.all()  # get all AddClub objects from the database
    context = {"lists": lists}

    return render(request, "home.html", context)


# users home
def usershome(request):
    form = SearchForm(request.GET)
    lists = AddClub.objects.all()  # get all AddClub objects from the database
    context = {"lists": lists, "form": form}

    return render(request, "users/usershome.html", context)


#j
def clubinfo(request, pk):
    club = AddClub.objects.get(id=pk)
    posts = ClubPost.objects.filter(name=club.id)
    upcoming = UpcomingEvent.objects.filter(name=club.id)
    leads = AddClubLeads.objects.filter(name=club.id)
    context = {"club": club, "posts": posts, "upcoming": upcoming, "leads": leads}
    return render(request, "users/club_info.html", context)


# Adding a club

class ClubListView(ListView):
    model = AddClub
    template_name = "club_list.html"
    context_object_name = "clubs"



def addclub(request):
    if request.method == "POST":
        form = AddClubForm(request.POST, request.FILES)

        if form.is_valid():
            club_name = form.cleaned_data["name"]
            if not AddClub.objects.filter(name=club_name).exists():
                form.save()
                return redirect("club_list")
            else:
                messages.error(request, "A club with this name already exists.")
    else:
        form = AddClubForm()

    return render(request, "addclub.html", {"form": form})


# PAst Events Posts

class club_detail(ListView):
    model = ClubPost
    template_name = "b/clubposts.html"
    context_object_name = "clubdetail"



def createpost(request):
    if request.method == "POST":
        form = ClubPostForm(request.POST, request.FILES)
        if form.is_valid():
            club_detail = form.save()
            return redirect("club_detail")
    else:
        form = ClubPostForm()
    return render(request, "createpost.html", {"form": form})


# UPcoming Event
class event_detail(ListView):
    model = UpcomingEvent
    template_name = "b/event_detail.html"
    context_object_name = "event_details"



def create_upcoming_event(request):
    if request.method == "POST":
        form = UpcomingEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            return redirect("event_detail")
    else:
        form = UpcomingEventForm()
    return render(request, "create_upcoming_event.html", {"form": form})


# creating a register

class addregister(ListView):
    model = Register
    template_name = "b/register.html"
    context_object_name = "registers"



def create_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            register = form.save()
            return redirect("addregister")
    else:
        form = RegisterForm()
    return render(request, "create_register.html", {"form": form})


# ADding club leaders
class addclubleads_detail(ListView):
    model = AddClubLeads
    template_name = "b/addclubleads_detail.html"
    context_object_name = "leads"


def create_addclubleads(request):
    if request.method == "POST":
        form = AddClubLeadsForm(request.POST, request.FILES)
        if form.is_valid():
            addclubleads = form.save()
            return redirect("addclubleads_detail")
    else:
        form = AddClubLeadsForm()
    return render(request, "create_addclubleads.html", {"form": form})

def loogin(request):

    return render(request, "loogin.html")


def loginpage(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")

    else:
        form = LoginForm()

    context = {"form": form}
    return render(request, "c/login.html", context)



