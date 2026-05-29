# Official Flutter Skills Strategy

Use this custom skill as the **orchestrator** for Flutter mobile app development.

The official Flutter Skills repo uses small, task-focused skills instead of one giant documentation skill. Follow that style:

- Architecture work: structure or refactor apps using layered separation.
- Responsive UI work: use responsive constraints, `LayoutBuilder`, `MediaQuery`, `Expanded`, `Flexible`, scroll views, and adaptive layouts.
- Layout debugging: fix overflow, unbounded constraints, keyboard issues, and nested scroll problems.
- Routing: configure declarative routing with `MaterialApp.router` and `go_router`.
- JSON/API work: create typed models and parse responses safely.
- HTTP work: use a dedicated service/API client, not direct calls in widgets.
- Localization: add `flutter_localizations`, `intl`, `l10n.yaml`, and generated ARB files.
- Testing: add widget/integration tests for important flows.

## Recommended use with official Flutter skills

For Claude Code or other agents that support the `.agents/skills` folder, install official Flutter skills into the project:

```bash
npx skills add flutter/skills --skill '*' --agent universal --yes
npx skills add dart-lang/skills --skill '*' --agent universal --yes
```

Then use this custom skill as the high-level mobile app development workflow and let the official task-specific skills guide individual tasks.

## Standalone behavior

If official skills are not installed, this skill must still work. Use the resources in this folder as the source of process and standards.
