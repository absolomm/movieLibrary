from django import forms

from .models import movies

class MovieForm(forms.ModelForm):
    class Meta:
        model = movies
        fields = ('Movie_Icon','Name','Type','Movie_File','Client','Project_Manager')
