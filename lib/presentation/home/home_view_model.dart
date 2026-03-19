import 'package:flutter/material.dart';
import '../../data/models/quote_model.dart';
import '../../data/repositories/quote_repository.dart';
import '../../data/services/storage_service.dart';
import '../../data/services/review_service.dart';

class HomeViewModel extends ChangeNotifier {
  // === Dependencies ===
  final QuoteRepository _repository = QuoteRepository();
  final StorageService _storage = StorageService.instance;

  // === Properties ===
  List<QuoteModel> _dailyQuotes = [];
  QuoteModel? _quoteOfDay;
  bool _isLoading = true;
  bool _hasLoadedOnce = false;
  bool _showingMore = false;
  List<QuoteModel> _moreQuotes = [];

  // === Getters ===
  List<QuoteModel> get dailyQuotes => _dailyQuotes;
  QuoteModel? get quoteOfDay => _quoteOfDay;
  bool get isLoading => _isLoading;
  bool get showingMore => _showingMore;
  List<QuoteModel> get moreQuotes => _moreQuotes;

  // === Public Methods ===
  Future<void> loadData() async {
    if (_hasLoadedOnce) {
      _refreshSilently();
      return;
    }
    _isLoading = true;
    notifyListeners();
    await Future.delayed(const Duration(milliseconds: 600));
    _quoteOfDay = _repository.getQuoteOfDay();
    _dailyQuotes = _repository.getDailyQuotes();
    _hasLoadedOnce = true;
    _isLoading = false;
    notifyListeners();
    await _storage.incrementUsageCount();
    await ReviewService.instance.requestReviewIfAppropriate();
  }

  void loadMore() {
    _showingMore = true;
    _moreQuotes = _repository.getMoreQuotes(_dailyQuotes.length);
    notifyListeners();
  }

  bool isFavorite(String id) => _repository.isFavorite(id);

  Future<void> toggleFavorite(String id) async {
    await _repository.toggleFavorite(id);
    notifyListeners();
  }

  String getGreeting() {
    final hour = DateTime.now().hour;
    if (hour < 12) return 'morning';
    if (hour < 18) return 'afternoon';
    return 'evening';
  }

  // === Private Methods ===
  void _refreshSilently() {
    _quoteOfDay = _repository.getQuoteOfDay();
    _dailyQuotes = _repository.getDailyQuotes();
    notifyListeners();
  }
}
