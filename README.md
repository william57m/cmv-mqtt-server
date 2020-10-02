# MQTT Server to communicate with relay

## Setup

```bash
git clone git@github.com:william57m/cmv-mqtt-server.git
cd cmv-mqtt-server
```

Run it as a service
```bash
sudo sh ./setup.sh
sudo systemctl start cmv.service
```

Run it manually
```bash
python3 server.py
```

## MQTT Commands

Here is the list of command to publish to set the state of the CMV.

| topic               | payload                        | description                |
|---------------------|--------------------------------|-----------------------------
| cmv/fan/toggle      | auto, high, medium, low, quiet | Set the fan mode           |
| cmv/reset/set       | (Empty)                        | Reset the state of the AC  |

On each of these commands, the server publish `cmv/state/get` to return the state of the CMV, the message contains a JSON object.

Example of status payload
```json
{"fan_restroom": "on"}
```
