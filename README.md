# MQTT Server to communicate with relay

## Regular installation

Clone the repository
```bash
git clone git@github.com:william57m/cmv-mqtt-server.git
cd cmv-mqtt-server
```

Install the requirements
```
pip install -r requirements.txt
```

Run it as a service
```bash
sudo sh ./setup.sh
sudo systemctl start cmv.service
```

Run it manually
```bash
python3 src/server.py
```

## Installation with docker

Run with docker
```
docker pull william57m/cmv-mqtt-server
docker run \
  --device /dev/gpiomem \
  -e MQTT_HOST='192.168.2.110' \
  william57m/cmv-mqtt-server:latest
```

## Build and publish

Build
```
docker build --tag william57m/cmv-mqtt-server .
```

Deploy
```
docker push william57m/cmv-mqtt-server
```

## MQTT Commands

Here is the list of command to publish to set the state of the CMV.

| topic               | payload                        | description                |
|---------------------|--------------------------------|-----------------------------
| cmv/fanrestroom/set | (Empty)                        | Toggle the restroom fan    |
| cmv/reset/set       | (Empty)                        | Reset the state of the CMV |

On each of these commands, the server publish `cmv/state/get` to return the state of the CMV, the message contains a JSON object.

Example of status payload
```json
{"fan_restroom": "on"}
```
