import 'package:flutter/material.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';

class OnboardingPage extends StatelessWidget {
  final IconData icon;
  final Color iconColor;
  final String title;
  final String description;

  const OnboardingPage({super.key, required this.icon, required this.iconColor, required this.title, required this.description});

  @override
  Widget build(BuildContext context) {
    return Padding(padding: const EdgeInsets.symmetric(horizontal: AppSpacing.xl),
      child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
        Container(width: 120, height: 120,
          decoration: BoxDecoration(color: iconColor.withValues(alpha: 0.15), shape: BoxShape.circle),
          child: Icon(icon, size: 56, color: iconColor)),
        const SizedBox(height: AppSpacing.xl),
        Text(title, style: AppFonts.title.copyWith(color: AppColors.textPrimary), textAlign: TextAlign.center),
        const SizedBox(height: AppSpacing.md),
        Text(description, style: AppFonts.body.copyWith(color: AppColors.textSecondary, height: 1.5), textAlign: TextAlign.center),
      ]));
  }
}
