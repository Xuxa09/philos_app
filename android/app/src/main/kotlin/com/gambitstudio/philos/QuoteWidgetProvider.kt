package com.gambitstudio.philos

import android.appwidget.AppWidgetManager
import android.content.Context
import android.content.SharedPreferences
import android.widget.RemoteViews
import es.antonborri.home_widget.HomeWidgetProvider

class QuoteWidgetProvider : HomeWidgetProvider() {
    override fun onUpdate(
        context: Context,
        appWidgetManager: AppWidgetManager,
        appWidgetIds: IntArray,
        widgetData: SharedPreferences
    ) {
        appWidgetIds.forEach { widgetId ->
            val views = RemoteViews(context.packageName, R.layout.quote_widget).apply {
                val quoteText = widgetData.getString("quote_text", "Toque para atualizar")
                val quoteAuthor = widgetData.getString("quote_author", "")

                setTextViewText(R.id.quote_text, "\u201C$quoteText\u201D")
                setTextViewText(R.id.quote_author, if (quoteAuthor.isNullOrEmpty()) "" else "\u2014 $quoteAuthor")
            }

            appWidgetManager.updateAppWidget(widgetId, views)
        }
    }
}
