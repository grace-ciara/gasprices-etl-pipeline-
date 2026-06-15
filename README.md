## Gas Prices ETL Pipeline

This project is a Python-based ETL (Extract, Transform, Load) pipeline that automates the collection and storage of US city gas prices.

### What it Does
*   **Extracts**: Fetches real-time gas price data from the CollectAPI.
*   **Transforms**: Uses Pandas to clean up the data, drop unnecessary columns, and rename fields.
*   **Loads**: Securely saves the finalized data into a PostgreSQL database table without exposing passwords.

### How the Code is Organized
The project is modularized into separate files to keep the code clean and organized:
*   `gasprices_main.py` - The main script that runs the entire process.
*   `extract.py` - Handles the API connection and data download.
*   `transform.py` - Cleans and formats the data using Pandas.
*   `load.py` - Connects to PostgreSQL and uploads the data.

