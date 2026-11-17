# Server-side Documents

> **Motivation**
> Users should be able to close or reload a browser tab without losing access to outputs from an ongoing computation, but browser-dependent output handling has made this a longstanding challenge ([notebook#641](https://github.com/jupyter/notebook/issues/641)).
> Supporting collaborative editing or agents and other tools that work with notebooks independently of the browser adds to the need for a shared server-side foundation.

We plan to move notebook document state to the server using CRDT-backed documents and making server-side execution a core API of `jupyter-server` and `jupyverse`.
This will provide a shared foundation for reliable notebook execution and output recovery for browser clients, agents, and other tools, without requiring an open browser.
Building on existing work across the Jupyter ecosystem, we will focus the next 2-3 months on collaborative design and implementation.

The API will initially be experimental, but reliability and protection against data loss are essential from the outset.
Moving beyond experimental status will depend on demonstrated reliability against explicit criteria for document persistence, synchronization, execution, and recovery.
We plan to build on the extensive Playwright test suite being developed by Zach Sailer and colleagues at Apple, which they plan to open-source for community development and maintenance.

We commit to working collaboratively and in public.
Specifically, we will:

- Jointly author a JEP describing the proposed architecture, API, compatibility requirements, and implementation plan.
- Open a coordinating meta-issue on `jupyter-server` and conduct design and implementation work in public repositories and issues.
- Develop and maintain shared tests, document known limitations, and establish criteria for moving the API out of experimental status.
- Hold weekly developer meetings for design discussions, PR triage and review, and roadmap updates, with decisions and open questions recorded publicly.
- Report progress and solicit feedback at the weekly Jupyter Contributor Meeting.
- Welcome additional contributors and revise the plan in response to community feedback.

Initial contributors will include @jtpio, @davidbrochart, @sylvaincorlay, @zsailer, @minrk, @jarrodmillman, @jasongrout, and @krassowski, with contributions spanning design, implementation, testing, review, and coordination. Additional contributors are welcome.

Detailed technical discussions and decisions will proceed through the public JEP and the relevant projects' public review processes.

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
