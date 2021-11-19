#!/bin/bash

# https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-967772871

wget https://github.com/ytdl-org/youtube-dl/archive/622b87d0fb10a50283b12ecd5304e66dd396809b.zip
unzip 622b87d0fb10a50283b12ecd5304e66dd396809b.zip
cd youtube-dl-622b87d0fb10a50283b12ecd5304e66dd396809b
pip install .
