
import maya.cmds as cmds

def create_forest(

    
    leaf_count=5,
    height=8,
    width=5,
    quality=8,
    rows=2,
    columns=2,
    spacing=None,
    leaf_color=(0.08, 0.35, 0.05),
    trunk_color=(0.30, 0.12, 0.04)
):

    #clear previous forest
    if cmds.objExists("forest_GRP"):
        cmds.delete("forest_GRP")

    if spacing is None:
        spacing = width * 2

    #creates leaf material
    leaf_material = cmds.shadingNode(
        "lambert", asShader=True, name="leaf_material"
    )

    leaf_SG = cmds.sets(
        renderable=True,
        noSurfaceShader=True,
        empty=True,
        name="leaf_SG"
    )

    cmds.connectAttr(leaf_material + ".outColor", leaf_SG + ".surfaceShader")
    cmds.setAttr(leaf_material + ".color", *leaf_color, type="double3")

    #creates trunk material
    trunk_material = cmds.shadingNode(
        "lambert", asShader=True, name="trunk_material"
    )

    trunk_SG = cmds.sets(
        renderable=True,
        noSurfaceShader=True,
        empty=True,
        name="trunk_SG"
    )

    cmds.connectAttr(trunk_material + ".outColor", trunk_SG + ".surfaceShader")
    cmds.setAttr(trunk_material + ".color", *trunk_color, type="double3")
    
    #trunk size
    trunk_height = height * 0.35 #35% of the tree will be leaf
    trunk_width = width * 0.08

    #leaf size
    leaf_height = height * 0.65/(1+(leaf_count-1)*0.65) if leaf_count > 0 else 0 #65% of the tree will be leaf

    #stores trees into "forest"
    forest = []
    
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

            #assign trunk material
            cmds.sets(tree_trunk, edit=True, forceElement=trunk_SG)

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

                #position each cone and size
                y = trunk_height + cone_height / 2 + tree_leaf * cone_height * 0.65

                #leaves position
                cmds.move(x, y, z, leaves)

                #assign leaves_material
                cmds.sets(leaves, edit=True, forceElement=leaf_SG)

                tree.append(leaves)

            #Combines the trees into one geometry
            if len(tree) > 1:

                tree_geo = cmds.polyUnite(
                    *tree,
                    name="tree_{}_{}geo".format(row + 1, column + 1),
                    constructionHistory=False
                )[0]

            else:
                tree_geo = tree[0]

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
