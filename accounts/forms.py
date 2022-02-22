from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            # we set for each form field a class attribute to use a Bootstrap class
            self.fields[fieldname].widget.attrs.update({'class':'form-control'})
