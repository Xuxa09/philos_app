import 'package:flutter/material.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';
import '../../../core/utils/haptic_service.dart';
import '../../../data/models/mood_model.dart';
import '../../common/widgets/pressable_scale.dart';

class MoodCard extends StatelessWidget {
  final MoodType mood;
  final String locale;
  final bool isSelected;
  final VoidCallback onTap;

  const MoodCard({super.key, required this.mood, required this.locale, required this.isSelected, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return PressableScale(
      onTap: () { HapticService.selection(); onTap(); },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 250),
        padding: const EdgeInsets.all(AppSpacing.md),
        decoration: BoxDecoration(
          color: isSelected ? mood.color.withValues(alpha: 0.15) : AppColors.surface,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: isSelected ? mood.color : AppColors.surfaceSecondary, width: isSelected ? 1.5 : 1),
        ),
        child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
          Icon(mood.icon, color: mood.color, size: 32),
          const SizedBox(height: AppSpacing.sm),
          Text(mood.localizedName(locale),
            style: AppFonts.footnote.copyWith(color: isSelected ? mood.color : AppColors.textSecondary,
              fontWeight: isSelected ? FontWeight.w600 : FontWeight.normal),
            textAlign: TextAlign.center, maxLines: 1, overflow: TextOverflow.ellipsis),
        ]),
      ),
    );
  }
}
