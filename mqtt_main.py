import json
import paho.mqtt.client as mqttclient
import shooting_star
shooting = shooting_star

with open('secrets.json', 'r') as file:
    data=json.load(file)

    def on_connect(client, userdata, flags, reason_code, properties):
        print("connected with reason code: "+ str(reason_code))
        client.subscribe(data['client_id'])

    def on_message(client, userdata, msg):
        print(msg.payload)
        if "shootingstar" in str(msg.payload):
            print("shooting star!")
            shooting.shootingstar()
    
    client=mqttclient.Client(mqttclient.CallbackAPIVersion.VERSION2)
    client.username_pw_set(data['username'], data['password'])
    client.on_connect=on_connect
    client.on_message= on_message

    client.connect(data['broker'], int(data['port']))

    client.loop_forever()