"""Support for SignalWire."""
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.const import CONF_WEBHOOK_ID
from homeassistant.helpers import config_entry_flow

DOMAIN = 'signalwire'

CONF_ACCOUNT_SID = 'account_sid'
CONF_AUTH_TOKEN = 'auth_token'
CONF_SPACE_URL = 'space_url'

DATA_SIGNALWIRE = DOMAIN

RECEIVED_DATA = '{}_data_received'.format(DOMAIN)

CONFIG_SCHEMA = vol.Schema({
    vol.Optional(DOMAIN): vol.Schema({
        vol.Required(CONF_ACCOUNT_SID): cv.string,
        vol.Required(CONF_AUTH_TOKEN): cv.string,
        vol.Required(CONF_SPACE_URL): cv.string
    }),
}, extra=vol.ALLOW_EXTRA)


async def async_setup(hass, config):
    """Set up the SignalWire component."""
    from signalwire.rest import Client as signalwire_client
    if DOMAIN not in config:
        return True

    conf = config[DOMAIN]
    hass.data[DATA_SIGNALWIRE] = signalwire_client(conf.get(CONF_ACCOUNT_SID), conf.get(CONF_AUTH_TOKEN), signalwire_space_url = conf.get(CONF_SPACE_URL))
    return True
