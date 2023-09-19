import tkinter as tk
from datetime import datetime, timedelta
import winsound  # For Windows systems

# Create the main application window
app = tk.Tk()
app.title("Python Alarm Clock")
app.geometry("400x200")  # Set the window size

# Create and configure widgets
label = tk.Label(app, text="Set the alarm (HH:MM):")
label.pack()

entry = tk.Entry(app)
entry.pack()

set_button = tk.Button(app, text="Set Alarm", command=lambda: set_alarm(entry.get()))
set_button.pack()

# Function to set and play the alarm
def set_alarm(alarm_time_str):
    try:
        alarm_time = datetime.strptime(alarm_time_str, "%H:%M")
        current_time = datetime.now().strftime("%H:%M")

        if alarm_time < datetime.now():
            alarm_time += timedelta(days=1)  # Set the alarm for the next day if it's in the past

        label.config(text=f"Alarm set for: {alarm_time.strftime('%H:%M')}")

        def check_alarm():
            nonlocal alarm_time
            current_time = datetime.now().strftime("%H:%M")

            if current_time == alarm_time.strftime("%H:%M"):
                label.config(text="Time to wake up!")
                play_alarm()
            else:
                app.after(1000, check_alarm)  # Check again in 1 second

        check_alarm()

    except ValueError:
        label.config(text="Invalid time format. Use HH:MM")

# Function to play the alarm sound
def play_alarm_sound():
    try:
        winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1 second
    except Exception as e:
        label.config(text="Failed to play alarm sound")

# Function to play the alarm sound five times
def play_alarm():
    for _ in range(5):
        play_alarm_sound()
        app.update()

# Start the tkinter main loop
app.mainloop()
