Shoop Beauty Theme
==================

This is Shoop Beauty Theme for Shoop.

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
