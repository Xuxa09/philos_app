// === Review Service ===

import 'package:in_app_review/in_app_review.dart';
import '../../core/constants/app_constants.dart';
import 'storage_service.dart';

class ReviewService {
  // === Singleton ===
  static final ReviewService instance = ReviewService._();
  ReviewService._();

  final _review = InAppReview.instance;
  final _storage = StorageService.instance;

  // === Public Methods ===
  Future<void> requestReviewIfAppropriate() async {
    final usageCount = _storage.reviewUsageCount;
    if (usageCount < AppConstants.reviewMinUsageCount) return;

    final lastRequest = _storage.lastReviewRequest;
    if (lastRequest != null) {
      final lastDate = DateTime.tryParse(lastRequest);
      if (lastDate != null) {
        final daysSince = DateTime.now().difference(lastDate).inDays;
        if (daysSince < AppConstants.reviewCooldownDays) return;
      }
    }

    if (await _review.isAvailable()) {
      await _review.requestReview();
      await _storage.setLastReviewRequest(DateTime.now().toIso8601String());
    }
  }
}
