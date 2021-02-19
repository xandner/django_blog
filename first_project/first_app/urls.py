from django.urls import path
from .views import home,detail,category
app_name="first_app"
urlpatterns = [
    path("", home ,name="test_app"),
    path("page/<int:page>", home ,name="test_app"),
    path("article/<slug:slug>", detail ,name="detail"),
    path("category/<slug:slug>", category ,name="category"),
    path("category/<slug:slug>/page/<int:page>", category ,name="category"),
]
