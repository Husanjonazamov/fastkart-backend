from django import forms

from ..models import WishlistModel


class WishlistForm(forms.ModelForm):

    class Meta:
        model = WishlistModel
        fields = "__all__"
