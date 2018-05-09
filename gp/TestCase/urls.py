from django.conf.urls import url
from .views import TestCaseListView, TestCaseDetailView, test_case_detail, test_case_list

app_name = 'TestCase'

urlpatterns = [
	url(r'^test-case-list/$', TestCaseListView.as_view(), name = 'test_case_list_view'),
	url(r'^(?P<slug>[-\w]+)$', TestCaseDetailView.as_view(), name = 'test_case_detail_view'),
	url(r'^test-case-list-function/$', test_case_list, name = 'test_case_list'),
	url(r'^(?P<slug>[-\w]+)$', test_case_detail, name = 'test_case_detail'),

]