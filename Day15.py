import qrcode,customtkinter,sys

def generate():
    link=linkbox.get()
    qr=qrcode.QRCode(
        box_size=20
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("Qrcode.png")
    img.show()
    sys.exit()

win=customtkinter.CTk()
linkbox=customtkinter.CTkEntry(win,fg_color="lightblue",bg_color="Black",
text_color="Green",font=("Arial", 16, "bold"),width=250,height=50)
linkbox.grid(row=0,column=0)

button=customtkinter.CTkButton(win,text="Generate",fg_color="Black",bg_color="Black",
text_color="Green",font=("Arial", 16, "bold"),width=250,height=50,cursor="hand2",command=generate)
button.grid(row=1,column=0)

win.mainloop()
