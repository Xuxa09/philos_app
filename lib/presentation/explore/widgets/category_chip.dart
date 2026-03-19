import 'package:flutter/material.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';
import '../../../core/utils/haptic_service.dart';
import '../../../data/models/category_model.dart';

class CategoryChip extends StatelessWidget {
  final QuoteCategory category;
  final String locale;
  final bool isSelected;
  final VoidCallback onTap;

  const CategoryChip({super.key, required this.category, required this.locale, required this.isSelected, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () { HapticService.selection(); onTap(); },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        padding: const EdgeInsets.symmetric(horizontal: AppSpacing.md, vertical: AppSpacing.sm),
        decoration: BoxDecoration(
          color: isSelected ? category.color.withValues(alpha: 0.2) : AppColors.surface,
          borderRadius: BorderRadius.circular(20),
          border: Border.all(color: isSelected ? category.color : AppColors.surfaceSecondary, width: 1),
        ),
        child: Row(mainAxisSize: MainAxisSize.min, children: [
          Icon(category.icon, size: 16, color: isSelected ? category.color : AppColors.textSecondary),
          const SizedBox(width: AppSpacing.xs),
          Flexible(child: Text(category.localizedName(locale),
            style: AppFonts.footnote.copyWith(color: isSelected ? category.color : AppColors.textSecondary,
              fontWeight: isSelected ? FontWeight.w600 : FontWeight.normal),
            overflow: TextOverflow.ellipsis, maxLines: 1)),
        ]),
      ),
    );
  }
}
