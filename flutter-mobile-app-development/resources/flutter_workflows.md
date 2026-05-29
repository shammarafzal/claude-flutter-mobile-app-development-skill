# Flutter Mobile App Development Workflows

## New app planning workflow

When the user describes an app idea, output:

```text
App summary
Target users
Core features
Screen list
Recommended stack
Backend/data model
Folder structure
Milestones
First files to create
Risks/questions
```

## Screen/UI implementation workflow

1. Define the screen purpose.
2. Identify static vs dynamic content.
3. Define states:
   - initial
   - loading
   - success
   - empty
   - error
4. Create reusable widgets.
5. Apply responsive constraints.
6. Add navigation actions.
7. Add mock data when backend is missing.

## Feature implementation workflow

For a feature named `orders`, create:

```text
features/orders/
├── data/
│   ├── datasources/orders_remote_data_source.dart
│   ├── models/order_model.dart
│   └── repositories/orders_repository_impl.dart
├── domain/
│   ├── entities/order.dart
│   ├── repositories/orders_repository.dart
│   └── usecases/get_orders.dart
└── presentation/
    ├── bloc/orders_bloc.dart
    ├── bloc/orders_event.dart
    ├── bloc/orders_state.dart
    ├── pages/orders_page.dart
    └── widgets/order_card.dart
```

## Debugging workflow

For errors:

1. Quote or summarize the exact error.
2. Explain root cause in simple language.
3. Show the minimum fix.
4. Show the corrected full snippet.
5. Mention how to prevent it.

## Responsive UI workflow

For every screen:

- Wrap page body in `SafeArea` when needed.
- Use `SingleChildScrollView` for forms or long content.
- Avoid `Expanded` inside unbounded scrollables.
- Use `LayoutBuilder` for breakpoint decisions.
- Use `Wrap` for chips/buttons that may overflow.
- Use `Flexible` for long text in rows.
- Test at small phone, normal phone, and tablet widths.

## Testing workflow

Minimum tests for production:

- Unit tests for usecases and repositories
- Widget tests for important screens/components
- Integration tests for critical flows:
  - login
  - checkout
  - booking
  - order tracking
  - onboarding
