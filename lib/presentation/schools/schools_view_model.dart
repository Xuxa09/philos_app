import 'package:flutter/material.dart';
import '../../data/models/category_model.dart';
import '../../data/models/quote_model.dart';
import '../../data/repositories/quote_repository.dart';

class SchoolsViewModel extends ChangeNotifier {
  final QuoteRepository _repository = QuoteRepository();
  late QuoteCategory _selectedSchool;
  List<QuoteModel> _quotes = [];
  String _searchQuery = '';

  SchoolsViewModel() {
    _selectedSchool = QuoteCategory.stoicism;
    _quotes = _repository.getQuotesByCategory(_selectedSchool);
  }

  QuoteCategory get selectedSchool => _selectedSchool;
  List<QuoteModel> get quotes => _filteredQuotes;
  List<QuoteCategory> get schools => QuoteCategory.values;

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

  void selectSchool(QuoteCategory school) {
    _selectedSchool = school;
    _quotes = _repository.getQuotesByCategory(school);
    notifyListeners();
  }

  bool isFavorite(String id) => _repository.isFavorite(id);

  Future<void> toggleFavorite(String id) async {
    await _repository.toggleFavorite(id);
    notifyListeners();
  }
}
