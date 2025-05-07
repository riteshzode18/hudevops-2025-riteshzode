from azure.storage.blob import BlobServiceClient

connection_string = "my_connection_string"  # Replace with your Azure Storage connection string
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

def transfer_file():
    source_container = 'container-a'
    destination_container = 'container-b'
    blob_name = 'file1.txt'

    source_blob = blob_service_client.get_blob_client(container=source_container, blob=blob_name)
    destination_blob = blob_service_client.get_blob_client(container=destination_container, blob=blob_name)

    # Download the blob from the source container
    download_stream = source_blob.download_blob()
    
    # Upload the blob to the destination container, overwriting if it exists
    destination_blob.upload_blob(download_stream.readall(), overwrite=True)

    # Delete the blob from the source container
    source_blob.delete_blob()

if __name__ == "__main__":
    transfer_file()
    print("File transferred successfully from container-a to container-b.")