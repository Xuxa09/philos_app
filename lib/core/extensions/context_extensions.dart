// === Context Extensions ===

import 'package:flutter/material.dart';
import '../l10n/app_localizations.dart';

extension ContextExtensions on BuildContext {
  // === Localization ===
  AppLocalizations get l10n => AppLocalizations.of(this)!;

  // === Theme ===
  ThemeData get theme => Theme.of(this);

  // === Media Query ===
  MediaQueryData get media => MediaQuery.of(this);
  double get screenWidth => media.size.width;
  double get screenHeight => media.size.height;
  bool get isTablet => screenWidth > 600;
}
