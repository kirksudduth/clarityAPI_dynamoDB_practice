from django.http import HttpResponseServerError
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from clarityAPIapp.models import PatientModel

class PatientsSerializer(serializers.HyperlinkedModelSerializer):
    
    url = serializers.HyperlinkedIdentityField(view_name='patient-detail')

    class Meta:
        model = PatientModel
        url = serializers.HyperlinkedIdentityField(
            view_name='patients',
            lookup_field='id'
        )
        fields = ('id', 'url', "patient_first_name", "patient_middle_name", "patient_last_name", "patient_Date_of_Birth")
        
class PatientView(viewsets.ViewSet):
    
    def create(self, request):
        newppatient = PatientModel()
        newppatient.patient_first_name= request.data["patient_first_name"]
        newppatient.patient_middle_name= request.data["patient_middle_name"]
        newppatient.patient_last_name= request.data["patient_last_name"]
        newppatient.patient_Date_of_Birth= request.data["patient_Date_of_Birth"]
        newppatient.patient_referral= request.data["patient_referral"]
        newppatient.save()

        serializer = PatientsSerializer(
            newppatient, context={'request': request})

        return Response(serializer.data)
  
    def retrieve(self, request, pk=None):
        try:
            patient = PatientModel.objects.get(pk=pk)
            serializer = PatientsSerializer(
                patient, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        patient = PatientModel.objects.get(pk=pk)
        patient.patient_first_name = request.data["patient_first_name"]
        patient.patient_middle_name = request.data["patient_middle_name"]
        patient.patient_last_name = request.data["patient_last_name"]
        patient.patient_Date_of_Birth = request.data["patient_Date_of_Birth"]
        patient.patient_referral= request.data["patient_referral"]
        
        patient.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            deletepatient = PatientModel.objects.get(pk=pk)
            deletepatient.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except PatientModel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        patients = PatientModel.objects.all()
        serializer = PatientsSerializer(
            patients, many=True, context={'request': request})
        return Response(serializer.data)