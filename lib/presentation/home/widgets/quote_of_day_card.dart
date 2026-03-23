import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:share_plus/share_plus.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';
import '../../../core/utils/haptic_service.dart';
import '../../../data/models/quote_model.dart';
import '../../common/widgets/pressable_scale.dart';

class QuoteOfDayCard extends StatefulWidget {
  final QuoteModel quote;
  final String locale;
  final bool isFavorite;
  final VoidCallback? onFavoriteTap;

  const QuoteOfDayCard({
    super.key,
    required this.quote,
    required this.locale,
    this.isFavorite = false,
    this.onFavoriteTap,
  });

  @override
  State<QuoteOfDayCard> createState() => _QuoteOfDayCardState();
}

class _QuoteOfDayCardState extends State<QuoteOfDayCard> {
  bool _expanded = false;
  bool _overflows = false;

  @override
  void didUpdateWidget(covariant QuoteOfDayCard oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.quote.id != widget.quote.id) {
      _expanded = false;
      _overflows = false;
    }
  }

  @override
  Widget build(BuildContext context) {
    return PressableScale(
      onTap: _overflows ? () => setState(() => _expanded = !_expanded) : null,
      onLongPress: () {
        HapticService.light();
        final text = '"${widget.quote.text(widget.locale)}" — ${widget.quote.author(widget.locale)}';
        Clipboard.setData(ClipboardData(text: text));
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(
              widget.locale == 'pt'
                  ? 'Frase copiada!'
                  : widget.locale == 'es'
                      ? '¡Frase copiada!'
                      : 'Quote copied!',
            ),
            duration: const Duration(seconds: 2),
            behavior: SnackBarBehavior.floating,
          ),
        );
      },
      child: AnimatedSize(
        duration: const Duration(milliseconds: 300),
        curve: Curves.easeInOut,
        alignment: Alignment.topCenter,
        child: Container(
          width: double.infinity,
          padding: const EdgeInsets.all(AppSpacing.lg),
          decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: [
                AppColors.primary.withValues(alpha: 0.3),
                AppColors.secondary.withValues(alpha: 0.2),
              ],
            ),
            borderRadius: BorderRadius.circular(20),
            border: Border.all(
              color: AppColors.primary.withValues(alpha: 0.3), width: 1,
            ),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              _buildHeader(),
              const SizedBox(height: AppSpacing.md),
              _buildQuoteText(),
              const SizedBox(height: AppSpacing.sm),
              _buildAuthor(),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildHeader() {
    return Row(
      children: [
        Icon(Icons.format_quote, size: 18, color: AppColors.primary),
        const SizedBox(width: AppSpacing.sm),
        Expanded(
          child: Text(
            widget.locale == 'pt'
                ? 'Frase do Dia'
                : widget.locale == 'es'
                    ? 'Frase del D\u00EDa'
                    : 'Quote of the Day',
            style: AppFonts.caption.copyWith(
              color: AppColors.primary,
              fontWeight: FontWeight.w600,
              letterSpacing: 0.5,
            ),
          ),
        ),
        if (widget.onFavoriteTap != null)
          GestureDetector(
            behavior: HitTestBehavior.opaque,
            onTap: () {
              HapticService.selection();
              widget.onFavoriteTap!();
            },
            child: SizedBox(
              width: 44, height: 44,
              child: Center(
                child: Icon(
                  widget.isFavorite ? Icons.favorite : Icons.favorite_border,
                  color: widget.isFavorite ? AppColors.love : AppColors.textTertiary,
                  size: 22,
                ),
              ),
            ),
          ),
        GestureDetector(
          behavior: HitTestBehavior.opaque,
          onTap: () {
            HapticService.light();
            Share.share(
              '\u201C${widget.quote.text(widget.locale)}\u201D \u2014 ${widget.quote.author(widget.locale)}',
            );
          },
          child: const SizedBox(
            width: 44, height: 44,
            child: Center(
              child: Icon(Icons.share_outlined, color: AppColors.textTertiary, size: 20),
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildQuoteText() {
    return LayoutBuilder(
      builder: (context, constraints) {
        final text = '\u201C${widget.quote.text(widget.locale)}\u201D';
        final style = AppFonts.headline.copyWith(
          color: AppColors.textPrimary,
          fontStyle: FontStyle.italic,
          height: 1.5,
        );

        final textPainter = TextPainter(
          text: TextSpan(text: text, style: style),
          maxLines: 4,
          textDirection: TextDirection.ltr,
        )..layout(maxWidth: constraints.maxWidth);

        WidgetsBinding.instance.addPostFrameCallback((_) {
          if (mounted && textPainter.didExceedMaxLines != _overflows) {
            setState(() => _overflows = textPainter.didExceedMaxLines);
          }
        });

        return Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              text,
              style: style,
              maxLines: _expanded ? null : 4,
              overflow: _expanded ? null : TextOverflow.ellipsis,
            ),
            if (_overflows)
              Padding(
                padding: const EdgeInsets.only(top: AppSpacing.xs),
                child: Text(
                  _expanded
                      ? (widget.locale == 'pt' ? 'ver menos' : widget.locale == 'es' ? 'ver menos' : 'see less')
                      : (widget.locale == 'pt' ? 'ver mais' : widget.locale == 'es' ? 'ver m\u00E1s' : 'see more'),
                  style: AppFonts.caption.copyWith(
                    color: AppColors.primary,
                    fontWeight: FontWeight.w600,
                  ),
                ),
              ),
          ],
        );
      },
    );
  }

  Widget _buildAuthor() {
    return Text(
      '\u2014 ${widget.quote.author(widget.locale)}',
      style: AppFonts.footnote.copyWith(color: AppColors.textSecondary),
    );
  }
}
