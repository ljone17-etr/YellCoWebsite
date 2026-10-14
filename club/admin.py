from django.contrib import admin

from .models import ClubValue, FinanceReport, Meeting


admin.site.register(Meeting)
admin.site.register(ClubValue)
admin.site.register(FinanceReport)