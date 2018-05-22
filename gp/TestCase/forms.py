from django import forms
from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet

from .models import Project, Screen, Element, TestData, Action, Condition, Step, TestStep, Tag, TestCase, Cases, TestCycle

'''class BaseTestCaseFormset(BaseInlineFormSet):

    def add_fields(self, form, index):
        super(BaseTestCaseFormset, self).add_fields(form, index)


        try:
            instance = self.get_queryset()[index]
            pk_value = instance.pk
        except IndexError:
            instance = None
            pk_value = hash(form.prefix)

        form.nested = [

        ]


TestCaseFormset = inlineformset_factory(TestCase, Condition, formset=BaseTestCaseFormset, extra=1)
'''



'''
class ConditionForm(forms.ModelForm):
    class Meta:
        model = Condition
        fields = ['title', 'screen', 'element', 'action', 'testdata', 'project',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'screen': forms.Select(attrs={'class': 'form-control'}),
            'element': forms.Select(attrs={'class': 'form-control'}),
        }

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
'''
