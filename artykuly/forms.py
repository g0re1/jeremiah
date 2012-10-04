from django.forms import ModelForm, CharField, Textarea, HiddenInput
from jeremiah.artykuly.models import *
 
class CommentForm(ModelForm):
     class Meta:
          model = Comment
          fields = ('content','login','email',)
     login = CharField(required=True)
     email = CharField(required=False)
     content = CharField(required=True,widget=Textarea)
