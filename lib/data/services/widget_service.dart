// === Home Screen Widget Service ===

import 'dart:math';
import 'package:home_widget/home_widget.dart';
import 'mock_data_provider.dart';

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

    await HomeWidget.saveWidgetData('quote_text', quote.text(locale));
    await HomeWidget.saveWidgetData('quote_author', quote.author(locale));
    await HomeWidget.updateWidget(
      androidName: _androidWidgetName,
      iOSName: _iOSWidgetName,
    );
  }
}
