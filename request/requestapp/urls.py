from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("request", views.request_page, name='request_page'),
    path("request/app_attributes", views.app_attibutes, name='app_attributes'),
    path('request/middleware/', views.middleware_view, name='middleware_view'),
    path('request/querydict/', views.querydict_view, name='querydict_view'),
    path('request/is-secure/', views.is_secure, name='is_secure_view'),
    path("response/streaming", views.streaming_response, name='streaming_response'),
    path("response/json", views.json_response, name='json_response'),
    path('home/', views.home, name='home'),
    path('response/',views.response, name='response'),
    path('response/subclasses', views.response_subclasses, name='response_subclasses'),
    path('response/file',views.file_response, name='file_resp'),
    path('response/base/', views.response_base, name='response_base'),
]