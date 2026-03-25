import 'package:flutter/material.dart';
import '../../data/models/category_model.dart';
import '../../data/models/quote_model.dart';
import '../../data/repositories/quote_repository.dart';

class SchoolsViewModel extends ChangeNotifier {
  final QuoteRepository _repository = QuoteRepository();
  late QuoteCategory _selectedSchool;
  List<QuoteModel> _quotes = [];

  SchoolsViewModel() {
    _selectedSchool = QuoteCategory.stoicism;
    _quotes = _repository.getQuotesByCategory(_selectedSchool);
  }

  QuoteCategory get selectedSchool => _selectedSchool;
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
