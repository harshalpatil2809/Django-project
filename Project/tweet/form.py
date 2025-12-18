from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']



# class SignupForm(forms.Form):
#     username = forms.CharField(
#         max_length=100,
#         label="Username"
#     )
#     email = forms.EmailField(
#         max_length=150,
#         label="Email"
#     )
#     password = forms.CharField(
#         max_length=30,
#         label="password"
#     )
