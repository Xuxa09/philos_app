// === Random Quote Bottom Sheet ===

import 'dart:math';
import 'package:flutter/material.dart';
import 'share_quote_sheet.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';
import '../../../core/utils/haptic_service.dart';
import '../../../data/models/quote_model.dart';
import '../../../data/services/mock_data_provider.dart';
import '../../../data/repositories/quote_repository.dart';
import 'app_button.dart';

class RandomQuoteSheet extends StatefulWidget {
  const RandomQuoteSheet({super.key});

  @override
  State<RandomQuoteSheet> createState() => _RandomQuoteSheetState();
}

class _RandomQuoteSheetState extends State<RandomQuoteSheet> {
  // === Properties ===
  final _repository = QuoteRepository();
  late QuoteModel _quote;

  // === Lifecycle ===
  @override
  void initState() {
    super.initState();
    _pickRandom();
  }

  // === Actions ===
  void _pickRandom() {
    final all = MockDataProvider.quotes;
    _quote = all[Random().nextInt(all.length)];
    HapticService.light();
    if (mounted) setState(() {});
  }

  // === Build ===
  @override
  Widget build(BuildContext context) {
    final locale = Localizations.localeOf(context).languageCode;

    return SafeArea(
      child: Padding(
        padding: const EdgeInsets.all(AppSpacing.screenPadding),
        child: Column(
          children: [
            Container(
              width: 40, height: 4,
              decoration: BoxDecoration(
                color: AppColors.surfaceSecondary,
                borderRadius: BorderRadius.circular(2),
              ),
            ),
            const SizedBox(height: AppSpacing.xl),
            Flexible(
              child: SingleChildScrollView(
                child: Column(
                  children: [
                    _buildIcon(),
                    const SizedBox(height: AppSpacing.lg),
                    _buildAuthor(locale),
                    const SizedBox(height: AppSpacing.md),
                    _buildQuoteText(locale),
                    const SizedBox(height: AppSpacing.lg),
                    _buildReflection(locale),
                    const SizedBox(height: AppSpacing.lg),
                    _buildActions(locale),
                    const SizedBox(height: AppSpacing.lg),
                    AppButton(
                      title: _anotherQuoteLabel(locale),
                      isOutlined: true,
                      icon: Icons.refresh,
                      onTap: _pickRandom,
                    ),
                    const SizedBox(height: AppSpacing.md),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  // === Subviews ===
  Widget _buildIcon() {
    return Container(
      width: 60, height: 60,
      decoration: BoxDecoration(
        color: AppColors.primary.withValues(alpha: 0.15),
        shape: BoxShape.circle,
      ),
      child: const Icon(Icons.auto_awesome, size: 28, color: AppColors.primary),
    );
  }

  Widget _buildAuthor(String locale) {
    return Text(
      _quote.author(locale),
      style: AppFonts.caption.copyWith(
        color: AppColors.primary,
        fontWeight: FontWeight.w600,
        letterSpacing: 1,
      ),
    );
  }

  Widget _buildQuoteText(String locale) {
    return Text(
      '\u201C${_quote.text(locale)}\u201D',
      style: AppFonts.title2.copyWith(
        color: AppColors.textPrimary,
        fontStyle: FontStyle.italic,
        height: 1.5,
      ),
      textAlign: TextAlign.center,
    );
  }

  Widget _buildReflection(String locale) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(AppSpacing.md),
      decoration: BoxDecoration(
        color: AppColors.surfaceSecondary,
        borderRadius: BorderRadius.circular(12),
      ),
      child: Text(
        _quote.reflection(locale),
        style: AppFonts.subheadline.copyWith(
          color: AppColors.textSecondary,
          height: 1.4,
        ),
        textAlign: TextAlign.center,
      ),
    );
  }

  Widget _buildActions(String locale) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        _buildActionButton(
          icon: _repository.isFavorite(_quote.id)
              ? Icons.favorite
              : Icons.favorite_border,
          color: _repository.isFavorite(_quote.id)
              ? AppColors.love
              : AppColors.textSecondary,
          onTap: () async {
            await _repository.toggleFavorite(_quote.id);
            HapticService.selection();
            setState(() {});
          },
        ),
        const SizedBox(width: AppSpacing.lg),
        Builder(builder: (ctx) => _buildActionButton(
          icon: Icons.share_outlined,
          color: AppColors.textSecondary,
          onTap: () {
            HapticService.light();
            ShareQuoteSheet.show(ctx, _quote, locale);
          },
        )),
      ],
    );
  }

  Widget _buildActionButton({
    required IconData icon,
    required Color color,
    required VoidCallback onTap,
  }) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        width: 44, height: 44,
        decoration: const BoxDecoration(
          color: AppColors.surfaceSecondary,
          shape: BoxShape.circle,
        ),
        child: Icon(icon, color: color, size: 28),
      ),
    );
  }

  String _anotherQuoteLabel(String locale) {
    switch (locale) {
      case 'pt': return 'Outra Frase';
      case 'es': return 'Otra Frase';
      default: return 'Another Quote';
    }
  }
}
