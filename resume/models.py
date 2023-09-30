from django.db import models

# Create your models here.
from django.db import models
from django import forms


class tb_memo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_memo'


class YourForm(forms.Form):
    name = forms.CharField(label='이름', max_length=100)
    content = forms.CharField(label='내용', widget=forms.Textarea)