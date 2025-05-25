# Minecraft Modpack

This template gives you everything to create your own Minecraft Modrinth modpack, including scripts to minimalize the things you have to do yourself!

## Things you need to change
### `packwiz/pack_content.py`
Add or remove projects to your modpack here. For more information, see the comments in the file.

### `packwiz/generate_modrinth_project_list.py`
Change the `CLIENT_PLUS_ID` field at the top of the file to a string of the ID of your Modrinth modpack.

### `packwiz/generate_packwiz_project_list.py`
Add strings of the Minecraft versions your modpack supports (1.20.1, 1.21.5, etc.) to the `SUPPORTED_MC_VERSIONS` list at the top of the file.

### `packwiz/mcX.X.X`
You can make your modpack for multiple Minecraft versions. They are loacated in different directories in this format: `mcX.X.X` (replace `X.X.X` with the Minecraft version). Note that the directory names have to start with `mc`.

### `packwiz/mcX.X.X/pack.toml`
Change the `name`, `author`, `version` `fabric` and `minecraft` fields to what you want. You can also add strings to the `acceptable-game-versions` list. When you do this, packwiz (the modpack manager) will know that these additional Minecraft versions are also acceptable to add to you modpack.

## After you have changed everything
- Read how to use packwiz and the included scripts in `packwiz/README.md`.
