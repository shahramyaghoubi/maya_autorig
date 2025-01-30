from maya import cmds
import os
import json
import pprint
import MakeEskeletonClass
import infoManagerNodeClass







NodeMaker = infoManagerNodeClass.infoManagerNodeClass()
mec = MakeEskeletonClass.MakeEskeletonClass()




NodeMaker.NodeMaker()

if cmds.window("Controllers" ,exists = True,rtf = True):
    cmds.deleteUI("Controllers")
dock = cmds.window("Controllers" )
cmds.frameLayout( label='Body' ,cll = True)

allowedAreas = ['bottom']

if dock == 1:
    cmds.deleteUI("Controllers")
dock = cmds.dockControl( area='left', content="Controllers", allowedArea=allowedAreas )



cmds.setParent( '..' )

cmds.setParent( '..' )

cmds.frameLayout( label='Scroll Bars' ,cll = True ,cl = True)
cmds.rowColumnLayout( numberOfColumns=3)
cmds.text("import ")
cmds.optionMenu( label='Eskeleton')
cmds.menuItem( label='Biped' )
cmds.menuItem( label='Bendy Biped' )
cmds.menuItem( label='Bird' )

cmds.button("Import" ,c = MakeEskeletonClass.MakeEskeletonClass().armMaker())
cmds.text("import ")
cmds.text("import ")
cmds.text("import ")

cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.frameLayout( label='Scroll' ,cll = True ,cl = True)
cmds.rowColumnLayout( numberOfColumns=3)

cmds.text("import ")
cmds.text("import ")
cmds.text("import ")
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.frameLayout( label='Check Boxes1' )
cmds.columnLayout()
cmds.checkBox()
cmds.checkBox()
cmds.checkBox()
cmds.setParent( '..' )


cmds.setParent( '..' )
cmds.frameLayout( label='Check Boxes2' )
cmds.columnLayout()
cmds.checkBox()
cmds.checkBox()
cmds.checkBox()
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.frameLayout( label='Check Boxes3' )
cmds.columnLayout()
cmds.checkBox()
cmds.checkBox()
cmds.checkBox()
cmds.setParent( '..' )
cmds.setParent( '..' )

cmds.showWindow()






