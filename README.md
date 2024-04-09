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

## FAQ

What image files will get converted?

[This line](https://github.com/ericmjl/webp-pre-commit/blob/main/webp_hook/cli.py#L14) in the source code tells it all. (I don't want information to go stale, so I don't duplicate it here.)
