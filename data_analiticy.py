import pandas as pd

authors_schools = {
    "Epicurus": "Epicurismo",
    "Albert Camus": "Existencialismo / Absurdismo",
    "Seneca": "Estoicismo",
    "Marcus Aurelius": "Estoicismo",
    "William James": "Pragmatismo",
    "Plato": "Platonismo",
    "Epictetus": "Estoicismo",
    "Aristotle": "Peripatético / Aristotelismo",
    "Socrates": "Filosofia Socrática",
    "Lucretius": "Epicurismo",
    "Ralph Waldo Emerson": "Transcendentalismo",
    "Lao Tzu": "Taoismo",
    "John Dewey": "Pragmatismo",
    "Friedrich Nietzsche": "Niilismo / Existencialismo (precursor)",
    "Confucius": "Confucionismo",
    "Buddha": "Budismo",
    "Simone de Beauvoir": "Existencialismo / Feminismo",
    "Jean-Paul Sartre": "Existencialismo",
    "Immanuel Kant": "Idealismo Transcendental",
    "Franz Kafka": "Existencialismo (influência) / Absurdo",
    "Baruch Spinoza": "Racionalismo",
    "Sun Tzu": "Filosofia Militar Chinesa",
    "Samuel Beckett": "Teatro do Absurdo",
    "Søren Kierkegaard": "Existencialismo Cristão",
    "Martin Heidegger": "Fenomenologia / Existencialismo",
    "Blaise Pascal": "Jansenismo / Existencialismo Cristão (precursor)",
    "René Descartes": "Racionalismo",
    "Eugène Ionesco": "Teatro do Absurdo",
    "Horace": "Epicurismo (influência)",
    "Gottfried Wilhelm Leibniz": "Racionalismo",
    "Georg Hegel": "Idealismo Alemão",
    "Heraclitus": "Pré-socrático",
    "Richard Rorty": "Neopragmatismo",
    "Charles Sanders Peirce": "Pragmatismo",
    "Thomas Nagel": "Filosofia Analítica",
    "Rumi": "Sufismo",
    "Philodemus": "Epicurismo",
    "Metrodorus": "Epicurismo",
    "Diogenes": "Cinismo",
}

df = pd.read_csv('c:/Users/lalli/Flutter/coach_phrase_app/quotes.csv')
df = df[df['author'].isin(authors_schools.keys())]
df['escola'] = df['author'].map(authors_schools)

df.to_csv('c:/Users/lalli/Flutter/coach_phrase_app/phrases.csv', index=False)
