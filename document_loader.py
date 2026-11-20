def load_document(path):
    try:
        with open(path, encoding="utf-8") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Dokument nicht gefunden: {path}")
        return None


if __name__ == "__main__":
    text = load_document("documents/mitarbeiterhandbuch.txt")
    print(text)

    missing = load_document("documents/gibtsnicht.txt")
    print(missing)