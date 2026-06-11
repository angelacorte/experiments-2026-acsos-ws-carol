"""Shared text labels for experiment plots."""

import re


EXPERIMENT_TITLES = {
    "differenttargets": "Different Targets",
    "followleader": "Follow Leader",
    "followtarget": "Follow Target",
    "multipleobstacles": "Multiple Obstacles",
    "noobstacle": "No Obstacles",
    "noobstacles": "No Obstacles",
}


def normalize_experiment_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def split_experiment_name(value: str) -> str:
    spaced = re.sub(r"(?<!^)(?=[A-Z])", " ", value)
    spaced = re.sub(r"[-_]+", " ", spaced)
    return " ".join(word.capitalize() for word in spaced.split())


def beautify_experiment_title(value: str) -> str:
    return EXPERIMENT_TITLES.get(normalize_experiment_name(value), split_experiment_name(value))
