from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent

DIRECTORIES = (
    "data",
    "scripts",
    "src/shopping_agent",
    "src/shopping_agent/prompts",
    "src/shopping_agent/content_understanding",
    "src/shopping_agent/catalog",
    "src/shopping_agent/retrieval",
    "src/shopping_agent/tools",
    "src/shopping_agent/observability",
)

FILES = (
    # Root files
    "pyproject.toml",
    ".env.example",
    ".gitignore",
    "README.md",

    # Application
    "src/shopping_agent/__init__.py",
    "src/shopping_agent/app.py",
    "src/shopping_agent/agent.py",
    "src/shopping_agent/config.py",
    "src/shopping_agent/schemas.py",
    "src/shopping_agent/prompts/shopping_agent.md",

    # Azure Content Understanding pre-analysis
    "src/shopping_agent/content_understanding/__init__.py",
    "src/shopping_agent/content_understanding/analyzer_definition.py",
    "src/shopping_agent/content_understanding/image_analyzer.py",

    # MySQL catalogue and Qdrant indexing
    "src/shopping_agent/catalog/__init__.py",
    "src/shopping_agent/catalog/mysql_repository.py",
    "src/shopping_agent/catalog/product_mapper.py",
    "src/shopping_agent/catalog/indexer.py",

    # Hybrid retrieval
    "src/shopping_agent/retrieval/__init__.py",
    "src/shopping_agent/retrieval/encoders.py",
    "src/shopping_agent/retrieval/qdrant_store.py",
    "src/shopping_agent/retrieval/hybrid_search.py",
    "src/shopping_agent/retrieval/reranker.py",

    # Agent tools
    "src/shopping_agent/tools/__init__.py",
    "src/shopping_agent/tools/search_products.py",

    # OpenTelemetry and Azure Application Insights
    "src/shopping_agent/observability/__init__.py",
    "src/shopping_agent/observability/telemetry.py",

    # Commands
    "scripts/create_analyzer.py",
    "scripts/rebuild_index.py",
    "scripts/run_local.py",

    # Generated catalogue snapshot
    "data/.gitkeep",
)


def safe_path(relative_path: str) -> Path:
    root = PROJECT_ROOT.resolve()
    path = (root / relative_path).resolve(strict=False)

    try:
        path.relative_to(root)
    except ValueError as exc:
        raise ValueError(
            f"Path is outside the project: {relative_path}"
        ) from exc

    return path


def main() -> None:
    created: list[str] = []
    skipped: list[str] = []

    for directory in DIRECTORIES:
        path = safe_path(directory)

        if path.exists():
            if not path.is_dir():
                raise FileExistsError(
                    f"Expected directory but found file: {path}"
                )
            skipped.append(directory)
            continue

        path.mkdir(parents=True)
        created.append(directory)

    for filename in FILES:
        path = safe_path(filename)

        if path.exists():
            if not path.is_file():
                raise FileExistsError(
                    f"Expected file but found directory: {path}"
                )
            skipped.append(filename)
            continue

        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=False)
        created.append(filename)

    print(f"Created: {len(created)}")
    print(f"Skipped existing: {len(skipped)}")
    print("Existing files were not overwritten.")


if __name__ == "__main__":
    main()