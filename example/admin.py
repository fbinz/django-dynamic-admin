from django.contrib import admin

from example.models import Customer, District, Employee
from dynamic_select.admin import DynamicModelAdminMixin


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(DynamicModelAdminMixin, admin.ModelAdmin):
    fields = ("name", "district", "employee")
    dynamic_fields = ("name", "employee",)

    def get_dynamic_employee_field(self, data):
        queryset = Employee.objects.filter(district=data.get("district"))
        value = data.get("employee")

        if value not in queryset:
            value = queryset.first()

        return queryset, value

    def get_dynamic_name_field(self, data):
        if name := data.get("name"):
            return None, name
        else:
            return None, data.get("district")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
