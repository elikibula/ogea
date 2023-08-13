from django.shortcuts import render
from .forms import ParticipantRegistrationForm
from .models import Participant
from django.views.generic.edit import CreateView

def register_participant(request):
    if request.method == 'POST':
        form = ParticipantRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
    else:
        form = ParticipantRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def dashboard(request):
    total_count = Participant.objects.count()
    coach_grade_1_count = Participant.objects.filter(designation='coach_grade_1').count()
    coach_grade_2_count = Participant.objects.filter(designation='coach_grade_2').count()
    coach_grade_a_count = Participant.objects.filter(designation='coach_grade_a').count()
    sports_trainer_grade_1_count = Participant.objects.filter(designation='sports_trainer_grade_1').count()
    sports_trainer_grade_2_count = Participant.objects.filter(designation='sports_trainer_grade_2').count()
    sports_trainer_grade_3_count = Participant.objects.filter(designation='sports_trainer_grade_3').count()
    sports_trainer_grade_4_count = Participant.objects.filter(designation='sports_trainer_grade_4').count()
    team_manager_grade_a_count = Participant.objects.filter(designation='team_manager_grade_a').count()
    team_manager_grade_b_count = Participant.objects.filter(designation='team_manager_grade_b').count()
    team_manager_grade_c_count = Participant.objects.filter(designation='team_manager_grade_c').count()
    volunteer_count = Participant.objects.filter(designation='volunteer').count()
    match_official_count = Participant.objects.filter(designation='match_official').count()
    team_official_count = Participant.objects.filter(designation='team_official').count()
    player_count = Participant.objects.filter(designation='player').count()

        # Add more count queries for other designations
    
    context = {
        'total_count': total_count,
        'coach_grade_1_count': coach_grade_1_count,
        'coach_grade_2_count': coach_grade_2_count,
        'coach_grade_a_count': coach_grade_a_count,
        'team_manager_grade_a_count': team_manager_grade_a_count,
        'team_manager_grade_b_count': team_manager_grade_b_count,
        'team_manager_grade_c_count':team_manager_grade_c_count,
        'player_count': player_count,
        'team_official_count': team_official_count,
        'match_official_count': match_official_count,
        'volunteer_count': volunteer_count,        
        'sports_trainer_grade_1_count': sports_trainer_grade_1_count,
        'sports_trainer_grade_2_count': sports_trainer_grade_2_count,
        'sports_trainer_grade_3_count': sports_trainer_grade_3_count,
        'sports_trainer_grade_4_count': sports_trainer_grade_4_count,
    


        # Add more count numbers to the context
    }
    
    return render(request, 'registration/dashboard.html', context)

class ParticipantRegistrationView(CreateView):
    model = Participant
    form_class = ParticipantRegistrationForm
    template_name = 'register.html'
    success_url = '/registration/success/'

