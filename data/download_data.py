import requests
import pandas as pd
from sodapy import Socrata
from pathlib import Path

# Create data directory if it doesn't exist
data_dir = Path('data')
data_dir.mkdir(exist_ok=True)

# Define the columns to keep
columns_to_keep = [
    'dr_no', 'date_rptd', 'date_occ', 'time_occ', 'area_name',
    'crm_cd_desc', 'vict_age', 'vict_sex', 'vict_descent',
    'weapon_desc', 'status_desc', 'location'
]

# URLs for the datasets (these are direct download links from Kaggle)
client = Socrata("data.lacity.org", None)
results = client.get("2nrs-mtv8")

# Download each file
df = pd.DataFrame.from_records(results)

# Keep only the specified columns
df = df[columns_to_keep]

# Save the cleaned data to CSV
df.to_csv(data_dir / 'crimes.csv', index=False)

print("Data download complete.")
