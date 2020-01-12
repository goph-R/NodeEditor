from PySide2.QtCore import QAbstractItemModel, QModelIndex, Qt


class SceneGraphModel(QAbstractItemModel):

    def __init__(self, rootNode):
        super(SceneGraphModel, self).__init__()
        self._rootNode = rootNode

    def parent(self, index):
        node = index.internalPointer()
        parentNode = node.parent()
        if parentNode == self._rootNode:
            return QModelIndex()
        return self.createIndex(parentNode.row(), 0, parentNode)

    def index(self, row, column, parent):
        if not parent.isValid():
            parentNode = self._rootNode
        else:
            parentNode = parent.internalPointer()
        childNode = parentNode.child(row)
        if childNode:
            return self.createIndex(row, column, childNode)
        else:
            return QModelIndex()

    def data(self, index, role):
        if not index.isValid():
            return None
        node = index.internalPointer()
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return node.data(index.column())

    def setData(self, index, value, role=Qt.EditRole):
        if role != Qt.EditRole or not index.isValid():
            return False
        node = index.internalPointer()
        node.setData(index.column(), value)
        self.dataChanged.emit(index, index)
        return True

    def set(self, index, column, value):
        node = index.internalPointer()
        node.setData(column, value)
        propertyIndex = self.index(index.row(), column, index.parent())
        self.dataChanged.emit(propertyIndex, propertyIndex)


    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            return 'Scene'

    def rowCount(self, parent):
        if not parent.isValid():
            parentNode = self._rootNode
        else:
            parentNode = parent.internalPointer()
        return parentNode.childCount()

    def columnCount(self, parent):
        return 1

    def flags(self, index):
        result = Qt.ItemIsEnabled | Qt.ItemIsSelectable
        parentIndex = index.parent()
        if parentIndex.isValid():
            result |= Qt.ItemIsEditable
        return result

