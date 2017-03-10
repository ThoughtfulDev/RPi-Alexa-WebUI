# Rasperry Pi Alexa Web UI
##### A Web UI for starting the three Alexa Services
---
This little Web UI will start
1. Companion Service
2. Alexa Java Client (with automated Amazon Login)
3. WakeWordAgent

## So i could also start the manually too...why this?
You *could* but you don't want to login everytime via VNC/SSH (with X11) and start the three Services **AND** manually login to Amazon to obtain a token right?

This Web UI/Python API does it all for you with a click of a Button, including a automated Amazon Login to obtain the Token ;)

---
## How to use
### Prerequisites
* Installed and functioning [Alexa Avs Sample App](https://github.com/alexa/alexa-avs-sample-app)
* Python (included in Raspbian)
* Flask (`pip install Flask && pip install pyuserinput && pip install -U flask-cors`)
* NodeJS,NPM (you should already have this, its part of the avs sample app)

### Installing
1. Clone the Repository

`git clone https://github.com/ThoughtfulDev/RPi-Alexa-WebUI.git`

2. Install the node modules

`cd [Projectfolder]/UI && npm install`

3. Edit Amazon Credentials in Server/creds.cfg

4. Run the Python API
```
cd [Projectfolder]/Server
export FLASK_APP=main.py
flask run --host=0.0.0.0
```

5. Configure the Client

Change SECRET in `UI/client/config.js` to your desire (hashed with bcrypt). - Default Password is *1234*



6. Run the UI Dev Server
```
cd [Projectfolder]/UI
npm run dev
```

###### **OR**

6. Build the UI
```
cd [Projectfolder]/UI
npm build
```
Move content of UI/dist to your Web Server (you should know how this works...)

---

I know this is not perfect and secure and so on but i just needed something to control/restart the Alexa Services so there you go...

---
##Screenshots
![Login](http://i.epvpimg.com/veISbab.png)
![Dashboard](http://i.epvpimg.com/IGAdfab.png)
![Companion Service](http://i.epvpimg.com/hPt9cab.png)
![WakeWordAgent](http://i.epvpimg.com/NHFpfab.png)
