// === App Fonts ===

import 'package:flutter/material.dart';

abstract class AppFonts {
  // === Large Title ===
  static const TextStyle largeTitle = TextStyle(
    fontSize: 34,
    fontWeight: FontWeight.bold,
    letterSpacing: -0.5,
  );

  // === Titles ===
  static const TextStyle title = TextStyle(
    fontSize: 24,
    fontWeight: FontWeight.bold,
  );

  static const TextStyle title2 = TextStyle(
    fontSize: 20,
    fontWeight: FontWeight.w600,
  );

  // === Headline ===
  static const TextStyle headline = TextStyle(
    fontSize: 17,
    fontWeight: FontWeight.w600,
  );

  // === Body ===
  static const TextStyle body = TextStyle(
    fontSize: 17,
    fontWeight: FontWeight.normal,
  );

  // === Callout ===
  static const TextStyle callout = TextStyle(
    fontSize: 16,
    fontWeight: FontWeight.normal,
  );

  // === Subheadline ===
  static const TextStyle subheadline = TextStyle(
    fontSize: 15,
    fontWeight: FontWeight.normal,
  );

  // === Footnote ===
  static const TextStyle footnote = TextStyle(
    fontSize: 13,
    fontWeight: FontWeight.normal,
  );

  // === Caption ===
  static const TextStyle caption = TextStyle(
    fontSize: 12,
    fontWeight: FontWeight.normal,
  );
}
