from django.contrib import admin
import datetime

from .models import *




admin.site.register(Rubric)
admin.site.register(SuperRubric)

admin.site.register(SubRubric)
admin.site.register(Bb)
admin.site.register(AdditionalImage)
admin.site.register(Comment)

