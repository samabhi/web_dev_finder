"""
Admin Backend  for the board app
"""
from django.contrib import admin
from board.models import Event, Musician_Advertisement
#from board.models import Job_Posting
# Register your models here.

admin.site.register(Event)
#admin.site.register(Job_Posting)
admin.site.register(Musician_Advertisement)
