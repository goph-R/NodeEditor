from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDockWidget, QMainWindow, QTreeView

from component.ComponentType import ComponentType
from node.NodeFactory import NodeFactory
from node.NodeType import NodeType

from PropertyEditor import PropertyEditor
from field.FieldFactory import FieldFactory
from SceneGraphModel import SceneGraphModel
from scene.SceneView import SceneView


class MainWindow(QMainWindow):

    def __init__(self, app):
        super(MainWindow, self).__init__()
        self._app = app
        self._selectedIndex = None

        # model
        nodeFactory = NodeFactory()
        rootNode = nodeFactory.create(NodeType.General, 'Root')
        # for i in range(10000):  # for testing
        childNode0 = nodeFactory.create(NodeType.General, 'RightPirateLeg', rootNode)
        childNode1 = nodeFactory.create(NodeType.General, 'RightPirateLeg_END', childNode0)
        childNode2 = nodeFactory.create(NodeType.General, 'LeftFemur', rootNode)
        childNode3 = nodeFactory.create(NodeType.Sphere, 'LeftTibia', childNode2)
        childNode4 = nodeFactory.create(NodeType.Sphere, 'LeftFoot', childNode3)
        transform = childNode4.component(ComponentType.Transform)
        qTransform = transform.component()
        translation = qTransform.translation()
        translation.setX(5)
        qTransform.setTranslation(translation)

        # childNode5 = nodeFactory.create(NodeType.Box, 'LeftFoot_END', childNode4)
        self._model = SceneGraphModel(rootNode)

        self._sceneView = SceneView(rootNode.entity())
        self._container = self.createWindowContainer(self._sceneView)

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
        propertyEditor = PropertyEditor(self._model, nodeFactory, FieldFactory())

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
        exitAction.triggered.connect(self.close)
        menu.addAction(exitAction)
        menu = menuBar.addMenu('&Windows')
        menu.addAction(sceneGraphToggleAction)
        menu.addAction(propertyEditorToggleAction)
        menuBar.addMenu(menu)

        # central widget
        #button = QPushButton()
        self.setCentralWidget(self._container)

        # selection change event
        selectionModel = self._treeView.selectionModel()
        selectionModel.currentChanged.connect(propertyEditor.changeSelection)

        # click event
        #button.clicked.connect(self.buttonClicked)

    def selectedNode(self):
        indices = self._treeView.selectedIndexes()
        result = None
        if len(indices) == 1:
            self._selectedIndex = indices[0]
            result = self._selectedIndex.internalPointer()
        return result

    def commitChange(self):
        self._model.dataChanged.emit(self._selectedIndex, self._selectedIndex)

    def closeEvent(self, event):
        self._app.exit()

    # data change example
    def buttonClicked(self):
        node = self.selectedNode()
        if not node:
            return
        general = node.component(ComponentType.General)
        general.setName('CLICKED')
        self.commitChange()
