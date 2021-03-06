from __future__ import unicode_literals

from django.db import models

from django import forms

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class meta(object):
        """docstring for meta"""
        ordering = ('-timestamp',)

class BlogPostForm(forms.ModelForm):
    """docstring for BlogPostForm"""
    class Meta:
        ''' base on BlogPost '''
        model = BlogPost
        exclude = ('timestamp',)