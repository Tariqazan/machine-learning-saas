from django.urls import path
from .views import *

urlpatterns = [
    path("", Dashboard.as_view(), name="dashboard"),
    path('ref__employeeProfile/', All_Employees, name='employees'),

    path("records/ref_employee/",EmployeeRecords, name = "employee_records"),
    path("records/ref_employee_create/",create_employee, name = "employee_create"),
    path("records/ref_employee_update/<str:pk>",update_employee, name = "employee_update"),
    path("records/ref_employee_delete/<str:pk>",delete_employee, name = "employee_delete"),

    path("ref__SalaryHistory/",employee_salary, name = "salary_history"),
    path("ref__create_payroll_account/",create_employee_payroll, name = "create_payroll_account"),
    path("ref_employee_payroll_update/<str:pk>",update_employee_payroll, name = "employee__payroll_update"),
    path("ref__SalaryManagement/",salary_management, name = "salary_management"),

    path("ref__Employee_Rewards_data/",employee_reward, name = "employee_reward"),
    

    path("clock?In?Out/ref_attendance", EmployeeClockInOut.as_view(), name = 'attendance'),
    path('ref__JobHistory/', JobHistory.as_view(), name='job_history'),
    path('ref__LeaveHistory/', LeaveHistory.as_view(), name='leave_history'),
    path('ref__HolidayCalendar/', Holidays.as_view(), name='holidays_calendar'),
    path('ref__absence/', Absence.as_view(), name='absence'),
    path('ref__overtime/Track/', MonthlyOverTimeTracking.as_view(), name='overtime_track'),
    path('ref__time/Track/', MonthlyTimeTracking.as_view(), name='time_track'),
    path('scheduling/', WorkForceScheduling.as_view(), name='work_force_schedule'),
    # path('em_Performance/', EmployeePerformance.as_view(), name='employee_performance'),
    path('em_Performance/', employee_performance_data, name='employee_performance'),
    path('em_reviews_feedback/', EmployeeReviewsAndFeedback.as_view(), name='employee_reviews_feedback'),
]
