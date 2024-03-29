import customtkinter as ctk
import tkinter as tk
import os
import Capacity
import LSB
import ImageQuality
from PIL import Image
my_image=ctk.CTkImage(light_image=Image.open(r"C:\Users\abina\OneDrive\Documents\Programming\programs\MiniProject\bg.jpg"),dark_image=Image.open(r"C:\Users\abina\OneDrive\Documents\Programming\programs\MiniProject\bg.jpg"),size=(1920,1080))
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root=ctk.CTk()
root.geometry("720x480")
root.minsize(height=480,width=720)
root.title("STEGANOGRAPHY TOOL")
image_label=ctk.CTkLabel(root,image=my_image,text="")
def homepage():
    for widget in root.winfo_children():
        if widget !=image_label:
            widget.destroy()
    def encpage():
        for widget in root.winfo_children():
            if widget !=image_label:
                widget.destroy()
        label2=ctk.CTkLabel(root,text="STEGANOGRAPHY TOOL",font=("Arial", 20,"bold"))
        label2.pack(pady=40)
        label3=ctk.CTkLabel(root,text="File name:",font=("Verdana",14))
        label3.place(relx = 0.395,rely = 0.289,anchor ='e')
        input_box_filename=ctk.CTkEntry(root)
        input_box_filename.pack(pady=20)
        bbut1=ctk.CTkButton(master=root,text="<--",command=homepage,width=40,height=4,font=("Arial",14,"bold"),fg_color="black")
        bbut1.place(relx=0.1,rely=0.1,anchor='nw')

        def search_filename():
            user_input_search=input_box_filename.get()
            search_directory=r"C:\Users\abina\OneDrive\Documents\Programming\programs\MiniProject"

            def search_file(search_directory, user_input_search) :
                for root, dirs, files in os.walk(search_directory):
                    if user_input_search in files and user_input_search[-4:]==".png":
                        return os.path.join(root, user_input_search)
                    else:

                        def encpage_go():
                            error_window.destroy()
                        error_window = tk.Tk()
                        error_window.geometry("400x200")
                        error_window.title("Error")
                        error_label = tk.Label(error_window, text="Check the file name and extension!!", font=("Arial", 14,"bold"))
                        error_label.pack(pady=20)
                        error_ok=tk.Button(master=error_window,text="OK", width=20, height=2,command=encpage_go)
                        error_ok.pack(pady=20)
                        error_window.mainloop()
                        
            search_result = search_file(search_directory, user_input_search)
            
            def encpage2():
                for widget in root.winfo_children():
                    if widget !=image_label:
                        widget.destroy()
                bbut1=ctk.CTkButton(master=root,text="<--",command=encpage,width=40,height=4,font=("Arial",14,"bold"),fg_color="black")
                bbut1.place(relx=0.1,rely=0.1,anchor='nw')
                Cap = Capacity.calculate_max_capacity(search_result)
                Cap=str(Cap)
                cap_print="Maximum capacity of data that can be encrypted :", Cap, "bits"
                cap_print=" ".join(cap_print)
                enc_pg2_label1=ctk.CTkLabel(root,text=cap_print,font=("Arial",16,"bold"))
                enc_pg2_label1.pack(pady=20)
                input_box_data=ctk.CTkEntry(root)
                input_box_data.pack(pady=20)

                def enc_data():
                    
                    def exit1():
                        root.destroy()
                    data_to_hide=input_box_data.get() + "\n"
                    LSB.encode_lsb(search_result,data_to_hide)
                    data_enc_button.destroy()
                    enc_pg2_label1.destroy()
                    input_box_data.destroy()
                    label4=ctk.CTkLabel(root,text="ENCRYPTED SUCCESSFULLY",font=("arial",20,"bold"))
                    label4.pack(pady=20)
                    enc_exit_button=ctk.CTkButton(master=root,text="FINISH",command=exit1)
                    enc_decpage_button=ctk.CTkButton(master=root,text="DECRYPTION",command=decpage)
                    enc_mainpage_button=ctk.CTkButton(master=root,text="HOME",command=homepage)
                    enc_decpage_button.pack(pady=20)
                    enc_mainpage_button.pack(pady=20)
                    enc_exit_button.pack(pady=20)
                data_enc_button=ctk.CTkButton(master=root,text="Encrypt",command=enc_data)
                data_enc_button.pack(pady=20)
            if search_result:
                output_label_true=ctk.CTkLabel(root,text="File found\n Click the encrypt button to get to the next step to encrypt text in your image",font=("Arial",14))
                output_label_true.pack(pady=20)
                step1_button=ctk.CTkButton(master=root,text="Next step",command=encpage2)
                step1_button.pack(pady=20)
                
        button_search_filename=ctk.CTkButton(master=root,text="Search",command=search_filename)
        button_search_filename.pack(pady=10)
        
    def decpage():
        for widget in root.winfo_children():
            if widget !=image_label:
                widget.destroy()
        bbut1=ctk.CTkButton(master=root,text="<--",command=homepage,width=40,height=4,font=("Arial",14,"bold"),fg_color="black")
        bbut1.place(relx=0.1,rely=0.1,anchor='nw')
        dec_label_main=ctk.CTkLabel(root,text="STEGANOGRAPHY TOOL",font=("Arial",20,"bold"))
        dec_label_main.pack(pady=20)
        label3=ctk.CTkLabel(root,text="File name:",font=("Verdana",14),fg_color="transparent")
        label3.place(relx = 0.395,rely = 0.289,anchor ='e')
        input_box_filename=ctk.CTkEntry(root)
        input_box_filename.pack(pady=55)

        def search_filename():
            user_input_search=input_box_filename.get()
            search_directory=r"C:\Users\abina\OneDrive\Documents\Programming\programs\MiniProject"
            def search_file(search_directory, user_input_search) :
                for root, dirs, files in os.walk(search_directory):
                    if user_input_search in files and user_input_search[-4:]==".png" and user_input_search[0:6]=="stego_":
                        return os.path.join(root, user_input_search)
                    elif user_input_search not in files:
                        def encpage_go():
                            error_window.destroy()
                        error_window = tk.Tk()
                        error_window.geometry("400x200")
                        error_window.title("Error")
                        error_label = tk.Label(error_window, text="Check the file name and extension!!", font=("Arial", 14,"bold"))
                        error_label.pack(pady=20)
                        error_ok=tk.Button(master=error_window,text="OK", width=20, height=2,command=encpage_go)
                        error_ok.pack(pady=20)
                        error_window.mainloop()
            search_result = search_file(search_directory, user_input_search)

            def decpage2():
                for widget in root.winfo_children():
                    if widget !=image_label:
                        widget.destroy()
                bbut1=ctk.CTkButton(master=root,text="<--",command=decpage,width=40,height=4,font=("Arial",14,"bold"),fg_color="black")
                bbut1.place(relx=0.1,rely=0.1,anchor='nw')
                stego_image=user_input_search
                base_image_file=user_input_search[6:]

                def searchfile(search_directory, user_input_search):
                    for root, dirs, files in os.walk(search_directory):
                        if user_input_search in files and user_input_search[-4:]==".png":
                            return os.path.join(root, user_input_search)
                        else:
                            print("File not found")

                base_image=searchfile(search_directory, base_image_file)
                decoded_message=LSB.decode_lsb(stego_image)
                dec_final_text=(f"The decoded message is: {decoded_message}")
                label4=ctk.CTkLabel(root,text="DECRYPTED SUCCESSFULLY",font=("Arial",20,"bold"))
                label4.pack(pady=30)
                decoded_output=ctk.CTkLabel(root,text=dec_final_text,font=("Arial",22,"bold"))
                decoded_output.pack(pady=15)
                PSNR=ImageQuality.calculate_psnr(base_image,stego_image)
                psnr=(f"Peak Signal-to-Noise Ratio: {PSNR} dB")
                SSIM=ImageQuality.calculate_ssim(base_image,stego_image)
                ssim=(f"Structural Similarity Index: {SSIM}")
                enc_pg2_label2=ctk.CTkLabel(root,text= ssim,font=("Arial",18))
                enc_pg2_label2.pack(pady=20)
                enc_pg2_label1=ctk.CTkLabel(root,text= psnr,font=("Arial",18))
                enc_pg2_label1.pack(pady=20)
                
                def dec_data():
                    def exit1():
                        root.destroy()
                    for widget in root.winfo_children():
                        if widget !=image_label:
                            widget.destroy()
                    enc_exit_button=ctk.CTkButton(master=root,text="FINISH",command=exit1)
                    enc_mainpage_button=ctk.CTkButton(master=root,text="HOME",command=homepage)
                    enc_mainpage_button.pack(pady=100)
                    enc_exit_button.pack()
                data_dec_button=ctk.CTkButton(master=root,text="Finish",command=dec_data)
                data_dec_button.pack(pady=20)
            if search_result:
                output_label_true=ctk.CTkLabel(root,text="File found\n Click the decrypt button to get to the next step to decrypt the text in your image",font=("Arial",14),bg_color="transparent")
                output_label_true.pack(pady=20)
                step1_button=ctk.CTkButton(master=root,text="Decrypt",command=decpage2)
                step1_button.pack(pady=20)
                
        button_search_filename=ctk.CTkButton(master=root,text="Search",command=search_filename)
        button_search_filename.pack(pady=10)
    
    
    image_label.place(relx=0,rely=0,anchor="nw")
    mainlabel=ctk.CTkLabel(root,text="STEGANOGRAPHY TOOL",font=('Arial',20,"bold"))
    mainlabel.pack(pady=30)
    encbutton=ctk.CTkButton(master=root,text="ENCODE",command=encpage,fg_color="#FF6B7F",text_color="black",font=("Arial",14,"bold"),width=200,height=40)
    encbutton.pack(pady=50)
    decbutton=ctk.CTkButton(master=root,text="DECODE",command=decpage,fg_color="light blue",text_color="black",font=("Arial",14,"bold"),width=200,height=40)
    decbutton.pack(pady=30)

    def info_window_func():
        def go_back():
            info_window.destroy()
            homepage()
        info_window = tk.Tk()
        info_window.geometry("400x200")
        info_window.title("Info")
        info_label = tk.Label(info_window, text="Credits:\n Keerthivasan M \n Abhinav B \n Danush S.V", font=("Arial", 14,"bold"))
        info_label.pack(pady=20)
        info_ok=tk.Button(master=info_window,text="OK", width=20, height=2,command=go_back)
        info_ok.pack(pady=20)
        info_window.mainloop()

    info=ctk.CTkButton(master=root,text="Info",fg_color="white",text_color="black",command=info_window_func,width=80,height=6,font=("Arial",16,"bold"))
    info.place(relx=0.9,rely=0.9,anchor="se")

homepage()
root.mainloop()