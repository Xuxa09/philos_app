// === Share Style Data (shared between widget editor and share image) ===

import 'package:flutter/material.dart';

class BgOption {
  final String key, label;
  final List<Color> colors;
  const BgOption({required this.key, required this.label, required this.colors});
}

class ImgBgOption {
  final String key, label, asset;
  const ImgBgOption({required this.key, required this.label, required this.asset});
}

class FontOption {
  final String key, label, family;
  final FontStyle style;
  const FontOption({required this.key, required this.label, required this.family, required this.style});
}

abstract class ShareStyleData {
  static const backgrounds = [
    BgOption(key: 'gradient', label: 'Gradiente', colors: [Color(0xFF1C1C1E), Color(0xFF0A84FF)]),
    BgOption(key: 'dark', label: 'Escuro', colors: [Color(0xFF000000), Color(0xFF1C1C1E)]),
    BgOption(key: 'gold', label: 'Dourado', colors: [Color(0xFF1C1C1E), Color(0x60D4A843)]),
    BgOption(key: 'purple', label: 'Roxo', colors: [Color(0xFF5E2D91), Color(0xFFBF5AF2)]),
    BgOption(key: 'green', label: 'Verde', colors: [Color(0xFF1C1C1E), Color(0x5030D158)]),
    BgOption(key: 'wine', label: 'Vinho', colors: [Color(0xFF2A0A1B), Color(0xFF8B1A4A)]),
  ];

  static const imageBackgrounds = [
    ImgBgOption(key: 'img_biblioteca', label: 'Biblioteca', asset: 'assets/images/backgrouns_cards_biblioteca.jpg'),
    ImgBgOption(key: 'img_escultura', label: 'Escultura', asset: 'assets/images/backgrouns_cards_escultura.jpg'),
    ImgBgOption(key: 'img_colorido', label: 'Colorido', asset: 'assets/images/backgrouns_cards_colorido.jpg'),
    ImgBgOption(key: 'img_cabeca', label: 'Arte', asset: 'assets/images/backgrouns_cards_cabeça_colorida.jpg'),
    ImgBgOption(key: 'img_papel', label: 'Papel', asset: 'assets/images/backgrouns_cards_papel_velho.jpg'),
  ];

  static const fonts = [
    FontOption(key: 'serif', label: 'Clássica', family: 'serif', style: FontStyle.italic),
    FontOption(key: 'sans', label: 'Moderna', family: 'sans-serif', style: FontStyle.normal),
    FontOption(key: 'mono', label: 'Mono', family: 'monospace', style: FontStyle.normal),
  ];

  static BgOption findBg(String key) => backgrounds.firstWhere((b) => b.key == key, orElse: () => backgrounds.first);
  static ImgBgOption findImg(String key) => imageBackgrounds.firstWhere((i) => i.key == key, orElse: () => imageBackgrounds.first);
  static FontOption findFont(String key) => fonts.firstWhere((f) => f.key == key, orElse: () => fonts.first);
}
