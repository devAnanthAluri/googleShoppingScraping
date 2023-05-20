# Google Product Scraper

This Python script allows you to scrape product information from Google Shopping and save the data in both Excel and JSON formats. You can specify search options such as minimum and maximum price, shipping availability, and product sorting.

## Prerequisites

- Python 3.7 or above
- Packages listed in the `requirements.txt`  file

## Installation

1. Clone the repository:

   ```bash
   gh repo clone devAnanthAluri/googleShoppingScraping
   
2. Navigate to the project directory:

   ```bash
   cd googleShoppingScraping-main

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   
## Usage
1. Open the config.ini file and configure the search options as needed. You can set the minimum price, maximum price, shipping availability, and product sorting.
2. Install the required packages:

   ```bash
   python gs.py
3. The script will scrape the product information from Google Shopping and save it in both Excel (.xlsx) and JSON (.json) formats. The files will be named based on the search query.
   - Excel file: data_<search_query>.xlsx
   - JSON file: data_<search_query>.json

## Contributing
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

Feel free to customize the content as per your requirements. Make sure to include the appropriate license file (e.g., `LICENSE`) in your repository and update the link in the `README.md` file accordingly.

