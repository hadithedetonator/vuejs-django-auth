# projects/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Bid
from notifications.models import Notification

@receiver(post_save, sender=Bid)
def create_notification_on_new_bid(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.project.created_by,
            message=f"You have received a new bid on your project: {instance.project.title}"
        )
