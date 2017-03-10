from flask import Flask, abort
from flask_cors import CORS, cross_origin
from pykeyboard import PyKeyboard
from flask import Response
import json
import os, subprocess, sys, threading, signal
import time
app = Flask(__name__)
CORS(app)

compThread = 0
javaThread = 0
wakeThread = 0
compStarted = False
javaStarted = False
wakeStarted = False


class threadService (threading.Thread):
    "Class for the threads"
    def __init__(self, bashFile, service):
        "Constructor"
        threading.Thread.__init__(self)
        self.bashFile = bashFile
        self.service = service
        self.stopped = False
        self.p = 0

    def run(self):
        "entry point"
        cmd = "sh bash/" + self.bashFile
        self.p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn = os.setsid)
        if os.path.exists('log/' + self.service + '.log'):
            os.remove('log/' + self.service + '.log')
            open('log/' + self.service + '.log', 'a').close()
        else:
            open('log/' + self.service + '.log', 'a').close()

        with self.p.stdout:
            for line in iter(self.p.stdout.readline, b''):
                with open('log/' + self.service + '.log', 'a') as f:
                    f.write(line)

        self.p.wait()

    def stop(self):
        pid = self.p.pid
        os.killpg(os.getpgid(self.p.pid), signal.SIGTERM)
        return pid


class AWSKeyAutmoation (threading.Thread):
    "Class for the threads"
    def __init__(self):
        "Constructor"
        threading.Thread.__init__(self)

    def run(self):
        "entry point"
        data = []
        with open('creds.cfg') as f:
            data = f.readlines()
        data = [x.strip() for x in data]
        k = PyKeyboard()
        time.sleep(30)
        k.tap_key(k.enter_key)
        time.sleep(20)
        k.type_string(data[0])
        time.sleep(1)
        k.tap_key(k.tab_key)
        time.sleep(1)
        k.type_string(data[1])
        time.sleep(1)
        k.tap_key(k.enter_key)
        time.sleep(10)
        k.press_keys([k.alt_key,k.function_keys[4]])
        time.sleep(7)
        k.tap_key(k.enter_key)
        time.sleep(2)
        with open('log/javaclient.log', 'a') as f:
            f.write('[INFO] Got AWS Key')




@app.route('/')
def notSupported():
    "Standart response"
    abort(501)


@app.route('/service/companion/start', methods = ['GET'])
def startComp():
    global compThread
    global compStarted
    compThread = threadService('startComp.sh', 'companion')
    compThread.start()
    compStarted = True
    resp = Response('OK', status=200, mimetype='text/plain')
    return resp

@app.route('/service/companion/stop', methods = ['GET'])
def stopComp():
    global compThread
    global compStarted
    pid = compThread.stop()
    resp = {
        'message': 'OK',
        'pid': pid
    }
    compStarted = False
    resp = json.dumps(resp)
    r = Response(resp, status=200, mimetype='application/json')
    return r

@app.route('/service/companion/log', methods = ['GET'])
def getCompLog():
    raw = open('log/companion.log').read().splitlines()
    log = ''
    for line in raw:
        log = log + str(line) + '<br/>'
    r = Response(log, status=200, mimetype='text/plain')
    return r

@app.route('/service/companion/status', methods = ['GET'])
def getCompStatus():
    resp = {
        'active': compStarted
    }
    return Response(json.dumps(resp), status=200, mimetype='application/json')
#-------------------------------------------------------------------------



# java
#-------------------------------------------------------------------------

@app.route('/service/javaclient/start', methods = ['GET'])
def startJava():
    global javaThread
    global javaStarted
    javaThread = threadService('startJavaClient.sh', 'javaclient')
    javaThread.start()
    javaStarted = True
    awsThread = AWSKeyAutmoation()
    awsThread.start()
    resp = Response('OK', status=200, mimetype='text/plain')
    return resp

@app.route('/service/javaclient/stop', methods = ['GET'])
def stopJava():
    global javaThread
    global javaStarted
    pid = javaThread.stop()
    resp = {
        'message': 'OK',
        'pid': pid
    }
    javaStarted = False
    resp = json.dumps(resp)
    r = Response(resp, status=200, mimetype='application/json')
    return r

@app.route('/service/javaclient/log', methods = ['GET'])
def getJavaLog():
    raw = open('log/javaclient.log').read().splitlines()
    log = ''
    for line in raw:
        log = log + str(line) + '<br/>'
    r = Response(log, status=200, mimetype='text/plain')
    return r

@app.route('/service/javaclient/status', methods = ['GET'])
def getJavaStatus():
    resp = {
        'active': javaStarted
    }
    return Response(json.dumps(resp), status=200, mimetype='application/json')
# -------------------------------------------------------------------------


# wakeword
# -------------------------------------------------------------------------

@app.route('/service/wakewordagent/start', methods = ['GET'])
def startWWA():
    global wakeThread
    global wakeStarted
    wakeThread = threadService('startWakeWordAgent.sh', 'wakewordagent')
    wakeThread.start()
    wakeStarted = True
    resp = Response('OK', status=200, mimetype='text/plain')
    return resp

@app.route('/service/wakewordagent/stop', methods = ['GET'])
def stopWWA():
    global wakeThread
    global wakeStarted
    pid = wakeThread.stop()
    resp = {
        'message': 'OK',
        'pid': pid
    }
    wakeStarted = False
    resp = json.dumps(resp)
    r = Response(resp, status=200, mimetype='application/json')
    return r

@app.route('/service/wakewordagent/log', methods = ['GET'])
def getWWALog():
    raw = open('log/wakewordagent.log').read().splitlines()
    log = ''
    for line in raw:
        log = log + str(line) + '<br/>'
    r = Response(log, status=200, mimetype='text/plain')
    return r

@app.route('/service/wakewordagent/status', methods = ['GET'])
def getWWAStatus():
    resp = {
        'active': wakeStarted,
    }
    return Response(json.dumps(resp), status=200, mimetype='application/json')
#-------------------------------------------------------------------------
