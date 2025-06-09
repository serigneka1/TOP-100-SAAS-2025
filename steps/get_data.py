import kagglehub

import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("shreyasdasari7/top-100-saas-companiesstartups")

def get_data() -> pd.DataFrame:
    df = pd.read_csv(os.path.join(path, "top_100_saas_companies_2025.csv"))
    df.to_csv("./data/top_100_saas_companies_2025.csv")
    return df


