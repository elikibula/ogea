from django import forms
from django.contrib.auth.models import Group
from django.forms import Textarea
from .models import Document, SubCategory, DocumentCategory

class DocumentForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
    )

    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    category = forms.ModelChoiceField(
        queryset=DocumentCategory.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    subcategory = forms.ModelMultipleChoiceField(
        queryset=SubCategory.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Document
        fields = ['title', 'file', 'description', 'category', 'subcategory', 'groups']
        widgets = {
            'subcategory': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
