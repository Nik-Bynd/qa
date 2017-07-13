---
# Pen Tests
---

## Zap via Behave

### Installation
Install pip, virtualenv, & libevent if not already installed.
```
sudo easy_install pip
pip install virtualenv
```
Create a  virtualbox, if you haven't before
```
virtualenv -p python3 env
```
Install dependancies while in the virtualenv
```
source env/bin/activate
pip install -r pen/requirements.txt
docker pull owasp/zap2docker-stable
```

### Running Tests
First start the docker machine with the api.key matching, -host matching ZAP_API_ADDRESS, and the ports matching ZAP_API_PORT from the root file accounts.py.
The command should look something like this
```
docker run -p 8090:8090 -i owasp/zap2docker-stable zap.sh -daemon -port 8090 -host 0.0.0.0 -config api.key=0123456789 -config api.addrs.addr.name=.* -config api.addrs.addr.regex=true -config scanner.strength=INSANE
BASE_URL=https://example.com ZAP_SERVER_PROXY=0.0.0.0:8090 python pen/zap_scanner.py
```

Run behave scenarios against scanner results:
```
behave qa/pen/
```

If you're not running under default domain in environment_variables.py
```
BASE_URL=https://example.com  behave pen/features
```

May switch to:
```
docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t https://www.example.com -n pen/custom.conf -r pen/testreport.html -z '-config scanner.strength=INSANE'
```
But not reading config. See https://github.com/zaproxy/zaproxy/wiki/ZAP-Baseline-Scan for progress file flag as well.


### Notes

While the docker session is running you can access settings at [http://0.0.0.0:8090/UI/core](http://0.0.0.0:8090/UI/core)