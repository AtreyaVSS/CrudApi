from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import empmodel
from .serializers import  EmpSerializers


class employee_data(APIView):
    def post(self, request):
        serializer = EmpSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=201)
        return Response({"errors": serializer.errors}, status=400)
    

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Employee ID (pk) is required for update."}, status=400)

        employee =empmodel.objects.get(id=pk)
        serializer = EmpSerializers(employee, data=request.data, partial=True)  # partial=True allows partial updates
        if serializer.is_valid():
            serializer.save()
        else:
             return Response({"errors": serializer.errors}, status=400)    

        return Response({"data": serializer.data}, status=200)
    


    def get(self, request, pk=None):
        if pk:
            employee = get_object_or_404(empmodel, pk=pk)
            serializer = EmpSerializers(employee)
            return Response({"data": serializer.data}, status=200)
        else:
            employees = empmodel.objects.all()
            serializer = EmpSerializers(employees, many=True)
            return Response({"data": serializer.data}, status=200)
        


    def delete(self, request, pk=None):
        if pk is None:
            return Response({"error": "Employee ID (pk) is required for deletion."})
        employee = empmodel.objects.get(id=pk)
        employee.delete()
        return Response({"message": f"Employee with id {pk} has been deleted."})
       

