from django.db import models

# Create your models here.
class Employee(models.Model):

    DESIGNATION_CHOICES= [
    ('','SELECT OPTIONS'),
    ('Engineer', 'Engineer'),
    ('Manager', 'Manager'),
    ('Quality Controller', 'Quality Controller'),
    ('Consultant', 'Consultant'),
    ]

    name = models.CharField(max_length=128,null=True)
    contact = models.CharField(max_length=128,null=True)
    email = models.EmailField(null=True)
    employee_id = models.CharField(max_length=128,null=True,unique=True)
    designation = models.CharField(choices=DESIGNATION_CHOICES,max_length=128,null=True)
    joining_date = models.DateTimeField(null=True)
    city = models.CharField(max_length=128,null=True)
    branch = models.CharField(max_length=128,null=True)
    salary = models.IntegerField(null=True)
    profile_pic = models.ImageField(upload_to='profile_pic',null=True,default='default.jpg')
    percent = models.IntegerField(null=True)
    def __str__(self):
        return self.name

    @property
    def taskProgressCount(self):

        tasks = Task.objects.filter(employee_id=self.id,task_progress=True).count()
        return tasks

    @property
    def taskProgressPercentage(self):
        tasks_done = Task.objects.filter(employee_id=self.id,task_progress=True).count()
        tasks_total = Task.objects.filter(employee_id=self.id).count()
        if tasks_total:
            percentage = int(tasks_done/tasks_total*100)
            Employee.objects.filter(id=self.id).update(percent=percentage)
            return percentage


class Employee_Payroll(models.Model):
    STATUS_CHOICES= [
    ('Paid', 'Paid'),
    ('Due', 'Due'),
    ]

    JOB_STATUS_CHOICES= [
    ('Running', 'Running'),
    ('Terminated', 'Terminated'),
    ('Retired', 'Retired'),
    ]

    JOB_TYPE_CHOICES= [
    ('Part Time', 'Part Time'),
    ('Permanent', 'Permanent'),
    ('Probation', 'Probation'),
    ]

    employee = models.ForeignKey(Employee, on_delete= models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES,max_length=12,null=True)
    job_status = models.CharField(choices=JOB_STATUS_CHOICES,max_length=12,null=True)
    job_type = models.CharField(choices=JOB_TYPE_CHOICES,max_length=12,null=True)
    salary_to_be_paid = models.CharField(max_length=128,null=True)
    overtime_amount = models.CharField(max_length=128,null=True)
    overtime = models.IntegerField(null=True,blank=True)
    salary_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.employee.name

class Task(models.Model):
    employee = models.ForeignKey(Employee, on_delete= models.CASCADE,null=True)
    task = models.CharField(max_length=128,null=True)
    task_progress = models.BooleanField(default=True)

    def __str__(self):
        return self.employee.name
