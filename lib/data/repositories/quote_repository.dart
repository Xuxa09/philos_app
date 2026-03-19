// === Quote Repository ===

import 'dart:math';
import '../models/quote_model.dart';
import '../models/category_model.dart';
import '../services/mock_data_provider.dart';
import '../services/storage_service.dart';

class QuoteRepository {
  // === Dependencies ===
  final _storage = StorageService.instance;

  // === Public Methods ===
  List<QuoteModel> getDailyQuotes() {
    final allQuotes = MockDataProvider.quotes;
    final seed =
        DateTime.now().day + DateTime.now().month + DateTime.now().year;
    final shuffled = List<QuoteModel>.from(allQuotes)
      ..shuffle(Random(seed));
    return shuffled.take(3).toList();
  }

  QuoteModel getQuoteOfDay() {
    final allQuotes = MockDataProvider.quotes;
    final index =
        (DateTime.now().day + DateTime.now().month) % allQuotes.length;
    return allQuotes[index];
  }

  List<QuoteModel> getQuotesByCategory(QuoteCategory category) {
    return MockDataProvider.quotes
        .where((q) => q.category == category.name)
        .toList();
  }

  List<QuoteModel> getAllQuotes() => MockDataProvider.quotes;

  List<QuoteModel> getMoreQuotes(int offset) {
    final all = MockDataProvider.quotes;
    if (offset >= all.length) return [];
    return all.sublist(offset);
  }

  // === Favorites ===
  List<String> getFavoriteIds() => _storage.favoriteIds;

  Future<void> toggleFavorite(String id) async {
    final ids = List<String>.from(_storage.favoriteIds);
    if (ids.contains(id)) {
      ids.remove(id);
    } else {
      ids.add(id);
    }
    await _storage.saveFavoriteIds(ids);
  }

  bool isFavorite(String id) => _storage.favoriteIds.contains(id);

  List<QuoteModel> getFavoriteQuotes() {
    final ids = _storage.favoriteIds;
    return MockDataProvider.quotes
        .where((q) => ids.contains(q.id))
        .toList();
  }

}
