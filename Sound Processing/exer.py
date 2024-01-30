import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
import math
import soundfile as sf

filename = 'input/Nums_5dot1_24_48000.wav'
sampling_rate = 22050
# Load audio file
y, sr = librosa.load(filename,sr = sampling_rate) #The sampling rate can be set here
y.shape
orig_copy = y.copy()
sampling_rate = 22050
orig_copy = y.copy()

def change_playback_speed(rate):
    sr = sampling_rate*rate
    sf.write('playback.wav',y,math.floor(sr))

def panning(rate):
    if rate > 100:
        print('valuetoohigh')
        return
    elif rate == 0:
        sf.write('panning.wav', y, sampling_rate)
        return

    rate_mult = rate/100
    inverse = 1 - np.abs(rate)
    right = y * inverse if rate > 0 else y * np.abs(rate_mult)

    left = y * inverse if rate < 0 else y *np.abs(rate_mult)
    length = y.shape[0]
    combined = np.stack((left/3, right/3), axis=-1)

    sf.write('panning.wav', combined, sampling_rate)

def fade_out(sec):
    file_name = 'files/C4 - 261.63.wav'
    sound, sr = librosa.load(file_name,sr = sampling_rate) #The sampling rate can be set here
    mult_shape = sec*sampling_rate
    array_to_modify = sound
    if sound.shape[0] > mult_shape:
        array_to_modify = sound[-mult_shape:]
    else:
        print(mult_shape- sound.shape[0])
        array_to_modify = np.pad(array_to_modify, (0, mult_shape -sound.shape[0]))
        sound= array_to_modify
    
    interval_ratio = 100/mult_shape
    mult_array = np.array([index*interval_ratio /100 for index in reversed(list(range(0,mult_shape)))])

    print()
    print(mult_array.shape)
    print(array_to_modify.shape)

    sound[-mult_shape:] = array_to_modify * mult_array
    print(y[148068])
    print(orig_copy[148068])
    
    sf.write('fade_out.wav', sound, sampling_rate)
        
def fade_in(sec):
    file_name = 'files/C4 - 261.63.wav'
    sound, sr = librosa.load(file_name,sr = sampling_rate) #The sampling rate can be set here
    print(sound.shape)
    mult_shape = sec*sampling_rate
    array_to_modify = sound
    if sound.shape[0] > mult_shape:
        array_to_modify = sound[-mult_shape:]
    else:
        print(mult_shape- sound.shape[0])
        array_to_modify = np.pad(array_to_modify, (mult_shape -sound.shape[0],0))
        sound= array_to_modify
    
    interval_ratio = 100/mult_shape
    mult_array = np.array([index*interval_ratio /100 for index in list(range(0,mult_shape))])

    print()
    print(mult_array.shape)
    print(array_to_modify.shape)

    sound[-mult_shape:] = array_to_modify * mult_array
    
    sf.write('fade_in.wav', sound, sampling_rate)

def adaptive_thresh(thresh):
    adaptive = y[np.abs(y) > thresh]
    for i in adaptive:
        print(i)

    sf.write('silence.wav', adaptive, sampling_rate)

def resample():
    test = librosa.effects.time_stretch(y, 3)
    sf.write('resample.wav', test, sampling_rate)

panning(-100)