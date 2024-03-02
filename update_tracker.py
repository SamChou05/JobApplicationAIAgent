from llama_index.core.tools import FunctionTool
import os

tracker_file = os.path.join("data", "application.txt")


def update_tracker(note):
    if not os.path.isfile(tracker_file):
        open(tracker_file, "w")

    with open(tracker_file, "a") as f:
        f.writelines([note + "\n"])

    return "Application tracker updated!"


tracker_engine = FunctionTool.from_defaults(
    fn=update_tracker,
    name="application_tracker",
    description="this tool adds and modifies statuses on a job application tracker",
)
