def save():
    import datetime
    entry=text.get("1.0",END)
    if entry:
      with open("Diary.txt","a") as f:
        f.write("\n---"+str(datetime.date.today())+"---\n")
        new_entry="*"*len(entry)
        f.write(new_entry)
    text.delete("1.0",END)
from tkinter import *
window= Tk()
window.geometry("500x400")
window.config(bg="#4C0A0B")
text=Text(window,font=("times new roman",15,"italic"),fg="white", bg="#4C0A0B", insertbackground="white")
label=Label(window,text="Brain Dump")
label.config(fg="white",bg="#4C0A0B",font=("ink free",25))
image=PhotoImage(file="gold heart.png")
label.config(image=image,compound="left")
button=Button(window,text="Save your entry",command=save)
icon=PhotoImage(file="stamp.png")
button.config(font=("ink free",12,"bold"), 
                fg="white",        # maroon text
                activeforeground="white",
                bg="#3b0a0a",
                relief="flat",
                padx=15, pady=8,image=icon,compound="right")
label.pack(anchor="center")
button.pack(anchor="center",pady=15)
text.pack(expand=True, fill="both", padx=20, pady=10)
window.mainloop()
