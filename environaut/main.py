from pathlib import Path
from environaut.core.cleanup import cleanup_env
from environaut.core.setup import setup_env
from environaut.constants import DEFAULT_PACKAGES

def main():
    mode = input("Choose an action: [1] Setup env  [2] Delete env: ").strip()
    if mode == "2":
        cleanup_env(Path.cwd())
    elif mode == "1":
        setup_env(DEFAULT_PACKAGES)
    else:
        print("❌ Invalid option. Exiting.")

if __name__ == "__main__":
    main()
