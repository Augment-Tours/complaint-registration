from django.db import models
from django import forms
from model_utils import Choices
from jsonfield import JSONField

from api.models import Timestampable, Activatable

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=200, unique=True)

class FormField(models.Model):
    FORM_TYPE = Choices('textbox', 'multiline_textbox')
    type = models.CharField(choices=FORM_TYPE, max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    hint = models.CharField(max_length=50, null=True, blank=True)
    label = models.CharField(max_length=50, null=True, blank=True)

    form = models.ForeignKey(Form,
                             related_name='form',
                             null=True,
                             on_delete=models.SET_NULL)
    data = JSONField()

class FormFieldResponse(models.Model):
    form_field = models.ForeignKey(FormField,
                                   related_name='form_field',
                                   null=True,
                                   on_delete=models.SET_NULL)

    data = JSONField()
    # test


class Category(Timestampable, Activatable):
    name = models.CharField(max_length=100)

    parent = models.ForeignKey('self',
                                related_name='children',
                                null=True,
                                on_delete=models.SET_NULL)
    
    ancestors = models.ManyToManyField('self',
                                        related_name='+',
                                        symmetrical=False)

    descendants = models.ManyToManyField('self',
                                            related_name='+', 
                                            symmetrical=False)