import tkinter as tk
import requests
import time

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Test")
        
        self.text_label = tk.Label(root, text="", wraplength=400)
        self.text_label.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_text)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=10)

        self.start_time = None

    def start_test(self):
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = time.time()

        # Fetch text from the Flask backend
        response = requests.get("http://127.0.0.1:5000/get_text")
        data = response.json()
        self.text_label.config(text=data['text'])

    def check_text(self, event):
        typed_text = self.entry.get()
        correct_text = self.text_label.cget("text")

        # Calculate time taken
        if self.start_time:
            time_taken = time.time() - self.start_time

            if typed_text == correct_text:
                self.result_label.config(text=f"Correct! Time taken: {time_taken:.2f} seconds")
                self.submit_result(time_taken)
            else:
                self.result_label.config(text="Incorrect, please try again.")

    def submit_result(self, time_taken):
        # Send results to the Flask backend
        result_data = {"time_taken": time_taken}
        response = requests.post("http://127.0.0.1:5000/submit_result", json=result_data)
        print(response.json())

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
