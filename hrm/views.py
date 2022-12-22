from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required


from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger

from .models import *
from .forms import *




# Create your views here.

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class Dashboard(TemplateView):
    template_name = "hrm/dashboard.html"


class EmployeeClockInOut(LoginRequiredMixin,TemplateView):
    template_name = 'hrm/clock/ClockInOut.html'


class JobHistory(LoginRequiredMixin, TemplateView):
    template_name = 'hrm/Job/job_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to show dummy contents on template(will be removed later on a real integration)
        context['loop'] = range(0, 15)
        return context

class SalaryHistory(LoginRequiredMixin, TemplateView):
    template_name = 'hrm/Salary/salary_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to show dummy contents on template(will be removed later on a real integration)
        context['loop'] = range(0, 15)
        return context

class LeaveHistory(LoginRequiredMixin, TemplateView):
    template_name = 'hrm/Leave/leave_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to show dummy contents on template(will be removed later on a real integration)
        context['loop'] = range(0, 15)
        return context

class Employees(LoginRequiredMixin, TemplateView):
    template_name = 'hrm/Employee/employee.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to show dummy contents on template(will be removed later on a real integration)
        context['loop'] = range(0, 15)
        return context

class Holidays(LoginRequiredMixin, TemplateView):
    template_name = 'hrm/Holidays/holidays.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to show dummy contents on template(will be removed later on a real integration)
        context['loop'] = range(0, 15)
        return context

class Absence(LoginRequiredMixin, TemplateView):
    template_name = 'hrm/Absence/absence.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to show dummy contents on template(will be removed later on a real integration)
        context['loop'] = range(0, 15)
        return context

class MonthlyOverTimeTracking(LoginRequiredMixin, TemplateView):
    template_name = 'hrm/Clock/overtime.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to show dummy contents on template(will be removed later on a real integration)
        context['loop'] = range(0, 15)
        return context


class MonthlyTimeTracking(LoginRequiredMixin, TemplateView):
    template_name = 'hrm/Clock/time.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to show dummy contents on template(will be removed later on a real integration)
        context['loop'] = range(0, 15)
        return context


class WorkForceScheduling(LoginRequiredMixin, TemplateView):
    template_name = 'hrm/Schedule/work_schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to show dummy contents on template(will be removed later on a real integration)
        context['loop'] = range(0, 15)
        return context

class EmployeePerformance(LoginRequiredMixin, TemplateView):
    template_name = 'hrm/Employee/employee_performance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to show dummy contents on template(will be removed later on a real integration)
        context['loop'] = range(0, 15)
        return context


# reviews and feedbacks for agains employees
class EmployeeReviewsAndFeedback(LoginRequiredMixin, TemplateView):
    template_name = 'hrm/Employee/employees_review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to show dummy contents on template(will be removed later on a real integration)
        context['loop'] = range(0, 15)
        return context

@login_required
def EmployeeRecords(request):

    all_users = Employee.objects.all()
    Total_Users = all_users.count()
    Engineer = all_users.filter(designation='Engineer').count()
    QC_Checker = all_users.filter(designation='Quality Controller').count()
    Other_Employees = Total_Users - Engineer - QC_Checker


    # pagintaion
    user_list = Employee.objects.all()[::-1]
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    try:
        Employees = paginator.page(page)
    except PageNotAnInteger:
        Employees = paginator.page(1)
    except EmptyPage:
        Employees = paginator.page(paginator.num_pages)

    dict = {'Employees':Employees,
            'QC_Checker':QC_Checker,
            'Engineer':Engineer,
            'Total_Users':Total_Users,
            'Other_Employees':Other_Employees}

    return render(request,'hrm/Employee/employee_records.html',context=dict)

@login_required
def All_Employees(request):

    user_list = Employee.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 4)
    try:
        Employees = paginator.page(page)
    except PageNotAnInteger:
        Employees = paginator.page(1)
    except EmptyPage:
        Employees = paginator.page(paginator.num_pages)

    return render(request,'hrm/Employee/employee.html',context={'Employees':Employees})

@login_required
def create_employee(request):

    form = EmployeeCreationForm()

    if request.method == "POST":
        form = EmployeeCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_records')

    dict = {'form':form}
    return render(request,'hrm/Employee/create_employee.html',context=dict)

@login_required
def update_employee(request,pk):
    employee_data = Employee.objects.get(id=pk)
    form = EmployeeCreationForm(instance = employee_data)

    if request.method == "POST":
        form = EmployeeCreationForm(request.POST,request.FILES,instance=employee_data)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            return redirect('employee_records')

    dict = {'form':form}
    return render(request,'hrm/Employee/update_employee.html',context=dict)

@login_required
def delete_employee(request,pk):
    employee_data = Employee.objects.get(id=pk)

    if request.method == "POST":
        employee_data.delete()
        return redirect('employee_records')
    context = {'item':employee_data}
    return render(request, 'hrm/Employee/delete_employee.html', context)

@login_required
def employee_salary(request):

    user_list = Employee_Payroll.objects.all()
    All_Payrolls = user_list.count()
    Paid_Employees = user_list.filter(status = 'Paid').count()
    Employees_Probation = user_list.filter(job_type = 'Probation').count()
    Employee_On_Overtime = user_list.exclude(overtime = None ).count()

    #pagination
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    try:
        Employees = paginator.page(page)
    except PageNotAnInteger:
        Employees = paginator.page(1)
    except EmptyPage:
        Employees = paginator.page(paginator.num_pages)

    dict={'Employees':Employees,
          'Paid_Employees':Paid_Employees,
          'All_Payrolls':All_Payrolls,
          'Employees_Probation':Employees_Probation,
          'Employee_On_Overtime':Employee_On_Overtime,}

    return render(request,'hrm/salary/salary_history.html',context=dict)

@login_required
def create_employee_payroll(request):

    form = PayrollCreationForm()

    if request.method == "POST":
        form = PayrollCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('salary_history')

    dict = {'form':form}
    return render(request,'hrm/Employee/create_employee.html',context=dict)

@login_required
def update_employee_payroll(request,pk):
    employee_data = Employee_Payroll.objects.get(id=pk)
    form = PayrollUpdateForm(instance = employee_data)

    if request.method == "POST":
        form = PayrollUpdateForm(request.POST,request.FILES,instance=employee_data)

        if form.is_valid():
            form.save()
            return redirect('salary_history')

    dict = {'form':form}
    return render(request,'hrm/salary/update_payroll.html',context=dict)


@login_required
def employee_performance_data(request):
    user_list = Employee.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    try:
        Employees = paginator.page(page)
    except PageNotAnInteger:
        Employees = paginator.page(1)
    except EmptyPage:
        Employees = paginator.page(paginator.num_pages)

    values = Employee.objects.all().values_list('id',flat = True)
    tasks = Task.objects.filter(employee_id__in=list(set(values)), task_progress = True)
    print(tasks)
    dict = {
        'Employees':Employees,
        'tasks': tasks,
    }

    return render(request,'hrm/Employee/employee_performance.html',context=dict)

@login_required
def salary_management(request):

    user_list = Employee_Payroll.objects.all()
    Paid_Employees = user_list.filter(status = 'Paid').count()
    Unpaid_Employees = user_list.exclude(status = 'Paid').count()


    #pagination
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    try:
        Employees = paginator.page(page)
    except PageNotAnInteger:
        Employees = paginator.page(1)
    except EmptyPage:
        Employees = paginator.page(paginator.num_pages)

    dict={'Employees':Employees,
          'Paid_Employees':Paid_Employees,
          'Unpaid_Employees':Unpaid_Employees,

          }

    return render(request,'hrm/salary/salary_management.html',context=dict)

@login_required
def employee_reward(request):


    user_list = Employee.objects.filter( percent__gt = 70)

    # employees = Employee.objects.all()

    new_good_tasker = user_list .count()


    # Paid_Employees = user_list.filter(status = 'Paid').count()
    # Unpaid_Employees = user_list.exclude(status = 'Paid').count()


    #pagination
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    try:
        Employees = paginator.page(page)
    except PageNotAnInteger:
        Employees = paginator.page(1)
    except EmptyPage:
        Employees = paginator.page(paginator.num_pages)

    dict={'Employees':Employees,
          # 'Paid_Employees':Paid_Employees,
          # 'Unpaid_Employees':Unpaid_Employees,
          'great_employees_list':new_good_tasker,
          }

    return render(request,'hrm/salary/rewards.html',context=dict)
