import 'dart:io';
import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:image_picker/image_picker.dart';
import 'package:path_provider/path_provider.dart';
import 'package:share_plus/share_plus.dart';
import '../../core/constants/share_style_data.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../../core/utils/haptic_service.dart';
import '../../data/models/quote_model.dart';
import '../common/widgets/pressable_scale.dart';

class ShareImageScreen extends StatefulWidget {
  final QuoteModel quote;
  final String locale;

  const ShareImageScreen({super.key, required this.quote, required this.locale});

  @override
  State<ShareImageScreen> createState() => _ShareImageScreenState();
}

class _ShareImageScreenState extends State<ShareImageScreen> {
  final _repaintKey = GlobalKey();
  final _picker = ImagePicker();
  String _selectedBg = 'gradient';
  String _selectedFont = 'serif';
  File? _customImage;
  bool _isSharing = false;

  Future<void> _pickImage(ImageSource source) async {
    final picked = await _picker.pickImage(source: source, maxWidth: 1920, maxHeight: 1920, imageQuality: 90);
    if (picked != null) {
      setState(() {
        _customImage = File(picked.path);
        _selectedBg = 'custom';
      });
    }
  }

  void _showImageSourcePicker() {
    final locale = widget.locale;
    showModalBottomSheet(
      context: context,
      backgroundColor: AppColors.surface,
      shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(20))),
      builder: (_) => SafeArea(child: Padding(
        padding: const EdgeInsets.all(AppSpacing.screenPadding),
        child: Column(mainAxisSize: MainAxisSize.min, children: [
          Container(width: 40, height: 4,
            decoration: BoxDecoration(color: AppColors.surfaceSecondary, borderRadius: BorderRadius.circular(2))),
          const SizedBox(height: AppSpacing.lg),
          Row(children: [
            Expanded(child: PressableScale(
              onTap: () { Navigator.pop(context); _pickImage(ImageSource.camera); },
              child: Container(
                padding: const EdgeInsets.symmetric(vertical: AppSpacing.lg),
                decoration: BoxDecoration(color: AppColors.surfaceSecondary, borderRadius: BorderRadius.circular(16)),
                child: Column(children: [
                  const Icon(Icons.camera_alt_outlined, color: AppColors.primary, size: 32),
                  const SizedBox(height: AppSpacing.sm),
                  Text(locale == 'pt' ? 'Câmera' : locale == 'es' ? 'Cámara' : 'Camera',
                    style: AppFonts.subheadline.copyWith(color: AppColors.textPrimary, fontWeight: FontWeight.w500)),
                ]),
              ),
            )),
            const SizedBox(width: AppSpacing.md),
            Expanded(child: PressableScale(
              onTap: () { Navigator.pop(context); _pickImage(ImageSource.gallery); },
              child: Container(
                padding: const EdgeInsets.symmetric(vertical: AppSpacing.lg),
                decoration: BoxDecoration(color: AppColors.surfaceSecondary, borderRadius: BorderRadius.circular(16)),
                child: Column(children: [
                  const Icon(Icons.photo_library_outlined, color: AppColors.primary, size: 32),
                  const SizedBox(height: AppSpacing.sm),
                  Text(locale == 'pt' ? 'Galeria' : locale == 'es' ? 'Galería' : 'Gallery',
                    style: AppFonts.subheadline.copyWith(color: AppColors.textPrimary, fontWeight: FontWeight.w500)),
                ]),
              ),
            )),
          ]),
          const SizedBox(height: AppSpacing.lg),
        ]),
      )),
    );
  }

  Future<void> _shareAsImage() async {
    if (_isSharing) return;
    setState(() => _isSharing = true);

    try {
      final boundary = _repaintKey.currentContext!.findRenderObject() as RenderRepaintBoundary;
      final image = await boundary.toImage(pixelRatio: 4.0);
      final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
      final bytes = byteData!.buffer.asUint8List();

      final dir = await getTemporaryDirectory();
      final file = File('${dir.path}/philos_quote.png');
      await file.writeAsBytes(bytes);

      await Share.shareXFiles([XFile(file.path)]);
    } finally {
      if (mounted) setState(() => _isSharing = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      body: SafeArea(child: Column(children: [
        _buildHeader(context),
        Expanded(child: ListView(
          padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
          children: [
            const SizedBox(height: AppSpacing.md),
            _buildCardPreview(),
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
            const SizedBox(height: AppSpacing.xl),
            _buildShareButton(),
            const SizedBox(height: AppSpacing.xxl),
          ],
        )),
      ])),
    );
  }

  Widget _buildHeader(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(AppSpacing.screenPadding),
      child: Row(children: [
        GestureDetector(onTap: () => Navigator.pop(context),
          child: const Icon(Icons.arrow_back_ios, color: AppColors.textPrimary, size: 20)),
        const SizedBox(width: AppSpacing.sm),
        Text(
          widget.locale == 'pt' ? 'Compartilhar imagem' : widget.locale == 'es' ? 'Compartir imagen' : 'Share image',
          style: AppFonts.title2.copyWith(color: AppColors.textPrimary)),
      ]),
    );
  }

  Widget _buildCardPreview() {
    final isCustom = _selectedBg == 'custom' && _customImage != null;
    final isAsset = _selectedBg.startsWith('img_');
    final fontOpt = ShareStyleData.findFont(_selectedFont);

    ImageProvider? bgImage;
    if (isCustom) {
      bgImage = FileImage(_customImage!);
    } else if (isAsset) {
      bgImage = AssetImage(ShareStyleData.findImg(_selectedBg).asset);
    }

    return Center(child: RepaintBoundary(
      key: _repaintKey,
      child: Container(
        width: 270, height: 480,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(24),
          image: bgImage != null ? DecorationImage(
            image: bgImage,
            fit: BoxFit.cover,
            colorFilter: ColorFilter.mode(Colors.black.withValues(alpha: 0.5), BlendMode.darken),
          ) : null,
          gradient: bgImage == null ? LinearGradient(
            begin: Alignment.topLeft, end: Alignment.bottomRight,
            colors: ShareStyleData.findBg(_selectedBg).colors,
          ) : null,
        ),
        padding: const EdgeInsets.all(28),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Row(children: [
            Text('\u275D', style: TextStyle(color: AppColors.primary, fontSize: 20)),
            Text('  Philos', style: TextStyle(color: Colors.white.withValues(alpha: 0.5), fontSize: 12, fontWeight: FontWeight.w500, letterSpacing: 0.5)),
          ]),
          const SizedBox(height: 24),
          Expanded(child: Center(child: Text(
            '\u201C${widget.quote.text(widget.locale)}\u201D',
            style: TextStyle(
              color: Colors.white, fontSize: 18,
              fontFamily: fontOpt.family,
              fontStyle: fontOpt.style, height: 1.5,
            ),
            textAlign: TextAlign.center,
          ))),
          const SizedBox(height: 20),
          Center(child: Text(
            '— ${widget.quote.author(widget.locale)}',
            style: TextStyle(color: AppColors.primary, fontSize: 14, fontWeight: FontWeight.w600),
          )),
        ]),
      ),
    ));
  }

  Widget _buildSectionTitle(String title) {
    return Text(title.toUpperCase(),
      style: AppFonts.caption.copyWith(color: AppColors.textTertiary, letterSpacing: 1, fontWeight: FontWeight.w600));
  }

  Widget _buildColorOptions() {
    return SizedBox(height: 72, child: ListView.separated(
      scrollDirection: Axis.horizontal,
      itemCount: ShareStyleData.backgrounds.length,
      separatorBuilder: (_, __) => const SizedBox(width: AppSpacing.sm),
      itemBuilder: (_, index) {
        final bg = ShareStyleData.backgrounds[index];
        final selected = _selectedBg == bg.key;
        return PressableScale(
          onTap: () { HapticService.selection(); setState(() => _selectedBg = bg.key); },
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
    final customSelected = _selectedBg == 'custom' && _customImage != null;
    return SizedBox(height: 80, child: ListView.separated(
      scrollDirection: Axis.horizontal,
      itemCount: ShareStyleData.imageBackgrounds.length + 1,
      separatorBuilder: (_, __) => const SizedBox(width: AppSpacing.sm),
      itemBuilder: (_, index) {
        // First item: pick from device
        if (index == 0) {
          return PressableScale(
            onTap: () { HapticService.selection(); _showImageSourcePicker(); },
            child: SizedBox(width: 56, child: Column(children: [
              AnimatedContainer(
                duration: const Duration(milliseconds: 200),
                width: 52, height: 52,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: customSelected ? AppColors.primary : AppColors.surfaceSecondary, width: customSelected ? 2 : 1),
                  image: _customImage != null ? DecorationImage(image: FileImage(_customImage!), fit: BoxFit.cover) : null,
                  color: _customImage == null ? AppColors.surfaceSecondary : null,
                ),
                child: _customImage == null
                    ? const Icon(Icons.add_photo_alternate_outlined, color: AppColors.textTertiary, size: 24)
                    : customSelected
                        ? Container(
                            decoration: BoxDecoration(color: Colors.black.withValues(alpha: 0.3), borderRadius: BorderRadius.circular(10)),
                            child: const Icon(Icons.check, color: Colors.white, size: 18))
                        : null,
              ),
              const SizedBox(height: 6),
              Text(widget.locale == 'pt' ? 'Sua foto' : widget.locale == 'es' ? 'Tu foto' : 'Your photo',
                style: AppFonts.caption.copyWith(color: customSelected ? AppColors.primary : AppColors.textTertiary),
                overflow: TextOverflow.ellipsis, maxLines: 1),
            ])),
          );
        }

        final imgIndex = index - 1;
        final img = ShareStyleData.imageBackgrounds[imgIndex];
        final selected = _selectedBg == img.key;
        return PressableScale(
          onTap: () { HapticService.selection(); setState(() => _selectedBg = img.key); },
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
          onTap: () { HapticService.selection(); setState(() => _selectedFont = font.key); },
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

  Widget _buildShareButton() {
    return PressableScale(
      onTap: _isSharing ? null : () { HapticService.light(); _shareAsImage(); },
      child: Container(
        width: double.infinity,
        padding: const EdgeInsets.symmetric(vertical: AppSpacing.md),
        decoration: BoxDecoration(
          color: AppColors.primary,
          borderRadius: BorderRadius.circular(14),
        ),
        child: Center(child: _isSharing
          ? const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2))
          : Row(mainAxisSize: MainAxisSize.min, children: [
              const Icon(Icons.share, color: Colors.white, size: 20),
              const SizedBox(width: AppSpacing.sm),
              Text(
                widget.locale == 'pt' ? 'Compartilhar' : widget.locale == 'es' ? 'Compartir' : 'Share',
                style: AppFonts.body.copyWith(color: Colors.white, fontWeight: FontWeight.w600),
              ),
            ]),
        ),
      ),
    );
  }
}
