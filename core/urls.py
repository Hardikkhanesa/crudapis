
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path("create/", core_views.CrudView.as_view(), name="create"),
    path("update/", core_views.UpdateView.as_view(), name="update"),
    path("delete/", core_views.DeleteView.as_view(), name="delete"),
    path("read/", core_views.GetCrudView.as_view(), name="read"),
]