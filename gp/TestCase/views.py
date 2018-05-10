from django.shortcuts import render, get_object_or_404
from gp.config import pagination
# Create your views here.

from .models import Action, Condition, Element, Screen, Tag, TestCase, TestData, TestStep, Project


def test_case_list(request):
	template = 'testcase/test_case_list.html'

	object_list = TestCase.objects.all()

	pages = pagination(request, object_list, 1)

	context = {
		'items' : pages[0],
		'page_range' : pages[1],

	}
	return render(request, template, context)

def test_case_detail(request, slug):
	template = 'testcase/test_case_detail.html'

	testcase = get_object_or_404(TestCase, slug = slug)

	context = {

		'TestCase' : testcase,
	}

	return render(request, template, context)

def project_detail(request, slug):
	template = 'testcase/project_detail.html'

	project = get_object_or_404(Project, slug = slug)
	testcase = TestCase.objects.filter(project = project)

	pages = pagination(request, testcase, 1)
	context = {
		'project' : project,
		'items' : pages[0],
		'page_range' : pages[1],
	}
	return render(request, template, context)