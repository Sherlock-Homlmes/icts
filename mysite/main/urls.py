from django.urls import path

from . import views

from .class_base_view import AboutView

urlpatterns = [
    path("v1/" , views.index , name="index"),
    path("home/" , views.home , name="home"),
    path("form-test/" , views.form_test , name="form_test"),
    path("about/" , AboutView.as_view()),
    path('cook/',views.cook, name="cookie"),
    path('test-static',views.test_static,name="test_static")
]