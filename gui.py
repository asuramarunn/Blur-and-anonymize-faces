import tkinter as tk
from tkinter import filedialog, ttk
from ultis import process_image, process_video, stream_from_camera


class FaceAnonymizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Blur and Anonymization")

        # Blur strength trackbar
        self.blur_strength = tk.IntVar(value=15)

        # Method combo box (Blur, Pixelize, Replace with Icon)
        self.method = tk.StringVar(value='Blur')

        # Icon path for "Replace with Icon" method
        self.icon_path = None

        # Buttons for different modes
        self.image_button = ttk.Button(self.root, text="Upload Image", command=self.load_image)
        self.image_button.pack(pady=5)

        self.video_button = ttk.Button(self.root, text="Upload Video", command=self.load_video)
        self.video_button.pack(pady=5)

        self.camera_button = ttk.Button(self.root, text="Start Camera Stream", command=self.stream_camera)
        self.camera_button.pack(pady=5)

        # Trackbar for blur strength
        self.trackbar_label = ttk.Label(self.root, text="Blur Strength")
        self.trackbar_label.pack(pady=5)

        self.trackbar = ttk.Scale(self.root, from_=1, to=30, variable=self.blur_strength)
        self.trackbar.pack(pady=5)

        self.method_label = ttk.Label(self.root, text="Anonymization Method")
        self.method_label.pack(pady=5)

        self.method_combo = ttk.Combobox(self.root, textvariable=self.method, values=['Blur', 'Pixelize', 'Replace with Icon'])
        self.method_combo.pack(pady=5)

        self.icon_button = ttk.Button(self.root, text="Upload Icon for Replacement", command=self.load_icon)
        self.icon_button.pack(pady=5)

    def load_image(self):
        image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if image_path:
            if self.method.get() == 'Replace with Icon' and not self.icon_path:
                tk.messagebox.showerror("Error", "Please upload an icon for face replacement.")
            else:
                process_image(image_path, self.method.get(), self.blur_strength.get(), self.icon_path)

    def load_video(self):
        video_path = filedialog.askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
        if video_path:
            if self.method.get() == 'Replace with Icon' and not self.icon_path:
                tk.messagebox.showerror("Error", "Please upload an icon for face replacement.")
            else:
                process_video(video_path, self.method.get(), self.blur_strength.get(), self.icon_path)

    def stream_camera(self):
        if self.method.get() == 'Replace with Icon' and not self.icon_path:
            tk.messagebox.showerror("Error", "Please upload an icon for face replacement.")
        else:
            stream_from_camera(self.method.get(), self.blur_strength.get(), self.icon_path)

    def load_icon(self):
        icon_path = filedialog.askopenfilename(title="Select an Icon", filetypes=[("Image Files", "*.png")])
        if icon_path:
            self.icon_path = icon_path
        
        return print(icon_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceAnonymizationApp(root)
    root.mainloop()
