import 'package:flutter/material.dart';
import '../../data/models/quote_model.dart';
import '../../data/repositories/quote_repository.dart';

class FavoritesViewModel extends ChangeNotifier {
  final QuoteRepository _repository = QuoteRepository();
  List<QuoteModel> _favorites = [];
  bool _isLoading = true;
  bool _hasLoadedOnce = false;

  List<QuoteModel> get favorites => _favorites;
  bool get isLoading => _isLoading;
  bool get isEmpty => _favorites.isEmpty && !_isLoading;

  Future<void> loadFavorites() async {
    if (_hasLoadedOnce) { _favorites = _repository.getFavoriteQuotes(); notifyListeners(); return; }
    _isLoading = true; notifyListeners();
    await Future.delayed(const Duration(milliseconds: 300));
    _favorites = _repository.getFavoriteQuotes();
    _hasLoadedOnce = true; _isLoading = false; notifyListeners();
  }

  Future<void> toggleFavorite(String id) async {
    await _repository.toggleFavorite(id);
    _favorites = _repository.getFavoriteQuotes();
    notifyListeners();
  }
}
