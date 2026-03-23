import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';
import '../../core/extensions/context_extensions.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../../core/utils/haptic_service.dart';
import '../common/widgets/pressable_scale.dart';
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
            if (vm.isSearching) return _buildSearchResults(vm, locale);
            return _buildHub(context, vm, locale);
          },
        ),
      ),
    );
  }

  // === Hub (default view) ===
  Widget _buildHub(BuildContext context, ExploreViewModel vm, String locale) {
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
        const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.lg)),

        // Category buttons grid
        SliverToBoxAdapter(child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
          child: _buildCategoryGrid(context, locale),
        )),
        const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.lg)),

        // Popular section
        SliverToBoxAdapter(child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
          child: Text(
            locale == 'pt' ? 'Mais populares' : locale == 'es' ? 'Más populares' : 'Most popular',
            style: AppFonts.title2.copyWith(color: AppColors.textPrimary),
          ),
        )),
        const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.md)),
        SliverPadding(
          padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
          sliver: SliverList(delegate: SliverChildBuilderDelegate(
            (context, index) {
              final q = vm.popularQuotes[index];
              return Padding(padding: const EdgeInsets.only(bottom: AppSpacing.md),
                child: QuoteCard(quote: q, locale: locale, isFavorite: vm.isFavorite(q.id),
                  onFavoriteTap: () => vm.toggleFavorite(q.id)));
            }, childCount: vm.popularQuotes.length))),
        const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.xxl)),
      ]),
    );
  }

  Widget _buildCategoryGrid(BuildContext context, String locale) {
    final items = [
      _CategoryItem(
        icon: Icons.edit_note,
        label: locale == 'pt' ? 'Suas frases' : locale == 'es' ? 'Tus frases' : 'Your quotes',
        color: AppColors.primary,
        route: '/journal',
      ),
      _CategoryItem(
        icon: Icons.emoji_emotions_outlined,
        label: locale == 'pt' ? 'Por sentimento' : locale == 'es' ? 'Por sentimiento' : 'By mood',
        color: AppColors.primary,
        route: '/moods',
      ),
      _CategoryItem(
        icon: Icons.account_balance_outlined,
        label: locale == 'pt' ? 'Por escola' : locale == 'es' ? 'Por escuela' : 'By school',
        color: AppColors.primary,
        route: '/schools',
      ),
      _CategoryItem(
        icon: Icons.person_outline,
        label: locale == 'pt' ? 'Por autor' : locale == 'es' ? 'Por autor' : 'By author',
        color: AppColors.primary,
        route: '/authors',
      ),
    ];

    return GridView.count(
      crossAxisCount: 2,
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      mainAxisSpacing: AppSpacing.sm,
      crossAxisSpacing: AppSpacing.sm,
      childAspectRatio: 1.8,
      children: items.map((item) => _buildCategoryCard(context, item)).toList(),
    );
  }

  Widget _buildCategoryCard(BuildContext context, _CategoryItem item) {
    return PressableScale(
      onTap: () {
        HapticService.light();
        context.push(item.route);
      },
      child: Container(
        padding: const EdgeInsets.all(AppSpacing.md),
        decoration: BoxDecoration(
          color: item.color.withValues(alpha: 0.12),
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: item.color.withValues(alpha: 0.25), width: 1),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Icon(item.icon, color: item.color, size: 24),
            Text(item.label,
              style: AppFonts.subheadline.copyWith(color: AppColors.textPrimary, fontWeight: FontWeight.w600),
              maxLines: 1, overflow: TextOverflow.ellipsis),
          ],
        ),
      ),
    );
  }

  // === Search results view ===
  Widget _buildSearchResults(ExploreViewModel vm, String locale) {
    return SafeArea(
      child: CustomScrollView(slivers: [
        SliverToBoxAdapter(child: Padding(
          padding: const EdgeInsets.fromLTRB(AppSpacing.screenPadding, AppSpacing.screenPadding, AppSpacing.screenPadding, AppSpacing.sm),
          child: _buildSearchBar(vm, locale),
        )),
        const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.md)),
        if (vm.filteredQuotes.isEmpty)
          SliverToBoxAdapter(child: Padding(
            padding: const EdgeInsets.only(top: 80),
            child: Center(child: Column(children: [
              Icon(Icons.search_off, size: 48, color: AppColors.textTertiary),
              const SizedBox(height: AppSpacing.md),
              Text(
                locale == 'pt' ? 'Nenhuma frase encontrada' : locale == 'es' ? 'No se encontraron frases' : 'No quotes found',
                style: AppFonts.body.copyWith(color: AppColors.textTertiary),
              ),
            ])),
          ))
        else
          SliverPadding(
            padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
            sliver: SliverList(delegate: SliverChildBuilderDelegate(
              (context, index) {
                final q = vm.filteredQuotes[index];
                return Padding(padding: const EdgeInsets.only(bottom: AppSpacing.md),
                  child: QuoteCard(quote: q, locale: locale, isFavorite: vm.isFavorite(q.id),
                    onFavoriteTap: () => vm.toggleFavorite(q.id), showReflection: true));
              }, childCount: vm.filteredQuotes.length))),
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
            ? 'Pesquisar tópicos...'
            : locale == 'es'
                ? 'Buscar temas...'
                : 'Search topics...',
        hintStyle: AppFonts.body.copyWith(color: AppColors.textTertiary),
        prefixIcon: const Icon(Icons.search, color: AppColors.textTertiary, size: 22),
        suffixIcon: _searchController.text.isNotEmpty
            ? GestureDetector(
                onTap: () {
                  _searchController.clear();
                  vm.setSearchQuery('', locale);
                  _searchFocus.unfocus();
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
        Row(children: [
          Expanded(child: ShimmerWidget(height: 80, borderRadius: 16)),
          const SizedBox(width: AppSpacing.sm),
          Expanded(child: ShimmerWidget(height: 80, borderRadius: 16)),
        ]),
        const SizedBox(height: AppSpacing.sm),
        Row(children: [
          Expanded(child: ShimmerWidget(height: 80, borderRadius: 16)),
          const SizedBox(width: AppSpacing.sm),
          Expanded(child: ShimmerWidget(height: 80, borderRadius: 16)),
        ]),
        const SizedBox(height: AppSpacing.lg),
        const ShimmerWidget(width: 120, height: 24),
        const SizedBox(height: AppSpacing.md),
        Expanded(child: ListView(padding: EdgeInsets.zero,
          children: List.generate(3, (_) => Padding(
            padding: const EdgeInsets.only(bottom: AppSpacing.md),
            child: ShimmerWidget(height: 100, borderRadius: 16))))),
      ]),
    ));
  }
}

class _CategoryItem {
  final IconData icon;
  final String label;
  final Color color;
  final String route;

  const _CategoryItem({required this.icon, required this.label, required this.color, required this.route});
}
