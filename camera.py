import cv2
import mediapipe as mp
from mediapipe.tasks import python
import time
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from datetime import datetime, timedelta


# Inisialisasi variabel
gesture_name = "none"
gesture_score = 0
selected_letter = None
correct_count = {letter: 0 for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
incorrect_count = {letter: 0 for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
start_time = None

# Tkinter GUI Setup
root = tk.Tk()
root.title("Hand Gesture Recognition")
root.geometry("1000x800")
root.configure(bg='#F0F0F0')  # Set elegant dark background

# Style variables
button_bg = "#4CAF50"  # Button background (Green)
button_fg = "#FFFFFF"  # Button text color (White)
frame_bg = "#F0F0F0"   # Frame background (Light Grey)
status_fg = "#000000"  # Status text color (Black)
selected_letter_bg = "#8BC34A"  # Selected letter background (Light Green)
selected_letter_fg = "#000000"

# Frame for the progress tracker (correct/incorrect for each letter)
frame_progress = tk.Frame(root, bg=frame_bg, bd=5, relief=tk.RIDGE)
frame_progress.pack(pady=10, padx=10, side=tk.LEFT, fill=tk.Y)

# Progress labels
progress_labels = []
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    frame_letter = tk.Frame(frame_progress, bg=frame_bg)
    frame_letter.pack(fill=tk.X, padx=5, pady=3)
    
    lbl_letter = tk.Label(frame_letter, text=f"{letter}: ", font=('Helvetica', 12, 'bold'),
                          bg=frame_bg, fg=selected_letter_fg, width=3)
    lbl_letter.pack(side=tk.LEFT)
    
    lbl_correct = tk.Label(frame_letter, text="Correct: 0", font=('Helvetica', 12), 
                           bg=frame_bg, fg="#00FF00", width=12)
    lbl_correct.pack(side=tk.LEFT, padx=5)
    
    lbl_incorrect = tk.Label(frame_letter, text="Incorrect: 0", font=('Helvetica', 12),
                             bg=frame_bg, fg="#FF3333", width=12)
    lbl_incorrect.pack(side=tk.LEFT)
    
    progress_labels.append((lbl_correct, lbl_incorrect))

# Callback when a letter button is pressed
def select_letter(letter):
    global selected_letter
    selected_letter = letter
    lbl_selected_letter.config(text=f"Selected Letter: {letter}", bg=selected_letter_bg, fg=selected_letter_fg)
    lbl_status.config(text="Match Status: Waiting...", fg=status_fg)

# Frame for buttons
frame_buttons = tk.Frame(root, bg=frame_bg, bd=5, relief=tk.RIDGE)
frame_buttons.pack(pady=10, padx=10, fill=tk.X)

# Add buttons for A-Z
# Function to change button style when hovered over
def on_enter(event, btn):
    btn['background'] = '#EEEEEE'  # Light grey on hover
    btn['foreground'] = '#393E46'  # Dark grey text

def on_leave(event, btn):
    btn['background'] = button_bg  # Return to original color
    btn['foreground'] = button_fg

# Improved buttons for A-Z with rounded corners, hover effects, and spacing
rows = 2  # Tentukan berapa baris yang ingin Anda gunakan
cols = 13  # Jumlah kolom per baris (26 huruf, 13 per baris)

for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    button = tk.Button(frame_buttons, text=letter, width=3, font=('Helvetica', 14, 'bold'),
                       bg=button_bg, fg=button_fg, 
                       relief='flat',  # Flat design
                       activebackground='#32E0C4',  # Aqua when pressed
                       activeforeground='#000000',  # Black text when pressed
                       bd=2,  # Border thickness for a polished look
                       highlightthickness=0,
                       cursor="hand2",  # Change cursor to hand on hover
                       padx=10, pady=5)  # Padding for spacing and size

    # Apply rounded button effect
    button.config(borderwidth=0, highlightthickness=0)

    # Tentukan posisi tombol di dalam grid
    row = i // cols  # Baris dihitung dengan membagi index tombol dengan jumlah kolom
    col = i % cols   # Kolom dihitung dengan sisa bagi dari index tombol

    # Gunakan grid layout untuk menyusun tombol-tombol tersebut
    button.grid(row=row, column=col, padx=8, pady=8)

    # Bind hover effects
    button.bind("<Enter>", lambda e, btn=button: on_enter(e, btn))
    button.bind("<Leave>", lambda e, btn=button: on_leave(e, btn))

    # Set the command to select the letter
    button.config(command=lambda l=letter: select_letter(l))

# Display selected letter and status
lbl_selected_letter = tk.Label(root, text="Selected Letter: None", font=('Helvetica', 18, 'bold'),
                               bg=selected_letter_bg, fg=selected_letter_fg)
lbl_selected_letter.pack(pady=10)

lbl_status = tk.Label(root, text="Match Status: Waiting...", font=('Helvetica', 18, 'bold'), fg=status_fg, bg=frame_bg)
lbl_status.pack(pady=10)

# Timer label to display lesson duration
lbl_timer = tk.Label(root, text="Lesson Time: 00:00:00", font=('Helvetica', 18, 'bold'), fg=status_fg, bg=frame_bg)
lbl_timer.pack(pady=10)

# Frame for camera feed
frame_camera = tk.Frame(root, bg=frame_bg, bd=5, relief=tk.RIDGE)
frame_camera.pack(pady=10)

# OpenCV and Gesture Recognition setup
model_path = "gesture_recognizer.task"
base_options = python.BaseOptions(model_asset_path=model_path)
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Get Result Callback Function for Gesture Recognition
def get_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    global gesture_name, gesture_score
    if result is not None and any(result.gestures):
        for single_hand_gesture_data in result.gestures:
            gesture_name = single_hand_gesture_data[0].category_name
            gesture_score = single_hand_gesture_data[0].score

# Inisialisasi Gesture Recognizer
options = GestureRecognizerOptions(
    base_options=python.BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=get_result)
recognizer = GestureRecognizer.create_from_options(options)

# MediaPipe and OpenCV Setup
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.65,
    min_tracking_confidence=0.65)

# OpenCV Video Capture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
timestamp = 0

# FPS Calculation
prev_time = time.time()

def calculate_fps(prev_time):
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    return current_time, fps

# Timer Update
def update_timer():
    global start_time
    if start_time is None:
        start_time = datetime.now()
    
    elapsed_time = datetime.now() - start_time
    lbl_timer.config(text=f"Lesson Time: {str(elapsed_time).split('.')[0]}")
    
    # Call again after 1 second
    lbl_timer.after(1000, update_timer)

# Inisialisasi variabel baru
previous_gesture_name = None
incorrect_recorded = False  # Untuk mencatat apakah incorrect sudah direkam


# Update the camera feed
# Update the camera feed
def update_camera_feed():
    global prev_time, timestamp, previous_gesture_name, incorrect_recorded

    # Capture frame from camera
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        np_array = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Calculate FPS
        prev_time, fps = calculate_fps(prev_time)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                h, w, c = frame.shape
                draw_spec_landmark = mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
                draw_spec_connection = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS, draw_spec_landmark, draw_spec_connection)

                # Convert image for gesture recognition
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np_array)
                recognizer.recognize_async(mp_image, timestamp)
                timestamp += 1

        # Check if gesture matches the selected letter
        if selected_letter:
            if gesture_name == selected_letter:
                # Jika gesture benar
                if previous_gesture_name != gesture_name:  # Hanya hitung benar jika gesture berubah
                    correct_count[selected_letter] += 1
                    lbl_status.config(text=f"Match Status: Correct ({gesture_name})", fg="#00FF00")
                    incorrect_recorded = False  # Reset pencatatan salah
            else:
                # Jika gesture salah
                if previous_gesture_name != gesture_name:  # Hitung salah hanya jika gesture berubah
                    incorrect_count[selected_letter] += 1
                    lbl_status.config(text=f"Match Status: Incorrect ({gesture_name})", fg="#FF3333")
                    incorrect_recorded = True  # Tandai bahwa kita sudah mencatat ini

            # Update previous gesture name
            previous_gesture_name = gesture_name

            # Update progress labels
            index = ord(selected_letter) - 65
            progress_labels[index][0].config(text=f"Correct: {correct_count[selected_letter]}")
            progress_labels[index][1].config(text=f"Incorrect: {incorrect_count[selected_letter]}")

        # Convert image to Tkinter format
        img = Image.fromarray(frame)
        img = img.resize((640, 480))
        imgtk = ImageTk.PhotoImage(image=img)

        # Update the label with the new frame
        lbl_camera.imgtk = imgtk
        lbl_camera.config(image=imgtk)

    # Call this function again after a delay
    lbl_camera.after(10, update_camera_feed)


# Camera feed label
lbl_camera = tk.Label(frame_camera)
lbl_camera.pack()

# Start updating camera feed and timer
update_camera_feed()
update_timer()

# Start Tkinter event loop
root.mainloop()
