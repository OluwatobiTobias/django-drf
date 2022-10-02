import re
from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.text[:20]