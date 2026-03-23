import 'package:flutter/material.dart';
import '../../data/models/category_model.dart';
import '../../data/models/quote_model.dart';
import '../../data/repositories/quote_repository.dart';

class ExploreViewModel extends ChangeNotifier {
  final QuoteRepository _repository = QuoteRepository();

  String _searchQuery = '';
  String _locale = 'pt';
  List<QuoteModel> _quotes = [];
  bool _isLoading = true;
  bool _hasLoadedOnce = false;

  String get searchQuery => _searchQuery;
  List<QuoteModel> get quotes => _quotes;
  bool get isLoading => _isLoading;

  Future<void> loadData() async {
    if (_hasLoadedOnce) { _applyFilters(); return; }
    _isLoading = true;
    notifyListeners();
    await Future.delayed(const Duration(milliseconds: 400));
    _applyFilters();
    _hasLoadedOnce = true;
    _isLoading = false;
    notifyListeners();
  }

  void setSearchQuery(String query, String locale) {
    _searchQuery = query;
    _locale = locale;
    _applyFilters();
    notifyListeners();
  }

  bool isFavorite(String id) => _repository.isFavorite(id);

  Future<void> toggleFavorite(String id) async {
    await _repository.toggleFavorite(id);
    notifyListeners();
  }

  void _applyFilters() {
    List<QuoteModel> source = _repository.getAllQuotes();

    if (_searchQuery.isNotEmpty) {
      source = _repository.searchQuotes(source, _searchQuery, _locale);
    }

    _quotes = source;
  }
}
