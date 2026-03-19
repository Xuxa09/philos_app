import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../common/widgets/empty_state_widget.dart';
import '../common/widgets/shimmer_widget.dart';
import 'journal_view_model.dart';
import 'widgets/journal_sheets.dart';
import 'widgets/note_card.dart';

class JournalScreen extends StatefulWidget {
  const JournalScreen({super.key});
  @override
  State<JournalScreen> createState() => _JournalScreenState();
}

class _JournalScreenState extends State<JournalScreen> {
  @override
  void initState() {
    super.initState();
    Future.microtask(() { if (!mounted) return; context.read<JournalViewModel>().loadNotes(); });
  }

  @override
  Widget build(BuildContext context) {
    final locale = Localizations.localeOf(context).languageCode;
    return Scaffold(
      backgroundColor: AppColors.background,
      floatingActionButton: FloatingActionButton(
        onPressed: () => showAddOptions(context, locale),
        backgroundColor: AppColors.accent,
        child: const Icon(Icons.add, color: Colors.white),
      ),
      body: Consumer<JournalViewModel>(builder: (context, vm, _) {
        if (vm.isLoading) return _buildShimmer();
        if (vm.isEmpty) return _buildEmpty(context, locale);
        return _buildContent(context, vm, locale);
      }),
    );
  }

  Widget _buildContent(BuildContext context, JournalViewModel vm, String locale) {
    return SafeArea(child: CustomScrollView(slivers: [
      SliverToBoxAdapter(child: Padding(
        padding: const EdgeInsets.all(AppSpacing.screenPadding),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          GestureDetector(onTap: () => context.pop(),
            child: Container(width: 44, height: 44, alignment: Alignment.centerLeft, color: Colors.transparent,
              child: const Icon(Icons.arrow_back_ios, color: AppColors.textPrimary, size: 20))),
          const SizedBox(height: AppSpacing.sm),
          Text(_screenTitle(locale), style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)),
        ]),
      )),
      SliverPadding(
        padding: const EdgeInsets.symmetric(horizontal: AppSpacing.screenPadding),
        sliver: SliverList(delegate: SliverChildBuilderDelegate(
          (context, index) {
            final note = vm.notes[index];
            return Padding(padding: const EdgeInsets.only(bottom: AppSpacing.md),
              child: NoteCard(note: note, locale: locale,
                onEdit: () => showEditSheet(context, vm, note, locale),
                onDelete: () => showDeleteConfirmation(context, locale, () => vm.deleteNote(note.id))));
          }, childCount: vm.notes.length))),
      const SliverToBoxAdapter(child: SizedBox(height: 100)),
    ]));
  }

  Widget _buildEmpty(BuildContext context, String locale) {
    return SafeArea(child: Column(children: [
      Padding(padding: const EdgeInsets.all(AppSpacing.screenPadding),
        child: Align(alignment: Alignment.centerLeft, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          GestureDetector(onTap: () => context.pop(),
            child: Container(width: 44, height: 44, alignment: Alignment.centerLeft, color: Colors.transparent,
              child: const Icon(Icons.arrow_back_ios, color: AppColors.textPrimary, size: 20))),
          const SizedBox(height: AppSpacing.sm),
          Text(_screenTitle(locale), style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)),
        ]))),
      Expanded(child: EmptyStateWidget(icon: Icons.edit_note,
        title: locale == 'pt' ? 'Seu di\u00E1rio est\u00E1 vazio' : locale == 'es' ? 'Tu diario est\u00E1 vac\u00EDo' : 'Your journal is empty',
        description: locale == 'pt' ? 'Escreva suas reflex\u00F5es e anota\u00E7\u00F5es' : locale == 'es' ? 'Escribe tus reflexiones y notas' : 'Write your reflections and notes')),
    ]));
  }

  Widget _buildShimmer() {
    return SafeArea(child: Padding(padding: const EdgeInsets.all(AppSpacing.screenPadding),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const ShimmerWidget(width: 24, height: 24),
        const SizedBox(height: AppSpacing.md),
        const ShimmerWidget(width: 200, height: 32),
        const SizedBox(height: AppSpacing.lg),
        ...List.generate(3, (_) => Padding(
          padding: const EdgeInsets.only(bottom: AppSpacing.md),
          child: ShimmerWidget(height: 100, borderRadius: 16))),
      ])));
  }

  String _screenTitle(String locale) {
    if (locale == 'pt') return 'Di\u00E1rio';
    if (locale == 'es') return 'Diario';
    return 'Journal';
  }
}
