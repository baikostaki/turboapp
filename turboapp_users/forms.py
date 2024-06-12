from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    email = forms.EmailField(label="Please enter a valid email address")
    password = forms.CharField(
        label="Please enter a secure password - 1 letter, 1 special symbol, min 8 characters.",
        max_length=100,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),  # type: ignore
    )

    repeat_password = forms.CharField(
        label="Please enter your password again - 1 letter, 1 special symbol, min 8 characters.",
        max_length=100,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),  # type: ignore
    )


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "autocomplete": "email"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "current-password",
            }
        )
    )
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "repeat_password",
                "autocomplete": "current-password",
            }
        )
    )
    terms_agree = forms.BooleanField(required=True)

    class Meta:
        model = get_user_model()
        fields = ["email", "password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password != repeat_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
