from django.db import models
from django.core.validators import MinValueValidator


class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True


class TreeMenu(BaseModel):
    menu_name = models.CharField(max_length=20)
    id_parent = models.IntegerField(db_index = True, null = True, blank = True,validators = [MinValueValidator(1)])
    menu_url = models.CharField(max_length = 50)

