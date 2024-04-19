import sys
import os
import zipfile

def install_dependencies():
    try:
        # Install pip if not already installed
        ensure_pip()
        
        # Install dependencies from requirements.txt
        install_requirements("requirements.txt")
        
        # Install requests
        install_package("requests")
        
        print("Dependencies installed successfully!")
        
        # Download files from GitHub
        download_files_from_github()
    except Exception as e:
        print(f"An error occurred: {e}")

def ensure_pip():
    try:
        import pip
    except ImportError:
        print("Installing pip...")
        import ensurepip
        ensurepip.bootstrap()
        print("Pip installed successfully!")

def install_requirements(requirements_file):
    try:
        import pip
        with open(requirements_file, "r") as f:
            requirements = f.readlines()
        
        for requirement in requirements:
            pip.main(['install', requirement.strip()])
    except Exception as e:
        print(f"An error occurred while installing requirements: {e}")

def install_package(package_name):
    try:
        import pip
        pip.main(['install', package_name])
    except Exception as e:
        print(f"An error occurred while installing {package_name}: {e}")

def download_files_from_github():
    try:
        import requests
        
        # Define GitHub repository URL and folder path
        github_url = "https://github.com/Buddy-Henderson/SportSta/archive/main.zip"
        folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "SportSta")
        
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
    