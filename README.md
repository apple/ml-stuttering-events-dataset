
# Stuttering Events in Podcasts Dataset (SEP-28k) 

The SEP-28k dataset contains stuttering event annotations for approximately 28,000 3-second clips. In addition we include stutter event annotations for about 4,000 3-second clips from the FluencyBank dataset. Audio files are not part of this released dataset but may be downloaded using URLs provided in the `*_episodes.csv` files. Original copyright remains with the podcast owners. 


## Annotation Descriptions

Each 3-second clip was annotated with the following labels by three annotators who were not clinicians but did have training on how to identify each type of stuttering event. Label files contain counts (out of three) corresponding to how many reviewers selected a given label. Multiple labels may be selected for a given clip. 

**Stuttering event labels**:
* **Prolongation**: Elongated syllable (e.g., M[mmm]ommy)
* **Block**: Gasps for air or stuttered pauses
* **Sound Repetition**: Repeated syllables (e.g., I [pr-pr-pr-]prepared dinner)
* **Word Repetition**: The same word or phrase is repeated (e.g., I made [made] dinner)
* **No Stuttered Words**: Confirmation that none of the above is true.
* **Interjection**: Common filler words such as "um" or "uh" or person-specific filler words that individuals use to cope with their stutter (e.g., some users frequently say "you know" as a filler).

**Additional labels**:
* **Unsure**: An annotator selects this if they are not confident in their labeling.
* **Poor Audio Quality**: It is difficult to understand due to, for example, microphone quality.
* **Difficult To Understand**: It is difficult to understand the speech.
* **Natural Pause**: There is a pause in speech that is not considered a block or other disfluency. 
* **Music**: There is background music playing (only in SEP-28k)
* **No Speech**: There is no speech in this clip. It is either silent or there is just background noise.

**Data Files**:
* **Links to media files:** Podcast/FluencyBank names, audio urls, and keycodes used with the annotation labels (`SEP-28k_episodes.csv` and `fluencybank_episodes.csv`)
* **Annotations:** Clips used within each audio file with corresponding start/stop time and fluency labels (`SEP-28k_labels.csv` and `fluencybank_labels.csv`). 


# Downloading & Processing Scripts


There are two scripts used to download the raw audio files and extract into clips that correspond to the clip annotations. `[WAV_DIR]` refers to the folder where you are storing all of the raw audio data and `[CLIP_DIR]` refers to where you want to place the clips. These may be the same folder. 

To download and extract clips from both datasets run the following from this directory

* `python download_audio.py --episodes SEP-28k_episodes.csv --wavs [WAV_DIR]`
* `python extract_clips.py --labels SEP-28k_labels.csv --wavs [DATA_DIR] --clips [CLIP_DIR]`
* `python download_audio.py --episodes fluencybank_episodes.csv --wavs [WAV_DIR]`
* `python extract_clips.py --labels fluencybank_labels.csv --wavs [DATA_DIR] --clips [CLIP_DIR]`

The raw SEP-28k wav files are 32 Gb and clipped SEP-28k wav files are 2.6 Gb. 


# Citation

If you find the SEP-28k dataset or this code useful in your research, please cite the following paper:
```
@misc{lea:2021,
    author       = {Colin Lea AND Vikramjit Mitra AND Aparna Joshi AND Sachin Kajarekar AND Jeffrey P. Bigham},
    title        = {{SEP-28k}: A Dataset for Stuttering Event Detection from Podcasts with People Who Stutter},
    howpublished = {ICASSP 2021},
}
```

# License

The code in this repository is licensed according to the [LICENSE](LICENSE) file.

The SEP-28k dataset is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0). To view a copy of this license, visit https://creativecommons.org/licenses/by-nc/4.0/.