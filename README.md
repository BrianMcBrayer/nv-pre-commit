# nv-pre-commit-hooks

Some NVIDIA specific hooks for pre-commit.

### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
- repo: https://github.com/tuttlebr/nv-pre-commit
  rev: v0.0.3 # Use the ref you want to point at
  hooks:
    - id: detect-nv-keys
  # -   id: ...
```

### Hooks available

#### `detect-nv-keys`

Checks for the existence of private keys.

### Local development

- Create virtual environment and activate it
- Run `pip install -e .[test]`
- Run `pre-commit run` (may take a few minutes)
