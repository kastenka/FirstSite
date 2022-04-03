from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Text', required=False,
                              widget=forms.Textarea(attrs={"class": "form-control", "rows": "5"}))
    is_published = forms.BooleanField(label='Published', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select a category',
                                      widget=forms.Select(attrs={"class": "form-control"}))
