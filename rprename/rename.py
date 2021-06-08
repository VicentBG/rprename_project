# -*- coding: utf-8 -*-
# rprename/rename.py

"""This module provides the Renamer class to rename multiple files."""

import time
import datetime as dt
from pathlib import Path

from PyQt5.QtCore import QObject, pyqtSignal

class Renamer(QObject):
    # Define custom signals
    progressed = pyqtSignal(int)
    renamedFile = pyqtSignal(Path)
    finished = pyqtSignal()

    def __init__(self, files, prefix):
        super().__init__()
        self._files = files
        self._prefix = prefix
        self.fecha = dt.datetime.now().strftime('%y%m%d%H%M')

    def renameFiles(self):
        for fileNumber, file in enumerate(self._files):
            newFile = file.parent.joinpath(
                f"{self.fecha}_{int(self._prefix) + fileNumber}{file.suffix}"
            )
            file.rename(newFile)
            time.sleep(0.1) # Comment this line to rename files faster.
            self.progressed.emit(fileNumber)
            self.renamedFile.emit(newFile)
        self.progressed.emit(0)
        self.finished.emit()