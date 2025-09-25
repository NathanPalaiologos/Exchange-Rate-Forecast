import subprocess
import os
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA


###############################################################################
# 
def data_parsing():
    """
    Execute the R script to parse and clean exchange rate data from CANSIM.
    The cleaned data will be saved in cache for future analysis.
    """
    r_script_path = os.path.join(os.getcwd(), 'data_parsing.r')
    try:
        subprocess.run(['Rscript', r_script_path], check=True)
        print("R script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the R script: {e}")
    # Load the cleaned data from cache
    cleaned_data_path = os.path.join(os.getcwd(), 'cleaned_exchange_rate.csv')
    df = pd.read_csv(cleaned_data_path, parse_dates=['date'])
    return df

class ARIMA_Model:
    """
    
    """
    


#####################################################################################
def main():
    
    df = data_parsing()
    print(df.head())
    
if __name__ == "__main__":
    main()
    
    
