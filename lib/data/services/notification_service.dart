// === Notification Service ===

import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:timezone/timezone.dart' as tz;
import 'package:timezone/data/latest_all.dart' as tz;
import 'storage_service.dart';

class NotificationService {
  // === Singleton ===
  static final NotificationService instance = NotificationService._();
  NotificationService._();

  final _plugin = FlutterLocalNotificationsPlugin();

  // === Notification Details ===
  static const _channelId = 'daily_reminder';
  static const _channelName = 'Daily Reminder';
  static const _notificationId = 0;

  // === Init ===
  Future<void> init() async {
    try {
      tz.initializeTimeZones();

      const androidSettings =
          AndroidInitializationSettings('@mipmap/ic_launcher');
      const iosSettings = DarwinInitializationSettings(
        requestAlertPermission: false,
        requestBadgePermission: false,
        requestSoundPermission: false,
      );

      await _plugin.initialize(
        const InitializationSettings(
          android: androidSettings,
          iOS: iosSettings,
        ),
      );

      final enabled = StorageService.instance.notificationsEnabled;
      if (enabled) {
        await scheduleDailyReminder();
      }
    } catch (_) {}
  }

  // === Request Permission ===
  Future<bool> requestPermission() async {
    try {
      final android = _plugin.resolvePlatformSpecificImplementation<
          AndroidFlutterLocalNotificationsPlugin>();
      if (android != null) {
        final granted = await android.requestNotificationsPermission();
        return granted ?? false;
      }

      final ios = _plugin.resolvePlatformSpecificImplementation<
          IOSFlutterLocalNotificationsPlugin>();
      if (ios != null) {
        final granted = await ios.requestPermissions(
          alert: true,
          badge: true,
          sound: true,
        );
        return granted ?? false;
      }

      return true;
    } catch (_) {
      return false;
    }
  }

  // === Schedule Daily Reminder ===
  Future<void> scheduleDailyReminder({int hour = 8, int minute = 0}) async {
    try {
      await _plugin.cancelAll();

      final now = tz.TZDateTime.now(tz.local);
      var scheduledDate = tz.TZDateTime(
        tz.local, now.year, now.month, now.day, hour, minute,
      );

      if (scheduledDate.isBefore(now)) {
        scheduledDate = scheduledDate.add(const Duration(days: 1));
      }

      const androidDetails = AndroidNotificationDetails(
        _channelId, _channelName,
        channelDescription: 'Daily inspirational quote reminder',
        importance: Importance.high,
        priority: Priority.defaultPriority,
        icon: '@mipmap/ic_launcher',
      );

      const iosDetails = DarwinNotificationDetails(
        presentAlert: true,
        presentBadge: true,
        presentSound: true,
      );

      await _plugin.zonedSchedule(
        _notificationId,
        'Coach Phrase',
        _getRandomMessage(),
        scheduledDate,
        const NotificationDetails(
          android: androidDetails,
          iOS: iosDetails,
        ),
        androidScheduleMode: AndroidScheduleMode.inexactAllowWhileIdle,
        matchDateTimeComponents: DateTimeComponents.time,
        uiLocalNotificationDateInterpretation:
            UILocalNotificationDateInterpretation.absoluteTime,
      );
    } catch (_) {}
  }

  // === Cancel ===
  Future<void> cancelAll() async {
    await _plugin.cancelAll();
  }

  // === Private Methods ===
  String _getRandomMessage() {
    final messages = [
      'Your daily dose of inspiration is ready!',
      'A powerful quote is waiting for you.',
      'Start your day with an inspiring thought!',
      'New motivational content just for you.',
      'Feed your mind with greatness today.',
    ];
    return messages[DateTime.now().microsecond % messages.length];
  }
}
