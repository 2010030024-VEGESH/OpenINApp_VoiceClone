```shell
conda create --name tortoise python=3.9 numba inflect
conda activate tortoise
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install transformers=4.29.2
git clone https://github.com/neonbjb/tortoise-tts.git
cd tortoise-tts
python setup.py install
```


This script allows you to speak a single phrase with one or more voices.
                           ⬇️
```shell
python tortoise/do_tts.py --text "I'm going to speak this" --voice random --preset fast
```

This script provides tools for reading large amounts of text.
                            ⬇️
```shell
python tortoise/read.py --textfile <your text to be read> --voice random
```




<h1>If you want to add a new voice</h1>
To add new voices to Tortoise, you will need to do the following:

1. Gather audio clips of your speaker(s). Good sources are YouTube interviews (you can use YouTube to fetch the audio), audiobooks or podcasts. 
2. Cut your clips into ~10-second segments. You want at least 3 clips.
3. Save the clips as a WAV file with floating point format and a 22,050 sample rate.
4. Create a subdirectory in voices/
5. Put your clips in that subdirectory.
6. Run tortoise utilities with --voice=<your_subdirectory_name>.
