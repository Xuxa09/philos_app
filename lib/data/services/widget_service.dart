// === Home Screen Widget Service ===

import 'dart:math';
import 'package:home_widget/home_widget.dart';
import 'mock_data_provider.dart';
import 'storage_service.dart';

abstract class WidgetService {
  static const _appGroupId = 'group.com.gambitstudio.philos';
  static const _androidWidgetName = 'QuoteWidgetProvider';
  static const _iOSWidgetName = 'PhilosWidget';

  static Future<void> initialize() async {
    await HomeWidget.setAppGroupId(_appGroupId);
  }

  static Future<void> updateRandomQuote({String locale = 'pt'}) async {
    final quotes = MockDataProvider.quotes;
    final quote = quotes[Random().nextInt(quotes.length)];
    final storage = StorageService.instance;

    await HomeWidget.saveWidgetData('quote_text', quote.text(locale));
    await HomeWidget.saveWidgetData('quote_author', quote.author(locale));
    await HomeWidget.saveWidgetData('widget_background', storage.widgetBackground);
    await HomeWidget.saveWidgetData('widget_font_style', storage.widgetFontStyle);
    await HomeWidget.updateWidget(
      androidName: _androidWidgetName,
      iOSName: _iOSWidgetName,
    );
  }

  static Future<void> updateStyle() async {
    final storage = StorageService.instance;
    await HomeWidget.saveWidgetData('widget_background', storage.widgetBackground);
    await HomeWidget.saveWidgetData('widget_font_style', storage.widgetFontStyle);
    await HomeWidget.updateWidget(
      androidName: _androidWidgetName,
      iOSName: _iOSWidgetName,
    );
  }
}
