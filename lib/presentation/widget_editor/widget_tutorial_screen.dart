import 'dart:io';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_fonts.dart';
import '../../core/theme/app_spacing.dart';
import '../../core/utils/haptic_service.dart';
import '../common/widgets/pressable_scale.dart';

class WidgetTutorialScreen extends StatelessWidget {
  const WidgetTutorialScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final locale = Localizations.localeOf(context).languageCode;
    final isAndroid = Platform.isAndroid;

    return Scaffold(
      backgroundColor: AppColors.background,
      body: SafeArea(child: Padding(
        padding: const EdgeInsets.all(AppSpacing.screenPadding),
        child: Column(children: [
          // Header
          Row(children: [
            GestureDetector(onTap: () => context.pop(),
              child: const Icon(Icons.arrow_back_ios, color: AppColors.textPrimary, size: 20)),
            const SizedBox(width: AppSpacing.sm),
            Text(
              locale == 'pt' ? 'Como adicionar' : locale == 'es' ? 'Cómo añadir' : 'How to add',
              style: AppFonts.title2.copyWith(color: AppColors.textPrimary)),
          ]),
          const SizedBox(height: AppSpacing.xl),

          // Icon
          Container(
            width: 72, height: 72,
            decoration: BoxDecoration(
              color: AppColors.primary.withValues(alpha: 0.12),
              shape: BoxShape.circle,
            ),
            child: Icon(
              isAndroid ? Icons.android : Icons.phone_iphone,
              color: AppColors.primary, size: 36,
            ),
          ),
          const SizedBox(height: AppSpacing.lg),

          // Title
          Text(
            isAndroid
                ? (locale == 'pt' ? 'Android' : locale == 'es' ? 'Android' : 'Android')
                : (locale == 'pt' ? 'iPhone' : locale == 'es' ? 'iPhone' : 'iPhone'),
            style: AppFonts.title.copyWith(color: AppColors.textPrimary),
          ),
          const SizedBox(height: AppSpacing.xl),

          // Steps
          Expanded(child: ListView(children: isAndroid
              ? _androidSteps(locale)
              : _iosSteps(locale))),

          // Done button
          PressableScale(
            onTap: () {
              HapticService.light();
              context.pop();
            },
            child: Container(
              width: double.infinity,
              padding: const EdgeInsets.symmetric(vertical: AppSpacing.md),
              decoration: BoxDecoration(
                color: AppColors.primary,
                borderRadius: BorderRadius.circular(14),
              ),
              child: Center(child: Text(
                locale == 'pt' ? 'Entendi' : locale == 'es' ? 'Entendido' : 'Got it',
                style: AppFonts.body.copyWith(color: Colors.white, fontWeight: FontWeight.w600),
              )),
            ),
          ),
        ]),
      )),
    );
  }

  List<Widget> _androidSteps(String locale) {
    final steps = locale == 'pt'
        ? [
            'Vá para a tela inicial do seu celular',
            'Segure pressionado em uma área vazia',
            'Toque em "Widgets"',
            'Procure por "Philos"',
            'Arraste o widget para a tela inicial',
          ]
        : locale == 'es'
            ? [
                'Ve a la pantalla de inicio de tu celular',
                'Mantén presionada un área vacía',
                'Toca en "Widgets"',
                'Busca "Philos"',
                'Arrastra el widget a la pantalla de inicio',
              ]
            : [
                'Go to your phone\'s home screen',
                'Long press on an empty area',
                'Tap "Widgets"',
                'Search for "Philos"',
                'Drag the widget to your home screen',
              ];
    return _buildStepsList(steps);
  }

  List<Widget> _iosSteps(String locale) {
    final steps = locale == 'pt'
        ? [
            'Vá para a tela inicial do seu iPhone',
            'Segure pressionado em uma área vazia',
            'Toque no "+" no canto superior',
            'Procure por "Philos"',
            'Escolha o tamanho e toque em "Adicionar Widget"',
          ]
        : locale == 'es'
            ? [
                'Ve a la pantalla de inicio de tu iPhone',
                'Mantén presionada un área vacía',
                'Toca el "+" en la esquina superior',
                'Busca "Philos"',
                'Elige el tamaño y toca "Añadir Widget"',
              ]
            : [
                'Go to your iPhone\'s home screen',
                'Long press on an empty area',
                'Tap the "+" in the top corner',
                'Search for "Philos"',
                'Choose a size and tap "Add Widget"',
              ];
    return _buildStepsList(steps);
  }

  List<Widget> _buildStepsList(List<String> steps) {
    return steps.asMap().entries.map((entry) {
      final index = entry.key;
      final text = entry.value;
      return Padding(
        padding: const EdgeInsets.only(bottom: AppSpacing.lg),
        child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Container(
            width: 32, height: 32,
            decoration: BoxDecoration(
              color: AppColors.primary.withValues(alpha: 0.12),
              shape: BoxShape.circle,
            ),
            child: Center(child: Text('${index + 1}',
              style: AppFonts.subheadline.copyWith(color: AppColors.primary, fontWeight: FontWeight.w700))),
          ),
          const SizedBox(width: AppSpacing.md),
          Expanded(child: Padding(
            padding: const EdgeInsets.only(top: 5),
            child: Text(text, style: AppFonts.body.copyWith(color: AppColors.textPrimary, height: 1.3)),
          )),
        ]),
      );
    }).toList();
  }
}
