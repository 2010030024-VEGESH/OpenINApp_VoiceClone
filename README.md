
Then run the following commands, using anaconda prompt as the terminal (or any other terminal configured to work with conda)

This will:
1. create conda environment with minimal dependencies specified
1. activate the environment
1. install pytorch with the command provided here: https://pytorch.org/get-started/locally/
1. clone tortoise-tts
1. change the current directory to tortoise-tts
1. run tortoise python setup install script

```shell
conda create --name tortoise python=3.9 numba inflect
conda activate tortoise
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install transformers=4.29.2
git clone https://github.com/neonbjb/tortoise-tts.git
cd tortoise-tts
python setup.py install
```

Optionally, pytorch can be installed in the base environment, so that other conda environments can use it too. To do this, simply send the `conda install pytorch...` line before activating the tortoise environment.

> **Note:** When you want to use tortoise-tts, you will always have to ensure the `tortoise` conda environment is activated.

If you are on windows, you may also need to install pysoundfile: `conda install -c conda-forge pysoundfile`

### do_tts.py

This script allows you to speak a single phrase with one or more voices.
```shell
python tortoise/do_tts.py --text "I'm going to speak this" --voice random --preset fast
```

### read.py

This script provides tools for reading large amounts of text.

```shell
python tortoise/read.py --textfile <your text to be read> --voice random
```

This will break up the textfile into sentences, and then convert them to speech one at a time. It will output a series
of spoken clips as they are generated. Once all the clips are generated, it will combine them into a single file and
output that as well.

Sometimes Tortoise screws up an output. You can re-generate any bad clips by re-running `read.py` with the --regenerate
argument.




### Adding a new voice

To add new voices to Tortoise, you will need to do the following:

1. Gather audio clips of your speaker(s). Good sources are YouTube interviews (you can use youtube-dl to fetch the audio), audiobooks or podcasts. Guidelines for good clips are in the next section.
2. Cut your clips into ~10 second segments. You want at least 3 clips. More is better, but I only experimented with up to 5 in my testing.
3. Save the clips as a WAV file with floating point format and a 22,050 sample rate.
4. Create a subdirectory in voices/
5. Put your clips in that subdirectory.
6. Run tortoise utilities with --voice=<your_subdirectory_name>.

### Picking good reference clips

As mentioned above, your reference clips have a profound impact on the output of Tortoise. Following are some tips for picking
good clips:

1. Avoid clips with background music, noise or reverb. These clips were removed from the training dataset. Tortoise is unlikely to do well with them.
2. Avoid speeches. These generally have distortion caused by the amplification system.
3. Avoid clips from phone calls.
4. Avoid clips that have excessive stuttering, stammering or words like "uh" or "like" in them.
5. Try to find clips that are spoken in such a way as you wish your output to sound like. For example, if you want to hear your target voice read an audiobook, try to find clips of them reading a book.
6. The text being spoken in the clips does not matter, but diverse text does seem to perform better.



## Notice

Tortoise was built entirely by me using my own hardware. My employer was not involved in any facet of Tortoise's development.

If you use this repo or the ideas therein for your research, please cite it! A bibtex entree can be found in the right pane on GitHub.
