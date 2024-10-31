import customtkinter as ctk

from paciente.gui import Frame  # Make sure this path is correct
ctk.set_appearance_mode("dark")


def main():
    root = ctk.CTk()
    root.title('HISTORIAL MEDICO')
    root.resizable(0, 0)
    
    
    frame = Frame(root)
    frame.pack()  # This ensures the frame is displayed within the root window
    
    root.mainloop()  # Run the main loop on the root window

if __name__ == '__main__':
    main()
