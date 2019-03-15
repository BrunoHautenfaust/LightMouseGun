# LightMouseGun
Program that controls the mouse with light

### About
Do you remember _Duck Hunt_? That's right, the NES game. Those were the days.

### Usage
![Screenshot](images/screenshot.png)

Press **START** to start your webcam
Select one of the positions (by default the middle bottom one is selected). The position defines the region which the camera sees.
Point a light towards the camera lense.
Press **PREVIEW** to see what the camera sees. That's optional.

WHAT ABOUT CLICKING? This program is **_SPECIFICALLY_** written for light gun shooter games. As such you would want to click/shoot with something that looks like a gun and has a trigger. Moreover, this program is tested with FCEUX and Nestopia (NES emulators) which, for some reason, register only hardware input. Not simulated clicks.

So what can you do about this? Here's an example:
![mouse-gun](images/mouse-gun.png)

- Cheap plastic toy gun. If it's not cheap it won't work.
- USB mouse.
- Flashlight.
- Soldering tool, and other stuff to stick things together.

### Known issues:
- Does not work with full-screen applications.
- Only the linux executable works. I can't seem to bundle the dependencies with Pyinstaller in a single exe for Windows yet.
---
_NOTE:_ The project is written with Pycharm under linux. So trying to open it up in Windows won't work because the files are not absolutely the same for both Operating Systems. That's why I'll provide executables here. 
