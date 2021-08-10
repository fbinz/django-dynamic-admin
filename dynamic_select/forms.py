from django.core.exceptions import ImproperlyConfigured

from dynamic_select.widgets import DynamicSelect


class DynamicFormMixin:
    dynamic_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.dynamic_fields:

            meta = self.instance._meta
            self.fields[field_name].widget.widget = DynamicSelect(
                app_label=meta.app_label,
                model_name=meta.model_name,
                field_name=field_name,
            )

            method_name = f"get_{field_name}_queryset"
            try:
                method = getattr(self, method_name)
                field = self[field_name].field
                field.queryset = method()
            except AttributeError:
                raise ImproperlyConfigured(f"Missing method {method_name} on form {self.__class__}")