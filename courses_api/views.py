from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Provider, Course


def home(request):
    providers_list = Provider.objects.all()
    paginator = Paginator(providers_list, 10)

    page = request.GET.get('page')
    try:
        providers = paginator.page(page)
    except PageNotAnInteger:
        providers = paginator.page(1)
    except EmptyPage:
        providers = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'providers': providers})


def provider_detail(request, provider_id):
    provider = get_object_or_404(Provider, pk=provider_id)
    return render(request, 'provider_detail.html', {'provider': provider})


def course_list(request):
    courses_list = Course.objects.all()
    paginator = Paginator(courses_list, 10)

    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    return render(request, 'course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_detail.html', {'course': course})
