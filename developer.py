from tkinter import *

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.title("Developer Info")
        self.root.geometry("400x200")

        Label(self.root, text="Developer:", font=("Arial", 14, "bold")).pack(pady=10)
        Label(self.root, text="Yogesh Kumar Sah", font=("Arial", 12)).pack()
        Label(self.root, text="Email: yogeshsah15@gmail.com").pack()
        Label(self.root, text="GitHub: github.com/yogeshsah15").pack()

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
