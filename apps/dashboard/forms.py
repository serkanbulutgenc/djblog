'''
class ProfileForm(forms.ModelForm):
    """Form definition for Profile."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = helper.FormHelper()
        self.helper.form_id = 'profile-form'
        self.helper.layout = Layout(
            Fieldset(
                'Profile',
                Row(
                    Column(Field('first_name')),
                    Column(Field('last_name')),
                ),
                'bio',
            )
        )

    class Meta:
        """Meta definition for Profileform."""

        model = Profile
        fields = ('first_name', 'last_name', 'bio')
'''
