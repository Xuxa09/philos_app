import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';
import '../../core/extensions/context_extensions.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../common/widgets/app_button.dart';
import '../common/widgets/quote_card.dart';
import '../common/widgets/pressable_scale.dart';
import '../common/widgets/random_quote_sheet.dart';
import '../common/widgets/shimmer_widget.dart';
import 'home_view_model.dart';
import 'widgets/quote_of_day_card.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  void initState() {
    super.initState();
    Future.microtask(() => context.read<HomeViewModel>().loadData());
  }

  @override
  Widget build(BuildContext context) {
    final locale = Localizations.localeOf(context).languageCode;
    return Scaffold(
      backgroundColor: AppColors.background,
      body: Consumer<HomeViewModel>(
        builder: (context, vm, _) {
          if (vm.isLoading) return _buildShimmer();
          return _buildContent(context, vm, locale);
        },
      ),
    );
  }

  // === Content ===
  Widget _buildContent(BuildContext context, HomeViewModel vm, String locale) {
    final greeting = vm.getGreeting();
    String greetingText;
    switch (greeting) {
      case 'morning': greetingText = context.l10n.homeGoodMorning; break;
      case 'afternoon': greetingText = context.l10n.homeGoodAfternoon; break;
      default: greetingText = context.l10n.homeGoodEvening;
    }
    return SafeArea(
      child: CustomScrollView(
        slivers: [
          SliverToBoxAdapter(
            child: Padding(
              padding: const EdgeInsets.all(AppSpacing.screenPadding),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  _buildHeader(context, vm, greetingText),
                  const SizedBox(height: AppSpacing.lg),
                  if (vm.quoteOfDay != null)
                    QuoteOfDayCard(
                      quote: vm.quoteOfDay!, locale: locale,
                      isFavorite: vm.isFavorite(vm.quoteOfDay!.id),
                      onFavoriteTap: () => vm.toggleFavorite(vm.quoteOfDay!.id),
                    ),
                  const SizedBox(height: AppSpacing.lg),
                ],
              ),
            ),
          ),
          SliverToBoxAdapter(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  _buildFeatureCard(context, icon: Icons.mood, color: AppColors.primary,
                    label: locale == 'pt' ? 'Humor' : locale == 'es' ? 'Estado' : 'Moods',
                    onTap: () => context.push('/moods')),
                  _buildFeatureCard(context, icon: Icons.edit_note, color: AppColors.primary,
                    label: locale == 'pt' ? 'Di\u00E1rio' : locale == 'es' ? 'Diario' : 'Journal',
                    onTap: () => context.push('/journal')),
                  _buildFeatureCard(context, icon: Icons.auto_awesome, color: AppColors.primary,
                    label: locale == 'pt' ? 'Aleat\u00F3rio' : locale == 'es' ? 'Aleatorio' : 'Random',
                    onTap: () => _showRandomQuote(context)),
                ],
              ),
            ),
          ),
          const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.lg)),
          _buildQuotesList(vm, locale),
          if (vm.showingMore) _buildMoreQuotesList(vm, locale),
          if (!vm.showingMore)
            SliverToBoxAdapter(
              child: Padding(
                padding: const EdgeInsets.all(AppSpacing.screenPadding),
                child: AppButton(title: context.l10n.homeSeeMore, isOutlined: true, onTap: vm.loadMore),
              ),
            ),
          const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.xxl)),
        ],
      ),
    );
  }

  // === Subviews ===
  Widget _buildHeader(BuildContext context, HomeViewModel vm, String greetingText) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(children: [
          Text(greetingText, style: AppFonts.title2.copyWith(color: AppColors.textSecondary)),
          const Spacer(),
          GestureDetector(
            onTap: () => context.push('/settings'),
            child: const Icon(Icons.settings_outlined, color: AppColors.textSecondary, size: 28),
          ),
        ]),
        const SizedBox(height: 4),
        Text(context.l10n.homeTitle, style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)),
      ],
    );
  }

  Widget _buildQuotesList(HomeViewModel vm, String locale) {
    return SliverPadding(
      padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
      sliver: SliverList(delegate: SliverChildBuilderDelegate(
        (context, index) {
          final q = vm.dailyQuotes[index];
          return Padding(padding: const EdgeInsets.only(bottom: AppSpacing.md),
            child: QuoteCard(quote: q, locale: locale, isFavorite: vm.isFavorite(q.id),
              onFavoriteTap: () => vm.toggleFavorite(q.id), showReflection: true));
        }, childCount: vm.dailyQuotes.length)),
    );
  }

  Widget _buildMoreQuotesList(HomeViewModel vm, String locale) {
    return SliverPadding(
      padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
      sliver: SliverList(delegate: SliverChildBuilderDelegate(
        (context, index) {
          final q = vm.moreQuotes[index];
          return Padding(padding: const EdgeInsets.only(bottom: AppSpacing.md),
            child: QuoteCard(quote: q, locale: locale, isFavorite: vm.isFavorite(q.id),
              onFavoriteTap: () => vm.toggleFavorite(q.id), showReflection: true));
        }, childCount: vm.moreQuotes.length)),
    );
  }

  Widget _buildFeatureCard(BuildContext context, {required IconData icon, required Color color, required String label, required VoidCallback onTap}) {
    return PressableScale(onTap: onTap, child: Container(
      width: 110, padding: const EdgeInsets.all(AppSpacing.sm + 4),
      decoration: BoxDecoration(color: color.withValues(alpha: 0.1), borderRadius: BorderRadius.circular(14),
        border: Border.all(color: color.withValues(alpha: 0.3))),
      child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
        Icon(icon, color: color, size: 24),
        const SizedBox(height: AppSpacing.xs),
        Text(label, style: AppFonts.footnote.copyWith(color: color, fontWeight: FontWeight.w600)),
      ]),
    ));
  }

  void _showRandomQuote(BuildContext context) {
    showModalBottomSheet(context: context, backgroundColor: AppColors.surface,
      isScrollControlled: true,
      shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(20))),
      builder: (_) => SizedBox(height: MediaQuery.of(context).size.height * 0.80, child: const RandomQuoteSheet()));
  }

  // === Shimmer ===
  Widget _buildShimmer() {
    return SafeArea(child: SingleChildScrollView(
      padding: const EdgeInsets.all(AppSpacing.screenPadding),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const ShimmerWidget(width: 120, height: 16),
        const SizedBox(height: AppSpacing.sm),
        const ShimmerWidget(width: 200, height: 32),
        const SizedBox(height: AppSpacing.lg),
        ShimmerWidget(height: 160, borderRadius: 20),
        const SizedBox(height: AppSpacing.lg),
        const ShimmerWidget(width: 140, height: 24),
        const SizedBox(height: AppSpacing.md),
        ...List.generate(3, (_) => Padding(
          padding: const EdgeInsets.only(bottom: AppSpacing.md),
          child: ShimmerWidget(height: 120, borderRadius: 16))),
      ]),
    ));
  }
}
