import sys
from pathlib import Path

ROOT = Path(__file__).parent

print("ROOT:", ROOT.resolve())


def update_main_readme():
    lines = [
        "# Coding Practice\n\n",
        "## Progress\n\n",
        "| Topic | Solved |\n",
        "|--------|--------:|\n",
    ]

    topic_data = []
    total = 0

    for topic_dir in sorted(ROOT.iterdir()):
        if (
            not topic_dir.is_dir()
            or topic_dir.name.startswith(".")
            or topic_dir.name == "__pycache__"
            or topic_dir.name == "venv"
        ):
            continue

        py_files = sorted(topic_dir.glob("*.py"))

        count = len(py_files)
        total += count

        topic_data.append(
            (
                topic_dir.name,
                count,
                py_files,
            )
        )

        topic_name = topic_dir.name.replace("-", " ").title()

        lines.append(
            f"| {topic_name} | {count} |\n"
        )

    lines.append(
        f"\n**Total Problems Solved:** {total}\n\n"
    )

    lines.append("---\n\n")

    for topic_name, _, py_files in topic_data:
        display_name = topic_name.replace("-", " ").title()

        lines.append(f"## {display_name}\n\n")
        lines.append("| # | Problem | Solution |\n")
        lines.append("|---|----------|----------|\n")

        for index, file in enumerate(py_files, start=1):
            problem_name = (
                file.stem
                .split("_", 1)[1]
                .replace("_", " ")
                .title()
            )

            lines.append(
                f"| {index} | "
                f"{problem_name} | "
                f"[Python]({topic_name}/{file.name}) |\n"
            )

        lines.append("\n")

    (ROOT / "README.md").write_text(
        "".join(lines),
        encoding="utf-8",
    )


def add_problem(topic, problem_name):
    topic_dir = ROOT / topic

    if not topic_dir.exists():
        print(f"❌ Topic '{topic}' does not exist")
        return

    py_files = sorted(topic_dir.glob("*.py"))
    next_no = len(py_files) + 1

    slug = (
        problem_name.lower()
        .replace(" ", "_")
        .replace("-", "_")
    )

    filename = f"{next_no:03d}_{slug}.py"

    template = f'''from typing import List


"""
{problem_name}

Problem Statement:
TODO

Approaches
----------
1. Brute Force
2. Better
3. Optimal
"""


class Solution:
    pass


if __name__ == "__main__":
    pass
'''

    (topic_dir / filename).write_text(
        template,
        encoding="utf-8",
    )

    update_main_readme()

    print(f"✅ Added: {topic}/{filename}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            'Usage: python add_problem.py arrays "Majority Element"'
        )
        sys.exit(1)

    add_problem(
        sys.argv[1],
        sys.argv[2],
    )