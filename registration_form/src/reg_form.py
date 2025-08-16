import tkinter as tkinder
from tkinter import messagebox
import json
import base64

class StudentRegistrationForm:
     def __init__(self, root):
         self.root = root
         self.root.title("Student Registration Form")

         
         self.first_name_label = tkinder.Label(root, text="First Name:")
         self.first_name_label.grid(row=0, column=0)
         self.first_name_entry = tkinder.Entry(root)
         self.first_name_entry.grid(row=0, column=1)

         self.last_name_label = tkinder.Label(root, text="Last Name:")
         self.last_name_label.grid(row=1, column=0)
         self.last_name_entry = tkinder.Entry(root)
         self.last_name_entry.grid(row=1, column=1)

         self.class_label = tkinder.Label(root, text="Class:")
         self.class_label.grid(row=2, column=0)
         self.class_entry = tkinder.Entry(root)
         self.class_entry.grid(row=2, column=1)

         self.phone_number_label = tkinder.Label(root, text="Phone Number:")
         self.phone_number_label.grid(row=3, column=0)
         self.phone_number_entry = tkinder.Entry(root)
         self.phone_number_entry.grid(row=3, column=1)

         self.adhar_no_label = tkinder.Label(root, text="Adhar No:")
         self.adhar_no_label.grid(row=4, column=0)
         self.adhar_no_entry = tkinder.Entry(root)
         self.adhar_no_entry.grid(row=4, column=1)

         self.register_button = tkinder.Button(root, text="Register", command=self.register_student)
         self.register_button.grid(row=5, column=0, columnspan=2)

         self.display_button = tkinder.Button(root, text="Display Registered Students", command=self.display_registered_students)
         self.display_button.grid(row=6, column=0, columnspan=2)
     def register_student(self):
         first_name = self.first_name_entry.get()
         last_name = self.last_name_entry.get()
         class_name = self.class_entry.get()
         phone_number = self.phone_number_entry.get()
         adhar_no = self.adhar_no_entry.get()

         if not first_name or not last_name or not class_name or not phone_number or not adhar_no:
            messagebox.showerror("Error", "All fields are required")
            return
         if not phone_number.isdigit() or len(phone_number) != 10:
            messagebox.showerror("Error", "Phone number should be 10 digits only")
            return
         if not adhar_no.isdigit() or len(adhar_no) != 12:
            messagebox.showerror("Error", "aadhar should be 12 digits only")
            return
         student_datas = {
                 "first_name": first_name,
                "last_name": last_name,
                 "class": class_name,
                 "phone_number": phone_number,
                 "adhar_no": adhar_no
         }
         # Encode data using base64 instead of encryption
         encoded_data = base64.b64encode(json.dumps(student_datas).encode())
         with open("db.json", "ab") as f:
             f.write(encoded_data + b"\n")
             messagebox.showinfo("Successfully Data stored.")

     def display_registered_students(self):
         try:
             with open("db.json", "rb") as f:
                 encoded_data = f.readlines()

             decrypted_data = []
             for data in encoded_data:
                 try:
                     # Decode base64 data and parse JSON
                     decoded = base64.b64decode(data.strip())
                     decrypted_data.append(json.loads(decoded.decode()))
                 except Exception:
                     # Skip lines that can't be decoded/parsed
                     continue

             display_window = tkinder.Toplevel(self.root)
             display_window.title("Registered Students")

             frame = tkinder.Frame(display_window)
             frame.pack()

             tkinder.Label(frame, text="Name").grid(row=0, column=0)
             tkinder.Label(frame, text="Class").grid(row=0, column=1)
             tkinder.Label(frame, text="Phone Number").grid(row=0, column=2)
             tkinder.Label(frame, text="Adhar No").grid(row=0, column=3)

             for i, student in enumerate(decrypted_data):
                 tkinder.Label(frame, text=f"{student['first_name']} {student['last_name']}").grid(row=i+1, column=0)
                 tkinder.Label(frame, text=student['class']).grid(row=i+1, column=1)
                 tkinder.Label(frame, text=student['phone_number']).grid(row=i+1, column=2)
                 tkinder.Label(frame, text=student['adhar_no']).grid(row=i+1, column=3)

         except FileNotFoundError:
             messagebox.showerror("Error", "No registered students found")
             

if __name__ == "__main__":
    root = tkinder.Tk()
    app = StudentRegistrationForm(root)
    root.mainloop()