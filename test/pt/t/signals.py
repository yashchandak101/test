from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel, SignalCreatedModel

@receiver(post_save, sender=TestModel)
def create_from_signal(sender, instance, **kwargs):
    print("Signal running: creating SignalCreatedModel")
    SignalCreatedModel.objects.create(message="Created in signal")


    # Yes, by default, Django signals run in the same database transaction as the caller. 
    # This means that if the outer transaction is rolled back, the effects of the signal (if they interact with the DB) are also rolled back.
