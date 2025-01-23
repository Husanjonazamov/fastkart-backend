from django import forms

from ..models import CouponModel


class CouponForm(forms.ModelForm):

    class Meta:
        model = CouponModel
        fields = "__all__"
