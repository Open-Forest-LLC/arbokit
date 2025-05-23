import os
import subprocess
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_checks() -> None:
    """Запускает все проверки: форматтер, линтеры и тесты."""
    os.environ["QT_QPA_PLATFORM"] = "offscreen"
    os.environ["QT_LOGGING_RULES"] = "qt5ct.debug=false"
    commands = [
        ["black", "--check", "src"],
        ["ruff", "check", "--fix", "src"],
        ["mypy", "src"],
    ]

    for cmd in commands:
        logger.info(f"Running: {' '.join(cmd)}")
        # Запускаем команду с явным указанием UTF-8
        result = subprocess.run(
            ["poetry", "run"] + cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"  # Заменяем нераспознанные символы
        )
        if result.returncode != 0:
            logger.error(f"Error in {' '.join(cmd)}:")
            logger.error(result.stdout)
            logger.error(result.stderr)
            sys.exit(result.returncode)
        else:
            logger.info(f"{' '.join(cmd)} passed.")


if __name__ == "__main__":
    run_checks()
