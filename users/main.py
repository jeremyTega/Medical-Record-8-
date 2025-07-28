from medical_application.address import Address
from medical_application.contact import Contact
from medical_application.doctor import Doctor
from users.clinic_admin import Admin
from config.database import get_database
import traceback

collections = get_database()

doctors_collection = collections["doctors"]
patients_collection = collections["patients"]
records_collection = collections["records"]
appointments_collection = collections["appointments"]
requested_collection = collections["request_appointments"]

admin = Admin("admin")


def main_menu():
    print("\n--- Welcome to the Medical App ---")
    print("1. Log in")
    print("2. Register Patient")
    print("3. Register Doctor")
    print("4. Exit")


def patient_menu(email):
    while True:
        print("\n--- Patient Menu ---")
        print("1. View Doctors")
        print("2. Request Appointment")
        print("3. View My Medical Records")
        print("4. Logout")
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                doctors = admin.get_all_doctors()
                for doc in doctors:
                    print(f"{doc['name']} ({doc['specialisation']}) - {doc['contact']['email']}")
            elif choice == "2":
                doctor_email = input("Doctor Email: ")
                reason = input("Reason: ")
                admin.book_appointment(email, doctor_email, reason, "")
                print("Appointment requested successfully.")
            elif choice == "3":
                records = admin.get_medical_records(email)
                for rec in records:
                    print(f"Type: {rec['diagnosis_type']}, Medication: {rec['medication']}")
            elif choice == "4":
                Admin.logout_user(email)
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)


def doctor_menu(email):
    while True:
        print("\n--- Doctor Menu ---")
        print("1. View Appointments")
        print("2. Add Diagnosis")
        print("3. Logout")
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                doc_data = doctors_collection.find_one({"contact.email": email})
                if doc_data:
                    addr = doc_data["contact"]["address"]
                    address = Address(**addr)
                    contact = Contact(
                        phone_no=doc_data["contact"]["phone_no"],
                        email=doc_data["contact"]["email"],
                        address=address
                    )
                    doctor = Doctor(
                        name=doc_data["name"],
                        password=doc_data["password"],
                        specialisation=doc_data["specialisation"],
                        contact=contact
                    )
                    appointments = doctor.get_appointments()
                    for appt in appointments:
                        print(appt)
                else:
                    print("Doctor not found.")
            elif choice == "2":
                patient_email = input("Patient Email: ")
                diagnosis = input("Diagnosis: ")
                medication = input("Medication: ")
                admin.add_diagnosis(patient_email, diagnosis, medication)
                print("Diagnosis added successfully.")
            elif choice == "3":
                Admin.logout_user(email)
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)


def run_app():
    while True:
        main_menu()
        try:
            option = input("Enter your choice: ")

            if option == "1":
                email = input("Email: ")
                password = input("Password: ")
                msg = admin.login_user(email, password)
                print(msg)

                if "Doctor" in msg:
                    doctor_menu(email)
                elif "Patient" in msg:
                    patient_menu(email)

            elif option == "2":
                name = input("Name: ")
                gender = input("Gender: ")
                password = input("Password: ")
                phone = input("Phone: ")
                email = input("Email: ")
                house_no = input("House number:  ")
                street = input("Street: ")
                city = input("City: ")
                state = input("State: ")
                address = Address(house_no, street, city, state)
                contact = Contact( phone, email, address)
                admin.create_patient(name, gender, password, contact)
                print("Patient registered successfully.")

            elif option == "3":
                name = input("Name: ")
                specialisation = input("Specialisation: ")
                password = input("Password: ")
                phone = input("Phone: ")
                email = input("Email: ")
                house_no = input("House: ")
                street = input("Street: ")
                city = input("City: ")
                state = input("State: ")
                address = Address(house_no, street, city, state)
                contact = Contact(phone, email, address)
                admin.create_doctor(name, password, specialisation, contact)
                print("Doctor registered successfully.")

            elif option == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            print("\nSomething went wrong:")
            print(traceback.format_exc())
            print("Returning to main menu...")


if __name__ == "__main__":
    run_app()
