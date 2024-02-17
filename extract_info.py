import pandas as pd
from email.parser import BytesParser
from email.policy import default
from enchant.checker import SpellChecker
from enchant.tokenize import get_tokenizer, URLFilter, HTMLChunker
import language_tool_python
import base64
import hashlib
from OTXv2 import OTXv2
import re 

def read_file(file_path):
        with open(file_path, 'rb') as file:
            content = file.read()
            parser = BytesParser(policy=default)
            msg = parser.parsebytes(content)
            return msg

def extract_domain(msg):
        sender = msg['From']
        domain = sender.split("@")
        check_domain = domain[1].rstrip('>')
        return check_domain

def extract_ip(msg):
        received_header = msg.get_all('Received', [])
        pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
        check_ip = []
        for received in received_header:
            matches = pattern.findall(received)
            check_ip.extend(matches)
        if not check_ip:
            print('No IP address detected')
        return check_ip

def get_attachment(msg):
        attachments_base64 = []
        if msg.is_multipart():
            for part in msg.walk():
                if part.get('Content-Transfer-Encoding') == 'base64':
                    attachment_content= part.get_payload()
                    attachments_base64.append(attachment_content)
        else:
            part.get('Content-Transfer-Encoding') == 'base64'
            attachment_content= part.get_payload()
            attachments_base64.append(attachment_content)
        return attachments_base64

def calculate_hash(msg):
        attachment_list = get_attachment(msg)
        hashing = []
        for attachment in attachment_list:
            decoded = base64.b64decode(attachment)
            hash = hashlib.sha256()
            hash.update(decoded)
            hashing.append(hash.hexdigest())
        return hashing
            
def get_hash(msg):
        if get_attachment(msg): 
            hashed = calculate_hash(msg)
        else:
            hashed = []
            print("No attachment detected")
        return hashed

def get_body(msg):
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body += part.get_payload(decode=True).decode()
        else:
                if msg.get_content_type() == 'text/plain':
                    body += msg.get_payload(decode=True).decode()
        return body

def extract_url(Body):
        urlRegex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(urlRegex, Body)
        check_url =  [x[0] for x in url]
        if not check_url:
            print("No URLs detected")
        return check_url




   