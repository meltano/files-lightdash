# files-lightdash

Meltano project [file bundle](https://docs.meltano.com/concepts/plugins#file-bundles) for [lightdash](https://www.lightdash.com/).

Files:
- [`analysis/lightdash/README.md`](./bundle/analysis/lightdash/README.md) instructions for getting started with Lightdash.
- [`analysis/lightdash/docker-compose.yml`](./bundle/analysis/lightdash/docker-compose.yml) the docker-compose file for starting up Lightdash running in Docker containers.

See [setup.py](./setup.py) for the full list of bundled files.

## Installation

To install Lightdash into your Meltano project you need to use a `custom` file bundle, soon it will be part of Meltano and the following custom installation details will not be needed, just `meltano add files lightdash`.

Until then we will install it as a custom bundle, run:

`meltano add --custom files lightdash`

Follow the prompts as shown below, entering the pip_url when prompted:

```bash
# Adding new custom file bundle with name 'lightdash'...
# 
# Specify the plugin's namespace, which will serve as the:
# - identifier to find related/compatible plugins
# 
# Hit Return to accept the default: plugin name with underscores instead of dashes

(namespace) [lightdash]: 

# Specify the plugin's `pip install` argument, for example:
# - PyPI package name:
#         lightdash
# - Git repository URL:
#         git+https://gitlab.com/meltano/lightdash.git
# - local directory, in editable/development mode:
#         -e extract/lightdash
# - 'n' if using a local executable (nothing to install)
# 
# Default: plugin name as PyPI package name

(pip_url) [lightdash]: git+https://gitlab.com/meltano/files-lightdash.git

# Specify the plugin's executable name
# 
# Default: name derived from `pip_url`

(executable) [files-lightdash]: 
# Adding file bundle 'lightdash' to your Meltano project...
# 
# Installing file bundle 'lightdash'...
```

Add the following utility configs to your meltano.yml file under the `plugins` key.
This will soon be added to Meltano so these configs will be added automatically using `meltano add utility lightdash`, but for now its manual.

```yaml
plugins:
  utilities:
  - name: lightdash
    namespace: lightdash
    commands:
      up:
        executable: /usr/local/bin/docker
        args: compose -f analysis/lightdash/docker-compose.yml up lightdash
      down:
        executable: /usr/local/bin/docker
        args: compose -f analysis/lightdash/docker-compose.yml down
    settings:
      - name: pgpassword
        kind: password
      - name: secret
        kind: password
      - name: pghost
      - name: pgport
        value: 5432
      - name: pguser
      - name: pgdatabase
      - name: dbt_project_dir
        value: "../../transform"
      - name: dbt_target_dir
        value: "../../.meltano/transformers/dbt/target"
```

## Configuration

Lightdash needs a backend postgres database to store application data, you can either let Lightdash spin up its own Postgres container automatically or you can pass it credentials to connect to an existing instance.
If you already have a Postgres instance running locally on 5432 the automatically created Postgres instance will fail to startup.
Either change the default ports or let Lightdash share your instance by providing it an empty database to connect to.

#### Existing Postgres Instance

For configuring Lightdash to use your existing running postgres instance you need to set the following configurations:

```bash
meltano config lightdash set secret "not very secret"
meltano config lightdash set pgpassword meltano
meltano config lightdash set pguser meltano
# Assuming postgres is running in a docker container not directly accessible to Lightdash, otherwise `localhost` is appropriate
meltano config lightdash set pghost host.docker.internal
# Lightdash will not create the database for you. Create it if it does not exist.
meltano config lightdash set pgdatabase lightdash
```

Lastly, invoke the UI only using `meltano invoke lightdash:up --no-deps` and navigate to http://localhost:5000 to begin registration and setup.

#### Automatically Create Local Postgres Instance For Me

Alternatively without any additional configuration you can run `meltano invoke lightdash:up` to have it automatically spin up its own Postgres instance and the UI.
Then navigate to http://localhost:5000 to begin registration and setup.


# Pro Tips and Troubleshooting

Lightdash reads your dbt target directory in order to retrieve metadata, so if you are having issues you can try running:

```
meltano invoke dbt:clean
meltano invoke dbt:compile
```

This will clean the target directory and recompile the artifacts, using the Lightdash "Refresh dbt" button in the Explore page.
