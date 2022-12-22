from django import template
register = template.Library()

# @register.filter(name='CountCounter')
# def CountCounter(Employees):
#     for i in Employees:
#         if i.taskProgressPercentage > 70:
#             count +=1
#     return count
