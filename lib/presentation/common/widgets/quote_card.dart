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

class _QuoteCardState extends State<QuoteCard> with TickerProviderStateMixin {
  late final AnimationController _favoriteController;
  late final Animation<double> _favoriteScale;
  late final AnimationController _shareController;
  late final Animation<double> _shareRotation;

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

    _shareController = AnimationController(
      vsync: this, duration: const Duration(milliseconds: 350),
    );
    _shareRotation = TweenSequence<double>([
      TweenSequenceItem(tween: Tween(begin: 0.0, end: -0.15), weight: 30),
      TweenSequenceItem(tween: Tween(begin: -0.15, end: 0.1), weight: 30),
      TweenSequenceItem(tween: Tween(begin: 0.1, end: 0.0), weight: 40),
    ]).animate(CurvedAnimation(parent: _shareController, curve: Curves.easeOut));
  }

  @override
  void dispose() {
    _favoriteController.dispose();
    _shareController.dispose();
    super.dispose();
  }

  void _onFavoriteTap() {
    HapticService.selection();
    _favoriteController.forward(from: 0);
    widget.onFavoriteTap?.call();
  }

  void _onShareTap(BuildContext ctx) {
    HapticService.light();
    _shareController.forward(from: 0);
    ShareQuoteSheet.show(ctx, widget.quote, widget.locale);
  }

  @override
  Widget build(BuildContext context) {
    return PressableScale(
      onTap: widget.onTap,
      onDoubleTap: widget.onFavoriteTap != null ? _onFavoriteTap : null,
      onLongPress: () {
        HapticService.light();
        final text = '"${widget.quote.text(widget.locale)}" \u2014 ${widget.quote.author(widget.locale)}';
        Clipboard.setData(ClipboardData(text: text));
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(
              widget.locale == 'pt'
                  ? 'Frase copiada!'
                  : widget.locale == 'es'
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
        if (widget.onFavoriteTap != null)
          GestureDetector(
            behavior: HitTestBehavior.opaque,
            onTap: _onFavoriteTap,
            child: SizedBox(
              width: 44, height: 44,
              child: Center(
                child: AnimatedBuilder(
                  animation: _favoriteScale,
                  builder: (context, child) => Transform.scale(
                    scale: _favoriteScale.value,
                    child: child,
                  ),
                  child: AnimatedSwitcher(
                    duration: const Duration(milliseconds: 200),
                    transitionBuilder: (child, anim) => FadeTransition(opacity: anim, child: child),
                    child: Icon(
                      widget.isFavorite ? Icons.favorite : Icons.favorite_border,
                      key: ValueKey(widget.isFavorite),
                      color: widget.isFavorite ? AppColors.love : AppColors.textTertiary,
                      size: 28,
                    ),
                  ),
                ),
              ),
            ),
          ),
        Builder(builder: (ctx) => GestureDetector(
          behavior: HitTestBehavior.opaque,
          onTap: () => _onShareTap(ctx),
          child: SizedBox(
            width: 44, height: 44,
            child: Center(
              child: AnimatedBuilder(
                animation: _shareRotation,
                builder: (context, child) => Transform.rotate(
                  angle: _shareRotation.value,
                  child: child,
                ),
                child: const Icon(
                  Icons.share_outlined,
                  color: AppColors.textTertiary,
                  size: 28,
                ),
              ),
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