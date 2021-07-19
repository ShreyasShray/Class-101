import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, "rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "QU-1Jk1Ff4kAAAAAAAAAAT4efYmSNSAv_FnYESxvPKcje3Ca6pCW1wBNGc3uiSyr"
    transferdata = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")

    transferdata.uploadFiles(file_from, file_to)
    print("File has been moved")

main()