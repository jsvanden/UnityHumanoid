Created by Jarrett van den Bergh for Unity Internship interview!
Works with Maya 2015 and Maya 2016

------------------READ ME------------------

The purpose of this tool is three-fold:

1)  To provide Maya users with a quick humanoid scale for their scene.

2)  To provide users with a customizable prototype character that can use Unity humanoid animations.

3)  To provide users with a quick way to create animations for general Unity humanoids.

-------------------SETUP-------------------

1)  Put 'UnityHumanoid.py' and 'style.qss' into your maya scripts folder.

        ex. C:\Users\Me\Documents\maya\2016\scripts

2)  Open the Maya script editor, open a Python tab and paste:

import UnityHumanoid
UnityHumanoid.create()

    It may be useful to save this script to the shelf.

3)  Run the code. The script may take some time to load for the first time.

----------------HOW TO USE-----------------

-   Initialize Rig will create a fresh rig and mesh to the standard Unity scale.
    The new rig / mesh deletes and replaces any previous rig / mesh.

-   The sliders adjust the general proportions of the prototype character.

-   Rebuild Mesh will readjust the mesh so that it fits the skeleton.
    This is useful if the skeleton was adjusted without using the sliders.

-   Bind Rig will smooth-bind the rig.

-   To auto-generate a rig, I suggest using Maya's Character Controls / HumanIK tool.
    Simply load the 'Unity Humanoid Skeleton.xml' file as the skeleton definition within the tool.
    Then click 'Create > Control Rig'.

-   Import the skeleton and mesh into Unity as an FBX. Set 'Import Settings > Animation Type > Humanoid'.
    The new character should be able to use all pre-existing humanoid animations.