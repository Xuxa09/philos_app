import 'package:flutter/material.dart';
import '../../data/models/quote_model.dart';
import '../../data/repositories/quote_repository.dart';

class ExploreViewModel extends ChangeNotifier {
  final QuoteRepository _repository = QuoteRepository();

  String _searchQuery = '';
  List<QuoteModel> _allQuotes = [];
  List<QuoteModel> _filteredQuotes = [];
  bool _isLoading = true;
  bool _hasLoadedOnce = false;

  String get searchQuery => _searchQuery;
  List<QuoteModel> get filteredQuotes => _filteredQuotes;
  bool get isLoading => _isLoading;
  bool get isSearching => _searchQuery.isNotEmpty;

  List<QuoteModel> get popularQuotes {
    final ids = _repository.getFavoriteIds();
    final favs = _allQuotes.where((q) => ids.contains(q.id)).toList();
    if (favs.length >= 3) return favs.take(6).toList();
    return _allQuotes.take(6).toList();
  }

  Future<void> loadData() async {
    if (_hasLoadedOnce) return;
    _isLoading = true;
    notifyListeners();
    await Future.delayed(const Duration(milliseconds: 400));
    _allQuotes = _repository.getAllQuotes();
    _hasLoadedOnce = true;
    _isLoading = false;
    notifyListeners();
  }

  void setSearchQuery(String query, String locale) {
    _searchQuery = query;
    if (query.isEmpty) {
      _filteredQuotes = [];
    } else {
      _filteredQuotes = _repository.searchQuotes(_allQuotes, query, locale);
    }
    notifyListeners();
  }

  bool isFavorite(String id) => _repository.isFavorite(id);

  Future<void> toggleFavorite(String id) async {
    await _repository.toggleFavorite(id);
    notifyListeners();
  }
}
