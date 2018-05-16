from django import forms

from .models import Action, Condition, Element, Screen, Tag, TestCase, TestData, TestStep, Project


class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ['title', 'project', 'priority', 'description', 'condition', 'teststep', 'tag']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'condition': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'teststep': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'tag': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }


class TestCaseView(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ['title', 'project', 'priority', 'description', 'condition', 'teststep', 'tag']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'project': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'priority': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'readonly': True}),
            'condition': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'readonly': True}),
            'teststep': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'readonly': True}),
            'tag': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'readonly': True}),
        }
