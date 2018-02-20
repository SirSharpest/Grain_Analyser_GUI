from PyQt5.QtWidgets import QListWidgetItem, QListWidget


class WidgetList():
    """
    Little item manager class for
    use with item widget lists
    """

    def __init__(self, widget):
        self.widget = widget
        self.items = []

    def update(self, items):
        self.items = items
        self.widget.addItems(self.items)

    def get_items(self):
        return self.items
