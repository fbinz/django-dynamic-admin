from django.urls import path


from dynamic_select.widgets import DynamicSelect

urlpatterns = [
    path('<app_label>/<model_name>/<field_name>/', DynamicSelect.render_field),
]
