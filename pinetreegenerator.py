import maya.cmds as cmds

cmds.polyCone(
    radius=2.5,
    height=3,
    subdivisionsAxis=8)

#making and testing cone

cmds.polyCylinder(
    radius=2.5,
    height=3,
    subdivisionsAxis=8)

#making cylinder