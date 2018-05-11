from django.conf.urls import url
from .views import test_case_detail, test_case_list, project_detail, search, new_test_case

app_name = 'TestCase'

urlpatterns = [

	url(r'^test-case-list/$', test_case_list, name = 'test_case_list'),
	url(r'^results/$', search, name = 'search'),
	url(r'^test-case-detail/(?P<slug>[-\w]+)/$', test_case_detail, name = 'test_case_detail'),
	url(r'^project-detail/(?P<slug>[-\w]+)/$', project_detail, name = 'project_detail'),
	#custom_admin
	url(r'^new-test-case/$', new_test_case, name = 'new_test_case'),


]