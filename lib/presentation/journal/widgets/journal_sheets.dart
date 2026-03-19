import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';
import '../../../core/utils/haptic_service.dart';
import '../../../data/models/note_model.dart';
import '../../common/widgets/app_button.dart';
import '../journal_view_model.dart';
import 'reflection_sheet.dart';

void showAddOptions(BuildContext context, String locale) {
  HapticService.light();
  showModalBottomSheet(context: context, backgroundColor: AppColors.surface,
    shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(20))),
    builder: (sheetContext) => SafeArea(child: Padding(
      padding: const EdgeInsets.all(AppSpacing.screenPadding),
      child: Column(mainAxisSize: MainAxisSize.min, children: [
        _handle(),
        const SizedBox(height: AppSpacing.lg),
        _buildOptionTile(icon: Icons.edit_note, color: AppColors.accent,
          title: locale == 'pt' ? 'Nova Nota' : locale == 'es' ? 'Nueva Nota' : 'New Note',
          subtitle: locale == 'pt' ? 'Escreva um pensamento' : locale == 'es' ? 'Escribe un pensamiento' : 'Write a thought',
          onTap: () { Navigator.pop(sheetContext); showAddNoteSheet(context, locale); }),
        const SizedBox(height: AppSpacing.md),
        _buildOptionTile(icon: Icons.format_quote, color: AppColors.accent,
          title: locale == 'pt' ? 'Reflex\u00E3o de Frase' : locale == 'es' ? 'Reflexi\u00F3n de Frase' : 'Quote Reflection',
          subtitle: locale == 'pt' ? 'Escolha uma frase e reflita' : locale == 'es' ? 'Elige una frase y reflexiona' : 'Choose a quote and reflect',
          onTap: () { Navigator.pop(sheetContext); showJournalReflectionSheet(context, locale); }),
        const SizedBox(height: AppSpacing.lg),
      ]))));
}

Widget _buildOptionTile({required IconData icon, required Color color, required String title, required String subtitle, required VoidCallback onTap}) {
  return GestureDetector(onTap: onTap, child: Container(
    constraints: const BoxConstraints(minHeight: 72), padding: const EdgeInsets.all(AppSpacing.md),
    decoration: BoxDecoration(color: color.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(14)),
    child: Row(children: [
      Container(width: 48, height: 48,
        decoration: BoxDecoration(color: color.withValues(alpha: 0.15), shape: BoxShape.circle),
        child: Icon(icon, color: color, size: 24)),
      const SizedBox(width: AppSpacing.md),
      Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Text(title, style: AppFonts.headline.copyWith(color: AppColors.textPrimary)),
        const SizedBox(height: 2),
        Text(subtitle, style: AppFonts.subheadline.copyWith(color: AppColors.textSecondary)),
      ])),
      const Icon(Icons.chevron_right, color: AppColors.textTertiary, size: 24),
    ])));
}

void showAddNoteSheet(BuildContext context, String locale) {
  final controller = TextEditingController();
  _showTextSheet(context: context,
    title: locale == 'pt' ? 'Nova Nota' : locale == 'es' ? 'Nueva Nota' : 'New Note',
    controller: controller,
    hintText: locale == 'pt' ? 'Escreva seu pensamento...' : locale == 'es' ? 'Escribe tu pensamiento...' : 'Write your thought...',
    saveLabel: locale == 'pt' ? 'Salvar' : locale == 'es' ? 'Guardar' : 'Save',
    onSave: (text) { context.read<JournalViewModel>().addNote(text); });
}

void showJournalReflectionSheet(BuildContext context, String locale) {
  showModalBottomSheet(context: context, isScrollControlled: true, backgroundColor: Colors.transparent,
    builder: (_) => ReflectionSheet(locale: locale));
}

void showEditSheet(BuildContext context, JournalViewModel vm, NoteModel note, String locale) {
  final controller = TextEditingController(text: note.text);
  _showTextSheet(context: context,
    title: locale == 'pt' ? 'Editar' : locale == 'es' ? 'Editar' : 'Edit',
    controller: controller,
    saveLabel: locale == 'pt' ? 'Salvar' : locale == 'es' ? 'Guardar' : 'Save',
    onSave: (text) { vm.updateNote(note.id, text); });
}

void _showTextSheet({required BuildContext context, required String title, required TextEditingController controller,
  required String saveLabel, required void Function(String text) onSave, String? hintText}) {
  showModalBottomSheet(context: context, isScrollControlled: true, backgroundColor: Colors.transparent,
    builder: (_) => _TextSheetContent(title: title, controller: controller, saveLabel: saveLabel, onSave: onSave, hintText: hintText));
}

class _TextSheetContent extends StatelessWidget {
  final String title;
  final TextEditingController controller;
  final String saveLabel;
  final void Function(String text) onSave;
  final String? hintText;

  const _TextSheetContent({required this.title, required this.controller, required this.saveLabel, required this.onSave, this.hintText});

  @override
  Widget build(BuildContext context) {
    final bottomInset = MediaQuery.of(context).viewInsets.bottom;
    return GestureDetector(onTap: () => Navigator.pop(context), behavior: HitTestBehavior.opaque,
      child: DraggableScrollableSheet(initialChildSize: 0.85, minChildSize: 0.5, maxChildSize: 0.95,
        builder: (sheetContext, scrollController) => GestureDetector(onTap: () {},
          child: Container(
            decoration: const BoxDecoration(color: AppColors.background, borderRadius: BorderRadius.vertical(top: Radius.circular(20))),
            child: Column(children: [
              Padding(padding: const EdgeInsets.only(top: AppSpacing.sm), child: _handle()),
              Padding(padding: const EdgeInsets.all(AppSpacing.screenPadding), child: Row(children: [
                Expanded(child: Text(title, style: AppFonts.title.copyWith(color: AppColors.textPrimary))),
                IconButton(onPressed: () => Navigator.pop(sheetContext), icon: const Icon(Icons.close, color: AppColors.textPrimary)),
              ])),
              Expanded(child: SingleChildScrollView(controller: scrollController,
                padding: EdgeInsets.only(left: AppSpacing.screenPadding, right: AppSpacing.screenPadding, bottom: bottomInset + AppSpacing.xxl),
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  TextField(controller: controller, maxLines: 8, autofocus: true,
                    style: AppFonts.body.copyWith(color: AppColors.textPrimary),
                    decoration: InputDecoration(hintText: hintText, hintStyle: AppFonts.body.copyWith(color: AppColors.textTertiary),
                      filled: true, fillColor: AppColors.surface,
                      border: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: BorderSide.none))),
                  const SizedBox(height: AppSpacing.lg),
                  AppButton(color: AppColors.accent, title: saveLabel, onTap: () {
                    final text = controller.text.trim();
                    if (text.isNotEmpty) { HapticService.success(); onSave(text); Navigator.pop(sheetContext); }
                  }),
                ]))),
            ])))));
  }
}

void showDeleteConfirmation(BuildContext context, String locale, VoidCallback onConfirm) {
  showModalBottomSheet(context: context, backgroundColor: AppColors.surface,
    shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(20))),
    builder: (sheetContext) => SafeArea(child: Padding(
      padding: const EdgeInsets.all(AppSpacing.screenPadding),
      child: Column(mainAxisSize: MainAxisSize.min, children: [
        _handle(),
        const SizedBox(height: AppSpacing.lg),
        Text(locale == 'pt' ? 'Excluir nota?' : locale == 'es' ? '\u00BFEliminar nota?' : 'Delete note?',
          style: AppFonts.headline.copyWith(color: AppColors.textPrimary)),
        const SizedBox(height: AppSpacing.sm),
        Text(locale == 'pt' ? 'Essa a\u00E7\u00E3o n\u00E3o pode ser desfeita.' : locale == 'es' ? 'Esta acci\u00F3n no se puede deshacer.' : 'This action cannot be undone.',
          style: AppFonts.body.copyWith(color: AppColors.textSecondary)),
        const SizedBox(height: AppSpacing.lg),
        GestureDetector(onTap: () { HapticService.error(); Navigator.pop(sheetContext); onConfirm(); },
          child: Container(width: double.infinity, constraints: const BoxConstraints(minHeight: 52), alignment: Alignment.center,
            decoration: BoxDecoration(color: AppColors.error.withValues(alpha: 0.12), borderRadius: BorderRadius.circular(12)),
            child: Text(locale == 'pt' ? 'Excluir' : locale == 'es' ? 'Eliminar' : 'Delete',
              style: AppFonts.body.copyWith(color: AppColors.error, fontWeight: FontWeight.w600)))),
        const SizedBox(height: AppSpacing.sm),
        GestureDetector(onTap: () => Navigator.pop(sheetContext),
          child: Container(width: double.infinity, constraints: const BoxConstraints(minHeight: 52), alignment: Alignment.center,
            decoration: BoxDecoration(color: AppColors.surfaceSecondary, borderRadius: BorderRadius.circular(12)),
            child: Text(locale == 'pt' ? 'Cancelar' : locale == 'es' ? 'Cancelar' : 'Cancel',
              style: AppFonts.body.copyWith(color: AppColors.textSecondary, fontWeight: FontWeight.w600)))),
        const SizedBox(height: AppSpacing.md),
      ]))));
}

Widget _handle() => Container(width: 40, height: 4,
  decoration: BoxDecoration(color: AppColors.surfaceSecondary, borderRadius: BorderRadius.circular(2)));
