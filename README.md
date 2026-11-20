# firmenwissen-assistant
AI assistant that answers questions from company documents (in development)
## How it works (v0.1)
- `document_loader.py` reads the handbook into a text
- `chatbot.py` splits it into lines and asks the user for questions
- `search.py` cleans the question (lowercase, no punctuation), splits it into words
  and returns every line that contains one of the words

## Known limitations of keyword search
- Words match inside other words: "ich" matches "möglich", "wo" matches "Woche"
- No synonyms: "von zu Hause arbeiten" does not find "Homeoffice"
- No real answer: the bot shows lines, it does not answer the question

These limitations are the reason for the next versions:
Claude for real answers  and embeddings for meaning-based search .