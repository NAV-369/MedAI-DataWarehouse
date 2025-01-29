
Task-1: Data Scraping and Collection Pipeline for Ethiopian Medical Businesses
Setup
Python Environment:
Use Python 3.7+
Install telethon:
bash
# pip install telethon
Authentication:
Obtain api_id and api_hash from my.telegram.org.

Scraping Script
Basic Structure:
python
# from telethon.sync import TelegramClient
# from telethon.tl.functions.messages import GetHistoryRequest

# api_id = 'YOUR_API_ID'
# api_hash = 'YOUR_API_HASH'
# phone = '+YOUR_PHONE_NUMBER'

# with TelegramClient(phone, api_id, api_hash) as client:
#     client.start()
#     for channel in ['DoctorsET', 'Chemed', 'lobelia4cosmetics', 'yetenaweg', 'EAHCI']:
#         try:
#             messages = client(GetHistoryRequest(peer=channel, limit=500))
#             # Process messages here
#         except Exception as e:
#             print(f"Error with {channel}: {e}")

Data Storage
Initial Storage: 
Use local CSV or JSON for temporary storage of raw data.

Monitoring & Logging
Logging: 
Implement logging within the script to track progress and errors:
python
# import logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

Image Scraping
For Images:
Fetch media messages, particularly those with photos:
python
# from telethon.tl.types import MessageMediaPhoto
# for message in messages:
#     if isinstance(message.media, MessageMediaPhoto):
#         # Download or process images here