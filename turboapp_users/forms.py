from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label="Please enter a valid email address")
    password = forms.CharField(
        label="Please enter a secure password - 1 letter, 1 special symbol, min 8 characters.",
        max_length=100,
        widget=forms.PasswordInput,
        attrs={"class": "form-control"},  # type: ignore
    )

    repeat_password = forms.CharField(
        label="Please enter a secure password - 1 letter, 1 special symbol, min 8 characters.",
        max_length=100,
        widget=forms.PasswordInput,
        attrs={"class": "form-control"},  # type: ignore
    )
