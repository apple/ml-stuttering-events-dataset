#
# For licensing see accompanying LICENSE file.
# Copyright (C) 2021 Apple Inc. All Rights Reserved.
#

"""
For each podcast episode:
* Get all clip information for that episode
* Save each clip as a new wav file. 
"""

import os
import pathlib
import subprocess

import numpy as np
import pandas as pd
from scipy.io import wavfile

import argparse

parser = argparse.ArgumentParser(description='Extract clips from SEP-28k or FluencyBank.')
parser.add_argument('--labels', type=str, 
                   help='Path to the labels csv files (e.g., SEP-28k_labels.csv)')
parser.add_argument('--wavs', type=str, 
                   help='Path where audio files from download_audio.py are saved')
parser.add_argument('--clips', type=str, 
                   help='Path where clips should be extracted')

args = parser.parse_args()
label_file = args.labels
data_dir = args.wavs
output_dir = args.clips


# Load label/clip file
data = pd.read_csv(label_file, dtype={"EpId":str})

# Get label columns from data file 
shows = data.Show
episodes = data.EpId
clip_idxs = data.ClipId
starts = data.Start
stops = data.Stop
labels = data.iloc[:,5:].values

n_items = len(shows)

loaded_wav = ""
for i in range(n_items):
	clip_idx = clip_idxs[i]
	show_abrev = shows[i]
	episode = episodes[i].strip()

	# Setup paths
	wav_path = f"{data_dir}/wavs/{shows[i]}/{episode}.wav"
	clip_dir = pathlib.Path(f"{output_dir}/clips/{show_abrev}/{episode}/")
	clip_path = f"{clip_dir}/{shows[i]}_{episode}_{clip_idx}.wav"

	if not os.path.exists(wav_path):
		print("Missing", wav_path)
		continue

	# Verify clip directory exists
	os.makedirs(clip_dir, exist_ok=True)	

	# Load audio. For efficiency reasons don't reload if we've already open the file. 
	if wav_path != loaded_wav:
		sample_rate, audio = wavfile.read(wav_path)
		assert sample_rate == 16000, "Sample rate must be 16 khz"

		# Keep track of the open file
		loaded_wav = wav_path

	# Save clip to file
	clip = audio[starts[i]:stops[i]]
	wavfile.write(clip_path, sample_rate, clip)


