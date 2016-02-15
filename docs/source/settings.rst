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

If you want disable `updater`, do not forget to set up its options:

.. code-block:: ini

    [updater]
    notification = 0
    enabled = 0
    automatic = False

Hide sections
~~~~~~~~~~~~~

.. deprecated:: 3.0.2
    Use :ref:`access-to-option`

Allow to hide all options from appropriate section of configuration file.

Allowed values:

* `section_hidden_internal_meta` = ( **True** | **False** )

Example:

.. code-block:: ini

    [section_name]
    section_hidden_internal_meta=1

See methods:

* :meth:`~couchpotato.core.settings.Settings.isSectionReadable`
* :meth:`~couchpotato.core.settings.Settings.optionMetaSuffix`

.. _access-to-option:

Meta-options
~~~~~~~~~~~~

**meta-options** - options in main configuration file, which define whether the related option will be visible/editable in the web-interface.

Allowed values for meta-options:

* <option>_internal_meta = ( **hidden** | **ro** | **rw** )

**By default** (without meta-options) - all options are writable.

In next example of `.couchpotato/settings.conf` we have added three meta-options:

1. `api_key_internal_meta` will make `api_key` visible, but immutable in web UI.
2. `username_internal_meta` will change nothing. All options remain writable by default.
3. `proxy_server_internal_meta` - will hide option `proxy_server` from web UI

.. code-block:: ini
    :emphasize-lines: 5,8,11

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
