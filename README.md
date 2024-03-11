Python script that analyzes emails for common phishing indicators. Parses an email file and extracts URLs, domain names, IP addresses, and attached files. Calculates the SHA256 hash value of the email attachment, from its base64 value, and uses it for verification. Utilizes AlienVault's Open Threat Exchange (OTX) database API to determine if any Indicators of Compromise (IOCs) have been identified as malicious. Also uses Natural Language Processing (NLP) techniques to run a spell/grammar check on the email, to detect grammatical errors common in phishing emails. Employs a list of 100 common phishing/spam email trigger words to check if they are contained within the email.

Instructions to load in your own AlienVault OTX API Key:
1. Open a Text Editor: Use any text editor like Notepad, Visual Studio Code, or Sublime Text.
2. Enter API Key Information: Type API_KEY=your_api_key_here, replacing your_api_key_here with your actual API key.
3. Save the File: Save the file in the root directory of the project where it's needed. Name the file .env and choose "All Files" as the file type if your editor asks.


