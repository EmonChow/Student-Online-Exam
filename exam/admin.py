from django.contrib import admin

from exam.models import Question, Result

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Question._meta.fields]
 
 
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Result._meta.fields] 
 
 
 