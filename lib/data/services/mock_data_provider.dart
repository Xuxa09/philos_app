// === Mock Data Provider ===

import '../models/quote_model.dart';
import 'quotes_data.dart';

abstract class MockDataProvider {
  // === All Quotes (3625 total — 8 philosophical schools) ===
  static const List<QuoteModel> quotes = [
    ...QuotesData.stoicism,
    ...QuotesData.classical,
    ...QuotesData.existentialism,
    ...QuotesData.eastern,
    ...QuotesData.epicureanism,
    ...QuotesData.rationalism,
    ...QuotesData.absurdism,
    ...QuotesData.pragmatism,
  ];
}
