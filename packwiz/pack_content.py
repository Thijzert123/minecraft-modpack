# if none are set, everything is included
# include: ONLY use this project for these versions
# exclude: use this project for all versions EXCEPT for these
# include and exclude can't be used at the same time
#
# force-versions: force download this modrinth url version for speicific mc version (see example for sodium)


# EXAMPLE FILE:

{
    "mods": [ # you don't have to sort everything correctly under mods, shaderpacks and resourcepacks, it is just for your convenience
        {"id": "yosbr", # use the Modrinth project ID
            "force-versions": {
                "1.21.5": "KMOzdYko" # use the version ID
        }},
        {"id": "eating-animation",
            "include": ["1.20.1", "1.20.4", "1.21.1", "1.21.3"]}, # only add eating-animation to these versions
        {"id": "sound",
            "exclude": ["1.21.4", "1.21.5"] # don't add sound to these versions
        }],
    "shaderpacks": [
        {"id": "makeup-ultra-fast-shaders"},
        {"id": "super-duper-vanilla"}],
    "resourcepacks": [
        {"id": "default-splashes"},
        {"id": "mace-but-3d-resourcepack",
            "exclude": ["1.20.1", "1.20.4", "1.21.1", "1.21.3"]}
    ]
}
