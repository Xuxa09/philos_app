// === Feature Flags ===

abstract class FeatureFlags {
  // === Monetization ===
  static const premiumEnabled = false;

  // === Mock Data ===
  static const isMockedData = false;

  // === Computed Flags ===
  static bool hasPremiumAccess() {
    if (!premiumEnabled) return true;
    return false;
  }
}
