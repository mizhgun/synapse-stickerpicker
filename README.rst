Matrix Synapse StickerPicker
============================

Pluggable module for Matrix (matrix.org) Synapse server that automatically enables sticker picker for
Element IM on self-hosted instances.

Installation
------------

::

    pip install synapse-stickerpicker

Usage
-----

Add external module settings to server's config (normally ``homeserver.yaml``):

.. code-block:: yaml

    modules:
      - module: synapse_stickerpicker.AppendStickerPickerData
        config:
          stickerpicker_url: '<stickerpicker_app_url>'


After server restart every time when new user is registered, its account data is automatically updated
with appropriate event to enable sticker picker in Element IM apps.


To get started one could try `Maunium sticker picker <https://github.com/maunium/stickerpicker>`__
or its external server's URL ``https://maunium.net/stickers-demo/?theme=$theme`` (**WARNING**:
Element IM stickerpicker widget passes instance URL as a parameter and thus disclosures it).
