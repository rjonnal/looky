## Looky: a simple fixation target program

### Installation instructions

These instructions assume that you are using the [Anaconda](https://www.anaconda.com/) or [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) Python distributions. Apart from Python's base libraries, looky requires [pygame](https://www.pygame.org/wiki/GettingStarted) and [watchdog](https://pypi.org/project/watchdog/). Python >=3.14 breaks some pygame functionality, so please strict the Python version to <=3.13.

To install:

1. Create a virtual environment called **looky**: `conda create looky python=3.13`.
2. Activate the **looky** environment: `conda activate looky`.
3. Install **pygame** using pip: `pip install pygame`.
4. Install **watchdog** using pip (`pip install watchdog`) or conda (`conda install watchdog`).
5. Clone this repo into your a folder that's in your PYTHONPATH. In CHOIR labs, this will typically be `/home/user/code` or `c:\code`. Move into the desired folder and issue `git clone https://