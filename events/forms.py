from django import forms
from events.models import * 

class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'location', 'category', 'status']
        widgets={
            'category': forms.Select()
        }

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ParticipantModelForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'events']