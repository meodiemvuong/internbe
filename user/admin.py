from django.contrib import admin

# Register your models here.
from company.models import Company, Level, Employee
from user.models import User
# Register your models here.
admin.site.register(Company)
admin.site.register(Level)
admin.site.register(Employee)
admin.site.register(User)