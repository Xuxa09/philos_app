import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import 'app.dart';
import 'data/services/notification_service.dart';
import 'data/services/storage_service.dart';
import 'data/services/widget_service.dart';
import 'providers/app_providers.dart';

// === Entry Point ===

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  SystemChrome.setSystemUIOverlayStyle(
    const SystemUiOverlayStyle(
      statusBarBrightness: Brightness.light,
      statusBarIconBrightness: Brightness.dark,
      statusBarColor: Colors.transparent,
    ),
  );

  await StorageService.instance.init();

  try { await NotificationService.instance.init(); } catch (_) {}

  try {
    await WidgetService.initialize();
    await WidgetService.updateRandomQuote();
  } catch (_) {}

  runApp(
    MultiProvider(
      providers: appProviders,
      child: const App(),
    ),
  );
}
