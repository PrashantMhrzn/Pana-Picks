from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Newsletter(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('pending', 'Pending'),
    )
    title = models.CharField(max_length=225, null=False, default='Pana Picks Weekly')
    description = models.TextField()
    # auto_now_add=True: Sets the timestamp only once, on creation. 
    # Ideal for created_at or added_on fields.
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now=True: Updates the timestamp every time the object is saved. 
    # Ideal for updated_at or last_modified fields.
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

class Newslettercontent(models.Model):
    CONTENT_CHOICES = (
        ('article', 'Article'),
        ('recommendation', 'Recommendation'),
        ('event', 'Event'),
        ('announcement', 'Announcement'),
    )
    newsletter = models.ForeignKey(Newsletter, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=225)
    body = models.TextField()
    content_type = models.CharField(max_length=20, choices=CONTENT_CHOICES)

    def __str__(self):
        return self.subject

