import os
from azure.storage.blob import BlobServiceClient
from .config import AZURE_STORAGE_CONNECTION_STRING, AZURE_BLOB_CONTAINER

def upload_to_blob(filename, data):
    """Uploads scraped data to Azure Blob Storage."""
    try:
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(AZURE_BLOB_CONTAINER)

        blob_client = container_client.get_blob_client(filename)
        blob_client.upload_blob(data, overwrite=True)

        print(f"✅ File uploaded to Azure Blob: {filename}")

    except Exception as e:
        print(f"❌ Azure Blob upload failed: {e}")
