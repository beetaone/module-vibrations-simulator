from os import getenv

PARAMS = {
    "SAMPLE_SIZE": int(getenv("SAMPLE_SIZE", 1024)),                            # number of samples taken per second, sample rate of 1024 means, 1024 values of the signal are recorded in one second
    "MEASUREMENT_DURATION": int(getenv("MEASUREMENT_DURATION", 5)),             # how often the measurements are simulated, measurements interval
    "FREQUENCY_MAGNITUDE": getenv("FREQUENCY_MAGNITUDE","2000:25, 4000:2"),     # for each elementary waveform defines pair frequency:magnitude
    "NOISE_PROBABILITY": float(getenv("NOISE_PROBABILITY", 0.1)),               # probability of noise in the generated data
    "NOISE_STANDARD_DEVIATION": float(getenv("NOISE_STANDARD_DEVIATION",3)),
    "OUTPUT_LABEL": getenv("OUTPUT_LABEL", "vibrations")
}
