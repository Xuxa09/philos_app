import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../core/extensions/context_extensions.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../../core/utils/haptic_service.dart';
import '../common/widgets/app_button.dart';
import 'onboarding_view_model.dart';
import 'widgets/onboarding_page.dart';

class OnboardingScreen extends StatefulWidget {
  const OnboardingScreen({super.key});
  @override
  State<OnboardingScreen> createState() => _OnboardingScreenState();
}

class _OnboardingScreenState extends State<OnboardingScreen> {
  late final OnboardingViewModel _vm;

  @override
  void initState() { super.initState(); _vm = OnboardingViewModel(); }

  @override
  void dispose() { _vm.dispose(); super.dispose(); }

  @override
  Widget build(BuildContext context) {
    return Scaffold(backgroundColor: AppColors.background,
      body: SafeArea(child: ListenableBuilder(listenable: _vm, builder: (context, _) {
        return Column(children: [
          Align(alignment: Alignment.topRight, child: Padding(
            padding: const EdgeInsets.all(AppSpacing.md),
            child: GestureDetector(onTap: () => _finish(context),
              child: Text(context.l10n.onboardingSkip, style: AppFonts.callout.copyWith(color: AppColors.textSecondary))))),
          Expanded(child: PageView(controller: _vm.pageController, onPageChanged: _vm.setPage, children: [
            OnboardingPage(icon: Icons.format_quote, iconColor: AppColors.primary,
              title: context.l10n.onboardingTitle1, description: context.l10n.onboardingDesc1),
            OnboardingPage(icon: Icons.explore, iconColor: AppColors.success,
              title: context.l10n.onboardingTitle2, description: context.l10n.onboardingDesc2),
            OnboardingPage(icon: Icons.favorite, iconColor: AppColors.love,
              title: context.l10n.onboardingTitle3, description: context.l10n.onboardingDesc3),
          ])),
          Row(mainAxisAlignment: MainAxisAlignment.center, children: List.generate(_vm.totalPages, (index) => AnimatedContainer(
            duration: const Duration(milliseconds: 300), margin: const EdgeInsets.symmetric(horizontal: 4),
            width: _vm.currentPage == index ? 24 : 8, height: 8,
            decoration: BoxDecoration(color: _vm.currentPage == index ? AppColors.primary : AppColors.surfaceSecondary,
              borderRadius: BorderRadius.circular(4))))),
          const SizedBox(height: AppSpacing.xl),
          Padding(padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
            child: AppButton(title: _vm.isLastPage ? context.l10n.onboardingGetStarted : context.l10n.onboardingNext,
              onTap: () { if (_vm.isLastPage) _finish(context); else _vm.nextPage(); })),
          const SizedBox(height: AppSpacing.xxl),
        ]);
      })));
  }

  void _finish(BuildContext context) { HapticService.success(); _vm.completeOnboarding(); context.go('/'); }
}
