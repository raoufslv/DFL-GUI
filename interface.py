import shutil
import threading
import tkinter as tk
import os
import subprocess
from tkinter import filedialog
import tkinter.messagebox as msg
import time





# create an interface to execute bat files by clicking on buttons 
class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Interface")
        self.master.geometry("900x665")
        self.master.resizable(True, True)
        self.master.config(bg="gray")
        
        self.status_text = tk.StringVar()
        self.status_text.set("Status: ")
        self.status = tk.Label(self.master, textvariable=self.status_text, font=("Arial", 12), bg="gray", fg="white")
        self.status.place(x=10, y=630)

        
        # title of the interface with  white color
        self.title = tk.Label(self.master, text="DeepFaceLab", font=("Arial", 32), bg="gray", fg="white")
        self.title.place(x=320, y=10)
        
        # draw a line to separate the title from the buttons and a text in the middle
        self.line = tk.Canvas(self.master, width=350, height=0, bg="white")
        self.line.place(x=0, y=85)
        self.line = tk.Canvas(self.master, width=350, height=0, bg="white")
        self.line.place(x=550, y=85)
        
        # text in the middle of the line with light font
        self.text = tk.Label(self.master, text="Videos Selection", font=("Arial", 16), bg="gray", fg="light gray")
        self.text.place(x=370, y=70)
        
        self.choose_Video_Src = tk.Button(self.master, text="Source Video", command=self.choose_Video_Src, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.choose_Video_Src.place(x=100, y=115)
        
        self.choose_Video_Dst = tk.Button(self.master, text="Destination Video", command=self.choose_Video_Dst, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.choose_Video_Dst.place(x=600, y=115)
        
        # draw a line to separate the title from the buttons and a text in the middle
        self.line = tk.Canvas(self.master, width=350, height=0, bg="white")
        self.line.place(x=0, y=180)
        self.line = tk.Canvas(self.master, width=350, height=0, bg="white")
        self.line.place(x=550, y=180)
        
        # text in the middle of the line with light font
        self.text = tk.Label(self.master, text="Images Extraction", font=("Arial", 16), bg="gray", fg="light gray")
        self.text.place(x=370, y=165)
        
        self.extract_images_Src = tk.Button(self.master, text="Source Video", command=self.extract_images_Src, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.extract_images_Src.place(x=100, y=210)
        
        self.extract_images_dst = tk.Button(self.master, text="Destination Video", command=self.extract_images_dst, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.extract_images_dst.place(x=600, y=210)
        
        
        # draw a line to separate the title from the buttons and a text in the middle
        self.line = tk.Canvas(self.master, width=350, height=0, bg="white")
        self.line.place(x=0, y=275)
        self.line = tk.Canvas(self.master, width=350, height=0, bg="white")
        self.line.place(x=550, y=275)
        
        # text in the middle of the line with light font
        self.text = tk.Label(self.master, text="Faces Extraction", font=("Arial", 16), bg="gray", fg="light gray")
        self.text.place(x=370, y=260)
        
        self.extract_face_src = tk.Button(self.master, text="Source Video", command=self.extract_face_src, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.extract_face_src.place(x=100, y=305)
        
        self.extract_face_dst = tk.Button(self.master, text="Destination Video", command=self.extract_face_dst, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.extract_face_dst.place(x=600, y=305)
        
        
        
        # draw a line to separate the title from the buttons and a text in the middle
        self.line = tk.Canvas(self.master, width=390, height=0, bg="white")
        self.line.place(x=0, y=370)
        self.line = tk.Canvas(self.master, width=390, height=0, bg="white")
        self.line.place(x=510, y=370)
        
        # text in the middle of the line with light font
        self.text = tk.Label(self.master, text="Training", font=("Arial", 16), bg="gray", fg="light gray")
        self.text.place(x=410, y=355)
        
        self.Train_AMP = tk.Button(self.master, text="Train AMP", command=self.Train_AMP, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.Train_AMP.place(x=100, y=400)
        
        self.Train_Quick96 = tk.Button(self.master, text="Train Quick96", command=self.Train_Quick96, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.Train_Quick96.place(x=350, y=400)
        
        self.Train_SAE_HD = tk.Button(self.master, text="Train SAEHD", command=self.Train_SAE_HD, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.Train_SAE_HD.place(x=600, y=400)
        
        
        
        
        # draw a line to separate the title from the buttons and a text in the middle
        self.line = tk.Canvas(self.master, width=390, height=0, bg="white")
        self.line.place(x=0, y=465)
        self.line = tk.Canvas(self.master, width=390, height=0, bg="white")
        self.line.place(x=510, y=465)
        
        # text in the middle of the line with light font
        self.text = tk.Label(self.master, text="Merging", font=("Arial", 16), bg="gray", fg="light gray")
        self.text.place(x=410, y=450)
        
        self.Merge_AMP = tk.Button(self.master, text="Merge AMP", command=self.Merge_AMP, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.Merge_AMP.place(x=100, y=495)
        
        self.Merge_Quick96 = tk.Button(self.master, text="Merge Quick96", command=self.Merge_Quick96, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.Merge_Quick96.place(x=350, y=495)
        
        self.Merge_SAE_HD = tk.Button(self.master, text="Merge SAEHD", command=self.Merge_SAE_HD, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.Merge_SAE_HD.place(x=600, y=495)
        
        
        
        
        # draw a line to separate the title from the buttons and a text in the middle
        self.line = tk.Canvas(self.master, width=350, height=0, bg="white")
        self.line.place(x=0, y=560)
        self.line = tk.Canvas(self.master, width=350, height=0, bg="white")
        self.line.place(x=550, y=560)
        
        # text in the middle of the line with light font
        self.text = tk.Label(self.master, text="Export & Reset", font=("Arial", 16), bg="gray", fg="light gray")
        self.text.place(x=370, y=545)
        
        self.Export_video = tk.Button(self.master, text="Export Video", command=self.Export_video, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.Export_video.place(x=100, y=590)
        
        self.clear_workspace = tk.Button(self.master, text="Clear Workspace", command=self.clear_workspace, bg="orange", fg="black", font=("Arial", 18), relief="groove", bd=0, width=15, height=1, borderwidth=0, border=0, highlightthickness=0, activebackground="orange", activeforeground="black", cursor="hand2", overrelief="groove", padx=0, pady=0)
        self.clear_workspace.place(x=600, y=590)






    def choose_Video_Dst(self):
        root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("video files", "*.mp4;*.mkv;*.avi"), ("all files", "*.*")))
        if root.filename:
            # Place the video file in the workspace directory
            workspace_dir = os.path.join(os.getcwd(), "workspace")
            if not os.path.exists(workspace_dir):
                os.makedirs(workspace_dir)
            basename, ext = os.path.splitext(os.path.basename(root.filename))
            new_filename = "data_dst" + ext
            destination = os.path.join(workspace_dir, new_filename)
            shutil.copy2(root.filename, destination)

    def choose_Video_Src(self):
        root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("video files", "*.mp4;*.mkv;*.avi"), ("all files", "*.*")))
        if root.filename:
            # Place the video file in the workspace directory
            workspace_dir = os.path.join(os.getcwd(), "workspace")
            if not os.path.exists(workspace_dir):
                os.makedirs(workspace_dir)
            basename, ext = os.path.splitext(os.path.basename(root.filename))
            new_filename = "data_src" + ext
            destination = os.path.join(workspace_dir, new_filename)
            shutil.copy2(root.filename, destination)
            
            
    def extract_images_Src(self):
        process = subprocess.Popen("2) extract images from video data_src.bat", stdout=subprocess.PIPE, shell=True)
        # afficher le status du processus with red font
        self.status_text.set("Status : Extracting images from video data_src...")
        # update the window
        self.master.update()
        
        while process.poll() is None:
            time.sleep(1)
        self.status_text.set("Process completed")
        self.master.update()
    
    def extract_images_dst(self):
        process = subprocess.Popen("3) extract images from video data_dst FULL FPS.bat", stdout=subprocess.PIPE, shell=True)
        # afficher le status du processus with red font
        self.status_text.set("Status : Extracting images from video data_dst...")
        # update the window
        self.master.update()
        
        while process.poll() is None:
            time.sleep(1)
        self.status_text.set("Process completed")
        self.master.update()
        
        
    def extract_face_src(self):
        process = subprocess.Popen("4) data_src faceset extract.bat", stdout=subprocess.PIPE, shell=True)
        # afficher le status du processus with red font
        self.status_text.set("Status : Extracting faces from data_src...")
        # update the window
        self.master.update()
        
        while process.poll() is None:
            time.sleep(1)
        self.status_text.set("Process completed")
        self.master.update()
        

    
        
        
        
    def extract_face_dst(self):
        process = subprocess.Popen("5) data_dst faceset extract.bat", stdout=subprocess.PIPE, shell=True)
        # afficher le status du processus with red font
        self.status_text.set("Status : Extracting faces from data_dst...")
        # update the window
        self.master.update()
        
        while process.poll() is None:
            time.sleep(1)
        self.status_text.set("Process completed")
        self.master.update()
    
            
        
        
    def Train_AMP(self):
        process = subprocess.Popen("6) train AMP.bat", stdout=subprocess.PIPE, shell=True)
        # afficher le status du processus with red font
        self.status_text.set("Status : Training AMP...")
        # update the window
        self.master.update()
        
        while process.poll() is None:
            time.sleep(1)
        self.status_text.set("Process completed")
        self.master.update()
    
    def Train_Quick96(self):
        process = subprocess.Popen("6) train Quick96.bat", stdout=subprocess.PIPE, shell=True)
        # afficher le status du processus with red font
        self.status_text.set("Status : Training Quick96...")
        # update the window
        self.master.update()
        
        while process.poll() is None:
            time.sleep(1)
        self.status_text.set("Process completed")
        self.master.update()
        

    def Train_SAE_HD(self):  
        process = subprocess.Popen("6) train SAEHD.bat", stdout=subprocess.PIPE, shell=True)
        # afficher le status du processus with red font
        self.status_text.set("Status : Training SAEHD...")
        # update the window
        self.master.update()
        
        while process.poll() is None:
            time.sleep(1)
        self.status_text.set("Process completed")
        self.master.update()
        
        
            
    
    def Merge_Quick96(self):
        process = subprocess.Popen("7) merge Quick96.bat", stdout=subprocess.PIPE, shell=True)
        # afficher le status du processus with red font
        self.status_text.set("Status : Merging Quick96...")
        # update the window
        self.master.update()
        
        while process.poll() is None:
            time.sleep(1)
        self.status_text.set("Process completed")
        self.master.update()
        
    def Merge_AMP(self):
        process = subprocess.Popen("7) merge AMP.bat", stdout=subprocess.PIPE, shell=True)
        # afficher le status du processus with red font
        self.status_text.set("Status : Merging AMP...")
        # update the window
        self.master.update()
        
        while process.poll() is None:
            time.sleep(1)
        self.status_text.set("Process completed")
        self.master.update()
        
    def Merge_SAE_HD(self):
        process = subprocess.Popen("7) merge SAEHD.bat", stdout=subprocess.PIPE, shell=True)
        # afficher le status du processus with red font
        self.status_text.set("Status : Merging SAEHD...")
        # update the window
        self.master.update()
        
        while process.poll() is None:
            time.sleep(1)
        self.status_text.set("Process completed")
        self.master.update()
        
        
        
                   
    def Export_video(self):
        process = subprocess.Popen("8) merged to mp4.bat", stdout=subprocess.PIPE, shell=True)
        # afficher le status du processus with red font
        self.status_text.set("Status : Merging to mp4...")
        # update the window
        self.master.update()
        
        while process.poll() is None:
            time.sleep(1)
        self.status_text.set("Process completed")
        self.master.update()
    
    def clear_workspace(self):
        process = subprocess.Popen("1) clear workspace.bat", stdout=subprocess.PIPE, shell=True)
        # afficher le status du processus with red font
        self.status_text.set("Status : clearing worspace...")
        # update the window
        self.master.update()
        
        while process.poll() is None:
            time.sleep(1)
        self.status_text.set("Process completed")
        self.master.update()
        


        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()




