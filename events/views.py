from django.shortcuts import render, redirect
from events.forms import EventModelForm, CategoryModelForm, ParticipantModelForm
from events.models import Event, Category, Participant
from django.contrib import messages

# Create your views here.

def event_dashboard(request):

    participant = Participant.objects.all()
    events = Event.objects.all()
    total_participant = participant.count()
    total_events = events.count()
    upcoming_events = Event.objects.filter(status='UPCOMING').count()
    past_events = Event.objects.filter(status='PAST').count()

    context = {
        'total_participant': total_participant,
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events
    }


    return render(request, "dashboard.html", context)

def create_event(request):
    if request.method=="POST":
        form = EventModelForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'create-event.html', {'form': form, 'message': "Event Added Successfully"})

    else:
        form = EventModelForm()       

    return render(request, 'create-event.html', {'form': form})

def create_category(request):
    if request.method=="POST":
        form = CategoryModelForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'add-category.html', {'form': form, 'message': "Category Added Successfully"})



    else:
        form = CategoryModelForm()       

    return render(request, 'add-category.html', {'form': form})

def add_participant(request):
    if request.method=="POST":
        form = ParticipantModelForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'add-participant.html', {'form': form, 'message': "Participant Added Successfully"})


    else:
        form = ParticipantModelForm()       

    return render(request, 'add-participant.html', {'form': form})

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'participant_list.html', {'participants': participants})
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})