from distutils.core import setup, Extension

pkg = 'Extensions.MeteoItalia'
setup (name = 'enigma2-plugin-extensions-meteoitalia',
       version = '0.1',
       license='GPLv2',
       url='https://github.com/E2OpenPlugins',
       description='MeteoItalia',
       long_description='Weather Forecast Italy',
       author='meo',
       author_email='lupomeo@hotmail.com',
       packages = [pkg],
       package_dir = {pkg: 'plugin'}
      )
