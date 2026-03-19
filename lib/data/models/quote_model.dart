// === Quote Model ===

class QuoteModel {
  // === Properties ===
  final String id;
  final String authorEn;
  final String authorPt;
  final String authorEs;
  final String textEn;
  final String textPt;
  final String textEs;
  final String reflectionEn;
  final String reflectionPt;
  final String reflectionEs;
  final String category;

  // === Constructor ===
  const QuoteModel({
    required this.id,
    required this.authorEn,
    required this.authorPt,
    required this.authorEs,
    required this.textEn,
    required this.textPt,
    required this.textEs,
    required this.reflectionEn,
    required this.reflectionPt,
    required this.reflectionEs,
    required this.category,
  });

  // === Localized Getters ===
  String author(String locale) {
    switch (locale) {
      case 'pt':
        return authorPt;
      case 'es':
        return authorEs;
      default:
        return authorEn;
    }
  }

  String text(String locale) {
    switch (locale) {
      case 'pt':
        return textPt;
      case 'es':
        return textEs;
      default:
        return textEn;
    }
  }

  String reflection(String locale) {
    switch (locale) {
      case 'pt':
        return reflectionPt;
      case 'es':
        return reflectionEs;
      default:
        return reflectionEn;
    }
  }

  String get reference => authorEn;
}
