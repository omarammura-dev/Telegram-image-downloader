import uuid
from CTkMessagebox import CTkMessagebox
from customtkinter import *
from telethon import TelegramClient, events, sync
from telethon.tl.types import PeerUser, PeerChat, PeerChannel




set_appearance_mode("dark")
set_default_color_theme("green")


def download():
    if(entry.get() == ""):
        CTkMessagebox(title="Error", message="Please enter video link")
    else:
        
        api_id=fake_id
        api_hash='hashahash'
        client = TelegramClient('session_name', api_id, api_hash)
        client.start()
        channel = client.get_entity(entry.get())
        c = client.get_entity(PeerChannel(channel.id))
        for m in client.iter_messages(c):
            print(m.download_media("image/"+str(uuid.uuid1())))
           
def submit():
    p.start()
    download()


root = CTk()
root.geometry("720x482")
root.title("Telegram image downloader")

frame  = CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label = CTkLabel(master=frame,text="Welcome to Telegram image downloader",font=('Arial',24))
label.pack(pady=10,padx=12)

entry = CTkEntry(master=frame,placeholder_text="Enter channel name",width=500)
entry.pack(pady=10,padx=12)
p = CTkProgressBar(master=frame,orientation="horizontal",mode='indeterminate')
p.set(0)


b = CTkButton(master=frame,command=submit,text="begin download")
b.pack()
p.pack(pady=12)


root.mainloop()