# Copyright (c) 2017 Looming
# Cura is released under the terms of the LGPLv3 or higher.

from . import JzTsWifiOutputDevice
from . import JzTsWifiStage


def getMetaData():
    return {
        "stage": {
            "name": "JzTsWifi",
            "weight": 99
        }
    }


def register(app):
    JzTsWifiStage.JzTsWifiStageIns = JzTsWifiStage.JzTsWifiStage(app)
    return {
        "output_device": JzTsWifiOutputDevice.JzTsWifiOutputDevicePlugin(),
        # "extension": JzTsWifiExtension.JzTsWifiExtensionIns,
        "stage": JzTsWifiStage.JzTsWifiStageIns
    }
