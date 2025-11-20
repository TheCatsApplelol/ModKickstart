import os

mod_name = input("mod name: ")
mod_id = input("mod id (no spaces, lowercase): ")

base = f"{mod_id}_mod"
os.makedirs(base, exist_ok=True)
os.makedirs(os.path.join(base, "src", "main", "java", mod_id), exist_ok=True)
os.makedirs(os.path.join(base, "src", "main", "resources", "assets", mod_id, "textures", "item"), exist_ok=True)
os.makedirs(os.path.join(base, "src", "main", "resources", "assets", mod_id, "lang"), exist_ok=True)
os.makedirs(os.path.join(base, "src", "main", "resources", "META-INF"), exist_ok=True)

main_class = f"""package {mod_id};

import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;

@Mod("{mod_id}")
public class {mod_name.replace(' ', '')} {{
    public {mod_name.replace(' ', '')}() {{
        FMLJavaModLoadingContext.get().getModEventBus().addListener(this::setup);
        FMLJavaModLoadingContext.get().getModEventBus().addListener(this::doClientStuff);
    }}

    private void setup(final FMLCommonSetupEvent event) {{}}

    private void doClientStuff(final FMLClientSetupEvent event) {{}}
}}
"""

item_class = f"""package {mod_id};

import net.minecraft.world.item.Item;
import net.minecraft.world.item.Item.Properties;

public class ExampleItem extends Item {{
    public ExampleItem() {{
        super(new Properties().tab(null));
    }}
}}
"""

with open(os.path.join(base, "src", "main", "java", mod_id, f"{mod_name.replace(' ', '')}.java"), "w") as f:
    f.write(main_class)

with open(os.path.join(base, "src", "main", "java", mod_id, "ExampleItem.java"), "w") as f:
    f.write(item_class)

with open(os.path.join(base, "src", "main", "resources", "META-INF", "mods.toml"), "w") as f:
    f.write(f"modLoader=\"javafml\"\nloaderVersion=\"[44,)\"\nminecraftVersion=\"1.19.2\"\nmodId=\"{mod_id}\"\nversion=\"1.0.0\"")

with open(os.path.join(base, "src", "main", "resources", "assets", mod_id, "lang", "en_us.json"), "w") as f:
    f.write('{\n  "item.' + mod_id + '.example_item": "Example Item"\n}')

print(f"{mod_name} basic mod structure created in {base}")
