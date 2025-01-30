# Task-1: Data Scraping and Collection Pipeline for Ethiopian Medical Businesses
This project involves scraping data from various Telegram channels related to Ethiopian medical businesses, including doctors, pharmacies, and cosmetic services, to gather insights or for further analysis.

### Setup
### Python Environment
##### Python Version: Use Python 3.7 or higher for compatibility and performance.
##### Dependencies: 
Install the Telethon library, which is used for interacting with the Telegram API:
  pip install telethon

Authentication
API Credentials: Obtain your api_id and api_hash from the Telegram Developer Portal at my.telegram.org. These are necessary for authenticating your script with Telegram's servers.

# Scraping Script
### Basic Structure
##### Initialization: Set up your script to connect to Telegram using your API credentials and phone number.
##### Channel Selection: Target specific channels known to be relevant to Ethiopian medical businesses:
DoctorsET
Chemed
lobelia4cosmetics
yetenaweg
EAHCI
# Data Retrieval: Fetch the last 500 messages from each channel. Here's a pseudo-structure:
python
  from telethon.sync import TelegramClient
  from telethon.tl.functions.messages import GetHistoryRequest

  api_id = 'YOUR_API_ID'
  api_hash = 'YOUR_API_HASH'
  phone = '+YOUR_PHONE_NUMBER'

  with TelegramClient(phone, api_id, api_hash) as client:
      client.start()
      for channel in ['DoctorsET', 'Chemed', 'lobelia4cosmetics', 'yetenaweg', 'EAHCI']:
          try:
              messages = client(GetHistoryRequest(peer=channel, limit=500))
              # Process messages here
          except Exception as e:
              print(f"Error with {channel}: {e}")

# Data Storage
### Initial Storage
##### Temporary Storage: Use local files in CSV or JSON format to store raw data temporarily for further processing or analysis.

# Monitoring & Logging
### Logging
##### Implementation: Add logging to your script to help monitor execution, track errors, and manage data flow:
python
 import logging
 logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Image Scraping
### For Images
##### Media Handling: Extract images from messages where media is present. Here's how you might structure this:
python
 from telethon.tl.types import MessageMediaPhoto
 for message in messages:
     if isinstance(message.media, MessageMediaPhoto):
         # Download or process images here