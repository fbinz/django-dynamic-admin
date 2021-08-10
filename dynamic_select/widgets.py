from django.apps import apps
from django.contrib import admin
from django.forms import widgets
from django.http import HttpResponse


class DynamicSelect(widgets.Select):
    template_name = "example/dynamic_select.html"

    def __init__(self, *args, app_label, model_name, field_name, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_label = app_label
        self.model_name = model_name
        self.field_name = field_name

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["app_label"] = self.app_label
        context["model_name"] = self.model_name
        context["field_name"] = self.field_name
        return context

    @staticmethod
    def render_field(request, app_label, model_name, field_name):
        model = apps.get_model(app_label, model_name)

        # instantiate model form from request data and get field
        ModelForm = admin.site._registry[model].form
        form = ModelForm(request.POST)

        bound_field = form[field_name]

        # save custom queryset in field
        method_name =  f"get_{field_name}_queryset"
        if hasattr(form, method_name):
            method = getattr(form, method_name)
            bound_field.field.queryset = method()


        # render field and return html
        html = bound_field.as_widget()
        return HttpResponse(html, status=200)

    class Media:
        js = ('https://unpkg.com/htmx.org@1.5.0',)
