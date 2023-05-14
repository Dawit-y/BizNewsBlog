
from django import forms
from .models import *


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('text',)