from django import forms
from .models import News
from django.core.exceptions import ValidationError
import re

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        #fields = '__all__'
        # widgets для название класса в html

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Значение не дожлно начинаться с цифры')
        return title