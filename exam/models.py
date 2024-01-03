from django.db import models
from django.utils.translation import gettext_lazy as _
from student.models import Student
class Course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   def __str__(self):
        return self.course_name

class Question(models.Model):
    class Subject(models.TextChoices):
        SUBJECT_ONE = 'Subject_One', _('SUBJECT_ONE')
        SUBJECT_TWO = 'Subject_Two', _('SUBJECT_TWO')
        SUBJECT_THREE = 'Subject_Three', _('SUBJECT_THREE')
        SUBJECT_FOUR = 'Subject_Four', _('SUBJECT_FOUR')
        SUBJECT_FIVE = 'Subject_Five', _('SUBJECT_FIVE')
        SUBJECT_SIX = 'Subject_Six', _('SUBJECT_SIX')
        SUBJECT_SEVEN = 'Subject_Seven', _('SUBJECT_SEVEN')
        SUBJECT_EIGHT = 'Subject_Eight', _('SUBJECT_EIGHT')
        SUBJECT_NINE = 'Subject_Nine', _('SUBJECT_NINE')
        SUBJECT_TEN = 'Subject_Ten', _('SUBJECT_TEN')   
        SUBJECT_ELEVEN = 'Subject_Eleven', _('SUBJECT_ELEVEN') 
      
    subject =  models.CharField(max_length=15, choices=Subject.choices, null=True, blank=True)  
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    question_number = models.IntegerField(null=True, blank=True)

    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
 

class SelectedAnswer(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='selectedanswer_set')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=200)  # You can change the field name as needed

    def __str__(self):
        return f"Result: {self.result}, Question: {self.question}, Selected Option: {self.selected_option}"