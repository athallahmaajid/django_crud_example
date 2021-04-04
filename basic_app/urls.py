from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r"^$", views.SchoolListView.as_view(), name="list"),
    url(r"^(?P<pk>\d+)$", views.SchoolDetailView.as_view(), name="detail"),
    url(r"^create_school/", views.SchoolCreateView.as_view(), name="create_school"),
    url(r"^update_school/(?P<pk>\d+)$", views.SchoolUpdateView.as_view(), name="update_school"),
    url(r"^delete_school/(?P<pk>\d+)$", views.SchoolDeleteView.as_view(), name="delete_school"),
]
