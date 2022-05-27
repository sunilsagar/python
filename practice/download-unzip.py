import urllib.request
import zipfile

from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
zipurl = 'https://apps.fas.usda.gov/psdonline/downloads/psd_coffee_csv.zip'
with urlopen(zipurl) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall('C:\\Temp\\1')