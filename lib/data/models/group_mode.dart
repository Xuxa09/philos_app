// === Group Mode Model ===

import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';

enum GroupMode {
  school(Icons.school, AppColors.primary),
  philosopher(Icons.person, AppColors.accent),
  mood(Icons.emoji_emotions, AppColors.warning);

  final IconData icon;
  final Color color;
  const GroupMode(this.icon, this.color);

  String localizedName(String locale) {
    switch (this) {
      case school:
        return locale == 'pt'
            ? 'Escola'
            : locale == 'es'
                ? 'Escuela'
                : 'School';
      case philosopher:
        return locale == 'pt'
            ? 'Filósofo'
            : locale == 'es'
                ? 'Filósofo'
                : 'Philosopher';
      case mood:
        return locale == 'pt'
            ? 'Sentimento'
            : locale == 'es'
                ? 'Sentimiento'
                : 'Mood';
    }
  }
}
