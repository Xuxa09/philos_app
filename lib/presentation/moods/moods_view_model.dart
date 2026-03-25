import 'package:flutter/material.dart';
import '../../data/models/quote_model.dart';
import '../../data/models/mood_model.dart';
import '../../data/repositories/quote_repository.dart';
import '../../data/services/moods_data.dart';

class MoodsViewModel extends ChangeNotifier {
  final QuoteRepository _repository = QuoteRepository();
  late MoodType _selectedMood;
  List<QuoteModel> _quotes = [];
  String _searchQuery = '';

  MoodsViewModel() {
    _selectedMood = MoodType.unmotivated;
    _quotes = MoodsData.moods[_selectedMood.name] ?? [];
  }

  MoodType get selectedMood => _selectedMood;
  List<QuoteModel> get quotes => _filteredQuotes;
  List<MoodType> get moods => MoodType.values;

  List<QuoteModel> get _filteredQuotes {
    if (_searchQuery.isEmpty) return _quotes;
    final q = _searchQuery.toLowerCase();
    return _quotes.where((quote) =>
      quote.textPt.toLowerCase().contains(q) ||
      quote.textEn.toLowerCase().contains(q) ||
      quote.textEs.toLowerCase().contains(q) ||
      quote.authorPt.toLowerCase().contains(q) ||
      quote.authorEn.toLowerCase().contains(q) ||
      quote.authorEs.toLowerCase().contains(q)
    ).toList();
  }

  void search(String query) {
    _searchQuery = query;
    notifyListeners();
  }

  void selectMood(MoodType mood) {
    _selectedMood = mood;
    _quotes = MoodsData.moods[mood.name] ?? [];
    notifyListeners();
  }

  bool isFavorite(String id) => _repository.isFavorite(id);

  Future<void> toggleFavorite(String id) async {
    await _repository.toggleFavorite(id);
    notifyListeners();
  }
}
