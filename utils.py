import os

from google.cloud import secretmanager

secret_manager_client = secretmanager.SecretManagerServiceClient()


def get_secret(secret_name: str):
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    secret_manager_response = secret_manager_client.access_secret_version(
        name=name
    ).payload.data.decode("UTF-8")
    return secret_manager_response
