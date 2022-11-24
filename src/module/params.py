from os import getenv

PARAMS = {
    "SAMPLE_SIZE": int(getenv("SAMPLE_SIZE", 1024)),                            # number of samples taken per second, sample rate of 1024 means, 1024 values of the signal are recorded in one second
    "MEASUREMENT_DURATION": int(getenv("MEASUREMENT_DURATION", 5)),             # how often the measurements are simulated, measurements interval
    "MAIN_FREQUENCY": float(getenv("MAIN_FREQUENCY", 2000)),
    "MAIN_MAGNITUDE": float(getenv("MAIN_MAGNITUDE", 25)),
    "VIBRATION_FREQUENCY": float(getenv("VIBRATION_FREQUENCY", 2000)),
    "VIBRATION_MAGNITUDE": float(getenv("VIBRATION_MAGNITUDE", 25)),
    "VIBRATION_PROBABILITY": float(getenv("VIBRATION_PROBABILITY", 0.1)),               # probability of noise in the generated data
    "CONTINUE_PROBABILITY": float(getenv("CONTINUE_PROBABILITY", 0.5)),
    "NOISE_STANDARD_DEVIATION": float(getenv("NOISE_STANDARD_DEVIATION",3)),
    "OUTPUT_LABEL": getenv("OUTPUT_LABEL", "vibrations")
}
