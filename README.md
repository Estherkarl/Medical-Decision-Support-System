# Medical Decision Support System (MDSS)

## Overview
The Medical Decision Support System (MDSS) is a Django-based web application designed to assist healthcare professionals in making clinical decisions. It integrates patient data, symptom analysis, and inference engine logic to provide diagnostic suggestions and treatment recommendations.

## Features
- **Patient Management**: Store and manage patient information including name, age, gender, symptoms, diagnosis, and treatment.
- **Inference Engine**: Utilizes an inference engine (e.g., Experta) to process symptoms and generate diagnostic suggestions based on predefined rules.
- **RESTful API**: Provides APIs using Django REST Framework for interacting with patient data programmatically.
- **Admin Interface**: Customized Django admin interface for managing patients and diagnostic records.
  

## Scenario
Imagine you are a healthcare professional using the MDSS to assist in diagnosing a patient presenting with symptoms of fever, cough, and fatigue. You enter the patient's information and symptoms into the system to generate a list of possible diagnoses and treatment recommendations based on medical guidelines and historical data.

## Installation
Follow these steps to set up and run the MDSS on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/Estherkarl/Medical-Decision-Support-System.git
   cd repository
