# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

for i in range(100):
    publish.single("escapp/mesures", "Hello la famille"+'i', hostname="broker.mqttdashboard.com")
print("Done")
