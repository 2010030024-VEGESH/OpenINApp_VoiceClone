# OpenINApp_VoiceClone
<h1>Local Installation</h1>
If you want to use this on your own computer, you must have an NVIDIA GPU.

On Windows, I highly recommend using the Conda installation path. I have been told that if you do not do this, you will spend a lot of time chasing dependency problems.

First, install miniconda: https://docs.conda.io/en/latest/miniconda.html

Then run the following commands, using anaconda prompt as the terminal (or any other terminal configured to work with conda)

#This will:

<li> create conda environment with minimal dependencies specified</li>
<li>activate the environment</li>
<li>install pytorch with the command provided here: https://pytorch.org/get-started/locally/</li>
<li>clone tortoise-tts</li>
<li>change the current directory to tortoise-tts</li>
<li>run tortoise python setup install script</li>
<li>conda create --name tortoise python=3.9 numba inflect</li>
<li>conda activate tortoise</li>
<li>conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia</li>
<li>conda install transformers=4.29.2</li>
<li> git clone https://github.com/neonbjb/tortoise-tts.git</li>
<li>cd tortoise-tts</li>
<li>python setup.py install</li>


#This script allows you to speak a single phrase with one or more voices.

<li>python tortoise/do_tts.py --text "I'm going to speak this" --voice random --preset fast</li>
#read.py

<li>This script provides tools for reading large amounts of text.</li>

<li>python tortoise/read.py --textfile <your text to be read> --voice random</li>


Adding a new voice
To add new voices to Tortoise, you will need to do the following:

Gather audio clips of your speaker(s). Good sources are YouTube interviews (you can use youtube-dl to fetch the audio), audiobooks or podcasts. Guidelines for good clips are in the next section.
Cut your clips into ~10 second segments. You want at least 3 clips. More is better, but I only experimented with up to 5 in my testing.
Save the clips as a WAV file with floating point format and a 22,050 sample rate.
Create a subdirectory in voices/
Put your clips in that subdirectory.
Run tortoise utilities with --voice=<your_subdirectory_name>.



