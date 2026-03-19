import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';
import '../../../core/utils/haptic_service.dart';
import '../../../data/models/quote_model.dart';
import '../../common/widgets/app_button.dart';
import '../journal_view_model.dart';

class ReflectionSheet extends StatefulWidget {
  final String locale;
  const ReflectionSheet({super.key, required this.locale});
  @override
  State<ReflectionSheet> createState() => _ReflectionSheetState();
}

class _ReflectionSheetState extends State<ReflectionSheet> {
  QuoteModel? _selectedQuote;
  final _textController = TextEditingController();
  final _searchController = TextEditingController();
  List<QuoteModel> _filteredQuotes = [];
  bool _isSearching = false;

  @override
  void dispose() { _textController.dispose(); _searchController.dispose(); super.dispose(); }

  void _filterQuotes(String query, List<QuoteModel> allQuotes) {
    if (query.trim().isEmpty) { setState(() { _filteredQuotes = []; _isSearching = false; }); return; }
    final lower = query.toLowerCase();
    setState(() { _isSearching = true;
      _filteredQuotes = allQuotes.where((q) {
        final author = q.author(widget.locale).toLowerCase();
        final text = q.text(widget.locale).toLowerCase();
        final category = q.category.toLowerCase();
        return author.contains(lower) || text.contains(lower) || category.contains(lower);
      }).toList();
    });
  }

  @override
  Widget build(BuildContext context) {
    final vm = context.read<JournalViewModel>();
    final locale = widget.locale;
    return GestureDetector(onTap: () => Navigator.pop(context), behavior: HitTestBehavior.opaque,
      child: DraggableScrollableSheet(initialChildSize: 0.85, minChildSize: 0.5, maxChildSize: 0.95,
        builder: (context, scrollController) => GestureDetector(onTap: () {},
          child: Container(
            decoration: const BoxDecoration(color: AppColors.background, borderRadius: BorderRadius.vertical(top: Radius.circular(20))),
            child: Column(children: [
              Padding(padding: const EdgeInsets.only(top: AppSpacing.sm),
                child: Container(width: 40, height: 4, decoration: BoxDecoration(color: AppColors.textTertiary, borderRadius: BorderRadius.circular(2)))),
              Padding(padding: const EdgeInsets.all(AppSpacing.screenPadding), child: Row(children: [
                Expanded(child: Text(locale == 'pt' ? 'Nova Reflex\u00E3o' : locale == 'es' ? 'Nueva Reflexi\u00F3n' : 'New Reflection',
                  style: AppFonts.title.copyWith(color: AppColors.textPrimary))),
                IconButton(onPressed: () => Navigator.pop(context), icon: const Icon(Icons.close, color: AppColors.textPrimary)),
              ])),
              Expanded(child: SingleChildScrollView(controller: scrollController,
                padding: EdgeInsets.only(left: AppSpacing.screenPadding, right: AppSpacing.screenPadding,
                  bottom: MediaQuery.of(context).viewInsets.bottom + AppSpacing.xxl),
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  if (_selectedQuote == null) ...[
                    Text(locale == 'pt' ? 'Escolha uma frase' : locale == 'es' ? 'Elige una frase' : 'Choose a quote',
                      style: AppFonts.headline.copyWith(color: AppColors.textPrimary)),
                    const SizedBox(height: AppSpacing.md),
                    _buildRandomButton(vm, locale),
                    const SizedBox(height: AppSpacing.md),
                    _buildSearchField(vm, locale),
                    const SizedBox(height: AppSpacing.md),
                    if (_isSearching) _buildSearchResults(locale) else _buildSuggestions(vm, locale),
                  ],
                  if (_selectedQuote != null) ...[
                    _buildSelectedQuote(locale),
                    const SizedBox(height: AppSpacing.lg),
                    Text(locale == 'pt' ? 'Sua reflex\u00E3o' : locale == 'es' ? 'Tu reflexi\u00F3n' : 'Your reflection',
                      style: AppFonts.headline.copyWith(color: AppColors.textPrimary)),
                    const SizedBox(height: AppSpacing.md),
                    TextField(controller: _textController, maxLines: 5,
                      style: AppFonts.body.copyWith(color: AppColors.textPrimary),
                      decoration: InputDecoration(
                        hintText: locale == 'pt' ? 'O que essa frase significa para voc\u00EA?' : locale == 'es' ? '\u00BFQu\u00E9 significa esta frase para ti?' : 'What does this quote mean to you?',
                        hintStyle: AppFonts.body.copyWith(color: AppColors.textTertiary),
                        filled: true, fillColor: AppColors.surface,
                        border: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: BorderSide.none))),
                    const SizedBox(height: AppSpacing.lg),
                    AppButton(color: AppColors.accent,
                      title: locale == 'pt' ? 'Salvar Reflex\u00E3o' : locale == 'es' ? 'Guardar Reflexi\u00F3n' : 'Save Reflection',
                      onTap: () {
                        final text = _textController.text.trim();
                        if (text.isEmpty) return;
                        HapticService.success();
                        final q = _selectedQuote!;
                        vm.addReflection(text: text, quoteAuthor: q.author(locale), quoteText: q.text(locale));
                        Navigator.pop(context);
                      }),
                  ],
                  const SizedBox(height: AppSpacing.xxl),
                ]))),
            ])))));
  }

  Widget _buildRandomButton(JournalViewModel vm, String locale) {
    return GestureDetector(onTap: () { HapticService.light(); setState(() { _selectedQuote = vm.getRandomQuote(); _searchController.clear(); _isSearching = false; _filteredQuotes = []; }); },
      child: Container(width: double.infinity, constraints: const BoxConstraints(minHeight: 52),
        padding: const EdgeInsets.symmetric(horizontal: AppSpacing.md, vertical: AppSpacing.sm),
        decoration: BoxDecoration(color: AppColors.accent.withValues(alpha: 0.1), borderRadius: BorderRadius.circular(12),
          border: Border.all(color: AppColors.accent.withValues(alpha: 0.3))),
        child: Row(mainAxisAlignment: MainAxisAlignment.center, children: [
          const Icon(Icons.shuffle, color: AppColors.accent, size: 20),
          const SizedBox(width: AppSpacing.sm),
          Text(locale == 'pt' ? 'Frase Aleat\u00F3ria' : locale == 'es' ? 'Frase Aleatoria' : 'Random Quote',
            style: AppFonts.body.copyWith(color: AppColors.accent, fontWeight: FontWeight.w600)),
        ])));
  }

  Widget _buildSearchField(JournalViewModel vm, String locale) {
    return TextField(controller: _searchController, style: AppFonts.body.copyWith(color: AppColors.textPrimary),
      onChanged: (q) => _filterQuotes(q, vm.quotes),
      decoration: InputDecoration(
        hintText: locale == 'pt' ? 'Buscar por autor, texto ou categoria...' : locale == 'es' ? 'Buscar por autor, texto o categor\u00EDa...' : 'Search by author, text or category...',
        hintStyle: AppFonts.body.copyWith(color: AppColors.textTertiary),
        prefixIcon: const Icon(Icons.search, color: AppColors.textTertiary),
        filled: true, fillColor: AppColors.surface,
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: BorderSide.none)));
  }

  Widget _buildSearchResults(String locale) {
    if (_filteredQuotes.isEmpty) return Padding(padding: const EdgeInsets.symmetric(vertical: AppSpacing.xl),
      child: Center(child: Text(locale == 'pt' ? 'Nenhuma frase encontrada' : locale == 'es' ? 'Ninguna frase encontrada' : 'No quotes found',
        style: AppFonts.body.copyWith(color: AppColors.textTertiary))));
    return Column(children: _filteredQuotes.map((q) => _buildQuoteItem(q, locale)).toList());
  }

  Widget _buildSuggestions(JournalViewModel vm, String locale) {
    final suggestions = (vm.quotes.toList()..shuffle()).take(5).toList();
    return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Text(locale == 'pt' ? 'Sugest\u00F5es' : locale == 'es' ? 'Sugerencias' : 'Suggestions',
        style: AppFonts.subheadline.copyWith(color: AppColors.textSecondary, fontWeight: FontWeight.w600)),
      const SizedBox(height: AppSpacing.sm),
      ...suggestions.map((q) => _buildQuoteItem(q, locale)),
    ]);
  }

  Widget _buildQuoteItem(QuoteModel quote, String locale) {
    return Padding(padding: const EdgeInsets.only(bottom: AppSpacing.sm),
      child: GestureDetector(onTap: () { HapticService.selection(); setState(() { _selectedQuote = quote; _searchController.clear(); _isSearching = false; _filteredQuotes = []; }); },
        child: Container(width: double.infinity, constraints: const BoxConstraints(minHeight: 52),
          padding: const EdgeInsets.all(AppSpacing.md),
          decoration: BoxDecoration(color: AppColors.surface, borderRadius: BorderRadius.circular(12)),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(quote.author(locale), style: AppFonts.body.copyWith(color: AppColors.textPrimary, fontWeight: FontWeight.w600)),
            const SizedBox(height: AppSpacing.xs),
            Text(quote.text(locale), style: AppFonts.subheadline.copyWith(color: AppColors.textSecondary, height: 1.4), maxLines: 2, overflow: TextOverflow.ellipsis),
          ]))));
  }

  Widget _buildSelectedQuote(String locale) {
    return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Row(children: [
        Expanded(child: Text(locale == 'pt' ? 'Frase selecionada' : locale == 'es' ? 'Frase seleccionada' : 'Selected quote',
          style: AppFonts.headline.copyWith(color: AppColors.textPrimary))),
        GestureDetector(onTap: () { HapticService.light(); setState(() => _selectedQuote = null); },
          child: Container(constraints: const BoxConstraints(minHeight: 44), alignment: Alignment.centerRight,
            color: Colors.transparent, padding: const EdgeInsets.symmetric(horizontal: AppSpacing.sm),
            child: Text(locale == 'pt' ? 'Trocar' : locale == 'es' ? 'Cambiar' : 'Change',
              style: AppFonts.body.copyWith(color: AppColors.accent, fontWeight: FontWeight.w600)))),
      ]),
      const SizedBox(height: AppSpacing.md),
      Container(width: double.infinity, padding: const EdgeInsets.all(AppSpacing.md),
        decoration: BoxDecoration(color: AppColors.accent.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(12),
          border: Border(left: BorderSide(color: AppColors.accent.withValues(alpha: 0.5), width: 3))),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text('\u201C${_selectedQuote!.text(locale)}\u201D', style: AppFonts.body.copyWith(color: AppColors.textPrimary, fontStyle: FontStyle.italic, height: 1.5)),
          const SizedBox(height: AppSpacing.sm),
          Text(_selectedQuote!.author(locale), style: AppFonts.subheadline.copyWith(color: AppColors.accent, fontWeight: FontWeight.w600)),
        ])),
    ]);
  }
}
