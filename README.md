
# Stuttering Events in Podcasts Dataset Extended (SEP-28k-E)

The SEP-28k-E dataset is an extension of the SEP-28k dataset.
It consists of the same data as the original [dataset](!https://github.com/apple/ml-stuttering-events-dataset/) with the following additions:

* speaker and gender information
* added number of speakers to expect per podcast episode
* named speaker labels for the podcast's hosts
* suggestions for balanced data split, helping with objective comparison of dysfluency detection systems

The SEP-28k dataset contains stuttering event annotations for approximately 28,000 3-second clips.
In addition we include stutter event annotations for about 4,000 3-second clips from the FluencyBank dataset. Audio files are not part of this released dataset but may be downloaded using URLs provided in the `*_episodes.csv` files. Original copyright remains with the podcast owners. 


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

## SEP-28k-Extended files:

* **Episodes**

Podcast names, audio urls, and keycodes used with the annotation labels (`SEP-28k-Extended_episodes.csv`) as well as a host name, guest name (if available), number of
speakers to expect per episode, and the host and respective guest gender.
In addition to that information, there are clustering quality metrics included, that were used to determine the individual speakers per episode (**all_samples_above_avg_silhouette**, **calinski_harabasz_score**, **cosine_dist**), that can be used to create splits using stricter quality metrics.


| url                                                                                   | Show       |   EpId | host         | guest    |   num_spk | true_num_spk_known   | host_gender   | guest_gender   | all_samples_above_avg_silhouette   |   calinski_harabasz_score |   cosine_dist |
|:--------------------------------------------------------------------------------------|:-----------|-------:|:-------------|:---------|----------:|:---------------------|:--------------|:---------------|:-----------------------------------|--------------------------:|--------------:|
| https://stutterrockstar.files.wordpress.com/2011/05/male-episode-1-with-alan1.mp3     | HeStutters |      0 | Pamela Mertz | alan1    |         2 | True                 | f             | m              | True                               |                   25.948  |      0.405554 |
| https://stutterrockstar.files.wordpress.com/2012/04/male-episode-10-with-landon.mp3   | HeStutters |      1 | Pamela Mertz | landon   |         2 | True                 | f             | m              | True                               |                  150.363  |      0.459398 |
...

* **Clips**

`SEP-28k-Extended_clips.csv` contains the label information. Compared to `SEP-28k_clips.csv`, SEP-28k-Extended contains columns with four suggested data partitionings SEP12k (for 5 fold CV, only train), SEP-28k-E (train, dev, test), SEP28k-T (train, dev, test), and SEP28k-D (train, dev, test).
The column **is_probably_host** indicates if the clips belongs to the host, a column containing the clip's silhouette score to enable splits with even stricter speaker separation, and a named **speaker** columns.

| Show       |   EpId |   ClipId |    Start |     Stop | is_probably_host   | speaker      |   clip_silhouette_score |   SEP12k | SEP28k-E   | SEP28k-T   | SEP28k-D   |   ... |
|:-----------|-------:|---------:|---------:|---------:|:-------------------|:-------------|------------------------:|---------:|:-----------|:-----------|:-----------|---------:|
| HeStutters |      0 |        0 | 31900320 | 31948320 | True               | Pamela Mertz |                0.565847 |      nan | train      | test       | test       |        ... |
| HeStutters |      0 |        1 | 31977120 | 32025120 | True               | Pamela Mertz |                0.440298 |      nan | train      | test       | test       |        ... |
...

# Downloading & Processing Scripts

There are two scripts used to download the raw audio files and extract into clips that correspond to the clip annotations. `[WAV_DIR]` refers to the folder where you are storing all of the raw audio data and `[CLIP_DIR]` refers to where you want to place the clips. These may be the same folder. 

To download and extract clips from both datasets run the following from this directory

* `python download_audio.py --episodes SEP-28k_episodes.csv --wavs [WAV_DIR]`
* `python extract_clips.py --labels SEP-28k_labels.csv --wavs [DATA_DIR] --clips [CLIP_DIR]`
* `python download_audio.py --episodes fluencybank_episodes.csv --wavs [WAV_DIR]`
* `python extract_clips.py --labels fluencybank_labels.csv --wavs [DATA_DIR] --clips [CLIP_DIR]`

The raw SEP-28k wav files are 32 Gb and clipped SEP-28k wav files are 2.6 Gb.

# Citation

If you use the SEP-28k-E dataset in your research, please cite our paper and the original SEP-28k contribution by Lea et al.:
```
@incollection{bayerl_sep28k_E_2022,
	title = {The {Influence} of {Dataset-Partitioning} on {Dysfluency} {Detection} {Systems}},
	booktitle = {Text, {Speech}, and {Dialogue}},
	author = {Bayerl, Sebastian P. and Wagner, Dominik and Bocklet, Tobias and Riedhammer, Korbinian},
	year = {2022},
}

@misc{lea:2021,
    author       = {Colin Lea AND Vikramjit Mitra AND Aparna Joshi AND Sachin Kajarekar AND Jeffrey P. Bigham},
    title        = {{SEP-28k}: A Dataset for Stuttering Event Detection from Podcasts with People Who Stutter},
    howpublished = {ICASSP 2021},
}
```

# License

The code in this repository is licensed according to the [LICENSE](LICENSE) file.

The SEP-28k-E dataset is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0). To view a copy of this license, visit https://creativecommons.org/licenses/by-nc/4.0/.