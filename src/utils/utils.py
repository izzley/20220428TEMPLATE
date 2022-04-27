from datetime import datetime
from typing import Optional, Union
from pathlib import Path

DATEFORMATS = {
    "yyyy-MM-dd HH:mm:ss": "%Y-%m-%d %H:%M:%S",
    "d/MM/yyyy h:mm:ss tt": "%e/%m/%Y %H:%M:%S %p",
}


def unix_to_datetime(epoch: Optional[Union[str, int]] = None) -> datetime:
    """
    UTC time from epoch integer."""
    # @NOTE: This is in UTC. Shouldn't matter coz its read straight in.
    return datetime.utcfromtimestamp(int(epoch))


def unix_to_format(epoch: Optional[Union[str, int]], format: str) -> str:
    """Datetime correct format based on importer config strings"""
    dtime = unix_to_datetime(epoch)
    return dtime.strftime(DATEFORMATS[format])


def is_csv(file: str) -> bool:
    """check file is csv format"""
    # @TODO: There are some zip files. How do we handle these?
    path = Path(file)
    return path.suffix == ".csv"


def flatten(nested_list: list) -> list:
    """
    Flatten list of lists:
    Usage:
        >> flatten([[1,2,3], [4,5,6], [7,8,9]]) -> [1,2,3,4,5,6,7,8,9]
    """
    flatlist = [item for sublist in nested_list for item in sublist]
    return sorted(flatlist)
