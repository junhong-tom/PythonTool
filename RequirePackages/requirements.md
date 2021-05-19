Python 套件管理 requirements.txt (python 安裝過的套件及相依的套件之紀錄檔)
Command Line 環境中，執行  pip freeze > requirements.txt


```python
# 在 jupyter notebook 上, 查看安裝那些套件。  在終端機環境中只要輸入 pip list
!pip list
```

    Package                  Version
    ------------------------ ---------------------
    absl-py                  0.12.0
    argon2-cffi              20.1.0
    astunparse               1.6.3
    async-generator          1.10
    attrs                    20.3.0
    backcall                 0.2.0
    bleach                   3.3.0
    cachetools               4.2.1
    certifi                  2020.12.5
    cffi                     1.14.5
    chardet                  4.0.0
    colorama                 0.4.4
    cycler                   0.10.0
    dataclasses              0.8
    decorator                5.0.6
    defusedxml               0.7.1
    dill                     0.3.3
    entrypoints              0.3
    flatbuffers              1.12
    future                   0.18.2
    gast                     0.3.3
    google-auth              1.28.0
    google-auth-oauthlib     0.4.3
    google-pasta             0.2.0
    googleapis-common-protos 1.53.0
    graphviz                 0.16
    grpcio                   1.32.0
    h5py                     2.10.0
    idna                     2.10
    importlib-metadata       3.10.1
    importlib-resources      5.1.2
    ipykernel                5.5.3
    ipython                  7.16.1
    ipython-genutils         0.2.0
    ipywidgets               7.6.3
    jedi                     0.18.0
    Jinja2                   2.11.3
    jsonschema               3.2.0
    jupyter                  1.0.0
    jupyter-client           6.1.12
    jupyter-console          6.4.0
    jupyter-core             4.7.1
    jupyterlab-pygments      0.1.2
    jupyterlab-widgets       1.0.0
    Keras                    2.4.3
    Keras-Preprocessing      1.1.2
    kiwisolver               1.3.1
    Markdown                 3.3.4
    MarkupSafe               1.1.1
    matplotlib               3.3.4
    matplotlylib             0.1.0
    mistune                  0.8.4
    nbclient                 0.5.3
    nbconvert                6.0.7
    nbformat                 5.1.3
    nest-asyncio             1.5.1
    notebook                 6.3.0
    numpy                    1.19.5
    oauthlib                 3.1.0
    opencv-python            4.5.1.48
    opt-einsum               3.3.0
    packaging                20.9
    pandas                   1.1.5
    pandocfilters            1.4.3
    parso                    0.8.2
    pickleshare              0.7.5
    Pillow                   8.2.0
    pip                      21.0.1
    plotly                   4.14.3
    prometheus-client        0.10.1
    promise                  2.3
    prompt-toolkit           3.0.18
    protobuf                 3.15.6
    pyasn1                   0.4.8
    pyasn1-modules           0.2.8
    pycparser                2.20
    pydot                    1.4.2
    pydot-ng                 2.0.0
    pydotplus                2.0.2
    Pygments                 2.8.1
    pyparsing                2.4.7
    pyrsistent               0.17.3
    python-dateutil          2.8.1
    pytz                     2021.1
    pywin32                  300
    pywinpty                 0.5.7
    PyYAML                   5.4.1
    pyzmq                    22.0.3
    qtconsole                5.0.3
    QtPy                     1.9.0
    requests                 2.25.1
    requests-oauthlib        1.3.0
    retrying                 1.3.3
    rsa                      4.7.2
    scipy                    1.5.4
    Send2Trash               1.5.0
    setuptools               44.1.1
    six                      1.15.0
    tensorboard              2.4.1
    tensorboard-plugin-wit   1.8.0
    tensorflow               2.4.1
    tensorflow-datasets      4.2.0
    tensorflow-estimator     2.4.0
    tensorflow-metadata      0.30.0
    termcolor                1.1.0
    terminado                0.9.4
    testpath                 0.4.4
    tfds-nightly             4.2.0.dev202104250106
    torch                    1.8.1+cu111
    tornado                  6.1
    tqdm                     4.60.0
    traitlets                4.3.3
    typing-extensions        3.7.4.3
    unrar                    0.4
    urllib3                  1.26.4
    wcwidth                  0.2.5
    webencodings             0.5.1
    Werkzeug                 1.0.1
    wheel                    0.36.2
    widgetsnbextension       3.5.1
    wrapt                    1.12.1
    zipp                     3.4.1
    

    WARNING: You are using pip version 21.0.1; however, version 21.1.1 is available.
    You should consider upgrading via the 'c:\users\tom\pycharmprojects\jupyternotebook\venv\scripts\python.exe -m pip install --upgrade pip' command.
    


```python
# 在 jupyter notebook 上, 查看本機上有哪些檔案。  在終端機環境中只要輸入 dir
!dir
```

     磁碟區 C 中的磁碟是 OS
     磁碟區序號:  1A3C-9264
    
     C:\Users\Tom\PycharmProjects\JupyterNoteBook\PythonTools\RequirePackages 的目錄
    
    2021/05/19  下午 04:29    <DIR>          .
    2021/05/19  下午 04:29    <DIR>          ..
    2021/05/19  下午 04:19    <DIR>          .ipynb_checkpoints
    2021/05/19  下午 04:17                 0 FreezeRequirements.py
    2021/05/19  下午 04:29             6,703 Untitled.ipynb
                   2 個檔案           6,703 位元組
                   3 個目錄  363,631,439,872 位元組可用
    


```python
# 在 jupyter notebook 上, 查看本機上的檔案。  在終端機環境中只要輸入 type 檔案名稱
!type FreezeRequirements.py
```

    1234
    


```python
# 在 jupyter notebook 上, 查看本機上的檔案。  在終端機環境中只要輸入 pip freeze > requirements.txt
!pip freeze > requirements.txt
```


```python
# 在 jupyter notebook 上, 查看本機上的檔案，是否有 requirements.txt 的產生  在終端機環境中只要輸入 dir
!dir
```

     磁碟區 C 中的磁碟是 OS
     磁碟區序號:  1A3C-9264
    
     C:\Users\Tom\PycharmProjects\JupyterNoteBook\PythonTools\RequirePackages 的目錄
    
    2021/05/19  下午 04:36    <DIR>          .
    2021/05/19  下午 04:36    <DIR>          ..
    2021/05/19  下午 04:19    <DIR>          .ipynb_checkpoints
    2021/05/19  下午 04:32                 4 FreezeRequirements.py
    2021/05/19  下午 04:36             2,257 requirements.txt
    2021/05/19  下午 04:33             7,890 Untitled.ipynb
                   3 個檔案          10,151 位元組
                   3 個目錄  363,626,258,432 位元組可用
    


```python
# 在 jupyter notebook 上, 查看本機上的檔案 requirements.txt 的內容  在終端機環境中只要輸入 type requirements.txt
!type requirements.txt
```

    absl-py==0.12.0
    argon2-cffi==20.1.0
    astunparse==1.6.3
    async-generator==1.10
    attrs==20.3.0
    backcall==0.2.0
    bleach==3.3.0
    cachetools==4.2.1
    certifi==2020.12.5
    cffi==1.14.5
    chardet==4.0.0
    colorama==0.4.4
    cycler==0.10.0
    dataclasses==0.8
    decorator==5.0.6
    defusedxml==0.7.1
    dill==0.3.3
    entrypoints==0.3
    flatbuffers==1.12
    future==0.18.2
    gast==0.3.3
    google-auth==1.28.0
    google-auth-oauthlib==0.4.3
    google-pasta==0.2.0
    googleapis-common-protos==1.53.0
    graphviz==0.16
    grpcio==1.32.0
    h5py==2.10.0
    idna==2.10
    importlib-metadata==3.10.1
    importlib-resources==5.1.2
    ipykernel==5.5.3
    ipython==7.16.1
    ipython-genutils==0.2.0
    ipywidgets==7.6.3
    jedi==0.18.0
    Jinja2==2.11.3
    jsonschema==3.2.0
    jupyter==1.0.0
    jupyter-client==6.1.12
    jupyter-console==6.4.0
    jupyter-core==4.7.1
    jupyterlab-pygments==0.1.2
    jupyterlab-widgets==1.0.0
    Keras==2.4.3
    Keras-Preprocessing==1.1.2
    kiwisolver==1.3.1
    Markdown==3.3.4
    MarkupSafe==1.1.1
    matplotlib==3.3.4
    matplotlylib==0.1.0
    mistune==0.8.4
    nbclient==0.5.3
    nbconvert==6.0.7
    nbformat==5.1.3
    nest-asyncio==1.5.1
    notebook==6.3.0
    numpy==1.19.5
    oauthlib==3.1.0
    opencv-python==4.5.1.48
    opt-einsum==3.3.0
    packaging==20.9
    pandas==1.1.5
    pandocfilters==1.4.3
    parso==0.8.2
    pickleshare==0.7.5
    Pillow==8.2.0
    plotly==4.14.3
    prometheus-client==0.10.1
    promise==2.3
    prompt-toolkit==3.0.18
    protobuf==3.15.6
    pyasn1==0.4.8
    pyasn1-modules==0.2.8
    pycparser==2.20
    pydot==1.4.2
    pydot-ng==2.0.0
    pydotplus==2.0.2
    Pygments==2.8.1
    pyparsing==2.4.7
    pyrsistent==0.17.3
    python-dateutil==2.8.1
    pytz==2021.1
    pywin32==300
    pywinpty==0.5.7
    PyYAML==5.4.1
    pyzmq==22.0.3
    qtconsole==5.0.3
    QtPy==1.9.0
    requests==2.25.1
    requests-oauthlib==1.3.0
    retrying==1.3.3
    rsa==4.7.2
    scipy==1.5.4
    Send2Trash==1.5.0
    six==1.15.0
    tensorboard==2.4.1
    tensorboard-plugin-wit==1.8.0
    tensorflow==2.4.1
    tensorflow-datasets==4.2.0
    tensorflow-estimator==2.4.0
    tensorflow-metadata==0.30.0
    termcolor==1.1.0
    terminado==0.9.4
    testpath==0.4.4
    tfds-nightly==4.2.0.dev202104250106
    torch==1.8.1+cu111
    tornado==6.1
    tqdm==4.60.0
    traitlets==4.3.3
    typing-extensions==3.7.4.3
    unrar==0.4
    urllib3==1.26.4
    wcwidth==0.2.5
    webencodings==0.5.1
    Werkzeug==1.0.1
    widgetsnbextension==3.5.1
    wrapt==1.12.1
    zipp==3.4.1
    


```python
import os
```


```python
command_string = r'dir'
os.system(command_string)
```




    0




```python
from subprocess import check_output as Command
# 執行外部明令，並獲取他的輸出
```


```python
batcmd="dir"
result = Command(batcmd, shell=True)
print(result)

# 終端機的編碼格式 cp950 , 可以試試對照其他的格式如 windows-1252， utf-8 等 看有甚麼差異
print(result.decode(encoding='cp950')) 
```

    b' \xba\xcf\xba\xd0\xb0\xcf C \xa4\xa4\xaa\xba\xba\xcf\xba\xd0\xacO OS\r\n \xba\xcf\xba\xd0\xb0\xcf\xa7\xc7\xb8\xb9:  1A3C-9264\r\n\r\n C:\\Users\\Tom\\PycharmProjects\\JupyterNoteBook\\PythonTools\\RequirePackages \xaa\xba\xa5\xd8\xbf\xfd\r\n\r\n2021/05/19  \xa4U\xa4\xc8 10:39    <DIR>          .\r\n2021/05/19  \xa4U\xa4\xc8 10:39    <DIR>          ..\r\n2021/05/19  \xa4U\xa4\xc8 04:19    <DIR>          .ipynb_checkpoints\r\n2021/05/19  \xa4U\xa4\xc8 04:32                 4 FreezeRequirements.py\r\n2021/05/19  \xa4U\xa4\xc8 04:36             2,257 requirements.txt\r\n2021/05/19  \xa4U\xa4\xc8 10:39            17,882 Untitled.ipynb\r\n               3 \xad\xd3\xc0\xc9\xae\xd7          20,143 \xa6\xec\xa4\xb8\xb2\xd5\r\n               3 \xad\xd3\xa5\xd8\xbf\xfd  363,180,257,280 \xa6\xec\xa4\xb8\xb2\xd5\xa5i\xa5\xce\r\n'
     磁碟區 C 中的磁碟是 OS
     磁碟區序號:  1A3C-9264
    
     C:\Users\Tom\PycharmProjects\JupyterNoteBook\PythonTools\RequirePackages 的目錄
    
    2021/05/19  下午 10:39    <DIR>          .
    2021/05/19  下午 10:39    <DIR>          ..
    2021/05/19  下午 04:19    <DIR>          .ipynb_checkpoints
    2021/05/19  下午 04:32                 4 FreezeRequirements.py
    2021/05/19  下午 04:36             2,257 requirements.txt
    2021/05/19  下午 10:39            17,882 Untitled.ipynb
                   3 個檔案          20,143 位元組
                   3 個目錄  363,180,257,280 位元組可用
    
    


```python
freeze_command = r'pip freeze > requirements.txt'
# 比較差異
# result = Command(freeze_command, shell=True)  
result = Command(freeze_command)

# 檢視 命令執行的結果
print(result.decode(encoding='cp950'))

```

    b'absl-py==0.12.0\r\nargon2-cffi==20.1.0\r\nastunparse==1.6.3\r\nasync-generator==1.10\r\nattrs==20.3.0\r\nbackcall==0.2.0\r\nbleach==3.3.0\r\ncachetools==4.2.1\r\ncertifi==2020.12.5\r\ncffi==1.14.5\r\nchardet==4.0.0\r\ncolorama==0.4.4\r\ncycler==0.10.0\r\ndataclasses==0.8\r\ndecorator==5.0.6\r\ndefusedxml==0.7.1\r\ndill==0.3.3\r\nentrypoints==0.3\r\nflatbuffers==1.12\r\nfuture==0.18.2\r\ngast==0.3.3\r\ngoogle-auth==1.28.0\r\ngoogle-auth-oauthlib==0.4.3\r\ngoogle-pasta==0.2.0\r\ngoogleapis-common-protos==1.53.0\r\ngraphviz==0.16\r\ngrpcio==1.32.0\r\nh5py==2.10.0\r\nidna==2.10\r\nimportlib-metadata==3.10.1\r\nimportlib-resources==5.1.2\r\nipykernel==5.5.3\r\nipython==7.16.1\r\nipython-genutils==0.2.0\r\nipywidgets==7.6.3\r\njedi==0.18.0\r\nJinja2==2.11.3\r\njsonschema==3.2.0\r\njupyter==1.0.0\r\njupyter-client==6.1.12\r\njupyter-console==6.4.0\r\njupyter-core==4.7.1\r\njupyterlab-pygments==0.1.2\r\njupyterlab-widgets==1.0.0\r\nKeras==2.4.3\r\nKeras-Preprocessing==1.1.2\r\nkiwisolver==1.3.1\r\nMarkdown==3.3.4\r\nMarkupSafe==1.1.1\r\nmatplotlib==3.3.4\r\nmatplotlylib==0.1.0\r\nmistune==0.8.4\r\nnbclient==0.5.3\r\nnbconvert==6.0.7\r\nnbformat==5.1.3\r\nnest-asyncio==1.5.1\r\nnotebook==6.3.0\r\nnumpy==1.19.5\r\noauthlib==3.1.0\r\nopencv-python==4.5.1.48\r\nopt-einsum==3.3.0\r\npackaging==20.9\r\npandas==1.1.5\r\npandocfilters==1.4.3\r\nparso==0.8.2\r\npickleshare==0.7.5\r\nPillow==8.2.0\r\nplotly==4.14.3\r\nprometheus-client==0.10.1\r\npromise==2.3\r\nprompt-toolkit==3.0.18\r\nprotobuf==3.15.6\r\npyasn1==0.4.8\r\npyasn1-modules==0.2.8\r\npycparser==2.20\r\npydot==1.4.2\r\npydot-ng==2.0.0\r\npydotplus==2.0.2\r\nPygments==2.8.1\r\npyparsing==2.4.7\r\npyrsistent==0.17.3\r\npython-dateutil==2.8.1\r\npytz==2021.1\r\npywin32==300\r\npywinpty==0.5.7\r\nPyYAML==5.4.1\r\npyzmq==22.0.3\r\nqtconsole==5.0.3\r\nQtPy==1.9.0\r\nrequests==2.25.1\r\nrequests-oauthlib==1.3.0\r\nretrying==1.3.3\r\nrsa==4.7.2\r\nscipy==1.5.4\r\nSend2Trash==1.5.0\r\nsix==1.15.0\r\ntensorboard==2.4.1\r\ntensorboard-plugin-wit==1.8.0\r\ntensorflow==2.4.1\r\ntensorflow-datasets==4.2.0\r\ntensorflow-estimator==2.4.0\r\ntensorflow-metadata==0.30.0\r\ntermcolor==1.1.0\r\nterminado==0.9.4\r\ntestpath==0.4.4\r\ntfds-nightly==4.2.0.dev202104250106\r\ntorch==1.8.1+cu111\r\ntornado==6.1\r\ntqdm==4.60.0\r\ntraitlets==4.3.3\r\ntyping-extensions==3.7.4.3\r\nunrar==0.4\r\nurllib3==1.26.4\r\nwcwidth==0.2.5\r\nwebencodings==0.5.1\r\nWerkzeug==1.0.1\r\nwidgetsnbextension==3.5.1\r\nwrapt==1.12.1\r\nzipp==3.4.1\r\n'
    


```python
# 開啟 Shell 來執行， 比較差異
freeze_command = r'pip freeze > requirements.txt'
result = Command(freeze_command, shell=True) 
print(result.decode(encoding='cp950'))
# 為什麼輸出是  b''，因為回報"輸出管導"到 requirements.txt 檔案的結果。
```

    
    


```python

```
