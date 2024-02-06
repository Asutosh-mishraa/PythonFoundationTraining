from dao.HospitalServiceImpl import HospitalServiceImpl
from entity.Appointments import Appointment
from util.DBConnection import DBConnection


class MainModule:
    def __init__(self):
        db_connection = DBConnection.getConnection()
        self.service = HospitalServiceImpl(db_connection)

    def main(self):
        while True:
            print("\nMenu:")
            print("1. Get Appointment by ID")
            print("2. Get Appointments for Patient")
            print("3. Get Appointments for Doctor")
            print("4. Schedule Appointment")
            print("5. Update Appointment")
            print("6. Cancel Appointment")
            print("7. Show all doctors")
            print("8. Show all patients")
            print("9. Show all appointments")
            print("10. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                appointment_id = int(input("Enter appointment ID: "))
                appointment = self.service.getAppointmentById(appointment_id)
                print("Appointment Details:", appointment)

            elif choice == '2':
                patient_id = int(input("Enter patient ID: "))
                appointments = self.service.getAppointmentsForPatient(patient_id)
                print("Appointments for Patient:")
                for appointment in appointments:
                    print(appointment)

            elif choice == '3':
                doctor_id = int(input("Enter doctor ID: "))
                appointments = self.service.getAppointmentsForDoctor(doctor_id)
                print("Appointments for Doctor:")
                for appointment in appointments:
                    print(appointment)

            elif choice == '4':
                patient_id = int(input("Enter patient ID: "))
                doctor_id = int(input("Enter doctor ID: "))
                appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
                description = input("Enter appointment description: ")
                appointment = Appointment(None,patientId=patient_id, doctorId=doctor_id, appointmentDate=appointment_date,
                                          description=description)
                success = self.service.scheduleAppointment(appointment)
                if success:
                    print("Appointment scheduled successfully.")
                else:
                    print("Failed to schedule appointment.")

            elif choice == '5':
                appointment_id = int(input("Enter appointment ID to update: "))
                apt = self.service.getAppointmentById(appointment_id)
                if apt is None:
                    print("Appointment with ID", appointment_id, "not found.")
                    continue
                patient_id = input("Enter patient ID(if dont want to change doctor give the old one): ")
                doctor_id = input("Enter doctor ID (if dont want to change doctor give the old one): ")
                appointment_date = input("Enter appointment date (YYYY-MM-DD) (press enter if you don't want to "
                                         "update): ")
                description = input("Enter appointment description (press enter if you don't want to update): ")
                appointment = Appointment(appointmentId=appointment_id, patientId=patient_id, doctorId=doctor_id,
                                          appointmentDate=appointment_date, description=description)
                success = self.service.updateAppointment(appointment)
                if success:
                    print("Appointment updated successfully.")
                else:
                    print("Failed to update appointment.")

            elif choice == '6':
                appointment_id = int(input("Enter appointment ID: "))
                success = self.service.cancelAppointment(appointment_id)
                if success:
                    print("Appointment canceled successfully.")
                else:
                    print("Failed to cancel appointment.")

            elif choice == '7':
                self.service.showAllDoctors()

            elif choice == '8':
                self.service.showAllPatients()
            elif choice == '9':
                self.service.showAllAppointments()
            elif choice == '10':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main_module = MainModule()
    main_module.main()
