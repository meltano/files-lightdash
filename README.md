# files-lightdash

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) for [lightdash](https://www.lightdash.com/).

Files:
- [`analysis/lightdash/README.md`](./bundle/analysis/lightdash/README.md) instructions for getting started with Lightdash.

See [setup.py](./setup.py)) for the full list of bundled files.

## Installation

Automated installation is not yet available.

To manually install, first add the below or append to the `utilities:` section of your `meltano.yml` file

```yml
  utilities:
  - name: lightdash
    namespace: lightdash
    pip_url: git+https://gitlab.com/meltano/files-lightdash.git
    # TODO: Investigate why `docker` alone does not resolve
    # executable: /usr/local/bin/docker
    # args doesn't appear to be supported at the top level:
    # args: compose -f analysis/lightdash/dev/docker-compose.yml up
    commands:
      # meltano invoke lightdash:ui
      ui:
        # TODO: Investigate why `docker` alone does not resolve from PATH
        executable: /usr/local/bin/docker
        args: compose -f analysis/lightdash/docker-compose.yml up
```

Next, run `meltano install utility lightdash`.

Lastly, invoke via `meltano invoke lightdash:ui`
