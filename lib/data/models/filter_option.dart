// === Filter Option Model ===

import 'package:flutter/material.dart';

class FilterOption {
  final String key;
  final String name;
  final IconData icon;
  final Color color;

  const FilterOption({
    required this.key,
    required this.name,
    required this.icon,
    required this.color,
  });
}
