# APIS Model Satellite Live Data Visualisation
Coded in Python by Ömer Kural

## Table of Contents
- [Concept of Competition](https://github.com/omerkural/APIS-High-School-Model-Satellite-Competition#concept-of-apis-model-satellite-competition)
- [The Aim of Our Program](https://github.com/omerkural/APIS-High-School-Model-Satellite-Competition#the-aim-of-our-program)
- [What Our Program Does](https://github.com/omerkural/APIS-High-School-Model-Satellite-Competition#what-our-program-does)
- [Technologies](https://github.com/omerkural/APIS-High-School-Model-Satellite-Competition#technologies)
- [Credits](https://github.com/omerkural/APIS-High-School-Model-Satellite-Competition#credit)

## Concept of APIS Model Satellite Competition
The competition is the Turkish version of CanSat, which is held in USA. Unlike real satellites, model satellites are elevated to a low altitude (250 meters in this case) by a drone or a rocket. Their sizes and weights are smaller than a real satellite. There are some mechanical and electronical expectations in the design of the model satellite. The mechanical expectations are the carrier and the payloads (chicken eggs in this case) protection with a passive or active landing system. And of course the dimensions and weight values of the model sattelite must be kept within specified limits. The electronical expectations are air pressure, measurement of various data such as air temperature, altitude, photo and video recording, processing of the received data with the help of a microprocessor. These data must be sent to the ground station regularly. The data, received by the ground station, must be visualised live.

## The Aim of Our Program
The aim of our program is to visualise live data which is sent to our ground station computer from our model satellite.

## What Our Program Does
Our model satellite gathers the data by a microchip (ESP8266), then it sends it to our ground station via a wireless connectivity module (XBee Pro S2C). When our ground station computer gets the data, it updates the sat_data.csv file. As soon as our code detects the update, it animates the data accordingly on the Data Visualisation window. The `sat_data.csv` file currently contains unrealistic randomly generated values for testing purposes. 

## Technologies
- Python 3.9
- matplotlib
- pandas
- Excel

## Credit
- Code by Ömer Kural
- Logo by Aziz Sencer Arabacı
