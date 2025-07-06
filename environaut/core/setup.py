import os
import subprocess
import venv
from pathlib import Path
from typing import Optional, List

from environaut.core.utils import is_file_nonempty

def get_venv_name() -> str:
    default_name = "venv"
    env_name = input(f"Enter a name for the virtual environment [{default_name}]: ").strip()
    return env_name if env_name else default_name

def create_virtual_env(env_path: Path) -> None:
    print(f"📦 Creating virtual environment at '{env_path}'...")
    venv.create(env_path, with_pip=True)
    print("✅ Virtual environment created.")

def install_dependencies(env_path: Path, requirements_file: Optional[Path], packages: Optional[List[str]]) -> None:
    pip_path = env_path / ("Scripts" if os.name == "nt" else "bin") / "pip"

    if requirements_file and is_file_nonempty(requirements_file):
        print(f"📜 Installing dependencies from '{requirements_file}'...")
        subprocess.check_call([str(pip_path), "install", "-r", str(requirements_file)])
    elif packages and len(packages) > 0:
        print(f"📦 Installing default packages: {packages}")
        subprocess.check_call([str(pip_path), "install", *packages])
    else:
        print("⚠️ No dependencies to install.")

def setup_env(default_packages: List[str]) -> None:
    current_dir = Path.cwd()
    env_name = get_venv_name()
    env_path = current_dir / env_name
    requirements_path = current_dir / "requirements.txt"

    if env_path.exists():
        print(f"ℹ️ Virtual environment '{env_name}' already exists. Skipping creation.")
    else:
        create_virtual_env(env_path)

    install_dependencies(
        env_path,
        requirements_file=requirements_path if requirements_path.exists() else None,
        packages=default_packages
    )

    activate_script = env_path / ("Scripts" if os.name == "nt" else "bin") / "activate"

    print("\n✅ Setup complete.")
    print(f"\n➡️ To activate the environment, run:\n")
    if os.name == "nt":
        print(f"    {activate_script}")
    else:
        print(f"    source {activate_script}")
