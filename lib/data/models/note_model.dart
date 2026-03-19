// === Note Model ===

import 'dart:convert';

class NoteModel {
  // === Properties ===
  final String id;
  final String text;
  final DateTime createdAt;
  final String? quoteAuthor;
  final String? quoteText;

  // === Computed ===
  bool get isReflection => quoteAuthor != null;

  // === Constructor ===
  const NoteModel({
    required this.id,
    required this.text,
    required this.createdAt,
    this.quoteAuthor,
    this.quoteText,
  });

  // === Copy ===
  NoteModel copyWith({String? text}) {
    return NoteModel(
      id: id,
      text: text ?? this.text,
      createdAt: createdAt,
      quoteAuthor: quoteAuthor,
      quoteText: quoteText,
    );
  }

  // === JSON ===
  factory NoteModel.fromJson(Map<String, dynamic> json) {
    return NoteModel(
      id: json['id'] as String,
      text: json['text'] as String,
      createdAt: DateTime.parse(json['createdAt'] as String),
      quoteAuthor: json['quoteAuthor'] as String?,
      quoteText: json['quoteText'] as String?,
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'text': text,
    'createdAt': createdAt.toIso8601String(),
    if (quoteAuthor != null) 'quoteAuthor': quoteAuthor,
    if (quoteText != null) 'quoteText': quoteText,
  };

  // === Helpers ===
  static List<NoteModel> listFromJson(String jsonStr) {
    final List<dynamic> list = json.decode(jsonStr);
    return list
        .map((e) => NoteModel.fromJson(e as Map<String, dynamic>))
        .toList();
  }

  static String listToJson(List<NoteModel> notes) {
    return json.encode(notes.map((e) => e.toJson()).toList());
  }
}
