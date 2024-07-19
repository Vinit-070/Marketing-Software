import tkinter as tk
from tkinter import ttk
import google.generativeai as genai
import pyperclip

class ContentWriterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Content Writer - Marketing Software By Vinit Patel")

        self.prompt_label = ttk.Label(root, text="Enter your topic:")
        self.prompt_label.grid(row=0, column=0, padx=10, pady=10)

        self.prompt_entry = ttk.Entry(root, width=50)
        self.prompt_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = ttk.Button(root, text="Generate Content", command=self.generate_content)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.copy_button = ttk.Button(root, text="Copy", command=self.copy_to_clipboard)
        self.copy_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.output_text = tk.Text(root, height=15, width=60)
        self.output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def generate_content(self):
        prom = self.prompt_entry.get()

        # Replace 'api-here' with your actual Google API key
        GOOGLE_API_KEY = 'AIzaSyBNEGGeG5YYBxngflhN_ByP9Y3IAv-X-L8'

        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-pro')

        response = model.generate_content(prom)

        content = response.text

        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, content)

    def copy_to_clipboard(self):
        content = self.output_text.get("1.0", "end-1c")
        pyperclip.copy(content)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContentWriterApp(root)
    root.mainloop()
