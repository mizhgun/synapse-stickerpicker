# -*- coding: utf-8 -*
__author__ = 'mizhgun@gmail.com'

import typing

if typing.TYPE_CHECKING:
    from synapse.module_api import ModuleApi


class AppendStickerPickerData:
    stickerpicker_data = {
        "stickerpicker": {
            "content": {
                "type": "m.stickerpicker",
                "url": "",
                "name": "Stickerpicker",
                "data": {}
            },
            "state_key": "stickerpicker",
            "type": "m.widget",
            "id": "stickerpicker"
        }
    }

    def __init__(self, config=None, api: 'ModuleApi' = None):
        self._store = api.http_client.hs.datastores.main
        self.stickerpicker_data['stickerpicker']['content']['url'] = config['stickerpicker_url']
        api.register_account_validity_callbacks(on_user_registration=self.on_user_registration)

    @staticmethod
    def parse_config(config):
        return config

    async def on_user_registration(self, user: str) -> None:
        await self._store.add_account_data_for_user(user, 'm.widgets', self.stickerpicker_data)
