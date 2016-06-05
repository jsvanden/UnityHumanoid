from PySide import QtCore as qc
from PySide import QtGui as qg
import maya.cmds as mc
import sys
import maya.OpenMayaUI as mui
from shiboken import wrapInstance
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
import pymel.core as pm
import os



class UnityHumanoid(MayaQWidgetBaseMixin, qg.QDialog):
    def __init__(self, parent=None):
        qg.QDialog.__init__(self)
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setWindowTitle('Unity Humanoid')
        self.setObjectName('Unity Humanoid')
        
        currentDir = os.path.split(__file__)[0]
        style_sheet_file = currentDir + "\style.qss"
        #style_sheet_file = "C:/Users/Jarrett/Documents/maya/2015-x64/scripts\style.qss"
        with open(style_sheet_file, "r") as fh:
            self.setStyleSheet(fh.read())
        
        # Main Layout
        self.setLayout(qg.QVBoxLayout())
        self.layout().setContentsMargins(5,5,5,5)
        self.layout().setSpacing(5)
        self.setFixedHeight(300)
        
        ## Slider Layout
        slider_layout = qg.QVBoxLayout()
        self.layout().addLayout(slider_layout)
        
        ### Head Size Label
        slider_layout.addWidget(qg.QLabel('Head Size'))

        ### Head Size Input Layout      
        headSize_layout = qg.QHBoxLayout()        
        slider_layout.addLayout(headSize_layout)
        
        #### Head Size Slider
        self.headSize_slider = qg.QSlider(value=100)
        self.headSize_slider.setRange(30,200)
        self.headSize_slider.setOrientation(qc.Qt.Horizontal)
        self.headSize_slider.valueChanged.connect(self.setHeadSize)
        headSize_layout.addWidget(self.headSize_slider)
        
        #### Head Size Spin Box
        self.headSize_spinBox = qg.QDoubleSpinBox()
        self.headSize_spinBox.setRange(0.3,2.0)
        self.headSize_spinBox.setValue(1.0)
        self.headSize_spinBox.setSingleStep(0.1)
        self.headSize_spinBox.valueChanged.connect(self.setHeadSize)
        headSize_layout.addWidget(self.headSize_spinBox)
        
         ### Torso Size Label
        slider_layout.addWidget(qg.QLabel('Torso Size'))

        ### Torso Size Input Layout      
        torsoSize_layout = qg.QHBoxLayout()        
        slider_layout.addLayout(torsoSize_layout)
        
        #### Torso Size Slider
        self.torsoSize_slider = qg.QSlider(value=100)
        self.torsoSize_slider.setRange(30,200)
        self.torsoSize_slider.setOrientation(qc.Qt.Horizontal)
        self.torsoSize_slider.valueChanged.connect(self.setTorsoSize)
        torsoSize_layout.addWidget(self.torsoSize_slider)
        
        #### Torso Size Spin Box
        self.torsoSize_spinBox = qg.QDoubleSpinBox()
        self.torsoSize_spinBox.setRange(0.3,2.0)
        self.torsoSize_spinBox.setValue(1.0)
        self.torsoSize_spinBox.setSingleStep(0.1)
        self.torsoSize_spinBox.valueChanged.connect(self.setTorsoSize)
        torsoSize_layout.addWidget(self.torsoSize_spinBox)
        
        ### Leg Height Label
        slider_layout.addWidget(qg.QLabel('Leg Height'))
        
        ### Leg Height Input Layout  
        legHeight_layout = qg.QHBoxLayout()
        slider_layout.addLayout(legHeight_layout)
        
        #### Leg Height Slider
        self.legHeight_slider = qg.QSlider(value=100)
        self.legHeight_slider.setRange(30,200)
        self.legHeight_slider.setOrientation(qc.Qt.Horizontal)
        self.legHeight_slider.valueChanged.connect(self.setLegHeight)
        legHeight_layout.addWidget(self.legHeight_slider)
        
        #### Leg Height Spin Box
        self.legHeight_spinBox = qg.QDoubleSpinBox()
        self.legHeight_spinBox.setRange(0.3,2.0)
        self.legHeight_spinBox.setValue(1.0)
        self.legHeight_spinBox.setSingleStep(0.1)
        self.legHeight_spinBox.valueChanged.connect(self.setLegHeight)
        legHeight_layout.addWidget(self.legHeight_spinBox)

        ### Left Arm Length Label
        slider_layout.addWidget(qg.QLabel('Left Arm Length'))
        
        ### Left Arm Length Layout  
        l_armLength_layout = qg.QHBoxLayout()
        slider_layout.addLayout(l_armLength_layout)
        
        #### Left Arm Length Slider
        self.l_armLength_slider = qg.QSlider(value=100)
        self.l_armLength_slider.setRange(30,200)
        self.l_armLength_slider.setOrientation(qc.Qt.Horizontal)
        self.l_armLength_slider.valueChanged.connect(self.setLeftArmLength)
        l_armLength_layout.addWidget(self.l_armLength_slider)
        
        #### Left Arm Length Spin Box
        self.l_armLength_spinBox = qg.QDoubleSpinBox()
        self.l_armLength_spinBox.setRange(0.3,2.0)
        self.l_armLength_spinBox.setValue(1.0)
        self.l_armLength_spinBox.setSingleStep(0.1)
        self.l_armLength_spinBox.valueChanged.connect(self.setLeftArmLength)
        l_armLength_layout.addWidget(self.l_armLength_spinBox)
        
        ### Right Arm Length Label
        slider_layout.addWidget(qg.QLabel('Right Arm Length'))
        
        ### Right Arm Length Layout  
        r_armLength_layout = qg.QHBoxLayout()
        slider_layout.addLayout(r_armLength_layout)
        
        #### Right Arm Length Slider
        self.r_armLength_slider = qg.QSlider(value=100)
        self.r_armLength_slider.setRange(30,200)
        self.r_armLength_slider.setOrientation(qc.Qt.Horizontal)
        self.r_armLength_slider.valueChanged.connect(self.setRightArmLength)
        r_armLength_layout.addWidget(self.r_armLength_slider)
        
        #### Left Arm Length Spin Box
        self.r_armLength_spinBox = qg.QDoubleSpinBox()
        self.r_armLength_spinBox.setRange(0.3,2.0)
        self.r_armLength_spinBox.setValue(1.0)
        self.r_armLength_spinBox.setSingleStep(0.1)
        self.r_armLength_spinBox.valueChanged.connect(self.setRightArmLength)
        r_armLength_layout.addWidget(self.r_armLength_spinBox)
        
        ## Button Layout
        button_layout = qg.QHBoxLayout()
        self.layout().addLayout(button_layout)
        
        ### Initialize Rig Button
        self.initRig_bttn = qg.QPushButton('Initialize Rig')
        button_layout.addWidget(self.initRig_bttn)
        self.initRig_bttn.clicked.connect(self.InitRig)
        
        ### Rebuild Mesh Button
        self.rebuildMesh_bttn = qg.QPushButton('Rebuild Mesh')
        button_layout.addWidget(self.rebuildMesh_bttn)
        self.rebuildMesh_bttn.clicked.connect(self.RebuildMesh)
        
        ### Bind Rig Button
        self.bindRig_bttn = qg.QPushButton('Bind Rig')
        button_layout.addWidget(self.bindRig_bttn)
        self.bindRig_bttn.clicked.connect(self.bindRig)
        
        ## Progress Bar
        self.progressBar = qg.QProgressBar()
        #self.progressBar.setVisible(False)
        #self.progressBar.setValue(50)
        self.layout().addWidget(self.progressBar)
        
        self.enableRigEdit(False)
        
#-----------------------------------------------------------------------------#

    def enableRigEdit(self, value):
        self.headSize_slider.setEnabled(value)
        self.headSize_spinBox.setEnabled(value)
        
        self.torsoSize_slider.setEnabled(value)
        self.torsoSize_spinBox.setEnabled(value)
        
        self.legHeight_slider.setEnabled(value)
        self.legHeight_spinBox.setEnabled(value)
        
        self.l_armLength_slider.setEnabled(value)
        self.l_armLength_spinBox.setEnabled(value)
        
        self.r_armLength_slider.setEnabled(value)
        self.r_armLength_spinBox.setEnabled(value)
        
        self.rebuildMesh_bttn.setEnabled(value)
        self.bindRig_bttn.setEnabled(value)

    def setTorsoSize(self, value):
        pm.undoInfo(openChunk=True)
        if value > 10.0:
            value = value / 100.0
            self.torsoSize_spinBox.setValue(value)
        else:
            self.torsoSize_slider.setValue(value*100)
            
        self.setJointScale(self.spine, value, self.torsoSize)
        self.setJointScale(self.chest, value, self.torsoSize)
        self.setJointScale(self.neck, value, self.torsoSize)
        
        self.torsoSize = value
        self.RebuildMesh()
        pm.undoInfo(closeChunk=True)
        
    def setLeftArmLength(self, value):
        pm.undoInfo(openChunk=True)
        self.progressBar.setValue(50)
        if value > 10.0:
            value = value / 100.0
            self.l_armLength_spinBox.setValue(value)
        else:
            self.l_armLength_slider.setValue(value*100)
            
        mc.select(self.l_upperArmMesh, self.l_lowerArmMesh, self.l_thumbMesh_a, self.l_thumbMesh_b, self.l_thumbMesh_c,
        self.l_indexMesh_a, self.l_indexMesh_b, self.l_indexMesh_c, self.l_middleMesh_a, self.l_middleMesh_b,
        self.l_middleMesh_c, self.l_ringMesh_a, self.l_ringMesh_b, self.l_ringMesh_c, self.l_pinkieMesh_a,
        self.l_pinkieMesh_b, self.l_pinkieMesh_c)
        mc.delete()
        
        self.setJointScale(self.l_shoulder, value, self.l_armLength)
        self.setJointScale(self.l_upperArm, value, self.l_armLength)
        self.setJointScale(self.l_lowerArm, value, self.l_armLength)
        self.setJointScale(self.l_wrist, value, self.l_armLength)
        self.setJointScale(self.l_thumb_a, value, self.l_armLength)
        self.setJointScale(self.l_thumb_b, value, self.l_armLength)
        self.setJointScale(self.l_thumb_c, value, self.l_armLength)
        self.setJointScale(self.l_thumb_d, value, self.l_armLength)
        
        self.setJointScale(self.l_index_a, value, self.l_armLength)
        self.setJointScale(self.l_index_b, value, self.l_armLength)
        self.setJointScale(self.l_index_c, value, self.l_armLength)
        self.setJointScale(self.l_index_d, value, self.l_armLength)
        
        self.setJointScale(self.l_middle_a, value, self.l_armLength)
        self.setJointScale(self.l_middle_b, value, self.l_armLength)
        self.setJointScale(self.l_middle_c, value, self.l_armLength)
        self.setJointScale(self.l_middle_d, value, self.l_armLength)
        
        self.setJointScale(self.l_ring_a, value, self.l_armLength)
        self.setJointScale(self.l_ring_b, value, self.l_armLength)
        self.setJointScale(self.l_ring_c, value, self.l_armLength)
        self.setJointScale(self.l_ring_d, value, self.l_armLength)
        
        self.setJointScale(self.l_pinkie_a, value, self.l_armLength)
        self.setJointScale(self.l_pinkie_b, value, self.l_armLength)
        self.setJointScale(self.l_pinkie_c, value, self.l_armLength)
        self.setJointScale(self.l_pinkie_d, value, self.l_armLength)
        
        self.l_upperArmMesh = CreateRightCube("char_l_upperArmMesh", self.l_upperArm, self.l_lowerArm, [5,1,5], [2,1,2])
        self.l_lowerArmMesh = CreateRightCube("char_l_lowerArmMesh", self.l_lowerArm, self.l_wrist, [3,1,3], [2,1,2])

        self.l_thumbMesh_a = CreateRightCube("char_l_thumbMesh_a", self.l_thumb_a, self.l_thumb_b, [1,1,1], [1,1,1])
        self.l_thumbMesh_b = CreateRightCube("char_l_thumbMesh_b", self.l_thumb_b, self.l_thumb_c, [1,1,1], [1,1,1])
        self.l_thumbMesh_c = CreateRightCube("char_l_thumbMesh_c", self.l_thumb_c, self.l_thumb_d, [1,1,1], [1,1,1])

        self.l_indexMesh_a = CreateRightCube("char_l_indexMesh_a", self.l_index_a, self.l_index_b, [1,1,1], [1,1,1])
        self.l_indexMesh_b = CreateRightCube("char_l_indexMesh_b", self.l_index_b, self.l_index_c, [1,1,1], [1,1,1])
        self.l_indexMesh_c = CreateRightCube("char_l_indexMesh_c", self.l_index_c, self.l_index_d, [1,1,1], [1,1,1])
        
        self.progressBar.setValue(100)

        self.l_middleMesh_a = CreateRightCube("char_l_middleMesh_a", self.l_middle_a, self.l_middle_b, [1,1,1], [1,1,1])
        self.l_middleMesh_b = CreateRightCube("char_l_middleMesh_b", self.l_middle_b, self.l_middle_c, [1,1,1], [1,1,1])
        self.l_middleMesh_c = CreateRightCube("char_l_middleMesh_c", self.l_middle_c, self.l_middle_d, [1,1,1], [1,1,1])

        self.l_ringMesh_a = CreateRightCube("char_l_ringMesh_a", self.l_ring_a, self.l_ring_b, [1,1,1], [1,1,1])
        self.l_ringMesh_b = CreateRightCube("char_l_ringMesh_b", self.l_ring_b, self.l_ring_c, [1,1,1], [1,1,1])
        self.l_ringMesh_c = CreateRightCube("char_l_ringMesh_c", self.l_ring_c, self.l_ring_d, [1,1,1], [1,1,1])

        self.l_pinkieMesh_a = CreateRightCube("char_l_pinkieMesh_a", self.l_pinkie_a, self.l_pinkie_b, [1,1,1], [1,1,1])
        self.l_pinkieMesh_b = CreateRightCube("char_l_pinkieMesh_b", self.l_pinkie_b, self.l_pinkie_c, [1,1,1], [1,1,1])
        self.l_pinkieMesh_c = CreateRightCube("char_l_pinkieMesh_c", self.l_pinkie_c, self.l_pinkie_d, [1,1,1], [1,1,1])
        
        self.l_armLength = value
        self.progressBar.setValue(0)
        pm.undoInfo(closeChunk=True)
        
    def setRightArmLength(self, value):
        pm.undoInfo(openChunk=True)
        self.progressBar.setValue(50)
        if value > 10.0:
            value = value / 100.0
            self.r_armLength_spinBox.setValue(value)
        else:
            self.r_armLength_slider.setValue(value*100)
            
        mc.select(self.r_upperArmMesh, self.r_lowerArmMesh, self.r_thumbMesh_a, self.r_thumbMesh_b, self.r_thumbMesh_c,
        self.r_indexMesh_a, self.r_indexMesh_b, self.r_indexMesh_c, self.r_middleMesh_a, self.r_middleMesh_b,
        self.r_middleMesh_c, self.r_ringMesh_a, self.r_ringMesh_b, self.r_ringMesh_c, self.r_pinkieMesh_a,
        self.r_pinkieMesh_b, self.r_pinkieMesh_c)
        mc.delete()
        
        self.setJointScale(self.r_shoulder, value, self.r_armLength)
        self.setJointScale(self.r_upperArm, value, self.r_armLength)
        self.setJointScale(self.r_lowerArm, value, self.r_armLength)
        self.setJointScale(self.r_wrist, value, self.r_armLength)
        self.setJointScale(self.r_thumb_a, value, self.r_armLength)
        self.setJointScale(self.r_thumb_b, value, self.r_armLength)
        self.setJointScale(self.r_thumb_c, value, self.r_armLength)
        self.setJointScale(self.r_thumb_d, value, self.r_armLength)
        
        self.setJointScale(self.r_index_a, value, self.r_armLength)
        self.setJointScale(self.r_index_b, value, self.r_armLength)
        self.setJointScale(self.r_index_c, value, self.r_armLength)
        self.setJointScale(self.r_index_d, value, self.r_armLength)
        
        self.setJointScale(self.r_middle_a, value, self.r_armLength)
        self.setJointScale(self.r_middle_b, value, self.r_armLength)
        self.setJointScale(self.r_middle_c, value, self.r_armLength)
        self.setJointScale(self.r_middle_d, value, self.r_armLength)
        
        self.setJointScale(self.r_ring_a, value, self.r_armLength)
        self.setJointScale(self.r_ring_b, value, self.r_armLength)
        self.setJointScale(self.r_ring_c, value, self.r_armLength)
        self.setJointScale(self.r_ring_d, value, self.r_armLength)
        
        self.setJointScale(self.r_pinkie_a, value, self.r_armLength)
        self.setJointScale(self.r_pinkie_b, value, self.r_armLength)
        self.setJointScale(self.r_pinkie_c, value, self.r_armLength)
        self.setJointScale(self.r_pinkie_d, value, self.r_armLength)
        
        self.r_upperArmMesh = CreateRightCube("char_r_upperArmMesh", self.r_lowerArm, self.r_upperArm, [2,1,2], [5,1,5])
        self.r_lowerArmMesh = CreateRightCube("char_r_lowerArmMesh", self.r_wrist, self.r_lowerArm, [2,1,2], [3,1,3])

        self.r_thumbMesh_a = CreateRightCube("char_r_thumbMesh_a", self.r_thumb_b, self.r_thumb_a, [1,1,1], [1,1,1])
        self.r_thumbMesh_b = CreateRightCube("char_r_thumbMesh_b", self.r_thumb_c, self.r_thumb_b, [1,1,1], [1,1,1])
        self.r_thumbMesh_c = CreateRightCube("char_r_thumbMesh_c", self.r_thumb_d, self.r_thumb_c, [1,1,1], [1,1,1])

        self.r_indexMesh_a = CreateRightCube("char_r_indexMesh_a", self.r_index_b, self.r_index_a, [1,1,1], [1,1,1])
        self.r_indexMesh_b = CreateRightCube("char_r_indexMesh_b", self.r_index_c, self.r_index_b, [1,1,1], [1,1,1])
        self.r_indexMesh_c = CreateRightCube("char_r_indexMesh_c", self.r_index_d, self.r_index_c, [1,1,1], [1,1,1])
        
        self.progressBar.setValue(100)
        
        self.r_middleMesh_a = CreateRightCube("char_r_middleMesh_a", self.r_middle_b, self.r_middle_a, [1,1,1], [1,1,1])
        self.r_middleMesh_b = CreateRightCube("char_r_middleMesh_b", self.r_middle_c, self.r_middle_b, [1,1,1], [1,1,1])
        self.r_middleMesh_c = CreateRightCube("char_r_middleMesh_c", self.r_middle_d, self.r_middle_c, [1,1,1], [1,1,1])

        self.r_ringMesh_a = CreateRightCube("char_r_ringMesh_a", self.r_ring_b, self.r_ring_a, [1,1,1], [1,1,1])
        self.r_ringMesh_b = CreateRightCube("char_r_ringMesh_b", self.r_ring_c, self.r_ring_b, [1,1,1], [1,1,1])
        self.r_ringMesh_c = CreateRightCube("char_r_ringMesh_c", self.r_ring_d, self.r_ring_c, [1,1,1], [1,1,1])

        self.r_pinkieMesh_a = CreateRightCube("char_r_pinkieMesh_a", self.r_pinkie_b, self.r_pinkie_a, [1,1,1], [1,1,1])
        self.r_pinkieMesh_b = CreateRightCube("char_r_pinkieMesh_b", self.r_pinkie_c, self.r_pinkie_b, [1,1,1], [1,1,1])
        self.r_pinkieMesh_c = CreateRightCube("char_r_pinkieMesh_c", self.r_pinkie_d, self.r_pinkie_c, [1,1,1], [1,1,1])
        
        self.r_armLength = value
        self.progressBar.setValue(0)
        pm.undoInfo(closeChunk=True)
        
    def setHeadSize(self, value):
        pm.undoInfo(openChunk=True)
        self.progressBar.setValue(100)
        if value > 10.0:
            value = value / 100.0
            self.headSize_spinBox.setValue(value)
        else:
            self.headSize_slider.setValue(value*100)
        
        mc.select(self.headMesh)
        mc.delete()
        
        self.setJointScale(self.headTop, value, self.headSize)
        self.headMesh = createSphere("char_headMesh", self.head, self.headTop)
        self.headSize = value
        self.progressBar.setValue(0)
        pm.undoInfo(closeChunk=True)
        
    def setLegHeight(self, value):
        pm.undoInfo(openChunk=True)
        
        if value > 10.0:
            value = value / 100.0
            self.legHeight_spinBox.setValue(value)
        else:
            self.legHeight_slider.setValue(value*100)
        
        self.setJointScale(self.hips, value, self.legHeight)
        self.setJointScale(self.l_upperLeg, value, self.legHeight)
        self.setJointScale(self.l_lowerLeg, value, self.legHeight)
        self.setJointScale(self.l_foot, value, self.legHeight)
        self.setJointScale(self.l_toes, value, self.legHeight)
        self.setJointScale(self.l_toeEnd, value, self.legHeight)
        self.setJointScale(self.r_upperLeg, value, self.legHeight)
        self.setJointScale(self.r_lowerLeg, value, self.legHeight)
        self.setJointScale(self.r_foot, value, self.legHeight)
        self.setJointScale(self.r_toes, value, self.legHeight)
        self.setJointScale(self.r_toeEnd, value, self.legHeight)

        self.legHeight = value
        self.RebuildMesh()
        
        pm.undoInfo(closeChunk=True)
        
    def setJointScale(self, joint, value, prevValue):
        tempPos = mc.xform(joint, q=True, t=True)
        diffLegHeight = value / prevValue
        mc.select(joint) 
        mc.xform(t=(tempPos[0]*diffLegHeight, tempPos[1]*diffLegHeight, tempPos[2]*diffLegHeight))
    
    def bindRig(self):
        pm.undoInfo(openChunk=True)
        
        self.progressBar.setValue(50)
        mc.polyUnite(self.hipsMesh, self.spineMesh, self.chestMesh, self.headMesh, self.l_upperArmMesh,
        self.l_lowerArmMesh, self.l_thumbMesh_a, self.l_thumbMesh_b, self.l_thumbMesh_c, self.l_indexMesh_a,
        self.l_indexMesh_b, self.l_indexMesh_c, self.l_middleMesh_a, self.l_middleMesh_b, self.l_middleMesh_c,
        self.l_ringMesh_a, self.l_ringMesh_b, self.l_ringMesh_c, self.l_pinkieMesh_a, self.l_pinkieMesh_b,
        self.l_pinkieMesh_c, self.r_upperArmMesh, self.r_lowerArmMesh, self.r_thumbMesh_a, self.r_thumbMesh_b,
        self.r_thumbMesh_c, self.r_indexMesh_a, self.r_indexMesh_b, self.r_indexMesh_c, self.r_middleMesh_a,
        self.r_middleMesh_b, self.r_middleMesh_c, self.r_ringMesh_a, self.r_ringMesh_b, self.r_ringMesh_c,
        self.r_pinkieMesh_a, self.r_pinkieMesh_b, self.r_pinkieMesh_c, self.l_upperLegMesh, self.l_lowerLegMesh,
        self.l_footMesh, self.l_toesMesh, self.r_upperLegMesh, self.r_lowerLegMesh, self.r_footMesh, self.r_toesMesh,
        n = "char_body")
        self.progressBar.setValue(100)
        mc.select(self.hips, tgl=True, hi=True)
        mc.SmoothBindSkin()
        self.enableRigEdit(False)
        self.progressBar.setValue(0)
        
        pm.undoInfo(closeChunk=True)
    
    def InitRig(self):
        pm.undoInfo(openChunk=True)
    
        self.legHeight_slider.blockSignals(True)
        self.legHeight_spinBox.blockSignals(True)
        self.legHeight = 1
        self.legHeight_slider.setValue(100) 
        self.legHeight_spinBox.setValue(1.0)
        self.legHeight_slider.blockSignals(False)
        self.legHeight_spinBox.blockSignals(False)
        
        self.headSize_slider.blockSignals(True)
        self.headSize_spinBox.blockSignals(True)
        self.headSize = 1
        self.headSize_slider.setValue(100)
        self.headSize_spinBox.setValue(1.0)
        self.headSize_slider.blockSignals(False)
        self.headSize_spinBox.blockSignals(False)
        
        self.torsoSize_slider.blockSignals(True)
        self.torsoSize_spinBox.blockSignals(True)
        self.torsoSize = 1
        self.torsoSize_slider.setValue(100)
        self.torsoSize_spinBox.setValue(1.0)
        self.torsoSize_slider.blockSignals(False)
        self.torsoSize_spinBox.blockSignals(False)
        
        self.l_armLength_slider.blockSignals(True)
        self.l_armLength_spinBox.blockSignals(True)
        self.l_armLength = 1
        self.l_armLength_slider.setValue(100) 
        self.l_armLength_spinBox.setValue(1.0)
        self.l_armLength_slider.blockSignals(False)
        self.l_armLength_spinBox.blockSignals(False)
        
        self.r_armLength_slider.blockSignals(True)
        self.r_armLength_spinBox.blockSignals(True)
        self.r_armLength = 1
        self.r_armLength_slider.setValue(100) 
        self.r_armLength_spinBox.setValue(1.0)
        self.r_armLength_slider.blockSignals(False)
        self.r_armLength_spinBox.blockSignals(False)
        
        self.enableRigEdit(True)
        self.InitializeRig();
        
        pm.undoInfo(closeChunk=True)
        
    def RebuildMesh(self):
        pm.undoInfo(openChunk=True)
        mc.select(self.hipsMesh, self.spineMesh, self.chestMesh, self.headMesh, self.l_upperArmMesh,
        self.l_lowerArmMesh, self.l_thumbMesh_a, self.l_thumbMesh_b, self.l_thumbMesh_c, self.l_indexMesh_a,
        self.l_indexMesh_b, self.l_indexMesh_c, self.l_middleMesh_a, self.l_middleMesh_b, self.l_middleMesh_c,
        self.l_ringMesh_a, self.l_ringMesh_b, self.l_ringMesh_c, self.l_pinkieMesh_a, self.l_pinkieMesh_b,
        self.l_pinkieMesh_c, self.r_upperArmMesh, self.r_lowerArmMesh, self.r_thumbMesh_a, self.r_thumbMesh_b,
        self.r_thumbMesh_c, self.r_indexMesh_a, self.r_indexMesh_b, self.r_indexMesh_c, self.r_middleMesh_a,
        self.r_middleMesh_b, self.r_middleMesh_c, self.r_ringMesh_a, self.r_ringMesh_b, self.r_ringMesh_c,
        self.r_pinkieMesh_a, self.r_pinkieMesh_b, self.r_pinkieMesh_c, self.l_upperLegMesh, self.l_lowerLegMesh,
        self.l_footMesh, self.l_toesMesh, self.r_upperLegMesh, self.r_lowerLegMesh, self.r_footMesh, self.r_toesMesh)
        mc.delete()
        self.BuildMesh()
        pm.undoInfo(closeChunk=True)
        
    def InitializeRig(self):  
        try:
            mc.select(self.hipsMesh, self.spineMesh, self.chestMesh, self.headMesh, self.l_upperArmMesh,
            self.l_lowerArmMesh, self.l_thumbMesh_a, self.l_thumbMesh_b, self.l_thumbMesh_c, self.l_indexMesh_a,
            self.l_indexMesh_b, self.l_indexMesh_c, self.l_middleMesh_a, self.l_middleMesh_b, self.l_middleMesh_c,
            self.l_ringMesh_a, self.l_ringMesh_b, self.l_ringMesh_c, self.l_pinkieMesh_a, self.l_pinkieMesh_b,
            self.l_pinkieMesh_c, self.r_upperArmMesh, self.r_lowerArmMesh, self.r_thumbMesh_a, self.r_thumbMesh_b,
            self.r_thumbMesh_c, self.r_indexMesh_a, self.r_indexMesh_b, self.r_indexMesh_c, self.r_middleMesh_a,
            self.r_middleMesh_b, self.r_middleMesh_c, self.r_ringMesh_a, self.r_ringMesh_b, self.r_ringMesh_c,
            self.r_pinkieMesh_a, self.r_pinkieMesh_b, self.r_pinkieMesh_c, self.l_upperLegMesh, self.l_lowerLegMesh,
            self.l_footMesh, self.l_toesMesh, self.r_upperLegMesh, self.r_lowerLegMesh, self.r_footMesh, self.r_toesMesh,
            self.hips)
            mc.delete()
        except:
            print("No preexisting mesh found.")
    
        #mc.select(all=True)
        #mc.delete()
        
        #Torso and Head

        self.hips = mc.joint(n="char_hips", rad=4, p=(0,82.4,0), o=(-90,-5,90))
        self.spine = mc.joint(n="char_spine", rad=4, r=True, p=(14.7,2.6,0))
        self.chest = mc.joint(n="char_chest", rad=4, r=True, p=(12.7,2.2,0))
        self.neck = mc.joint(n="char_neck", rad=4, r=True, p=(12.6,2.2,0), o=(0,0,15))
        self.head = mc.joint(n="char_head", rad=4, r=True, p=(9.1,-4.1,0), o=(0,0,-10))
        self.headTop = mc.joint(n="char_headTop", rad=4, r=True, p=(17.5,0,0))

        #Left Arm

        mc.select(self.neck)
        self.l_shoulder = mc.joint(n="char_l_shoulder", rad=4, r=True, p=(0,0,-2.6), o=(0,-65,165))
        self.l_upperArm = mc.joint(n="char_l_upperArm", rad=4, r=True, p=(-8.2,0.9,-9.6), o=(9,9.6,1.1))
        self.l_lowerArm = mc.joint(n="char_l_lowerArm", rad=4, r=True, p=(-8.8,-1.4,-23), o=(0,0,-26.5))
        self.l_wrist = mc.joint(n="char_l_wrist", rad=4, r=True, p=(-7,3.6,-14.1), o=(0,10,0))

        self.l_thumb_a = mc.joint(n="char_l_thumb_a", rad=2, r=True, p=(0.5,4.9,-3), o=(44.2,-43.5,29.5))
        self.l_thumb_b = mc.joint(n="char_l_thumb_b", rad=2, r=True, p=(-0.1,-0.5,-3), o=(-10.4,1.4,1.1))
        self.l_thumb_c = mc.joint(n="char_l_thumb_c", rad=2, r=True, p=(-0.3,-0.4,-2.2), o=(-9.3,9.1,10.2))
        self.l_thumb_d = mc.joint(n="char_l_thumb_d", rad=2, r=True, p=(-0.4,-0.5,-2.3))

        mc.select(self.l_wrist)
        self.l_index_a = mc.joint(n="char_l_index_a", rad=2, r=True, p=(-1.8,5.1,-8), o=(19.3,-28.6,73.2))
        self.l_index_b = mc.joint(n="char_l_index_b", rad=2, r=True, p=(-0.4,-0.5,-2.7), o=(-9.1,10.1,7.3))
        self.l_index_c = mc.joint(n="char_l_index_c", rad=2, r=True, p=(0.3,-0.7,-2.3), o=(-15.4,-10.2,-10.5))
        self.l_index_d = mc.joint(n="char_l_index_d", rad=2, r=True, p=(0.2,-0.6,-2.1))

        mc.select(self.l_wrist)
        self.l_middle_a = mc.joint(n="char_l_middle_a", rad=2, r=True, p=(-1.3,3.2,-8.4), o=(11.6,-21.9,82.9))
        self.l_middle_b = mc.joint(n="char_l_middle_b", rad=2, r=True, p=(-0.3,0.1,-3.2), o=(-1.9,6.2,5.1))
        self.l_middle_c = mc.joint(n="char_l_middle_c", rad=2, r=True, p=(0.5,-1.2,-2.2), o=(-22.5,-19.2,-17.8))
        self.l_middle_d = mc.joint(n="char_l_middle_d", rad=2, r=True, p=(0.3,-0.4,-2.3))

        mc.select(self.l_wrist)
        self.l_ring_a = mc.joint(n="char_l_ring_a", rad=2, r=True, p=(-1.2,0.9,-9.7), o=(5.9,-6.5,100.6))
        self.l_ring_b = mc.joint(n="char_l_ring_b", rad=2, r=True, p=(0.9,-0.9,-2.5), o=(-10.2,-25.1,-23.4))
        self.l_ring_c = mc.joint(n="char_l_ring_c", rad=2, r=True, p=(0.4,-0.5,-2), o=(-8.8,-14.4,-22.3))
        self.l_ring_d = mc.joint(n="char_l_ring_d", rad=2, r=True, p=(0.2,-0.2,-2.1))

        mc.select(self.l_wrist)
        self.l_pinkie_a = mc.joint(n="char_l_pinkie_a", rad=2, r=True, p=(0.7,0.5,-9.8), o=(-4.7,-1.7,105.6))
        self.l_pinkie_b = mc.joint(n="char_l_pinkie_b", rad=2, r=True, p=(0.5,-0.5,-1.6), o=(-6.4,-23.3,-31.5))
        self.l_pinkie_c = mc.joint(n="char_l_pinkie_c", rad=2, r=True, p=(0.2,-0.3,-1.9), o=(-6.7,-10.3,-21.6))
        self.l_pinkie_d = mc.joint(n="char_l_pinkie_d", rad=2, r=True, p=(0.3,-0.1,-1.2))

        #Right Arm

        mc.select(self.neck)
        self.r_shoulder = mc.joint(n="char_r_shoulder", rad=4, r=True, p=(0,0,2.6), o=(0,65,165))
        self.r_upperArm = mc.joint(n="char_r_upperArm", rad=4, r=True, p=(-8.2,0.9,9.6), o=(-9,-9.6,1.1))
        self.r_lowerArm = mc.joint(n="char_r_lowerArm", rad=4, r=True, p=(-8.8,-1.4,23), o=(0,0,-26.5))
        self.r_wrist = mc.joint(n="char_r_wrist", rad=4, r=True, p=(-7,3.6,14.1), o=(0,-10,0))

        self.r_thumb_a = mc.joint(n="char_r_thumb_a", rad=2, r=True, p=(0.5,4.9,3), o=(-44.2,43.5,29.5))
        self.r_thumb_b = mc.joint(n="char_r_thumb_b", rad=2, r=True, p=(-0.1,-0.5,3), o=(10.4,-1.4,1.1))
        self.r_thumb_c = mc.joint(n="char_r_thumb_c", rad=2, r=True, p=(-0.3,-0.4,2.2), o=(9.3,-9.1,10.2))
        self.r_thumb_d = mc.joint(n="char_r_thumb_d", rad=2, r=True, p=(-0.4,-0.5,2.3))

        mc.select(self.r_wrist)
        self.r_index_a = mc.joint(n="char_r_index_a", rad=2, r=True, p=(-1.8,5.1,8), o=(-19.3,28.6,73.2))
        self.r_index_b = mc.joint(n="char_r_index_b", rad=2, r=True, p=(-0.4,-0.5,2.7), o=(9.1,-10.1,7.3))
        self.r_index_c = mc.joint(n="char_r_index_c", rad=2, r=True, p=(0.3,-0.7,2.3), o=(15.4,10.2,-10.5))
        self.r_index_d = mc.joint(n="char_r_index_d", rad=2, r=True, p=(0.2,-0.6,2.1))

        mc.select(self.r_wrist)
        self.r_middle_a = mc.joint(n="char_r_middle_a", rad=2, r=True, p=(-1.3,3.2,8.4), o=(-11.6,21.9,82.9))
        self.r_middle_b = mc.joint(n="char_r_middle_b", rad=2, r=True, p=(-0.3,0.1,3.2), o=(1.9,-6.2,5.1))
        self.r_middle_c = mc.joint(n="char_r_middle_c", rad=2, r=True, p=(0.5,-1.2,2.2), o=(22.5,19.2,-17.8))
        self.r_middle_d = mc.joint(n="char_r_middle_d", rad=2, r=True, p=(0.3,-0.4,2.3))

        mc.select(self.r_wrist)
        self.r_ring_a = mc.joint(n="char_r_ring_a", rad=2, r=True, p=(-1.2,0.9,9.7), o=(-5.9,6.5,100.6))
        self.r_ring_b = mc.joint(n="char_r_ring_b", rad=2, r=True, p=(0.9,-0.9,2.5), o=(10.2,25.1,-23.4))
        self.r_ring_c = mc.joint(n="char_r_ring_c", rad=2, r=True, p=(0.4,-0.5,2), o=(8.8,14.4,-22.3))
        self.r_ring_d = mc.joint(n="char_r_ring_d", rad=2, r=True, p=(0.2,-0.2,2.1))

        mc.select(self.r_wrist)
        self.r_pinkie_a = mc.joint(n="char_r_pinkie_a", rad=2, r=True, p=(0.7,0.5,9.8), o=(4.7,1.7,105.6))
        self.r_pinkie_b = mc.joint(n="char_r_pinkie_b", rad=2, r=True, p=(0.5,-0.5,1.6), o=(6.4,23.3,-31.5))
        self.r_pinkie_c = mc.joint(n="char_r_pinkie_c", rad=2, r=True, p=(0.2,-0.3,1.9), o=(6.7,10.3,-21.6))
        self.r_pinkie_d = mc.joint(n="char_r_pinkie_d", rad=2, r=True, p=(0.3,-0.1,1.2))

        # Left Leg

        mc.select(self.hips)
        self.l_upperLeg = mc.joint(n="char_l_upperLeg", rad=4, r=True, p=(-4.5,-0.4,-7.4), o=(0.3,182.8,1.1))
        self.l_lowerLeg = mc.joint(n="char_l_lowerLeg", rad=4, r=True, p=(35.3,-4.7,3.5), o=(0,0,-19.5))
        self.l_foot = mc.joint(n="char_l_foot", rad=4, r=True, p=(28.3,17.2,3.1), o=(-10.1,-2.8,15.6))
        self.l_toes = mc.joint(n="char_l_toes", rad=4, r=True, p=(8.6,-11,0), o=(15.1,5.2,-70.4))
        self.l_toeEnd = mc.joint(n="char_l_toeEnd", rad=4, r=True, p=(7.7,-2.5,-1.4))

        # Right Leg

        mc.select(self.hips)
        self.r_upperLeg = mc.joint(n="char_r_upperLeg", rad=4, r=True, p=(-4.5,-0.4,7.4), o=(-0.3,-182.8,1.1))
        self.r_lowerLeg = mc.joint(n="char_r_lowerLeg", rad=4, r=True, p=(35.3,-4.7,-3.5), o=(0,0,-19.5))
        self.r_foot = mc.joint(n="char_r_foot", rad=4, r=True, p=(28.3,17.2,-3.1), o=(10.1,2.8,15.6))
        self.r_toes = mc.joint(n="char_r_toes", rad=4, r=True, p=(8.6,-11,0), o=(-15.1,-5.2,-70.4))
        self.r_toeEnd = mc.joint(n="char_r_toeEnd", rad=4, r=True, p=(7.7,-2.5,1.4))

        ##############
        self.BuildMesh()
        
    def BuildMesh(self):
        # Torso And Head Mesh
        self.progressBar.setValue(20)
        self.hipsMesh = CreateUprightCube("char_hipsMesh", self.hips, self.spine, [20,1,11], [13,1,8])
        self.spineMesh = CreateUprightCube("char_spineMesh", self.spine, self.chest, [13,1,6], [13,1,8])
        self.chestMesh = CreateUprightCube("char_neckMesh", self.chest, self.neck, [13,1,10], [18,1,5])
        self.headMesh = createSphere("char_headMesh", self.head, self.headTop)

        # Left Arm Mesh
        self.progressBar.setValue(40)
        self.l_upperArmMesh = CreateRightCube("char_l_upperArmMesh", self.l_upperArm, self.l_lowerArm, [5,1,5], [2,1,2])
        self.l_lowerArmMesh = CreateRightCube("char_l_lowerArmMesh", self.l_lowerArm, self.l_wrist, [3,1,3], [2,1,2])

        self.l_thumbMesh_a = CreateRightCube("char_l_thumbMesh_a", self.l_thumb_a, self.l_thumb_b, [1,1,1], [1,1,1])
        self.l_thumbMesh_b = CreateRightCube("char_l_thumbMesh_b", self.l_thumb_b, self.l_thumb_c, [1,1,1], [1,1,1])
        self.l_thumbMesh_c = CreateRightCube("char_l_thumbMesh_c", self.l_thumb_c, self.l_thumb_d, [1,1,1], [1,1,1])

        self.l_indexMesh_a = CreateRightCube("char_l_indexMesh_a", self.l_index_a, self.l_index_b, [1,1,1], [1,1,1])
        self.l_indexMesh_b = CreateRightCube("char_l_indexMesh_b", self.l_index_b, self.l_index_c, [1,1,1], [1,1,1])
        self.l_indexMesh_c = CreateRightCube("char_l_indexMesh_c", self.l_index_c, self.l_index_d, [1,1,1], [1,1,1])

        self.l_middleMesh_a = CreateRightCube("char_l_middleMesh_a", self.l_middle_a, self.l_middle_b, [1,1,1], [1,1,1])
        self.l_middleMesh_b = CreateRightCube("char_l_middleMesh_b", self.l_middle_b, self.l_middle_c, [1,1,1], [1,1,1])
        self.l_middleMesh_c = CreateRightCube("char_l_middleMesh_c", self.l_middle_c, self.l_middle_d, [1,1,1], [1,1,1])

        self.l_ringMesh_a = CreateRightCube("char_l_ringMesh_a", self.l_ring_a, self.l_ring_b, [1,1,1], [1,1,1])
        self.l_ringMesh_b = CreateRightCube("char_l_ringMesh_b", self.l_ring_b, self.l_ring_c, [1,1,1], [1,1,1])
        self.l_ringMesh_c = CreateRightCube("char_l_ringMesh_c", self.l_ring_c, self.l_ring_d, [1,1,1], [1,1,1])

        self.l_pinkieMesh_a = CreateRightCube("char_l_pinkieMesh_a", self.l_pinkie_a, self.l_pinkie_b, [1,1,1], [1,1,1])
        self.l_pinkieMesh_b = CreateRightCube("char_l_pinkieMesh_b", self.l_pinkie_b, self.l_pinkie_c, [1,1,1], [1,1,1])
        self.l_pinkieMesh_c = CreateRightCube("char_l_pinkieMesh_c", self.l_pinkie_c, self.l_pinkie_d, [1,1,1], [1,1,1])

        # Right Arm Mesh
        self.progressBar.setValue(60)
        self.r_upperArmMesh = CreateRightCube("char_r_upperArmMesh", self.r_lowerArm, self.r_upperArm, [2,1,2], [5,1,5])
        self.r_lowerArmMesh = CreateRightCube("char_r_lowerArmMesh", self.r_wrist, self.r_lowerArm, [2,1,2], [3,1,3])

        self.r_thumbMesh_a = CreateRightCube("char_r_thumbMesh_a", self.r_thumb_b, self.r_thumb_a, [1,1,1], [1,1,1])
        self.r_thumbMesh_b = CreateRightCube("char_r_thumbMesh_b", self.r_thumb_c, self.r_thumb_b, [1,1,1], [1,1,1])
        self.r_thumbMesh_c = CreateRightCube("char_r_thumbMesh_c", self.r_thumb_d, self.r_thumb_c, [1,1,1], [1,1,1])

        self.r_indexMesh_a = CreateRightCube("char_r_indexMesh_a", self.r_index_b, self.r_index_a, [1,1,1], [1,1,1])
        self.r_indexMesh_b = CreateRightCube("char_r_indexMesh_b", self.r_index_c, self.r_index_b, [1,1,1], [1,1,1])
        self.r_indexMesh_c = CreateRightCube("char_r_indexMesh_c", self.r_index_d, self.r_index_c, [1,1,1], [1,1,1])

        self.r_middleMesh_a = CreateRightCube("char_r_middleMesh_a", self.r_middle_b, self.r_middle_a, [1,1,1], [1,1,1])
        self.r_middleMesh_b = CreateRightCube("char_r_middleMesh_b", self.r_middle_c, self.r_middle_b, [1,1,1], [1,1,1])
        self.r_middleMesh_c = CreateRightCube("char_r_middleMesh_c", self.r_middle_d, self.r_middle_c, [1,1,1], [1,1,1])

        self.r_ringMesh_a = CreateRightCube("char_r_ringMesh_a", self.r_ring_b, self.r_ring_a, [1,1,1], [1,1,1])
        self.r_ringMesh_b = CreateRightCube("char_r_ringMesh_b", self.r_ring_c, self.r_ring_b, [1,1,1], [1,1,1])
        self.r_ringMesh_c = CreateRightCube("char_r_ringMesh_c", self.r_ring_d, self.r_ring_c, [1,1,1], [1,1,1])

        self.r_pinkieMesh_a = CreateRightCube("char_r_pinkieMesh_a", self.r_pinkie_b, self.r_pinkie_a, [1,1,1], [1,1,1])
        self.r_pinkieMesh_b = CreateRightCube("char_r_pinkieMesh_b", self.r_pinkie_c, self.r_pinkie_b, [1,1,1], [1,1,1])
        self.r_pinkieMesh_c = CreateRightCube("char_r_pinkieMesh_c", self.r_pinkie_d, self.r_pinkie_c, [1,1,1], [1,1,1])

        # Left Leg Mesh
        self.progressBar.setValue(80)
        self.l_upperLegMesh = CreateUprightCube("char_l_upperLegMesh", self.l_upperLeg, self.l_lowerLeg, [10,1,10], [5,1,5])
        self.l_lowerLegMesh = CreateUprightCube("char_l_lowerLegMesh", self.l_lowerLeg, self.l_foot, [6,1,6], [3,1,3])
        self.l_footMesh = CreateUprightCube("char_l_footMesh", self.l_foot, self.l_toes, [4,1,4], [2,1,2])
        self.l_toesMesh = CreateUprightCube("char_l_toesMesh", self.l_toes, self.l_toeEnd, [3,1,3], [2,1,2])

        # Right Leg Mesh
        self.progressBar.setValue(100)
        self.r_upperLegMesh = CreateUprightCube("char_r_upperLegMesh", self.r_upperLeg, self.r_lowerLeg, [10,1,10], [5,1,5])
        self.r_lowerLegMesh = CreateUprightCube("char_r_lowerLegMesh", self.r_lowerLeg, self.r_foot, [6,1,6], [3,1,3])
        self.r_footMesh = CreateUprightCube("char_r_footMesh", self.r_foot, self.r_toes, [4,1,4], [2,1,2])
        self.r_toesMesh = CreateUprightCube("char_r_toesMesh", self.r_toes, self.r_toeEnd, [3,1,3], [2,1,2])
        self.progressBar.setValue(0)
#-----------------------------------------------------------------------------#
dialog = None

def create(docked=True):
    global dialog
    if dialog is None:
        dialog = UnityHumanoid()
    #if docked is True:
        #dialog.dock_ui()
    dialog.show()
    return dialog

def delete():
    print("close")
    global dialog
    if dialog is None:
        return
    dialog.deleteLater()
    dialog = None

#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

def CreateUprightCube(name, startJoint, endJoint, startScale, endScale):
    tempCube = mc.polyCube(n = name)
    tempFace = ('%s.f[1]' % (tempCube[0]))
    mc.select (tempFace)
    tempPos = mc.xform(endJoint, q=True, ws=True, t=True)
    mc.move(tempPos[0], tempPos[1], tempPos[2], r=True)
    tempPivot = mc.xform(endJoint, q=True, ws=True, t=True)
    tempRot = mc.xform(endJoint, q=True, ws=True, ro=True)
    mc.rotate(-tempRot[1],tempRot[0]+90,tempRot[2]-90,r=True, os=True, p=tempPivot)
    mc.scale(endScale[0],endScale[1],endScale[2],r=True,p=tempPivot)
    
    tempFace = ('%s.f[3]' % (tempCube[0]))
    mc.select (tempFace)
    tempPos = mc.xform(startJoint, q=True, ws=True, t=True)
    mc.move(tempPos[0], tempPos[1], tempPos[2], r=True)
    tempPivot = mc.xform(startJoint, q=True, ws=True, t=True)
    tempRot = mc.xform(startJoint, q=True, ws=True, ro=True)
    mc.rotate(-tempRot[1],tempRot[0]+90,tempRot[2]-90,r=True, os=True, p=tempPivot)
    mc.scale(startScale[0],startScale[1],startScale[2],r=True,p=tempPivot)
    
    mc.select(tempCube[0])
    mc.scale(1,0.85,1,r=True, ocp=True)
    
    return tempCube[0]
    
def CreateRightCube(name, startJoint, endJoint, startScale, endScale):
    tempCube = mc.polyCube(n = name)
    tempFace = ('%s.f[4]' % (tempCube[0]))
    mc.select (tempFace)
    tempPos = mc.xform(endJoint, q=True, ws=True, t=True)
    mc.move(tempPos[0], tempPos[1], tempPos[2], r=True)
    tempPivot = mc.xform(endJoint, q=True, ws=True, t=True)
    tempRot = mc.xform(endJoint, q=True, ws=True, ro=True)
    mc.rotate(-tempRot[1],tempRot[0]+90,tempRot[2]-90,r=True, os=True, p=tempPivot)
    mc.scale(endScale[0],endScale[1],endScale[2],r=True,p=tempPivot)
    
    tempFace = ('%s.f[5]' % (tempCube[0]))
    mc.select (tempFace)
    tempPos = mc.xform(startJoint, q=True, ws=True, t=True)
    mc.move(tempPos[0], tempPos[1], tempPos[2], r=True)
    tempPivot = mc.xform(startJoint, q=True, ws=True, t=True)
    tempRot = mc.xform(startJoint, q=True, ws=True, ro=True)
    mc.rotate(-tempRot[1],tempRot[0]+90,tempRot[2]-90,r=True, os=True, p=tempPivot)
    mc.scale(startScale[0],startScale[1],startScale[2],r=True,p=tempPivot)
    
    mc.select(tempCube[0])    
    return tempCube[0]
    
def createSphere(name, startJoint, endJoint):
    startHeight = mc.xform(startJoint, q=True, ws=True, t=True)
    endHeight = mc.xform(endJoint, q=True, ws=True, t=True)
    radius = (endHeight[1]-startHeight[1])/2
    tempSphere = mc.polySphere(n=name,r=radius)
    tempPos = (startHeight[0], startHeight[1]+radius, startHeight[2])
    mc.move(tempPos[0], tempPos[1], tempPos[2], r=True)
    return tempSphere[0]

class Defaults():
    def __init__(self, parent=None):
        self.testVar = ["wow", (0,0,0), (1,1,1)]
        self.legHeight = 1
        
        self.hips = ["char_hips", 4, False,[0,82.4,0], (-90,-5,90)]
        self.spine = ["char_spine", 4, True, (14.7,2.6,0), (0,0,0)]
        self.chest = ["char_chest", 4, True, (12.7,2.2,0), (0,0,0)]
        self.neck = ["char_neck", 4, True, (12.6,2.2,0), (0,0,15)]
        self.head = ["char_head", 4, True, (9.1,-4.1,0), (0,0,-10)]
        self.headTop = ["char_headTop", 4, True, (17.5,0,0), (0,0,0)]

        self.l_shoulder = ["char_l_shoulder", 4, True, (0,0,-2.6), (0,-65,165)]
        self.l_upperArm = ["char_l_upperArm", 4, True, (-8.2,0.9,-9.6), (9,9.6,1.1)]
        self.l_lowerArm = ["char_l_lowerArm", 4, True, (-8.8,-1.4,-23), (0,0,-26.5)]
        self.l_wrist = ["char_l_wrist", 4, True, (-7,3.6,-14.1), (0,10,0)]

        self.l_thumb_a = ["char_l_thumb_a", 2, True, (0.5,4.9,-3), (44.2,-43.5,29.5)]
        self.l_thumb_b = ["char_l_thumb_b", 2, True, (-0.1,-0.5,-3), (-10.4,1.4,1.1)]
        self.l_thumb_c = ["char_l_thumb_c", 2, True, (-0.3,-0.4,-2.2), (-9.3,9.1,10.2)]
        self.l_thumb_d = ["char_l_thumb_d", 2, True, (-0.4,-0.5,-2.3), (0,0,0)]

        self.l_index_a = ["char_l_index_a", 2, True, (-1.8,5.1,-8), (19.3,-28.6,73.2)]
        self.l_index_b = ["char_l_index_b", 2, True, (-0.4,-0.5,-2.7), (-9.1,10.1,7.3)]
        self.l_index_c = ["char_l_index_c", 2, True, (0.3,-0.7,-2.3), (-15.4,-10.2,-10.5)]
        self.l_index_d = ["char_l_index_d", 2, True, (0.2,-0.6,-2.1), (0,0,0)]

        self.l_middle_a = ["char_l_middle_a", 2, True, (-1.3,3.2,-8.4), (11.6,-21.9,82.9)]
        self.l_middle_b = ["char_l_middle_b", 2, True, (-0.3,0.1,-3.2), (-1.9,6.2,5.1)]
        self.l_middle_c = ["char_l_middle_c", 2, True, (0.5,-1.2,-2.2), (-22.5,-19.2,-17.8)]
        self.l_middle_d = ["char_l_middle_d", 2, True, (0.3,-0.4,-2.3), (0,0,0)]

        self.l_ring_a = ["char_l_ring_a", 2, True, (-1.2,0.9,-9.7), (5.9,-6.5,100.6)]
        self.l_ring_b = ["char_l_ring_b", 2, True, (0.9,-0.9,-2.5), (-10.2,-25.1,-23.4)]
        self.l_ring_c = ["char_l_ring_c", 2, True, (0.4,-0.5,-2), (-8.8,-14.4,-22.3)]
        self.l_ring_d = ["char_l_ring_d", 2, True, (0.2,-0.2,-2.1), (0,0,0)]

        self.l_pinkie_a = ["char_l_pinkie_a", 2, True, (0.7,0.5,-9.8), (-4.7,-1.7,105.6)]
        self.l_pinkie_b = ["char_l_pinkie_b", 2, True, (0.5,-0.5,-1.6), (-6.4,-23.3,-31.5)]
        self.l_pinkie_c = ["char_l_pinkie_c", 2, True, (0.2,-0.3,-1.9), (-6.7,-10.3,-21.6)]
        self.l_pinkie_d = ["char_l_pinkie_d", 2, True, (0.3,-0.1,-1.2), (0,0,0)]

        self.r_shoulder = ["char_r_shoulder", 4, True, (0,0,2.6), (0,65,165)]
        self.r_upperArm = ["char_r_upperArm", 4, True, (-8.2,0.9,9.6), (-9,-9.6,1.1)]
        self.r_lowerArm = ["char_r_lowerArm", 4, True, (-8.8,-1.4,23), (0,0,-26.5)]
        self.r_wrist = ["char_r_wrist", 4, True, (-7,3.6,14.1), (0,-10,0)]

        self.r_thumb_a = ["char_r_thumb_a", 2, True, (0.5,4.9,3), (-44.2,43.5,29.5)]
        self.r_thumb_b = ["char_r_thumb_b", 2, True, (-0.1,-0.5,3), (10.4,-1.4,1.1)]
        self.r_thumb_c = ["char_r_thumb_c", 2, True, (-0.3,-0.4,2.2), (9.3,-9.1,10.2)]
        self.r_thumb_d = ["char_r_thumb_d", 2, True, (-0.4,-0.5,2.3), (0,0,0)]

        self.r_index_a = ["char_r_index_a", 2, True, (-1.8,5.1,8), (-19.3,28.6,73.2)]
        self.r_index_b = ["char_r_index_b", 2, True, (-0.4,-0.5,2.7), (9.1,-10.1,7.3)]
        self.r_index_c = ["char_r_index_c", 2, True, (0.3,-0.7,2.3), (15.4,10.2,-10.5)]
        self.r_index_d = ["char_r_index_d", 2, True, (0.2,-0.6,2.1), (0,0,0)]

        self.r_middle_a = ["char_r_middle_a", 2, True, (-1.3,3.2,8.4), (-11.6,21.9,82.9)]
        self.r_middle_b = ["char_r_middle_b", 2, True, (-0.3,0.1,3.2), (1.9,-6.2,5.1)]
        self.r_middle_c = ["char_r_middle_c", 2, True, (0.5,-1.2,2.2), (22.5,19.2,-17.8)]
        self.r_middle_d = ["char_r_middle_d", 2, True, (0.3,-0.4,2.3), (0,0,0)]

        self.r_ring_a = ["char_r_ring_a", 2, True, (-1.2,0.9,9.7), (-5.9,6.5,100.6)]
        self.r_ring_b = ["char_r_ring_b", 2, True, (0.9,-0.9,2.5), (10.2,25.1,-23.4)]
        self.r_ring_c = ["char_r_ring_c", 2, True, (0.4,-0.5,2), (8.8,14.4,-22.3)]
        self.r_ring_d = ["char_r_ring_d", 2, True, (0.2,-0.2,2.1), (0,0,0)]

        self.r_pinkie_a = ["char_r_pinkie_a", 2, True, (0.7,0.5,9.8), (4.7,1.7,105.6)]
        self.r_pinkie_b = ["char_r_pinkie_b", 2, True, (0.5,-0.5,1.6), (6.4,23.3,-31.5)]
        self.r_pinkie_c = ["char_r_pinkie_c", 2, True, (0.2,-0.3,1.9), (6.7,10.3,-21.6)]
        self.r_pinkie_d = ["char_r_pinkie_d", 2, True, (0.3,-0.1,1.2), (0,0,0)]

        self.l_upperLeg = ["char_l_upperLeg", 4, True, (-4.5,-0.4,-7.4), (0.3,182.8,1.1)]
        self.l_lowerLeg = ["char_l_lowerLeg", 4, True, (35.3,-4.7,3.5), (0,0,-19.5)]
        self.l_foot = ["char_l_foot", 4, True, (28.3,17.2,3.1), (-10.1,-2.8,15.6)]
        self.l_toes = ["char_l_toes", 4, True, (8.6,-11,0), (15.1,5.2,-70.4)]
        self.l_toeEnd = ["char_l_toeEnd", 4, True, (7.7,-2.5,-1.4), (0,0,0)]

        self.r_upperLeg = ["char_r_upperLeg", 4, True, (-4.5,-0.4,7.4), (-0.3,-182.8,1.1)]
        self.r_lowerLeg = ["char_r_lowerLeg", 4, True, (35.3,-4.7,-3.5), (0,0,-19.5)]
        self.r_foot = ["char_r_foot", 4, True, (28.3,17.2,-3.1), (10.1,2.8,15.6)]
        self.r_toes = ["char_r_toes", 4, True, (8.6,-11,0), (-15.1,-5.2,-70.4)]
        self.r_toeEnd = ["char_r_toeEnd", 4, True, (7.7,-2.5,1.4), (0,0,0)]






