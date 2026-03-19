import 'package:flutter/material.dart';
import '../../data/services/storage_service.dart';

class OnboardingViewModel extends ChangeNotifier {
  final _storage = StorageService.instance;
  int _currentPage = 0;
  final pageController = PageController();

  int get currentPage => _currentPage;
  int get totalPages => 3;
  bool get isLastPage => _currentPage == totalPages - 1;

  void setPage(int page) { _currentPage = page; notifyListeners(); }

  void nextPage() {
    if (!isLastPage) pageController.nextPage(duration: const Duration(milliseconds: 400), curve: Curves.easeOutCubic);
  }

  Future<void> completeOnboarding() async { await _storage.setOnboardingComplete(); }

  @override
  void dispose() { pageController.dispose(); super.dispose(); }
}
