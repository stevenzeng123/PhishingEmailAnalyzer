import API
import spell_check
import extract_info
import check_keywords
from OTXv2 import OTXv2
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

file_path = input("Enter file path: ")
file_path = file_path.replace('"', '')

OTX_SERVER = 'https://otx.alienvault.com/'
otx = OTXv2(API_KEY, server=OTX_SERVER)

msg = extract_info.read_file(file_path)
Body = extract_info.get_body(msg)

check_domain = extract_info.extract_domain(msg)
check_ip = extract_info.extract_ip(msg)
hashed = extract_info.get_hash(msg)
check_url = extract_info.extract_url(Body)

filtered_words = spell_check.process_body(Body)
spell_check.spell_grammar_check(filtered_words)

check_keywords.find_keywords(Body)

API.verify_domain(check_domain, otx)
API.verify_hash(hashed, otx)
API.verify_ip(check_ip, otx)
API.verify_url(check_url, otx)

