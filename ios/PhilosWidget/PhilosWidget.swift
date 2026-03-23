import WidgetKit
import SwiftUI

struct QuoteEntry: TimelineEntry {
    let date: Date
    let quoteText: String
    let quoteAuthor: String
}

struct QuoteProvider: TimelineProvider {
    func placeholder(in context: Context) -> QuoteEntry {
        QuoteEntry(date: Date(), quoteText: "A felicidade da sua vida depende da qualidade dos seus pensamentos.", quoteAuthor: "Marco Aurélio")
    }

    func getSnapshot(in context: Context, completion: @escaping (QuoteEntry) -> Void) {
        let entry = QuoteEntry(
            date: Date(),
            quoteText: getWidgetData("quote_text") ?? "Toque para atualizar",
            quoteAuthor: getWidgetData("quote_author") ?? ""
        )
        completion(entry)
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<QuoteEntry>) -> Void) {
        let entry = QuoteEntry(
            date: Date(),
            quoteText: getWidgetData("quote_text") ?? "Toque para atualizar",
            quoteAuthor: getWidgetData("quote_author") ?? ""
        )
        let nextUpdate = Calendar.current.date(byAdding: .hour, value: 1, to: Date())!
        let timeline = Timeline(entries: [entry], policy: .after(nextUpdate))
        completion(timeline)
    }

    private func getWidgetData(_ key: String) -> String? {
        let defaults = UserDefaults(suiteName: "group.com.gambitstudio.philos")
        return defaults?.string(forKey: key)
    }
}

struct PhilosWidgetEntryView: View {
    var entry: QuoteEntry

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Spacer()
            Text("\u{201C}\(entry.quoteText)\u{201D}")
                .font(.system(size: 14, design: .serif))
                .italic()
                .foregroundColor(.white)
                .lineLimit(6)
                .minimumScaleFactor(0.8)
            if !entry.quoteAuthor.isEmpty {
                HStack {
                    Spacer()
                    Text("— \(entry.quoteAuthor)")
                        .font(.system(size: 12))
                        .foregroundColor(Color(red: 0.56, green: 0.56, blue: 0.58))
                        .lineLimit(1)
                }
            }
        }
        .padding(16)
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color(red: 0.11, green: 0.11, blue: 0.12))
        .cornerRadius(20)
    }
}

@main
struct PhilosWidget: Widget {
    let kind: String = "PhilosWidget"

    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: QuoteProvider()) { entry in
            PhilosWidgetEntryView(entry: entry)
        }
        .configurationDisplayName("Philos")
        .description("Frase filosófica aleatória")
        .supportedFamilies([.systemSmall, .systemMedium])
    }
}
