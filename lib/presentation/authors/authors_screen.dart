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

class AuthorsScreen extends StatelessWidget {
  const AuthorsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final locale = Localizations.localeOf(context).languageCode;
    return Scaffold(
      backgroundColor: AppColors.background,
      body: Consumer<AuthorsViewModel>(builder: (context, vm, _) {
        final authors = vm.getAuthors(locale);
        return SafeArea(child: CustomScrollView(slivers: [
          _buildHeader(context, locale),
          _buildAuthorsRow(vm, authors),
          const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.md)),
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
        Text(locale == 'pt' ? 'Filósofos' : locale == 'es' ? 'Filósofos' : 'Philosophers',
          style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)),
        const SizedBox(height: AppSpacing.xs),
        Text(locale == 'pt' ? 'Escolha um filósofo' : locale == 'es' ? 'Elige un filósofo' : 'Choose a philosopher',
          style: AppFonts.body.copyWith(color: AppColors.textSecondary)),
      ]),
    ));
  }

  SliverToBoxAdapter _buildAuthorsRow(AuthorsViewModel vm, List<AuthorInfo> authors) {
    return SliverToBoxAdapter(child: SizedBox(
      height: 40,
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

  SliverToBoxAdapter _buildQuotesHeader(AuthorsViewModel vm, String locale) {
    final authors = vm.getAuthors(locale);
    final current = authors.where((a) => a.key == vm.selectedAuthor).firstOrNull;
    return SliverToBoxAdapter(child: Padding(
      padding: const EdgeInsets.fromLTRB(AppSpacing.screenPadding, AppSpacing.sm, AppSpacing.screenPadding, AppSpacing.md),
      child: Text(current?.name ?? '',
        style: AppFonts.title2.copyWith(color: current?.color ?? AppColors.textPrimary)),
    ));
  }

  SliverPadding _buildQuotesList(AuthorsViewModel vm, String locale) {
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
