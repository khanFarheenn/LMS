from rest_framework import serializers
from . models import *



class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"
        
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        
        
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"




class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = "__all__"     
        
        
                                                                    
        
        
class Return_recordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Return_records
        fields = "__all__"                        
        
        
        
        
                
        
        