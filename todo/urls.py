from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task_list"),
    path("task/<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    path("task/new/", views.TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/edit/", views.TaskUpdateView.as_view(), name="task_edit"),
    path("task/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task_delete"),
    re_path(
        r"^task/(?P<pk>\d+)/$", views.TaskDetailView.as_view(), name="task_detail_regex"
    ),
]
