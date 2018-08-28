from datetime import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(
        max_length = 50,
        blank = False
    )
    input_text = models.TextField(
        verbose_name = 'Post Body',
#        max_length = 99,
        blank = False
    )
    author = models.CharField(
        max_length = 20,
        blank = False
    )
#    save date of the post
#    cannot be overriden
    date_created = models.DateTimeField(
        verbose_name = 'Timestamp',
        auto_now_add = True
    )
    last_modified = models.DateTimeField(
        verbose_name = 'Last Modified',
        auto_now = True
    )
    date_posted = models.DateField(
        verbose_name = 'Publication Schedule',
        default = datetime.now,
        blank = False
    )
    post_status = models.BooleanField(
        verbose_name = 'Post Status',
        default = False
    )