# nv-pre-commit-hooks

Some NVIDIA specific hooks for pre-commit.

### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.6.0 # Use the ref you want to point at
  hooks:
    - id: detect-nv-keys
  # -   id: ...
```

### Hooks available

#### `detect-nv-keys`

Checks for the existence of private keys.
