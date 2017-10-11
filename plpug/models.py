from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    """
    Events
    """
    title = models.CharField(
        max_length=255,
        verbose_name=_('Title'),
    )
    started_at = models.DateTimeField(
        verbose_name=_('Started at'),
    )
    ended_at = models.DateTimeField(
        verbose_name=_('Ended at'),
    )
    place = models.CharField(
        max_length=255,
        verbose_name=_('Place'),
    )
    content = models.TextField(
        verbose_name=_('Content'),
    )
    user = models.ForeignKey(
        to=User,
        related_name='event',
        related_query_name='events',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at'),
    )
    updated_at = models.DateTimeField(
        default=None,
        null=True,
        verbose_name=_('Updated at'),
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name=_('Is published'),
    )
