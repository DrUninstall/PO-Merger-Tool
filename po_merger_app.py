import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from polib import pofile, POFile

class POFileMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PO File Merger")
        self.root.geometry("450x300")
        self.root.configure(bg="#f5f6fa")  # Light gray background

        # Heading label
        self.heading = tk.Label(root, text="PO File Merger Tool", font=("Helvetica", 16, "bold"), fg="#db3d2d", bg="#f5f6fa")
        self.heading.pack(pady=10)

        # Folder selection label
        self.label = tk.Label(root, text="Select the root folder with culture folders:", fg="#636981", bg="#f5f6fa")
        self.label.pack(pady=5)

        # Folder selection button
        self.folder_path = tk.StringVar()
        self.select_button = tk.Button(root, text="Select Folder", command=self.select_folder, bg="#0078d4", fg="white", font=("Helvetica", 10, "bold"))
        self.select_button.pack(pady=5)

        # Checkbox for custom output path
        self.custom_output_var = tk.BooleanVar()
        self.custom_output_checkbox = tk.Checkbutton(root, text="Custom Output Path", variable=self.custom_output_var, bg="#f5f6fa", command=self.toggle_output_path)
        self.custom_output_checkbox.pack(pady=5)

        # Output path selection button
        self.output_path = tk.StringVar()
        self.output_button = tk.Button(root, text="Select Output Folder", command=self.select_output_folder, state="disabled", bg="#e6e8ef", fg="#2b2e4a", font=("Helvetica", 10, "bold"))
        self.output_button.pack(pady=5)

        # Feedback label for current process
        self.status_label = tk.Label(root, text="", font=("Helvetica", 10), fg="#636981", bg="#f5f6fa")
        self.status_label.pack(pady=5)

        # Progress bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=350, mode="determinate")
        self.progress.pack(pady=10)

        # Close button
        self.close_button = tk.Button(root, text="Close", command=self.root.quit, bg="#e6e8ef", fg="#2b2e4a", font=("Helvetica", 10, "bold"))
        self.close_button.pack(pady=10)

    def toggle_output_path(self):
        # Enable or disable output path selection based on checkbox
        if self.custom_output_var.get():
            self.output_button.config(state="normal")
        else:
            self.output_button.config(state="disabled")
            self.output_path.set("")  # Clear custom output path if checkbox is unchecked

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)
            self.merge_po_files_in_all_cultures(folder_selected)

    def select_output_folder(self):
        output_folder = filedialog.askdirectory()
        if output_folder:
            self.output_path.set(output_folder)

    def merge_po_files_in_all_cultures(self, root_directory):
        culture_folders = [f for f in os.listdir(root_directory) if os.path.isdir(os.path.join(root_directory, f))]
        self.progress["maximum"] = len(culture_folders)

        for idx, culture_folder in enumerate(culture_folders, 1):
            culture_path = os.path.join(root_directory, culture_folder)
            self.status_label.config(text=f"Processing: {culture_folder}")  # Display current culture folder
            self.merge_po_files(culture_path, culture_folder)
            self.progress["value"] = idx  # Update progress bar
            self.root.update_idletasks()  # Ensure smooth progress updates

        # Notify user of completion
        self.status_label.config(text="")  # Clear status label
        messagebox.showinfo("Completed", "All PO files have been merged successfully.")

    def merge_po_files(self, culture_path, culture_folder):
        merged_po = POFile()  # This will hold the merged entries

        # Walk through files in the culture directory
        for dirpath, _, files in os.walk(culture_path):
            for file_name in files:
                if file_name.endswith('.po'):
                    file_path = os.path.join(dirpath, file_name)
                    po = pofile(file_path)

                    for entry in po:
                        # Avoid duplicate entries by checking msgid
                        if not any(e.msgid == entry.msgid for e in merged_po):
                            merged_po.append(entry)

        # Determine output path and filename
        if self.custom_output_var.get() and self.output_path.get():
            # Use custom output folder and culture-prefixed filename
            merged_file_path = os.path.join(self.output_path.get(), f"{culture_folder}_merged.po")
        else:
            # Default to original culture folder
            merged_file_path = os.path.join(culture_path, 'merged.po')

        merged_po.save(merged_file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = POFileMergerApp(root)
    root.mainloop()
