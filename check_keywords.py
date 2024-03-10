import re


def find_keywords(email_body, spam_words_file = 'spam_words.txt'):
    with open(spam_words_file, 'r') as file:
        spam_words = [line.strip() for line in file.readlines()]
        
    email_body_normalized = re.sub(r'[^\w\s]', '', email_body).lower()

    found_spam_words = set()

    for word in spam_words:
        if re.search(r'\b' + re.escape(word.lower()) + r'\b', email_body_normalized):
            found_spam_words.add(word)

    print("Phishing/Spam Trigger Words Identified:", found_spam_words)
    

