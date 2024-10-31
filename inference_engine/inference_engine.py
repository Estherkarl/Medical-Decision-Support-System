
from experta import Rule, Fact, KnowledgeEngine

class MedicalKnowledgeEngine(KnowledgeEngine):
    @Rule(Fact(symptom='fever') & Fact(symptom='cough'))
    def diagnose_flu(self):
        self.declare(Fact(diagnosis='flu'))

    @Rule(Fact(symptom='sore throat') & Fact(symptom='runny nose'))
    def diagnose_cold(self):
        self.declare(Fact(diagnosis='cold'))

    @Rule(Fact(symptom='rash'))
    def diagnose_measles(self):
        self.declare(Fact(diagnosis='measles'))

    @Rule(Fact(symptom='chest pain') & Fact(symptom='shortness of breath'))
    def diagnose_heart_attack(self):
        self.declare(Fact(diagnosis='heart attack'))

    @Rule(Fact(symptom='headache', severity='severe'))
    def diagnose_migraine(self):
        self.declare(Fact(diagnosis='migraine'))

    @Rule(Fact(symptom='joint pain', duration='chronic'))
    def diagnose_arthritis(self):
        self.declare(Fact(diagnosis='arthritis'))

    @Rule(Fact(symptom='shortness of breath') & Fact(symptom='wheezing'))
    def diagnose_asthma(self):
        self.declare(Fact(diagnosis='asthma'))

    @Rule(Fact(symptom='nausea') & Fact(symptom='vomiting'))
    def diagnose_gastroenteritis(self):
        self.declare(Fact(diagnosis='gastroenteritis'))

    @Rule(Fact(symptom='muscle weakness') & Fact(symptom='fatigue'))
    def diagnose_muscular_dystrophy(self):
        self.declare(Fact(diagnosis='muscular dystrophy'))

    @Rule(Fact(symptom='chest pain') & Fact(symptom='shortness of breath') & Fact(symptom='sweating'))
    def diagnose_heart_attack(self):
        self.declare(Fact(diagnosis='heart attack'))

    @Rule(Fact(symptom='headache', severity='severe') & Fact(symptom='nausea'))
    def diagnose_migraine(self):
        self.declare(Fact(diagnosis='migraine'))

    @Rule(Fact(symptom='joint pain', duration='chronic') & Fact(symptom='morning stiffness'))
    def diagnose_rheumatoid_arthritis(self):
        self.declare(Fact(diagnosis='rheumatoid arthritis'))

    @Rule(Fact(symptom='abdominal pain', severity='severe') & Fact(symptom='blood in stool'))
    def diagnose_colorectal_cancer(self):
        self.declare(Fact(diagnosis='colorectal cancer'))

    @Rule(Fact(symptom='frequent urination') & Fact(symptom='excessive thirst'))
    def diagnose_diabetes(self):
        self.declare(Fact(diagnosis='diabetes'))

    @Rule(Fact(symptom='visual disturbances') & Fact(symptom='headache', severity='moderate'))
    def diagnose_migraine_with_aura(self):
        self.declare(Fact(diagnosis='migraine with aura'))

    @Rule(Fact(symptom='fatigue', duration='persistent') & Fact(symptom='unexplained weight loss'))
    def diagnose_chronic_fatigue_syndrome(self):
        self.declare(Fact(diagnosis='chronic fatigue syndrome'))

    @Rule(Fact(symptom='skin rash', duration='acute') & Fact(symptom='fever'))
    def diagnose_infectious_disease(self):
        self.declare(Fact(diagnosis='infectious disease'))

    @Rule(Fact(symptom='depression') & Fact(symptom='loss of interest or pleasure'))
    def diagnose_major_depressive_disorder(self):
        self.declare(Fact(diagnosis='major depressive disorder'))

    @Rule(Fact(symptom='memory loss') & Fact(symptom='confusion'))
    def diagnose_alzheimers_disease(self):
        self.declare(Fact(diagnosis='Alzheimer\'s disease'))

    @Rule(Fact(symptom='loss of appetite') & Fact(symptom='abdominal pain', severity='mild'))
    def diagnose_gastritis(self):
        self.declare(Fact(diagnosis='gastritis'))

    @Rule(Fact(symptom='irregular menstrual cycles') & Fact(symptom='excessive hair growth'))
    def diagnose_polycystic_ovary_syndrome(self):
        self.declare(Fact(diagnosis='polycystic ovary syndrome'))

    @Rule(Fact(symptom='persistent cough', duration='more than 3 weeks') & Fact(symptom='blood in sputum'))
    def diagnose_tuberculosis(self):
        self.declare(Fact(diagnosis='tuberculosis'))

    @Rule(Fact(symptom='swollen lymph nodes') & Fact(symptom='night sweats'))
    def diagnose_lymphoma(self):
        self.declare(Fact(diagnosis='lymphoma'))

    @Rule(Fact(symptom='shortness of breath', severity='sudden onset') & Fact(symptom='sharp chest pain'))
    def diagnose_pulmonary_embolism(self):
        self.declare(Fact(diagnosis='pulmonary embolism'))

    @Rule(Fact(symptom='difficulty swallowing') & Fact(symptom='hoarseness'))
    def diagnose_esophageal_cancer(self):
        self.declare(Fact(diagnosis='esophageal cancer'))

    @Rule(Fact(symptom='abdominal pain', severity='severe') & Fact(symptom='bloody vomit'))
    def diagnose_peptic_ulcer_disease(self):
        self.declare(Fact(diagnosis='peptic ulcer disease'))

    @Rule(Fact(symptom='decreased urine output') & Fact(symptom='swelling in ankles'))
    def diagnose_kidney_failure(self):
        self.declare(Fact(diagnosis='kidney failure'))

    @Rule(Fact(symptom='joint pain', duration='intermittent') & Fact(symptom='morning stiffness'))
    def diagnose_osteoarthritis(self):
        self.declare(Fact(diagnosis='osteoarthritis'))

    @Rule(Fact(symptom='confusion', duration='sudden onset') & Fact(symptom='seizures'))
    def diagnose_epilepsy(self):
        self.declare(Fact(diagnosis='epilepsy'))

    @Rule(Fact(symptom='vision loss') & Fact(symptom='eye pain'))
    def diagnose_glaucoma(self):
        self.declare(Fact(diagnosis='glaucoma'))

    @Rule(Fact(symptom='fatigue', severity='chronic') & Fact(symptom='difficulty concentrating'))
    def diagnose_fibromyalgia(self):
        self.declare(Fact(diagnosis='fibromyalgia'))
