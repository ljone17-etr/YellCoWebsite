# This file is for the bio app views.

from django.views.generic import TemplateView
from .models import Member


class HomepageView(TemplateView):
        template_name = "bio/bio.html"

        # This creates the information that will be sent
        # from the database to bio.html.
        def get_context_data(self, **kwargs):

                
                context = super().get_context_data(**kwargs)
                context["officers"] = Member.objects.filter(is_officer=True)
                context["members"] = Member.objects.filter(is_officer=False)

                return context