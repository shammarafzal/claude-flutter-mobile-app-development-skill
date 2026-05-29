# Feature-First Clean Architecture Structure

## Default recommendation

Use **Feature-First Clean Architecture** for production Flutter mobile apps.

This is the default for:

- Flutter + Laravel API apps
- Firebase apps
- Ecommerce apps
- Booking apps
- Delivery apps
- Marketplace apps
- Multi-role apps
- Client projects that may grow
- Apps with authentication, payments, chat, notifications, maps, or admin dashboards

## Dependency rule

Dependencies point inward:

```text
Presentation -> Domain <- Data
```

Rules:

- Domain never imports Flutter.
- Domain never imports Data.
- Domain never imports Presentation.
- Data implements repository contracts from Domain.
- Presentation calls UseCases or a ViewModel/Bloc/Cubit that calls UseCases.
- Data layer throws/handles technical exceptions.
- Domain layer exposes business failures/results.
- UI displays state and sends user events only.

## Complete folder structure

```text
lib/
├── main.dart
├── injection_container.dart
├── app/
│   ├── app.dart
│   ├── router.dart
│   └── bootstrap.dart
├── core/
│   ├── constants/
│   │   ├── app_constants.dart
│   │   ├── api_constants.dart
│   │   └── asset_paths.dart
│   ├── error/
│   │   ├── exceptions.dart
│   │   └── failures.dart
│   ├── network/
│   │   ├── api_client.dart
│   │   └── network_info.dart
│   ├── storage/
│   │   ├── secure_storage_service.dart
│   │   └── local_storage_service.dart
│   ├── theme/
│   │   ├── app_colors.dart
│   │   ├── app_text_styles.dart
│   │   └── app_theme.dart
│   ├── usecases/
│   │   └── usecase.dart
│   ├── utils/
│   │   ├── form_validators.dart
│   │   ├── input_converter.dart
│   │   └── debouncer.dart
│   └── widgets/
│       ├── app_button.dart
│       ├── app_text_field.dart
│       ├── app_error_view.dart
│       └── app_loading.dart
├── features/
│   └── auth/
│       ├── data/
│       │   ├── datasources/
│       │   │   ├── auth_remote_data_source.dart
│       │   │   └── auth_local_data_source.dart
│       │   ├── models/
│       │   │   └── user_model.dart
│       │   └── repositories/
│       │       └── auth_repository_impl.dart
│       ├── domain/
│       │   ├── entities/
│       │   │   └── user.dart
│       │   ├── repositories/
│       │   │   └── auth_repository.dart
│       │   └── usecases/
│       │       ├── login_user.dart
│       │       ├── logout_user.dart
│       │       └── get_current_user.dart
│       └── presentation/
│           ├── bloc/
│           │   ├── auth_bloc.dart
│           │   ├── auth_event.dart
│           │   └── auth_state.dart
│           ├── pages/
│           │   ├── login_page.dart
│           │   └── register_page.dart
│           └── widgets/
│               ├── login_form.dart
│               └── social_login_buttons.dart
└── shared/
    └── widgets/
```

## Layer responsibilities

### Presentation

Contains:

- Pages/screens
- Widgets
- Bloc/Cubit/ViewModel/Provider controllers
- UI state
- Form state
- Navigation triggers

Does not contain:

- API calls
- SQL/Firebase queries
- JSON parsing
- Token storage
- Business rules

### Domain

Contains:

- Entities
- Repository interfaces
- UseCases
- Business rules
- Value objects

Does not contain:

- Flutter imports
- HTTP/Firebase/local database code
- JSON serialization
- UI state classes

### Data

Contains:

- API clients/data sources
- Firebase services
- Local storage sources
- Models with `fromJson`/`toJson`
- Repository implementations

Does not contain:

- Widgets
- BuildContext
- UI state

### Core

Contains shared, app-wide utilities:

- Errors/failures
- Network info
- API client
- Theme
- Constants
- Shared widgets
- Validators
- Base usecase/result types

Keep `core` lean. If something is only used by one feature, keep it inside that feature.

## Feature-first vs layer-first

Prefer:

```text
features/auth/{data,domain,presentation}
```

Instead of:

```text
data/auth
domain/auth
presentation/auth
```

Feature-first scales better because teams can own features and features can be added/removed with fewer conflicts.

## Pragmatic simplification

Do not over-engineer.

- For simple CRUD screens, a repository + controller may be enough.
- For very small apps, skip strict use cases.
- For complex apps, keep usecases.
- For client projects, consistency matters more than theoretical purity.
