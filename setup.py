import setuptools


if __name__ == '__main__':
    setuptools.setup(
        name="shoop-beauty-theme",
        version="1.0.0",
        description="Shoop Beauty Theme",
        packages=setuptools.find_packages(),
        include_package_data=True,
        entry_points={"shoop.addon": "shoop_beauty_theme=shoop_beauty_theme"}
    )
