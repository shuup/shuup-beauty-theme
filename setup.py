import setuptools


if __name__ == '__main__':
    setuptools.setup(
        name="nicca-theme",
        version="1.0.0",
        description="Nicca Theme",
        packages=setuptools.find_packages(),
        include_package_data=True,
        entry_points={"shoop.addon": "nicca_theme=nicca_theme"}
    )
