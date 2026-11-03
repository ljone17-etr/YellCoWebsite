# I will connect my members model here !
# this will allow the end user to work the backend and imput new members and change officers
# simply and easy 

from django.contrib import admin
from django.contrib import admin

# Import the Member model from this app's models.py
from .models import Member


# Register the Member model with Django Admin
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

    # These are the columns we will see when looking
    # at the list of members in Django Admin.
    list_display = (
        "full_name",
        "position",
        "is_officer",
        "display_order",
    )

    # Adds a filter on the side of the Admin page.
    # This will let us quickly view officers or regular members.
    list_filter = ("is_officer",)

    # Adds a search box so we can find someone
    # by their name or position.
    search_fields = ("full_name", "position")

    # Controls the default order of members in Admin.
    ordering = ("display_order", "full_name")