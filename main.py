import os
import pandas as pd
from PIL import Image
from PIL.ExifTags import TAGS

mdf = pd.DataFrame()

for filename in os.listdir('/file directory here/'):

    if filename.endswith('.jpg') or ('jpeg') or ('.png'): 
        filepath = '/file directory here/' + filename
        print(filename + " exporting meta data...")

        image = Image.open(filepath)

        exif = {
            "fielename": filename, 
            "filepath" : filepath
            }

        for tag, value in image._getexif().items():
            if tag in TAGS:
                exif[TAGS[tag]] = value
                df = pd.DataFrame(data=exif, index=[0])
        mdf = mdf.append(df, ignore_index=True)

mdf.to_excel("export.xlsx") # outputs to the root directory the script runs from