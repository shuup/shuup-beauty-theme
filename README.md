Nicca theme
===========

This is the Nicca theme usable with Shoop.

Getting started
---------------

For Bash-based shells, this should do:

```bash
pip install -r requirements.txt
(cd nicca_theme && npm run build)
cd ..
python -m shoop_workbench migrate
python -m shoop_workbench createsuperuser
python -m shoop_workbench runserver 0.0.0.0:8000
```

For mock data, run

```bash
python -m shoop_workbench shoop_populate_mock
```
