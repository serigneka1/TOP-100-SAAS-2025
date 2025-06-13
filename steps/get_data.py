import kagglehub
import logging

import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("shreyasdasari7/top-100-saas-companiesstartups")

def get_data() -> pd.DataFrame:
    try:
        file_name = "top_100_saas_companies_2025.csv"
        df = pd.read_csv(os.path.join(path,file_name ))
        logging.info("Le dataset est bien trouvé....")
        saving_path = "./data/raw"
        if not os.path.exists(saving_path):
            os.makedirs(saving_path)
            logging.info("Répertoire /data/raw est créé ...")
        df.to_csv(os.path.join(saving_path, file_name))
        logging.info("Le dataset est bien chargé dans data/raw")
        return df
    except Exception as e:
        logging.error(f"Il y a une erreur lors de la collecte du dataset: {e}")
        raise e 

