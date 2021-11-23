import dropbox 
class transfardata:
    def __init__(self,token):
        self.token=token 

    def uploadfile(self,filefrom,fileto):
        db=dropbox.Dropbox(self.token)

        f=open(filefrom,'rb')
        db.files_upload(f.read(),fileto)

    

        



