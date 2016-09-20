from django.core import serializers
from models import Students,Teachers,Quiz,Questions,Certificates,Students_Record

#############Students Model Serializer######################
students_serialized_obj = serializers.serialize('json', Students.objects.all())

#############Teachers Model Serializer######################
teachers_serialized_obj = serializers.serialize('json', Teachers.objects.all())

#############Quiz Model Serializer######################
quiz_serialized_obj = serializers.serialize('json', Quiz.objects.all())

#############Questions Model Serializer######################
questions_serialized_obj = serializers.serialize('json', Questions.objects.all())

#############Certificates Model Serializer######################
certificate_serialized_obj = serializers.serialize('json', Certificates.objects.all())

#############Student_Records Model Serializer######################
record_serialized_obj = serializers.serialize('json', Students_Record.objects.all())