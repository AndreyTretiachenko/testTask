from django.db import models
from django.core.validators import MinValueValidator


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Menu(BaseModel):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class TreeMenu(BaseModel):

    title = models.CharField(max_length=30)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', db_index=True, null=True, blank =True,validators=[MinValueValidator(0)], on_delete=models.CASCADE)
    menu_url = models.CharField(max_length=50)
    is_root = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "TreeMenu"

