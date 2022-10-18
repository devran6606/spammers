import glob
from pathlib import Path
from ANKIT.utils import load_plugins
import logging
from . import worker


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "ANKIT/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("başarıyla dağıtıldı")
print("Bu bot Affetmez tarafından geliştirilmiştir")
if __name__ == "__main__":
    worker.run_until_disconnected()
