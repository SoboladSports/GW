from django.shortcuts import render, get_object_or_404
from gp.config import pagination
from django.db.models import Q
from django.contrib import messages
# Create your views here.

from .models import Project, Screen, Element, TestData, Action, Condition, Step, TestStep, Tag, TestCase, Cases, TestCycle
#from .forms import TestCaseForm, TestCaseView


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

    context = {
        'testcase': testcase,
    }

    return render(request, template, context)
















def project_detail(request, slug):
    template = 'testcase/project_detail.html'

    project = get_object_or_404(Project, slug=slug)
    testcase = TestCase.objects.filter(project=project)

    pages = pagination(request, testcase, 2)

    context = {
        'project': project,
        'items': pages[0],
        'page_range': pages[1],
    }
    return render(request, template, context)


def search(request):
    template = 'testcase/test_case_list_admin.html'
    testcase = TestCase.objects.all()

#   query parsing
    queryProject = request.GET.get('qProject')
    queryText = request.GET.get('qText')
    queryPriority = request.GET.get('qPriority')
    queryTags = request.GET.get('qTags')


#   Project query part
#   Findning all the projects
    projects = Project.objects.all()

#   Checking, if project from query exists
#   If true -> saving the id of this project in project_id var
    project_id = 0
    if queryProject:
        for p in projects:
            if p.get_title() == queryProject:
                project_id = p.id

#   creating the result part for the project query
    resultsProject = []
#   if the project doesn't exist: result = []
    if (not project_id and queryProject != ''):
        resultsProject = []
#   trying to find some testcases with existing project_id otherwise
    elif queryProject:
        for t in testcase:
            if t.get_project().id == project_id:
                resultsProject.append(t)
#   if project query is '', result = all()
    else:
        resultsProject = TestCase.objects.all()




#   Text query part
#   Finding all the projects with this text in title or in description
    if queryText:
        resultsText = TestCase.objects.filter(Q(title__icontains=queryText) | Q(description__icontains=queryText))
#   If query = '', result = all()
    else:
        resultsText = TestCase.objects.all()




#   Priority query part
    resultsPriority = []
    if queryPriority:
        for t in testcase:
            if (t.get_priority() == queryPriority):
                resultsPriority.append(t)
#   If query = '', result = all()
    else:
        resultsPriority = TestCase.objects.all()




#   Tags query part
    resultsTag = []
    if queryTags:

        tmpQueryTags = queryTags.replace(' ', '').split(',')
        for t in testcase:
            for tmp in tmpQueryTags:
                if (set(tmpQueryTags).issubset(set(t.get_tags()))):
                    resultsTag.append(t)
    else:
        resultsTag = TestCase.objects.all()


    results = list(set(resultsText) & set(resultsProject) & set(resultsPriority) & set(resultsTag))

    pages = pagination(request, results, num=5)

    context = {
        'items': pages[0],
        'page_range': pages[1],
        'queryText': queryText,
        'queryProject': queryProject,
        'queryTags': queryTags,
        'queryPriority': queryPriority,
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



def test_cycle_list(request):
    template = 'testcase/test_cycle_list.html'
    testcycle = TestCycle.objects.all()
    pages = pagination(request, testcycle, 5)
    context = {
        'items': pages[0],
        'page_range': pages[1]
    }

    return render(request, template, context)


def test_cycle_detail(request, slug):
    template = 'testcase/test_cycle_detail.html'
    testcycle = get_object_or_404(TestCycle, slug=slug)
    testcases = []
    for t in testcycle.testcase.all():
        testcases.append(t)
    pages = pagination(request, testcases, 5)

    context = {
        'items': pages[0],
        'page_range': pages[1],
        'testcycle': testcycle,
    }

    return render(request, template, context)


def test_case_detail_in_progress(request, slug):
    template = 'testcase/new_test_case.html'

    testcase = get_object_or_404(TestCase, slug=slug)

    context = {
        'testcase': testcase,
    }

    return render(request, template, context)




def sample(request):
    template = 'testcase/sample.html'



    context = {

    }
    return render(request, template, context)

def edit_test_case(request, pk):
    template = 'testcase/new_test_case.html'
    testcase = get_object_or_404(TestCase, pk=pk)


    def create_new_tag():
        queryTag = request.POST.get('NewTag')
        if request.method == "POST":
            try:
                if queryTag:
                    newTag = Tag()
                    newTag.title = queryTag
                    newTag.save()
                    messages.success(request, 'SUCCESS')
            except Exception as e:
                messages.warning(request, 'Got some troubles. Error: {}'.format(e))
        else:
            pass
    create_new_tag()
    '''if request.method == "POST":
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Test Case has been updated in the database')
        except Exception as e:
            messages.warning(request, 'Test Case has not been updated. Error: {}'.format(e))
    else:
        pass
        '''
    context = {
        'testcase': testcase,
    }
    return render(request, template, context)
