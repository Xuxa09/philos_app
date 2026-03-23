import 'package:flutter/material.dart';
import '../../../core/constants/share_style_data.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';
import '../../../core/utils/haptic_service.dart';
import '../../../data/models/quote_model.dart';
import '../../../data/services/storage_service.dart';
import '../../common/widgets/pressable_scale.dart';

class CardEditorSheet extends StatefulWidget {
  final QuoteModel quote;
  final String locale;
  final VoidCallback onChanged;

  const CardEditorSheet({super.key, required this.quote, required this.locale, required this.onChanged});

  static void show(BuildContext context, QuoteModel quote, String locale, VoidCallback onChanged) {
    showModalBottomSheet(
      context: context,
      useRootNavigator: true,
      backgroundColor: AppColors.surface,
      isScrollControlled: true,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
      ),
      builder: (_) => DraggableScrollableSheet(
        initialChildSize: 0.85,
        minChildSize: 0.5,
        maxChildSize: 0.92,
        expand: false,
        builder: (_, scrollController) => CardEditorSheet(
          quote: quote, locale: locale, onChanged: onChanged,
        )._buildScrollable(scrollController),
      ),
    );
  }

  Widget _buildScrollable(ScrollController controller) {
    return _CardEditorSheetContent(
      quote: quote, locale: locale, onChanged: onChanged, scrollController: controller,
    );
  }

  @override
  State<CardEditorSheet> createState() => _CardEditorSheetState();
}

class _CardEditorSheetState extends State<CardEditorSheet> {
  @override
  Widget build(BuildContext context) => const SizedBox.shrink();
}

class _CardEditorSheetContent extends StatefulWidget {
  final QuoteModel quote;
  final String locale;
  final VoidCallback onChanged;
  final ScrollController scrollController;

  const _CardEditorSheetContent({
    required this.quote, required this.locale, required this.onChanged, required this.scrollController,
  });

  @override
  State<_CardEditorSheetContent> createState() => _CardEditorSheetContentState();
}

class _CardEditorSheetContentState extends State<_CardEditorSheetContent> {
  final _storage = StorageService.instance;
  late String _selectedBg;
  late String _selectedFont;

  static const _defaultBg = BgOption(key: 'default', label: 'Padrão', colors: [Color(0xFF0A84FF), Color(0xFF0060CC)]);

  @override
  void initState() {
    super.initState();
    _selectedBg = _storage.cardBackground;
    _selectedFont = _storage.cardFontStyle;
  }

  Future<void> _save() async {
    await _storage.setCardBackground(_selectedBg);
    await _storage.setCardFontStyle(_selectedFont);
    widget.onChanged();
  }

  BoxDecoration _previewDecoration() {
    final key = _selectedBg;
    final isImage = key.startsWith('img_');

    if (key == 'default') {
      return BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment.topLeft, end: Alignment.bottomRight,
          colors: [AppColors.primary.withValues(alpha: 0.3), AppColors.secondary.withValues(alpha: 0.2)],
        ),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: AppColors.primary.withValues(alpha: 0.3), width: 1),
      );
    }
    if (isImage) {
      return BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        image: DecorationImage(
          image: AssetImage(ShareStyleData.findImg(key).asset),
          fit: BoxFit.cover,
          colorFilter: ColorFilter.mode(Colors.black.withValues(alpha: 0.5), BlendMode.darken),
        ),
      );
    }
    return BoxDecoration(
      gradient: LinearGradient(
        begin: Alignment.topLeft, end: Alignment.bottomRight,
        colors: ShareStyleData.findBg(key).colors,
      ),
      borderRadius: BorderRadius.circular(20),
    );
  }

  @override
  Widget build(BuildContext context) {
    final font = ShareStyleData.findFont(_selectedFont);
    return ListView(
      controller: widget.scrollController,
      padding: const EdgeInsets.all(AppSpacing.screenPadding),
      children: [
        Center(child: Container(width: 40, height: 4,
          decoration: BoxDecoration(color: AppColors.surfaceSecondary, borderRadius: BorderRadius.circular(2)))),
        const SizedBox(height: AppSpacing.lg),

        // Preview
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(AppSpacing.lg),
          decoration: _previewDecoration(),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Row(children: [
              Icon(Icons.format_quote, size: 18, color: AppColors.primary),
              const SizedBox(width: AppSpacing.sm),
              Text(
                widget.locale == 'pt' ? 'Frase do Dia' : widget.locale == 'es' ? 'Frase del Día' : 'Quote of the Day',
                style: AppFonts.caption.copyWith(color: AppColors.primary, fontWeight: FontWeight.w600, letterSpacing: 0.5),
              ),
            ]),
            const SizedBox(height: AppSpacing.md),
            Text(
              '\u201C${widget.quote.text(widget.locale)}\u201D',
              style: TextStyle(
                color: AppColors.textPrimary, fontSize: 17,
                fontFamily: font.family, fontStyle: font.style,
                fontWeight: FontWeight.w600, height: 1.5,
              ),
              maxLines: 4, overflow: TextOverflow.ellipsis,
            ),
            const SizedBox(height: AppSpacing.sm),
            Text('\u2014 ${widget.quote.author(widget.locale)}',
              style: AppFonts.footnote.copyWith(color: AppColors.textSecondary)),
          ]),
        ),

        const SizedBox(height: AppSpacing.lg),
        _buildSectionTitle(widget.locale == 'pt' ? 'Fundo' : widget.locale == 'es' ? 'Fondo' : 'Background'),
        const SizedBox(height: AppSpacing.sm),
        _buildColorOptions(),
        const SizedBox(height: AppSpacing.md),
        _buildSectionTitle(widget.locale == 'pt' ? 'Imagens' : widget.locale == 'es' ? 'Imágenes' : 'Images'),
        const SizedBox(height: AppSpacing.sm),
        _buildImageOptions(),
        const SizedBox(height: AppSpacing.lg),
        _buildSectionTitle(widget.locale == 'pt' ? 'Fonte' : widget.locale == 'es' ? 'Fuente' : 'Font'),
        const SizedBox(height: AppSpacing.sm),
        _buildFontOptions(),
        const SizedBox(height: AppSpacing.lg),
      ],
    );
  }

  Widget _buildSectionTitle(String title) {
    return Text(title.toUpperCase(),
      style: AppFonts.caption.copyWith(color: AppColors.textTertiary, letterSpacing: 1, fontWeight: FontWeight.w600));
  }

  Widget _buildColorOptions() {
    final all = [_defaultBg, ...ShareStyleData.backgrounds];
    return SizedBox(height: 72, child: ListView.separated(
      scrollDirection: Axis.horizontal,
      itemCount: all.length,
      separatorBuilder: (_, __) => const SizedBox(width: AppSpacing.sm),
      itemBuilder: (_, index) {
        final bg = all[index];
        final selected = _selectedBg == bg.key;
        return PressableScale(
          onTap: () { HapticService.selection(); setState(() => _selectedBg = bg.key); _save(); },
          child: SizedBox(width: 52, child: Column(children: [
            AnimatedContainer(
              duration: const Duration(milliseconds: 200),
              width: 44, height: 44,
              decoration: BoxDecoration(
                gradient: LinearGradient(colors: bg.colors, begin: Alignment.topLeft, end: Alignment.bottomRight),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: selected ? AppColors.primary : Colors.transparent, width: 2),
              ),
              child: selected ? const Icon(Icons.check, color: Colors.white, size: 18) : null,
            ),
            const SizedBox(height: 6),
            Text(bg.label, style: AppFonts.caption.copyWith(color: selected ? AppColors.primary : AppColors.textTertiary),
              overflow: TextOverflow.ellipsis, maxLines: 1),
          ])),
        );
      },
    ));
  }

  Widget _buildImageOptions() {
    return SizedBox(height: 80, child: ListView.separated(
      scrollDirection: Axis.horizontal,
      itemCount: ShareStyleData.imageBackgrounds.length,
      separatorBuilder: (_, __) => const SizedBox(width: AppSpacing.sm),
      itemBuilder: (_, index) {
        final img = ShareStyleData.imageBackgrounds[index];
        final selected = _selectedBg == img.key;
        return PressableScale(
          onTap: () { HapticService.selection(); setState(() => _selectedBg = img.key); _save(); },
          child: SizedBox(width: 56, child: Column(children: [
            AnimatedContainer(
              duration: const Duration(milliseconds: 200),
              width: 52, height: 52,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: selected ? AppColors.primary : Colors.transparent, width: 2),
                image: DecorationImage(image: AssetImage(img.asset), fit: BoxFit.cover),
              ),
              child: selected ? Container(
                decoration: BoxDecoration(color: Colors.black.withValues(alpha: 0.3), borderRadius: BorderRadius.circular(10)),
                child: const Icon(Icons.check, color: Colors.white, size: 18),
              ) : null,
            ),
            const SizedBox(height: 6),
            Text(img.label, style: AppFonts.caption.copyWith(color: selected ? AppColors.primary : AppColors.textTertiary),
              overflow: TextOverflow.ellipsis, maxLines: 1),
          ])),
        );
      },
    ));
  }

  Widget _buildFontOptions() {
    return Row(children: ShareStyleData.fonts.map((font) {
      final selected = _selectedFont == font.key;
      return Expanded(child: Padding(
        padding: EdgeInsets.only(right: font == ShareStyleData.fonts.last ? 0 : AppSpacing.sm),
        child: PressableScale(
          onTap: () { HapticService.selection(); setState(() => _selectedFont = font.key); _save(); },
          child: AnimatedContainer(
            duration: const Duration(milliseconds: 200),
            padding: const EdgeInsets.symmetric(vertical: AppSpacing.md),
            decoration: BoxDecoration(
              color: selected ? AppColors.primary.withValues(alpha: 0.12) : AppColors.surfaceSecondary,
              borderRadius: BorderRadius.circular(14),
              border: Border.all(color: selected ? AppColors.primary : Colors.transparent, width: selected ? 1.5 : 1),
            ),
            child: Column(children: [
              Text('Abc', style: TextStyle(
                fontFamily: font.family, fontStyle: font.style,
                color: selected ? AppColors.primary : AppColors.textSecondary,
                fontSize: 18, fontWeight: FontWeight.w500,
              )),
              const SizedBox(height: 4),
              Text(font.label, style: AppFonts.caption.copyWith(
                color: selected ? AppColors.primary : AppColors.textTertiary,
                fontWeight: selected ? FontWeight.w600 : FontWeight.normal,
              )),
            ]),
          ),
        ),
      ));
    }).toList());
  }
}
