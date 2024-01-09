# OpenComputers Controller

OpenComputers Controller is a program that controls in-game drones with a USB controller. Right now this is for the hell of it but if I ever find a practical use for this in-game I'll add it here if I remember to (spoiler: I won't.)

## Server Installation

### Pre-Built Installation

Executables built with pyinstaller are available on the releases page

### Manual Installation

  - Clone the repository to your install location of choice.
  - Install poetry with `pip install -r requirements.txt`
  - Install project dependencies with `poetry install`
  - Start the server with `python -m server`

## Client Installation

#### TL;DR: 
  On a computer with an internet card, `oppm` installed, and your EEPROM of choice inserted, run
  `oppm install crunch && wget -f https://raw.githubusercontent.com/quinn-n/OpenComputers_Controller/master/Clients/dronecontroller.lua && crunch dronecontroller.lua dronecontroller.cr.lua && flash -q dronecontroller.cr.lua DroneController`. Then insert the EEPROM into your drone of choice.

The client is an [OpenComputers] drone. If you don't know, [OpenComputers] is a Minecraft mod that adds different types of programmable computers to the game. This installation guide assumes you have at least some passing familiarity with the drones, or can use your search engine of choice to figure out what you don't know.

The easiest way to get the client code onto a computer is to use the built-in `wget` command and an internet card. `wget https://raw.githubusercontent.com/quinn-n/OpenComputers_Controller/master/Clients/dronecontroller.lua`

You will have to update the `SERVER_URL` constant if your control server is running on something other than `localhost`

If your control server is running on `localhost`, you will have to go into the mod's config at `$MINECRAFT_HOME/config/opencomputers/settings.conf` and allow connections to the local network by changing `deny private` in `filteringRules` to `allow private`.

There are 4KiB of storage available on the EEPROMs used to program the drones. The [client](./Clients/dronecontroller.lua) is about 7KiB so it has to be minified. I recommend using [Crunch] which can be installed in-game with `oppm install crunch`, and ran using `crunch dronecontroller.lua`. This should auto-output the crunched file to `dronecontroller.cr.lua`. If this for some reason is still not small enough (it should be), you can also enable LZ77 compression with `--lz77`.

After that all you have to do is flash the code to an EEPROM using `flash dronecontroller.cr.lua DroneController`, craft the drone with the EEPROM to "insert" it, and turn it on.

## Licencing

This project is licenced under the [WTFPL].

[OpenComputers]: https://www.curseforge.com/minecraft/mc-mods/opencomputers
[Crunch]: https://oc.cil.li/topic/511-crunch-break-the-4k-limit/
[WTFPL]: http://www.wtfpl.net/about/
