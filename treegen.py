import bpy
import math
import pdb
from mathutils import Vector
from random import seed
from random import randint
import random

seed(1)

for object in bpy.data.objects:
    print(object.name)

num_trees = 1
# Generating n trees
for i in range(0, num_trees):
    seed = randint(0, 1000)
    split_height = random.uniform(0.2, 0.4)
    wind = random.uniform(0.3, 0.5)
    leaf_size = random.uniform(0.22, 0.28)
    frame_rate = random.uniform(0.65, 0.80)
    print(str.format("SEED: {0}", seed))
    bpy.ops.curve.tree_add(do_update=True, 
                           chooseSet='7', 
                           bevel=True, 
                           prune=False, 
                           showLeaves=True, 
                           useArm=True, 
                           seed=seed, 
                           handleType='0', 
                           levels=3, 
                           length=(1, 0.46, 0.45, 0.45), 
                           lengthV=(0, 0.03, 0.15, 0), 
                           taperCrown=0.2, 
                           branches=(0, 110, 18, 10), 
                           curveRes=(8, 5, 2, 1), 
                           curve=(0, -10, 0, 0), 
                           curveV=(10, 35, 35, 0), 
                           curveBack=(0, -30, -20, 0), 
                           baseSplits=1, 
                           segSplits=(0.45, 0.5, 0.8, 0), 
                           splitByLen=True, 
                           rMode='rotate', 
                           splitAngle=(13, 18, 18, 0), 
                           splitAngleV=(2, 5, 5, 0), 
                           scale=8, 
                           scaleV=2, 
                           attractUp=(-0.5, -0.7, 0, 0), 
                           attractOut=(0, 0.4, 0.5, 0), 
                           shape='7', 
                           shapeS='7', 
                           customShape=(0.5, 1, 0.3, 0.5), 
                           branchDist=1.25,
                           nrings=0, 
                           baseSize=0.28, 
                           baseSize_s=0.25, 
                           splitHeight=split_height, 
                           splitBias=0, 
                           ratio=0.02, 
                           minRadius=0.002, 
                           closeTip=False, 
                           rootFlare=1, 
                           autoTaper=True, 
                           taper=(1, 1, 1, 1), 
                           radiusTweak=(1, 1, 1, 1), 
                           ratioPower=1.2, 
                           downAngle=(90, 48, 45, 45), 
                           downAngleV=(0, 48, 10, 10), 
                           useOldDownAngle=False, 
                           useParentAngle=True, 
                           rotate=(90, 137.5, 137.5, 137.5), 
                           rotateV=(15, 0, 0, 0), 
                           scale0=1, 
                           scaleV0=0.2, 
                           pruneWidth=0.4, 
                           pruneBase=0.3, 
                           pruneWidthPeak=0.6, 
                           prunePowerHigh=0.5, 
                           prunePowerLow=0.001, 
                           pruneRatio=1, 
                           leaves=32, 
                           leafDownAngle=45, 
                           leafDownAngleV=10, 
                           leafRotate=137.5, 
                           leafRotateV=33, 
                           leafScale=leaf_size, 
                           leafScaleX=0.65, 
                           leafScaleT=0.35, 
                           leafScaleV=0.2, 
                           leafShape='hex', 
                           bend=0, 
                           leafangle=-35, 
                           horzLeaves=True, 
                           leafDist='6', 
                           bevelRes=3, 
                           resU=1, 
                           armAnim=True, 
                           previewArm=False, 
                           leafAnim=False, 
                           frameRate=0.7, 
                           loopFrames=0, 
                           wind=wind, 
                           gust=1, 
                           gustF=0.075, 
                           af1=1, 
                           af2=1, 
                           af3=4, 
                           makeMesh=True, 
                           armLevels=2, 
                           boneStep=(1, 1, 1, 1))

    treeName = 'Tree' + str(i)
    bpy.context.active_object.name = treeName
    # each tree is moved 20 units to the left to the l
    # this operator will 'work' or 'operate' on the active object we just set
    print("Applying modifiers")
    # Apply modifiers and uv unwrap                        
    for obj in bpy.context.scene.objects: 
        print(obj.name, obj, obj.type)
        if obj.name == 'treemesh':
            print("Applying Skin modifier")
            # skin modifier
            bpy.ops.object.modifier_apply({"object": obj},
                                          modifier='Skin')
            
            print("Applying Decimate modifier")
            # decimate modifier
            m = obj.modifiers.new("Decimate", type='DECIMATE')
            m.decimate_type = 'DISSOLVE'
            
            bpy.ops.object.modifier_apply({"object": obj},
                                          modifier=m.name)
            # Now,select tree mesh and uv unwrap
            print("UV unwrapping")
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
            bpy.ops.object.mode_set(mode='EDIT', toggle=True)
            
            lm = obj.data.uv_layers.new(name="LightMap")
            lm.active = True
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.uv.smart_project(angle_limit=30, island_margin=0.00, area_weight=0.00, correct_aspect=True)
            bpy.ops.object.mode_set(mode='OBJECT', toggle=True)
            x_translation = 15 * i
            print("Moving tree")
            bpy.data.objects[treeName].location = (x_translation, 0, 0)
                    
            # change name 
            obj.name = "treeMesh" + str(i)
