# --- TASK 2: Anatolii Kovtoniuk ---
def clean_input(text):
    try:
        # checking if text is actually text
        if text is None or not isinstance(text, str):
            return ""
            
        # strip spaces and lowercase
        res = text.strip().lower()
        return res
        
    except Exception as e:
        # John Pettey wants error handling here
        print("Error:", e)
        return ""


# --- FRANKLIN: TASK 1 (KNOWLEDGE BASE) ---
# Franklin, put your dict and logic here
answers = {
    "password": "Click 'Forgot Password' and follow the steps sent to your email.",
    "wifi": "Restart WiFi or router. Check airplane mode.",
    "slow": "Close apps and restart. Check Task Manager.",
    "bsod": "Restart. If it continues, update drivers.",
    "battery": "Check Lenovo Vantage for battery health and limits.",
    "charge": "Check charger and power port.",
    "driver": "Update drivers using Lenovo Vantage.",
    "vantage": "Use it for updates and system checks.",
    "heat": "Clear vents and avoid soft surfaces.",
    "fan": "Close heavy apps. Device may be overheating.",
    "screen": "Restart or test with external display.",
    "keyboard": "Reconnect or update drivers.",
    "touchpad": "Enable with Fn key or settings.",
    "usb": "Try another port or restart.",
    "audio": "Check volume and output device.",
    "camera": "Check permissions in settings.",
    "bluetooth": "Turn off/on and reconnect.",
    "update": "Install updates in settings or Vantage.",
    "storage": "Delete unused files or apps.",
    "reset": "Use Windows reset in settings.",
    "printer": "Check connection, restart printer, and install driver.",
    "network": "Restart router and run network troubleshooter.",
    "dns": "Flush DNS or use Google DNS.",
    "ip": "Release and renew IP using ipconfig commands.",
    "login": "Verify credentials or reset password.",
    "vpn": "Reconnect VPN or check settings.",
    "malware": "Run a full antivirus scan.",
    "disk": "Run disk cleanup and check disk health.",
    "boot": "Check BIOS boot order and startup devices.",
    "app": "Update or reinstall the application."
}

# --- CAOLAN: TASK 3 (GUI) ---
# Caolan, put your tkinter code here
