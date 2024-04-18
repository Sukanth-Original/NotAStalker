#!/bin/bash
export PATH="/usr/bin/python3"

python DistanceEstimation.py &
python MotorControl.py &

wait