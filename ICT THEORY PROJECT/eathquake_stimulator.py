# earthquake_simulator.py
import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime

# ---------------------------
# Helper functions
# ---------------------------
def generate_earthquake():
    """
    Generate realistic-looking random earthquake data.
    Returns a dictionary with magnitude, depth, time, intensity, level, and tip.
    """
    # Magnitude between 2.0 and 7.5 (float with 1 decimal)
    magnitude = round(random.uniform(2.0, 7.5), 1)

    # Depth between 5 and 200 km
    depth = random.randint(5, 200)

    # Time - current time string
    time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Decide intensity and alert level based on magnitude (simple scale)
    if magnitude < 3.5:
        intensity = "Minor"
        level = "Green"
        tip = "No action needed. Stay aware."
    elif 3.5 <= magnitude < 5.0:
        intensity = "Light"
        level = "Yellow"
        tip = "Check secure items. Avoid tall buildings temporarily."
    elif 5.0 <= magnitude < 6.5:
        intensity = "Moderate"
        level = "Orange"
        tip = "Take cover under sturdy furniture. Move away from windows."
    else:
        intensity = "Severe"
        level = "Red"
        tip = "Evacuate if instructed. Stay in open area if outside."

    return {
        "magnitude": magnitude,
        "depth": depth,
        "time": time_str,
        "intensity": intensity,
        "level": level,
        "tip": tip
    }

# ---------------------------
# GUI functions
# ---------------------------
def simulate():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input required", "Please enter a city or location.")
        return

    data = generate_earthquake()

    # Update labels
    city_val_label.config(text=city.title())
    mag_val_label.config(text=str(data["magnitude"]))
    depth_val_label.config(text=f"{data['depth']} km")
    time_val_label.config(text=data["time"])
    intensity_val_label.config(text=data["intensity"])
    tip_text.config(state="normal")
    tip_text.delete("1.0", tk.END)
    tip_text.insert(tk.END, data["tip"])
    tip_text.config(state="disabled")

    # Color coding frame based on alert level
    level = data["level"]
    if level == "Green":
        color = "#b6f5b6"  # light green
    elif level == "Yellow":
        color = "#fff6b6"  # light yellow
    elif level == "Orange":
        color = "#ffd9a6"  # light orange
    else:
        color = "#ffb6b6"  # light red

    alert_frame.config(bg=color)
    # Also update small label backgrounds to match (for neat look)
    for lbl in [city_label, mag_label, depth_label, time_label, intensity_label]:
        lbl.config(bg=color)
    for val in [city_val_label, mag_val_label, depth_val_label, time_val_label, intensity_val_label]:
        val.config(bg=color)

def clear_all():
    city_entry.delete(0, tk.END)
    city_val_label.config(text="-")
    mag_val_label.config(text="-")
    depth_val_label.config(text="-")
    time_val_label.config(text="-")
    intensity_val_label.config(text="-")
    tip_text.config(state="normal")
    tip_text.delete("1.0", tk.END)
    tip_text.config(state="disabled")
    alert_frame.config(bg=main_bg)
    for lbl in [city_label, mag_label, depth_label, time_label, intensity_label]:
        lbl.config(bg=main_bg)
    for val in [city_val_label, mag_val_label, depth_val_label, time_val_label, intensity_val_label]:
        val.config(bg=main_bg)

def about():
    messagebox.showinfo("About", "Mini Earthquake Alert Simulator\nBuilt with Python + Tkinter\nEducational simulator only (no real data).")

# ---------------------------
# GUI layout
# ---------------------------
root = tk.Tk()
root.title("Mini Earthquake Alert Simulator")
root.geometry("520x380")
root.resizable(False, False)

main_bg = root.cget("bg")

# Title
title = tk.Label(root, text="Mini Earthquake Alert Simulator", font=("Helvetica", 14, "bold"))
title.pack(pady=8)

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=6)

city_label_in = tk.Label(input_frame, text="Enter City / Location:")
city_label_in.grid(row=0, column=0, padx=4, pady=4, sticky="e")

city_entry = tk.Entry(input_frame, width=30)
city_entry.grid(row=0, column=1, padx=4, pady=4)

simulate_btn = tk.Button(input_frame, text="Simulate Alert", command=simulate)
simulate_btn.grid(row=0, column=2, padx=6)

clear_btn = tk.Button(input_frame, text="Clear", command=clear_all)
clear_btn.grid(row=0, column=3, padx=6)

about_btn = tk.Button(input_frame, text="About", command=about)
about_btn.grid(row=0, column=4, padx=6)

# Alert display frame
alert_frame = tk.Frame(root, bd=2, relief="groove", padx=8, pady=8)
alert_frame.pack(padx=12, pady=10, fill="x")

# Labels in alert frame (left = field, right = value)
city_label = tk.Label(alert_frame, text="City:", width=12, anchor="w")
city_label.grid(row=0, column=0, sticky="w")
city_val_label = tk.Label(alert_frame, text="-", width=20, anchor="w")
city_val_label.grid(row=0, column=1, sticky="w")

mag_label = tk.Label(alert_frame, text="Magnitude:", width=12, anchor="w")
mag_label.grid(row=1, column=0, sticky="w")
mag_val_label = tk.Label(alert_frame, text="-", width=20, anchor="w")
mag_val_label.grid(row=1, column=1, sticky="w")

depth_label = tk.Label(alert_frame, text="Depth:", width=12, anchor="w")
depth_label.grid(row=2, column=0, sticky="w")
depth_val_label = tk.Label(alert_frame, text="-", width=20, anchor="w")
depth_val_label.grid(row=2, column=1, sticky="w")

time_label = tk.Label(alert_frame, text="Time:", width=12, anchor="w")
time_label.grid(row=3, column=0, sticky="w")
time_val_label = tk.Label(alert_frame, text="-", width=20, anchor="w")
time_val_label.grid(row=3, column=1, sticky="w")

intensity_label = tk.Label(alert_frame, text="Intensity:", width=12, anchor="w")
intensity_label.grid(row=4, column=0, sticky="w")
intensity_val_label = tk.Label(alert_frame, text="-", width=20, anchor="w")
intensity_val_label.grid(row=4, column=1, sticky="w")

# Safety tips box
tip_frame = tk.Frame(root)
tip_frame.pack(pady=8, padx=12, fill="x")

tip_label = tk.Label(tip_frame, text="Safety Tip:", anchor="w")
tip_label.pack(anchor="w")

tip_text = tk.Text(tip_frame, height=3, state="disabled")
tip_text.pack(fill="x")

# Footer
footer = tk.Label(root, text="Note: This is a simulator. It does NOT use real earthquake data.", font=("Helvetica", 8))
footer.pack(side="bottom", pady=6)

root.mainloop()
