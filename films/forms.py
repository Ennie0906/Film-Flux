from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Films

class FilmForm(forms.ModelForm):
    """ Form to create a recipe """ 
    class Meta:
        model = Films
        fields = ['title', 'review', 'rating', 'film_type', 'image', 'image_alt']

        review = forms.CharField(widget=RichTextWidget())

        widget = {
            'description' : forms.Textarea(attrs={'rows': 5})
    
        }

        labels = {
            'title' : 'Films Title',
            'description': 'Description',
            'review': 'Review',
            'image': 'Film Image',
            'image_alt': 'Describe Image',
            'film_type': 'Film Type',
            'rating': 'Rating',
        }