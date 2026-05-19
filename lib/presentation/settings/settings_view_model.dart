import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import 'package:package_info_plus/package_info_plus.dart';
import '../../data/services/notification_service.dart';
import '../../data/services/storage_service.dart';

class SettingsViewModel extends ChangeNotifier {
  final StorageService _storage = StorageService.instance;
  final NotificationService _notifications = NotificationService.instance;
  static const _supportedCodes = {'en', 'pt', 'es'};
  String _appVersion = '';
  late Locale _locale;
  late bool _notificationsEnabled;

  SettingsViewModel() {
    final saved = _storage.selectedLocale;
    _locale = saved != null ? Locale(saved) : _systemLocale();
    _notificationsEnabled = _storage.notificationsEnabled;
  }

  Locale _systemLocale() {
    final systemCode = ui.PlatformDispatcher.instance.locale.languageCode;
    return Locale(_supportedCodes.contains(systemCode) ? systemCode : 'en');
  }

  String get appVersion => _appVersion;
  Locale get locale => _locale;
  String get selectedLocale => _locale.languageCode;
  bool get notificationsEnabled => _notificationsEnabled;

  Future<void> loadSettings() async {
    final info = await PackageInfo.fromPlatform();
    _appVersion = '${info.version} (${info.buildNumber})';
    final saved = _storage.selectedLocale;
    if (saved != null) _locale = Locale(saved);
    _notificationsEnabled = _storage.notificationsEnabled;
    notifyListeners();
  }

  Future<void> setLocale(String code) async {
    _locale = Locale(code);
    await _storage.setSelectedLocale(code);
    notifyListeners();
  }

  Future<void> toggleNotifications(bool value) async {
    _notificationsEnabled = value; notifyListeners();
    try {
      await _storage.setNotificationsEnabled(value);
      if (value) {
        final granted = await _notifications.requestPermission();
        if (granted) { await _notifications.scheduleDailyReminder(); }
        else { _notificationsEnabled = false; await _storage.setNotificationsEnabled(false); notifyListeners(); }
      } else { await _notifications.cancelAll(); }
    } catch (_) { _notificationsEnabled = false; await _storage.setNotificationsEnabled(false); notifyListeners(); }
  }
}
