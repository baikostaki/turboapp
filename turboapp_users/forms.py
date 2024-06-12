from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    # email = forms.EmailField(label="Please enter a valid email address")
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "autocomplete": "email",
                "placeholder": "Please enter your email",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "current-password",
                "placeholder": "Please enter your password",
            }
        )
    )


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "autocomplete": "email",
                "placeholder": "Please enter a valid email address",
            },
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "current-password",
                "placeholder": "Please enter your password",
            }
        )
    )
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "repeat_password",
                "autocomplete": "current-password",
                "placeholder": "Please re-enter your password",
            }
        )
    )
    terms_agree = forms.BooleanField(required=True)

    class Meta:
        model = get_user_model()
        fields = ["email", "password"]
        # TODO: Check if fields need to contain the checkbox
        # TODO: When raising error, checkbox is checkeds, should be unchecked.

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password != repeat_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
