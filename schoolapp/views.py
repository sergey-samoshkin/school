# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from .models import School, SchoolClass


class IndexView(generic.ListView):
    def get_queryset(self):
        return School.objects.all()


#def index(request):
#    obj_list = School.objects.all()
#     if len(obj_list) == 1:
#         return redirect('school:school', school_id=obj_list[0].id)
#     return render(request, 'school/list.html', RequestContext(request, {
#         'school_list': obj_list
#     }))


class ClassList(generic.ListView):
    def get_queryset(self):
        obj = get_object_or_404(School, pk=self.kwargs['pk'])
        return obj.schoolclass_set.all()


class SchoolView(generic.DetailView):
    model = School


class SchoolClassView(generic.DetailView):
    model = SchoolClass

    def get_queryset(self):
        qs = super(SchoolClassView, self).get_queryset()
        return qs.filter(school=self.kwargs['school_id'])

    def get_context_data(self, **kwargs):
        context = super(SchoolClassView, self).get_context_data(**kwargs)
        context['home_works'] = self.get_object().homework_set.order_by('-created_at')[:20]
        return context


def add_hw(request, school_id, class_id):
    obj = get_object_or_404(SchoolClass, pk=class_id, school=school_id)
    if not request.POST['description']:
        return render(request, 'school/class.html', {
            'schoolclass': obj, 'school': obj.school, 'error_message': 'Требуется описание'
        })
    obj.add_home_work(request.POST['description'])
    return redirect('school:schoolclass', obj.school.id, obj.id)

