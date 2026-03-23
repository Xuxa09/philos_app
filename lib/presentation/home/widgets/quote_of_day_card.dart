import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../../common/widgets/share_quote_sheet.dart';
import '../../../core/constants/share_style_data.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';
import '../../../core/utils/haptic_service.dart';
import '../../../data/models/quote_model.dart';
import '../../../data/services/storage_service.dart';
import '../../common/widgets/pressable_scale.dart';
import 'card_editor_sheet.dart';

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
  final _storage = StorageService.instance;

  String get _bgKey => _storage.cardBackground;
  String get _fontKey => _storage.cardFontStyle;

  bool get _isLightBg {
    final key = _bgKey;
    return key == 'img_papel' || key == 'img_colorido';
  }

  Color get _iconColor => _isLightBg ? Colors.white.withValues(alpha: 0.9) : AppColors.textTertiary;
  Color get _accentColor => _isLightBg ? Colors.white : AppColors.primary;

  @override
  void didUpdateWidget(covariant QuoteOfDayCard oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.quote.id != widget.quote.id) {
      _expanded = false;
      _overflows = false;
    }
  }

  BoxDecoration _buildCardDecoration() {
    final key = _bgKey;
    final isImage = key.startsWith('img_');

    if (key == 'default') {
      return BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment.topLeft, end: Alignment.bottomRight,
          colors: [
            AppColors.primary.withValues(alpha: 0.3),
            AppColors.secondary.withValues(alpha: 0.2),
          ],
        ),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: AppColors.primary.withValues(alpha: 0.3), width: 1),
      );
    }

    if (isImage) {
      final img = ShareStyleData.findImg(key);
      return BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        image: DecorationImage(
          image: AssetImage(img.asset),
          fit: BoxFit.cover,
          colorFilter: ColorFilter.mode(Colors.black.withValues(alpha: 0.5), BlendMode.darken),
        ),
      );
    }

    final bg = ShareStyleData.findBg(key);
    return BoxDecoration(
      gradient: LinearGradient(
        begin: Alignment.topLeft, end: Alignment.bottomRight,
        colors: bg.colors,
      ),
      borderRadius: BorderRadius.circular(20),
    );
  }

  TextStyle _buildQuoteStyle() {
    final font = ShareStyleData.findFont(_fontKey);
    return TextStyle(
      color: AppColors.textPrimary,
      fontSize: 17,
      fontFamily: font.family,
      fontStyle: font.style,
      fontWeight: FontWeight.w600,
      height: 1.5,
    );
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
          decoration: _buildCardDecoration(),
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
        Icon(Icons.format_quote, size: 18, color: _accentColor),
        const SizedBox(width: AppSpacing.sm),
        Expanded(
          child: Text(
            widget.locale == 'pt'
                ? 'Frase do Dia'
                : widget.locale == 'es'
                    ? 'Frase del D\u00EDa'
                    : 'Quote of the Day',
            style: AppFonts.caption.copyWith(
              color: _accentColor,
              fontWeight: FontWeight.w600,
              letterSpacing: 0.5,
            ),
          ),
        ),
        GestureDetector(
          behavior: HitTestBehavior.opaque,
          onTap: () {
            HapticService.selection();
            CardEditorSheet.show(context, widget.quote, widget.locale, () => setState(() {}));
          },
          child: SizedBox(
            width: 44, height: 44,
            child: Center(
              child: Icon(Icons.palette_outlined, color: _iconColor, size: 20),
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
                  color: widget.isFavorite ? AppColors.love : _iconColor,
                  size: 22,
                ),
              ),
            ),
          ),
        Builder(builder: (ctx) => GestureDetector(
          behavior: HitTestBehavior.opaque,
          onTap: () {
            HapticService.light();
            ShareQuoteSheet.show(ctx, widget.quote, widget.locale);
          },
          child: SizedBox(
            width: 44, height: 44,
            child: Center(
              child: Icon(Icons.share_outlined, color: _iconColor, size: 20),
            ),
          ),
        )),
      ],
    );
  }

  Widget _buildQuoteText() {
    return LayoutBuilder(
      builder: (context, constraints) {
        final text = '\u201C${widget.quote.text(widget.locale)}\u201D';
        final style = _buildQuoteStyle();

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
                    color: _accentColor,
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
