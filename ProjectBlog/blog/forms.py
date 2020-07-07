from django import forms
from .models import Comment


class commentForm(forms.ModelForm):
    
    
    class Meta:
        model = Comment
        fields = (('coms'),)
        widgets={
                   "coms":forms.Textarea(attrs={'placeholder':'Enter Comment','name':'Name','id':'common_id_for_imputfields','class':'form-control','rows':'3'})
                }      