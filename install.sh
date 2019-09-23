#!/bin/bash
wget "https://downloader.disk.yandex.ru/disk/a1e9ddc360a4363ed41eb5a633b6353548088cad23b27ed13b40928584f46683/5d896959/fKqInKw3d7bLFOeFnMGnhF9KYQaNtBzovNKAjJHaQsKJaHObZkf8iQAh0RsrGoXCiCSdMTXCenPbM948Exvp9V-RJbPxMjahZrADX0HzfSer8npumZHI4midPdWhecNq?uid=0&filename=model_1_nimish.tflearn.data-00000-of-00001&disposition=attachment&hash=crLY1G1dENtJLIjMhc7EowxCoC7UOY5gawvXSGod4z0h90djNG9MnWd5DIu3%2Btcbq/J6bpmRyOJonT3VoXnDag%3D%3D%3A&limit=0&content_type=application%2Foctet-stream&owner_uid=358568674&fsize=455064145&hid=1b32ffa8881f23f8b32120fb8a3d754b&media_type=data&tknv=v2" -O model_1_nimish.tflearn.data-00000-of-00001
python3 -m venv venv
. venv/bin/activate
pip install setuptools wheel numpy tensorflow==1.5 tflearn imutils opencv-python
exit
