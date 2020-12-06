# Testing with Appium 

## Android Studio
- Download and install Android Studio [link](https://developer.android.com/studio)
- Choose Standard and finish Setup
- In the “Welcome to Android Studio” window choose “Import an Android Studio Code Sample” and select Crane sample. Click Finish and wait until loaded (it can take a while)
- Open SDK Manager (package icon) and Download/Install **Android 10.0 (API 29)**
- Open AVD Manager (smartphone icon). Click **“Create Virtual Device”**, choose **Pixel 4** -> Next -> Select Q -> Finish
- Try to run the device. You should see a new window with **Pixel Emulator**
- (Optional) In the main Android, Studio window click run and check if the project is built. You should see Application opened in Pixel Emulator

## ANDROID_HOME
- You have to add the Android SDK to the environment variable.
- Please follow the instruction [link](https://www.dev2qa.com/how-to-set-android-sdk-path-in-windows-and-mac/)


## Java JDK & JAVA_HOME
- Download and install Java JDK (if you have a problem with downloading try to use Internet Explorer/Edge Browser) [link](https://www.oracle.com/java/technologies/javase-jdk15-downloads.html)

- Add JAVA_HOME environment variable [link](https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html)


## Appium
- Download and install [link](http://appium.io/)
- Run Appium. Click Edit Configuration and check if **ANDROID_HOME** and **JAVA_HOME** are found. If not, please try to follow the proper steps or use the tutorial.
- Start Server. ***Appium REST http interface listener started on 0.0.0.0:4723*** message should appear


###### You can also use this tutorial as support: [link](https://www.swtestacademy.com/appium-tutorial/)

## How to run
1) Run Appium server
2) Run Mobile Device Emulator
3) Create new project
4) Install "appium" package in python
5) Copy your app to the main project

## Looking for elements & inspection [link](http://appium.io/docs/en/commands/element/find-elements/#find-elements)


