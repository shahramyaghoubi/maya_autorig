from maya import cmds
import os
import json
import pprint
import MakeEskeletonClass
import infoManagerNodeClass
import sys
import importlib
import UiManager
import Test



print ("Run")


infoManagerNodeClass.infoManagerNodeClass.info()



MakeEskeletonClass.SkeletonBuilder().NodeMaker()


UiManager.UiManager().UiMaker()
UiManager.UiManager().UiMaker()

Test.Test().TestMaker()



