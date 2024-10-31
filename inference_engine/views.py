# inference_engine/views.py

from django.http import JsonResponse
from rest_framework import viewsets
from .models import Patient, Symptom, Diagnosis
from .serializers import PatientSerializer, SymptomSerializer, DiagnosisSerializer
from .inference_engine import MedicalKnowledgeEngine, Fact

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # Run the expert system
        engine = MedicalKnowledgeEngine()
        engine.reset()
        for symptom in request.data.get('symptoms', []):
            engine.declare(Fact(symptom=symptom['name']))
        engine.run()

        # Gather the diagnoses
        diagnoses = [fact['diagnosis'] for fact in engine.facts.values() if 'diagnosis' in fact]
        
        # Add the diagnoses to the response
        response.data['diagnoses'] = diagnoses
        
        return response
