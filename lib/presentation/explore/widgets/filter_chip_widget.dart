import 'package:flutter/material.dart';
import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_fonts.dart';
import '../../../core/theme/app_spacing.dart';
import '../../../core/utils/haptic_service.dart';
import '../../../data/models/filter_option.dart';

class FilterChipWidget extends StatefulWidget {
  final FilterOption option;
  final bool isSelected;
  final VoidCallback onTap;

  const FilterChipWidget({super.key, required this.option, required this.isSelected, required this.onTap});

  @override
  State<FilterChipWidget> createState() => _FilterChipWidgetState();
}

class _FilterChipWidgetState extends State<FilterChipWidget> with SingleTickerProviderStateMixin {
  late final AnimationController _controller;
  late final Animation<double> _scaleAnim;
  late final Animation<double> _checkAnim;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 250),
    );
    _scaleAnim = TweenSequence<double>([
      TweenSequenceItem(tween: Tween(begin: 1.0, end: 0.92), weight: 40),
      TweenSequenceItem(tween: Tween(begin: 0.92, end: 1.02), weight: 40),
      TweenSequenceItem(tween: Tween(begin: 1.02, end: 1.0), weight: 20),
    ]).animate(CurvedAnimation(parent: _controller, curve: Curves.easeOutCubic));
    _checkAnim = CurvedAnimation(parent: _controller, curve: const Interval(0.3, 1.0, curve: Curves.easeOut));
    if (widget.isSelected) _controller.value = 1.0;
  }

  @override
  void didUpdateWidget(covariant FilterChipWidget oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (widget.isSelected != oldWidget.isSelected) {
      if (widget.isSelected) {
        _controller.forward(from: 0);
      } else {
        _controller.reverse();
      }
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () { HapticService.selection(); widget.onTap(); },
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, child) {
          return Transform.scale(
            scale: _scaleAnim.value,
            child: child,
          );
        },
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 250),
          curve: Curves.easeOutCubic,
          padding: EdgeInsets.only(
            left: widget.isSelected ? 10 : AppSpacing.md,
            right: AppSpacing.md,
            top: AppSpacing.sm,
            bottom: AppSpacing.sm,
          ),
          decoration: BoxDecoration(
            color: widget.isSelected
                ? widget.option.color.withValues(alpha: 0.18)
                : AppColors.surfaceSecondary.withValues(alpha: 0.6),
            borderRadius: BorderRadius.circular(24),
          ),
          child: Row(mainAxisSize: MainAxisSize.min, children: [
            // Animated check icon
            AnimatedSize(
              duration: const Duration(milliseconds: 250),
              curve: Curves.easeOutCubic,
              child: widget.isSelected
                  ? Padding(
                      padding: const EdgeInsets.only(right: 6),
                      child: FadeTransition(
                        opacity: _checkAnim,
                        child: Icon(Icons.check_rounded, size: 16, color: widget.option.color),
                      ),
                    )
                  : const SizedBox.shrink(),
            ),
            // Icon
            Icon(widget.option.icon, size: 15,
              color: widget.isSelected ? widget.option.color : AppColors.textSecondary),
            const SizedBox(width: 5),
            // Label
            Flexible(child: Text(widget.option.name,
              style: AppFonts.footnote.copyWith(
                color: widget.isSelected ? widget.option.color : AppColors.textSecondary,
                fontWeight: widget.isSelected ? FontWeight.w600 : FontWeight.w500,
                letterSpacing: 0.1,
              ),
              overflow: TextOverflow.ellipsis, maxLines: 1)),
          ]),
        ),
      ),
    );
  }
}
