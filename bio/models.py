## store the information for each member of the club in the database
## this will become a back end EZ system to add/edit/delete for end users.

from django.db import models


class Member(models.Model):

# Store members full name  
    full_name = models.CharField(max_length=70)
    
    
# Position is a string that can be blank, with a max length of 70 characters
    position = models.CharField(
        max_length=70,
        blank=True
    )

# Stores a photo of the member. 
    photo = models.ImageField(
        upload_to="bio_images/",
        blank=True,
        null=True
    )

# If you would like to add additional information you can ... 
    biography = models.TextField(
        blank=True
    )

# this should allow a check mark for if the member is
# an officer of the club.
    is_officer = models.BooleanField(
        default=False
    )

# added to control the order of members. how they look on the html. 
    display_order = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ["display_order", "full_name"]