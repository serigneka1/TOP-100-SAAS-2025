# Installation 
```bash
pip install dvc[gs] #installer dvc avec support gcs
pip install pandas scikit-learn joblib
```
# Initialiser le projte 
```bash
git init 
dvc init
```
# Config stockage distant GCS
- creation bucket dans gcs 
- creer une authentification via IAM et telecharger la clé json


# Config DVC pour utiliser ce compte
```bash
export GOOGLE_APPLICATION_CREDENTIALS="chemin vers le fichier clé json" # dans bash
$env:GOOGLE_APPLICATION_CREDENTIALS="chemin vers le fichier clé json" # pour windows
```

# Ajouter le remote GCS à DVC
```bash
git remote add -d TOP_100_SAAS_2025 gs://projet-churn-employes/dvcstore
``` 

# Ajouter les données au bu remote
```bash
dvc add data/top_100_saas_2025_data.csv # Ajouter le suivi dvc aux données
git add data/top_100_saas_2025_data.csv.dvc data/.gitignore # ajouter le suivi git aux fichiers créé par dvc quand on fait dvc add
```