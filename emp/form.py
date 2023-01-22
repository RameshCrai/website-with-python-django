from django import forms
# from .models import Emp


class FeedbackForm(forms.Form):
   email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
   name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
   feedback = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))



# class EmpForm(forms.ModelForm):
#     class Meta:
#         model=Emp
#         fields=['name''email','mobile','address']

