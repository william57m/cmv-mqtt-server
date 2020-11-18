service_path="/etc/systemd/system/cmv.service"

# Create service file
printf "%s\n" "[Unit]
Description=CMV
After=network.target

[Service]
User=root
ExecStart=/usr/bin/python3 /home/pi/cmv-mqtt-server/src/server.py

[Install]
WantedBy=multi-user.target" > "$service_path"

# Print
printf "cmv.service created\n" 

sleep 3

# Reload deamon and enable service
systemctl daemon-reload
systemctl enable cmv.service

# Print
printf "cmv.service enabled\n"
