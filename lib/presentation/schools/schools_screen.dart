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

class SchoolsScreen extends StatefulWidget {
  const SchoolsScreen({super.key});

  @override
  State<SchoolsScreen> createState() => _SchoolsScreenState();
}

class _SchoolsScreenState extends State<SchoolsScreen> {
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
        child: Consumer<SchoolsViewModel>(builder: (context, vm, _) {
        return SafeArea(child: CustomScrollView(keyboardDismissBehavior: ScrollViewKeyboardDismissBehavior.onDrag, slivers: [
          _buildHeader(context, locale),
          _buildSearchBar(vm, locale),
          const SliverToBoxAdapter(child: SizedBox(height: AppSpacing.md)),
          _buildSchoolsGrid(vm, locale),
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
        Text(locale == 'pt' ? 'Escolas Filos\u00f3ficas' : locale == 'es' ? 'Escuelas Filos\u00f3ficas' : 'Philosophical Schools',
          style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)),
      ]),
    ));
  }

  SliverToBoxAdapter _buildSearchBar(SchoolsViewModel vm, String locale) {
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

  SliverPadding _buildSchoolsGrid(SchoolsViewModel vm, String locale) {
    return SliverPadding(
      padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
      sliver: SliverGrid(
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 4, mainAxisSpacing: AppSpacing.sm, crossAxisSpacing: AppSpacing.sm, childAspectRatio: 1.3),
        delegate: SliverChildBuilderDelegate(
          (context, index) {
            final school = vm.schools[index];
            final selected = vm.selectedSchool == school;
            return PressableScale(
              onTap: () { HapticService.selection(); vm.selectSchool(school); },
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 250),
                padding: const EdgeInsets.all(AppSpacing.xs + 2),
                decoration: BoxDecoration(
                  color: selected ? school.color.withValues(alpha: 0.15) : AppColors.surface,
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: selected ? school.color : AppColors.surfaceSecondary, width: selected ? 1.5 : 1),
                ),
                child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
                  Icon(school.icon, color: school.color, size: 20),
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

  SliverPadding _buildQuotesList(SchoolsViewModel vm, String locale) {
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
