# Changelog

All notable changes to this project will be documented in this file.

## [2025-09-21] – First Refactor

### Added
- Complete refactor of the project structure with modular separation (`core/`, `entities/`, `hud/`).
- Custom HUD with `Scoreboard` and `GameOverScreen` for real-time score display and clear Game Over state.
- Sound system with `SoundPlayer` (background music + sound effects with adjustable volume).
- Collision detection using `pygame.Rect` for improved accuracy and performance.
- Restart functionality after Game Over by pressing **Enter**, restoring all game elements without closing the application.
- Progressive difficulty: enemy speed increases slightly after each enemy is destroyed.
- Dynamic FPS display in the window title for performance monitoring.

### Changed
- Improved enemy grid distribution for consistent spacing and alignment.
- Updated scoring system to award points in increments of 10 per enemy destroyed.
- Refined bullet firing logic to prevent overlapping shots.
- Organized assets into dedicated folders: `fonts/`, `images/`, and `sounds/`.

## [2022-09-07] – Initial Release
- First public version developed during TechCamp Adakademy 2022 (*Videogame Design with Python*).
- Basic Space Invaders clone using Pygame.
- Single-file structure with minimal separation of logic.
- Basic enemy movement and shooting mechanics.