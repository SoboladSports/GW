from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

from .models import Action, Condition, Element, Screen, Tag, TestCase, TestData, TestStep


class TestCaseListView(ListView):
	model = TestCase

	def get_context_data(self, **kwargs):
		context = super(TestCaseListView, self).get_context_data(**kwargs)
		return context


class TestCaseDetailView(DetailView):
	model = TestCase

	def get_context_data(self, **kwargs):
		context = super(TestCaseDetailView, self).get_context_data(**kwargs)
		return context


def test_case_list(request):
	template = 'testcase/test_case_list.html'
	object_list = TestCase.objects.all()
	context = {
		'object_list' : object_list,

	}
	return render(request, template, context)

def test_case_detail(request, slug):
	template = 'testcase/test_case_detail.html'
	testcase = get_object_or_404(TestCase, slug = slug)
	context = {

		'TestCase' : testcase,
	}

	return render(request, template, context)
