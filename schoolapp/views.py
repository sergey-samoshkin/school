# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.views import generic
from django.http import HttpResponse
import mimetypes, os
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required


from .models import School, SchoolClass


class IndexView(generic.ListView):

    def get_queryset(self):
        return School.objects.all()

    def dispatch(self, request, *args, **kwargs):
        obj_list = self.get_queryset()
        if len(obj_list) == 1:
            return redirect('school:school', pk=obj_list[0].id)
        return super(IndexView, self).dispatch(request, *args, **kwargs)


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
        context['home_works'] = self.get_object().homework_set.order_by('-created_at')[:100]
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('schoolapp.add_homework'):
            return super(SchoolClassView, self).dispatch(request, *args, **kwargs)

        if not self.get_object().login_user or self.get_object().login_user.id != request.user.id:
            return render(request, 'schoolapp/schoolclass_wrong_user.html', { 'schoolclass': self.get_object() })
        return super(SchoolClassView, self).dispatch(request, *args, **kwargs)


@permission_required('schoolapp.add_homework')
def add_hw(request, school_id, class_id):
    obj = get_object_or_404(SchoolClass, pk=class_id, school=school_id)
    if not request.POST['description']:
        return render(request, 'schoolapp/schoolclass_detail.html', {
            'schoolclass': obj, 'error_message': 'Требуется описание'
        })
    if not request.POST['discipline']:
        return render(request, 'schoolapp/schoolclass_detail.html', {
            'schoolclass': obj, 'error_message': 'Требуется указать предмет'
        })
    obj.add_home_work(
        request.POST['description'],
        request.POST['discipline'],
        request.user,
        request.FILES.get('file')
    )
    return redirect('school:schoolclass', obj.school.id, obj.id)


@permission_required('schoolapp.delete_homework')
def remove_hw(request, school_id, class_id, hw_id):
    obj = get_object_or_404(SchoolClass, pk=class_id, school=school_id)
    hw = obj.homework_set.filter(pk=hw_id)
    if len(hw) == 0:
        raise Http404("Homework doesn't exists")
    else:
        hw = hw[0]
    obj.remove_home_work(hw)
    return redirect('school:schoolclass', obj.school.id, obj.id)


def download_hw(request, school_id, class_id, hw_id):
    obj = get_object_or_404(SchoolClass, pk=class_id, school=school_id)

    if not obj.login_user or obj.login_user.id != request.user.id:
        if not request.user.has_perm('schoolapp.add_homework'):
            return render(request, 'schoolapp/schoolclass_wrong_user.html', { 'schoolclass': obj })

    hw = obj.homework_set.filter(pk=hw_id)
    if len(hw) > 0:
        f = hw[0].file
        file_name = os.path.basename(f.name)

        fp = open(f.path, 'rb')
        response = HttpResponse(fp.read())
        fp.close()
        mime_type, encoding = mimetypes.guess_type(file_name)
        if mime_type is None:
            mime_type = 'application/octet-stream'
        response['Content-Type'] = mime_type
        response['Content-Length'] = str(os.stat(f.path).st_size)
        if encoding is not None:
            response['Content-Encoding'] = encoding

        response['Content-Disposition'] = 'attachment; filename=%s' % file_name
        return response
    else:
        raise Http404("Homework doesn't exists")


def login_view(request):
    next = request.GET.get('next', '/')
    return render(request, 'schoolapp/login.html', { 'next': next })


def do_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next'] or request.META.get('HTTP_REFERER', None) or '/'
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(next)
            else:
                return render(request, 'schoolapp/login.html', {
                    'next': next, 'error_message': 'Пользователь заблокирован'
                })
        else:
            return render(request, 'schoolapp/login.html', {
                'next': next, 'error_message': 'Неверный логин или пароль'
            })
    else:
        return render(request, 'schoolapp/login.html', {})


def do_logout_view(request):
    logout(request)
    return redirect('school:index')
