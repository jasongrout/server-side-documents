# server-side-documents

## Documentation

The documentation is a Sphinx site written in Markdown (MyST), with the API
reference rendered from `ssd-execute-openapi.yaml`. It is built with
[pixi](https://pixi.sh):

```bash
pixi run docs
```

The site is written to `docs/_build/html`. To lint the OpenAPI spec with
Redocly:

```bash
pixi run lint
```
