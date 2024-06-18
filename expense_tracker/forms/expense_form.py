from django import forms
from ..models import Expense, Category, SubCategory, Shop


class ExpenseForm(forms.ModelForm):
    new_category = forms.CharField(max_length=100, required=False, label="New Category")
    # exitsing_categories = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     requred=False,
    #     blank=True,
    #     label="Current categories",
    # )

    class Meta:
        model = Expense
        fields = [
            "name",
            "description",
            "amount",
            "date",
            "categories",
            "new_category",
            "shop",
        ]
        widgets = {
            "category": forms.CheckboxSelectMultiple(
                {"class": "form-control", "size": "5"}
            ),
            "shop": forms.Select,
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["categories"].required = False

    def clean(self):
        cleaned_data = super().clean()
        new_category_name = cleaned_data.get("new_category")
        existing_categories = cleaned_data.get("existing_categories")
        if not new_category_name:
            return cleaned_data

        if new_category_name and existing_categories:
            raise forms.ValidationError(
                "Choose an existing category or add a new one"
            )  # TODO: Add custom valdidation form

        if new_category_name:
            existing_categories = Category.objects.filter(
                name__iexact=new_category_name
            )
            if existing_categories.exists():
                cleaned_data["new_category"] = (
                    None  # Clear the new_category field if category exists. TODO: examine this
                )
        return cleaned_data
