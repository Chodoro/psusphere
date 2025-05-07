from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from studentorg.forms import OrganizationForm, OrgmemberForm, StudentForm, ProgramForm, CollegeForm
from studentorg.models import Organization, Orgmember, Student, College, Program


# Apply login_required decorator to ALL class-based views
@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"


# -------- ORGANIZATION --------
@method_decorator(login_required, name='dispatch')
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = "org_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(college__college_name__icontains=query) |
                Q(description__icontains=query)
            )
        return qs


@method_decorator(login_required, name='dispatch')
class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

    def form_valid(self, form):
        messages.success(self.request, 'Organization created successfully!')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

    def form_valid(self, form):
        messages.success(self.request, f'Organization "{form.instance.name}" updated successfully!')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Organization deleted successfully!')
        return super().delete(request, *args, **kwargs)


# -------- ORGMEMBER --------
@method_decorator(login_required, name='dispatch')
class OrgmemberList(ListView):
    model = Orgmember
    context_object_name = 'orgmember'
    template_name = "orgmem_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(student__firstname__icontains=query) |
                Q(student__lastname__icontains=query) |
                Q(student__middlename__icontains=query)
            )
        return qs


@method_decorator(login_required, name='dispatch')
class OrgmemberCreateView(CreateView):
    model = Orgmember
    form_class = OrgmemberForm
    template_name = 'orgmem_add.html'
    success_url = reverse_lazy('orgmember-list')

    def form_valid(self, form):
        messages.success(self.request, 'Organization member created successfully!')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class OrgmemberUpdateView(UpdateView):
    model = Orgmember
    form_class = OrgmemberForm
    template_name = 'orgmem_edit.html'
    success_url = reverse_lazy('orgmember-list')

    def form_valid(self, form):
        messages.success(self.request, f'Organization member "{form.instance.student.firstname} {form.instance.student.lastname}" updated successfully!')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class OrgmemberDeleteView(DeleteView):
    model = Orgmember
    template_name = 'orgmem_del.html'
    success_url = reverse_lazy('orgmember-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Organization member deleted successfully!')
        return super().delete(request, *args, **kwargs)


# -------- STUDENT --------
@method_decorator(login_required, name='dispatch')
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = "student_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(firstname__icontains=query) |
                Q(lastname__icontains=query) |
                Q(middlename__icontains=query) |
                Q(student_id__icontains=query) |
                Q(program__prog_name__icontains=query)
            )
        return qs


@method_decorator(login_required, name='dispatch')
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')

    def form_valid(self, form):
        messages.success(self.request, 'Student created successfully!')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')

    def form_valid(self, form):
        messages.success(self.request, f'Student "{form.instance.firstname} {form.instance.lastname}" updated successfully!')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Student deleted successfully!')
        return super().delete(request, *args, **kwargs)


# -------- COLLEGE --------
@method_decorator(login_required, name='dispatch')
class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = "college_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(college_name__icontains=query)
        return qs


@method_decorator(login_required, name='dispatch')
class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')

    def form_valid(self, form):
        messages.success(self.request, 'College created successfully!')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')

    def form_valid(self, form):
        college_name = form.instance.college_name
        messages.success(self.request, f'College "{college_name}" updated successfully!')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'College deleted successfully!')
        return super().delete(request, *args, **kwargs)


# -------- PROGRAM --------
@method_decorator(login_required, name='dispatch')
class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = "program_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(prog_name__icontains=query) |
                Q(college__college_name__icontains=query)
            )
        return qs


@method_decorator(login_required, name='dispatch')
class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')

    def form_valid(self, form):
        messages.success(self.request, 'Program created successfully!')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program-list')

    def form_valid(self, form):
        messages.success(self.request, f'Program "{form.instance.prog_name}" updated successfully!')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Program deleted successfully!')
        return super().delete(request, *args, **kwargs)
