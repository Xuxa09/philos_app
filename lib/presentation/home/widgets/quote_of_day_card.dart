import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:go_router/go_router.dart';
import '../../common/widgets/share_quote_sheet.dart';
import '../../../core/constants/share_style_data.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';
import '../../../core/utils/haptic_service.dart';
import '../../../data/models/quote_model.dart';
import '../../../data/services/storage_service.dart';
import '../../common/widgets/pressable_scale.dart';
import '../../journal/widgets/reflection_sheet.dart';

class QuoteOfDayCard extends StatefulWidget {
  final QuoteModel quote;
  final String locale;
  final bool isFavorite;
  final VoidCallback? onFavoriteTap;
  final VoidCallback? onStyleChanged;

  const QuoteOfDayCard({
    super.key,
    required this.quote,
    required this.locale,
    this.isFavorite = false,
    this.onFavoriteTap,
    this.onStyleChanged,
  });

  @override
  State<QuoteOfDayCard> createState() => _QuoteOfDayCardState();
}

class _QuoteOfDayCardState extends State<QuoteOfDayCard> with SingleTickerProviderStateMixin {
  bool _expanded = false;
  bool _overflows = false;
  final _storage = StorageService.instance;

  late final AnimationController _favoriteController;
  late final Animation<double> _favoriteScale;

  String get _bgKey => _storage.cardBackground;
  String get _fontKey => _storage.cardFontStyle;

  bool get _isDarkBg {
    final key = _bgKey;
    if (key == 'default') return false;
    return true;
  }

  Color get _textColor => _isDarkBg ? Colors.white : AppColors.textPrimary;
  Color get _subtextColor => _isDarkBg ? Colors.white.withValues(alpha: 0.7) : AppColors.textSecondary;
  Color get _iconColor => _isDarkBg ? Colors.white.withValues(alpha: 0.8) : AppColors.textTertiary;
  Color get _accentColor => _isDarkBg ? Colors.white : AppColors.primary;

  @override
  void initState() {
    super.initState();
    _favoriteController = AnimationController(vsync: this, duration: const Duration(milliseconds: 400));
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

  @override
  void didUpdateWidget(covariant QuoteOfDayCard oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.quote.id != widget.quote.id) {
      _expanded = false;
      _overflows = false;
    }
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
            _menuItem(
              icon: Icons.edit_note,
              label: locale == 'pt' ? 'Refletir' : locale == 'es' ? 'Reflexionar' : 'Reflect',
              onTap: () {
                Navigator.pop(ctx);
                ReflectionSheet.show(context, locale, quote: widget.quote);
              },
            ),
            _menuItem(
              icon: Icons.palette_outlined,
              label: locale == 'pt' ? 'Personalizar' : locale == 'es' ? 'Personalizar' : 'Customize',
              onTap: () async {
                Navigator.pop(ctx);
                await context.push('/widget-editor');
                if (mounted) {
                  setState(() {});
                  widget.onStyleChanged?.call();
                }
              },
            ),
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

  BoxDecoration _buildCardDecoration() {
    final key = _bgKey;
    final isImage = key.startsWith('img_');

    if (key == 'custom') {
      final customPath = _storage.cardCustomImagePath;
      if (customPath != null && File(customPath).existsSync()) {
        return BoxDecoration(
          borderRadius: BorderRadius.circular(20),
          image: DecorationImage(
            image: FileImage(File(customPath)),
            fit: BoxFit.cover,
            colorFilter: ColorFilter.mode(Colors.black.withValues(alpha: 0.35), BlendMode.darken),
          ),
        );
      }
    }

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
          colorFilter: ColorFilter.mode(Colors.black.withValues(alpha: 0.35), BlendMode.darken),
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
      color: _textColor,
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
        _showOptionsMenu(context);
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
        if (widget.isFavorite)
          GestureDetector(
            behavior: HitTestBehavior.opaque,
            onTap: _doFavorite,
            child: AnimatedBuilder(
              animation: _favoriteScale,
              builder: (context, child) => Transform.scale(scale: _favoriteScale.value, child: child),
              child: const SizedBox(
                width: 44, height: 44,
                child: Center(child: Icon(Icons.favorite, color: AppColors.love, size: 28)),
              ),
            ),
          ),
        Builder(builder: (ctx) => GestureDetector(
          behavior: HitTestBehavior.opaque,
          onTap: () {
            HapticService.light();
            _showOptionsMenu(ctx);
          },
          child: SizedBox(
            width: 44, height: 44,
            child: Center(
              child: Icon(Icons.more_vert, color: _iconColor, size: 28),
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
      style: AppFonts.footnote.copyWith(color: _subtextColor),
    );
  }
}
