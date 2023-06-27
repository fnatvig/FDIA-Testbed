"""This module defines project-level constants."""


# Socket address and ports
UDP_IP = "127.0.0.1"
PLOT_PORT = 5006
GUI_PORT = 5010
POWER_PORT = 5005

# Socket messages
POWERENGINE_READY = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
PLOTSERVER_READY = b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
LOAD14 = b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
LOAD9 = b'\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
TOGGLE_PLOT = b'\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
START_SIM = b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
PAUSE_SIM = b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
KILL_SIM = b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
SAVE_SIM = b'\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
EXPORT_EXCEL = b'\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
EXPORT_CSV = b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Attack specific messages
SINGLE_BUS_ATTACK = 2
MULTI_BUS_ATTACK = 4
LAST_ATTACK_MSG = 8

# Power Engine specific constants
SIGMA_BUS_V  = 0.0001
SIGMA_BUS_PQ  = 50*0.0001
SIGMA_LINE = 0.1
SIGMA_TRAFO = 0.1
