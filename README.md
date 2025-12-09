# Cyber Compass Documentation

This repository contains the source code for the Cyber Compass documentation site. The documentation is built with [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

## Hosting

The documentation is automatically built and hosted on [ReadTheDocs](https://readthedocs.org/).

## Development

This project uses [`uv`](https://github.com/astral-sh/uv) for dependency management.

### Prerequisites

- Python 3.13+
- `uv`

### Setup

Clone the repository and install dependencies:

```bash
uv sync
```

### Running Locally

To preview the documentation with hot-reloading:

```bash
uv run mkdocs serve
```

The site will be available at `http://127.0.0.1:8000/`.

### Building

To build the static site:

```bash
uv run mkdocs build
```

The output will be in the `site/` directory.

## Contributing

1.  Create a new branch for your changes.
2.  Make your edits in the `docs/` directory.
3.  Preview your changes locally using `uv run mkdocs serve`.
4.  Submit a Pull Request.
