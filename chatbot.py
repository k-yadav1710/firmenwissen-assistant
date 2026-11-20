from document_loader import load_document
from search import search

text = load_document("documents/mitarbeiterhandbuch.txt")
lines = text.splitlines()

print("Firmenwissen-Assistent. Tippe 'exit' zum Beenden.")

while True:
    question = input("Deine Frage: ")

    if question == "exit":
        break

    results = search(question, lines)

    if results == []:
        print("Keine passende Information gefunden.")
    else:
        for line in results:
            print("-", line)