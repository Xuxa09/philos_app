// === Storage Service ===

import 'package:shared_preferences/shared_preferences.dart';
import '../../core/constants/storage_keys.dart';

class StorageService {
  // === Singleton ===
  static final StorageService instance = StorageService._();
  StorageService._();

  late SharedPreferences _prefs;

  // === Init ===
  Future<void> init() async {
    _prefs = await SharedPreferences.getInstance();
  }

  // === Onboarding ===
  bool get isOnboardingComplete =>
      _prefs.getBool(StorageKeys.onboardingComplete) ?? false;

  Future<void> setOnboardingComplete() =>
      _prefs.setBool(StorageKeys.onboardingComplete, true);

  // === Favorites ===
  List<String> get favoriteIds =>
      _prefs.getStringList(StorageKeys.favoriteIds) ?? [];

  Future<void> saveFavoriteIds(List<String> ids) =>
      _prefs.setStringList(StorageKeys.favoriteIds, ids);

  // === Review ===
  String? get lastReviewRequest =>
      _prefs.getString(StorageKeys.lastReviewRequest);

  Future<void> setLastReviewRequest(String date) =>
      _prefs.setString(StorageKeys.lastReviewRequest, date);

  int get reviewUsageCount =>
      _prefs.getInt(StorageKeys.reviewUsageCount) ?? 0;

  Future<void> incrementUsageCount() =>
      _prefs.setInt(StorageKeys.reviewUsageCount, reviewUsageCount + 1);

  // === Notifications ===
  bool get notificationsEnabled =>
      _prefs.getBool(StorageKeys.notificationsEnabled) ?? false;

  Future<void> setNotificationsEnabled(bool value) =>
      _prefs.setBool(StorageKeys.notificationsEnabled, value);

  // === Locale ===
  String? get selectedLocale => _prefs.getString(StorageKeys.selectedLocale);

  Future<void> setSelectedLocale(String locale) =>
      _prefs.setString(StorageKeys.selectedLocale, locale);
}
