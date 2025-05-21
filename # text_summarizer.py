import tkinter as tk
from tkinter import scrolledtext, messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.tokenize import sent_tokenize
import nltk

# Download punkt tokenizer if not already
nltk.download('punkt')

def summarize_text(text, num_sentences=3):
    sentences = sent_tokenize(text)
    if len(sentences) <= num_sentences:
        return "Text is too short to summarize."

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(sentences)

    kmeans = KMeans(n_clusters=num_sentences, random_state=0)
    kmeans.fit(X)

    selected_sentences = []
    for i in range(num_sentences):
        cluster_idx = list(kmeans.labels_).index(i)
        selected_sentences.append(sentences[cluster_idx])

    summary = " ".join(selected_sentences)
    return summary

def on_summarize():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text to summarize.")
        return
    try:
        num = int(num_sentences_var.get())
        if num < 1:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Input Error", "Number of sentences must be a positive integer.")
        return

    summary = summarize_text(text, num)
    summary_output.config(state='normal')
    summary_output.delete("1.0", tk.END)
    summary_output.insert(tk.END, summary)
    summary_output.config(state='disabled')

# Create main window
root = tk.Tk()
root.title("Text Summarizer")
root.geometry("700x600")
root.resizable(False, False)

# Input label and textbox
tk.Label(root, text="Enter Text to Summarize:", font=("Arial", 14)).pack(pady=5)
text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=15, font=("Arial", 12))
text_input.pack(pady=5)

# Number of sentences input
frame = tk.Frame(root)
frame.pack(pady=10)
tk.Label(frame, text="Number of sentences:", font=("Arial", 12)).pack(side=tk.LEFT)
num_sentences_var = tk.StringVar(value="3")
num_entry = tk.Entry(frame, width=5, textvariable=num_sentences_var, font=("Arial", 12))
num_entry.pack(side=tk.LEFT, padx=5)

# Summarize button
summarize_btn = tk.Button(root, text="Summarize", command=on_summarize, font=("Arial", 12), bg="#4CAF50", fg="white", width=15)
summarize_btn.pack(pady=10)

# Summary output label and textbox (read-only)
tk.Label(root, text="Summary:", font=("Arial", 14)).pack(pady=5)
summary_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10, font=("Arial", 12))
summary_output.pack(pady=5)
summary_output.config(state='disabled')

# Start the GUI loop
root.mainloop()
