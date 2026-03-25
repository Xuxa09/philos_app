// === App Colors ===

import 'package:flutter/material.dart';

abstract class AppColors {
  // === Light Theme (Parchment / Ancient Manuscript) ===
  static const background = Color(0xFFF5EFE0); // warm parchment
  static const surface = Color(0xFFFFF8ED);     // ivory manuscript
  static const surfaceSecondary = Color(0xFFD4C4A8); // sand border

  // === Primary (Sepia Ink) ===
  static const primary = Color(0xFF6B4226);     // sepia ink
  static const secondary = Color(0xFF523218);   // dark sepia
  static const accent = Color(0xFF8B6B42);       // aged bronze

  // === Semantic ===
  static const error = Color(0xFF8B3030);
  static const success = Color(0xFF3E6B4A);
  static const warning = Color(0xFF8B7020);

  // === Text ===
  static const textPrimary = Color(0xFF3A2A1A);  // ink brown
  static const textSecondary = Color(0xFF6B5840); // faded ink
  static const textTertiary = Color(0xFF9A8A6E);  // aged text

  // === Categories (Philosophical Schools) ===
  static const categoryStoicism = Color(0xFF4A6848);     // olive leaf
  static const categoryClassical = Color(0xFF8B6B28);    // old gold
  static const categoryExistentialism = Color(0xFF6B4888); // aged violet
  static const categoryEastern = Color(0xFF3E6278);       // ink blue
  static const categoryEpicureanism = Color(0xFF4A7070);  // verdigris
  static const categoryRationalism = Color(0xFF884848);   // faded crimson
  static const categoryAbsurdism = Color(0xFF7A6B28);     // mustard
  static const categoryPragmatism = Color(0xFF4A6B50);    // herb green

  // === Favorite ===
  static const love = Color(0xFF884040);
}