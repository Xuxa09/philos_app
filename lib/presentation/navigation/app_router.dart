import 'package:go_router/go_router.dart';
import '../../data/services/storage_service.dart';
import '../favorites/favorites_screen.dart';
import '../home/home_screen.dart';
import '../explore/explore_screen.dart';
import '../journal/journal_screen.dart';
import '../authors/authors_screen.dart';
import '../moods/moods_screen.dart';
import '../onboarding/onboarding_screen.dart';
import '../schools/schools_screen.dart';
import '../settings/settings_screen.dart';
import '../widget_editor/widget_editor_screen.dart';
import '../widget_editor/widget_tutorial_screen.dart';
import 'main_shell.dart';

GoRouter createRouter() {
  final isOnboarded = StorageService.instance.isOnboardingComplete;
  return GoRouter(
    initialLocation: isOnboarded ? '/' : '/onboarding',
    routes: [
      GoRoute(path: '/onboarding', builder: (context, state) => const OnboardingScreen()),
      GoRoute(path: '/settings', builder: (context, state) => const SettingsScreen()),
      GoRoute(path: '/moods', builder: (context, state) => const MoodsScreen()),
      GoRoute(path: '/schools', builder: (context, state) => const SchoolsScreen()),
      GoRoute(path: '/authors', builder: (context, state) => const AuthorsScreen()),
      GoRoute(path: '/journal', builder: (context, state) => const JournalScreen()),
      GoRoute(path: '/widget-editor', builder: (context, state) => const WidgetEditorScreen()),
      GoRoute(path: '/widget-tutorial', builder: (context, state) => const WidgetTutorialScreen()),
      ShellRoute(
        builder: (context, state, child) => MainShell(child: child),
        routes: [
          GoRoute(path: '/', pageBuilder: (context, state) => const NoTransitionPage(child: HomeScreen())),
          GoRoute(path: '/explore', pageBuilder: (context, state) => const NoTransitionPage(child: ExploreScreen())),
          GoRoute(path: '/favorites', pageBuilder: (context, state) => const NoTransitionPage(child: FavoritesScreen())),
        ],
      ),
    ],
  );
}
