import 'dart:math';
import 'package:flutter/material.dart';
import '../../data/models/quote_model.dart';
import '../../data/models/note_model.dart';
import '../../data/repositories/note_repository.dart';
import '../../data/services/mock_data_provider.dart';

class JournalViewModel extends ChangeNotifier {
  final NoteRepository _repository = NoteRepository();
  List<NoteModel> _notes = [];
  bool _isLoading = true;
  bool _hasLoadedOnce = false;

  List<NoteModel> get notes => _notes;
  bool get isLoading => _isLoading;
  bool get isEmpty => _notes.isEmpty && !_isLoading;
  List<QuoteModel> get quotes => MockDataProvider.quotes;

  Future<void> loadNotes() async {
    if (_hasLoadedOnce) { _notes = await _repository.getNotes(); notifyListeners(); return; }
    _isLoading = true; notifyListeners();
    await Future.delayed(const Duration(milliseconds: 300));
    _notes = await _repository.getNotes();
    _hasLoadedOnce = true; _isLoading = false; notifyListeners();
  }

  Future<void> addNote(String text) async {
    final note = NoteModel(id: DateTime.now().millisecondsSinceEpoch.toString(), text: text, createdAt: DateTime.now());
    await _repository.addNote(note);
    _notes = await _repository.getNotes();
    notifyListeners();
  }

  Future<void> addReflection({required String text, required String quoteAuthor, required String quoteText}) async {
    final reflection = NoteModel(
      id: DateTime.now().millisecondsSinceEpoch.toString(), text: text, createdAt: DateTime.now(),
      quoteAuthor: quoteAuthor, quoteText: quoteText);
    await _repository.addNote(reflection);
    _notes = await _repository.getNotes();
    notifyListeners();
  }

  QuoteModel getRandomQuote() => quotes[Random().nextInt(quotes.length)];

  Future<void> updateNote(String id, String newText) async {
    final index = _notes.indexWhere((n) => n.id == id);
    if (index == -1) return;
    await _repository.updateNote(_notes[index].copyWith(text: newText));
    _notes = await _repository.getNotes();
    notifyListeners();
  }

  Future<void> deleteNote(String id) async {
    await _repository.deleteNote(id);
    _notes = await _repository.getNotes();
    notifyListeners();
  }
}
