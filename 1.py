import tkinter as tk

# Story content
story_lines = [
    "On March 25th, during Holi, he proposed to me.",
    "I like him very much, more than words can say.",
    "I want to be with him forever, through every joy and every sorrow.",
    "He should never be sad, never and ever, because I will always be by his side.",
    "He is now sad and i hate everybody who made him sad , always be happy pandu",
    "And to show how much I care, here is my heart for you... ❤️"
]

# Function to update the label with the next or previous line
class StoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Our Love Story")
        self.index = 0

        # Label to display the story line
        self.label = tk.Label(root, text=story_lines[self.index], font=('Helvetica', 16), wraplength=400, width=50, height=5)
        self.label.pack(pady=20)

        # Next button
        self.next_button = tk.Button(root, text="Next", command=self.next_line, font=('Helvetica', 12))
        self.next_button.pack(side=tk.LEFT, padx=20)

        # Previous button
        self.prev_button = tk.Button(root, text="Previous", command=self.prev_line, font=('Helvetica', 12))
        self.prev_button.pack(side=tk.LEFT, padx=20)

    def next_line(self):
        if self.index < len(story_lines) - 1:
            self.index += 1
            self.label.config(text=story_lines[self.index])

    def prev_line(self):
        if self.index > 0:
            self.index -= 1
            self.label.config(text=story_lines[self.index])

# Create the main window and run the app
root = tk.Tk()
app = StoryApp(root)
root.mainloop()
