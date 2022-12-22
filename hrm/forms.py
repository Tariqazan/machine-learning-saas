from django.forms import ModelForm
from .models import *

class EmployeeCreationForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class PayrollCreationForm(ModelForm):
    class Meta:
        model = Employee_Payroll
        fields = '__all__'

class PayrollUpdateForm(ModelForm):
    class Meta:
        model = Employee_Payroll
        fields = ['status','job_status']
