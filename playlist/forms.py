from django import forms
from .models import Soundcode

#
# class SoundcodeModelForm(forms.ModelForm):
#     class Meta:
#         model = Soundcode
#
#     def __init__(self, *args, **kwargs):
#         forms.ModelForm.__init__(self, *args, **kwargs)
#         self.fields['soundcode'].queryset = Song.soundcode.all()
