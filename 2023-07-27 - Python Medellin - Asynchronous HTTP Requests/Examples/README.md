Useful commands for this talk:

Create a virtual env:
```
python -m virtualenv -p python3 ~/.python_envs/aiohttp_talk
```

Activate a virtual env:
```
source ~/.python_envs/aiohttp_talk/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Install dev server and use it:
```
pip install aiohttp-devtools
adev runserver Examples/Server/Data\ sharing
```