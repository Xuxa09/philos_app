import 'package:flutter/material.dart';
import '../../data/models/quote_model.dart';
import '../../data/models/mood_model.dart';
import '../../data/repositories/quote_repository.dart';
import '../../data/services/moods_data.dart';

class MoodsViewModel extends ChangeNotifier {
  final QuoteRepository _repository = QuoteRepository();
  late MoodType _selectedMood;
  List<QuoteModel> _quotes = [];

  MoodsViewModel() {
    _selectedMood = MoodType.unmotivated;
    _quotes = MoodsData.moods[_selectedMood.name] ?? [];
  }

  MoodType get selectedMood => _selectedMood;
  List<QuoteModel> get quotes => _quotes;
  List<MoodType> get moods => MoodType.values;

  void selectMood(MoodType mood) {
    _selectedMood = mood;
    _quotes = MoodsData.moods[mood.name] ?? [];
    notifyListeners();
  }

  bool isFavorite(String id) => _repository.isFavorite(id);

  Future<void> toggleFavorite(String id) async {
    await _repository.toggleFavorite(id);
    notifyListeners();
  }
}
