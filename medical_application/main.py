from medical_application.contact import Contact
from medical_application.address import Address
from medical_application.doctor import Doctor

address = Address("12", "Health Ave", "Lagos", "Lagos")
contact = Contact("Dr. John", "08012345678", "john@example.com", address)

new_doctor = Doctor.sign_up("Dr. John", "securepass", "Cardiologist", contact)
