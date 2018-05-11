from django import forms

from .models import TestCase


class TestCaseForm(forms.ModelForm):

	class Meta:
		model = TestCase
		fields = ['title', 'project', 'priority', 'description', 'condition', 'teststep', 'tag']
		widgets = {
			'title' : forms.TextInput(attrs={'class' : 'form-control'}),
			'project' : forms.Select(attrs={'class' : 'form-control'}),
			'priority' : forms.Select(attrs={'class' : 'form-control'}),
			'description' : forms.TextInput(attrs={'class' : 'form-control'}),
			'condition' : forms.Select(attrs={'class' : 'form-control'}),
			'teststep' : forms.Select(attrs={'class' : 'form-control'}),
			'tag' :	forms.Select(attrs={'class' : 'form-control'}),
		}
		