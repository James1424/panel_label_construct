from src.get_holdings_universe import build_seed_universe
from src.build_panel import build_panel
from src.update_readme import main as update_readme
import subprocess
import sys

if __name__ == "__main__":
    build_seed_universe()
    subprocess.check_call([sys.executable, "-m", "src.download_data"])
    build_panel()
    update_readme()
