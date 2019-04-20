## About
**LightMouseGun** is a program that controls the mouse with light. It aims to let you play light gun shooter games on newer displays simulating the unique experience of the classic light gun games (like Duck Hunt for NES).

## Usage
![Screenshot](images/screenshot.png)

Press **START** to start your webcam

Select one of the positions (by default the middle bottom one is selected). The position defines the region which the camera sees.

Point a light towards the camera lense.

Press **PREVIEW** to see what the camera sees. That's optional.

WHAT ABOUT CLICKING? This program is **_SPECIFICALLY_** written for light gun shooter games. As such you would want to click/shoot with something that has a button/trigger. Moreover, this program is tested with FCEUX and Nestopia (NES emulators) which, for some reason, register only hardware input. Not simulated clicks.

So what can you do about this? Here's an example:
![mouse-gun_1](images/mouse-gun_1.jpg)

But if that's too much for you, then how about this:
![mouse-gun_2](images/mouse-gun_2.jpg)

- USB mouse.
- Flashlight.
- Rubber band.

## Known issues:
- Does not work with full-screen applications.
- Only the linux executable works. I can't seem to bundle the dependencies with Pyinstaller in a single exe for Windows yet.
- The program utulizes *v4l2-ctl* to turn off the webcam auto exposure. The library is not available for Windows.
---
_DEVELOPER NOTE:_
To setup the project in Linux run the following commands in terminal in the `src` folder:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To setup the project in Windows run the following commands in terminal in the `src` folder:
```
pip install virtualenv
virtualenv venv
\path\to\venv\Scripts\activate
pip install -r requirements.txt
```
These commands will create a virtual environment in `venv` folder and install the needed dependencies. You'll need to have `python3-env` installed. And `python3-tk`. For both Operating Systems, things might differ. 
