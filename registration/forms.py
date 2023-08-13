from django import forms
from .models import Participant

GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female")
)

DESIGNATION_CHOICES = (
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

class ParticipantRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    middle_name = forms.CharField(label='Middle Name', required=False)
    surname = forms.CharField(label='Surname')
    date_of_birth = forms.DateField(label='Date of Birth')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES)
    preferred_name = forms.CharField(label='Preferred Name', required=False)
    address = forms.CharField(label='Address')
    city = forms.CharField(label='City')
    yasana = forms.CharField(label='Yasana')
    tikina = forms.CharField(label='Tikina')
    koro = forms.CharField(label='Koro')
    country_of_birth = forms.CharField(label='Country of Birth')
    phone_number = forms.CharField(label='Phone Number')
    mobile_number = forms.CharField(label='Mobile Number')
    email = forms.EmailField(label='Email')
    bc_number = forms.CharField(label='BC Number')
    passport_number = forms.CharField(label='Passport Number')
    driverslicense_number = forms.CharField(label='Driver\'s License Number')
    evr_number = forms.CharField(label='EVR Number')
    designation = forms.ChoiceField(label='Designation', choices=DESIGNATION_CHOICES)
    club_name = forms.CharField(label='Club Name', required=False)
    age = forms.IntegerField(label='Age', required=False)
    grade = forms.CharField(label='Grade', required=False)
    regional_league_zone = forms.CharField(label='Regional League Zone', required=False)
    state = forms.CharField(label='State', required=False)
    clearance = forms.CharField(label='Clearance', required=False)

    class Meta:
        model = Participant
        fields = ('first_name', 'middle_name', 'surname', 'date_of_birth', 'gender', 'preferred_name', 'address',
                  'city', 'yasana', 'tikina', 'koro', 'country_of_birth', 'phone_number', 'mobile_number', 'email',
                  'bc_number', 'passport_number', 'driverslicense_number', 'evr_number', 'designation', 'club_name',
                  'age', 'grade', 'regional_league_zone', 'state', 'clearance')
