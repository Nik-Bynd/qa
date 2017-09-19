# End-to-End

## Introduction

Test written using [Behave Framework](http://pythonhosted.org/behave/) and [Hamcrest Assertions](https://github.com/hamcrest/PyHamcrest)

## Install
*(if you didn't use main setup.sh script)*
Create a virtualenv if not already.
```
virtualenv -p python3 qa/env
```
Install dependencies to virtualenv.
```
source env/bin/activate
pip3 install -r qa/functional/requirements.txt
curl -L https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-macos.tar.gz | tar xz -C qa/env/bin
curl -L https://chromedriver.storage.googleapis.com/2.30/chromedriver_mac64.zip | tar xz -C qa/env/bin
```
* pip install chromedriver_installer==0.0.6 not working in python 3.6 due to certificate issue

#### Safari setup
To test in Safari you must turn on automation in the dev menu, (Develop > Allow Remote Automation) and directly run webdriver once to authorize permissions (In Terminal: /usr/bin/safaridriver -p 8000).

## Running Tests
Be sure to source virtualenv (```source qa/env/bin/activate```) before running tests.

#### Run all tests.

```
behave qa/functional/features
```

#### Changing domain or browser
The Driver default, base url, and other variables are being defaulted in the environment_variables.py but can be overwritten on the command line.
```
DRIVER='chrome' BASE_URL='http://google.com' behave qa/functional/features
```

#### Running Single files or tests
Behave breaks things up by **features**. A feature is what it sounds like, it might have several user stories or as Behave calls them **scenarios**,
You can include or exclude tests with the ```--include``` or ```--exclude``` flags that use feature file names.
```
behave qa/functional/features -i google -e example
```
Or run a single scenario from a feature with the ```--name``` flag:
```
behave qa/functional/features -n 'This is a scenario name'
```

Currently there's a bug in selenium that causes an error on remote chrome standalone. If you need to run the remote docker selenium standalone image do it on the 3.4 tag.
```
docker run -p 4444:4444 selenium/standalone-chrome:3.4
```

And this should work for Sauce Labs (Note that the parenthesis on SL_DC on mandatory on this command when they're optional for the rest of example variables.) You of course have to change the url where is says *YOUR_SAUCE_USERNAME* and *YOUR_SAUCE_ACCESS_KEY* to credentials:
```
SELENIUM=http://YOUR_SAUCE_USERNAME:YOUR_SAUCE_ACCESS_KEY@ondemand.saucelabs.com:80/wd/hub SL_DC='{"platform": "Mac OS X 10.9", "browserName": "chrome", "version": "31"}'  DRIVER=saucelabs BASE_URL=https://bynd.com behave qa/functional/features
```
\* haven't tried sauce yet.


#### Running for Allure Reports
```
BASE_URL=https://google.com behave -f allure_behave.formatter:AllureFormatter -o qa/utilities/allure/allure_result_folder ./qa/functional/features
```



### Notes about example tests.

* Useful documentation about selenium and webdriver can be found [here](http://selenium-python.readthedocs.io/) (don't miss the webdriver part [here](http://selenium-python.readthedocs.io/api.html#locate-elements-by)) I find the better than the [Selenium documentation](http://www.seleniumhq.org/docs/) but you should check that out as well. For Behave I suggest [behave integration](http://behave.readthedocs.io/en/latest/tutorial.html), [behave features](https://pythonhosted.org/behave/gherkin.html#given-when-then-and-but), and beware they hide really important stuff in the appendix.

* To stop getting Python Permission prompts on Chromedriver launch follow these [instructions](http://bd808.com/blog/2013/10/21/creating-a-self-signed-code-certificate-for-xcode/) to create a certificate. Run `. env/bin/activate` once and then stop it to get in the virtual env. It should now say `(env)` on Terminal command line, then run this command, replacing *NAME* with the name of the certificate you created.
```
codesign -s NAME -f `which python`
```

* You may need to change the install gitlab-ci file or makefile for the server environment to a linux or other OS, e.g.:
```
curl -L https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz | tar xz -C qa/env/bin
curl -L https://chromedriver.storage.googleapis.com/2.30/chromedriver_linux64.zip > chromedriver.zip && unzip chromedriver.zip &&  cp -i chromedriver.zip qa/env/bin && rm chromedriver.zip
```

* I can't promise I will keep it up to date but I have a login to google Behave Step in qa/functional/steps/login. It is dependent on setting up environmental variables. pass in the name of the account, e.g. `editor`. You then need to import the step into the tests named stepfile or common, e.g. `from qa.functional.features.steps.login import LoginPage`. But the IAP setup mentioned in the main readme is definitely a better option if you are using chrome and chrome emulator only.