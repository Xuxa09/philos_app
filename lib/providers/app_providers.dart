import 'package:provider/provider.dart';
import 'package:provider/single_child_widget.dart';
import '../presentation/authors/authors_view_model.dart';
import '../presentation/home/home_view_model.dart';
import '../presentation/explore/explore_view_model.dart';
import '../presentation/journal/journal_view_model.dart';
import '../presentation/moods/moods_view_model.dart';
import '../presentation/favorites/favorites_view_model.dart';
import '../presentation/schools/schools_view_model.dart';
import '../presentation/settings/settings_view_model.dart';

// === App-Wide Providers ===

List<SingleChildWidget> get appProviders => [
  ChangeNotifierProvider(create: (_) => HomeViewModel()),
  ChangeNotifierProvider(create: (_) => ExploreViewModel()),
  ChangeNotifierProvider(create: (_) => FavoritesViewModel()),
  ChangeNotifierProvider(create: (_) => SettingsViewModel()),
  ChangeNotifierProvider(create: (_) => MoodsViewModel()),
  ChangeNotifierProvider(create: (_) => JournalViewModel()),
  ChangeNotifierProvider(create: (_) => SchoolsViewModel()),
  ChangeNotifierProvider(create: (_) => AuthorsViewModel()),
];
