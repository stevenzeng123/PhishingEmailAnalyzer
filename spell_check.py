from enchant.tokenize import get_tokenizer, URLFilter, HTMLChunker
import language_tool_python
from enchant.checker import SpellChecker


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

def process_body(Body):
        token = get_tokenizer("en_US", filters=[URLFilter], chunkers=(HTMLChunker,))
        token_input = token(Body)
        words = [word for word, pos in token_input]
        filtered_words = ' '.join(words)
        return filtered_words

def spell_grammar_check(filtered_words):
        spell = SpellChecker("en_US")
        spell.set_text(filtered_words)
        grammar = language_tool_python.LanguageTool("en-US")
        gram_check = grammar.check(filtered_words)
        for err in spell:
            print("Spelling Error:", err.word)
        for err in gram_check:
            print("Grammatical Error:", err.message)