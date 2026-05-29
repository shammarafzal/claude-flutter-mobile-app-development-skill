# Flutter App Review Checklist

## Architecture

- [ ] Feature-first structure is consistent.
- [ ] Presentation does not call APIs directly.
- [ ] Domain has no Flutter imports.
- [ ] Data layer handles external services.
- [ ] Repository boundaries are clear.
- [ ] UseCases are not oversized.
- [ ] Core folder is not a dumping ground.

## Code quality

- [ ] Dart analyzer passes.
- [ ] `dart format` applied.
- [ ] `const` used where possible.
- [ ] No large god widgets.
- [ ] No duplicated business logic.
- [ ] Meaningful names used.
- [ ] Null safety handled correctly.

## UI/UX

- [ ] No overflow on small screens.
- [ ] Works on common phone sizes.
- [ ] SafeArea used where needed.
- [ ] Tap targets are comfortable.
- [ ] Empty states exist.
- [ ] Error states exist.
- [ ] Loading states exist.
- [ ] Forms validate input clearly.

## State management

- [ ] State is not mixed with UI rendering.
- [ ] Async states are represented clearly.
- [ ] Controllers/ViewModels/Blocs are testable.
- [ ] No unnecessary rebuilds.

## API/security

- [ ] No secrets in Flutter code.
- [ ] Auth token logic is centralized.
- [ ] 401/unauthorized handled.
- [ ] Timeouts handled.
- [ ] Validation errors shown properly.
- [ ] Payment secrets stay on backend.

## Performance

- [ ] Lists use builders.
- [ ] Heavy work is not done in `build`.
- [ ] Images are optimized/cached as needed.
- [ ] Avoids unnecessary full-screen rebuilds.

## Testing/release

- [ ] Unit tests for business logic.
- [ ] Widget tests for key components.
- [ ] Critical flows tested manually or with integration tests.
- [ ] Release build tested on real devices.
- [ ] Store readiness checklist complete.
