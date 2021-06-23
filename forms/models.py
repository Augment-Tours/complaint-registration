from django.db import models
from django import forms

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=200, unique=True)

class FormTextBox(forms.CharField, models.Model):
    # max_length
    