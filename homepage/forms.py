from .models import FoodImages
from django import forms


class UploadForms(forms.ModelForm):

    name = forms.CharField(required=True)
    category = forms.CharField(required=True)
    cost = forms.DecimalField()

    #     images = forms.CharField(
    #        widget = forms.ClearableFileInput(attrs={'class':'form-control'}),
    #        required=True
    #    )
    class Meta:
        model = FoodImages
        fields = ["name", "category", "cost"]
