from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AdminUserCreationForm,
    AuthenticationForm,
    BaseUserCreationForm,
    UserChangeForm,
    UserCreationForm,
)


class CustomAdminUserCreationForm(AdminUserCreationForm):
    class Meta(AdminUserCreationForm.Meta):
        model = get_user_model()
        # fields = AdminUserCreationForm.Meta.fields + ('phone',)
        # exclude = ('usable_password')


class CustomAdminUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # fields = AdminUserCreationForm.Meta.fields + ('phone',)
        # exclude = ('first_name', 'last_name')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserLoginForm(AuthenticationForm):

    def __init__(self, request = None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        print(self.request)
        self.fields["username"].widget.attrs["class"] = 'form-control'

    class Meta:
        widgets = {"username":forms.TextInput(attrs={"class":'form-control', "placeholder":'username or email'})}


class SignupForm(BaseUserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={"placeholder":"password", "class":'form-control'}),
    )
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password again"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    

    class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        fields = BaseUserCreationForm.Meta.fields+ ('phone',)
        # field_classes={
        #    "username":forms.CharField
        # }
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'username'}) }


    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone = self.cleaned_data.get('phone', None)
        user = super().save(commit)
        print("user:",user)
        return user
    
class TestForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(max_value=120, min_value=18, help_text='Age help text')

    class Meta:
        fields = ['name', 'age']
        
