from django.conf.urls import url
from .views import test_case_detail, test_case_list, project_detail, search, new_test_case, test_case_list_admin, \
    edit_test_case, delete_test_case, test_cycle_list, test_cycle_detail, test_case_detail_in_progress, sample

app_name = 'TestCase'

urlpatterns = [

    url(r'^test-case-list/$', test_case_list, name='test_case_list'),
    url(r'^results/$', search, name='search'),
    url(r'^test-case-detail/(?P<slug>[-\w]+)/$', test_case_detail, name='test_case_detail'),
    url(r'^project-detail/(?P<slug>[-\w]+)/$', project_detail, name='project_detail'),
    url(r'^sample/$', sample, name='sample'),
    # custom_admin
    url(r'^new-test-case/$', new_test_case, name='new_test_case'),
    url(r'test-case-list-admin/$', test_case_list_admin, name='test-case-list-admin'),
    url(r'edit_test_case/(?P<pk>\d+)/$', edit_test_case, name='edit_test_case'),
    url(r'delete_test_case/(?P<pk>\d+)/$', delete_test_case, name='delete_test_case'),
    url(r'test-cycle-list/$', test_cycle_list, name='test-cycle-list'),
    url(r'test-cycle-detail/(?P<slug>[-\w]+)/$', test_cycle_detail, name='test_cycle_detail'),
    url(r'test-case-detail-in-progress/(?P<slug>[-\w]+)/$', test_case_detail_in_progress, name='test_case_detail_in_progress'),

]
