# pa-mouse

## Introduction

_Pictionary Air_ is a modern take on the classic Pictionary game in which players draw in the air with an electronic pen instead of on paper. Using a special AR app on a smartphone or tablet teammates can see what is being drawn.

The pa-mouse is a simple Python script that allows a user to control the mouse pointer using this Pictionary Air pen. It uses the webcam to track the pen and translate its position and color to mouse movements and clicks. This way you could play Pictionary Air on a larger computer screen, or simply use the pen as an alternative input device.

Currently it only runs on Linux.

## Installation

The command below creates a new conda environment with the necessary requirements.

```conda env create -f environment.yml```

The Python script also calls the v4l-ctl command-line tool to adjust some webcam settings. You can install this tool using the following command.

```sudo apt install v4l-utils```

To run the script, type:

```
conda activate pa-mouse
python pa-mouse.py
```

Entering Ctrl+C will exit the script and restore the webcam settings.

## Status

This program was hacked together on a Saturday morning and I've only tested it on my computer.  It seems to run fine on my computer, but doesn't come with any warranties or support. You very likely need to adjust webcam settings to make it work for you. You may use it however you see fit. If you make any improvements I'm more than happy to accept a pull request. 

