import tkinter as tk
from twilio.rest import Client

class GUI:
    def __init__(self):

        self.set_gui()

    def set_gui(self):
        # Set window
        self.master_frame = tk.Tk()
        self.master_frame.title("Whatsapp")

        # Set Account SID
        self.SID_label = tk.Label(self.master_frame, fg='black', text=f'Account SID: ')
        self.SID_label.grid(row=0, column=0)

        self.SID_text = tk.Text(self.master_frame, height = 1, width = 50)
        self.SID_text.grid(row=0, column=1)

        # Set Auth Token
        self.auth_token_label = tk.Label(self.master_frame, fg='black', text=f'Auth Token: ')
        self.auth_token_label.grid(row=1, column=0)

        self.auth_token_text = tk.Text(self.master_frame, height=1, width=50)
        self.auth_token_text.grid(row=1, column=1)

        # Set From Number
        self.from_number_label = tk.Label(self.master_frame, fg='black', text=f'From Number: ')
        self.from_number_label.grid(row=2, column=0)

        self.from_number_text = tk.Text(self.master_frame, height=1, width=50)
        self.from_number_text.grid(row=2, column=1)

        # Set To Number
        self.to_number_label = tk.Label(self.master_frame, fg='black', text=f'To Number: ')
        self.to_number_label.grid(row=3, column=0)

        self.to_number_text = tk.Text(self.master_frame, height=1, width=50)
        self.to_number_text.grid(row=3, column=1)

        # Set Message
        self.message_label = tk.Label(self.master_frame, fg='black', text=f'Message: ')
        self.message_label.grid(row=4, column=0)

        self.message_text = tk.Text(self.master_frame, height=3, width=50)
        self.message_text.grid(row=4, column=1)

        # Send Button
        self.send_button = tk.Button(self.master_frame, text='Send', cursor='hand2')
        self.send_button.grid(row=7, column=0, columnspan=2)
        self.send_button.bind('<Button-1>', self.send_button_clicked)

    def run(self):
        self.master_frame.mainloop()

    def send_button_clicked(self, event):
        # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
        accountSid = self.SID_text.get("1.0",'end-1c')
        authToken = self.auth_token_text.get("1.0",'end-1c')
        client = Client(accountSid, authToken)

        # this is the Twilio sandbox testing number
        from_whatsapp_number = self.from_number_text.get("1.0",'end-1c')
        # replace this number with your own WhatsApp Messaging number
        to_whatsapp_number = self.to_number_text.get("1.0",'end-1c')

        text = self.message_text.get("1.0",'end-1c')

        client.messages.create(body=text,
                                from_=from_whatsapp_number,
                                to=to_whatsapp_number)