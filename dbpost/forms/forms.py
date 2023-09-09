from django import forms
from dbpost.models.models import *

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    # title = forms.CharField(max_length=500)
    # user_id = forms.IntegerField()