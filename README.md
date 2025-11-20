# ModKickstart

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

ModKickstart is a small Python tool that quickly generates the basic folder structure and starter files for a new Minecraft Forge mod. Perfect for getting started fast without setting up everything manually.

## Features

- Creates main mod class file  
- Creates an example item class  
- Generates necessary `resources` folders  
- Adds a basic `mods.toml`  
- Adds a simple `en_us.json` language file for the item  

## Usage

1. Make sure Python 3.x is installed on your system.  
2. Clone the repo or download the files:

    git clone https://github.com/TheCatsApplelol/ModKickstart.git
    cd ModKickstart

3. Run the script:

    python modkickstart.py

4. Enter your mod name and mod id when prompted.  
5. The script will create a folder `{mod_id}_mod` with all starter files ready.  
6. Open the folder in your IDE (IntelliJ, Eclipse, etc.) and start coding your mod.

## Notes

- Mod id must be lowercase and contain no spaces.  
- The example item is just a placeholder. You can delete or modify it.  
- Currently built for Forge mods. NeoForge or other platforms require extra tweaks.

## License

MIT License
