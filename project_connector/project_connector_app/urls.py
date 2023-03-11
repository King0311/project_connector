from django.urls import path, include
from . import views


urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("homepage",views.homepage,name="homepage"),
    path("registor",views.registor,name="registor"),
    path("login",views.login,name="login"),
    path("guide",views.guide,name="guide"),
    path("guide_assign",views.guide_assign,name="guide_assign"),
    path("guide_updates",views.guide_updates,name="guide_updates"),
    path("student_chat",views.student_chat,name="student_chat"),
    path("student_work",views.student_work,name="student_work"),
    path("student_updates",views.student_updates,name="student_updates"),
]
