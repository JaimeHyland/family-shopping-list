from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Proposed"), (0, "Listable"))

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="list_items"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
