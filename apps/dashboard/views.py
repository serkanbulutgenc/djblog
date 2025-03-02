from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class BaseDashboardView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['path_name'] = [path for path in self.request.path_info.split(sep='/') if path]
        return context
    
class DashboardView(BaseDashboardView):
    template_name = 'dashboard/index.html'

class ProfileView(BaseDashboardView):
    template_name = 'dashboard/profile.html'
    
    