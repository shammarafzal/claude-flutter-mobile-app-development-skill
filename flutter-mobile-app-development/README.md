# Flutter Mobile App Development Claude Skill

A custom Claude Skill for building professional Flutter mobile apps.

## What it does

This skill helps Claude:

- Plan Flutter app architecture
- Build Flutter UI from requirements, screenshots, or Figma-like descriptions
- Scaffold feature-first Clean Architecture modules
- Integrate REST APIs, Laravel APIs, Firebase, local storage, auth, and payments safely
- Debug Flutter/Dart errors
- Review Flutter projects
- Prepare Android/iOS apps for publishing

## Why this version is stronger

This package follows the official Flutter Skills approach: skills should be task-oriented and workflow-driven, not just long static documentation.

It also uses a stricter feature-first Clean Architecture default:

```text
features/feature_name/{data,domain,presentation}
```

This is suitable for client apps, API-backed apps, Flutter + Laravel projects, Firebase apps, ecommerce apps, booking apps, and apps that may grow.

## Install in claude.ai

1. Keep the folder name as `flutter-mobile-app-development`.
2. Zip the folder so the ZIP contains the folder at its root.
3. Upload the ZIP in Claude custom Skills settings.

Correct:

```text
flutter-mobile-app-development.zip
└── flutter-mobile-app-development/
    ├── SKILL.md
    ├── resources/
    ├── templates/
    ├── checklists/
    └── scripts/
```

## Use with Claude Code

Place the folder in a Skills directory supported by your Claude Code setup.

For Flutter projects, also consider installing the official Flutter/Dart Skills:

```bash
npx skills add flutter/skills --skill '*' --agent universal --yes
npx skills add dart-lang/skills --skill '*' --agent universal --yes
```

## Example prompts

- Build a Flutter app architecture for a food delivery app with Laravel backend.
- Create a feature-first Clean Architecture auth module using Bloc.
- Convert this mobile app screen into Flutter UI.
- Review my Flutter project structure and tell me what to fix.
- Fix this RenderFlex overflow error.
- Add Dio API client and token interceptor.
- Prepare my Flutter app for Play Store release.

## Install from GitHub with `npx skills`

```bash
npx skills add shammarafzal/claude-flutter-mobile-app-development-skill --skill flutter-mobile-app-development --agent universal --yes
```

For Claude Code only:

```bash
npx skills add shammarafzal/claude-flutter-mobile-app-development-skill --skill flutter-mobile-app-development --agent claude-code --yes
```
