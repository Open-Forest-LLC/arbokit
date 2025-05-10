import subprocess
import sys


def run_checks() -> None:
    """Запускает все проверки: форматтер, линтеры и тесты."""
    commands = [
        ["black", "--check", "src"],
        ["ruff", "check", "--fix", "src"],
        ["mypy", "src"],
        ["pytest", "-m", "not qt"],
        ["pytest", "-m", "qt"],
    ]

    for cmd in commands:
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(["poetry", "run"] + cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error in {' '.join(cmd)}:")
            print(result.stdout)
            print(result.stderr)
            sys.exit(result.returncode)
        else:
            print(f"{' '.join(cmd)} passed.")


if __name__ == "__main__":
    run_checks()
