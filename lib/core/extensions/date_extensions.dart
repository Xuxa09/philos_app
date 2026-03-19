// === Date Extensions ===

extension DateExtensions on DateTime {
  // === Day Checks ===
  bool get isToday {
    final now = DateTime.now();
    return year == now.year && month == now.month && day == now.day;
  }

  bool get isYesterday {
    final yesterday = DateTime.now().subtract(const Duration(days: 1));
    return year == yesterday.year &&
        month == yesterday.month &&
        day == yesterday.day;
  }

  // === Formatting ===
  String get dateKey => '$year-$month-$day';
}
