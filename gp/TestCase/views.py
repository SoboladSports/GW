from django.shortcuts import render, get_object_or_404
from gp.config import pagination
from django.db.models import Q
from django.contrib import messages
# Create your views here.

from .models import Action, Condition, Element, Screen, Tag, TestCase, TestData, TestStep, Project
from .forms import TestCaseForm, TestCaseView


def test_case_list(request):
    template = 'testcase/test_case_list.html'

    object_list = TestCase.objects.all()

    pages = pagination(request, object_list, 1)

    context = {
        'items': pages[0],
        'page_range': pages[1],

    }
    return render(request, template, context)


def test_case_detail(request, slug):
    template = 'testcase/new_test_case.html'

    testcase = get_object_or_404(TestCase, slug=slug)
    form = TestCaseView(instance=testcase)

    context = {

        'TestCase': testcase,
        'form': form,
    }

    return render(request, template, context)


def project_detail(request, slug):
    template = 'testcase/project_detail.html'

    project = get_object_or_404(Project, slug=slug)
    testcase = TestCase.objects.filter(project=project)

    pages = pagination(request, testcase, 10)
    context = {
        'project': project,
        'items': pages[0],
        'page_range': pages[1],
    }
    return render(request, template, context)


def search(request):
    template = 'testcase/test_case_list_admin.html'

    query = request.GET.get('qText')

    if query:
        results = TestCase.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        results = TestCase.objects.all()

    pages = pagination(request, results, num=5)

    context = {
        'items': pages[0],
        'page_range': pages[1],
        'query': query,
    }

    return render(request, template, context)


def new_test_case(request):
    template = 'testcase/new_test_case.html'
    form = TestCaseForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Test Case has been saved to the database')
    # else:
    except Exception as e:
        messages.warning(request, 'Test Case has not been saved. Error: {}'.format(e))

    context = {

        'form': form,

    }

    return render(request, template, context)


def edit_test_case(request, pk):
    template = 'testcase/new_test_case.html'
    testcase = get_object_or_404(TestCase, pk=pk)

    if request.method == "POST":
        form = TestCaseForm(request.POST, instance=testcase)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Test Case has been updated in the database')
        except Exception as e:
            messages.warning(request, 'Test Case has not been updated. Error: {}'.format(e))
    else:
        form = TestCaseForm(instance=testcase)

    context = {
        'form': form,
        'testcase': testcase,
    }
    return render(request, template, context)


def delete_test_case(request, pk):
    template = 'testcase/new_test_case.html'

    testcase = get_object_or_404(TestCase, pk=pk)
    try:
        if request.method == 'POST':
            form = TestCaseForm(request.POST, instance=testcase)
            testcase.delete()
            messages.success(request, 'Test Case was deleted from the database')
        else:
            form = TestCaseForm(instance=testcase)
    except Exception as e:
        messages.warning(request, 'Test Case could not been deleted. Error: {}'.format(e))

    context = {
        'form': form,
    }

    return render(request, template, context)


def test_case_list_admin(request):
    template = 'testcase/test_case_list_admin.html'
    testcase = TestCase.objects.all()
    pages = pagination(request, testcase, 5)
    context = {
        'items': pages[0],
        'page_range': pages[1],
    }

    return render(request, template, context)
