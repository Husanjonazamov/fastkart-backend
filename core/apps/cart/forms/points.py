from django import forms

from ..models import PointsModel


class PointsForm(forms.ModelForm):

    class Meta:
        model = PointsModel
        fields = "__all__"
