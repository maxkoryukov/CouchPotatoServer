.. _settings:

Setting and configuration
=========================

*No one wrote here yet*

Common features
---------------

*No one wrote here yet*

SoftChroot
----------

.. code-block:: ini
    :emphasize-lines: 2

    [core]
    soft_chroot = /torrents/

Web UI Tuning
-------------

You could tune the web interface of CP, with small changes in the configuration

.. code-block:: ini

    [webui_feature]
    hide_about_dirs = 1
    hide_about_update = 1
    hide_menuitem_update = 1

Aditionally:

.. code-block:: ini

    [updater]
    notification = 0
    enabled = 0
    automatic = False

Hide sections
~~~~~~~~~~~~~

.. deprecated:: 3.0.2
    Use :ref:`access-to-option`

You could hide all options from appropriate section of configuration file.

Example:

.. code-block:: ini

    [section_name]
    section_hidden_internal_meta=1

See methods:

* :meth:`~couchpotato.core.settings.Settings.optionMetaSuffix`
* :meth:`~couchpotato.core.settings.Settings.optionMetaSuffix`

_internal_meta

.. _access-to-option:

Access to options
~~~~~~~~~~~~~~~~~

The behavior of common options is defined by internal meta-options, which you might add to the config file. These meta-options define whether the particular option will be visible/editable in the web-interface.

In this example we have made the updater section invisible, so you couldn't see its config values in the web interface.
The second thing: option core.username will be immutable in the web UI, since there is meta-option username_internal_meta.

Allowed values for options:

* <option>_internal_meta = ( hidden | ro | rw )

* section_hidden_internal_meta = ( True | False )

**By default** - all settings are writable.

Example of usage `.couchpotato/settings.conf`

.. code-block:: ini
    :emphasize-lines: 4,7,10

    [core]
    ssl_key = 

    api_key = 12345678901234567
    api_key_internal_meta = ro

    username = cp
    username_internal_meta = rw

    proxy_server = 
    proxy_server_internal_meta = hidden

    # ...

Default behavior for options
****************************

You could define default values for meta-options in the python code

::

    config = [{
        'name': 'core',
        'order': 1,
        'groups': [
            {
                'tab': 'general',
                'name': 'basics',
                'description': 'Needs restart before changes take effect.',
                'wizard': True,
                'options': [
                    {
                        'name': 'username',
                        'default': '',
                        'ui-meta' : 'rw',
                    },
                    {
                        'name': 'password',
                        'default': '',
                        'type': 'password',
                        'ui-meta' : 'ro',
                    },
                    {
                        'name': 'port',
                        'default': 5050,
                        'type': 'int',
                        'description': 'The port I should listen to.',
                        'ui-meta' : 'hidden',
                    }
                ]
            }
       ]
    }]

Methods

* :meth:`~couchpotato.core.settings.Settings.optionMetaSuffix`
* :meth:`~couchpotato.core.settings.Settings.isOptionReadable`
* :meth:`~couchpotato.core.settings.Settings.isOptionWritable`
