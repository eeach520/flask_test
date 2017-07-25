import imaplib
import email

class myImap:
    def __init__(self,host,port,username,password,open_box):
        self.imap=imaplib.IMAP4(host,port)
        self.username=username
        self.password=password
        self.open_box=open_box

    def login_and_choose(self):
        self.imap.login(self.username,self.password)
        self.imap.select(self.open_box)