from maya import cmds
import os
import json
import pprint
import sys
import importlib
import Make_Eskeleton
import infoManagerNode

print ("Run")

Make_Eskeleton.SkeletonBuilder().NodeMaker()
infoManagerNode.infoManagerNodeClass().makeInfoNode()

