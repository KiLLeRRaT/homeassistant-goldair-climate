"""
Setup for different kinds of Goldair climate devices
"""
from homeassistant.const import CONF_HOST
from custom_components.goldair_climate import (
    DOMAIN, CONF_TYPE, CONF_TYPE_HEATER, CONF_TYPE_DEHUMIDIFIER, CONF_TYPE_FAN, CONF_TYPE_MODEL
)
from custom_components.goldair_climate.heater.climate import GoldairHeater
from custom_components.goldair_climate.dehumidifier.climate import GoldairDehumidifier
from custom_components.goldair_climate.fan.climate import GoldairFan


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the Goldair climate device according to its type."""
    device = hass.data[DOMAIN][discovery_info[CONF_HOST]]
    if discovery_info[CONF_TYPE] == CONF_TYPE_HEATER:
        add_devices([GoldairHeater(device)])
    elif discovery_info[CONF_TYPE] == CONF_TYPE_DEHUMIDIFIER:
        add_devices([GoldairDehumidifier(device)])
    elif discovery_info[CONF_TYPE] == CONF_TYPE_FAN:
        add_devices([GoldairFan(device)])
