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

# noisy = False

VIBRATION = False  # A vibration is added to the signal


def module_main():
    """
    Implements module's main logic for inputting data.
    Function description should not be modified.
    """

    global start_time, end_time, VIBRATION

    log.debug("Inputting data...")

    try:
        # start thread with given interval (generate measurements at given time rate)
        threading.Timer(PARAMS["MEASUREMENT_DURATION"], module_main).start()

        # Generate the time array
        N = (end_time - start_time) * PARAMS["SAMPLE_SIZE"]             # number of samples during the measurement (number of data)
        time = np.linspace(start_time, end_time, N, endpoint=False)     # measurement timestamps (time domain signal)

        # create the main signal
        main_signal = PARAMS["MAIN_MAGNITUDE"] * np.sin(2 * np.pi * PARAMS["MAIN_FREQUENCY"] * time)      # clean waveform = magnitude * np.sin(2*pi*frequency*time)

        # create the noise

        if not VIBRATION and random.random() < PARAMS["VIBRATION_PROBABILITY"]:
            # We start vibration signal
            vibration_signal = PARAMS["VIBRATION_MAGNITUDE"] * np.sin(2 * np.pi * PARAMS["VIBRATION_FREQUENCY"] * time)
            composite_signal = main_signal + vibration_signal
            VIBRATION = True
        elif VIBRATION and random.random() < PARAMS["CONTINUE_PROBABILITY"]:
            # We continue vibration signal
            vibration_signal = PARAMS["VIBRATION_MAGNITUDE"] * np.sin(2 * np.pi * PARAMS["VIBRATION_FREQUENCY"] * time)
            composite_signal = main_signal + vibration_signal
            VIBRATION = True
        else:
            # We stop the vibration signal
            VIBRATION = False
            composite_signal = main_signal

        composite_signal += np.random.normal(0, PARAMS["NOISE_STANDARD_DEVIATION"], N)

        # superposed_waveform += PARAMS["VIBRATION_MAGNITUDE"] * np.sin(2 * np.pi * PARAMS["VIBRATION_FREQUENCY"] * time)

        # if not noisy:
        #     # try to start noise
        #     if random.random() < PARAMS["NOISE_PROBABILITY"]:
        #         # start random noise
        #         noisy = True
        #         superposed_waveform += np.random.normal(0, PARAMS["NOISE_STANDARD_DEVIATION"], N)
        # else:
        #     if random.random() < PARAMS["CONTINUE_PROBABILITY"]:
        #         # continue noisy
        #         superposed_waveform += np.random.normal(0, PARAMS["NOISE_STANDARD_DEVIATION"], N)
        #     else:
        #         # do not continue noisy
        #         noisy = False

        # shift time window (need it when MEASUREMENT_DURATION is not integer as sine function must shift)
        start_time, end_time = end_time, end_time + PARAMS["MEASUREMENT_DURATION"]

        # compress data
        lzma_superposed = lzma.compress(composite_signal.astype(float))

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
