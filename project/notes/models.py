from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from django.db import models


class Note(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



