import tkinter as tk
import threading

class TextClearerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Write Right Away...Or Else!")

        self.text_widget = tk.Text(self.root)
        self.text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.timer_thread = None
        self.delay = 5  # 5 seconds of inactivity

        self.text_widget.bind("<Key>", self.reset_timer)
        self.start_timer()

    def start_timer(self):
        self.stop_timer()  # Stop any ongoing timers
        self.timer_thread = threading.Timer(self.delay, self.clear_text)
        self.timer_thread.start()

    def stop_timer(self):
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.cancel()

    def reset_timer(self, event):
        self.start_timer()

    def clear_text(self):
        self.text_widget.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextClearerApp(root)
    root.mainloop()
