# This file is for the bio app views.

from django.template import context
from django.views.generic import TemplateView
from .models import Member

def home(request):
        template_name= "bio/bio.html"

        def get_context_data(self, **kwargs):

                context= super().get_context_data(**kwargs)
                context["officers"] = Member.objects.filter(is_officer=True)
                context["members"] = Member.objects.filter(is_officer=False)

        return context