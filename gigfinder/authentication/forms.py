import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


'''class RegistrationForm(forms.Form):

    CHOICES = (
        ('Musician', 'Musician'),
        ('Venue', 'Venue'),
    )

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_(
        "Username"), error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(
        required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(
        required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(
        required=True, max_length=30, render_value=False)), label=_("Password (again)"))
    user_type = forms.ChoiceField(choices = CHOICES, required = True, label = 'User Type')

    def clean_username(self):
        try:
            user = User.objects.get(
                username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(
            _("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(
                    _("Passwords did not match! Please Try Again."))
        return self.cleaned_data'''

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['__all__']
