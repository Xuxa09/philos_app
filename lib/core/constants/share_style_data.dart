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
    BgOption(key: 'gradient', label: 'Sépia', colors: [Color(0xFF3A2A1A), Color(0xFF6B4226)]),
    BgOption(key: 'dark', label: 'Noturno', colors: [Color(0xFF1A1410), Color(0xFF3A2A1A)]),
    BgOption(key: 'gold', label: 'Dourado', colors: [Color(0xFF3A2A1A), Color(0xFF8B6B28)]),
    BgOption(key: 'purple', label: 'Violeta', colors: [Color(0xFF2D1B3D), Color(0xFF6B4888)]),
    BgOption(key: 'green', label: 'Oliva', colors: [Color(0xFF1A2418), Color(0xFF4A6848)]),
    BgOption(key: 'wine', label: 'Carmesim', colors: [Color(0xFF2A0A1B), Color(0xFF884848)]),
  ];

  static const imageBackgrounds = [
    ImgBgOption(key: 'img_default', label: 'Cl\u00e1ssico', asset: 'assets/images/backgrouns_cards.jpg'),
    ImgBgOption(key: 'img_biblioteca', label: 'Biblioteca', asset: 'assets/images/backgrouns_cards_biblioteca.jpg'),
    ImgBgOption(key: 'img_escultura', label: 'Escultura', asset: 'assets/images/backgrouns_cards_escultura.jpg'),
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
