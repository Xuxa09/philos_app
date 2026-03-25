import 'package:flutter/material.dart';
import '../../data/models/category_model.dart';
import '../../data/models/quote_model.dart';
import '../../data/repositories/quote_repository.dart';

class AuthorsViewModel extends ChangeNotifier {
  final QuoteRepository _repository = QuoteRepository();
  String? _selectedAuthor;
  List<QuoteModel> _quotes = [];
  String _searchQuery = '';

  AuthorsViewModel() {
    final authors = _repository.getUniqueAuthors();
    if (authors.isNotEmpty) {
      _selectedAuthor = authors.first;
      _quotes = _repository.getQuotesByAuthor(_selectedAuthor!);
    }
  }

  String? get selectedAuthor => _selectedAuthor;
  List<QuoteModel> get quotes => _filteredQuotes;

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

  List<AuthorInfo> getAuthors(String locale) {
    return _repository.getUniqueAuthors().map((authorEn) {
      final sample = _repository.getQuotesByAuthor(authorEn).first;
      final cat = QuoteCategory.values.where((c) => c.name == sample.category).firstOrNull;
      return AuthorInfo(
        key: authorEn,
        name: sample.author(locale),
        icon: cat?.icon ?? Icons.person,
        color: cat?.color ?? const Color(0xFF8E8E93),
      );
    }).toList();
  }

  void selectAuthor(String authorEn) {
    _selectedAuthor = authorEn;
    _quotes = _repository.getQuotesByAuthor(authorEn);
    notifyListeners();
  }

  bool isFavorite(String id) => _repository.isFavorite(id);

  Future<void> toggleFavorite(String id) async {
    await _repository.toggleFavorite(id);
    notifyListeners();
  }
}

class AuthorInfo {
  final String key;
  final String name;
  final IconData icon;
  final Color color;

  const AuthorInfo({required this.key, required this.name, required this.icon, required this.color});
}
