import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../../core/utils/haptic_service.dart';
import '../common/widgets/pressable_scale.dart';
import '../common/widgets/quote_card.dart';
import 'authors_view_model.dart';

class AuthorsScreen extends StatefulWidget {
  const AuthorsScreen({super.key});

  @override
  State<AuthorsScreen> createState() => _AuthorsScreenState();
}

class _AuthorsScreenState extends State<AuthorsScreen> {
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
        child: Consumer<AuthorsViewModel>(builder: (context, vm, _) {
        final authors = vm.getAuthors(locale);
        return SafeArea(child: CustomScrollView(keyboardDismissBehavior: ScrollViewKeyboardDismissBehavior.onDrag, slivers: [
          _buildHeader(context, locale),
          _buildSearchBar(vm, locale),
          const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.md)),
          _buildAuthorsRow(vm, authors),
          const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.lg)),
          if (vm.selectedAuthor == null)
            SliverToBoxAdapter(child: Padding(
              padding: const EdgeInsets.only(top: 60),
              child: Center(child: Column(children: [
                const Icon(Icons.touch_app_outlined, size: 40, color: AppColors.textTertiary),
                const SizedBox(height: AppSpacing.md),
                Text(
                  locale == 'pt' ? 'Selecione um fil\u00f3sofo acima' : locale == 'es' ? 'Selecciona un fil\u00f3sofo arriba' : 'Select a philosopher above',
                  style: AppFonts.body.copyWith(color: AppColors.textTertiary),
                ),
              ])),
            ))
          else if (vm.quotes.isNotEmpty)
            _buildQuotesList(vm, locale)
          else if (_searchController.text.isNotEmpty)
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
        Text(locale == 'pt' ? 'Fil\u00f3sofos' : locale == 'es' ? 'Fil\u00f3sofos' : 'Philosophers',
          style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)),
      ]),
    ));
  }

  SliverToBoxAdapter _buildSearchBar(AuthorsViewModel vm, String locale) {
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

  SliverToBoxAdapter _buildAuthorsRow(AuthorsViewModel vm, List<AuthorInfo> authors) {
    return SliverToBoxAdapter(child: SizedBox(
      height: 44,
      child: ListView.separated(
        scrollDirection: Axis.horizontal,
        padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
        itemCount: authors.length,
        separatorBuilder: (_, __) => const SizedBox(width: AppSpacing.sm),
        itemBuilder: (context, index) {
          final author = authors[index];
          final selected = vm.selectedAuthor == author.key;
          return PressableScale(
            onTap: () { HapticService.selection(); vm.selectAuthor(author.key); },
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 250),
              padding: const EdgeInsets.symmetric(horizontal: AppSpacing.md, vertical: AppSpacing.sm),
              decoration: BoxDecoration(
                color: selected ? author.color.withValues(alpha: 0.15) : AppColors.surface,
                borderRadius: BorderRadius.circular(20),
                border: Border.all(color: selected ? author.color : AppColors.surfaceSecondary, width: selected ? 1.5 : 1),
              ),
              child: Text(author.name,
                style: AppFonts.footnote.copyWith(
                  color: selected ? author.color : AppColors.textSecondary,
                  fontWeight: selected ? FontWeight.w600 : FontWeight.normal,
                )),
            ),
          );
        },
      ),
    ));
  }

  SliverPadding _buildQuotesList(AuthorsViewModel vm, String locale) {
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
