Python script that analyzes emails for common phishing indicators. Takes in an email file and extracts URLs, domain names, IP addresses, and attached files. Uses AlienVault's Open Threat Exchange (OTX) database to determine if those factors have been identified as malicious. Also runs a spell/grammar check on the email, to detect grammatical errors common in phishing emails.

Instructions to load in your own AlienVault OTX API Key:
1. Open a Text Editor: Use any text editor like Notepad, Visual Studio Code, or Sublime Text.
2. Enter API Key Information: Type API_KEY=your_api_key_here, replacing your_api_key_here with your actual API key.
3. Save the File: Save the file in the root directory of the project where it's needed. Name the file .env and choose "All Files" as the file type if your editor asks.
4. Add .env to .gitignore: Ensure .env is listed in your project's .gitignore file to prevent it from being uploaded to version control.

