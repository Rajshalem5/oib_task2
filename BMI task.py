# Importing necessary modules
import tkinter as tk
from tkinter import messagebox


# Defining the BMIApp class for the GUI application
class BMIApp:
    def __init__(self, window):
        # Setting up window title and labels
        self.window = window
        self.window.title("BMI APP")
        self.l1 = tk.Label(window, text="Let's find out your health status.\n\nBody Mass Index(BMI)", fg="Blue",
                           font="18")
        self.l1.pack(pady=10)

        # Creating frames and input fields for weight and height
        self.f1 = tk.Frame(window)
        self.f1.pack()
        self.l2 = tk.Label(self.f1, text="Enter Weight(KG): ")
        self.l2.pack(side=tk.LEFT)
        self.weight = tk.Entry(self.f1, width=20)
        self.weight.pack(side=tk.LEFT, padx=10)

        self.f2 = tk.Frame(window)
        self.f2.pack()
        self.l3 = tk.Label(self.f2, text="Enter Height(cm): ")
        self.l3.pack(side=tk.LEFT, pady=10)
        self.height = tk.Entry(self.f2, width=20)
        self.height.pack(side=tk.LEFT, padx=10)

        # Adding a button to submit the entries
        self.sb = tk.Button(window, text="Submit", command=self.check)
        self.sb.pack(pady=10)

        # Setting the window size
        window.geometry('350x250')

    # Method to validate input and calculate BMI
    def check(self):
        weight = self.weight.get()
        height = self.height.get()
        if not weight or not height:
            messagebox.showwarning("Missing", "Enter all the entries")
            return
        self.calculate_bmi(weight, height)

    # Method to compute BMI and update the UI
    def calculate_bmi(self, weight, height):
        try:
            height_in_meters = float(height) / 100
        except ValueError:
            messagebox.showerror("Invalid Height", "Please enter a valid height in centimeters.")
            return

        bmi = float(weight) / (height_in_meters ** 2)
        bmi = round(bmi, 1)

        # Destroying previous UI elements
        self.l2.destroy()
        self.l3.destroy()
        self.weight.destroy()
        self.height.destroy()
        self.sb.destroy()

        # Determining BMI status and color
        color = "Red"
        if bmi < 18.5:
            message = "You are UNDERWEIGHT"
        elif 18.5 <= bmi < 25:
            message = "You are Normal Weighted"
            color = "Green"
        elif 25 <= bmi < 30:
            message = "You are OVERWEIGHT"
        else:
            message = "You are OBESITY"

        # Updating label with BMI result and status
        self.l1.config(text=f"Your BMI is {bmi}\n" + message, fg=color)
        self.l1.pack(pady=50)


# Main program entry point
if __name__ == "__main__":
    window = tk.Tk()
    app = BMIApp(window)
    window.mainloop()
