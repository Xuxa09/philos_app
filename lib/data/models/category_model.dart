// === Category Model ===

import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';

enum QuoteCategory {
  stoicism(Icons.shield_outlined, AppColors.categoryStoicism),
  classical(Icons.account_balance, AppColors.categoryClassical),
  existentialism(Icons.psychology_alt, AppColors.categoryExistentialism),
  eastern(Icons.self_improvement, AppColors.categoryEastern),
  epicureanism(Icons.spa, AppColors.categoryEpicureanism),
  rationalism(Icons.lightbulb_outline, AppColors.categoryRationalism),
  absurdism(Icons.blur_on, AppColors.categoryAbsurdism),
  pragmatism(Icons.handyman, AppColors.categoryPragmatism);

  // === Properties ===
  final IconData icon;
  final Color color;
  const QuoteCategory(this.icon, this.color);

  // === Localized Name ===
  String localizedName(String locale) {
    switch (this) {
      case stoicism:
        return locale == 'pt'
            ? 'Estoicismo'
            : locale == 'es'
                ? 'Estoicismo'
                : 'Stoicism';
      case classical:
        return locale == 'pt'
            ? 'Filosofia Cl\u00E1ssica'
            : locale == 'es'
                ? 'Filosof\u00EDa Cl\u00E1sica'
                : 'Classical Philosophy';
      case existentialism:
        return locale == 'pt'
            ? 'Existencialismo'
            : locale == 'es'
                ? 'Existencialismo'
                : 'Existentialism';
      case eastern:
        return locale == 'pt'
            ? 'Filosofia Oriental'
            : locale == 'es'
                ? 'Filosof\u00EDa Oriental'
                : 'Eastern Philosophy';
      case epicureanism:
        return locale == 'pt'
            ? 'Epicurismo'
            : locale == 'es'
                ? 'Epicure\u00EDsmo'
                : 'Epicureanism';
      case rationalism:
        return locale == 'pt'
            ? 'Racionalismo'
            : locale == 'es'
                ? 'Racionalismo'
                : 'Rationalism';
      case absurdism:
        return locale == 'pt'
            ? 'Absurdismo'
            : locale == 'es'
                ? 'Absurdismo'
                : 'Absurdism';
      case pragmatism:
        return locale == 'pt'
            ? 'Pragmatismo'
            : locale == 'es'
                ? 'Pragmatismo'
                : 'Pragmatism';
    }
  }
}
