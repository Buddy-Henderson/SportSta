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



if __name__ == "__main__":
    install_dependencies()
    