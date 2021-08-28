

from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
import io
from apiclient import errors
from apiclient import http
import logging
import json
from apiclient import discovery

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']
root_folder={}
# To list folders
def listfolders(service, filid,f_name):
    files=[]
    folder_names={}
    results = service.files().list(
        pageSize=1000, q="\'" + filid + "\'" + " in parents",
        fields="nextPageToken, files(id, name, mimeType)").execute()
    # logging.debug(folder)
    folder_content = results.get('files', [])
    folder_items = []
    # print(folder_content)
    for item in folder_content:
        if str(item['mimeType']) == str('application/vnd.google-apps.folder'):
            subfolder_items = listfolders(service, item['id'], item['name'])  # LOOP un-till the files are found
            folder_items.append({
                item['name']: subfolder_items
            })
            # files.append(fold_names)
        else:
            temp=base_url+item['id']
            folder_items.append(temp)
            # files.append(temp)
            # fold_str.append(temp)
            # downloadfiles(service, item['id'], item['name'], des)
    # folder_names[f_name]=list(files)
    # if folder:
    #     root_folder[f_name]=list(files)
    # print(folder_items)
    return folder_items
    

fold_names={}
base_url="https://drive.google.com/file/d/"
def main_fn(url):
    if(url[-1]=="/"):
        url=url[:-1]
    elif(url.rfind("?")>0):
        url=url[:url.rfind("?")]
    c=url.rfind("/")
    url=url[c+1:]
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.


    # flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    # 'client_secret.json',
    # scopes=['https://www.googleapis.com/auth/drive.metadata.readonly'])
    try:
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            #else:
                #flow = InstalledAppFlow.from_client_secrets_file(
                    #'client_.json', SCOPES)  # credentials.json download from drive API
                #creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
    except Exception as e:
        print("pickle file not found")
    # if os.path.exists('token.pickle'):
    #     with open('token.pickle', 'rb') as token:
    #         creds = pickle.load(token)
    # # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             'client_.json', SCOPES)  # credentials.json download from drive API
    #         creds = flow.run_local_server()
    #     # Save the credentials for the next run
    #     with open('token.pickle', 'wb') as token:
    #         pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    # Call the Drive v3 A
    # Folder_id = "'1LMQAeahaunpKQ335dwER6NR3h-QG5F8b'"  # Enter The Downloadable folder ID From Shared Link
    Folder_id = "'%s'"%(url) 
    print(Folder_id)
    results = service.files().list(
        pageSize=1000, q=Folder_id+" in parents", fields="nextPageToken, files(id, name, mimeType)").execute()
    # contents = listfolders(service, Folder_id, 'root')
    items = results.get('files', [])
    root_content = []
    if not items:
        print('No files found.')
    else:
        files=[]
        for item in reversed(items):
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                # if not os.path.isdir("Folder"):
                #     os.mkdir("Folder")
                # bfolderpath = os.getcwd()+"/Folder/"
                # if not os.path.isdir(bfolderpath+item['name']):
                #     os.mkdir(bfolderpath+item['name'])

                # folderpath = bfolderpath+item['name']
                # temp=url+item['id']
                # fold_str.append(temp)
                # folder_names.append(item['name'])
                root_content.append({
                    item['name']: listfolders(service, item['id'],item['name'])
                })
            else:
                temp=base_url+item['id']
                root_content.append(temp)
                # files.append(temp)
                # fold_str.append(temp)
                # downloadfiles(service, item['id'], item['name'], filepath)
        # root_folder['root']=list(files)
    return root_content

if __name__ == '__main__':
    # main_fn("https://drive.google.com/drive/folders/1LMQAeahaunpKQ335dwER6NR3h-QG5F8b/")
    root_content=main_fn("https://drive.google.com/drive/folders/1A3whUVC426JiuArQj1nVoYkYOkozgHrT?usp=sharing")
    print(root_content)
    # result_json= json.dumps(fold_str)
    # print(result_json)







# # To Download Files
# def downloadfiles(service, dowid, name,dfilespath):
#     request = service.files().get_media(fileId=dowid)
#     fh = io.BytesIO()
#     downloader = MediaIoBaseDownload(fh, request)
#     done = False
#     while done is False:
#         status, done = downloader.next_chunk()
#         print("Download %d%%." % int(status.progress() * 100))
#     with io.open(dfilespath + "/" + name, 'wb') as f:
#         fh.seek(0)
#         f.write(fh.read())

