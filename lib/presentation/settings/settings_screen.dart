import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:in_app_review/in_app_review.dart';
import 'package:provider/provider.dart';
import 'package:share_plus/share_plus.dart';
import 'package:url_launcher/url_launcher.dart';
import '../../core/constants/app_constants.dart';
import '../../core/extensions/context_extensions.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../../core/utils/haptic_service.dart';
import 'settings_view_model.dart';

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key});
  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  @override
  void initState() { super.initState(); Future.microtask(() => context.read<SettingsViewModel>().loadSettings()); }

  @override
  Widget build(BuildContext context) {
    return Scaffold(backgroundColor: AppColors.background,
      body: Consumer<SettingsViewModel>(builder: (context, vm, _) => _buildContent(context, vm)));
  }

  Widget _buildContent(BuildContext context, SettingsViewModel vm) {
    return SafeArea(child: ListView(padding: const EdgeInsets.all(AppSpacing.screenPadding), children: [
      Row(children: [
        GestureDetector(onTap: () => context.pop(), child: const Icon(Icons.arrow_back_ios, color: AppColors.textPrimary, size: 20)),
        const SizedBox(width: AppSpacing.sm),
        Text(context.l10n.settingsTitle, style: AppFonts.largeTitle.copyWith(color: AppColors.textPrimary)),
      ]),
      const SizedBox(height: AppSpacing.xl),
      _buildSectionTitle(context.l10n.settingsGeneral),
      const SizedBox(height: AppSpacing.sm),
      _buildSettingsTile(icon: Icons.language, title: context.l10n.settingsLanguage,
        trailing: Text(_localeName(vm.selectedLocale), style: AppFonts.subheadline.copyWith(color: AppColors.textSecondary)),
        onTap: () => _showLanguagePicker(context, vm)),
      _buildSettingsTile(icon: Icons.notifications_outlined, title: context.l10n.settingsDailyReminder,
        trailing: Switch.adaptive(value: vm.notificationsEnabled, activeTrackColor: AppColors.primary, onChanged: vm.toggleNotifications)),
      const SizedBox(height: AppSpacing.lg),
      _buildSectionTitle(context.l10n.settingsSupport),
      const SizedBox(height: AppSpacing.sm),
      _buildSettingsTile(icon: Icons.star_outline, title: context.l10n.settingsRateApp,
        onTap: () async { HapticService.light(); final r = InAppReview.instance; if (await r.isAvailable()) await r.requestReview(); }),
      _buildSettingsTile(icon: Icons.share_outlined, title: context.l10n.settingsShareApp,
        onTap: () { HapticService.light(); Share.share(context.l10n.settingsShareMessage); }),
      const SizedBox(height: AppSpacing.lg),
      _buildSectionTitle(_widgetSectionTitle(vm.selectedLocale)),
      const SizedBox(height: AppSpacing.sm),
      _buildSettingsTile(
        icon: Icons.palette_outlined,
        title: vm.selectedLocale == 'pt' ? 'Personalizar' : vm.selectedLocale == 'es' ? 'Personalizar' : 'Customize',
        onTap: () => context.push('/widget-editor'),
      ),
      _buildSettingsTile(
        icon: Icons.widgets_outlined,
        title: vm.selectedLocale == 'pt' ? 'Adicionar Widget' : vm.selectedLocale == 'es' ? 'Añadir Widget' : 'Add Widget',
        onTap: () => context.push('/widget-tutorial'),
      ),
      const SizedBox(height: AppSpacing.lg),
      _buildSectionTitle(context.l10n.settingsLegal),
      const SizedBox(height: AppSpacing.sm),
      _buildSettingsTile(icon: Icons.privacy_tip_outlined, title: context.l10n.settingsPrivacyPolicy,
        onTap: () => launchUrl(Uri.parse(AppConstants.privacyPolicyUrl))),
      const SizedBox(height: AppSpacing.lg),
      Center(child: Text('${context.l10n.settingsVersion} ${vm.appVersion}', style: AppFonts.caption.copyWith(color: AppColors.textTertiary))),
      const SizedBox(height: AppSpacing.xxl),
    ]));
  }

  Widget _buildSectionTitle(String title) => Text(title.toUpperCase(),
    style: AppFonts.caption.copyWith(color: AppColors.textTertiary, letterSpacing: 1, fontWeight: FontWeight.w600));

  Widget _buildSettingsTile({required IconData icon, required String title, Widget? trailing, VoidCallback? onTap}) {
    return GestureDetector(onTap: onTap, child: Container(
      padding: const EdgeInsets.symmetric(horizontal: AppSpacing.md, vertical: AppSpacing.md - 2),
      margin: const EdgeInsets.only(bottom: 1),
      decoration: BoxDecoration(color: AppColors.surface, borderRadius: BorderRadius.circular(12)),
      child: Row(children: [
        Icon(icon, color: AppColors.primary, size: 28),
        const SizedBox(width: AppSpacing.md),
        Expanded(child: Text(title, style: AppFonts.body.copyWith(color: AppColors.textPrimary))),
        trailing ?? const Icon(Icons.chevron_right, color: AppColors.textTertiary, size: 28),
      ])));
  }

  void _showLanguagePicker(BuildContext context, SettingsViewModel vm) {
    showModalBottomSheet(context: context, backgroundColor: AppColors.surface, isScrollControlled: true,
      shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(20))),
      builder: (_) => SafeArea(child: Column(mainAxisSize: MainAxisSize.min, children: [
        const SizedBox(height: AppSpacing.md),
        Container(width: 40, height: 4, decoration: BoxDecoration(color: AppColors.surfaceSecondary, borderRadius: BorderRadius.circular(2))),
        const SizedBox(height: AppSpacing.lg),
        _buildLanguageOption(context, vm, 'en', 'English'),
        _buildLanguageOption(context, vm, 'pt', 'Portugu\u00EAs'),
        _buildLanguageOption(context, vm, 'es', 'Espa\u00F1ol'),
        const SizedBox(height: AppSpacing.lg),
      ])));
  }

  Widget _buildLanguageOption(BuildContext context, SettingsViewModel vm, String code, String name) {
    final isSelected = vm.selectedLocale == code;
    return ListTile(
      title: Text(name, style: AppFonts.body.copyWith(
        color: isSelected ? AppColors.primary : AppColors.textPrimary,
        fontWeight: isSelected ? FontWeight.w600 : FontWeight.normal)),
      trailing: isSelected ? const Icon(Icons.check, color: AppColors.primary) : null,
      onTap: () { HapticService.selection(); vm.setLocale(code); Navigator.pop(context); });
  }

  String _localeName(String code) { switch (code) { case 'pt': return 'Portugu\u00EAs'; case 'es': return 'Espa\u00F1ol'; default: return 'English'; } }

  String _widgetSectionTitle(String locale) {
    if (locale == 'pt') return 'Widget';
    if (locale == 'es') return 'Widget';
    return 'Widget';
  }
}
