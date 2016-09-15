Shoop Beauty Theme
==================

This is Shoop Beauty Theme for Shoop.

Version 1.0.0 is compatible with Shoop [Shoop 4.0.0][1].

Getting started
---------------

For Bash-based shells, this should do:

```bash
pip install -r requirements.txt
(cd shoop_beauty_theme && npm run build)
cd ..
python -m shoop_workbench migrate
python -m shoop_workbench createsuperuser
python -m shoop_workbench runserver 0.0.0.0:8000
```

For mock data, run

```bash
python -m shoop_workbench shoop_populate_mock
```

[1]: https://github.com/shuup/shuup/releases/tag/v4.0.0