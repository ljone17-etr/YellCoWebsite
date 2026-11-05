# This file is for the bio app views/renders the bio templete 

from django.shortcuts import render

from .models import Member

def home(request):
        context = {
        "officers": Member.objects.filter(is_officer=True),
        "members": Member.objects.filter(is_officer=False),
        }

        return render(request, "bio/bio.html", context)
        
