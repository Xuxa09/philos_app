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

class ExploreScreen extends StatefulWidget {
  const ExploreScreen({super.key});
  @override
  State<ExploreScreen> createState() => _ExploreScreenState();
}

class _ExploreScreenState extends State<ExploreScreen> {
  final _searchController = TextEditingController();
  final _searchFocus = FocusNode();

  @override
  void initState() {
    super.initState();
    Future.microtask(() => context.read<ExploreViewModel>().loadData());
  }

  @override
  void dispose() {
    _searchController.dispose();
    _searchFocus.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final locale = Localizations.localeOf(context).languageCode;
    return Scaffold(
      backgroundColor: AppColors.background,
      body: GestureDetector(
        onTap: () => _searchFocus.unfocus(),
        child: Consumer<ExploreViewModel>(
          builder: (context, vm, _) {
            if (vm.isLoading) return _buildShimmer();
            return _buildContent(context, vm, locale);
          },
        ),
      ),
    );
  }

  Widget _buildContent(BuildContext context, ExploreViewModel vm, String locale) {
    return SafeArea(
      child: CustomScrollView(slivers: [
        // Title
        SliverToBoxAdapter(child: Padding(
          padding: const EdgeInsets.fromLTRB(AppSpacing.screenPadding, AppSpacing.screenPadding, AppSpacing.screenPadding, AppSpacing.sm),
          child: Text(context.l10n.exploreTitle, style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)),
        )),

        // Search bar
        SliverToBoxAdapter(child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
          child: _buildSearchBar(vm, locale),
        )),
        const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.md)),

        // Quotes list
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

  Widget _buildSearchBar(ExploreViewModel vm, String locale) {
    return TextField(
      controller: _searchController,
      focusNode: _searchFocus,
      onChanged: (value) => vm.setSearchQuery(value, locale),
      style: AppFonts.body.copyWith(color: AppColors.textPrimary),
      cursorColor: AppColors.primary,
      decoration: InputDecoration(
        hintText: locale == 'pt'
            ? 'Buscar frases ou filósofos...'
            : locale == 'es'
                ? 'Buscar frases o filósofos...'
                : 'Search quotes or philosophers...',
        hintStyle: AppFonts.body.copyWith(color: AppColors.textTertiary),
        prefixIcon: const Icon(Icons.search, color: AppColors.textTertiary, size: 22),
        suffixIcon: _searchController.text.isNotEmpty
            ? GestureDetector(
                onTap: () {
                  _searchController.clear();
                  vm.setSearchQuery('', locale);
                },
                child: const Icon(Icons.close, color: AppColors.textTertiary, size: 20),
              )
            : null,
        filled: true,
        fillColor: AppColors.surface,
        contentPadding: const EdgeInsets.symmetric(horizontal: AppSpacing.md, vertical: AppSpacing.sm + 2),
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(14), borderSide: BorderSide(color: AppColors.surfaceSecondary)),
        enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(14), borderSide: BorderSide(color: AppColors.surfaceSecondary)),
        focusedBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(14), borderSide: BorderSide(color: AppColors.primary, width: 1.5)),
      ),
    );
  }

  Widget _buildShimmer() {
    return SafeArea(child: Padding(
      padding: const EdgeInsets.all(AppSpacing.screenPadding),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const ShimmerWidget(width: 140, height: 32),
        const SizedBox(height: AppSpacing.md),
        const ShimmerWidget(height: 44, borderRadius: 14),
        const SizedBox(height: AppSpacing.lg),
        Expanded(child: ListView(padding: EdgeInsets.zero,
          children: List.generate(4, (_) => Padding(
            padding: const EdgeInsets.only(bottom: AppSpacing.md),
            child: ShimmerWidget(height: 120, borderRadius: 16))))),
      ]),
    ));
  }
}
