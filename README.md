DartCMS
=======

DartCMS is an open-source content management system based on the popular Django Framework. It's friendly for developers
and end-users.


Features
--------

- Tree-like website page structure
- Fast and easy CMS module developing
- Fully customizable admin interface color scheme (LESS sources are provided)
- Multi-language support (currently only 2 languages - Russian (main) and English)
- Built with Twitter Bootstrap 3
- TinyMCE as rich editor
- Custom filemanager to work with TinyMCE


Modules
-------

At the moment, only few modules are included:

- Site Structure
- CMS Users
- Metrics (based on the Yandex.Metrika API)
- Site Settings
- News and Articles
- Advertising (ads, ad places and ad sections)


Installation
------------

You need the virtualenv package to start. Also, of course you need to create the database and database user before you'll
run the installation script.

Clone this repository to your local machine and rename conf/dev/project_settings_template.py
to /conf/dev/project_settings.py. This is the start point for your project - settings file. Tune it and run the
install/install.sh script. This script will install virtual environment for your project and all necessary dependencies
(see the install/dependencies.txt file).
