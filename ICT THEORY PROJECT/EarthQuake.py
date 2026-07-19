import time

print("===========================================")
print("         EARTHQUAKE SIMULATION SYSTEM       ")
print("===========================================")

# Function to get intensity based on magnitude
def get_intensity(mag):
    if mag < 2.0:
        return "Micro"
    elif mag < 4.0:
        return "Minor"
    elif mag < 5.0:
        return "Light"
    elif mag < 6.0:
        return "Moderate"
    elif mag < 7.0:
        return "Strong"
    elif mag < 8.0:
        return "Major"
    else:
        return "Great"

# Function to get alert level
def get_alert_level(mag):
    if mag < 4.0:
        return "Green"
    elif mag < 6.0:
        return "Yellow"
    elif mag < 7.0:
        return "Orange"
    else:
        return "Red"

# Safety tips dictionary
safety_tips = {
    "Green": "Stay calm. No action required.",
    "Yellow": "Stay away from windows and avoid elevators.",
    "Orange": "Drop, cover, hold. Move to an open area.",
    "Red": "Evacuate immediately. Stay clear of buildings."
}

# Function to get damage estimation
def get_damage(mag):
    if mag < 4.0:
        return "No damage expected."
    elif mag < 5.0:
        return "Very slight damage to weak structures."
    elif mag < 6.0:
        return "Some damage to poorly built buildings."
    elif mag < 7.0:
        return "Moderate to major damage in populated areas."
    else:
        return "Severe destruction and collapse of structures."

# Step 1: INPUTS
city = input("Enter city name: ")
magnitude = float(input("Enter magnitude: "))
depth = float(input("Enter depth (km): "))

# Step 2: PROCESSING
intensity = get_intensity(magnitude)
alert_level = get_alert_level(magnitude)
safety_tip = safety_tips[alert_level]
damage = get_damage(magnitude)

# Risk score (simple formula for students)
risk_score = (magnitude * 10) - (depth * 0.3)

# Step 3: OUTPUT
print("\n\n======= EARTHQUAKE REPORT =======")
print("City:", city)
print("Magnitude:", magnitude)
print("Depth:", depth, "km")
print("Intensity Level:", intensity)
print("Alert Level:", alert_level)
print("Safety Tip:", safety_tip)
print("Damage Estimate:", damage)
print("Risk Score:", round(risk_score, 2))
print("Report Generated At:", time.ctime())
print("===================================")
print("      END OF EARTHQUAKE REPORT      ")
print("===================================")
