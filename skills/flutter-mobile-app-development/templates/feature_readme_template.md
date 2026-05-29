# {{feature_name}} Feature

## Purpose

Describe what this feature does.

## Folder map

```text
{{feature_name}}/
├── data/
│   ├── datasources/
│   ├── models/
│   └── repositories/
├── domain/
│   ├── entities/
│   ├── repositories/
│   └── usecases/
└── presentation/
    ├── bloc/ or cubit/ or providers/ or view_models/
    ├── pages/
    └── widgets/
```

## Data flow

```text
Page -> Controller/Bloc/Cubit -> UseCase -> Repository Interface -> Repository Impl -> DataSource
```

## States to implement

- Initial
- Loading
- Success
- Empty
- Error
