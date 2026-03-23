import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../../core/utils/haptic_service.dart';
import '../../data/services/storage_service.dart';
import '../../data/services/widget_service.dart';
import '../common/widgets/pressable_scale.dart';

class WidgetEditorScreen extends StatefulWidget {
  const WidgetEditorScreen({super.key});
  @override
  State<WidgetEditorScreen> createState() => _WidgetEditorScreenState();
}

class _WidgetEditorScreenState extends State<WidgetEditorScreen> {
  final _storage = StorageService.instance;
  late String _selectedBg;
  late String _selectedFont;

  static const _backgrounds = [
    _BgOption(key: 'gradient', label: 'Gradiente', colors: [Color(0xFF1C1C1E), Color(0xFF0A84FF)]),
    _BgOption(key: 'dark', label: 'Escuro', colors: [Color(0xFF000000), Color(0xFF1C1C1E)]),
    _BgOption(key: 'gold', label: 'Dourado', colors: [Color(0xFF1C1C1E), Color(0x60D4A843)]),
    _BgOption(key: 'purple', label: 'Roxo', colors: [Color(0xFF5E2D91), Color(0xFFBF5AF2)]),
    _BgOption(key: 'green', label: 'Verde', colors: [Color(0xFF1C1C1E), Color(0x5030D158)]),
  ];

  static const _imageBackgrounds = [
    _ImgBgOption(key: 'img_biblioteca', label: 'Biblioteca', asset: 'assets/images/backgrouns_cards_biblioteca.jpg'),
    _ImgBgOption(key: 'img_escultura', label: 'Escultura', asset: 'assets/images/backgrouns_cards_escultura.jpg'),
    _ImgBgOption(key: 'img_colorido', label: 'Colorido', asset: 'assets/images/backgrouns_cards_colorido.jpg'),
    _ImgBgOption(key: 'img_cabeca', label: 'Arte', asset: 'assets/images/backgrouns_cards_cabeça_colorida.jpg'),
    _ImgBgOption(key: 'img_papel', label: 'Papel', asset: 'assets/images/backgrouns_cards_papel_velho.jpg'),
  ];

  static const _fonts = [
    _FontOption(key: 'serif', label: 'Clássica', family: 'serif', style: FontStyle.italic),
    _FontOption(key: 'sans', label: 'Moderna', family: 'sans-serif', style: FontStyle.normal),
    _FontOption(key: 'mono', label: 'Mono', family: 'monospace', style: FontStyle.normal),
  ];

  @override
  void initState() {
    super.initState();
    _selectedBg = _storage.widgetBackground;
    _selectedFont = _storage.widgetFontStyle;
  }

  Future<void> _save() async {
    await _storage.setWidgetBackground(_selectedBg);
    await _storage.setWidgetFontStyle(_selectedFont);
    await WidgetService.updateStyle();
  }

  @override
  Widget build(BuildContext context) {
    final locale = Localizations.localeOf(context).languageCode;
    return Scaffold(
      backgroundColor: AppColors.background,
      body: SafeArea(child: Column(children: [
        _buildHeader(context, locale),
        Expanded(child: ListView(padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding), children: [
          const SizedBox(height: AppSpacing.md),
          _buildPreview(),
          const SizedBox(height: AppSpacing.lg),
          _buildSectionTitle(locale == 'pt' ? 'Fundo' : locale == 'es' ? 'Fondo' : 'Background'),
          const SizedBox(height: AppSpacing.sm),
          _buildColorOptions(),
          const SizedBox(height: AppSpacing.md),
          _buildSectionTitle(locale == 'pt' ? 'Imagens' : locale == 'es' ? 'Imágenes' : 'Images'),
          const SizedBox(height: AppSpacing.sm),
          _buildImageOptions(),
          const SizedBox(height: AppSpacing.lg),
          _buildSectionTitle(locale == 'pt' ? 'Fonte' : locale == 'es' ? 'Fuente' : 'Font'),
          const SizedBox(height: AppSpacing.sm),
          _buildFontOptions(),
          const SizedBox(height: AppSpacing.xl),
          _buildAddButton(locale),
          const SizedBox(height: AppSpacing.xxl),
        ])),
      ])),
    );
  }

  Widget _buildHeader(BuildContext context, String locale) {
    return Padding(
      padding: const EdgeInsets.all(AppSpacing.screenPadding),
      child: Row(children: [
        GestureDetector(onTap: () => context.pop(),
          child: const Icon(Icons.arrow_back_ios, color: AppColors.textPrimary, size: 20)),
        const SizedBox(width: AppSpacing.sm),
        Text(locale == 'pt' ? 'Personalizar Widget' : locale == 'es' ? 'Personalizar Widget' : 'Customize Widget',
          style: AppFonts.title2.copyWith(color: AppColors.textPrimary)),
      ]),
    );
  }

  Widget _buildPreview() {
    final isImage = _selectedBg.startsWith('img_');
    final fontOpt = _fonts.firstWhere((f) => f.key == _selectedFont, orElse: () => _fonts.first);

    return Center(child: Container(
      width: 280, height: 160,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(24),
        image: isImage ? DecorationImage(
          image: AssetImage(_imageBackgrounds.firstWhere((i) => i.key == _selectedBg, orElse: () => _imageBackgrounds.first).asset),
          fit: BoxFit.cover,
          colorFilter: ColorFilter.mode(Colors.black.withValues(alpha: 0.4), BlendMode.darken),
        ) : null,
        gradient: !isImage ? LinearGradient(
          begin: Alignment.topLeft, end: Alignment.bottomRight,
          colors: _backgrounds.firstWhere((b) => b.key == _selectedBg, orElse: () => _backgrounds.first).colors,
        ) : null,
      ),
      padding: const EdgeInsets.all(20),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Row(children: [
          Text('❝', style: TextStyle(color: AppColors.primary, fontSize: 16)),
          Text('  Philos', style: TextStyle(color: AppColors.textTertiary, fontSize: 11, fontWeight: FontWeight.w500, letterSpacing: 0.5)),
        ]),
        const SizedBox(height: 10),
        Expanded(child: Center(child: Text(
          '\u201CA felicidade depende da qualidade dos seus pensamentos.\u201D',
          style: TextStyle(
            color: Colors.white, fontSize: 14,
            fontFamily: fontOpt.family,
            fontStyle: fontOpt.style, height: 1.4,
          ),
          maxLines: 3, overflow: TextOverflow.ellipsis,
        ))),
        Align(alignment: Alignment.centerRight,
          child: Text('— Marco Aurélio', style: TextStyle(color: AppColors.primary, fontSize: 12, fontWeight: FontWeight.w500))),
      ]),
    ));
  }

  Widget _buildSectionTitle(String title) {
    return Text(title.toUpperCase(),
      style: AppFonts.caption.copyWith(color: AppColors.textTertiary, letterSpacing: 1, fontWeight: FontWeight.w600));
  }

  Widget _buildColorOptions() {
    return SizedBox(height: 72, child: ListView.separated(
      scrollDirection: Axis.horizontal,
      itemCount: _backgrounds.length,
      separatorBuilder: (_, __) => const SizedBox(width: AppSpacing.sm),
      itemBuilder: (_, index) {
        final bg = _backgrounds[index];
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
      itemCount: _imageBackgrounds.length,
      separatorBuilder: (_, __) => const SizedBox(width: AppSpacing.sm),
      itemBuilder: (_, index) {
        final img = _imageBackgrounds[index];
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
                decoration: BoxDecoration(
                  color: Colors.black.withValues(alpha: 0.3),
                  borderRadius: BorderRadius.circular(10),
                ),
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
    return Row(children: _fonts.map((font) {
      final selected = _selectedFont == font.key;
      return Expanded(child: Padding(
        padding: EdgeInsets.only(right: font == _fonts.last ? 0 : AppSpacing.sm),
        child: PressableScale(
          onTap: () { HapticService.selection(); setState(() => _selectedFont = font.key); _save(); },
          child: AnimatedContainer(
            duration: const Duration(milliseconds: 200),
            padding: const EdgeInsets.symmetric(vertical: AppSpacing.md),
            decoration: BoxDecoration(
              color: selected ? AppColors.primary.withValues(alpha: 0.12) : AppColors.surface,
              borderRadius: BorderRadius.circular(14),
              border: Border.all(color: selected ? AppColors.primary : AppColors.surfaceSecondary, width: selected ? 1.5 : 1),
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

  Widget _buildAddButton(String locale) {
    return PressableScale(
      onTap: () {
        HapticService.light();
        context.push('/widget-tutorial');
      },
      child: Container(
        width: double.infinity,
        padding: const EdgeInsets.symmetric(vertical: AppSpacing.md),
        decoration: BoxDecoration(
          color: AppColors.primary,
          borderRadius: BorderRadius.circular(14),
        ),
        child: Center(child: Text(
          locale == 'pt' ? 'Adicionar Widget' : locale == 'es' ? 'Añadir Widget' : 'Add Widget',
          style: AppFonts.body.copyWith(color: Colors.white, fontWeight: FontWeight.w600),
        )),
      ),
    );
  }
}

class _BgOption {
  final String key, label;
  final List<Color> colors;
  const _BgOption({required this.key, required this.label, required this.colors});
}

class _ImgBgOption {
  final String key, label, asset;
  const _ImgBgOption({required this.key, required this.label, required this.asset});
}

class _FontOption {
  final String key, label, family;
  final FontStyle style;
  const _FontOption({required this.key, required this.label, required this.family, required this.style});
}
