import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../common/widgets/quote_card.dart';
import 'moods_view_model.dart';
import 'widgets/mood_card.dart';

class MoodsScreen extends StatefulWidget {
  const MoodsScreen({super.key});

  @override
  State<MoodsScreen> createState() => _MoodsScreenState();
}

class _MoodsScreenState extends State<MoodsScreen> {
  final _searchController = TextEditingController();

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final locale = Localizations.localeOf(context).languageCode;
    return Scaffold(
      backgroundColor: AppColors.background,
      body: GestureDetector(
        onTap: () => FocusManager.instance.primaryFocus?.unfocus(),
        child: Consumer<MoodsViewModel>(builder: (context, vm, _) {
        return SafeArea(child: CustomScrollView(keyboardDismissBehavior: ScrollViewKeyboardDismissBehavior.onDrag, slivers: [
          _buildHeader(context, locale),
          _buildSearchBar(vm, locale),
          const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.md)),
          _buildMoodsGrid(vm, locale),
          const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.lg)),
          if (vm.quotes.isNotEmpty)
            _buildQuotesList(vm, locale),
          if (vm.quotes.isEmpty && _searchController.text.isNotEmpty)
            _buildEmptySearch(locale),
          const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.xxl)),
        ]));
      })),
    );
  }

  SliverToBoxAdapter _buildHeader(BuildContext context, String locale) {
    return SliverToBoxAdapter(child: Padding(
      padding: const EdgeInsets.all(AppSpacing.screenPadding),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        GestureDetector(onTap: () => context.pop(),
          child: const Icon(Icons.arrow_back_ios, color: AppColors.textPrimary, size: 20)),
        const SizedBox(height: AppSpacing.md),
        Text(locale == 'pt' ? 'Como voc\u00ea est\u00e1?' : locale == 'es' ? '\u00bfC\u00f3mo te sientes?' : 'How are you feeling?',
          style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)),
      ]),
    ));
  }

  SliverToBoxAdapter _buildSearchBar(MoodsViewModel vm, String locale) {
    return SliverToBoxAdapter(child: Padding(
      padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
      child: TextField(
        controller: _searchController,
        onChanged: (value) { setState(() {}); vm.search(value); },
        style: AppFonts.body.copyWith(color: AppColors.textPrimary),
        cursorColor: AppColors.primary,
        decoration: InputDecoration(
          hintText: locale == 'pt' ? 'Pesquisar frases...' : locale == 'es' ? 'Buscar frases...' : 'Search quotes...',
          hintStyle: AppFonts.body.copyWith(color: AppColors.textTertiary),
          prefixIcon: const Icon(Icons.search, color: AppColors.textTertiary, size: 22),
          suffixIcon: _searchController.text.isNotEmpty
              ? GestureDetector(
                  onTap: () { _searchController.clear(); setState(() {}); vm.search(''); },
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
      ),
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

  SliverPadding _buildQuotesList(MoodsViewModel vm, String locale) {
    return SliverPadding(
      padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
      sliver: SliverList(delegate: SliverChildBuilderDelegate(
        (context, index) {
          final q = vm.quotes[index];
          return Padding(key: ValueKey(q.id), padding: const EdgeInsets.only(bottom: AppSpacing.md),
            child: QuoteCard(quote: q, locale: locale, isFavorite: vm.isFavorite(q.id),
              onFavoriteTap: () => vm.toggleFavorite(q.id), showReflection: true));
        }, childCount: vm.quotes.length)),
    );
  }

  SliverToBoxAdapter _buildEmptySearch(String locale) {
    return SliverToBoxAdapter(child: Padding(
      padding: const EdgeInsets.only(top: 40),
      child: Center(child: Text(
        locale == 'pt' ? 'Nenhuma frase encontrada' : locale == 'es' ? 'Ninguna frase encontrada' : 'No quotes found',
        style: AppFonts.body.copyWith(color: AppColors.textTertiary),
      )),
    ));
  }
}
