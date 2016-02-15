.. _settings:

Setting and configuration
=========================

Common features
---------------

*No one wrote here yet*

SoftChroot
----------

	[core]
	soft_chroot = /torrents/

Web UI Tuning
-------------

You could tune the web interface of CP, with small changes in the configuration

	[webui_feature]
	hide_about_dirs = 1
	hide_menuitem_update = 1

Aditionally:

	[updater]
	notification = 0
	enabled = 0
	automatic = False

Access to options
~~~~~~~~~~~~~~~~~

by default - all is writable:

couchpotato.core.settings.Settings::optionMetaSuffix
couchpotato.core.settings.Settings::optionMetaSuffix

_internal_meta

Hide sections
~~~~~~~~~~~~~

by default - every section is readable

couchpotato.core.settings.Settings::optionMetaSuffix
couchpotato.core.settings.Settings::isOptionReadable(self, section, option):
couchpotato.core.settings.Settings::isOptionWritable(self, section, option):

	[section_name]
	section_hidden_internal_meta
