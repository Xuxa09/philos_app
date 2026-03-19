// === String Extensions ===

extension StringExtensions on String {
  // === Capitalization ===
  String get capitalized {
    if (isEmpty) return this;
    return '${this[0].toUpperCase()}${substring(1)}';
  }
}
