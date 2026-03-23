import 'package:flutter/material.dart';
import '../../data/models/category_model.dart';
import '../../data/models/quote_model.dart';
import '../../data/repositories/quote_repository.dart';

class SchoolsViewModel extends ChangeNotifier {
  final QuoteRepository _repository = QuoteRepository();
  QuoteCategory? _selectedSchool;
  List<QuoteModel> _quotes = [];

  QuoteCategory? get selectedSchool => _selectedSchool;
  List<QuoteModel> get quotes => _quotes;
  List<QuoteCategory> get schools => QuoteCategory.values;

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
