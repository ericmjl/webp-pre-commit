# webp-precommit

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
