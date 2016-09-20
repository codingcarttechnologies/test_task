from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
import datetime
from django.utils import timezone


####################################Students Model####################################
class Students(models.Model):
	user_name=models.CharField(max_length=255, verbose_name='user_name')
	password=models.CharField(max_length=255, verbose_name='password')
	student_id=models.PositiveIntegerField(unique=True, verbose_name='student_id')
	student_name=models.CharField(max_length=255, verbose_name='student_name')
	student_standard=models.CharField(max_length=255, verbose_name='student_standard')
	student_school=models.CharField(max_length=255, verbose_name='student_school')
	student_city=models.CharField(max_length=255, verbose_name='student_city')
	timestamp=models.DateTimeField(default=timezone.localtime(timezone.now()), verbose_name='Created on')


####################################Teachers Model####################################
class Teachers(models.Model):
	username=models.CharField(max_length=255, verbose_name='username')
	pass_word=models.CharField(max_length=255, verbose_name='pass_word')
	teacher_id=models.PositiveIntegerField(unique=True, verbose_name='teacher_id')
	teacher_name=models.CharField(max_length=255, verbose_name='teacher_name')
	teacher_school=models.CharField(max_length=255, verbose_name='teacher_school')
	teacher_city=models.CharField(max_length=255, verbose_name='teacher_city')
	timestamp=models.DateTimeField(default=timezone.localtime(timezone.now()), verbose_name='Created on')

####################################Quiz Model####################################
class Quiz(models.Model):
	quiz_id=models.PositiveIntegerField(unique=True, verbose_name='quiz_id')
	timestamp=models.DateTimeField(default=timezone.localtime(timezone.now()), verbose_name='Created on')


####################################Questions Model####################################
class Questions(models.Model):
	question_id=models.PositiveIntegerField(max_length=255, verbose_name='question_id')
	question=models.CharField(max_length=255, verbose_name='question')
	option_1=models.CharField(max_length=255, verbose_name='option_1')
	option_2=models.CharField(max_length=255, verbose_name='option_2')
	option_3=models.CharField(max_length=255, verbose_name='option_3')
	option_4=models.CharField(max_length=255, verbose_name='option_4')
	answer=models.CharField(max_length=255, verbose_name='answer')
	quiz_id=models.ForeignKey(Quiz, blank=True, null=False)


####################################Certificate Model####################################
class Certificate(models.Model):
	MY_CHOICES = (
        ('a', 'Excellent'),
        ('b', 'Best'),
        ('c', 'Good'),
        ('d', 'Average'),
    )True
	certificate_id=models.PositiveIntegerField(unique=True, verbose_name='certificate_id')
	certificate_type = models.CharField(max_length=1, choices=MY_CHOICES)
	

####################################Student's Record Model####################################
class Students_Record(models.Model):
	record_id=models.PositiveIntegerField(unique=True, verbose_name='record_id')
	question_id=models.ForeignKey(Questions, blank=True, null=False)
	student_id=models.ForeignKey(Students, blank=True, null=False)
	right_question_id=models.CharField(max_length=255, verbose_name='right_answers')
	given_answer=models.CharField(max_length=255, verbose_name='given_answer')
	certificate_id=models.ForeignKey(Certificate, blank=True, null=False)
	score=models.CharField(max_length=255, verbose_name='score')
	timestamp=models.DateTimeField(default=timezone.localtime(timezone.now()), verbose_name='Created on')

