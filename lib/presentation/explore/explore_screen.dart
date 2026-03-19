import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../core/extensions/context_extensions.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../common/widgets/empty_state_widget.dart';
import '../common/widgets/quote_card.dart';
import '../common/widgets/shimmer_widget.dart';
import 'explore_view_model.dart';
import 'widgets/category_chip.dart';

class ExploreScreen extends StatefulWidget {
  const ExploreScreen({super.key});
  @override
  State<ExploreScreen> createState() => _ExploreScreenState();
}

class _ExploreScreenState extends State<ExploreScreen> {
  @override
  void initState() {
    super.initState();
    Future.microtask(() => context.read<ExploreViewModel>().loadData());
  }

  @override
  Widget build(BuildContext context) {
    final locale = Localizations.localeOf(context).languageCode;
    return Scaffold(
      backgroundColor: AppColors.background,
      body: Consumer<ExploreViewModel>(
        builder: (context, vm, _) {
          if (vm.isLoading) return _buildShimmer();
          return _buildContent(context, vm, locale);
        },
      ),
    );
  }

  Widget _buildContent(BuildContext context, ExploreViewModel vm, String locale) {
    return SafeArea(
      child: CustomScrollView(slivers: [
        SliverToBoxAdapter(child: Padding(
          padding: const EdgeInsets.all(AppSpacing.screenPadding),
          child: Text(context.l10n.exploreTitle, style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)),
        )),
        SliverToBoxAdapter(child: SizedBox(height: 44, child: ListView.separated(
          scrollDirection: Axis.horizontal,
          padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
          itemCount: vm.categories.length,
          separatorBuilder: (_, __) => const SizedBox(width: AppSpacing.sm),
          itemBuilder: (context, index) {
            final cat = vm.categories[index];
            return CategoryChip(category: cat, locale: locale, isSelected: vm.selectedCategory == cat, onTap: () => vm.selectCategory(cat));
          },
        ))),
        const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.md)),
        if (vm.quotes.isEmpty)
          SliverFillRemaining(child: EmptyStateWidget(icon: Icons.search_off,
            title: locale == 'pt' ? 'Nenhuma frase encontrada' : locale == 'es' ? 'No se encontraron frases' : 'No quotes found'))
        else
          SliverPadding(
            padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
            sliver: SliverList(delegate: SliverChildBuilderDelegate(
              (context, index) {
                final q = vm.quotes[index];
                return Padding(padding: const EdgeInsets.only(bottom: AppSpacing.md),
                  child: QuoteCard(quote: q, locale: locale, isFavorite: vm.isFavorite(q.id),
                    onFavoriteTap: () => vm.toggleFavorite(q.id), showReflection: true));
              }, childCount: vm.quotes.length))),
        const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.xxl)),
      ]),
    );
  }

  Widget _buildShimmer() {
    return SafeArea(child: Padding(
      padding: const EdgeInsets.all(AppSpacing.screenPadding),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const ShimmerWidget(width: 140, height: 32),
        const SizedBox(height: AppSpacing.md),
        SingleChildScrollView(scrollDirection: Axis.horizontal, child: Row(
          children: List.generate(4, (_) => Padding(
            padding: const EdgeInsets.only(right: AppSpacing.sm),
            child: ShimmerWidget(width: 80, height: 36, borderRadius: 20))))),
        const SizedBox(height: AppSpacing.lg),
        Expanded(child: ListView(padding: EdgeInsets.zero,
          children: List.generate(4, (_) => Padding(
            padding: const EdgeInsets.only(bottom: AppSpacing.md),
            child: ShimmerWidget(height: 120, borderRadius: 16))))),
      ]),
    ));
  }
}
