# Pictionary Air Mouse

_Pictionary Air_ is a modern take on the classic Pictionary game in which players draw in the air with an electronic pen instead of on paper. Using a special AR app on a smartphone or tablet teammates can see what is being drawn.

The pa-mouse program is a simple Python script that allows a user to control the mouse pointer using the Pictionary Air pen. It uses the webcam to track the pen and translate its position and color to mouse movements and clicks. This way you could play Pictionary Air on a larger computer screen, or simply use the pen as an alternative input device.

Currently it only runs on Linux.

## Getting Started

### Prerequisites

* [Anaconda](https://www.anaconda.com/distribution/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) must be installed on your machine.
* You should have basic knowledge of using Anaconda or Miniconda.

### Installing

1. Clone the repository:
```bash
git clone https://github.com/afvanwoudenberg/pa-mouse.git
```

2. Navigate into the project folder:
```bash
cd pa-mouse
```

3. Create the conda environment from the environment.yml file:
```bash
conda env create -f environment.yml
```

4. Activate the conda environment:
```bash
conda activate pa-mouse
```

5. The Python script also calls the `v4l-ctl` command-line tool to adjust some webcam settings. On Debian-based systems you can install this tool using the following command:

```bash
sudo apt install v4l-utils
```

6. To run the script, type:

```
python pa-mouse.py
```

Entering Ctrl+C will exit the script and restore the webcam settings.

## Disclaimer

This program runs fine on my laptop, but you likely need to adjust webcam settings to make it work for you. If this program doesn't seem to work for you, try experimenting with the parameters in the calls that are made to the `v4l2-ctl` tool in the `set_short_exposure_time` and `restore_camera_settings` functions.

Enter `v4l2-ctl --all` on the command line to see the available options.

## Author

Aswin van Woudenberg ([afvanwoudenberg](https://github.com/afvanwoudenberg))

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

