import pandas as pd
import src.data.collector as dc
import src.data.process_data as process_data
import os
import logging

# set up logging
logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), "../../logs/main.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def main():
    """scrape data from the Google Play """
    dc.collect_data()

    "clean and process the data"
    BANKS = process_data.load_data()
    if not BANKS:
        logging.error("No data found to process.")
        return
    for bank_name, df in BANKS.items():
        processed_df = process_data.process_data(df, bank_name)
        if processed_df is  None:
            logging.info(f"No data to process for {bank_name}.")


if __name__ == "__main__":
    main()
