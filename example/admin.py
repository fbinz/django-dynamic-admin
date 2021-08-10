from django.contrib import admin

from example.models import Customer, District, Employee
from example.forms import CustomerForm


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    form = CustomerForm
    fields = ("name", "district", "employee", "valid")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
