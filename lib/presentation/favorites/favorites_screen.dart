import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../core/extensions/context_extensions.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../common/widgets/empty_state_widget.dart';
import '../common/widgets/quote_card.dart';
import '../common/widgets/shimmer_widget.dart';
import 'favorites_view_model.dart';

class FavoritesScreen extends StatefulWidget {
  const FavoritesScreen({super.key});
  @override
  State<FavoritesScreen> createState() => _FavoritesScreenState();
}

class _FavoritesScreenState extends State<FavoritesScreen> {
  @override
  void initState() {
    super.initState();
    Future.microtask(() => context.read<FavoritesViewModel>().loadFavorites());
  }

  @override
  Widget build(BuildContext context) {
    final locale = Localizations.localeOf(context).languageCode;
    return Scaffold(
      backgroundColor: AppColors.background,
      body: Consumer<FavoritesViewModel>(builder: (context, vm, _) {
        if (vm.isLoading) return _buildShimmer();
        if (vm.isEmpty) return _buildEmpty(context);
        return _buildContent(vm, locale);
      }),
    );
  }

  Widget _buildContent(FavoritesViewModel vm, String locale) {
    return SafeArea(child: CustomScrollView(slivers: [
      SliverToBoxAdapter(child: Padding(
        padding: const EdgeInsets.all(AppSpacing.screenPadding),
        child: Text(context.l10n.favoritesTitle, style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)),
      )),
      SliverPadding(
        padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
        sliver: SliverList(delegate: SliverChildBuilderDelegate(
          (context, index) {
            final q = vm.favorites[index];
            return Padding(padding: const EdgeInsets.only(bottom: AppSpacing.md),
              child: QuoteCard(quote: q, locale: locale, isFavorite: true,
                onFavoriteTap: () => vm.toggleFavorite(q.id), showReflection: true));
          }, childCount: vm.favorites.length))),
      const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.xxl)),
    ]));
  }

  Widget _buildEmpty(BuildContext context) {
    return SafeArea(child: Column(children: [
      Padding(padding: const EdgeInsets.all(AppSpacing.screenPadding),
        child: Align(alignment: Alignment.centerLeft,
          child: Text(context.l10n.favoritesTitle, style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)))),
      Expanded(child: EmptyStateWidget(icon: Icons.favorite_border,
        title: context.l10n.favoritesEmpty, description: context.l10n.favoritesEmptyDesc)),
    ]));
  }

  Widget _buildShimmer() {
    return SafeArea(child: Padding(
      padding: const EdgeInsets.all(AppSpacing.screenPadding),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const ShimmerWidget(width: 140, height: 32),
        const SizedBox(height: AppSpacing.lg),
        ...List.generate(3, (_) => Padding(
          padding: const EdgeInsets.only(bottom: AppSpacing.md),
          child: ShimmerWidget(height: 120, borderRadius: 16))),
      ]),
    ));
  }
}
