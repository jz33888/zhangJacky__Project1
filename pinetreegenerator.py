import maya.cmds as cmds

#PARAMETERS
leaf_count = 5
height = 8
width = 5
quality = 8
rows = 2
columns = 2
spacing = width * 2 #change the (2) to adjust the spacing

#trunk size
trunk_height = height * 0.35 #35% of the tree will be leaf
trunk_width = width * 0.08

#leaf size
leaf_height = height * 0.65/(1+(leaf_count-1)*0.65) #65% of the tree will be leaf

#make rows and columns
for row in range(rows):

    for column in range(columns):

        # Calculate tree position
        x = column * spacing
        z = row * spacing

        #make the trunk
        tree_trunk = cmds.polyCylinder(
            radius=trunk_width,
            height=trunk_height,
            subdivisionsAxis=quality,
            name="tree_trunk"
        )[0]

        #trunk position
        cmds.move(x, trunk_height / 2, z, tree_trunk)

        #store the tree objs
        tree = [tree_trunk]

        #make stacking leaves
        for tree_leaf in range(leaf_count):

            cone_width = width * (1 - tree_leaf / leaf_count)
            cone_height = leaf_height

            leaves = cmds.polyCone(
                radius=cone_width / 2,
                height=cone_height,
                subdivisionsAxis=quality,
                name="tree_leaves"
            )[0]

            #position each cone
            y = trunk_height + cone_height / 2 + tree_leaf * cone_height * 0.65

            cmds.move(x, y, z, leaves)

            tree.append(leaves)

    #Combines the trees into one geometry
    tree_geo = cmds.polyUnite(
        tree,
        name = "tree_{}_{}geo".format(row + 1, column + 1),
        )

    forest.append(tree_geo)

#Group em all together
cmds.group(
    forest,
    name = "forest_GRP"
)

#Goals:
#scaling of the trees as a whole object
#quality of the trees (subdivs up to 20)
#color of tree leaves
#trunk color
