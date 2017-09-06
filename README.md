## looky: a pygame-based fixation target for vision experiments

### Prerequisites

An easy way to avoid version conflicts is to use a Python distribution with a repository and/or package manager, such as [Anaconda](https://docs.continuum.io/anaconda/).

After installing Anaconda, install pygame using `pip install pygame`.

If you have a pre-existing Python installation you want to use, or if you want a lightweight installation without all of Anaconda, you need the following:

1. [Python 2.7.x](https://www.python.org/downloads/)

2. [Pygame](http://www.pygame.org/download.shtml). Make sure you get the version matching your Python installation.

### Installation

1. Clone this repository with git: `git clone https://github.com/rjonnal/looky` or download the zip file and unzip.

2. In the resulting directory, copy `looky_config_template.py` to `looky_config.py`, and edit it the latter as you wish. In particular, the distance between the viewer and screen (`SCREEN_DISTANCE_M`) must be set, as well as `VERTICAL_ORIENTATION` and `HORIZONTAL_ORIENTATION`.

3. 