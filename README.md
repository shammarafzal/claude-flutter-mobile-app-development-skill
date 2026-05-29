# Claude Flutter Mobile App Development Skill

A community Claude Skill for Flutter developers, freelancers, and agencies who want to plan, build, debug, review, and publish production-ready Flutter mobile apps faster.

This Skill helps Claude generate better Flutter guidance using feature-first Clean Architecture, scalable project structure, API integration patterns, Firebase workflows, Laravel backend support, responsive UI rules, debugging workflows, and publishing checklists.

> Independent community project. Not affiliated with, sponsored by, or endorsed by Google, Flutter, Anthropic, or Claude.

---

## What this Skill helps with

- Flutter app architecture planning
- Feature-first Clean Architecture
- Flutter UI from screenshots, requirements, or Figma-style descriptions
- REST API integration
- Laravel API integration
- Firebase Auth, Firestore, FCM, Crashlytics, and Analytics guidance
- Local storage and caching guidance
- Authentication and token handling
- Payment integration safety rules
- State management with Bloc, Cubit, Riverpod, Provider, or setState
- Flutter/Dart error debugging
- Project structure review
- Play Store and App Store publishing preparation

---

## Why this Skill exists

AI-generated Flutter code often has the same problems:

- Messy folder structure
- API calls inside widgets
- No clean separation between UI, data, and business logic
- Missing loading, error, and empty states
- Poor scalability for client projects
- Weak publishing guidance
- No clear architecture standard

This Skill gives Claude a stronger development workflow so it can produce cleaner, more production-friendly Flutter output.

---

## Default project structure

This Skill uses **Feature-First Clean Architecture** as the default structure for professional Flutter apps.

```text
lib/
├── main.dart
├── injection_container.dart
├── core/
│   ├── constants/
│   ├── error/
│   ├── network/
│   ├── storage/
│   ├── theme/
│   ├── usecases/
│   ├── utils/
│   └── widgets/
├── features/
│   └── feature_name/
│       ├── data/
│       │   ├── datasources/
│       │   ├── models/
│       │   └── repositories/
│       ├── domain/
│       │   ├── entities/
│       │   ├── repositories/
│       │   └── usecases/
│       └── presentation/
│           ├── bloc/ or cubit/ or providers/
│           ├── pages/
│           └── widgets/
└── shared/
    └── widgets/
```

This structure is suitable for:

- Client apps
- API-backed apps
- Flutter + Laravel projects
- Firebase apps
- Ecommerce apps
- Booking apps
- Delivery apps
- Marketplace apps
- Apps that may grow over time

---

## Repository structure

```text
claude-flutter-mobile-app-development-skill/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── THIRD_PARTY_NOTICES.md
├── .gitignore
├── examples/
├── assets/
└── flutter-mobile-app-development/
    ├── SKILL.md
    ├── README.md
    ├── resources/
    ├── templates/
    ├── checklists/
    └── scripts/
```

---

## Included in this Skill

```text
flutter-mobile-app-development/
├── SKILL.md
├── README.md
├── resources/
│   ├── official_flutter_skills_strategy.md
│   ├── clean_architecture_structure.md
│   ├── flutter_workflows.md
│   ├── state_management.md
│   ├── api_firebase_laravel.md
│   └── publishing_checklist.md
├── templates/
│   ├── dio_api_client.dart
│   ├── go_router_template.dart
│   ├── result_failure.dart
│   └── feature_readme_template.md
├── checklists/
│   └── flutter_app_review_checklist.md
└── scripts/
    └── scaffold_flutter_feature.py
```

---

## Example prompts

```text
Build a Flutter app architecture for a food delivery app with Laravel backend.
```

```text
Create a feature-first Clean Architecture auth module using Cubit, Dio, and Laravel API.
```

```text
Convert this mobile app screen into Flutter UI with responsive layout.
```

```text
Review my Flutter project structure and tell me what to fix.
```

```text
Fix this RenderFlex overflow error in my Flutter screen.
```

```text
Add a Dio API client with token interceptor and error handling.
```

```text
Prepare my Flutter app for Play Store release.
```

---

## Install in claude.ai

1. Download or clone this repository.
2. Keep the Skill folder name as:

```text
flutter-mobile-app-development
```

3. Zip the folder so the ZIP contains the folder at its root.

Correct Claude Skill ZIP structure:

```text
flutter-mobile-app-development.zip
└── flutter-mobile-app-development/
    ├── SKILL.md
    ├── resources/
    ├── templates/
    ├── checklists/
    └── scripts/
```

4. Upload the ZIP in Claude custom Skills settings.

---

## Install with `npx skills`

Install this Skill directly from GitHub into your project:

```bash
npx skills add shammarafzal/claude-flutter-mobile-app-development-skill --skill flutter-mobile-app-development --agent universal --yes
```

Install it specifically for Claude Code:

```bash
npx skills add shammarafzal/claude-flutter-mobile-app-development-skill --skill flutter-mobile-app-development --agent claude-code --yes
```

List the Skills detected in this repository:

```bash
npx skills add shammarafzal/claude-flutter-mobile-app-development-skill --list
```

Install all Skills from this repository:

```bash
npx skills add shammarafzal/claude-flutter-mobile-app-development-skill --skill '*' --agent universal --yes
```

For Flutter projects, you can also install the official Flutter and Dart agent skills:

```bash
npx skills add flutter/skills --skill '*' --agent universal --yes
npx skills add dart-lang/skills --skill '*' --agent universal --yes
```

### Notes

- `--agent universal` installs to the shared `.agents/skills/` location.
- `--agent claude-code` installs to Claude Code's `.claude/skills/` location.
- This repository keeps the actual Claude Skill in `flutter-mobile-app-development/`.
- The Skills CLI discovers valid `SKILL.md` files with `name` and `description` frontmatter.

## Use with Claude Code

Place the `flutter-mobile-app-development` folder inside your Claude Code Skills directory.

For Flutter projects, you can also install the official Flutter and Dart agent skills:

```bash
npx skills add flutter/skills --skill '*' --agent universal --yes
npx skills add dart-lang/skills --skill '*' --agent universal --yes
```

This community Skill works well as a higher-level mobile app development workflow on top of official Flutter/Dart task-specific skills.

---

## Feature scaffolding script

This Skill includes a helper script to generate a feature-first Clean Architecture module.

```bash
python flutter-mobile-app-development/scripts/scaffold_flutter_feature.py auth
```

With Cubit:

```bash
python flutter-mobile-app-development/scripts/scaffold_flutter_feature.py orders --state cubit
```

---

## Recommended use cases

This Skill is useful for:

- Flutter freelancers
- Mobile app agencies
- Solo developers
- AI-assisted coding workflows
- Flutter + Laravel developers
- Firebase app developers
- Developers building client apps
- Developers who want cleaner AI-generated Flutter code

---

## Roadmap

- [x] Clean Architecture workflow
- [x] Feature-first project structure
- [x] Flutter UI workflow
- [x] Laravel API workflow
- [x] Firebase workflow
- [x] Publishing checklist
- [x] App review checklist
- [ ] Supabase workflow
- [ ] In-app purchase workflow
- [ ] Animation workflow
- [ ] Testing workflow
- [ ] Sample generated app
- [ ] More real-world example prompts

---

## Disclaimer

This is an independent community Claude Skill for Flutter mobile app development.

It is inspired by the official Flutter Agent Skills project, but it is not affiliated with, sponsored by, or endorsed by Google, Flutter, Anthropic, or Claude.

Flutter is a trademark of Google LLC. Claude is a product of Anthropic.

---

## License

MIT License

If you copy or include direct content from third-party repositories, make sure to include their original license notices in `THIRD_PARTY_NOTICES.md`.
