import json
import traceback
from typing import Optional

import aiohttp


class WaClient:
    def __init__(self, instance_id: str = '', api_token: str = ''):
        """
        WhatsApp API Client using Green API (or similar provider)
        
        Args:
            instance_id: Instance ID from the API provider
            api_token: API token for authentication
        """
        self.instance_id = instance_id
        self.api_token = api_token
        self.base_url = f"https://api.green-api.com/waInstance{instance_id}"

    def get_url(self, method: str):
        """Construct API URL for a given method"""
        return f"{self.base_url}/{method}/{self.api_token}"

    async def get_state_instance(self) -> dict:
        """Get instance state"""
        url = self.get_url("getStateInstance")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()

    async def receive_notification(self) -> dict:
        """
        Receive incoming notification (message, status, etc.)
        Similar to get_updates in Telegram API
        """
        url = self.get_url("receiveNotification")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()

    async def delete_notification(self, receipt_id: int) -> dict:
        """Delete processed notification"""
        url = self.get_url("deleteNotification")
        params = {'receiptId': receipt_id}
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, params=params) as resp:
                return await resp.json()

    async def send_message(self, chat_id: str, text: str, buttons=None, parse_mode=None):
        """
        Send text message to WhatsApp chat
        
        Args:
            chat_id: WhatsApp chat ID (phone number with country code + @c.us)
            text: Message text
            buttons: Optional buttons (not directly supported in base API)
            parse_mode: Optional parse mode (Markdown, HTML)
        """
        try:
            url = self.get_url("sendMessage")
            payload = {
                'chatId': chat_id,
                'message': text
            }
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload) as resp:
                    res_dict = await resp.json()
                    return res_dict
        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())
            return {'error': True, 'message': str(e)}

    async def send_file_by_url(self, chat_id: str, url_file: str, filename: str, caption: str = ''):
        """
        Send file by URL
        
        Args:
            chat_id: WhatsApp chat ID
            url_file: URL of the file to send
            filename: Name of the file
            caption: Optional caption for the file
        """
        try:
            url = self.get_url("sendFileByUrl")
            payload = {
                'chatId': chat_id,
                'urlFile': url_file,
                'fileName': filename,
                'caption': caption
            }
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload) as resp:
                    res_dict = await resp.json()
                    return res_dict
        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())
            return {'error': True, 'message': str(e)}

    async def send_file_by_upload(self, chat_id: str, file_path: str, filename: str, caption: str = ''):
        """
        Send file by upload
        
        Args:
            chat_id: WhatsApp chat ID
            file_path: Path to file to upload
            filename: Name of the file
            caption: Optional caption for the file
        """
        try:
            url = self.get_url("sendFileByUpload")
            # Read file content before creating the request
            with open(file_path, 'rb') as f:
                file_content = f.read()
            
            data = aiohttp.FormData()
            data.add_field('chatId', chat_id)
            data.add_field('file', file_content, filename=filename)
            if caption:
                data.add_field('caption', caption)
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, data=data) as resp:
                    res_dict = await resp.json()
                    return res_dict
        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())
            return {'error': True, 'message': str(e)}

    async def get_chat_history(self, chat_id: str, count: int = 100) -> dict:
        """
        Get chat history
        
        Args:
            chat_id: WhatsApp chat ID
            count: Number of messages to retrieve (default 100)
        """
        url = self.get_url("getChatHistory")
        payload = {
            'chatId': chat_id,
            'count': count
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as resp:
                res_dict = await resp.json()
                return res_dict

    async def forward_messages(self, chat_id: str, chat_id_from: str, messages: list):
        """
        Forward messages
        
        Args:
            chat_id: Target WhatsApp chat ID
            chat_id_from: Source WhatsApp chat ID
            messages: List of message IDs to forward
        """
        try:
            url = self.get_url("forwardMessages")
            payload = {
                'chatId': chat_id,
                'chatIdFrom': chat_id_from,
                'messages': messages
            }
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload) as resp:
                    res_dict = await resp.json()
                    return res_dict
        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())
            return {'error': True, 'message': str(e)}

    async def send_contact(self, chat_id: str, contact_phone: str, contact_name: str):
        """
        Send contact
        
        Args:
            chat_id: WhatsApp chat ID
            contact_phone: Contact phone number
            contact_name: Contact name
        """
        try:
            url = self.get_url("sendContact")
            payload = {
                'chatId': chat_id,
                'contact': {
                    'phoneContact': contact_phone,
                    'firstName': contact_name
                }
            }
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload) as resp:
                    res_dict = await resp.json()
                    return res_dict
        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())
            return {'error': True, 'message': str(e)}

    async def send_location(self, chat_id: str, latitude: float, longitude: float, name_location: str = '', address: str = ''):
        """
        Send location
        
        Args:
            chat_id: WhatsApp chat ID
            latitude: Location latitude
            longitude: Location longitude
            name_location: Optional location name
            address: Optional address
        """
        try:
            url = self.get_url("sendLocation")
            payload = {
                'chatId': chat_id,
                'latitude': latitude,
                'longitude': longitude
            }
            if name_location:
                payload['nameLocation'] = name_location
            if address:
                payload['address'] = address
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload) as resp:
                    res_dict = await resp.json()
                    return res_dict
        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())
            return {'error': True, 'message': str(e)}

    async def get_settings(self) -> dict:
        """Get instance settings"""
        url = self.get_url("getSettings")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()

    async def set_settings(self, settings: dict) -> dict:
        """
        Set instance settings
        
        Args:
            settings: Dictionary with settings to update
        """
        url = self.get_url("setSettings")
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=settings) as resp:
                return await resp.json()

    async def logout(self) -> dict:
        """Logout from instance"""
        url = self.get_url("logout")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()

    async def reboot(self) -> dict:
        """Reboot instance"""
        url = self.get_url("reboot")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()

    async def get_qr_code(self) -> dict:
        """Get QR code for authentication"""
        url = self.get_url("qr")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()
