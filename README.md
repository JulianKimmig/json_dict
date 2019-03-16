A self saving json based config file.
Storable data are all classical JSON datatypes including lists/arrays and dictionaries, which will be stored as JSON Objects.

The Json_Dict object can be initalized via `jd = JsonDict()`

The Object can be initalized with a file (as path) , which will be
created if not existend (turn off by passing `createfile=False` as parameter).
You can also pass initial data to the instance via the `data`. The data can be in the form of another JsonDict, an JSON string or an JSON serializable dictionary.
If a file is specified the JsonDict will first try to read the file and if this does not work fall back to the initial provided data.

`jd = JsonDict(file=path_to_file,creatfile=False,autosave=False)`

If a file is provided the JsonDict will be saved to the file on value addition/change. This can be turned of generally 
by providing the initial argument `autosave=False` or setting the `autosave` attribute to False any time.
For not saving at a specific request you can also pass the `autosave=False` parameter to a get or put request.

The data in the JsonDic object is set via the `js.put("key","subkey","subsubkey",...,value=value)`.
where all the args are used as keys to the value which is set by the value kwarg