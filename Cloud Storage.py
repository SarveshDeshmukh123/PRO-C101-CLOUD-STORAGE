import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Aty1nDxB3bWF8mkUTbisTTmsdpV0lI1Y-dv7QgTh7mEtEvAWob6qqDAhG7JvV9zP_T92xpDjk8eBbeEXrOZHP87SjsaV48K705eBSnL2zeJ-AJtqqjeU1sj5QUMsyebEMDKc1jE'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
