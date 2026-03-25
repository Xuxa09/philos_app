// === Quote Repository ===

import 'dart:math';
import '../models/quote_model.dart';
import '../models/category_model.dart';
import '../models/mood_model.dart';
import '../services/mock_data_provider.dart';
import '../services/moods_data.dart';
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
    return shuffled.take(6).toList();
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

  // === Philosopher Filtering ===
  List<String> getUniqueAuthors() {
    final authors = <String>{};
    for (final q in MockDataProvider.quotes) {
      authors.add(q.authorEn);
    }
    return authors.toList()..sort();
  }

  List<QuoteModel> getQuotesByAuthor(String authorEn) {
    return MockDataProvider.quotes
        .where((q) => q.authorEn == authorEn)
        .toList();
  }

  // === Mood Filtering ===
  List<QuoteModel> getQuotesByMood(MoodType mood) {
    return MoodsData.moods[mood.name] ?? [];
  }

  List<QuoteModel> getAllMoodQuotes() {
    return MoodsData.moods.values.expand((list) => list).toList();
  }

  // === Search ===
  List<QuoteModel> searchQuotes(List<QuoteModel> source, String query, String locale) {
    final terms = query.toLowerCase().split(RegExp(r'\s+')).where((t) => t.isNotEmpty).toList();
    if (terms.isEmpty) return source;

    return source.where((q) {
      final author = q.author(locale).toLowerCase();
      final text = q.text(locale).toLowerCase();
      final cat = QuoteCategory.values.where((c) => c.name == q.category).firstOrNull;
      final school = cat?.localizedName(locale).toLowerCase() ?? '';

      return terms.every((term) =>
        author.contains(term) || text.contains(term) || school.contains(term)
      );
    }).toList();
  }
}
