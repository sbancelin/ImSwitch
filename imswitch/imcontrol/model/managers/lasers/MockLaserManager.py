import clr
import time
import sys
import inspect
#import os
from .LaserManager import LaserManager
from imswitch.imcommon.model import initLogger


class MockLaserManager(LaserManager):
    """ LaserManager for analog-value NI-DAQ-controlled lasers.
    Manager properties:
    - "serial_no_rotator": serial number of the motorized rotation half waveplate use to adjust laser power
    - "conversion_factor": rotator conversion from ° to motor count
    - "velocity": speed of the rotator
    """

    def __init__(self, laserInfo, name, **lowLevelManagers):
        self.__logger = initLogger(self, tryInheritParent=True)
        super().__init__(laserInfo, name, isBinary=False, valueUnits='mW',
                         valueDecimals=0)  # Appel du constructeur de la classe de base
        
    def setEnabled(self, enabled):
        pass

    def setValue(self, target_position_deg):
        pass

    def close(self):
        pass


# Copyright (C) 2020-2021 ImSwitch developers
# This file is part of ImSwitch.
#
# ImSwitch is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ImSwitch is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
