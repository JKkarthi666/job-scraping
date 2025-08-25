# Indeed Job Scraper

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful and robust Python script to scrape job listings from Indeed.com. This tool extracts comprehensive job details including titles, companies, locations, summaries, and full job descriptions, then saves the data into a well-formatted and ready-to-use Excel spreadsheet.

## Features

-   **Multi-Page Scraping**: Scrape job listings across multiple search result pages.
-   **Full Job Descriptions**: Navigates to each job's detail page to extract the complete description.
-   **Formatted Excel Output**: Saves data to an `.xlsx` file with auto-filtered columns, a frozen header row, and text wrapping for easy analysis.
-   **Command-Line Interface**: Easily specify search query, location, number of pages, and output file name via CLI arguments.
-   **Robust & Polite**: Includes error handling for network issues and rate-limiting delays to avoid getting blocked.
-   **Progress Tracking**: Uses `tqdm` to display a progress bar during scraping.

---

### Ethical Use & Disclaimer

**Warning**: Web scraping may be against the terms of service of some websites. This script is for educational purposes only. Please use it responsibly.
-   Always check Indeed's `robots.txt` file before scraping.
-   Do not use this script for commercial purposes without permission.
-   The structure of websites changes frequently. This scraper may need maintenance to continue working correctly. The author is not responsible for any misuse of this script.

---

### Prerequisites

-   Python 3.7 or newer

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/indeed-job-scraper.git](https://github.com/your-username/indeed-job-scraper.git)
    cd indeed-job-scraper
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

### Usage

The script is run from the command line and accepts several arguments to customize your search.

**Basic Usage (uses default values):**
This will scrape 2 pages of "Python Developer" jobs in "Chennai" and save to `indeed_jobs_formatted.xlsx`.
```bash
python job_scraper.py