# State Management Guide

## Default choices

### Local UI state

Use `setState` for:

- selected tab
- show/hide password
- dropdown selection
- animation toggles
- temporary form-only state

### Small apps

Use Provider or Riverpod.

### Medium/large apps

Use Bloc/Cubit or Riverpod.

### Existing project

Follow the existing project if it is consistent.

## Bloc/Cubit

Use when:

- Team prefers strict structure
- App has complex flows
- You need explicit event/state logs
- Enterprise/client code requires predictable patterns

Folder:

```text
presentation/
└── bloc/
    ├── feature_bloc.dart
    ├── feature_event.dart
    └── feature_state.dart
```

Or with Cubit:

```text
presentation/
└── cubit/
    ├── feature_cubit.dart
    └── feature_state.dart
```

## Riverpod

Use when:

- You want modern, testable providers
- You want less boilerplate than Bloc
- App has many async dependencies
- You need provider composition

Folder:

```text
presentation/
└── providers/
    ├── feature_provider.dart
    └── feature_state.dart
```

## Provider/ChangeNotifier

Use when:

- App is small/medium
- Team is beginner-friendly
- Official Flutter architecture style is desired
- MVVM with `ChangeNotifier` is enough

Folder:

```text
presentation/
└── view_models/
    └── feature_view_model.dart
```

## GetX

Do not choose GetX by default for new professional apps. Continue using it only when:

- Existing project already uses GetX heavily
- Client explicitly requests it
- Team accepts the tradeoffs
