
# Food-Grab

Food-Grab is a web scraping application designed to extract food-related data from specified URLs. It provides functionalities to scrape data, persist it into gzip and JSON files, and parse HTML content using Beautiful Soup.

## Files

### 1. Constants.py

- **Description**: This file contains headers and URLs used throughout the application.
- **Purpose**: Centralizes constants to ensure consistency and ease of maintenance.
- **Usage**: Import relevant constants into other modules for headers and URLs.

### 2. Persist.py

- **Description**: This module is responsible for persisting scraped data into gzip and JSON files.
- **Purpose**: Facilitates data storage and retrieval for later use.
- **Usage**: Import into the main application to save scraped data in a compressed and structured format.

### 3. Scraper.py

- **Description**: Contains the main scraping logic of the application.
- **Purpose**: Implements the functionality to extract data from specified URLs.
- **Usage**: Utilize functions and classes defined here to scrape data from web pages.

### 4. SoupParse.py

- **Description**: Provides methods to send requests to URLs and parse the responses using Beautiful Soup.
- **Purpose**: Handles HTTP requests and parses HTML content for extraction.
- **Usage**: Import into Scraper.py for parsing web pages and extracting relevant information.

## Usage

1. **Setup Environment**: Ensure Python and required libraries are installed (`Beautiful Soup`, `requests`, etc.).
2. **Configure Constants**: Update Constants.py with appropriate headers and URLs for scraping.
3. **Run Scraper**: Execute Scraper.py to initiate the scraping process.
4. **Persist Data**: Utilize Persist.py to save scraped data into gzip and JSON files.
5. **Customization**: Modify scraping logic and parsing methods as per requirements.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
