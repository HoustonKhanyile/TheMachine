from django.contrib import admin
from .models import Appear, Bookings, Performance, Profile, Publicity


admin.site.register(Appear)
admin.site.register(Performance)
admin.site.register(Publicity)
admin.site.register(Profile)
admin.site.register(Bookings)
