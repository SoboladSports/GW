from django.conf.urls import url
from .views import TestCaseListView, TestCaseDetailView, test_case_detail, test_case_list, project_detail

app_name = 'TestCase'

urlpatterns = [

	url(r'^test-case-list/$', test_case_list, name = 'test_case_list'),
	url(r'^test-case-detail/(?P<slug>[-\w]+)/$', test_case_detail, name = 'test_case_detail'),
	url(r'^project-detail/(?P<slug>[-\w]+)/$', project_detail, name = 'project_detail'),


]