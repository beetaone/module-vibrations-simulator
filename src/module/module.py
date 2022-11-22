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
import lzma
import base64

log = getLogger("module")

start_time = 0
end_time = PARAMS["MEASUREMENT_DURATION"]

noisy = False

def module_main():
    """
    Implements module's main logic for inputting data.
    Function description should not be modified.
    """

    global start_time, end_time, noisy

    log.debug("Inputting data...")

    try:
        # start thread with given interval (generate measurements at given time rate)
        threading.Timer(PARAMS["MEASUREMENT_DURATION"], module_main).start()

        N = (end_time - start_time) * PARAMS["SAMPLE_SIZE"]             # number of samples during the measurement (number of data)
        time = np.linspace(start_time, end_time, N, endpoint=False)     # measurement timestamps (time domain signal)

        # create waves
        superposed_waveform = 0
        superposed_waveform += PARAMS["MAIN_MAGNITUDE"] * np.sin(2 * np.pi * PARAMS["MAIN_FREQUENCY"] * time)      # clean waveform = magnitude * np.sin(2*pi*frequency*time)
        superposed_waveform += PARAMS["VIBRATION_MAGNITUDE"] * np.sin(2 * np.pi * PARAMS["VIBRATION_FREQUENCY"] * time)

        if not noisy:
            # try to start noise
            if random.random() < PARAMS["NOISE_PROBABILITY"]:
                # start random noise
                noisy = True
                superposed_waveform += np.random.normal(0, PARAMS["NOISE_STANDARD_DEVIATION"], N)
        else:
            if random.random() < PARAMS["CONTINUE_PROBABILITY"]:
                # continue noisy
                superposed_waveform += np.random.normal(0, PARAMS["NOISE_STANDARD_DEVIATION"], N)
            else:
                # do not continue noisy
                noisy = False

        # shift time window (need it when MEASUREMENT_DURATION is not integer as sine function must shift)
        start_time, end_time = end_time, end_time + PARAMS["MEASUREMENT_DURATION"]

        # compress data
        lzma_superposed = lzma.compress(superposed_waveform.astype(float))

        # construct output data
        output_data = {
            PARAMS["OUTPUT_LABEL"]: base64.b64encode(lzma_superposed).decode('ascii')
        }

        # send data to the next module
        send_error = send_data(output_data)

        if send_error:
            log.error(send_error)
        else:
            log.debug("Data sent successfully.")

    except Exception as e:
        log.error(f"Exception in the module business logic: {e}")
