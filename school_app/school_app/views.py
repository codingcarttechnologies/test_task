########## import modules ########################
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import check_password
from django.template import Context
from models import Students,Teachers,Quiz,Questions,Certificates,Students_Record
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
import datetime
import time


########################Views############################

####################  Student Login Function ############################
def Login(request):
	try:
		if (request.method=='POST'):
			username=request.POST['username']
			password=request.POST['password']
			user=Students.objects.filter(username=username)
			for us in user:
				user_password=us.password
				check=check_password(password,user_password)
				if check==True:
					return render(request, 'student_dashboard.html', {}})
				else:
					return HttpResponseRedirect("Wrong credentials")
		else:
			return render(request, 'home.html', {})
	except Exception as e:
		print e	

####################  Student Dashboard Function ############################
def student_dashboard(request):
	try:
		student_id=request.POST['student_id']
		student_record=Students_Record.objects_filter(student_id=student_id)
		right_questions_list=[]
		right_questions_dict={'question_id':'','question':'','answer':'','quiz_id':''}
		wrong_questions_list=[]
		wrong_questions_dict={'question_id':'','question':'','answer':'','quiz_id':''}
		for rec in student_record:
			right_answers=rec.right_question_id
			right_questions_data=Questions.objects.filter(question_id__in=right_answers])
			for ques in right_questions_data:
				right_questions_dict['question_id']=ques.question_id
				right_questions_dict['question']=ques.question
				right_questions_dict['answer']=ques.answer
				right_questions_dict['quiz_id']=ques.quiz_id
				right_questions_list.append(right_questions_dict.copy())
			wrong_questions_data=Questions.objects.filter(~Q(question_id__in=right_answers])
			for ques in wrong_questions_data:
				wrong_questions_dict['question_id']=ques.question_id
				wrong_questions_dict['question']=ques.question
				wrong_questions_dict['answer']=ques.answer
				wrong_questions_dict['quiz_id']=ques.quiz_id
				wrong_questions_list.append(wrong_questions_dict.copy())
		return render(request, 'student_dashboard.html', {'right_questions':right_questions_list,'wrong_questions':wrong_questions_list})
	except Exception as e:
		print e	


####################  Teachers Dashboard Function ############################
def teacher_dashboard(request):
	try:
		teacher_id=request.POST['teacher_id']
		student_info_list=[]
		student_info_dict={'student_id':'','score':''}
		student_id_array=[]
		teacher_info=Teachers.objects.filter(teacher_id=teacher_id)
		for info in teacher_info:
			school_name=info.teacher_school
		students_info=Students.objects.filter(student_school=school_name)
		for info in students_info:
			student_id=info.student_id
			student_id_array.append(str(student_id))
		student_record=Students_Record.objects_filter(student_id__in=student_id_array)
		for record in student_record:
			student_id=record.student_id
			score=record.score
			student_info_dict['student_id']=student_id
			student_info_dict['score']=score
			student_info_list.append(student_info_dict.copy())
		return render(request, 'teacher_dashboard.html', {'info':student_info_list,})


####################  Leaderboard View Function for City ############################
def Leaderboard_city(request):
	try:
		student_city=request.POST['student_city']
		student_info_list=[]
		student_id_array=[]
		student_info_dict={'student_id':'','score':''}
		students_info=Students.objects.filter(student_city=student_city)
		for info in students_info:
			student_id=info.student_id
			student_id_array.append(str(student_id))
		student_record=Students_Record.objects_filter(student_id__in=student_id_array)
		for record in student_record:
			student_id=record.student_id
			score=record.score
			student_info_dict['student_id']=student_id
			student_info_dict['score']=score
			student_info_list.append(student_info_dict.copy())
		return render(request, 'leaderboard_city.html', {'info':student_info_list,})

	except Exception as e:
		print e

####################  Leaderboard View Function for School ############################
def Leaderboard_school(request):
	try:
		student_school=request.POST['student_school']
		student_info_list=[]
		student_id_array=[]
		student_info_dict={'student_id':'','score':''}
		students_info=Students.objects.filter(student_school=student_school)
		for info in students_info:
			student_id=info.student_id
			student_id_array.append(str(student_id))
		student_record=Students_Record.objects_filter(student_id__in=student_id_array)
		for record in student_record:
			student_id=record.student_id
			score=record.score
			student_info_dict['student_id']=student_id
			student_info_dict['score']=score
			student_info_list.append(student_info_dict.copy())
		return render(request, 'leaderboard_school.html', {'info':student_info_list,})

	except Exception as e:
		print e

####################  Teachers Login Function ############################
def Teacher_Login(request):
	try:
		if (request.method=='POST'):
			username=request.POST['user_name']
			password=request.POST['pass_word']
			user=Teachers.objects.filter(username=username)
			for us in user:
				user_password=us.password
				check=check_password(password,user_password)
				if check==True:
					return render(request, 'teachers_dashboard.html', {}})
				else:
					return HttpResponseRedirect("Wrong credentials")
		else:
			return render(request, 'home.html', {})
	except Exception as e:
		print e	



#################### Student Signup   ############################
def Register(request):
	if (request.method=='POST'):
		try:
			customer=Students.objects.create(username=request.POST['username'], password=request.POST['password'],
			student_name=request.POST['student_name'],student_standard=request.POST['student_standard'],student_school=request.POST['student_school'],
			student_city=request.POST['student_city'], )
			return HttpResponse('success')
		except Exception as e:
			print 'error',e
	else:
		return render(request, 'home.html', {})


