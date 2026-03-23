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
            quoteText: getWidgetData("quote_text") ?? "Toque para abrir o Philos",
            quoteAuthor: getWidgetData("quote_author") ?? ""
        )
        completion(entry)
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<QuoteEntry>) -> Void) {
        let entry = QuoteEntry(
            date: Date(),
            quoteText: getWidgetData("quote_text") ?? "Toque para abrir o Philos",
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
        ZStack {
            // Background with subtle gradient
            Color(red: 0.11, green: 0.11, blue: 0.12)
            LinearGradient(
                gradient: Gradient(colors: [
                    Color(red: 0.04, green: 0.52, blue: 1.0).opacity(0.1),
                    Color(red: 0.39, green: 0.82, blue: 1.0).opacity(0.03)
                ]),
                startPoint: .topLeading,
                endPoint: .bottomTrailing
            )
        }
        .overlay(
            VStack(alignment: .leading, spacing: 0) {
                // Header
                HStack(spacing: 4) {
                    Text("\u{275D}")
                        .font(.system(size: 16))
                        .foregroundColor(Color(red: 0.04, green: 0.52, blue: 1.0))
                    Text("Philos")
                        .font(.system(size: 11, weight: .medium))
                        .foregroundColor(Color(red: 0.39, green: 0.39, blue: 0.40))
                        .tracking(0.5)
                    Spacer()
                }
                .padding(.bottom, 10)

                // Quote
                Spacer()
                Text("\u{201C}\(entry.quoteText)\u{201D}")
                    .font(.system(size: 14, design: .serif))
                    .italic()
                    .foregroundColor(.white)
                    .lineSpacing(4)
                    .lineLimit(5)
                    .minimumScaleFactor(0.8)
                Spacer()

                // Author
                if !entry.quoteAuthor.isEmpty {
                    HStack {
                        Spacer()
                        Text("— \(entry.quoteAuthor)")
                            .font(.system(size: 12, weight: .medium))
                            .foregroundColor(Color(red: 0.04, green: 0.52, blue: 1.0))
                            .lineLimit(1)
                    }
                    .padding(.top, 8)
                }
            }
            .padding(18)
        )
        .cornerRadius(24)
    }
}

@main
struct PhilosWidget: Widget {
    let kind: String = "PhilosWidget"

    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: QuoteProvider()) { entry in
            PhilosWidgetEntryView(entry: entry)
                .widgetURL(URL(string: "philos://"))
        }
        .configurationDisplayName("Philos")
        .description("Frase filosófica aleatória")
        .supportedFamilies([.systemSmall, .systemMedium])
    }
}
