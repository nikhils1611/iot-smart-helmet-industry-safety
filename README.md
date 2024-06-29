# IOT BASED SMART HELMET FOR INDUSTRY SAFETY

 
<!-- ![GitHub](https://img.shields.io/github/license/hegdepavankumar/smart-garbage-monitoring-system-using-iot?style=flat) -->
<!-- ![GitHub top language](https://img.shields.io/github/languages/top/hegdepavankumar/smart-garbage-monitoring-system-using-iot?style=flat)
![GitHub last commit](https://img.shields.io/github/last-commit/hegdepavankumar/smart-garbage-monitoring-system-using-iot?style=flat)
![ViewCount](https://views.whatilearened.today/views/github/hegdepavankumar/smart-garbage-monitoring-system-using-iot.svg?cache=remove) -->

## Overview

IoT-based smart helmets offer a revolutionary solution across industries, not just in
construction, to mitigate accidents and enhance workplace safety. The prevalence of accidents
in various sectors underscores the urgent need for such technological innovations.Across
industries, accidents can occur due to a multitude of factors, ranging from machinery
malfunctions to human error. These incidents not only endanger the lives of workers but also
disrupt operations, leading to delays and financial losses. By integrating GPS sensors and
Emergency Buttons into helmets, workers environment can be instantly monitored by
supervisors in case of emergencies, facilitating swift response and rescue operations. This
real-time monitoring capability is valuable in any industry where workers face potential
hazards.Moreover, the benefits of wearing helmets extend beyond safety alone. Helmets
protect workers from falling objects, head injuries, and other workplace hazards, ensuring
their well-being and productivity.In today's rapidly evolving business landscape, completing
projects on time is paramount for sustained growth and competitiveness. IoT-based smart
helmets streamline operations by enhancing safety protocols, thereby enabling timely project
completion without compromising on worker welfare. As industries continue to expand and
evolve, embracing technological innovations like smart helmets becomes imperative. Whether
in manufacturing, logistics, or any other sector, ensuring the safety and efficiency of workers
remains a top priority for sustainable growth and success.


## Abstract

IOT-enabled worker safety helmet equipped with a web-based monitoring and alert system. The helmet integrates sensors for temperature, heart rate, humidity, and harmful gases, alongside GPS for real-time location tracking. Data collected by the sensors is transmitted to the ThingSpeak platform and visualized on a web interface, enabling supervisors to monitor worker safety in real-time. The system analyzes data and triggers alerts when unsafe conditions like high temperature, excessive heart rate, or gas presence are detected, facilitating proactive responses to ensure worker well-being. This application of IoT technology promotes workplace safety and protects workers from environmental hazards. The system incorporates various sensors, including temperature, heart rate, humidity, harmful gases, and GPS, providing a comprehensive approach to monitoring and ensuring the safety of workers in real-time.

<br>

# Real-Time Implemented Images: [click here to view](https://github.com/nikhils1611/iot-smart-helmet-industry-safety/tree/main/Project-images)

# Project Report: [click here to download](https://github.com/user-attachments/files/15880862/Report.Content.pdf)




<br>


## Hardware Requirements

1) ### Arduino Nano

![Picture3](https://github.com/nikhils1611/iot-smart-helmet-industry-safety/assets/149647718/f93d031d-296a-4b9b-beae-c53f51ba0f20)

<br>
The Arduino Nano emerges as a pivotal microcontroller board renowned for its compact design and formidable performance, catering to a broad spectrum of embedded applications and IoT projects. Anchored by the ATmega328 microcontroller, it embodies the quintessential Arduino ethos, delivering a harmonious blend of functionality and accessibility. With a clock speed of 16 MHz and ample memory resources boasting 32KB of flash memory and 2KB of SRAM, the Nano stands primed for executing tasks with finesse.

<br>

2) ### DHT11 Sensor

![Picture4](https://github.com/nikhils1611/iot-smart-helmet-industry-safety/assets/149647718/a0b9f219-2ec7-4865-b81a-83f792a797bb)

<br>

The DHT11 sensor stands as a cornerstone in the realm of temperature and humidity sensing, offering a cost-effective yet reliable solution for a myriad of projects spanning from environmental monitoring to home automation. Its compact form factor belies its robust capabilities, making it a favored choice among hobbyists and professionals alike. Featuring a calibrated digital signal output, the DHT11 sensor simplifies integration into projects by obviating the need for complex analog signal processing.

<br>

3) ### GPS Module

![image](https://user-images.githubusercontent.com/85627085/235178820-0b356695-8667-4847-88ac-0c4257ed9e4a.png)

<br>
These GPS modules are compatible with Arduino and Raspberry Pi, making it easy for you to start to try out. The Air 530 Module in Grove - GPS(Air 530) is a high-performance, highly integrated multi-mode satellite positioning and navigation module. It supports GPS / Beidou / Glonass / Galileo / QZSS / SBAS, which makes it suitable for GNSS positioning applications such as car navigation, smart wear, and drones. And Air530 module is also supports NMEA 0183 V4.1 protocol and compatible with previous versions. Meanwhile, the E-1612-UB module series of Grove - GPS Module is a family of stand-alone GPS receivers featuring the high-performance u-blox 5 positioning engine. The 50-channel u-blox 5 positioning engine boasts a Time-To-First-Fix ( TTFF ) of under 1 second. The dedicated acquisition engine, with over 1 million correlators, is capable of massive parallel time/frequency space searches, enabling it to find satellites instantly.

<br>
<br>

4) ### GSM/GPRS Module <br>
<br>

![image](https://user-images.githubusercontent.com/85627085/235181834-9da83f7b-62f2-4f13-a14d-0e01c9c88718.png)



<br>
  - What is GSM? <br>
  GSM (Global System for Mobile Communications, originally Groupe Spécial Mobile), is a standard developed by the European Telecommunications Standards Institute (ETSI).
It was created to describe the protocols for second-generation (2G) digital cellular networks used by mobile phones and is now the default global standard for mobile communications – with over 90% market share, operating in over 219 countries and territories.
<br>
  - What is GPRS? <br>
  General Packet Radio Service (GPRS) is a packet-oriented mobile data service on the 2G and 3G cellular communication system’s global system for mobile communications (GSM). GPRS was originally standardized by the European Telecommunications Standards Institute (ETSI) in response to the earlier CDPD and i-mode packet-switched cellular technologies. It is now maintained by the 3rd Generation Partnership Project (3GPP).


<br>
<br>



5) ###  MQ2 Gas Sensor
<br>


![Picture5](https://github.com/nikhils1611/iot-smart-helmet-industry-safety/assets/149647718/f2b0847c-8af6-497d-8c08-a8cbce28be77)

<br>

The MQ2 gas sensor emerges as a pivotal component in the domain of gas detection and monitoring, offering a versatile solution for a wide array of applications ranging from air quality assessment to industrial safety protocols. Characterized by its compact size and robust construction, the MQ2 sensor epitomizes reliability and performance, making it a staple choice among hobbyists, researchers, and industrial practitioners alike.

<br>


6) ### Connecting Wires

<br>

![image](https://user-images.githubusercontent.com/85627085/235187067-c6bc9a3e-2112-49f5-962f-e3123f8fb0d5.png)

<br>

A connecting wire allows the electric current from one point to another point without resistivity. The resistance of the connecting wire should always be near zero. Copper wires have low resistance and are therefore suitable for low resistance.


<br>


7) ### NodeMCU(Node MicroController Unit) 
<br>

![image](https://user-images.githubusercontent.com/85627085/235187953-d709a102-3247-4f2b-bbe8-c1292dd6dff6.png)

<br>

NodeMCU is an open-source firmware for which open-source prototyping board designs are available. The name "NodeMCU" combines "node" and "MCU" (micro-controller unit). Strictly speaking, the term "NodeMCU" refers to the firmware rather than the associated development kits. NodeMCU was created shortly after the ESP8266 came out. On December 30, 2013, Espressif Systems began production of the ESP8266.NodeMCU started on 13 Oct 2014, when Hong committed the first file of nodemcu-firmware to GitHub.Two months later, the project expanded to include an open-hardware platform when developer Huang R committed the Gerber file of an ESP8266 board, named devkit v0.9.

<br>

8) ### 16x2 LCD
 <br>
 
 ![image](https://user-images.githubusercontent.com/85627085/235443559-a2a7fdfc-966e-4357-b004-9edb3c93a655.png)


<br>
The Liquid Crystal library allows you to control LCDs that are compatible with the Hitachi HD44780 driver. There are many of them out there, and you can usually tell them by the 16-pin interface. The LCDs have a parallel interface, meaning that the microcontroller has to manipulate several interface pins at once to control the display.

<br>


9) ### Max30100 heart rate sensor
 <br>

![Picture6](https://github.com/nikhils1611/iot-smart-helmet-industry-safety/assets/149647718/bf998f63-b95d-45ee-b167-4a9be172a05d)

<br>
The MAX30100 heart rate sensor stands at the forefront of wearable health technology, offering a sophisticated yet accessible solution for monitoring vital signs and cardiovascular health. Engineered with precision and reliability in mind, the MAX30100 sensor caters to a diverse range of applications, from fitness trackers and smartwatches to medical-grade monitoring devices.
At its core, the MAX30100 sensor integrates advanced photoplethysmography (PPG) technology, leveraging an optical sensor to measure changes in blood volume through the skin. This enables the sensor to accurately detect heart rate and blood oxygen saturation (SpO2) levels in real time, providing valuable insights into cardiovascular health and overall well- being.

<br>




## Software Requirements

  - Windows 7/10/11 OS with Min 4GB RAM and 250GB Hard Disk <br>
  - [Arduino IDE](https://www.arduino.cc/en/software) <br>
  - Local Server and web Page for Monitoring<br>
  - Visual Studio Code <br>
<br>

## Implementation & Testing

  - <b><u>System Architecture </u></b><br>
  
  ![Screenshot 2024-06-29 193233](https://github.com/nikhils1611/iot-smart-helmet-industry-safety/assets/149647718/e5cb2073-d7b0-46c1-95a4-b9dac2cb4484)

  <br>
  
  On the completion of previous existing models, newly upgraded prototypes have been designed to overcome the existing limitations.<br><br>
1.<b><u>Sensing and Data Collection Unit</u></b> :
   -Nano 1 is equipped with a DHT11 sensor for temperature and humidity monitoring, an MQ2 gas sensor for detecting CO gas, and an ESP8266 Wi-Fi module for communication.
  -Additionally, Nano 1 features an LCD for local display of sensor readings.
  -Data collected from sensors (temperature, humidity, CO gas) is stored locally on Nano 1.
  -Nano 1 communicates with Nano 2 to receive heartbeat data.
  -Nano 2 is dedicated to monitoring heartbeat using an SpO2 heartbeat sensor.
  -It collects heartbeat data and transmits it to Nano 1 for further processing.<br>
  <br>
  <b><u>2.Data Processing and Communication Unit:</u></b>
  -Nano 1 receives data from both Nano 2 (heartbeat) and its own sensors (temperature, humidity, CO gas).
  -It aggregates all data and sends it to the ThingSpeak IoT cloud platform via the ESP8266 Wi-Fi module for real-time monitoring.
  -Additionally, Nano 1 communicates with Nano 3 to trigger emergency communication in case of an SOS event.
  -Nano 3 is independent and separate from Nano 1 and Nano 2.-	It features an A9G GSM module for emergency communication, a GPS module for location tracking, and an emergency SOS switch.<br>
  <br>
  <b><u>3.Monitoring Interface and Alerting Unit:</u></b>
  -Data collected by Nano 1 is sent to the ThingSpeak IoT cloud platform for storage and monitoring.
  -Caretakers can access a Flask-based web application to monitor the sensor readings remotely and in real-time.
  -When the SOS button is pressed, Nano 3 sends the GPS location to a smartphone via SMS using the A9G GSM module.
  -A LM2596 regulated power supply is connected to Nano 1 and Nano 3 to ensure stable power delivery.<br>
  
  <br>
  
  ## Source Code
  
 1) ### Code for sensor unit and wifi module
 
 <br>
 
 ```
#include<LiquidCrystal.h>
#include <SoftwareSerial.h>
#include "DHT.h"
#define DHTPIN A1     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);

SoftwareSerial esp8266(10, 11); // RX, TX of controller

#define DEBUG true
#define IP "184.106.153.149"// thingspeak.com ip
String Api_key = "GET /update?key=BRHXM8FXX082Q3DG"; //change it with your api key like "GET /update?key=Your Api Key"
int error;

#define DEBUG true

LiquidCrystal lcd(2, 3, 4, 5, 6, 7);

const int mqPin = A0;
int mqState = 0;

String h;

int hum;
int temp;
int f;

void setup()
{
  dht.begin();
  Serial.begin(115200);
  esp8266.begin(115200);
  pinMode(mqPin, INPUT);
  lcd.begin(16, 2);
  lcd.clear();
  lcd.print("  Smart Helmet");
  delay(1000);
  //=====================================
  send_command("AT+RST\r\n", 2000, DEBUG); //reset module
  send_command("AT+CWMODE=1\r\n", 1000, DEBUG); //set station mode
  send_command("AT+CWJAP=\"ABC\",\"11111111\"\r\n", 2000, DEBUG);
  //====================================
  delay(2000);
}

//void(* resetFunc) (void) = 0;//declare reset function at address 0

void loop()
{
  hum = dht.readHumidity();
  temp = dht.readTemperature();
  f = dht.readTemperature(true);
  if (isnan(hum) || isnan(temp) || isnan(f))
  {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  mqState = analogRead(mqPin);
  lcd.clear();
  lcd.print("HB:");
  lcd.print(h);
  lcd.print("bpm");
  lcd.setCursor(9, 0);
  lcd.print("CO:");
  lcd.print(mqState);
  lcd.setCursor(0, 1);
  lcd.print("H:");
  lcd.print(hum);
  lcd.print("%");
  lcd.setCursor(9, 1);
  lcd.print("T:");
  lcd.print(temp);

  if (Serial.find('$'))
  {
    // Serial.println("Recieved $");
    h = Serial.readStringUntil('&');
    Serial.print("Heart rate:");
    Serial.print(h);
    Serial.println("bpm");
  }
  /*  if (Serial.find('&'))
    {
      // Serial.println("Recieved &");
      o  = Serial.readStringUntil('@');
      Serial.print("SpO2:");
      Serial.print(o);
      Serial.println("%");
    }
  */
  Serial.print("Carbon Monoxide:");
  Serial.println(mqState);
  Serial.print("Humidity:");
  Serial.println(hum);
  Serial.print("Temperature:");
  Serial.println(temp);

  if ( h > "30")
  {
    updatedata();

  }

  delay(100);
}

void updatedata()
{
  String command = "AT+CIPSTART=\"TCP\",\"";
  command += IP;
  command += "\",80";
  Serial.begin(115200);
  delay(200);
  esp8266.begin(115200);
  delay(200);
  Serial.println(command);
  delay(200);
  esp8266.println(command);
  delay(2000);
  if (esp8266.find("Error")) {
    return;
  }



  command = Api_key ;

  command += "&field1=";
  command += String(h);

  command += "&field2=";
  command += String(mqState);

  command += "&field3=";
  command += String(hum);

  command += "&field4=";
  command += String(temp);
  /*
          command += "&field5=";
          command += String(t5);

          command += "&field6=";
          command += String(t6);



          command += "&field7=";
          command += String(t7);
          command += "&field8=";
          command += String(t8);



            command += "&field9=";
            command += String(t9);
            command += "&field10=";
            command += String(t10);

  */
  command += "\r\n\r\n\r\n\r\n\r\n\r\n";
  Serial.print("AT+CIPSEND=");
  esp8266.print("AT+CIPSEND=");
  Serial.println(command.length());
  esp8266.println(command.length());

  if (esp8266.find(">")) {
    delay(200);
    Serial.print(command);
    delay(200);
    esp8266.print(command);
    delay(200);
    esp8266.println("AT+RST");
    delay(200);
    esp8266.println("AT");
    delay(200);
    esp8266.println("AT");
    delay(200);

  }

  else {

    Serial.println("AT+CIPCLOSE");
    esp8266.println("AT+CIPCLOSE");
    //Resend...
    error = 1;
  }
}


String send_command(String command, const int timeout, boolean debug)
{
  esp8266.begin(115200);
  String response = "";
  esp8266.print(command);
  long int time = millis();
  while ( (time + timeout) > millis())
  {
    while (esp8266.available())
    {
      char c = esp8266.read();
      response += c;
    }
  }
  if (debug)
  {
    Serial.print(response);
  }
  return response;
}

 ```
  
2) ### Code for GPS MOdule

<br>

```
#include <SoftwareSerial.h>
SoftwareSerial esp8266(2,3);
 #include <LiquidCrystal.h>
LiquidCrystal lcd(8,9,10,11,12,13);//RS,EN,D4,D5,D6,D7
#include <Servo.h>
#define buzzer 4
#define trigPin1 A4  //// front
#define echoPin1 A5
int lvl1=0;
long duration, distance,sensor1,sensor2,sensor3; // us variable
int onetime=0,onetime1=0 ;
int wet=0,moisture=0,object=0,cabin2=0,c1=0,c2=0;
int powers=0,powers1=0,powers2=0,powers3=0;
void setup() 
{
 Serial.begin(115200);
 esp8266.begin(9600);
 lcd.begin(16, 2);//initializing LCD
 lcd.setCursor(0,0); 
 lcd.print("Automatic WASTE");
 delay(3000);
 pinMode(buzzer,OUTPUT);
 pinMode(trigPin1, OUTPUT);
 pinMode(echoPin1, INPUT);
 delay(3000);
}
void loop()
{
 ultrasensor(trigPin1, echoPin1);
 sensor1 = distance;  
 delay(10);
 esp8266.println(sensor1);
 lvl1=(20-sensor1)*7;
 esp8266.println(lvl1);
 if(lvl1<0){lvl1=0;}
 if(lvl1>100){lvl1=100;}
 lcd.clear();
 lcd.setCursor(0,0); 
 lcd.print("Dustbin Level");
 lcd.setCursor(6,1); 
 lcd.print(lvl1);
 delay(1000);
 if(lvl1>70)
 {      
  if(onetime==0)
  {
    lcd.clear();
   lcd.setCursor(0,0); 
   lcd.print("-send msg-");
   digitalWrite(buzzer,HIGH); 
   tracking(); 
   digitalWrite(buzzer,LOW);
   onetime=1;
  }
 }  
 else
 {
  onetime=0;
 }
 ////////////////////////////////////////////////
 String data = "";
 data+= "{";
 data+= "\"anloga\":";
 data+= "\""+String(lvl1)+"\",";
 data+= "\"anlogb\":";
 data+= "\""+String(powers)+"\",";
 data+= "\"anlogc\":";
 data+= "\""+String(powers1)+"\",";
 data+= "\"anlogd\":";
 data+= "\""+String(powers2)+"\"";
 data+= "}";
 Serial.print('\r');
 Serial.print(data);
 delay(10);
 Serial.print('\n');
 delay(200);
 ///////////////////////////////////////////////   
}
 void init_sms()
 {
  esp8266.println("AT+CMGF=1");
  delay(400);
  esp8266.println("AT+CMGS=\"+919X083X52XX\"");   // use your 10 digit cell no. here //
  delay(400);
 }
 void init_sms1()
 {
  esp8266.println("AT+CMGF=1");
  delay(400);
  esp8266.println("AT+CMGS=\"+918XX227XX8X\"");   // use your 10 digit cell no. here
  delay(400);
 }  
 void send_data(String message)
 {
  esp8266.println(message);
  delay(200);
 }
 
 void send_sms()
 {
  esp8266.write(26);
 }
  void tracking()
 {
  init_sms();
  send_data("dustbin-001  is almost full:\n");
  send_sms();
  delay(6000);
  init_sms1();
  send_data("dustbin-001  is almost full:\n");
  esp8266.print(" Level in %");
   esp8266.print(lvl1);
  send_sms();
  delay(6000);
 }
 void ultrasensor(int trigPin,int echoPin)
 { 
  digitalWrite(trigPin, LOW);  // Added this line
  delayMicroseconds(2); // Added this line
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10); // Added this line
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) / 29.1;
 }

```
## Instructions/Setup

- Download and install Arduino IDE
- Make all the necessary connections
- Compile and upload the code to the board
<br>

## Conclusion

The project aims to enhance worker safety through an IoT-enabled helmet equipped with various sensors and a web-based monitoring system. Nano 1, the sensing and data collection unit, features sensors for temperature, humidity, CO gas, and communicates with Nano 2 for heartbeat monitoring. Data is processed on Nano 1 and transmitted to ThingSpeak for real- time monitoring. In case of emergencies, Nano 3 triggers communication via SMS with GPS location. The system provides comprehensive monitoring of environmental conditions and worker well-being, promoting proactive responses to ensure safety.The integration of Nano units facilitates seamless data collection, processing, and communication, enabling real-time monitoring of worker safety. By leveraging IoT technology, supervisors can remotely monitor sensor readings through a user-friendly web interface. In emergencies, the system enables swift communication of the worker's location, enhancing response times. Overall, the project underscores the importance of IoT in promoting workplace safety and mitigating environmental hazards, ultimately safeguarding the well-being of workers.
  

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Creators [🔝](# smart-garbage-monitoring-system-using-iot)

This Project is Created by:-

  - [Nikhil Kumar S](https://github.com/nikhils1611) [Team Leader]
  - [Nuthan Kumar S](https://github.com/)
  - [Pydi Vineel ](https://github.com/)
  - [Sreenivaslu reddy](https://github.com/)



<br>
<h3 align="center">Show some &nbsp;❤️&nbsp; by starring some of the repositories!</h3>
<br>


 <!-- Support Me --> 

 
<!-- if you like what I do, maybe consider buying me a coffee 🥺👉👈

<a href="https://www.buymeacoffee.com/hegdepavankumar" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" width="150" ></a> -->



