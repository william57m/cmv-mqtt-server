import json
import paho.mqtt.client as mqtt
import re

from cmv import CMV

# MQTT Settings
mqtt_host = 'localhost'
mqtt_port = 1883


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {str(rc)}')

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe('cmv/#')


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

  print(f'Received: {msg.topic} / Message: {msg.payload.decode("utf-8")}')

  # Command to trigger publish update
  if msg.topic == 'cmv/state/send':
    state = cmv.get_state()
    client.publish('cmv/state/get', json.dumps(state))

  # Update settings
  if msg.topic == 'cmv/fanrestroom/set':
    cmv.toggle_fan_restroom()
  elif msg.topic == 'cmv/reset/set':
    cmv.reset()

  # Publish update
  if re.match(r'cmv/.*/set', msg.topic):
    state = cmv.get_state()
    client.publish('cmv/state/get', json.dumps(state))

# Init CMV
cmv = CMV()

# Init MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_host, mqtt_port, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
