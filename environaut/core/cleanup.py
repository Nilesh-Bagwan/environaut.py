import shutil
import sys
from pathlib import Path
from environaut.core.utils import is_in_virtualenv

def cleanup_env(current_dir: Path) -> None:
    if is_in_virtualenv():
        print("⚠️ You are currently inside a virtual environment.")
        print("🚫 Please deactivate it first using `deactivate` before deleting.")
        return

    env_name = input("Enter the name of the virtual environment to delete: ").strip()

    if not env_name:
        print("❌ No environment name provided. Exiting.")
        sys.exit(1)

    env_path = current_dir / env_name

    if not env_path.exists():
        print(f"❌ Virtual environment '{env_path}' does not exist.")
        return

    confirm = input(f"⚠️ Are you sure you want to delete the environment '{env_name}'? (y/n): ").strip().lower()
    if confirm == "y":
        try:
            shutil.rmtree(env_path)
            print(f"✅ Deleted virtual environment '{env_name}'")
        except Exception as e:
            print(f"❌ Failed to delete: {e}")
    else:
        print("❎ Deletion cancelled.")
