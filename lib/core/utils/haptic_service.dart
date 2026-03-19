// === Haptic Service ===

import 'package:flutter/services.dart';

abstract class HapticService {
  // === Feedback Types ===
  static void success() => HapticFeedback.mediumImpact();
  static void error() => HapticFeedback.heavyImpact();
  static void selection() => HapticFeedback.selectionClick();
  static void light() => HapticFeedback.lightImpact();
}
