from django.contrib import admin

from inference_engine.models import Patient

# also have an admin class
admin.site.register(Patient)