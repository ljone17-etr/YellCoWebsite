import django.db

# Create your models here.
#-----------------------
# Monthly meetings, club values, and finance reports are stored in the database. These models represent the data structure for each of these entities.
#-----------------------
class Meeting(django.db.models.Model):
    title = django.db.models.CharField(max_length=200)
    date_time = django.db.models.DateTimeField()
    location = django.db.models.CharField(max_length=255)
    agenda = django.db.models.TextField()

# UPDATE --added an image field for a flyer or image related to the meeting, and a file field for any documents or presentations associated with the meeting.
    meeting_image = django.db.models.ImageField(
        upload_to="meeting_images/",
        blank=True,
        null=True
    )

    meeting_file = django.db.models.FileField(
        upload_to="meeting_files/",
        blank=True,
        null=True
    )

    class Meta:
        ordering = ("date_time",)

    def __str__(self):
        return self.title
    

#-----------------------
# Club values represent the core principles and beliefs of the organization. these will dispaly in order. 
#-----------------------
class ClubValue(django.db.models.Model):
    title = django.db.models.CharField(max_length=100)
    description = django.db.models.TextField()
    icon = django.db.models.CharField(max_length=50, blank=True)
    display_order = django.db.models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("display_order",)

    def __str__(self):
        return self.title

#-----------------------
# Finance reports provide a summary of the club's financial activities, including income and expenses. These reports are generated monthly and stored in the database for reference.
#-----------------------
class FinanceReport(django.db.models.Model):
    title = django.db.models.CharField(max_length=200)
    report_date = django.db.models.DateField()

    total_income = django.db.models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    total_expenses = django.db.models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    summary = django.db.models.TextField()

    class Meta:
        ordering = ("report_date",)

    def __str__(self):
        return self.title