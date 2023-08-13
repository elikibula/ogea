from django.contrib import admin
from .models import Participant

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'date_of_birth', 'gender', 'email')
    list_filter = ('gender', 'designation')
    search_fields = ('first_name', 'surname', 'email')
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'middle_name', 'surname', 'date_of_birth', 'gender')
        }),
        ('Contact Information', {
            'fields': ('address', 'city', 'yasana', 'tikina', 'koro', 'country_of_birth', 'phone_number', 'mobile_number', 'email')
        }),
        ('Identification Numbers', {
            'fields': ('bc_number', 'passport_number', 'driverslicense_number', 'evr_number')
        }),
        ('Additional Information', {
            'fields': ('preferred_name', 'designation', 'club_name', 'age', 'grade', 'regional_league_zone', 'state', 'clearance')
        })
    )

admin.site.register(Participant, ParticipantAdmin)
