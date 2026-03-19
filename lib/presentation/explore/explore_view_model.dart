import 'package:flutter/material.dart';
import '../../data/models/category_model.dart';
import '../../data/models/quote_model.dart';
import '../../data/repositories/quote_repository.dart';

class ExploreViewModel extends ChangeNotifier {
  final QuoteRepository _repository = QuoteRepository();
  QuoteCategory? _selectedCategory;
  List<QuoteModel> _quotes = [];
  bool _isLoading = true;
  bool _hasLoadedOnce = false;

  QuoteCategory? get selectedCategory => _selectedCategory;
  List<QuoteModel> get quotes => _quotes;
  bool get isLoading => _isLoading;
  List<QuoteCategory> get categories => QuoteCategory.values;

  Future<void> loadData() async {
    if (_hasLoadedOnce) { _refreshSilently(); return; }
    _isLoading = true;
    notifyListeners();
    await Future.delayed(const Duration(milliseconds: 400));
    _quotes = _repository.getAllQuotes();
    _hasLoadedOnce = true;
    _isLoading = false;
    notifyListeners();
  }

  void selectCategory(QuoteCategory? category) {
    if (_selectedCategory == category) {
      _selectedCategory = null;
      _quotes = _repository.getAllQuotes();
    } else {
      _selectedCategory = category;
      _quotes = category != null ? _repository.getQuotesByCategory(category) : _repository.getAllQuotes();
    }
    notifyListeners();
  }

  bool isFavorite(String id) => _repository.isFavorite(id);

  Future<void> toggleFavorite(String id) async {
    await _repository.toggleFavorite(id);
    notifyListeners();
  }

  void _refreshSilently() {
    _quotes = _selectedCategory != null ? _repository.getQuotesByCategory(_selectedCategory!) : _repository.getAllQuotes();
    notifyListeners();
  }
}
