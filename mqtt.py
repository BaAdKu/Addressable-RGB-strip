import paho.mqtt.client as mqttclient

def on_connect(client, userdata, flags, reason_code, properties):
    print("connected with reason code: "+ str(reason_code))
    client.subscribe("")