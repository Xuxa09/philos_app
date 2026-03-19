// === Mood Model ===

import 'package:flutter/material.dart';

enum MoodType {
  // === Values ===
  unmotivated(Icons.battery_1_bar, Color(0xFF0A84FF)),
  anxious(Icons.psychology_alt, Color(0xFFFF9F0A)),
  frustrated(Icons.sentiment_dissatisfied, Color(0xFFBF5AF2)),
  fearful(Icons.shield, Color(0xFFFF453A)),
  lost(Icons.explore_off, Color(0xFF64D2FF)),
  grateful(Icons.favorite, Color(0xFFFF375F)),
  ambitious(Icons.rocket_launch, Color(0xFF30D158)),
  tired(Icons.bedtime, Color(0xFFFFD60A));

  // === Properties ===
  final IconData icon;
  final Color color;

  const MoodType(this.icon, this.color);

  // === Localized Name ===
  String localizedName(String locale) {
    switch (this) {
      case MoodType.unmotivated:
        return locale == 'pt'
            ? 'Desmotivado'
            : locale == 'es'
                ? 'Desmotivado'
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
