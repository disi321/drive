# extract dir

echo "installing requirements"

sudo apt remove python-socketio -y
sudo apt remove python3-socketio -y
sudo pip install -r requirements.txt
sudo pip install "python-socketio[client]"

echo "dont forget to update the cred file"
echo "dont forget to add your componints to \'attack_management.json\'"
echo "done"