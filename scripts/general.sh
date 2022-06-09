echo "[+] updating system"
sudo apt update -y 
sudo apt full-upgrade -y 

echo "[+] system updated"

sudo apt install nodejs -y
sudo apt install npm -y
sudo npm install pm2 -g
echo "[+] done"