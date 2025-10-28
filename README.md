# webp-precommit

[![CI](https://github.com/ericmjl/webp-pre-commit/workflows/CI/badge.svg)](https://github.com/ericmjl/webp-pre-commit/actions)
[![codecov](https://codecov.io/gh/ericmjl/webp-pre-commit/branch/main/graph/badge.svg)](https://codecov.io/gh/ericmjl/webp-pre-commit)

Automatically convert image files in your repo to `.webp` format.

## Usage

Use this with the `pre-commit` framework by adding the following to your `.pre-commit-config.yaml` file:

```yaml
  - repo: https://github.com/ericmjl/webp-pre-commit
    rev: v0.0.8
    hooks:
      - id: convert-to-webp
```

To ensure that you have the latest tagged version, you can either:

- Run `pre-commit autoupdate` to auto-update all of the pre-commit hooks (recommended), or
- Manually change the `rev` to the latest tagged release on GitHub.

## Development

This project uses modern Python tooling:

- **Testing**: pytest with coverage reporting
- **Code formatting**: Black
- **Linting**: Ruff
- **Documentation**: Interrogate for docstring coverage
- **CI/CD**: GitHub Actions for testing across Python 3.9-3.13
- **Package management**: uv for fast dependency resolution

### Running tests locally

```bash
# Install dependencies
uv sync --dev

# Run tests
uv run pytest tests/ -v

# Run linting
uv run ruff check .
uv run black --check .
uv run interrogate webp_hook/ --fail-under=100
```

## FAQ

What image files will get converted?

[This line](https://github.com/ericmjl/webp-pre-commit/blob/main/webp_hook/cli.py#L16) in the source code tells it all. (I don't want information to go stale, so I don't duplicate it here.)
