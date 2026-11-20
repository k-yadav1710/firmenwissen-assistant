def search(question, lines):
    cleaned = question.lower()
    for sign in "?!.,":
        cleaned = cleaned.replace(sign, "")
    words = cleaned.split()

    results = []
    for line in lines:
        line_lower = line.lower()
        for word in words:
            if word in line_lower:
                results.append(line)
                break

    return results


if __name__ == "__main__":
    test_lines = [
        "Jeder Mitarbeiter erhält 30 Urlaubstage pro Jahr.",
        "Homeoffice ist an bis zu zwei Tagen pro Woche möglich.",
        "Die Kantine ist von 11:30 bis 14:00 Uhr geöffnet.",
    ]
    print(search("Wie viele Urlaubstage habe ich?", test_lines))
    print(search("Raumschiff?", test_lines))