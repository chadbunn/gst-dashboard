from django.contrib.gis import admin
from models import Incident

class IncidentAdmin(admin.GeoModelAdmin):
    list_display = ('name', 'category', 'jrsdtn', 'time')

admin.site.register(Incident, IncidentAdmin)
