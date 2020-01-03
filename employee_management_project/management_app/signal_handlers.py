from django.dispatch import receiver
from django.db.models.signals import post_save
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import Company


@receiver(post_save, sender=Company)
def companies_list_reload_page(**kwargs):
    """
    Automatically reloads companies list page 
    when changes have occurred in the `Company` model.
    """
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        'companies_list',
        {
            'type': 'reload_page',
            'reload_page': True,
        }
    )
