from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from . models import *

# Create your views here.


@api_view()
def hello(request):
    return Response({"message":"Hi i am LGS"})

# ===============student=================

@api_view(['POST','GET'])
def Studentfun(request):
    if request.method =='POST':
        json_Data = request.data
        # print(json_Data)# quret set give as a output
        add_StudentSerializer=StudentSerializer(data=json_Data)
        # print(add_StudentSerializer)#jason data give 
        if add_StudentSerializer.is_valid():
            add_StudentSerializer.save()
            return Response({"massage":"Student Recode Added Successfully"})
        return Response({"message":"Invalid Data insert pls Add valid Data"})
    
    else:
        request.method =='GET'
        get_student=Student.objects.all()
        # print(get_student)
        serializerData=StudentSerializer(get_student, many=True)
        # print(serializerData)# give output as a model fields 
        # print(serializerData.data)# give output as a json data 
        # print({"get_student":serializerData.data})# give output as a tuples of dictinary
        return Response({"get_student":serializerData.data})
        # return Response(serializerData.data)
            

# ====================BOOKS==========================

@api_view(['POST','GET'])
def Booksfun(request):
    if request.method =='POST':
        json_Data = request.data
        # print(json_Data)
        add_BooksSerializer=BooksSerializer(data=json_Data)
        # print(add_BooksSerializer)
        if add_BooksSerializer.is_valid():
            add_BooksSerializer.save()
            return Response({"massage":"Book  Added Successfully"})
        return Response({"message":"Invalid Data insert pls Add valid Data"})
    
    else:
        request.method =='GET'
        get_Books=Books.objects.all()
        # print(get_Books)
        serializerData=BooksSerializer(get_Books, many=True)
        # print(serializerData)
        return Response({"get_Books":serializerData.data})
    
    
    
#    =====================ISSUE=============== 
    
    
@api_view(['POST','GET'])
def Issuesfun(request,pk=None):
    
    if request.method =='GET':
        if pk is not None:
            get_issue_id=Issue.objects.get(id=pk)
            serializerData=IssueSerializer(get_issue_id, many=False)
            # print(serializerData)
            return Response({"get_issue_id":serializerData.data})
       
       
        else:
            get_Issue=Issue.objects.all()
            # print(get_Issue)
            serializerData=IssueSerializer(get_Issue, many=True)
            # print(serializerData)
            return Response({"get_Issue":serializerData.data})
           
        
       
    
      
        
    else:
        request.method =='POST'
        json_Data = request.data
        # print(json_Data)
        add_IssueSerializer=IssueSerializer(data=json_Data)
        # print(add_IssueSerializer)
        if add_IssueSerializer.is_valid():
            add_IssueSerializer.save()
            return Response({"massage":"Issue  Added Successfully"})
        return Response({"message":"Invalid Data insert pls Add valid Data"})
    
#   ==================MANAGER=====================  
        
@api_view(['POST','GET','PUT'])
def Managerfun(request,pk=None):
    if request.method =='POST':
        json_Data = request.data
        # print(json_Data)
        add_ManagerSerializer=ManagerSerializer(data=json_Data)
        # print(add_ManagerSerializer)
        if add_ManagerSerializer.is_valid():
            add_ManagerSerializer.save()
            return Response({"massage":"Manager  Added Successfully"})
        return Response({"message":"Invalid Data insert pls Add valid Data"})
    
    elif request.method=='PUT':
        ManagerUpdate =Manager.objects.filter(id=pk)
        if ManagerUpdate is not None :
           serializerUpdate=ManagerSerializer(instance = ManagerUpdate,data = request.data)
           if serializerUpdate.is_valid():
               serializerUpdate.save()
               return Response({"massage":"manager recored updated Successfully "})
           return Response({"massage":"Invalid data enter "})
       
       
    
           
        
        
        
    
    else:
        request.method =='GET'
        get_Manager=Manager.objects.all()
        # print(get_Manager)
        serializerData=ManagerSerializer(get_Manager, many=True)
        # print(serializerData)
        return Response({"get_Manager":serializerData.data})
    
    
# =====DELETE FUN ISSUE AND SAVE DATA RETURN RECODE TABLE========
@api_view(['DELETE'])
def Issuesdelete(request, pk=None):
    if request.method == 'DELETE':
        try:
            issue = Issue.objects.get(id=pk)
            # Save the record to Return_record table
            # Return_records.objects.create(issue=issue)
            create_return_record(issue)
            # Now delete the issue
            issue.delete()
            return Response({"message": "Issue deleted successfully"})
        except Issue.DoesNotExist:
            return Response({"message": "Issue not found"})        
    
def create_return_record(issue):
    # Assuming the fields for Return_record are the same as in the model
    Return_records.objects.create(
        book_id=issue.book_id,
        student_id=issue.student_id,
        date=issue.date,
        time=issue.time,
    )        
    # ================return recode========
@api_view(['POST','GET'])
def Return_recordsfun(request):
    if request.method =='POST':
        json_Data = request.data
        # print(json_Data)
        add_Return_recordsSerializer=Return_recordsSerializer(data=json_Data)
        # print(add_StudentSerializer)
        if add_Return_recordsSerializer.is_valid():
            add_Return_recordsSerializer.save()
            return Response({"massage":"Return_records Recode Added Successfully"})
        return Response({"message":"Invalid Data insert pls Add valid Data"})
    
    else:
        request.method =='GET'
        get_Return_records=Return_records.objects.all()
        # print(Return_records)
        serializerData=Return_recordsSerializer(get_Return_records, many=True)
        # print(serializerData)
        return Response({"get_Return_records":serializerData.data})
            

    
    
    
    
    
    
    
    
    
    
    
#  ================login ========   
@api_view(['POST'])
def loginfun(request):
   
        Email = request.data.get('email')
        Password = request.data.get('password')
        role = request.data.get('role')
        
        if role =="Manager":
            Managerdata = Manager.objects.filter(email=Email, password=Password)
            if Managerdata.exists():
                return Response({"message":"Login successfully"})
            else:
                return Response({"message":"not login  successfully"})  
        
        
    
    