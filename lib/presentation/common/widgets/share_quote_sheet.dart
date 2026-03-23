import 'package:flutter/material.dart';
import 'package:share_plus/share_plus.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';
import '../../../core/utils/haptic_service.dart';
import '../../../data/models/quote_model.dart';
import '../../share_image/share_image_screen.dart';
import 'pressable_scale.dart';

class ShareQuoteSheet extends StatelessWidget {
  final QuoteModel quote;
  final String locale;

  const ShareQuoteSheet({super.key, required this.quote, required this.locale});

  static void show(BuildContext context, QuoteModel quote, String locale) {
    showModalBottomSheet(
      context: context,
      useRootNavigator: true,
      backgroundColor: AppColors.surface,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
      ),
      builder: (_) => ShareQuoteSheet(quote: quote, locale: locale),
    );
  }

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Padding(
        padding: const EdgeInsets.all(AppSpacing.screenPadding),
        child: Column(mainAxisSize: MainAxisSize.min, children: [
          Container(width: 40, height: 4,
            decoration: BoxDecoration(color: AppColors.surfaceSecondary, borderRadius: BorderRadius.circular(2))),
          const SizedBox(height: AppSpacing.lg),
          Text(
            locale == 'pt' ? 'Compartilhar como' : locale == 'es' ? 'Compartir como' : 'Share as',
            style: AppFonts.title2.copyWith(color: AppColors.textPrimary),
          ),
          const SizedBox(height: AppSpacing.lg),
          Row(children: [
            Expanded(child: _buildOption(
              context,
              icon: Icons.text_fields,
              label: locale == 'pt' ? 'Texto' : locale == 'es' ? 'Texto' : 'Text',
              onTap: () {
                Navigator.pop(context);
                HapticService.light();
                Share.share('\u201C${quote.text(locale)}\u201D \u2014 ${quote.author(locale)}');
              },
            )),
            const SizedBox(width: AppSpacing.md),
            Expanded(child: _buildOption(
              context,
              icon: Icons.image_outlined,
              label: locale == 'pt' ? 'Imagem' : locale == 'es' ? 'Imagen' : 'Image',
              onTap: () {
                Navigator.pop(context);
                HapticService.light();
                Navigator.push(context, MaterialPageRoute(
                  builder: (_) => ShareImageScreen(quote: quote, locale: locale),
                ));
              },
            )),
          ]),
          const SizedBox(height: AppSpacing.lg),
        ]),
      ),
    );
  }

  Widget _buildOption(BuildContext context, {required IconData icon, required String label, required VoidCallback onTap}) {
    return PressableScale(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: AppSpacing.lg),
        decoration: BoxDecoration(
          color: AppColors.surfaceSecondary,
          borderRadius: BorderRadius.circular(16),
        ),
        child: Column(children: [
          Icon(icon, color: AppColors.primary, size: 32),
          const SizedBox(height: AppSpacing.sm),
          Text(label, style: AppFonts.subheadline.copyWith(color: AppColors.textPrimary, fontWeight: FontWeight.w500)),
        ]),
      ),
    );
  }
}
