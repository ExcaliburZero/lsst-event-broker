# LSST Event Broker
LSST Event Broker is a Python framework for creating transient classifiers for the [Large Synoptic Survey Telescope](https://www.lsst.org/). It allows researchers to create classifiers which are run against incomming data in order to classify astronomical transients.

## Installation
### From Source
To build and install the package from the source code using Conda, run the following commands. You can skip some of the steps if you have already downloaded the source or have already setup a Conda environment.

```bash
git clone https://github.com/CSC380Team8/lsst-event-broker.git
cd lsst-event-broker

conda create -q --name lsstbroker-environment python=2.7
source activate lsstbroker-environment

conda build .
conda install lsstbroker --use-local
```

Also be sure that you have `conda-build` installed, as it is needed to build the Conda package. You can install it by running `conda install conda-build` in your root environment.

## License
The source code of the LSST Event Broker is available under the [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license, see `LICENSE` for more information.
