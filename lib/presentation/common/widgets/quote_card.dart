import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'share_quote_sheet.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';
import '../../../core/utils/haptic_service.dart';
import '../../../data/models/quote_model.dart';
import 'app_card.dart';
import 'pressable_scale.dart';

class QuoteCard extends StatelessWidget {
  final QuoteModel quote;
  final String locale;
  final bool isFavorite;
  final VoidCallback? onFavoriteTap;
  final VoidCallback? onTap;
  final bool showReflection;

  const QuoteCard({
    super.key,
    required this.quote,
    required this.locale,
    this.isFavorite = false,
    this.onFavoriteTap,
    this.onTap,
    this.showReflection = false,
  });

  @override
  Widget build(BuildContext context) {
    return PressableScale(
      onTap: onTap,
      onLongPress: () {
        HapticService.light();
        final text = '"${quote.text(locale)}" \u2014 ${quote.author(locale)}';
        Clipboard.setData(ClipboardData(text: text));
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(
              locale == 'pt'
                  ? 'Frase copiada!'
                  : locale == 'es'
                      ? '\u00A1Frase copiada!'
                      : 'Quote copied!',
            ),
            duration: const Duration(seconds: 2),
            behavior: SnackBarBehavior.floating,
          ),
        );
      },
      child: AppCard(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            _buildHeader(),
            const SizedBox(height: AppSpacing.sm),
            _buildQuoteText(),
            if (showReflection) ...[
              const SizedBox(height: AppSpacing.md),
              _buildReflection(),
            ],
          ],
        ),
      ),
    );
  }

  // === Subviews ===
  Widget _buildHeader() {
    return Row(
      children: [
        Expanded(
          child: Text(
            quote.author(locale),
            style: AppFonts.callout.copyWith(
              color: AppColors.primary,
              fontWeight: FontWeight.w600,
              letterSpacing: 0.3,
            ),
          ),
        ),
        if (onFavoriteTap != null)
          GestureDetector(
            behavior: HitTestBehavior.opaque,
            onTap: () {
              HapticService.selection();
              onFavoriteTap!();
            },
            child: SizedBox(
              width: 44, height: 44,
              child: Center(
                child: Icon(
                  isFavorite ? Icons.favorite : Icons.favorite_border,
                  color: isFavorite ? AppColors.love : AppColors.textTertiary,
                  size: 22,
                ),
              ),
            ),
          ),
        Builder(builder: (ctx) => GestureDetector(
          behavior: HitTestBehavior.opaque,
          onTap: () {
            HapticService.light();
            ShareQuoteSheet.show(ctx, quote, locale);
          },
          child: const SizedBox(
            width: 44, height: 44,
            child: Center(
              child: Icon(
                Icons.share_outlined,
                color: AppColors.textTertiary,
                size: 20,
              ),
            ),
          ),
        )),
      ],
    );
  }

  Widget _buildQuoteText() {
    return Text(
      '\u201C${quote.text(locale)}\u201D',
      style: AppFonts.body.copyWith(
        color: AppColors.textPrimary,
        fontStyle: FontStyle.italic,
        height: 1.5,
      ),
    );
  }

  Widget _buildReflection() {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(AppSpacing.sm + 4),
      decoration: BoxDecoration(
        color: AppColors.surfaceSecondary,
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              const Icon(Icons.lightbulb_outline, size: 18, color: AppColors.accent),
              const SizedBox(width: AppSpacing.xs),
              Text(
                locale == 'pt'
                    ? 'Reflex\u00E3o'
                    : locale == 'es'
                        ? 'Reflexi\u00F3n'
                        : 'Reflection',
                style: AppFonts.subheadline.copyWith(
                  color: AppColors.accent,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ],
          ),
          const SizedBox(height: AppSpacing.xs),
          Text(
            quote.reflection(locale),
            style: AppFonts.body.copyWith(
              color: AppColors.textSecondary,
              height: 1.5,
            ),
          ),
        ],
      ),
    );
  }
}
