from __future__ import annotations
import faulthandler

import os
import sys

from worlds.poe.Client import launch
import Utils

if __name__ == "__main__":
    faulthandler.enable()
    Utils.init_logging("pathofexile", exception_logger="Client")
    launch()
