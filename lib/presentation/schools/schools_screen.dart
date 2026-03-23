import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../../core/utils/haptic_service.dart';
import '../common/widgets/pressable_scale.dart';
import '../common/widgets/quote_card.dart';
import 'schools_view_model.dart';

class SchoolsScreen extends StatelessWidget {
  const SchoolsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final locale = Localizations.localeOf(context).languageCode;
    return Scaffold(
      backgroundColor: AppColors.background,
      body: Consumer<SchoolsViewModel>(builder: (context, vm, _) {
        return SafeArea(child: CustomScrollView(slivers: [
          _buildHeader(context, locale),
          _buildSchoolsGrid(vm, locale),
          if (vm.quotes.isNotEmpty) ...[
            _buildQuotesHeader(vm, locale),
            _buildQuotesList(vm, locale),
          ],
          const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.xxl)),
        ]));
      }),
    );
  }

  SliverToBoxAdapter _buildHeader(BuildContext context, String locale) {
    return SliverToBoxAdapter(child: Padding(
      padding: const EdgeInsets.all(AppSpacing.screenPadding),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        GestureDetector(onTap: () => context.pop(),
          child: const Icon(Icons.arrow_back_ios, color: AppColors.textPrimary, size: 20)),
        const SizedBox(height: AppSpacing.md),
        Text(locale == 'pt' ? 'Escolas Filosóficas' : locale == 'es' ? 'Escuelas Filosóficas' : 'Philosophical Schools',
          style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)),
        const SizedBox(height: AppSpacing.xs),
        Text(locale == 'pt' ? 'Escolha uma escola' : locale == 'es' ? 'Elige una escuela' : 'Choose a school',
          style: AppFonts.body.copyWith(color: AppColors.textSecondary)),
      ]),
    ));
  }

  SliverPadding _buildSchoolsGrid(SchoolsViewModel vm, String locale) {
    return SliverPadding(
      padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
      sliver: SliverGrid(
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 3, mainAxisSpacing: AppSpacing.sm, crossAxisSpacing: AppSpacing.sm, childAspectRatio: 1.1),
        delegate: SliverChildBuilderDelegate(
          (context, index) {
            final school = vm.schools[index];
            final selected = vm.selectedSchool == school;
            return PressableScale(
              onTap: () { HapticService.selection(); vm.selectSchool(school); },
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 250),
                padding: const EdgeInsets.all(AppSpacing.sm + 2),
                decoration: BoxDecoration(
                  color: selected ? school.color.withValues(alpha: 0.15) : AppColors.surface,
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: selected ? school.color : AppColors.surfaceSecondary, width: selected ? 1.5 : 1),
                ),
                child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
                  Icon(school.icon, color: school.color, size: 24),
                  const SizedBox(height: AppSpacing.xs),
                  Flexible(child: Text(school.localizedName(locale),
                    style: AppFonts.caption.copyWith(color: selected ? school.color : AppColors.textSecondary,
                      fontWeight: selected ? FontWeight.w600 : FontWeight.normal),
                    textAlign: TextAlign.center, maxLines: 2, overflow: TextOverflow.ellipsis)),
                ]),
              ),
            );
          }, childCount: vm.schools.length),
      ),
    );
  }

  SliverToBoxAdapter _buildQuotesHeader(SchoolsViewModel vm, String locale) {
    return SliverToBoxAdapter(child: Padding(
      padding: const EdgeInsets.fromLTRB(AppSpacing.screenPadding, AppSpacing.lg, AppSpacing.screenPadding, AppSpacing.md),
      child: Text(vm.selectedSchool?.localizedName(locale) ?? '',
        style: AppFonts.title2.copyWith(color: vm.selectedSchool?.color ?? AppColors.textPrimary)),
    ));
  }

  SliverPadding _buildQuotesList(SchoolsViewModel vm, String locale) {
    return SliverPadding(
      padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
      sliver: SliverList(delegate: SliverChildBuilderDelegate(
        (context, index) {
          final q = vm.quotes[index];
          return Padding(padding: const EdgeInsets.only(bottom: AppSpacing.md),
            child: QuoteCard(quote: q, locale: locale, isFavorite: vm.isFavorite(q.id),
              onFavoriteTap: () => vm.toggleFavorite(q.id), showReflection: true));
        }, childCount: vm.quotes.length)),
    );
  }
}
