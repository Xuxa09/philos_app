import 'package:flutter/material.dart';
import '../../data/models/category_model.dart';
import '../../data/models/quote_model.dart';
import '../../data/repositories/quote_repository.dart';

class AuthorsViewModel extends ChangeNotifier {
  final QuoteRepository _repository = QuoteRepository();
  String? _selectedAuthor;
  List<QuoteModel> _quotes = [];

  AuthorsViewModel() {
    final authors = _repository.getUniqueAuthors();
    if (authors.isNotEmpty) {
      _selectedAuthor = authors.first;
      _quotes = _repository.getQuotesByAuthor(_selectedAuthor!);
    }
  }

  String? get selectedAuthor => _selectedAuthor;
  List<QuoteModel> get quotes => _quotes;

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
