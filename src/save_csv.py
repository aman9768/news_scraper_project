import pandas as pd
import os

def save_to_csv(data):
    # Create data folder if not exists
    os.makedirs("data", exist_ok=True)
    
    df = pd.DataFrame(data)

    df.to_csv("data/headlines.csv", index=False)

    print("CSV file saved successfully!")