// === Note Repository ===

import 'package:shared_preferences/shared_preferences.dart';
import '../models/note_model.dart';

class NoteRepository {
  // === Constants ===
  static const _key = 'notes_list';

  // === Public Methods ===
  Future<List<NoteModel>> getNotes() async {
    final prefs = await SharedPreferences.getInstance();
    final jsonStr = prefs.getString(_key);
    if (jsonStr == null || jsonStr.isEmpty) return [];
    return NoteModel.listFromJson(jsonStr);
  }

  Future<void> addNote(NoteModel note) async {
    final notes = await getNotes();
    notes.insert(0, note);
    await _save(notes);
  }

  Future<void> updateNote(NoteModel updated) async {
    final notes = await getNotes();
    final index = notes.indexWhere((n) => n.id == updated.id);
    if (index != -1) {
      notes[index] = updated;
      await _save(notes);
    }
  }

  Future<void> deleteNote(String id) async {
    final notes = await getNotes();
    notes.removeWhere((n) => n.id == id);
    await _save(notes);
  }

  // === Private ===
  Future<void> _save(List<NoteModel> notes) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(_key, NoteModel.listToJson(notes));
  }
}
