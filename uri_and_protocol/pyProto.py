import urllib.request as urlreq
import urllib.error
# from io import StringIO as strio
import random
import requests
import subprocess
import sys
import os

class PyProtoHandler(urlreq.BaseHandler):
    def python_open(self, req):
        defaultInstallPath = "E:\\pyproto"
        serverFile = None
        fullUrl = req.get_full_url()
        filePath = "".join(fullUrl.split("://")[1:])
        if filePath.startswith("@web@"):
            serverFile = True
        else:
            serverFile = False
            
        if serverFile:
            try:
                fileUrl = filePath.replace('@web@', 'https://')
                res = requests.get(fileUrl, allow_redirects=True)
                randomName = str(random.randint(1, 99999))+'.py'
                serverFilePath = defaultInstallPath+randomName
                open(serverFilePath, 'wb').write(res.content)
                parsed_cmd = 'python {}'.format(serverFilePath)
                subprocess.run(parsed_cmd, shell=True)
            except Exception:
                print("Invalid URL or File already exists, please Try Again!")
        else:
            try:
                parsed_cmd = 'python {}'.format(filePath)
                subprocess.run(parsed_cmd, shell=True)
            except Exception:
                print("Invalid URL!")

opener = urlreq.build_opener(PyProtoHandler())
urlreq.install_opener(opener)

urlArg = sys.argv[1]

try:
    urlreq.urlopen(urlArg)
except urllib.error.URLError as e:
    pass
