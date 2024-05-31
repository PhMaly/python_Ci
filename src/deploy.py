import subprocess
import requests
from datetime import datetime
from src.secrets import api_token


# Instruction :
# sur le dépot local (client)
# git add .
# git commit "message automatique"
# git push

# sur le serveur (pythonAnywhere)
# git pull
# reload app


def deploy():
    # Chemin local vers le projet buttle
    project_path = "/home/philemon/Workspace/PYTHON/Projet Python/python_Ci"

    # Message du commit avec le timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"Déploiement automatique - {timestamp}"

    # Commandes git add, commit, push les modifications.
    subprocess.run(["git", "add", "."], cwd=project_path)  # cwd spécifie le répertoire de travail pour les commandes.
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=project_path)
    subprocess.run(["git", "push"], cwd=project_path)

    # Information d'authentification à l'API pythonAnywhere
    username = 'PhMaly'
    token = api_token
    # id de la console utilisé sur pythonAnywhere
    console_id = 34056427

    # Endpoints de l'Api pythonAnywhere que je stock dans des variables.
    git_pull_url = f"https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{console_id}/send_input/"
    reload_app_url = f"https://www.pythonanywhere.com/api/v0/user/{username}/webapps/PhMaly.pythonanywhere.com/reload/"

    # En-têtes de requête avec l'authentification
    headers = {
        "Authorization": f"Token {token}",
    }
    # Corps de la requête avec la commande
    payload = {
        "input": "git pull\n"
    }
    # Effectuer une requête POST pour mettre à jour le dépôt Git
    git_pull_response = requests.post(git_pull_url, headers=headers, data=payload)

    # Effectuer une requête POST pour recharger l'application
    reload_app_response = requests.post(reload_app_url, headers=headers)

    # Vérifier les réponses
    if git_pull_response.status_code == 200:
        print("Dépôt Git mis à jour avec succès")
    else:
        print(f"Échec de la mise à jour du dépôt Git : {git_pull_response.text}")

    if reload_app_response.status_code == 200:
        print("Application rechargée avec succès")
    else:
        print(f"Échec du rechargement de l'application : {reload_app_response.text}")


if __name__ == '__main__':
    deploy()
