

# Google Drive Folder Downloader

This Python script allows you to download all files from a specified Google Drive folder to a local folder on your computer.

## Features

- Authenticate using Google OAuth 2.0
- Download all files from a specified Google Drive folder
- Save files to a specified local directory

## Prerequisites

- Python 3
- Google Cloud Platform account
- Google Drive API enabled
- `client_secret.json` file for OAuth 2.0 authentication

## Setup Instructions

### Step 1: Enable Google Drive API and Obtain `client_secret.json`

1. **Access Google Cloud Console**: Go to [Google Cloud Console](https://console.cloud.google.com/).
2. **Create a New Project**: Navigate to "IAM & Admin" > "Manage Resources", click "CREATE PROJECT", enter project details, and click "CREATE".
3. **Enable Google Drive API**: Select your project, go to "API & Services" > "Dashboard", click "+ ENABLE APIS AND SERVICES", find and enable "Google Drive API".
4. **Create Credentials**: Go to "Credentials" page, click "CREATE CREDENTIALS", select "OAuth client ID", configure the consent screen, select "Desktop app", and create the credentials.
5. **Download `client_secret.json`**: Once the credentials are created, download the `client_secret.json` file.


### Step 2: Install Required Libraries

Run the following command in your terminal to install the necessary Python libraries:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

These libraries are essential for interacting with the Google Drive API and handling authentication.

### Step 3: Set Up the Script

Place the `client_secret.json` file, which you obtained from the Google Cloud Platform, in the same directory as your Python script. This file is required for authenticating with the Google Drive API.

### Step 4: Usage

1. **Run the Script**: Execute the Python script. It will prompt you for the Google Drive folder URL and the local destination folder path.
2. **Authenticate**: A web browser window will open for authentication. Log in to your Google account and authorize the script to access your Google Drive.
3. **Downloading Files**: The script will start downloading the files from the specified Google Drive folder to the designated local directory.

### Creating a Virtual Environment (Optional)

Creating a virtual environment is recommended to avoid conflicts with other Python projects or libraries.

1. **Create a Virtual Environment**:
   ```bash
   python -m venv myenv
   ```
2. **Activate the Environment**:
   - On Windows: `myenv\Scripts\activate`
   - On macOS/Linux: `source myenv/bin/activate`
3. **Install Libraries in the Virtual Environment**:
   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```
4. **Deactivate the Environment**:
   ```bash
   deactivate
   ```

### Notes

- Ensure you have the necessary permissions to access the files in the specified Google Drive folder.
- Handle your `client_secret.json` file securely as it contains sensitive information.

### Troubleshooting

If you encounter any issues:
- Ensure your Python version is compatible with the libraries.
- Verify the correctness of your `client_secret.json` file.
- Check your internet connection and permissions on Google Drive.

