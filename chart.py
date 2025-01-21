import plotly.graph_objects as go
from typing import Dict, List
from os import listdir
from os.path import isfile, join
from os import getcwd

OUTPUT = "chart.png"
IGNORED_FOLDERS = [".git", "venv", "utils"]
IGNORED_FILES = ["__init__.py", OUTPUT]


PIE_COLORS = []
DIR = getcwd()


def get_folders() -> List[str]:
    # Get a list of folders in the repo excluding ignored folders

    folders: List[str] = [
        folder
        for folder in listdir(DIR)
        if folder not in IGNORED_FOLDERS and not isfile(join(DIR, folder))
    ]
    return folders


def get_files_in_folders(folders: List[str]) -> Dict[str, List[str]]:
    files: Dict[str, List[str]] = {}
    for folder in folders:
        files[folder] = [
            file for file in listdir(join(DIR, folder)) if file not in IGNORED_FILES
        ]
    return files


def generate_chart(files: Dict[str, List[str]]) -> None:
    labels = list(files.keys())
    values = [len(values) for values in files.values()]
    chart = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                textinfo="label+value",
                textposition="outside",
                hole=0.8,
            )
        ]
    )
    chart.update_layout(
        annotations=[
            dict(
                text=f"Solved Questions: {sum(values)}",
                x=0.5,
                y=0.5,
                showarrow=False,
            )
        ],
        font=dict(family="Fira Code, monospace", color="#dedede"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    chart.write_image(OUTPUT)


if __name__ == "__main__":
    folders = get_folders()
    files_map = get_files_in_folders(folders)
    generate_chart(files_map)
