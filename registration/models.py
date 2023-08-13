from django.db import models
from datetime import date

designation_Choices = (
    ("coach_grade_1", "Coach Grade 1"),
    ("coach_grade_2", "Coach Grade 2"),
    ("coach_grade_a", "Coach Grade A"),
    ("sports_trainer_grade_1","Sports Trainer 1"),
    ("sports_trainer_grade_2","Sports Trainer 2"),
    ("sports_trainer_grade_3","Sports Trainer 3"),
    ("sports_trainer_grade_4","Sports Trainer 4"),
    ("team_manager_grade_a","Team Manager Grade A"),
    ("team_manager_grade_b","Team Manager Grade B"),
    ("team_manager_grade_c","Team Manager Grade C"),
    ("volunteer", "Volunteer"),
    ("match_official","Match Official"),
    ("team_official","Team Official"),
    ("player", "Player"),
    ("others","Others"),
)

gender_Choices = (
    ("male", "Male"),
    ("female", "Female")
)
    

class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=gender_Choices, max_length=50, blank=True)
    preferred_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    yasana = models.CharField(max_length=255)
    tikina = models.CharField(max_length=255)
    koro = models.CharField(max_length=255)
    country_of_birth = models.CharField(max_length=255)  # Add the appropriate max_length
    phone_number = models.CharField(max_length=15)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    bc_number = models.BigIntegerField()
    passport_number = models.BigIntegerField()
    driverslicense_number = models.BigIntegerField()
    evr_number = models.BigIntegerField()
    designation = models.CharField(choices=designation_Choices, max_length=50, blank=True, help_text='Please select Designation')
    club_name = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    regional_league_zone = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    clearance = models.CharField(max_length=255, blank=True, null=True)

    # Calculation of age from date_of_birth field
    def save(self, *args, **kwargs):
        today = date.today()
        age = today.year - self.date_of_birth.year

        # Adjust age if the birthday hasn't occurred yet this year
        if (
            self.date_of_birth.month > today.month
            or (self.date_of_birth.month == today.month and self.date_of_birth.day > today.day)
        ):
            age -= 1

        self.age = age
        super().save(*args, **kwargs)
