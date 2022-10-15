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






def min_distance(distance,distances):
    dict1 = {}
    temp_arr = []
    for i,j in enumerate(distances):
        dict1[i] = abs(j - distance)

    sorted_values = sorted(dict1.values()) # Sort the values
    sorted_dict = {}

    for i in sorted_values:
        for k in dict1.keys():
            if dict1[k] == i:
                sorted_dict[k] = dict1[k]
    for k in (sorted_dict.keys()):
        temp_arr.append(distances[k])
    return temp_arr


# distance1 = 5 
# distances1 = [7,9,2,5,1]
# ans = min_distance(distance1,distances1)
# # to get first 3 closest location 
# ans = ans[:3]
# print(*ans)



# print(doctor_db.keys())