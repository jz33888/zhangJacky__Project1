import maya.cmds as cmds

cmds.polyCone(
    radius=2.5,
    height=3,
    subdivisionsAxis=8,
    name="tree_leaves"
)

#making tree_leaves

cmds.move(0, 3, 0, "tree_leaves")

#position the treeleaves

cmds.polyCylinder(
    radius=0.5,
    height=3,
    name="tree_trunk"
)

#making tree_trunk

cmds.move(0, 1.5, 0, "tree_trunk")

#group them all
cmds.group("tree_leaves", "tree_trunk", name="tree_grp")

#number of leaves
#scaling of the trees as a whole object
#quality of the trees (subdivs up to 20)
#color of tree leaves
#trunk color
