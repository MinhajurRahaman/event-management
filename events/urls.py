from django.urls import path
from events.views import event_dashboard, create_event, create_category, add_participant, participant_list, event_list, home

urlpatterns = [
    path('event-dashboard/', event_dashboard, name='dashboard'),
    path('create-event/', create_event, name='create_event'),
    path('create-category/', create_category, name='create_category'),
    path('create-participant/', add_participant, name='create_participant'),
    path('participants/', participant_list, name='participant_list'),
    path('events/', event_list, name='event_list'),
    path("", home)
]
