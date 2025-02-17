from maya import cmds

class infoManagerNodeClass:
    def makeInfoNode(self):
        rigDataNode = cmds.createNode("network", name="rigDataNode")
        cmds.addAttr(rigDataNode, shortName="RigExist", attributeType="float")
        cmds.setAttr(rigDataNode + ".RigExist", 1)

