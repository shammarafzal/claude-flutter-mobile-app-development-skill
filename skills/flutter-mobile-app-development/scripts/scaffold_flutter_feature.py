#!/usr/bin/env python3
"""
Scaffold a feature-first Clean Architecture folder structure for a Flutter app.

Usage:
  python scripts/scaffold_flutter_feature.py auth
  python scripts/scaffold_flutter_feature.py orders --state cubit
  python scripts/scaffold_flutter_feature.py profile --state riverpod
"""

from __future__ import annotations

import argparse
from pathlib import Path


def snake(name: str) -> str:
    return name.strip().lower().replace("-", "_").replace(" ", "_")


def pascal(name: str) -> str:
    return "".join(part.capitalize() for part in snake(name).split("_"))


def write(path: Path, content: str, force: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        print(f"skip existing: {path}")
        return
    path.write_text(content, encoding="utf-8")
    print(f"created: {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("feature", help="Feature name, for example auth or orders")
    parser.add_argument(
        "--state",
        choices=["bloc", "cubit", "riverpod", "view_model"],
        default="cubit",
        help="Presentation state-management folder/template",
    )
    parser.add_argument("--lib", default="lib", help="Path to Flutter lib folder")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    feature = snake(args.feature)
    class_name = pascal(feature)
    base = Path(args.lib) / "features" / feature

    dirs = [
        "data/datasources",
        "data/models",
        "data/repositories",
        "domain/entities",
        "domain/repositories",
        "domain/usecases",
        f"presentation/{args.state}",
        "presentation/pages",
        "presentation/widgets",
    ]

    for d in dirs:
        (base / d).mkdir(parents=True, exist_ok=True)
        print(f"dir: {base / d}")

    write(
        base / "domain" / "entities" / f"{feature}.dart",
        f"""class {class_name} {{
  const {class_name}({{
    required this.id,
  }});

  final String id;
}}
""",
        args.force,
    )

    write(
        base / "domain" / "repositories" / f"{feature}_repository.dart",
        f"""import '../entities/{feature}.dart';

abstract class {class_name}Repository {{
  Future<List<{class_name}>> get{class_name}List();
}}
""",
        args.force,
    )

    write(
        base / "domain" / "usecases" / f"get_{feature}_list.dart",
        f"""import '../entities/{feature}.dart';
import '../repositories/{feature}_repository.dart';

class Get{class_name}List {{
  const Get{class_name}List(this.repository);

  final {class_name}Repository repository;

  Future<List<{class_name}>> call() {{
    return repository.get{class_name}List();
  }}
}}
""",
        args.force,
    )

    write(
        base / "data" / "models" / f"{feature}_model.dart",
        f"""import '../../domain/entities/{feature}.dart';

class {class_name}Model extends {class_name} {{
  const {class_name}Model({{
    required super.id,
  }});

  factory {class_name}Model.fromJson(Map<String, dynamic> json) {{
    return {class_name}Model(
      id: json['id'].toString(),
    );
  }}

  Map<String, dynamic> toJson() {{
    return {{
      'id': id,
    }};
  }}
}}
""",
        args.force,
    )

    write(
        base / "data" / "datasources" / f"{feature}_remote_data_source.dart",
        f"""import '../models/{feature}_model.dart';

abstract class {class_name}RemoteDataSource {{
  Future<List<{class_name}Model>> get{class_name}List();
}}

class {class_name}RemoteDataSourceImpl implements {class_name}RemoteDataSource {{
  @override
  Future<List<{class_name}Model>> get{class_name}List() async {{
    // TODO: Replace with API/Firebase implementation.
    return const [];
  }}
}}
""",
        args.force,
    )

    write(
        base / "data" / "repositories" / f"{feature}_repository_impl.dart",
        f"""import '../../domain/entities/{feature}.dart';
import '../../domain/repositories/{feature}_repository.dart';
import '../datasources/{feature}_remote_data_source.dart';

class {class_name}RepositoryImpl implements {class_name}Repository {{
  const {class_name}RepositoryImpl({{
    required this.remoteDataSource,
  }});

  final {class_name}RemoteDataSource remoteDataSource;

  @override
  Future<List<{class_name}>> get{class_name}List() {{
    return remoteDataSource.get{class_name}List();
  }}
}}
""",
        args.force,
    )

    state_dir = base / "presentation" / args.state
    if args.state == "cubit":
        write(
            state_dir / f"{feature}_state.dart",
            f"""sealed class {class_name}State {{
  const {class_name}State();
}}

class {class_name}Initial extends {class_name}State {{
  const {class_name}Initial();
}}

class {class_name}Loading extends {class_name}State {{
  const {class_name}Loading();
}}

class {class_name}Loaded extends {class_name}State {{
  const {class_name}Loaded();
}}

class {class_name}Error extends {class_name}State {{
  const {class_name}Error(this.message);

  final String message;
}}
""",
            args.force,
        )
        write(
            state_dir / f"{feature}_cubit.dart",
            f"""import 'package:flutter_bloc/flutter_bloc.dart';

import '../../domain/usecases/get_{feature}_list.dart';
import '{feature}_state.dart';

class {class_name}Cubit extends Cubit<{class_name}State> {{
  {class_name}Cubit({{
    required this.get{class_name}List,
  }}) : super(const {class_name}Initial());

  final Get{class_name}List get{class_name}List;

  Future<void> load() async {{
    emit(const {class_name}Loading());

    try {{
      await get{class_name}List();
      emit(const {class_name}Loaded());
    }} catch (error) {{
      emit({class_name}Error(error.toString()));
    }}
  }}
}}
""",
            args.force,
        )

    write(
        base / "presentation" / "pages" / f"{feature}_page.dart",
        f"""import 'package:flutter/material.dart';

class {class_name}Page extends StatelessWidget {{
  const {class_name}Page({{super.key}});

  @override
  Widget build(BuildContext context) {{
    return const Scaffold(
      body: SafeArea(
        child: Center(
          child: Text('{class_name} Page'),
        ),
      ),
    );
  }}
}}
""",
        args.force,
    )


if __name__ == "__main__":
    main()
