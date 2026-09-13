import os
import platform
import shutil


def get_system_info():
    return {
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "python": platform.python_version(),
        "termux": "PREFIX" in os.environ
        and "com.termux" in os.environ.get("PREFIX", ""),
    }


def command_exists(command):
    return shutil.which(command) is not None


def run_checks():
    info = get_system_info()

    print("[+] Environment check")
    print(f"    System: {info['system']}")
    print(f"    Release: {info['release']}")
    print(f"    Architecture: {info['machine']}")
    print(f"    Python: {info['python']}")
    print(f"    Termux: {'Yes' if info['termux'] else 'No'}")

    return info