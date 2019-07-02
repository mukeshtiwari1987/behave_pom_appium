# Python Behave Local BrowserStack
This framework utilizes Behaviour Driven Development (BDD) and Page Object Model (POM) for running Appium tests.
Currently, the framework comes with out of the box support for running tests on a local android and ios devices behind a
local Appium Grid & BrowserStack.

# Software Requirements
1. brew <br>
2. Android Studio <br>
3. XCode <br>
4. python 3.7.3 <br>
5. git <br>
6. nodejs <br>
7. appium <br>

![](https://i.imgflip.com/34qjei.jpg)

# Instructions on installing the softwares
1. This framework was tested only on OS X Mojave but theoretically should work on other OS X as well.
2. Follow the instructions to install [brew](https://brew.sh/).
3. Follow the instructions to install [Android Studio and Emulator](https://hdorgeval.gitbooks.io/setup-your-mac-to-develop-nativescript-apps/content/install-android-studio-on-mac-os-x.html).
4. Follow the instructions to install [XCode](https://medium.com/@LondonAppBrewery/how-to-download-and-setup-xcode-10-for-ios-development-b63bed1865c).
5. To install python3, type ```brew install python3``` in command prompt.
6. To install git, type ```brew install git``` in command prompt.
7. To install NodeJS, type ```brew install node@10``` in command prompt.
8. To install Appium, type ```npm install -g appium``` in command prompt.
9. Download the framework as a zip file or type
```git clone https://github.com/mukeshtiwari1987/behave_pom_appium```
10. To install python libraries uses in the framework, type ```pip install -r requirements.txt``` in the command prompt type.

# Structure
![Folder Structure Image](https://i.ibb.co/4Kc1jYj/behave-bdd-copy.png)
 
# How to start Appium server
1. To run test on a local Android or iOS, start appium server by typing ```appium``` in command prompt. 

# How to run test on local Android emulator
1. Start 'Android emulator' from under 'Android Studio' -> 'AVD Manager'.
2. In command prompt, type ```adb devices``` and make the note of Android UDID.
3. In android.json file under config folder, replace the value of 'deviceName' with Android UDID.    
4. Type ```paver run android``` in command prompt to see the test running
![](https://memegenerator.net/img/instances/68740545/oh-really-show-me-the-proof.jpg)<br>
##### Here is the Proof!
![](images/android_proof.gif) 
# How to run test on local iOS simulator
1. Open XCode, Click 'Open Developer Tool' and click 'Simulator'. Select an iPhone simulator of your choice.
2. Get the iOS device name from under iPhone settings.
3. In the ios.json file under config folder, replace the value of 'deviceName' with iOS device name.    
4. Type following in command prompt
```paver run ios```

# How to run test on BrowserStack
1. Sign up for a free trial account on [BrowserStack](https://www.browserstack.com/).
2. Make a note of your __Username__ and __Access Key__
3. Place Username and Access Key in ```config/browserstack.json```
4. In the command prompt type
```paver run browserstack```

# How to integrate test with Travis
1. Sign up for an account on [Travis CI](https://travis-ci.org/).
2. Ensure you have Ruby installed on your machine.
3. In the command prompt type
```gem install travis```
4. In the command prompt type ```travis encrypt access_key="BROWSERSTACK_ACCESS_KEY"``` and make the note of output.
5. Place the output in under secure in .travis.yml.

# Todo List
1. Add Allure Reporting
2. Move common methods to Python class
