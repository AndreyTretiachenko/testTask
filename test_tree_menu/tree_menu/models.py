from django.db import models
from django.core.validators import MinValueValidator


class TreeMenu(models.Model):
    menu_name = models.CharField(max_length=20)
    id_parent = models.IntegerField(db_index = True, null = True, blank = True,validators = [MinValueValidator(1)])
    menu_url = models.CharField(max_length = 50)