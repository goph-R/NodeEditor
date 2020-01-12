from PySide2.QtCore import Qt, QSettings
from PySide2.QtWidgets import QDockWidget, QMainWindow, QTreeView, QPushButton

from node.Box import Box
from node.NodeFactory import NodeFactory
from node.NodeType import NodeType
from node.Node import Node

from PropertyEditor import PropertyEditor
from PropertyWidgetFactory import PropertyWidgetFactory
from SceneGraphModel import SceneGraphModel


class MainWindow(QMainWindow):

    def __init__(self, app):
        super(MainWindow, self).__init__()
        self._app = app

        # model
        nodeFactory = NodeFactory()
        rootNode = nodeFactory.create(NodeType.Box, 'Hips')
        childNode0 = nodeFactory.create(NodeType.Sphere, 'RightPirateLeg', rootNode)
        childNode1 = nodeFactory.create(NodeType.Box, 'RightPirateLeg_END', childNode0)
        childNode2 = nodeFactory.create(NodeType.Box, 'LeftFemur', rootNode)
        childNode3 = nodeFactory.create(NodeType.Box, 'LeftTibia', childNode2)
        childNode4 = nodeFactory.create(NodeType.Box, 'LeftFoot', childNode3)
        childNode5 = nodeFactory.create(NodeType.Box, 'LeftFoot_END', childNode4)
        self._model = SceneGraphModel(rootNode)

        # scene graph view
        self._treeView = QTreeView()
        self._treeView.setModel(self._model)
        self._treeView.setHeaderHidden(True)
        self._treeView.setAlternatingRowColors(True)

        dockWidget = QDockWidget()
        dockWidget.setWidget(self._treeView)
        dockWidget.setWindowTitle('Scene Graph')
        dockWidget.setObjectName('sceneGraph')
        sceneGraphToggleAction = dockWidget.toggleViewAction()
        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget)

        # property editor
        propertyEditor = PropertyEditor()
        propertyEditor.setup(self._model, PropertyWidgetFactory(), nodeFactory)

        dockWidget = QDockWidget()
        dockWidget.setWidget(propertyEditor)
        dockWidget.setWindowTitle('Property Editor')
        dockWidget.setObjectName('propertyEditor')
        propertyEditorToggleAction = dockWidget.toggleViewAction()
        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget)

        # menu
        menuBar = self.menuBar()
        menu = menuBar.addMenu('&File')
        exitAction = menu.addAction('E&xit')
        exitAction.triggered.connect(self._app.exit)
        menu.addAction(exitAction)
        menu = menuBar.addMenu('&Windows')
        menu.addAction(sceneGraphToggleAction)
        menu.addAction(propertyEditorToggleAction)
        menuBar.addMenu(menu)

        # central widget
        button = QPushButton()
        self.setCentralWidget(button)

        # selection change event
        self._treeView.selectionModel().currentChanged.connect(propertyEditor.changeSelection)

        # click event
        button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        indices = self._treeView.selectionModel().selectedIndexes()
        if len(indices) == 1:
            index = indices[0]
            self._model.set(index, Node.Name, 'CLICKED')
            node = index.internalPointer()
            if node.type() == NodeType.Box:
                self._model.set(index, Box.Width, 50)

    def closeEvent(self, event):
        self._app.exit()
