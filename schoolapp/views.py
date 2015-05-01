# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

from .models import School, SchoolClass


def index(request):
    obj_list = School.objects.all()
    if len(obj_list) == 1:
        return redirect('school:school', school_id=obj_list[0].id)
    return render(request, 'school/list.html', RequestContext(request, {
        'school_list': obj_list
    }))


def classes(request, school_id):
    obj = get_object_or_404(School, pk=school_id)
    class_list = obj.schoolclass_set.all()
    return render(request, 'school/classes.html', RequestContext(request, {
        'school': obj, 'class_list': class_list
    }))


def school(request, school_id):
    obj = get_object_or_404(School, pk=school_id)
    return render(request, 'school/index.html', { 'school': obj })


def schoolclass(request, school_id, class_id):
    obj = get_object_or_404(SchoolClass, pk=class_id, school=school_id)
    home_works = obj.homework_set.order_by('-created_at')[:20]
    return render(request, 'school/class.html', RequestContext(request, {
        'schoolclass': obj, 'school': obj.school, 'home_works': home_works
    }))


def add_hw(request, school_id, class_id):
    obj = get_object_or_404(SchoolClass, pk=class_id, school=school_id)
    if not request.POST['description']:
        return render(request, 'school/class.html', {
            'schoolclass': obj, 'school': obj.school, 'error_message': 'Требуется описание'
        })
    obj.add_home_work(request.POST['description'])
    return redirect('school:schoolclass', obj.school.id, obj.id)
