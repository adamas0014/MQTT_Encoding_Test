  
import paho.mqtt.client as mqtt
import time
import struct
import keyboard

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
    pass

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

mqttc.on_log = on_log

mqttc.connect("192.168.12.1", 1883, 60)

mqttc.loop_start()

infot = mqttc.publish("controller/action", "standDown", qos=2)
infot.wait_for_publish()
time.sleep(2)
infot = mqttc.publish("controller/action", "standUp", qos=2)
infot.wait_for_publish()
time.sleep(2)
infot = mqttc.publish("controller/action", "recoverStand", qos=2)
infot.wait_for_publish()
time.sleep(2)
infot = mqttc.publish("controller/action", "walk", qos=2)
infot.wait_for_publish()
time.sleep(2)

while True:
    if(keyboard.is_pressed('q')):
        exit(0)
    elif(keyboard.is_pressed('w')):
        print("w")
        infot = mqttc.publish("controller/stick", b"*\x15\x01\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", qos=2) # shuffle left
        #infot = mqttc.publish("controller/stick", b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00", qos=2)  # tilt head dn
    elif(keyboard.is_pressed('s')):
        print("S")
        infot = mqttc.publish("controller/stick", b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\xf8\r?", qos=2) #fwd
        #infot = mqttc.publish("controller/stick", b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00", qos=2) # tilt head up
    elif(keyboard.is_pressed('a')):
        print('A')
        infot = mqttc.publish("controller/stick", b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\xf8\r\xbf", qos=2) #bwd
        # infot = mqttc.publish("controller/stick", b"\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00", qos=2) # turn right
    elif(keyboard.is_pressed('d')):
        print("D")
        # infot = mqttc.publish("controller/stick", b"$\xf8\r?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", qos=2) #move right
    elif(keyboard.is_pressed('e')):
        print("E")
        # infot = mqttc.publish("controller/stick", b"$\xf8\r?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", qos=2) #shuffle right
    else:
        print("Stop")
        infot = mqttc.publish("controller/stick", b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", qos=2)
    time.sleep(0.2)
"""   
  if(t_sign>0 and diff_tilt>50):
                    infot = mqttc.publish("controller/stick", b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00", qos=2)
                
                if(t_sign<0 and diff_tilt>50):
                    infot = mqttc.publish("controller/stick", b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00", qos=2)
                
                if(p_sign>0 and diff_pan>50):
                    infot = mqttc.publish("controller/stick", b"\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00", qos=2)
                
                if(p_sign<0 and diff_pan>50):
                    infot = mqttc.publish("controller/stick", b"\x00\x00\x00\x00\x00\x00\x80\xbf\x00\x00\x00\x00\x00\x00\x00\x00", qos=2)
                
                if(f_sign>0 and diff_focus>50):
                    infot = mqttc.publish("controller/stick", b"$\xf8\r?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", qos=2)
                
                if(f_sign<0 and diff_focus>50):
                    infot = mqttc.publish("controller/stick", b"*\x15\x01\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", qos=2)
                
                if(z_sign<0 and diff_zoom>50):
                    infot = mqttc.publish("controller/stick", b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\xf8\r?", qos=2)
                
                if(z_sign>0 and diff_zoom>50):
                    infot = mqttc.publish("controller/stick", b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\xf8\r\xbf", qos=2) """