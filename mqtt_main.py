import json
import paho.mqtt.client as mqttclient
import shooting_star
import timer
import rainbow
import re

shooting = shooting_star
timer1 = timer
rain=rainbow
with open('secrets.json', 'r') as file:
    data=json.load(file)
    
    def on_connect(client, userdata, flags, reason_code, properties):
        print("connected with reason code: "+ str(reason_code))
        client.subscribe(data['client_id'])

    def on_message(client, userdata, msg):
        message= str(msg.payload)
        print(msg.payload)
        if "shootingstar" in message:
            print("shooting star!")
            shooting.shootingstar()
        if "timer" in message:
            print("timer starts")
            time= int(re.search(r'\d+', message).group())
            timer1.timer_start(time)
        if "rainbow" in message:
            print("rainbow")
            rain.rainbow_cycle(0.001)

    
    client=mqttclient.Client(mqttclient.CallbackAPIVersion.VERSION2)
    client.username_pw_set(data['username'], data['password'])
    client.on_connect=on_connect
    client.on_message= on_message

    client.connect(data['broker'], int(data['port']))

    client.loop_forever()