from django import forms
from django.db.models import TextChoices

from apps.userprofile.models import Profile


class ProfileForm(forms.ModelForm):
    class Gender(TextChoices):
        FEMALE = 'female'
        MALE = 'male'

    first_name = forms.CharField(max_length=30, help_text='First Name')
    last_name = forms.CharField(max_length=50, help_text='Last Name')
    birthday = forms.DateField(help_text='Birthday')
    gender = forms.ChoiceField(
        choices=Gender.choices,
        required=False,
    )

    class Meta:
        model = Profile
        fields = forms.ModelForm.Meta.fields + ('first_name', 'last_name', 'birthday', 'gender')
