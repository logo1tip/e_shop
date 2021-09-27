from django import forms
from user.models import User

class UserSignIn(forms.Form):

    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(
            attrs={
                "id": "first_name",
                "class": "form-control",
                "placeholder": "First name",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'First name'",
            }
        ),
    )
    email = forms.EmailField(
        label="User email",
        widget=forms.TextInput(
            attrs={
                "id": "email",
                "class": "form-control",
                "placeholder": "User email",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'User email'",
            }
        ),
    )
    phone = forms.CharField(
    label="Phome number",
    widget=forms.TextInput(
        attrs={
            "id": "subject",
            "class": "form-control",
            "placeholder": "Phone Number",
            "onfocus": "this.placeholder = ''",
            "onblur": "this.placeholder = 'Phone Number'",
        }
    ),
)
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "id": "password",
                "class": "form-control",
                "placeholder": "Password",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Password'",
            }
        ),
    )
    repeat_password = forms.CharField(
        label="Password repeat",
        widget=forms.PasswordInput(
            attrs={
                "id": "repeat_password",
                "class": "form-control",
                "placeholder": "Password repeat",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Password repeat'",
            }
        ),
    )
    is_agree = forms.BooleanField(
        label="Is agree",
        widget=forms.CheckboxInput(
            attrs={
                "id": "is_agree",
                "class": "form-control",
            }
        ),
    )

    def clean(self):
        is_error = False
        try:
            tmp_user = User.objects.get(email=self.cleaned_data["email"])
        except User.DoesNotExist:
            ...
        else:
            self.add_error("email", "Такой пользователь уже существует.")
            is_error = True
        if self.cleaned_data["password"] != self.cleaned_data["repeat_password"]:
            self.add_error("password", "Пароли не совпадают.")
            self.add_error("repeat_password", "Пароли не совпадают.")
            is_error = True
        if not self.cleaned_data["is_agree"]:
            self.add_error("is_agree", "Нужно подтвердить.")
            is_error = True
        if is_error:
            raise forms.ValidationError("Что-то пошло не так.")
        return super().clean()

    def save(self):
        new_user = User(
            first_name=self.changed_data["first_name"],
            email=self.changed_data["email"],
            phone=self.changed_data["phone"],
            password=self.changed_data["password"],
        )
        new_user.save()