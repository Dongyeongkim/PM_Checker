
import os
import numpy as np
from keras.layers import Input, Conv2D, MaxPooling2D, BatchNormalization, UpSampling2D, Concatenate
from keras.models import Model
import sys
# add system path for console, conversion and data.py
sys.path.insert(0, 'M_Vex/')

import console
import conversion
from data import Data


class AcapellaBot:
    def __init__(self):
        mashup = Input(shape=(None, None, 1), name='input')
        convA = Conv2D(64, 3, activation='relu', padding='same')(mashup)
        conv = Conv2D(64, 4, activation='relu', padding='same', use_bias=False)(convA)
        conv = BatchNormalization()(conv)

        conv = Conv2D(64, 3, activation='relu', padding='same')(conv)
        conv = Conv2D(64, 3, activation='relu', padding='same')(conv)
        conv = Conv2D(64, 3, activation='relu', padding='same', use_bias=False)(conv)
        conv = BatchNormalization()(conv)
        conv = Conv2DTranspose(64, 2)(conv)
        conv = Concatenate()([conv, convA])
        conv = Conv2D(64, 3, activation='relu', padding='same')(conv)
        conv = Conv2D(64, 3, activation='relu', padding='same')(conv)
        conv = Conv2D(32, 3, activation='relu', padding='same')(conv)
        conv = Conv2D(1, 3, activation='relu', padding='same')(conv)
        acapella = conv
        m = Model(inputs=mashup, outputs=acapella)
        console.log("Model has", m.count_params(), "params")
        m.compile(loss='mean_squared_error', optimizer='adam')
        self.model = m
        # need to know so that we can avoid rounding errors with spectrogram
        # this should represent how much the input gets downscaled
        # in the middle of the network
        self.peakDownscaleFactor = 4


    def loadWeights(self, path):
        self.model.load_weights(path)
    def isolateVocals(self, path, fftWindowSize, phaseIterations=10):
        console.log("Attempting to isolate vocals from", path)
        audio, sampleRate = conversion.loadAudioFile('Test_Music/'+path)
        spectrogram, phase = conversion.audioFileToSpectrogram(audio, fftWindowSize=fftWindowSize)
        console.log("Retrieved spectrogram; processing...")
        expandedSpectrogram = conversion.expandToGrid(spectrogram, self.peakDownscaleFactor)
        expandedSpectrogramWithBatchAndChannels = expandedSpectrogram[np.newaxis, :, :, np.newaxis]
        predictedSpectrogramWithBatchAndChannels = self.model.predict(expandedSpectrogramWithBatchAndChannels)
        predictedSpectrogram = predictedSpectrogramWithBatchAndChannels[0, :, :, 0] # o /// o
        newSpectrogram = predictedSpectrogram[:spectrogram.shape[0], :spectrogram.shape[1]]
        console.log("Processed spectrogram; reconverting to audio")

        newAudio = conversion.spectrogramToAudioFile(newSpectrogram, fftWindowSize=fftWindowSize, phaseIterations=phaseIterations)
        pathParts = os.path.split(path)
        fileNameParts = os.path.splitext(pathParts[1])
        outputFileNameBase = os.path.join(pathParts[0], fileNameParts[0] + "_acapella")
        console.log("Converted to audio; writing to", outputFileNameBase)

        conversion.saveAudioFile(newAudio,'Test_Acapella/'+outputFileNameBase + ".wav", sampleRate)
        console.log("Vocal isolation complete")

f = open("Test_Music/Music.txt",'r');path = f.read();Vextractor = AcapellaBot();
Vextractor.isolateVocals(path,1536)
