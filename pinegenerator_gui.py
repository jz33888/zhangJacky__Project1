from PySide6 import QtWidgets, QtCore, QtGui
from shiboken6 import wrapInstance

import pinetreegenerator

#maya window
def get_maya_main_win():
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window), QtWidgets.QWidget)

#gui class
class PineTreeGeneratorWin(QtWidgets.QDialog):

    def __init__(self):
        super(PineTreeGeneratorWin, self).__init__(
            parent=get_maya_main_win()
        )

        self.leaf_color = (0.08, 0.35, 0.05)
        self.trunk_color = (0.30, 0.12, 0.04) #set the default colors to green and brown respectively

        self.setWindowTitle("Pine Tree Generator")
        self.setMinimumWidth(350) 

        self.create_widgets()
        self.create_layout()
        self.connect_signals()

    #widgets
    def create_widgets(self):

        #leaf count
        self.leaf_count_input = QtWidgets.QSpinBox()
        self.leaf_count_input.setRange(1, 20)
        self.leaf_count_input.setValue(5)

        #tree height
        self.height_input = QtWidgets.QDoubleSpinBox()
        self.height_input.setRange(1, 100)
        self.height_input.setValue(8)

        # tree width
        self.width_input = QtWidgets.QDoubleSpinBox()
        self.width_input.setRange(1, 100)
        self.width_input.setValue(5)

        #tree quality
        self.quality_input = QtWidgets.QSpinBox()
        self.quality_input.setRange(3, 20)
        self.quality_input.setValue(8)

        #rows
        self.rows_input = QtWidgets.QSpinBox()
        self.rows_input.setRange(1, 20)
        self.rows_input.setValue(2)

        #columns
        self.columns_input = QtWidgets.QSpinBox()
        self.columns_input.setRange(1, 20)
        self.columns_input.setValue(2)

        #colors
        self.leaf_color_btn = QtWidgets.QPushButton("Choose Leaf Color")
        self.trunk_color_btn = QtWidgets.QPushButton("Choose Trunk Color")

        #make the forest! (generate)
        self.create_btn = QtWidgets.QPushButton("Generate Forest")

    #layout
    def create_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.form_layout = QtWidgets.QFormLayout()

        #inputs
        self.form_layout.addRow("Leaf Layers:", self.leaf_count_input)
        self.form_layout.addRow("Tree Height:", self.height_input)
        self.form_layout.addRow("Tree Width:", self.width_input)
        self.form_layout.addRow("Tree Quality:", self.quality_input)
        self.form_layout.addRow("Rows:", self.rows_input)
        self.form_layout.addRow("Columns:", self.columns_input)

        self.main_layout.addLayout(self.form_layout)

        self.main_layout.addWidget(self.leaf_color_btn)
        self.main_layout.addWidget(self.trunk_color_btn)

        self.main_layout.addWidget(self.create_btn)
        self.main_layout.addWidget(self.output_lbl)

        self.setLayout(self.main_layout)

    #connects the buttons
    def connect_signals(self):

        self.create_btn.clicked.connect(self.generate_forest)
        self.leaf_color_btn.clicked.connect(self.choose_leaf_color)
        self.trunk_color_btn.clicked.connect(self.choose_trunk_color)

    #color buttons
    def choose_leaf_color(self):
        color = QtWidgets.QColorDialog.getColor()

        if color.isValid():
            self.leaf_color = (
                color.redF(),
                color.greenF(),
                color.blueF()
            )

    def choose_trunk_color(self):
        color = QtWidgets.QColorDialog.getColor()

        if color.isValid():
            self.trunk_color = (
                color.redF(),
                color.greenF(),
                color.blueF()
            )

    #generate forest
    def generate_forest(self):

        pinetreegenerator.create_forest(
            leaf_count=self.leaf_count_input.value(),
            height=self.height_input.value(),
            width=self.width_input.value(),
            quality=self.quality_input.value(),
            rows=self.rows_input.value(),
            columns=self.columns_input.value(),
            leaf_color=self.leaf_color,
            trunk_color=self.trunk_color
        )


#open gui
win = PineTreeGeneratorWin()
win.show()
