from django.urls import path

from .views import home, provider_detail, course_detail, course_list

urlpatterns = [
    path('', home, name='home'),
    path('provider/<int:provider_id>/', provider_detail, name='provider_detail'),
    path('courses/', course_list, name='course_list'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
]
