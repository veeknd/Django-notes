from .models import Record
from django import forms


class addRecordForm(forms.ModelForm):
    title =  forms.CharField(label='',max_length=100,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
    content = forms.CharField(label='',max_length=400,widget=forms.widgets.Textarea(attrs={'class':'form-control','placeholder':'Note'}))
    
    class Meta:
        model = Record
        fields= ['title','content']