class Staff:

    def __init__(self,name,id):

        self.name=name

        self.id=id

class Doctor(Staff):

    def __init__(self, name, id,specialization,consultation_fee):

        super().__init__(name, id)

        self.specialization=specialization

        self.consultation_fee=consultation_fee

    def display_doctor(self):

        print(self.name,self.id,self.specialization,self.consultation_fee)
    
    def earning(self,patient_no):

        self.patients_no=patient_no

        print("earning",self.consultation_fee*self.patients_no)

doctor_instance=Doctor("ravi",221,"cardiology",500)

doctor_instance.display_doctor()
doctor_instance.earning(5)
