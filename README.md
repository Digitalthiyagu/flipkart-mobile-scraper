# 🛒 Flipkart Mobile Phone Scraper

A Python-based web scraper designed to extract mobile phone listings from Flipkart for price comparison, market analysis, and research purposes.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## 📋 Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Sample Output](#sample-output)
- [Legal Disclaimer](#legal-disclaimer)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## ✨ Features

- **Smart Rate Limiting**: Respectful scraping with configurable delays
- **Robust Error Handling**: Comprehensive exception management
- **Data Validation**: Ensures data integrity and quality
- **Logging System**: Detailed logging for debugging and monitoring
- **CSV Export**: Clean, structured data export
- **Scalable Architecture**: Object-oriented design for easy extension
- **User-Agent Rotation**: Mimics real browser behavior

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Requests**: HTTP library for web requests
- **BeautifulSoup4**: HTML parsing and data extraction
- **lxml**: Fast XML and HTML parser
- **Pandas**: Data manipulation and CSV handling
- **Logging**: Built-in Python logging for monitoring

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/flipkart-mobile-scraper.git
cd flipkart-mobile-scraper
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Basic Usage
```bash
python scraper.py
```

### Programmatic Usage
```python
from scraper import FlipkartMobileScraper

# Initialize scraper
scraper = FlipkartMobileScraper(max_pages=5, delay=2.0)

# Scrape data
df = scraper.scrape_all(start_page=1)

# Save to CSV
scraper.save_to_csv(df, 'my_data.csv')

# Get statistics
stats = scraper.get_statistics(df)
print(stats)
```

### Configuration Options

| Parameter | Description | Default |
|-----------|-------------|---------|
| `max_pages` | Number of pages to scrape | 10 |
| `delay` | Delay between requests (seconds) | 2.0 |
| `start_page` | Starting page number | 1 |

## 📁 Project Structure
```
flipkart-mobile-scraper/
│
├── scraper.py              # Main scraper implementation
├── requirements.txt        # Project dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
├── LICENSE                # MIT License
│
├── data/                  # Data directory
│   └── sample_output.csv  # Sample scraped data
│
└── screenshots/           # Project screenshots
    └── demo.png          # Demo screenshot
```

## 📊 Sample Output

| Product Name | Price | Description | Reviews | Scraped Date |
|--------------|-------|-------------|---------|--------------|
| Samsung Galaxy M34 | ₹18,999 | 6GB RAM, 128GB Storage | 4.3★ (25,431) | 2024-10-23 |
| Realme 11 Pro | ₹23,999 | 8GB RAM, 256GB Storage | 4.4★ (18,522) | 2024-10-23 |

[View Full Sample Data](data/sample_output.csv)

## ⚖️ Legal Disclaimer

**⚠️ IMPORTANT: This project is for educational purposes only.**

- Always respect website Terms of Service
- Check `robots.txt` before scraping
- Use responsibly and ethically
- Do not use for commercial purposes without permission
- Implement appropriate rate limiting
- This tool is for learning web scraping techniques

**The author is not responsible for misuse of this tool.**

## 🔮 Future Enhancements

- [ ] Add database integration (SQLite/PostgreSQL)
- [ ] Implement proxy rotation
- [ ] Add price tracking and alerts
- [ ] Create data visualization dashboard
- [ ] Add support for multiple e-commerce sites
- [ ] Implement concurrent scraping
- [ ] Add email notifications
- [ ] Create REST API wrapper

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Your Name**
- LinkedIn: Thiyagarajan Balasubramanian [https://www.linkedin.com/in/digitalthiyagu/]
-- GitHub: https://github.com/Digitalthiyagu/

---

⭐ **If you found this project helpful, please consider giving it a star!**

**Built with ❤️ for learning and exploration**