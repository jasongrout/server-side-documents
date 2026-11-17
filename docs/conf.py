from pathlib import Path

import yaml

project = "Server-side Documents"
copyright = "2026, Jupyter Development Team"
author = "Jupyter Development Team"

extensions = [
    "myst_parser",
    "sphinxcontrib.httpdomain",
    "sphinxcontrib.openapi",
]

myst_enable_extensions = [
    "attrs_inline",
    "colon_fence",
    "substitution",
]

exclude_patterns = ["_build"]

# Same theme and options as the jupyter_server documentation.
html_theme = "pydata_sphinx_theme"
# The default "<project> documentation" overlaps the navbar links.
html_title = project
# All pages are top-level (shown in the navbar), so the section navigation
# sidebar would be empty. Remove this once pages have subpages.
html_sidebars = {"**": []}
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/jupyter-server/server-side-documents",
            "icon": "fa-brands fa-github",
        }
    ],
    "navigation_with_keys": False,
    "use_edit_page_button": True,
}
# Used by the "Edit on GitHub" button.
html_context = {
    "github_user": "jupyter-server",
    "github_repo": "server-side-documents",
    "github_version": "main",
    "doc_path": "docs",
}

# Use the newer renderer: it lists request body fields with types and
# "required". The default ("httpdomain:old") does not.
openapi_default_renderer = "httpdomain"

# sphinxcontrib-openapi renders paths only, not the spec's `info` block, so
# expose the description for use as {{ api_description }} in Markdown pages.
_spec = yaml.safe_load(
    (Path(__file__).parent.parent / "ssd-execute-openapi.yaml").read_text()
)
myst_substitutions = {
    "api_title": _spec["info"]["title"],
    "api_version": _spec["info"]["version"],
    "api_description": _spec["info"].get("description", ""),
}
