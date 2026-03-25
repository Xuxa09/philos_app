// === Mood Model ===

import 'package:flutter/material.dart';

enum MoodType {
  // === Values ===
  unmotivated(Icons.battery_1_bar, Color(0xFF3E6278)),
  anxious(Icons.psychology_alt, Color(0xFF8B6B28)),
  frustrated(Icons.sentiment_dissatisfied, Color(0xFF6B4888)),
  fearful(Icons.shield, Color(0xFF884848)),
  lost(Icons.explore_off, Color(0xFF4A7070)),
  grateful(Icons.favorite, Color(0xFF884040)),
  ambitious(Icons.rocket_launch, Color(0xFF4A6848)),
  tired(Icons.bedtime, Color(0xFF7A6B28));

  // === Properties ===
  final IconData icon;
  final Color color;

  const MoodType(this.icon, this.color);

  // === Localized Name ===
  String localizedName(String locale) {
    switch (this) {
      case MoodType.unmotivated:
        return locale == 'pt'
            ? 'Desanimado'
            : locale == 'es'
                ? 'Desanimado'
                : 'Unmotivated';
      case MoodType.anxious:
        return locale == 'pt'
            ? 'Ansioso'
            : locale == 'es'
                ? 'Ansioso'
                : 'Anxious';
      case MoodType.frustrated:
        return locale == 'pt'
            ? 'Frustrado'
            : locale == 'es'
                ? 'Frustrado'
                : 'Frustrated';
      case MoodType.fearful:
        return locale == 'pt'
            ? 'Com Medo'
            : locale == 'es'
                ? 'Con Miedo'
                : 'Fearful';
      case MoodType.lost:
        return locale == 'pt'
            ? 'Perdido'
            : locale == 'es'
                ? 'Perdido'
                : 'Lost';
      case MoodType.grateful:
        return locale == 'pt'
            ? 'Grato'
            : locale == 'es'
                ? 'Agradecido'
                : 'Grateful';
      case MoodType.ambitious:
        return locale == 'pt'
            ? 'Ambicioso'
            : locale == 'es'
                ? 'Ambicioso'
                : 'Ambitious';
      case MoodType.tired:
        return locale == 'pt'
            ? 'Cansado'
            : locale == 'es'
                ? 'Cansado'
                : 'Tired';
    }
  }
}
