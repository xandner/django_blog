from django.urls import path
from .views import home,detail
app_name="first_app"
urlpatterns = [
    path("", home ,name="test_app"),
    path("article/<slug:slug>", detail ,name="detail"),
]
