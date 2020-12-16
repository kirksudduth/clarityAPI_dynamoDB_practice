from django.http import HttpResponseServerError
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from clarityAPIapp.models import EmployeeModel
from .userviewset import UserSerializer


class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
  
    url = serializers.HyperlinkedIdentityField(view_name='employee-detail')

    user = UserSerializer()
    
    class Meta:
        model = EmployeeModel
        url = serializers.HyperlinkedIdentityField(
            view_name='employees',
            lookup_field='id'
        )
        fields = ('id', 'url', 'employee_number', 'employee_admin', 'user')
        
class EmployeeView(viewsets.ViewSet):
    
    def create(self, request):
        newemployee = EmployeeModel()
        newemployee.employee_number= request.data["employee_number"]
        newemployee.employee_admin= request.data["emplee_admin"]
        newemployee.save()

        serializer = EmployeesSerializer(
            newemployee, context={'request': request})

        return Response(serializer.data)
  
    def retrieve(self, request, pk=None):
        try:
            employee = EmployeeModel.objects.get(pk=pk)
            serializer = EmployeesSerializer(
                employee, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        employee = EmployeeModel.objects.get(pk=pk)
        employee.employee_number = request.data["employee_number"]
        employee.employee_admin = request.data["employee_admin"] 
        employee.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            deleteemployee = EmployeeModel.objects.get(pk=pk)
            deleteemployee.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except EmployeeModel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        employees = EmployeeModel.objects.all()
        serializer = EmployeesSerializer(
        employees, many=True, context={'request': request})
        return Response(serializer.data)