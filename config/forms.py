from django.forms.renderers import TemplatesSetting


class CustomFormRenderer(TemplatesSetting):
    form_template_name = 'form/template.html'
    field_template_name = 'form/field.html'
