#!/bin/bash
json=`curl -s "https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key=https%3A%2F%2Fyadi.sk%2Fd%2F_k1RiNI7yeEF_g" | python3 -c "import sys, json; print(json.load(sys.stdin)['href'])"`
wget $json -O model.tflearn.data-00000-of-00001
python3 -m venv venv
. venv/bin/activate
pip install setuptools wheel numpy tensorflow==1.8 tflearn imutils opencv-python flask bjoern
exit