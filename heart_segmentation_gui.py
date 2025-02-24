#!/usr/bin/python3

import os
import sys
import tkinter as tk
from tkinter import filedialog, ttk
import SimpleITK as sitk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from platipy.imaging.projects.cardiac.run import run_hybrid_segmentation
from platipy.imaging import ImageVisualiser
from platipy.imaging.label.utils import get_com

class HeartSegmentationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Heart Segmentation Tool")
        
        # Add protocol handler for window closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Set minimum window size
        self.root.minsize(800, 600)
        
        # Configure grid weights
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        # Create main frame with padding
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.main_frame.grid_columnconfigure(1, weight=1)
        
        # Create control panel frame
        control_frame = ttk.LabelFrame(self.main_frame, text="Controls", padding="10")
        control_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N), padx=5, pady=5)
        
        # Input file selection
        ttk.Button(control_frame, text="Select Input File", width=20, command=self.select_file).grid(
            row=0, column=0, padx=(0,10), pady=5)
        self.file_label = ttk.Label(control_frame, text="No file selected")
        self.file_label.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Output directory selection
        ttk.Button(control_frame, text="Select Output Directory", width=20, command=self.select_output_dir).grid(
            row=1, column=0, padx=(0,10), pady=5)
        self.output_label = ttk.Label(control_frame, text="No directory selected")
        self.output_label.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Process button
        self.process_button = ttk.Button(control_frame, text="Process", width=20, command=self.process_image)
        self.process_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.process_button.state(['disabled'])
        
        # Create status frame
        status_frame = ttk.LabelFrame(self.main_frame, text="Status", padding="10")
        status_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Status label
        self.status_label = ttk.Label(status_frame, text="")
        self.status_label.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Create results frame
        results_frame = ttk.LabelFrame(self.main_frame, text="Results", padding="10")
        results_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
        results_frame.grid_columnconfigure(0, weight=1)
        results_frame.grid_rowconfigure(0, weight=1)
        
        # Result display
        self.figure_frame = ttk.Frame(results_frame)
        self.figure_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    def select_output_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_dir = directory
            self.output_label.config(text=directory)
            self.check_process_ready()
            
    def select_file(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("NIFTI files", "*.nii.gz"), ("All files", "*.*")]
        )
        if filepath:
            self.input_file = filepath
            self.file_label.config(text=os.path.basename(filepath))
            self.check_process_ready()
            
    def check_process_ready(self):
        if hasattr(self, 'input_file') and hasattr(self, 'output_dir'):
            self.process_button.state(['!disabled'])
        else:
            self.process_button.state(['disabled'])
            
    def process_image(self):
        if not hasattr(self, 'input_file') or not hasattr(self, 'output_dir'):
            return
            
        self.status_label.config(text="Processing...")
        self.process_button.state(['disabled'])
        
        self.root.after(100, self.run_segmentation)
        
    def run_segmentation(self):
        try:
            # Create output directory
            filename = os.path.splitext(os.path.splitext(os.path.basename(self.input_file))[0])[0]
            output_dir = os.path.join(self.output_dir, filename)
            os.makedirs(output_dir, exist_ok=True)
            
            # Read image
            self.status_label.config(text="Loading image...")
            self.root.update()
            test_image = sitk.ReadImage(self.input_file)
            
            # Process image
            self.status_label.config(text="Running heart segmentation...")
            self.root.update()
            auto_structures, _ = run_hybrid_segmentation(test_image)
            
            # Save segmentations
            self.status_label.config(text="Saving segmentation results...")
            self.root.update()
            for struct_name in auto_structures.keys():
                output_path = os.path.join(output_dir, f"{filename}_{struct_name}.nii.gz")
                sitk.WriteImage(auto_structures[struct_name], output_path)
            
            # Create visualization
            self.status_label.config(text="Generating visualization...")
            self.root.update()
            vis = ImageVisualiser(test_image, cut=get_com(auto_structures["Heart"]))
            vis.add_contour({struct: auto_structures[struct] for struct in auto_structures.keys()})
            fig = vis.show()
            
            # Adjust figure size
            fig.set_size_inches(10, 10)
            fig.tight_layout()
            
            # Save visualization
            plt.savefig(os.path.join(output_dir, f"{filename}_heart_visualization.png"))
            
            # Display in GUI
            for widget in self.figure_frame.winfo_children():
                widget.destroy()
            
            canvas = FigureCanvasTkAgg(fig, master=self.figure_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
            self.status_label.config(text=f"Processing complete. Results saved to {output_dir}")
            
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")
        
        finally:
            self.process_button.state(['!disabled'])

    def on_closing(self):
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HeartSegmentationGUI(root)
    root.mainloop()
    sys.exit(0)
