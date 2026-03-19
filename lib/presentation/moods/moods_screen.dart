import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../common/widgets/quote_card.dart';
import 'moods_view_model.dart';
import 'widgets/mood_card.dart';

class MoodsScreen extends StatelessWidget {
  const MoodsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final locale = Localizations.localeOf(context).languageCode;
    return Scaffold(
      backgroundColor: AppColors.background,
      body: Consumer<MoodsViewModel>(builder: (context, vm, _) {
        return SafeArea(child: CustomScrollView(slivers: [
          _buildHeader(context, locale),
          _buildMoodsGrid(vm, locale),
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
        Text(locale == 'pt' ? 'Como voc\u00EA est\u00E1?' : locale == 'es' ? '\u00BFC\u00F3mo te sientes?' : 'How are you feeling?',
          style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)),
        const SizedBox(height: AppSpacing.xs),
        Text(locale == 'pt' ? 'Escolha seu estado de esp\u00EDrito' : locale == 'es' ? 'Elige tu estado de \u00E1nimo' : 'Choose your mood',
          style: AppFonts.body.copyWith(color: AppColors.textSecondary)),
      ]),
    ));
  }

  SliverPadding _buildMoodsGrid(MoodsViewModel vm, String locale) {
    return SliverPadding(
      padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
      sliver: SliverGrid(
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 3, mainAxisSpacing: AppSpacing.sm, crossAxisSpacing: AppSpacing.sm, childAspectRatio: 1.1),
        delegate: SliverChildBuilderDelegate(
          (context, index) {
            final mood = vm.moods[index];
            return MoodCard(mood: mood, locale: locale, isSelected: vm.selectedMood == mood, onTap: () => vm.selectMood(mood));
          }, childCount: vm.moods.length),
      ),
    );
  }

  SliverToBoxAdapter _buildQuotesHeader(MoodsViewModel vm, String locale) {
    return SliverToBoxAdapter(child: Padding(
      padding: const EdgeInsets.fromLTRB(AppSpacing.screenPadding, AppSpacing.lg, AppSpacing.screenPadding, AppSpacing.md),
      child: Text(vm.selectedMood?.localizedName(locale) ?? '',
        style: AppFonts.title2.copyWith(color: vm.selectedMood?.color ?? AppColors.textPrimary)),
    ));
  }

  SliverPadding _buildQuotesList(MoodsViewModel vm, String locale) {
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
