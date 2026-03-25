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

class QuoteCard extends StatefulWidget {
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
  State<QuoteCard> createState() => _QuoteCardState();
}

class _QuoteCardState extends State<QuoteCard> with SingleTickerProviderStateMixin {
  late final AnimationController _favoriteController;
  late final Animation<double> _favoriteScale;

  @override
  void initState() {
    super.initState();
    _favoriteController = AnimationController(
      vsync: this, duration: const Duration(milliseconds: 400),
    );
    _favoriteScale = TweenSequence<double>([
      TweenSequenceItem(tween: Tween(begin: 1.0, end: 1.4), weight: 30),
      TweenSequenceItem(tween: Tween(begin: 1.4, end: 0.85), weight: 30),
      TweenSequenceItem(tween: Tween(begin: 0.85, end: 1.0), weight: 40),
    ]).animate(CurvedAnimation(parent: _favoriteController, curve: Curves.easeOut));
  }

  @override
  void dispose() {
    _favoriteController.dispose();
    super.dispose();
  }

  void _doFavorite() {
    if (widget.onFavoriteTap == null) return;
    HapticService.selection();
    _favoriteController.forward(from: 0);
    widget.onFavoriteTap!();
  }

  void _doCopy() {
    HapticService.light();
    final text = '"${widget.quote.text(widget.locale)}" \u2014 ${widget.quote.author(widget.locale)}';
    Clipboard.setData(ClipboardData(text: text));
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(
          widget.locale == 'pt' ? 'Frase copiada!'
              : widget.locale == 'es' ? '\u00A1Frase copiada!'
              : 'Quote copied!',
        ),
        duration: const Duration(seconds: 2),
        behavior: SnackBarBehavior.floating,
      ),
    );
  }

  void _showOptionsMenu(BuildContext ctx) {
    final locale = widget.locale;
    showModalBottomSheet(
      context: ctx,
      backgroundColor: AppColors.surface,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
      ),
      builder: (_) => SafeArea(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const SizedBox(height: AppSpacing.sm),
            Container(width: 40, height: 4, decoration: BoxDecoration(
              color: AppColors.surfaceSecondary, borderRadius: BorderRadius.circular(2))),
            const SizedBox(height: AppSpacing.md),
            _menuItem(
              icon: widget.isFavorite ? Icons.favorite : Icons.favorite_border,
              color: widget.isFavorite ? AppColors.love : AppColors.textPrimary,
              label: widget.isFavorite
                  ? (locale == 'pt' ? 'Remover dos favoritos' : locale == 'es' ? 'Quitar de favoritos' : 'Remove from favorites')
                  : (locale == 'pt' ? 'Curtir' : locale == 'es' ? 'Me gusta' : 'Like'),
              onTap: () { Navigator.pop(ctx); _doFavorite(); },
            ),
            _menuItem(
              icon: Icons.copy_outlined,
              label: locale == 'pt' ? 'Copiar frase' : locale == 'es' ? 'Copiar frase' : 'Copy quote',
              onTap: () { Navigator.pop(ctx); _doCopy(); },
            ),
            Builder(builder: (shareCtx) => _menuItem(
              icon: Icons.share_outlined,
              label: locale == 'pt' ? 'Compartilhar' : locale == 'es' ? 'Compartir' : 'Share',
              onTap: () {
                Navigator.pop(ctx);
                ShareQuoteSheet.show(shareCtx, widget.quote, locale);
              },
            )),
            const SizedBox(height: AppSpacing.md),
          ],
        ),
      ),
    );
  }

  Widget _menuItem({required IconData icon, required String label, required VoidCallback onTap, Color? color}) {
    return ListTile(
      leading: Icon(icon, color: color ?? AppColors.textPrimary, size: 24),
      title: Text(label, style: AppFonts.body.copyWith(color: AppColors.textPrimary)),
      onTap: onTap,
    );
  }

  @override
  Widget build(BuildContext context) {
    return PressableScale(
      onTap: widget.onTap,
      onLongPress: () {
        HapticService.light();
        _showOptionsMenu(context);
      },
      child: AppCard(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            _buildHeader(),
            const SizedBox(height: AppSpacing.sm),
            _buildQuoteText(),
            if (widget.showReflection) ...[
              const SizedBox(height: AppSpacing.md),
              _buildReflection(),
            ],
          ],
        ),
      ),
    );
  }

  Widget _buildHeader() {
    return Row(
      children: [
        Expanded(
          child: Text(
            widget.quote.author(widget.locale),
            style: AppFonts.callout.copyWith(
              color: AppColors.primary,
              fontWeight: FontWeight.w600,
              letterSpacing: 0.3,
            ),
          ),
        ),
        if (widget.isFavorite)
          GestureDetector(
            behavior: HitTestBehavior.opaque,
            onTap: _doFavorite,
            child: AnimatedBuilder(
              animation: _favoriteScale,
              builder: (context, child) => Transform.scale(scale: _favoriteScale.value, child: child),
              child: const SizedBox(
                width: 44, height: 44,
                child: Center(child: Icon(Icons.favorite, color: AppColors.love, size: 32)),
              ),
            ),
          ),
        Builder(builder: (ctx) => GestureDetector(
          behavior: HitTestBehavior.opaque,
          onTap: () {
            HapticService.light();
            _showOptionsMenu(ctx);
          },
          child: const SizedBox(
            width: 44, height: 44,
            child: Center(
              child: Icon(Icons.more_vert, color: AppColors.textTertiary, size: 44),
            ),
          ),
        )),
      ],
    );
  }

  Widget _buildQuoteText() {
    return Text(
      '\u201C${widget.quote.text(widget.locale)}\u201D',
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
                widget.locale == 'pt'
                    ? 'Reflex\u00E3o'
                    : widget.locale == 'es'
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
            widget.quote.reflection(widget.locale),
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
