from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os
import io

def google_drive_authentication():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('drive', 'v3', credentials=creds)

def download_files(service, folder_id, destination_folder):
    results = service.files().list(q=f"'{folder_id}' in parents", 
                                   fields="nextPageToken, files(id, name, mimeType)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found in the folder.')
    else:
        for item in items:
            file_id = item['id']
            file_name = item['name']
            mime_type = item['mimeType']

            if 'google-apps' in mime_type:
                # Gestire l'esportazione dei file di Google Docs (aggiungi qui il codice)
                continue  # Salta i file di Google Docs o gestiscili come necessario

            if mime_type != 'application/vnd.google-apps.folder':
                # Gestire il download di file normali
                request = service.files().get_media(fileId=file_id)
                file_path = os.path.join(destination_folder, file_name)
                fh = io.FileIO(file_path, 'wb')
                downloader = MediaIoBaseDownload(fh, request)

                try:
                    done = False
                    while done is False:
                        status, done = downloader.next_chunk()
                        print(f"Download {int(status.progress() * 100)}% of {file_name}.")
                except googleapiclient.errors.HttpError as error:
                    print(f"Errore nel download di {file_name}: {error}")
                finally:
                    fh.close()




def main():
    folder_url = input("Enter the Google Drive folder URL: ")
    folder_id = folder_url.split('/')[-1]  # Extract the folder ID from the URL
    destination_folder = input("Enter the local destination folder path: ")

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    service = google_drive_authentication()
    download_files(service, folder_id, destination_folder)

if __name__ == '__main__':
    main()
