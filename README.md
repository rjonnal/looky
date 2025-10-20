## Looky: a simple fixation target program

### Installation instructions

These instructions assume that you are using the [Anaconda](https://www.anaconda.com/) or [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) Python distributions. Apart from Python's base libraries, looky requires [pygame](https://www.pygame.org/wiki/GettingStarted) and [watchdog](https://pypi.org/project/watchdog/). Python >=3.14 breaks some pygame functionality, so please strict the Python version to <=3.13.

#### To install and run:

1. Create a virtual environment called **looky**: `conda create looky python=3.13`.
2. Activate the **looky** environment: `conda activate looky`.
3. Install **pygame** using pip: `pip install pygame`.
4. Install **watchdog** using pip (`pip install watchdog`) or conda (`conda install watchdog`).
5. Clone this repo into your a folder that's in your PYTHONPATH. In CHOIR labs, this will typically be `/home/user/code` or `c:\code`. Move into the desired folder and issue `git clone https://github.com/rjonnal/looky`.
6. Edit `config.py` as necessary. In particular, set the value of `data_monitoring_folder` to a real folder in your filesystem where the acquired images will be written.
7. Run with: `python looky.py`.

#### Keyboard shortcuts

Arrows: move target in large increments; with **Shift** key, move in small increments; increments are set in config.py.

Page-up and Page-down: move through location script; see `location_script.py`.

i: turn on and off inset image, in this case a dead leaves animation.
