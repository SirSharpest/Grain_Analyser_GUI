echo "Generating main ui"
pyuic5 main_gui.ui > main_view.py
echo "Generating dataview ui"
pyuic5 dataview.ui > data_view.py
echo "Done!"
