import 'package:flutter/material.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';
import '../../../core/utils/haptic_service.dart';
import '../../../data/models/note_model.dart';
import '../../common/widgets/app_card.dart';

class NoteCard extends StatelessWidget {
  final NoteModel note;
  final String locale;
  final VoidCallback onEdit;
  final VoidCallback onDelete;

  const NoteCard({super.key, required this.note, required this.locale, required this.onEdit, required this.onDelete});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () { HapticService.light(); onEdit(); },
      onLongPress: () { HapticService.selection(); _showOptionsSheet(context); },
      child: AppCard(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Row(children: [
          Icon(note.isReflection ? Icons.format_quote : Icons.edit_note, size: 28, color: AppColors.accent),
          const SizedBox(width: AppSpacing.sm),
          Expanded(child: Text(
            note.isReflection ? '${_reflectionLabel(locale)} \u2014 ${_formatDate(note.createdAt, locale)}' : _formatDate(note.createdAt, locale),
            style: AppFonts.subheadline.copyWith(color: AppColors.textSecondary))),
          GestureDetector(
            onTap: () { HapticService.selection(); _showOptionsSheet(context); },
            child: Container(width: 44, height: 44, alignment: Alignment.center, color: Colors.transparent,
              child: const Icon(Icons.more_vert, size: 28, color: AppColors.textTertiary))),
        ]),
        if (note.isReflection) ...[
          const SizedBox(height: AppSpacing.sm),
          Container(width: double.infinity, padding: const EdgeInsets.all(AppSpacing.md),
            decoration: BoxDecoration(
              color: AppColors.accent.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(12),
              border: Border(left: BorderSide(color: AppColors.accent.withValues(alpha: 0.5), width: 3))),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text('\u201C${note.quoteText}\u201D', style: AppFonts.body.copyWith(color: AppColors.textPrimary, fontStyle: FontStyle.italic, height: 1.5)),
              const SizedBox(height: AppSpacing.sm),
              Text(note.quoteAuthor!, style: AppFonts.subheadline.copyWith(color: AppColors.accent, fontWeight: FontWeight.w600)),
            ])),
        ],
        const SizedBox(height: AppSpacing.sm),
        Text(note.text, style: AppFonts.body.copyWith(color: AppColors.textPrimary, height: 1.5)),
      ])),
    );
  }

  void _showOptionsSheet(BuildContext context) {
    showModalBottomSheet(context: context, backgroundColor: AppColors.surface,
      shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(20))),
      builder: (_) => SafeArea(child: Padding(
        padding: const EdgeInsets.all(AppSpacing.screenPadding),
        child: Column(mainAxisSize: MainAxisSize.min, children: [
          Container(width: 40, height: 4, decoration: BoxDecoration(color: AppColors.surfaceSecondary, borderRadius: BorderRadius.circular(2))),
          const SizedBox(height: AppSpacing.lg),
          _buildOptionRow(icon: Icons.edit_outlined, color: AppColors.accent, label: _editLabel(locale),
            onTap: () { Navigator.pop(context); onEdit(); }),
          const SizedBox(height: AppSpacing.sm),
          _buildOptionRow(icon: Icons.delete_outline, color: AppColors.error, label: _deleteLabel(locale),
            onTap: () { Navigator.pop(context); onDelete(); }),
          const SizedBox(height: AppSpacing.md),
        ]))));
  }

  Widget _buildOptionRow({required IconData icon, required Color color, required String label, required VoidCallback onTap}) {
    return GestureDetector(onTap: () { HapticService.light(); onTap(); },
      child: Container(constraints: const BoxConstraints(minHeight: 52),
        padding: const EdgeInsets.symmetric(horizontal: AppSpacing.md, vertical: AppSpacing.md),
        decoration: BoxDecoration(color: color.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(12)),
        child: Row(children: [
          Icon(icon, color: color, size: 28),
          const SizedBox(width: AppSpacing.md),
          Text(label, style: AppFonts.body.copyWith(color: color, fontWeight: FontWeight.w600)),
        ])));
  }

  String _reflectionLabel(String locale) { if (locale == 'pt') return 'Reflex\u00E3o'; if (locale == 'es') return 'Reflexi\u00F3n'; return 'Reflection'; }
  String _editLabel(String locale) { if (locale == 'pt') return 'Editar'; if (locale == 'es') return 'Editar'; return 'Edit'; }
  String _deleteLabel(String locale) { if (locale == 'pt') return 'Deletar'; if (locale == 'es') return 'Eliminar'; return 'Delete'; }
  String _formatDate(DateTime date, String locale) {
    final months = locale == 'pt' ? ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
      : locale == 'es' ? ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
      : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    return '${date.day} ${months[date.month - 1]}, ${date.year}';
  }
}
