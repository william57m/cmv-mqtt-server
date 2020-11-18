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

Run is with docker
```

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
