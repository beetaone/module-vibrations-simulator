"""
This file implements module's main logic.
Data inputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from api.send_data import send_data
from .params import PARAMS

import random
import threading
import numpy as np

log = getLogger("module")

# extract frequency-magnitude pairs for waveforms
waves_freq_mag = [freq_mag.strip().split(":") for freq_mag in PARAMS["FREQUENCY_MAGNITUDE"].split(',')]

start_time = 0
end_time = PARAMS["MEASUREMENT_DURATION"]

def module_main():
    """
    Implements module's main logic for inputting data.
    Function description should not be modified.
    """

    log.debug("Inputting data...")

    try:
        # start thread with given interval (generate measurements at given time rate)
        threading.Timer(PARAMS["MEASUREMENT_DURATION"], module_main).start()

        N = (end_time - start_time) * PARAMS["SAMPLE_SIZE"]             # number of samples during the measurement (number of data)
        time = np.linspace(start_time, end_time, N, endpoint=False)     # measurement timestamps (time domain signal)

        # create waves
        superposed_waveform = 0
        for wave_spec in waves_freq_mag:
            waveform = wave_spec[1] * np.sin(2 * np.pi * wave_spec[0] * time)      # clean waveform = magnitude * np.sin(2*pi*frequency*time)
            superposed_waveform += waveform       # add waveform to the superposed wave

        # add random noise
        if random.random() < PARAMS["NOISE_PROBABILITY"]:
            noise = np.random.normal(0, PARAMS["NOISE_STANDARD_DEVIATION"], N)
            superposed_waveform += noise

        # shift time window (need it when MEASUREMENT_DURATION is not integer as sine function must shift)
        start_time, end_time = end_time, end_time + PARAMS["MEASUREMENT_DURATION"]

        # construct output data
        output_data = {
            PARAMS["OUTPUT_LABEL"]: superposed_waveform,
        }

        # send data to the next module
        send_error = send_data(output_data)

        if send_error:
            log.error(send_error)
        else:
            log.debug("Data sent successfully.")

    except Exception as e:
        log.error(f"Exception in the module business logic: {e}")
