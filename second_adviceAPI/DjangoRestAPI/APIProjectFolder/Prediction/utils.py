diseases = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis',
       'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 'Diabetes ',
       'Gastroenteritis', 'Bronchial Asthma', 'Hypertension ', 'Migraine',
       'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice',
       'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
       'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E',
       'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia',
       'Dimorphic hemmorhoids(piles)', 'Heart attack', 'Varicose veins',
       'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
       'Osteoarthristis', 'Arthritis',
       '(vertigo) Paroymsal  Positional Vertigo', 'Acne',
       'Urinary tract infection', 'Psoriasis', 'Impetigo']
doctor_db = {}

for i in diseases:
    doctor_db[i] = ""

doctor_db["Fungal infection"] = "Dermatologist"
doctor_db["Allergy"] = "Dermatologist"
doctor_db["GERD"] = "Gastroenterologist"
doctor_db["Chronic cholestasis"] = "Gastroenterologist"
doctor_db["Drug Reaction"] = "General Physician"
doctor_db["Peptic ulcer disease"] = "Gastroenterologist"
doctor_db["AIDS"] = "HIV specialist"
doctor_db["Diabetes"] = "General Physician"
doctor_db["Gastroenteritis"] = "Gastroenterologist"
doctor_db["Hypertension"] = "General Physician"
doctor_db["Migraine"] = "Neurologist"
doctor_db["Cervical spondylosis"] = "Physiotherapist"
doctor_db["Paralysis (brain hemorrhage)"] = "Neurologist"
doctor_db["Jaundice"] = "Gastroenterologist"
doctor_db["Malaria"] = "General Physician"
doctor_db["Chicken pox"] =  "General Physician"
doctor_db["Dengue"] = "General Physician"
doctor_db["Typhoid"] = "GeneraL Physician"
doctor_db["hepatitis A"] = "Hepatologist"
doctor_db["Hepatitis B"] = "Hepatologist"
doctor_db["Hepatitis C"] = "Hepatologist"
doctor_db["Hepatitis D"] = "Hepatologist"
doctor_db["Hepatitis E"] = "Hepatologist"
doctor_db["Alcoholic hepatitis"] = "Hepatologist"
doctor_db["Tuberculosis"] = "Pulmonologist"
doctor_db["Common Cold"] = "General Physician"
doctor_db["Pneumonia"] = "Pulmonologist"
doctor_db["Dimorphic hemmorhoids(piles)"] = "Urologist"
doctor_db["Heart attack"] = "Cardiologist"
doctor_db["Varicose veins"] = "Vascular Surgeons"
doctor_db["Hypothyroidism"] = "Endocrinologist"
doctor_db["Hypoglycemia"] = "Endocrinologist"
doctor_db["Osteoarthristis"] = "Rheumatologist"
doctor_db["Arthritis"] = "Rheumatologist"
doctor_db["(vertigo) Paroymsal  Positional Vertigo"] = "Neurologist"
doctor_db["Acne"] = "Dermatologist"
doctor_db["Urinary tract infection"] = "Urologist"
doctor_db["Psoriasis"] = "Dermatologist"
doctor_db["Impetigo"] = "Dermatologist"










# print(doctor_db.keys())