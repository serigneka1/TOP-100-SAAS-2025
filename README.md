# TOP 100 SAAS 2025
Ce projet utilise Git pour la gestion du code, DVC (Data Version Control) pour la gestion des données volumineuses, et Google Cloud Storage (GCS) pour le stockage distant des fichiers de données.

# Prérequis
Git installé
Python (avec venv) installé
DVC installé (pip install dvc[s3,gdrive,gcs] ou pip install dvc[gdrive,gcs] selon besoin)
Un bucket Google Cloud Storage configuré
Un fichier de credentials Google Cloud JSON pour authentification

# Configuration initiale
### 1. Cloner le dépôt
```bash
git clone https://github.com/serigneka1/TOP-100-SAAS-2025.git
cd TOP-100-SAAS-2025
```
### 2. Créer venv
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows PowerShell
# ou
source venv/bin/activate  # Linux/macOS
```

### 3. Installer les requirements
```bash
pip install -r requirements.txt
# ou au minimum installer dvc avec support gcs
pip install dvc[gcs]
```
# Authentification Google Cloud

### 1- Créer un bucket, configurer une clé service et placer le fichier JSON des credentials dans le projet 
### 2- Définir la variable d'env GOOGLE_APPLICATION_CREDENTIALS
```bash
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\chemin\vers\fichier.json" # Sur PowerShell (Windows) 
export GOOGLE_APPLICATION_CREDENTIALS="C:\chemin\vers\fichier.json" # Sur Linux/macOS
```
NB: Il y a moyen de créer un script, mais la variable d'env suffit pour le moment
# Configuration de DVC

### 1. Initialiser DVC 
```bash
dvc init
```
### 2. Ajouter les fichiers de données (ici un CSV)
```bash
dvc add data/top_100_saas_companies_2025.csv # J'ai mis mon fichier dans data/
```
### 3. Configurer le remote DVC sur Google Cloud Storage
```bash
dvc remote add -d TOP_100_SAAS_2025 gs://top_100_saas_2025/dvcstore # Mon bucket dans GS c'est top_100_saas_2025 alors les donnees se trouveront dans dvcstore
```
### 4. Pousser les données vers le remote
```bash
dvc push
```
# Git
### 1. Ajouter les fichiers .dvc et .gitignore
```bash
git add data/top_100_saas_companies_2025.csv.dvc .gitignore
git commit -m "Ajouter le dataset suivi par DVC"
git push origin main
```
---
# Architecture global du projet
```bash
TOP-100-SAAS-2025/
│
├── data/                     # données versionnées avec dvc: fichiers.dvc
│   ├── raw/                  # Données brutes chargées
│   ├── cleaned/              # Données nettoyées et préparées
│   ├── features/             # Données enrichies avec nouvelles features
│   ├── split/                # Données train/test splittées
│   └── ready_features/       # Features finales prêtes pour entraînement
│
├── models/                   
│   ├── trained_models/       # Modèles entraînés sauvegardés
│   └── reports/              # Rapports d’évaluation, courbes, logs
│
├── src/                     
│   ├── steps/                # Scripts étapes
│   │   ├── get_data.py
│   │   ├── clean_data.py
│   │   ├── feature_engineering.py
│   │   ├── split_data.py
│   │   ├── featurization.py
│   │   ├── train_model.py
│   │   └── evaluate_model.py
│   ├── gs_authenticate.py    # Authentification GCS
│   └── main.py               # Script principal pour lancer pipeline
│
├── tests/                    # Tests avec pytest
│
├── configs/                  
│   └── model_params.yml      # Hyperparamètres et paramètres
│
├── Dockerfile                
├── requirements.txt          
├── .gitignore               
├── README.md                 
└── .env.example              # Exemple de fichier d’environnement 

```
## Workflow global
- Récupération des données avec 01_get_data.py
- Nettoyage via 02_clean_data.py
- Ingénierie des features dans 03_feature_engineering.py
- Split train/test avec 04_split_data.py
- Préparation finale des features (05_featurization.py)
- Entraînement du modèle (06_train_model.py)
- Évaluation et génération des rapports (07_evaluate_model.py)

## Technos
- Python
- GIT/Github
- DVC pour versionner les données et orchestrer le pipeline
- Docker pour un environnement reproductible en local et CI/CD
- pytest pour tests automatisés
- Click pour CLI simple et paramétrable (ex: authentification)
- GitHub Actions pour CI/CD (tests + pipeline + déploiement)