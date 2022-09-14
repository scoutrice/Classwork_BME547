def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient

def print_database(db):
    for patient in db:
        print(patient)
        print("Name: {}, id: {}, age: {}".format(patient[0], patient[1], patient[2]))

def find_patient(db, patient_id):
    for patient in db:
        if patient[1] == patient_id:
            return patient
    return False 

def add_results(db, patient_id, test_name, test_value):
    patient = find_patient(db, patient_id)
    patient[3].append((test_name, test_value))


def main():
    db = []
    db.append(create_patient_entry("Anne Ables", 1, 30))
    db.append(create_patient_entry("Bob Boyles", 2, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    add_results(db, 3, "HDL", 100)
    print_database(db)

if __name__ == "__main__":
    main()