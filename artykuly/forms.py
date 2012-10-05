from django.forms import ModelForm, CharField, Textarea
from artykuly.models import Comment
 
class CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ('content', 'login', 'email',)
    
    login = CharField(required=True)
    email = CharField(required=False)
    content = CharField(required=True, widget=Textarea)
