import maya.cmds as cmds

#PARAMETERS
leaf_count = 5
height = 8
width = 5
quality = 8
#rows
#columns

#trunk size
trunk_height = height * 0.35 #35% of the tree will be leaf
trunk_width = width * 0.08

#make the trunk
tree_trunk = cmds.polyCylinder(
    radius=trunk_width,
    height=trunk_height,
    subdivisionsAxis=quality,
    name="tree_trunk"
)[0]

#trunk position
cmds.move(0, trunk_height/2, 0, tree_trunk)

#store the tree objs
tree = [tree_trunk]

#leaf size

leaf_height = height * 0.65/(1+(leaf_count-1)*0.65) #65% of the tree will be leaf

#create the stacking leafs

for tree_leaf in range(leaf_count):

    cone_width = width * (1 - tree_leaf / leaf_count)
    cone_height = leaf_height

    leaves = cmds.polyCone(
        radius=cone_width / 2,
        height=cone_height,
        subdivisionsAxis=quality,
        name="tree_leaves"
    )[0]

    # Position each cone
    y = trunk_height + cone_height / 2 + tree_leaf * cone_height * 0.65

    cmds.move(0, y, 0, leaves)

    tree.append(leaves)

# Group entire tree
cmds.group(tree, name="tree_grp")

#scaling of the trees as a whole object
#quality of the trees (subdivs up to 20)
#color of tree leaves
#trunk color
