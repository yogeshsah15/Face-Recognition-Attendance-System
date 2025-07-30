from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import subprocess
import sys

class Facial_recognition_attendance_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Facial Recognition Attendance System")

        # ========== Header Images ==========
        img = Image.open("images/1grp.jpg").resize((420, 110), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=420, height=110)

        img1 = Image.open("images/1grp.jpg").resize((420, 110), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=420, y=0, width=420, height=110)

        img2 = Image.open("images/1grp.jpg").resize((440, 110), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=840, y=0, width=440, height=110)

        # ========== Background Image ==========
        img3 = Image.open("images/bgrd.jpg").resize((1280, 610), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=110, width=1280, height=610)

        # Title
        title_lbl = Label(bg_img, text="FACIAL RECOGNITION ATTENDANCE SYSTEM", 
                          font=("times new roman", 30, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1280, height=45)

        # ========== Button Functions ==========
        def run_script(script_name):
            subprocess.Popen([sys.executable, script_name])

        def open_student_details():
            run_script("studentdetails.py")

        def open_face_detector():
            run_script("face_recognition.py")

        def open_attendance():
            run_script("attendance.py")

        def open_help():
            run_script("help.py")

        def open_train_data():
            run_script("train.py")

        def open_photos():
            folder = "photos"
            if not os.path.exists(folder):
                os.makedirs(folder)
            os.startfile(folder)

        def open_developer():
            run_script("developer.py")

        def exit_app():
            self.root.quit()

        # ========== Create Button Function ==========
        def create_button(image_path, x, y, text, command=None):
            img = Image.open(image_path)
            img = img.resize((180, 180), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            btn = Button(bg_img, image=photo, cursor="hand2", command=command)
            btn.image = photo  # keep a reference
            btn.place(x=x, y=y, width=180, height=180)
            btn_lbl = Button(bg_img, text=text, cursor="hand2", font=("times new roman", 12, "bold"),
                             bg="black", fg="white", command=command)
            btn_lbl.place(x=x, y=y+190, width=180, height=35)

        # ========== Create All Buttons ==========
        create_button("images/studentdetails.webp", 150, 60, "Student Details", open_student_details)
        create_button("images/Facedet.png", 370, 60, "Face Detector", open_face_detector)
        create_button("images/attendance.jpg", 590, 60, "Attendance", open_attendance)
        create_button("images/help.jpg", 810, 60, "Help", open_help)
        create_button("images/train.jpg", 150, 300, "Train Data", open_train_data)
        create_button("images/photos.jpg", 370, 300, "Photos", open_photos)
        create_button("images/developer.png", 590, 300, "Developer", open_developer)
        create_button("images/exit.png", 810, 300, "Exit", exit_app)


if __name__ == "__main__":
    root = Tk()
    obj = Facial_recognition_attendance_system(root)
    root.mainloop()
