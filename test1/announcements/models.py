from datetime import datetime
from django.db import models

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(
        max_length = 50,
        blank = False
    )
    input_text = models.TextField(
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
        'Date of Post Creation',
        auto_now_add = True
    )
    date_post = models.DateTimeField(
        'Date of Posting',
        default = datetime.now(),
        blank = False
    )
    post_status = models.BooleanField(
        default = False
    )