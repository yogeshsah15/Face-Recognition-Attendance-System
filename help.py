import tkinter as tk
from tkinter import messagebox, scrolledtext

class HelpWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Help - Facial Recognition Attendance System")
        self.root.geometry("600x400")
        self.root.configure(bg="white")

        # Heading
        title = tk.Label(self.root, text="📘 Help & User Guide", font=("Helvetica", 18, "bold"), bg="white", fg="#004080")
        title.pack(pady=20)

        # Help instructions (can be expanded)
        help_text = """
Welcome to the Facial Recognition Attendance System!

📌 Step-by-Step Guide:

1️⃣ Register Students:
   - Open the 'Student Details' module.
   - Fill in the required details (Name, Roll No., etc.).
   - Click 'Take Photo' to capture 50 facial images per student.

2️⃣ Train Data:
   - After registration, click 'Train Data'.
   - The system will process and save facial data in 'classifier.xml'.

3️⃣ Start Face Detection:
   - Click 'Face Detector' to activate real-time recognition.
   - Recognized students will be marked present automatically.

4️⃣ View Attendance:
   - Attendance will be saved in CSV format.
   - Open 'Attendance' module to review or export logs.

🛠 Troubleshooting Tips:
- Ensure the webcam is properly connected.
- Make sure 'photos/' folder contains student images before training.
- Train data again if new students are added.

ℹ️ For further assistance, contact the developer section.

Thank you for using our system!
        """

        scroll = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Segoe UI", 11), width=70, height=15, bg="#f7faff")
        scroll.insert(tk.END, help_text)
        scroll.config(state=tk.DISABLED)
        scroll.pack(padx=20, pady=10, fill="both", expand=True)

        # Exit button
        tk.Button(self.root, text="Close", font=("Helvetica", 12), bg="#004080", fg="white", command=self.root.destroy).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = HelpWindow(root)
    root.mainloop()
