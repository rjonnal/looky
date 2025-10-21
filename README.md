## Looky: a simple fixation target program

### Installation instructions

These instructions assume that you are using the [Anaconda](https://www.anaconda.com/) or [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) Python distributions. Apart from Python's base libraries, looky requires [pygame](https://www.pygame.org/wiki/GettingStarted) and [watchdog](https://pypi.org/project/watchdog/). Python >=3.14 breaks some pygame functionality, so please strict the Python version to <=3.13.

#### To install and run:

1. Create a virtual environment called **looky**: `conda create -n looky python=3.13`
2. Activate the **looky** environment: `conda activate looky`
3. Install **pygame** using pip: `pip install pygame`
4. Install **watchdog** using pip (`pip install watchdog`) or conda (`conda install watchdog`)
5. Clone this repo into your a folder that's in your PYTHONPATH. In CHOIR labs, this will typically be `/home/user/code` or `c:\code`. Move into the desired folder and issue `git clone https://github.com/rjonnal/looky`
6. Edit `config.py` as necessary. In particular, set the value of `data_monitoring_folder` to a real folder in your filesystem where the acquired images will be written.
7. Run with: `python looky.py`

#### Keyboard shortcuts

<kbd>Up</kbd>: Move target up.
<kbd>Down</kbd>: Move target down.
<kbd>Left</kbd>: Move target left.
<kbd>Right</kbd>: Move target right.

<kbd>Shift</kbd>+<kbd>Up</kbd>: Move target up (small step).
<kbd>Shift</kbd>+<kbd>Down</kbd>: Move target down (small step).
<kbd>Shift</kbd>+<kbd>Left</kbd>: Move target left (small step).
<kbd>Shift</kbd>+<kbd>Right</kbd>: Move target right (small step).

<kbd>Alt</kbd>+<kbd>Up</kbd>: Move origin up.
<kbd>Alt</kbd>+<kbd>Down</kbd>: Move origin down.
<kbd>Alt</kbd>+<kbd>Left</kbd>: Move origin left.
<kbd>Alt</kbd>+<kbd>Right</kbd>: Move origin right.

<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>Up</kbd>: Move origin up (small step).
<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>Down</kbd>: Move origin down (small step).
<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>Left</kbd>: Move origin left (small step).
<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>Right</kbd>: Move origin right (small step).

<kbd>i</kbd>: Toggle inset image/video, e.g. dead leaves animation.

<kbd>PageDown</kbd>: Next location in location script.

<kbd>PageUp</kbd>: Previous location in location script.

<kbd>Escape</kbd> or <kbd>q</kbd>: Quit.

