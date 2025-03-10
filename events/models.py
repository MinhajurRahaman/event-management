from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    STATUS_CHOICES = [
        ('UPCOMING', 'Upcoming'),
        ('PAST', 'Past')
    ]
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    date = models.DateField()
    time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="events", default=1)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='UPCOMING')

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    events = models.ManyToManyField(Event, related_name="participants")

    def __str__(self):
        return self.name