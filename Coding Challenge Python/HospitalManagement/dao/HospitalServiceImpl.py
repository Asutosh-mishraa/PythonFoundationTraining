from mysql.connector import Error
from dao.IHospitalService import IHospitalService
from entity.Appointments import Appointment
from myexception.PatientNumberNotFoundException import PatientNumberNotFoundException


class HospitalServiceImpl(IHospitalService):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def getAppointmentById(self, appointmentId):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM appointment WHERE appointmentId = %s", (appointmentId,))
            appointment_record = cursor.fetchone()
            cursor.close()

            if appointment_record:
                appointment = Appointment(
                    appointmentId=appointment_record['appointmentId'],
                    patientId=appointment_record['patientId'],
                    doctorId=appointment_record['doctorId'],
                    appointmentDate=appointment_record['appointmentDate'],
                    description=appointment_record['description']
                )
                return appointment
            else:
                raise PatientNumberNotFoundException()

        except Error as e:
            print("Error getting appointment by ID:", e)
            return None

    def getAppointmentsForPatient(self, patientId):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM appointment WHERE patientId = %s", (patientId,))
            appointment_records = cursor.fetchall()
            cursor.close()

            appointments = []
            for appointment_record in appointment_records:
                appointment = Appointment(
                    appointmentId=appointment_record['appointmentId'],
                    patientId=appointment_record['patientId'],
                    doctorId=appointment_record['doctorId'],
                    appointmentDate=appointment_record['appointmentDate'],
                    description=appointment_record['description']
                )
                appointments.append(appointment)

            return appointments

        except Error as e:
            print("Error getting appointments for patient:", e)
            return []

    def getAppointmentsForDoctor(self, doctorId):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM appointment WHERE doctorId = %s", (doctorId,))
            appointment_records = cursor.fetchall()
            cursor.close()

            appointments = []
            for appointment_record in appointment_records:
                appointment = Appointment(
                    appointmentId=appointment_record['appointmentId'],
                    patientId=appointment_record['patientId'],
                    doctorId=appointment_record['doctorId'],
                    appointmentDate=appointment_record['appointmentDate'],
                    description=appointment_record['description']
                )
                appointments.append(appointment)

            return appointments

        except Error as e:
            print("Error getting appointments for doctor:", e)
            return []

    def scheduleAppointment(self, appointment):
        try:
            if not self.isValidAppointment(appointment):
                print("Invalid appointment data.")
                return False
            if self.hasAppointmentConflict(appointment):
                print("Appointment conflicts with existing appointments.")
                return False

            cursor = self.db_connection.cursor()
            query = ("INSERT INTO appointment (patientId, doctorId, appointmentDate, description) VALUES (%s, %s, %s, "
                     "%s)")
            data = (appointment.get_patientId(), appointment.get_doctorId(), appointment.get_appointmentDate(),
                    appointment.get_description())
            cursor.execute(query, data)
            self.db_connection.commit()
            new_appointment_id = cursor.lastrowid
            print("Your Appointment ID:", new_appointment_id)
            cursor.close()
            # print("Appointment Scheduled...")
            return True

        except Error as e:
            print("Error scheduling appointment:", e)
            return False

    def updateAppointment(self, appointment):
        try:
            # if not self.isValidAppointment(appointment):
            #     print("Invalid appointment data.")
            #     return False

            if self.hasAppointmentConflict(appointment):
                print("Appointment conflicts with existing appointments.")
                return False

            cursor = self.db_connection.cursor()
            query = ("UPDATE appointment SET patientId = %s, doctorId = %s, appointmentDate = %s, description = %s "
                     "WHERE appointmentId = %s")
            data = (appointment.get_patientId(), appointment.get_doctorId(), appointment.get_appointmentDate(),
                    appointment.get_description(),
                    appointment.get_appointmentId())
            cursor.execute(query, data)
            self.db_connection.commit()
            cursor.close()
            # print("Updated Successfully....")
            return True

        except Error as e:
            print("Error updating appointment:", e)
            return False

    def cancelAppointment(self, appointmentId):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM appointment WHERE appointmentId = %s", (appointmentId,))
            appointment_exists = cursor.fetchone()
            if not appointment_exists:
                print("Appointment with ID", appointmentId, "does not exist.")
                cursor.close()
                return False
            query = "DELETE FROM appointment WHERE appointmentId = %s"
            cursor.execute(query, (appointmentId,))
            self.db_connection.commit()
            cursor.close()
            # print("Appointment Cancelled...")
            return True

        except Error as e:
            print("Error canceling appointment:", e)
            return False

    def isValidAppointment(self, appointment):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM patient WHERE patientId = %s", (appointment.get_patientId(),))
            patient_exists = cursor.fetchone()
            cursor.execute("SELECT * FROM doctor WHERE doctorId = %s", (appointment.get_doctorId(),))
            doctor_exists = cursor.fetchone()
            cursor.close()
            return patient_exists is not None and doctor_exists is not None
        except Error as e:
            print("Error validating appointment:", e)
            return False

    def hasAppointmentConflict(self, appointment):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM appointment WHERE doctorId = %s AND appointmentDate = %s",
                           (appointment.get_doctorId(), appointment.get_appointmentDate()))
            conflicting_appointments = cursor.fetchall()
            cursor.close()
        except Error as e:
            print("Error checking appointment conflict:", e)
            return False

    def showAllDoctors(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM doctor")
            doctors = cursor.fetchall()
            cursor.close()
            print("All Doctor Details:")
            for doctor in doctors:
                print(doctor)

        except Error as e:
            print("Error fetching doctor details:", e)

    def showAllPatients(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM patient")
            patients = cursor.fetchall()
            cursor.close()
            print("All Patient Details:")
            for patient in patients:
                print(patient)

        except Error as e:
            print("Error fetching patient details:", e)

    def showAllAppointments(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM appointment")
            appointments = cursor.fetchall()
            cursor.close()

            print("All Appointment Details:")
            for appointment in appointments:
                print(appointment)

        except Error as e:
            print("Error fetching appointment details:", e)
