package com.gambitstudio.philos

import android.app.PendingIntent
import android.appwidget.AppWidgetManager
import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.graphics.Color
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
                val quoteText = widgetData.getString("quote_text", "Toque para abrir o Philos")
                val quoteAuthor = widgetData.getString("quote_author", "")
                val fontStyle = widgetData.getString("widget_font_style", "serif")
                val background = widgetData.getString("widget_background", "gradient")

                setTextViewText(R.id.quote_text, "\u201C$quoteText\u201D")
                setTextViewText(R.id.quote_author, if (quoteAuthor.isNullOrEmpty()) "" else "— $quoteAuthor")

                // Apply font size based on style
                val fontSize = when (fontStyle) {
                    "sans" -> 14f
                    "mono" -> 13f
                    else -> 15f // serif
                }
                setFloat(R.id.quote_text, "setTextSize", fontSize)

                // Apply background color tint on author based on theme
                val authorColor = when (background) {
                    "gold" -> Color.parseColor("#D4A843")
                    "purple" -> Color.parseColor("#BF5AF2")
                    "green" -> Color.parseColor("#30D158")
                    else -> Color.parseColor("#0A84FF")
                }
                setTextColor(R.id.quote_author, authorColor)

                // Open app on tap
                val intent = Intent(context, MainActivity::class.java).apply {
                    flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP
                }
                val pendingIntent = PendingIntent.getActivity(
                    context, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
                )
                setOnClickPendingIntent(R.id.widget_container, pendingIntent)
            }

            appWidgetManager.updateAppWidget(widgetId, views)
        }
    }
}
