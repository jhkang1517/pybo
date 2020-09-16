from django.contrib import admin

# ----- edit -----
from .models import Question
# -

# Register your models here.
# ----- edit -----
# admin.site.register(Question)
# -

# ----- edit -----
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)


