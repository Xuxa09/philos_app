import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../core/theme/app_colors.dart';
import '../../core/utils/haptic_service.dart';

class MainShell extends StatelessWidget {
  final Widget child;
  const MainShell({super.key, required this.child});

  int _currentIndex(BuildContext context) {
    final location = GoRouterState.of(context).uri.toString();
    if (location.startsWith('/explore')) return 1;
    if (location.startsWith('/favorites')) return 2;
    return 0;
  }

  void _onTap(BuildContext context, int index) {
    HapticService.selection();
    switch (index) {
      case 0: context.go('/');
      case 1: context.go('/explore');
      case 2: context.go('/favorites');
    }
  }

  @override
  Widget build(BuildContext context) {
    final locale = Localizations.localeOf(context).languageCode;
    return Scaffold(
      body: child,
      bottomNavigationBar: NavigationBar(
        selectedIndex: _currentIndex(context),
        onDestinationSelected: (index) => _onTap(context, index),
        backgroundColor: AppColors.surface,
        indicatorColor: AppColors.primary.withValues(alpha: 0.15),
        height: 65,
        animationDuration: Duration.zero,
        labelBehavior: NavigationDestinationLabelBehavior.alwaysShow,
        destinations: [
          NavigationDestination(
            icon: const Icon(Icons.format_quote_outlined),
            selectedIcon: const Icon(Icons.format_quote),
            label: locale == 'pt' ? 'In\u00EDcio' : locale == 'es' ? 'Inicio' : 'Home',
          ),
          NavigationDestination(
            icon: const Icon(Icons.explore_outlined),
            selectedIcon: const Icon(Icons.explore),
            label: locale == 'pt' ? 'Explorar' : locale == 'es' ? 'Explorar' : 'Explore',
          ),
          NavigationDestination(
            icon: const Icon(Icons.favorite_border),
            selectedIcon: const Icon(Icons.favorite),
            label: locale == 'pt' ? 'Favoritos' : locale == 'es' ? 'Favoritos' : 'Favorites',
          ),
        ],
      ),
    );
  }
}
