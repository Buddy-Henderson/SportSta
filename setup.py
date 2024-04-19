import subprocess
import sys
import os

import zipfile

def install_dependencies():
    try:
        # Install pip if not already installed
        subprocess.run([sys.executable, '-m', 'ensurepip', '--default-pip'])
        
        # Install dependencies from requirements.txt
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        
        print("Dependencies installed successfully!")
        
        # Download files from GitHub
        download_files_from_github()
    except Exception as e:
        print(f"An error occurred: {e}")
        
def download_files_from_github():
    try:
        # Import requests here after ensuring it's installed
        import requests
        
        # Define GitHub repository URL and folder path
        github_url = "https://github.com/yourusername/yourrepository/archive/main.zip"
        folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "MyProjectFolder")
        
        # Create folder on desktop if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Download and extract files
        response = requests.get(github_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            zip_file_path = os.path.join(folder_path, "temp.zip")
            
            # Save zip file to disk
            with open(zip_file_path, "wb") as f:
                f.write(response.content)
            
            # Extract zip file
            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(folder_path)
            
            # Remove zip file
            os.remove(zip_file_path)
            
            print(f"Files downloaded and extracted to {folder_path}")
        else:
            print("Failed to download files from GitHub.")
    except ImportError:
        print("Requests library is not installed. Please install it manually.")
    except Exception as e:
        print(f"An error occurred while downloading files: {e}")

if __name__ == "__main__":
    install_dependencies()
    