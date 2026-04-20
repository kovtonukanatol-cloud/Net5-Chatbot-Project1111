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


# --- CAOLAN: TASK 3 (GUI) ---
# Caolan, put your tkinter code here
