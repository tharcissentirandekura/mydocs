import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("Moving Circle")

# Create a Canvas widget
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

# Circle properties
x = 200  # Initial x-coordinate
y = 200  # Initial y-coordinate
radius = 50

# Function to draw the circle at the current position
def draw_circle():
    canvas.delete("circle")  # Remove any existing circle
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="blue", tags="circle")

# Function to update the circle's position
def update_position(new_x, new_y):
    global x, y
    x = new_x
    y = new_y
    draw_circle()

# Initial draw
draw_circle()

# Move the circle when arrow keys are pressed
def on_key_press(event):
    move_distance = 10

    if event.keysym == "Up":
        update_position(x, y - move_distance)
    elif event.keysym == "Down":
        update_position(x, y + move_distance)
    elif event.keysym == "Left":
        update_position(x - move_distance, y)
    elif event.keysym == "Right":
        update_position(x + move_distance, y)

# Bind the key press event to the window
window.bind("<KeyPress>", on_key_press)
window.focus_set()

# Start the Tkinter event loop
window.mainloop()