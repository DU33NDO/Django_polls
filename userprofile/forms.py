from django import forms
from .models import UserProf


class CvForm(forms.ModelForm):

    class Meta:
        model = UserProf
        fields = "__all__"
