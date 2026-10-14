from django.shortcuts import render
from django.utils import timezone

from .models import ClubValue, FinanceReport, Meeting

#--------------------
# Home view  - this  shows upcoming meeting and club values
#--------------------

def home(request):
    upcoming_meetings = Meeting.objects.filter(
        date_time__gte=timezone.now()
    )

    club_values = ClubValue.objects.all()

    context = {
    "meetings": upcoming_meetings,
    "values": club_values,
}

    return render(
        request,
        "club/home.html",
        context
    )

#---------------
# finance view - this shows finance reports
#---------------

def finance(request):
    reports = FinanceReport.objects.all()

    context = {
        "reports": reports,
    }

    return render(
        request,
        "club/finance.html",
        context
    )

#---------------
# old business view - this shows all old meetings placed in the past.
#---------------
# UPDATED - now both meetings AND Finance reports are shown on old business page. automation by date. 

def old_business(request):
    past_meetings = Meeting.objects.filter(
        date_time__lt=timezone.now()
    )

    finance_reports = FinanceReport.objects.all()

    context = {
        "past_meetings": past_meetings,
        "finance_reports": finance_reports,
    }

    return render(
        request,
        "club/old_business.html",
        context
    )
