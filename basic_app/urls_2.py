from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r"^$", views.SchoolListView.as_view(), name="list"),
    url(r"^create_student/", views.StudentCreateView.as_view(), name="create_student"),
    url(r"^update_student/(?P<pk>\d+)$", views.StudentUpdateView.as_view(), name="update_student"),
    url(r"^delete_student/(?P<pk>\d+)$", views.StudentDeleteView.as_view(), name="delete_student"),
]