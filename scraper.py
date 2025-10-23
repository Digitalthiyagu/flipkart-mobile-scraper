"""
Flipkart Mobile Phone Scraper
Author: [Your Name]
Description: Web scraper to collect mobile phone data from Flipkart
for price comparison and market analysis.

DISCLAIMER: For educational purposes only. Always respect website Terms of Service.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
import logging
from typing import List, Dict, Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class FlipkartMobileScraper:
    """
    A professional web scraper for Flipkart mobile phones.
    
    Features:
    - Respectful rate limiting
    - Comprehensive error handling
    - Data validation
    - CSV export functionality
    """
    
    def __init__(self, max_pages: int = 10, delay: float = 2.0):
        """
        Initialize the scraper with configuration.
        
        Args:
            max_pages: Maximum number of pages to scrape
            delay: Delay between requests in seconds (rate limiting)
        """
        self.max_pages = max_pages
        self.delay = delay
        self.base_url = "https://www.flipkart.com/search"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
    def scrape_page(self, page_num: int) -> List[Dict]:
        """
        Scrape a single page of mobile phone listings.
        
        Args:
            page_num: Page number to scrape
            
        Returns:
            List of product dictionaries
        """
        products = []
        url = f"{self.base_url}?q=mobile+phones+under+50000&page={page_num}"
        
        try:
            logger.info(f"Scraping page {page_num}...")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "lxml")
            container = soup.find("div", class_="DOjaWF gdgoEp")
            
            if not container:
                logger.warning(f"No product container found on page {page_num}")
                return products
            
            # Extract product elements
            names = container.find_all("div", class_="KzDlHZ")
            prices = container.find_all("div", class_="Nx9bqj _4b5DiR")
            descriptions = container.find_all("ul", class_="G4BRas")
            reviews = container.find_all("div", class_="XQDdHH")
            
            # Combine data
            for name, price, desc, review in zip(names, prices, descriptions, reviews):
                product = {
                    'product_name': name.text.strip(),
                    'price': price.text.strip(),
                    'description': desc.text.strip(),
                    'reviews': review.text.strip(),
                    'scraped_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'page_number': page_num
                }
                products.append(product)
            
            logger.info(f"✓ Found {len(products)} products on page {page_num}")
            
        except requests.exceptions.Timeout:
            logger.error(f"Timeout on page {page_num}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error on page {page_num}: {e}")
        except Exception as e:
            logger.error(f"Parsing error on page {page_num}: {e}")
        
        return products
    
    def scrape_all(self, start_page: int = 1) -> pd.DataFrame:
        """
        Scrape multiple pages with rate limiting.
        
        Args:
            start_page: Starting page number
            
        Returns:
            DataFrame containing all scraped products
        """
        all_products = []
        end_page = start_page + self.max_pages
        
        logger.info(f"Starting scrape from page {start_page} to {end_page}")
        
        for page in range(start_page, end_page):
            products = self.scrape_page(page)
            all_products.extend(products)
            
            # Rate limiting - be respectful to the server
            if page < end_page - 1:
                logger.info(f"Waiting {self.delay}s before next request...")
                time.sleep(self.delay)
        
        df = pd.DataFrame(all_products)
        logger.info(f"✓ Total products scraped: {len(df)}")
        
        return df
    
    def save_to_csv(self, df: pd.DataFrame, filename: str = None) -> str:
        """
        Save DataFrame to CSV file.
        
        Args:
            df: DataFrame to save
            filename: Output filename (auto-generated if None)
            
        Returns:
            Path to saved file
        """
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'flipkart_mobiles_{timestamp}.csv'
        
        df.to_csv(filename, index=False, encoding='utf-8')
        logger.info(f"✓ Data saved to {filename}")
        
        return filename
    
    def get_statistics(self, df: pd.DataFrame) -> Dict:
        """
        Generate basic statistics from scraped data.
        
        Args:
            df: DataFrame with scraped data
            
        Returns:
            Dictionary with statistics
        """
        stats = {
            'total_products': len(df),
            'unique_products': df['product_name'].nunique(),
            'pages_scraped': df['page_number'].nunique() if 'page_number' in df.columns else 0,
            'date_range': f"{df['scraped_date'].min()} to {df['scraped_date'].max()}" if 'scraped_date' in df.columns else 'N/A'
        }
        
        return stats


def main():
    """Main execution function"""
    print("="*60)
    print("     FLIPKART MOBILE PHONE SCRAPER")
    print("="*60)
    print("\n⚠️  DISCLAIMER: For educational purposes only.")
    print("   Always respect website Terms of Service.\n")
    
    # Configuration
    MAX_PAGES = 10
    DELAY = 2.0
    START_PAGE = 1
    
    # Initialize scraper
    scraper = FlipkartMobileScraper(max_pages=MAX_PAGES, delay=DELAY)
    
    # Scrape data
    df = scraper.scrape_all(start_page=START_PAGE)
    
    if not df.empty:
        # Save to CSV
        filename = scraper.save_to_csv(df)
        
        # Display statistics
        stats = scraper.get_statistics(df)
        print("\n" + "="*60)
        print("     SCRAPING STATISTICS")
        print("="*60)
        for key, value in stats.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        # Display preview
        print("\n" + "="*60)
        print("     DATA PREVIEW (First 5 Products)")
        print("="*60)
        print(df[['product_name', 'price', 'reviews']].head())
        
        print(f"\n✓ SUCCESS! Data saved to: {filename}\n")
    else:
        print("\n❌ No data was scraped. Please check the logs.\n")


if __name__ == "__main__":
    main()