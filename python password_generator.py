import random
import string
import os
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12):
    """
    Generate a secure password with a combination of uppercase, lowercase, numbers, and special characters.

    Args:
        length (int): The desired length of the password. Must be at least 12.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If the length is less than 12.
    """
    if length < 12:
        raise ValueError("Password length must be at least 12 characters.")

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password contains at least one character from each pool
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill the rest of the password length with random choices from all pools
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def save_password(password, filename="passwords.txt"):
    """
    Save the password to a file in the same directory as the program.

    Args:
        password (str): The password to save.
        filename (str): The file to save the password in.
    """
    # Ensure the file is in the same directory as the program
    file_path = os.path.join(os.path.dirname(__file__), filename)

    # Open the file in append mode and write the password
    with open(file_path, "a") as file:
        file.write(password + "\n")
    messagebox.showinfo("Success", f"Password saved to {file_path}")

def generate_and_display_password():
    """
    Generate a password based on the user input and display it in the GUI.
    """
    try:
        length = int(length_entry.get())
        if length < 12:
            messagebox.showerror("Error", "Password length must be at least 12 characters.")
            return
        password = generate_password(length)
        password_display.delete(0, tk.END)
        password_display.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")

def save_password_from_gui():
    """
    Save the displayed password to a file.
    """
    password = password_display.get()
    if not password:
        messagebox.showerror("Error", "No password to save. Generate a password first.")
        return
    save_password(password)

# Create the main GUI window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.grid(row=0, column=0)

# Input for password length
tk.Label(frame, text="Enter password length (minimum 12):").grid(row=0, column=0, sticky="w", pady=5)
length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1, pady=5)

# Buttons for generating and saving passwords
button_frame = tk.Frame(frame, pady=10)
button_frame.grid(row=1, column=0, columnspan=2)

generate_button = tk.Button(button_frame, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=0, column=0, padx=5)

save_button = tk.Button(button_frame, text="Save Password", command=save_password_from_gui)
save_button.grid(row=0, column=1, padx=5)

# Display for generated password
tk.Label(frame, text="Generated Password:").grid(row=2, column=0, sticky="w", pady=5)
password_display = tk.Entry(frame, width=40)
password_display.grid(row=2, column=1, pady=5)

# Start the GUI event loop
root.mainloop()