from django import forms

from dynamic_select.forms import DynamicFormMixin
from example.models import Customer, Employee, District


class CustomerForm(DynamicFormMixin, forms.ModelForm):
    valid = forms.BooleanField()
    dynamic_fields = ("employee",)

    class Meta:
        model = Customer
        fields = "__all__"

    def get_employee_queryset(self):
        return Employee.objects.filter(district_id=self["district"].value() or None)

    def get_district_queryset(self):
        return District.objects.all()
