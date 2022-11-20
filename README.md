# Vibrations Simulator

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | Vibrations Simulator                           |
| Version        | v1.0.0                                |
| DockerHub | [weevenetwork/vibrations-simulator](https://hub.docker.com/r/weevenetwork/vibrations-simulator) |
| Authors        | Jakub Grzelak                    |

- [Vibrations Simulator](#vibrations-simulator)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Simulate vibrations waveform data. Provide sample size, measurement duration and frequencies of the base waveforms.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| Sample Size    | SAMPLE_SIZE         | string   | Number of samples taken per second, sample rate of 1024 means that 1024 values of the signal are recorded in one second.            |
| Measurement Duration    | MEASUREMENT_DURATION         | string  | How often (in seconds) the measurements are simulated. Measurements interval in seconds.            |
| Frequency Magnitude Pairs    | FREQUENCY_MAGNITUDE         | string  | List of comma (,) separated pairs of elementary waveforms frequencies and magnitudes in the format frequency:magnitude.   |
| Noise Probability    | NOISE_PROBABILITY         | string   | Probability of noise in the generated data.            |
| Noise Standard Deviation    | NOISE_STANDARD_DEVIATION         | string   | Standard deviation of the noise randomly generated from the normal distribution.    |
| Output Label   | OUTPUT_LABEL         | string   | The out label at which data is dispatched.   |


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (INGRESS, PROCESS, EGRESS)  |
| EGRESS_URLS            | string | HTTP ReST endpoint for the next module         |

## Dependencies

```txt
requests
numpy
```

## Input

This module does not take any input.

## Output

Output of this module is a compressed array of data points of a simulated waveform.

![Waveform 1](assets-readme/waveform-1.png)

![Waveform 2](assets-readme/waveform-2.png)
