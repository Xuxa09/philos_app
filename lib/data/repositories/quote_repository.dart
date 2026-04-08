// === Quote Repository ===

import 'dart:math';
import '../models/quote_model.dart';
import '../models/category_model.dart';
import '../models/mood_model.dart';
import '../services/mock_data_provider.dart';
import '../services/storage_service.dart';

class QuoteRepository {
  // === Dependencies ===
  final _storage = StorageService.instance;

  // === Locale-aware quotes ===
  String get _currentLocale => _storage.selectedLocale ?? 'pt';

  List<QuoteModel> get _quotes => MockDataProvider.quotes
      .where((q) => q.isTranslated(_currentLocale))
      .toList();

  // === Public Methods ===
  List<QuoteModel> getDailyQuotes() {
    final allQuotes = _quotes;
    final seed =
        DateTime.now().day + DateTime.now().month + DateTime.now().year;
    final shuffled = List<QuoteModel>.from(allQuotes)
      ..shuffle(Random(seed));
    return shuffled.take(6).toList();
  }

  QuoteModel getQuoteOfDay() {
    final allQuotes = _quotes;
    final index =
        (DateTime.now().day + DateTime.now().month) % allQuotes.length;
    return allQuotes[index];
  }

  List<QuoteModel> getQuotesByCategory(QuoteCategory category) {
    return _quotes
        .where((q) => q.category == category.name)
        .toList();
  }

  List<QuoteModel> getAllQuotes() => _quotes;

  List<QuoteModel> getMoreQuotes(int offset) {
    final all = _quotes;
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
    return _quotes
        .where((q) => ids.contains(q.id))
        .toList();
  }

  // === Philosopher Filtering ===
  List<String> getUniqueAuthors() {
    final authors = <String>{};
    for (final q in _quotes) {
      authors.add(q.authorEn);
    }
    return authors.toList()..sort();
  }

  List<QuoteModel> getQuotesByAuthor(String authorEn) {
    return _quotes
        .where((q) => q.authorEn == authorEn)
        .toList();
  }

  // === Mood Filtering ===
  List<QuoteModel> getQuotesByMood(MoodType mood) {
    return _quotes
        .where((q) => q.moods.contains(mood.name))
        .toList();
  }

  List<QuoteModel> getAllMoodQuotes() {
    return _quotes
        .where((q) => q.moods.isNotEmpty)
        .toList();
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
