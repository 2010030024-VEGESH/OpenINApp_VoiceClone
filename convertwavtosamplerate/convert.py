import os
from pydub import AudioSegment

# Replace 'input_file.wav' with the path to your input .wav file
input_file = 'D:\Andrewtates voice\sample122050.wav'
audio = AudioSegment.from_file(input_file, format="wav")
# Define the duration of each segment in milliseconds (10 seconds = 10,000 milliseconds)
segment_duration = 10000

# Split the audio into 10-second segments
num_segments = len(audio) // segment_duration
segments = [audio[i * segment_duration:(i + 1) * segment_duration] for i in range(num_segments)]

# Create a new directory to save the output files
output_dir = 'output_segments'
os.makedirs(output_dir, exist_ok=True)

# Specify the path to the FFmpeg executable (use the path where you installed FFmpeg)
ffmpeg_path = 'D:\Downloads\ffmpeg_path'  # Replace '/path/to/ffmpeg' with the actual path

# Save each segment as a separate .wav file in the output directory
for i, segment in enumerate(segments):
    output_file = os.path.join(output_dir, f'output_segment_{i}.wav')
    segment.export(output_file, format="wav", ffmpeg=ffmpeg_path)

