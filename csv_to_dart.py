import csv
import re

# === Mapping: escola (CSV) → app category ===
ESCOLA_TO_CATEGORY = {
    "Estoicismo": "stoicism",
    "Platonismo": "classical",
    "Peripatético / Aristotelismo": "classical",
    "Filosofia Socrática": "classical",
    "Pré-socrático": "classical",
    "Cinismo": "classical",
    "Epicurismo": "epicureanism",
    "Epicurismo (influência)": "epicureanism",
    "Existencialismo": "existentialism",
    "Existencialismo / Absurdismo": "existentialism",
    "Existencialismo Cristão": "existentialism",
    "Existencialismo (influência) / Absurdo": "existentialism",
    "Existencialismo / Feminismo": "existentialism",
    "Fenomenologia / Existencialismo": "existentialism",
    "Niilismo / Existencialismo (precursor)": "existentialism",
    "Jansenismo / Existencialismo Cristão (precursor)": "existentialism",
    "Teatro do Absurdo": "absurdism",
    "Taoismo": "eastern",
    "Confucionismo": "eastern",
    "Budismo": "eastern",
    "Filosofia Militar Chinesa": "eastern",
    "Sufismo": "eastern",
    "Racionalismo": "rationalism",
    "Idealismo Transcendental": "rationalism",
    "Idealismo Alemão": "rationalism",
    "Filosofia Analítica": "rationalism",
    "Pragmatismo": "pragmatism",
    "Neopragmatismo": "pragmatism",
    "Transcendentalismo": "pragmatism",
}

def escape_dart(s):
    """Escape special characters for Dart single-quoted strings."""
    s = s.replace("\\", "\\\\")
    s = s.replace("'", "\\'")
    s = s.replace("\n", "\\n")
    s = s.replace("\r", "")
    return s

def main():
    quotes_by_category = {
        "stoicism": [],
        "classical": [],
        "existentialism": [],
        "eastern": [],
        "epicureanism": [],
        "rationalism": [],
        "absurdism": [],
        "pragmatism": [],
    }

    csv_path = "c:/Users/lalli/Flutter/coach_phrase_app/phrases.csv"

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        idx = 0
        skipped = 0
        for row in reader:
            escola = row.get("escola", "").strip()
            category = ESCOLA_TO_CATEGORY.get(escola)
            if not category:
                skipped += 1
                continue

            quote_text = row.get("quote", "").strip()
            author = row.get("author", "").strip()

            if not quote_text or not author:
                skipped += 1
                continue

            idx += 1
            quote_id = f"csv_{idx:04d}"

            quotes_by_category[category].append({
                "id": quote_id,
                "author": author,
                "text": quote_text,
                "category": category,
            })

    # Generate Dart file
    lines = []
    lines.append("// === Quotes Data ===")
    lines.append("// Generated from phrases.csv — do not edit manually")
    lines.append("")
    lines.append("import '../models/quote_model.dart';")
    lines.append("")
    lines.append("abstract class QuotesData {")

    for category, quotes in quotes_by_category.items():
        lines.append(f"  // === {category.capitalize()} ({len(quotes)} quotes) ===")
        lines.append(f"  static const List<QuoteModel> {category} = [")

        for q in quotes:
            text = escape_dart(q["text"])
            author = escape_dart(q["author"])
            cat = q["category"]
            qid = q["id"]

            lines.append(f"    QuoteModel(")
            lines.append(f"      id: '{qid}',")
            lines.append(f"      authorEn: '{author}', authorPt: '{author}', authorEs: '{author}',")
            lines.append(f"      textEn: '{text}',")
            lines.append(f"      textPt: '{text}',")
            lines.append(f"      textEs: '{text}',")
            lines.append(f"      reflectionEn: '',")
            lines.append(f"      reflectionPt: '',")
            lines.append(f"      reflectionEs: '',")
            lines.append(f"      category: '{cat}',")
            lines.append(f"    ),")

        lines.append(f"  ];")
        lines.append("")

    lines.append("}")
    lines.append("")

    out_path = "c:/Users/lalli/Flutter/coach_phrase_app/lib/data/services/quotes_data.dart"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # Print summary
    total = sum(len(q) for q in quotes_by_category.values())
    print(f"Generated {total} quotes ({skipped} skipped)")
    for cat, quotes in quotes_by_category.items():
        print(f"  {cat}: {len(quotes)}")

if __name__ == "__main__":
    main()
