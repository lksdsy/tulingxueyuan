import requests, os

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1543390584&di=2fa7c4c11d709a5a8c780ad92a2f0b96&imgtype=jpg&er=1&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201504%2F10%2F20150410H5025_B3CTE.thumb.700_0.jpeg'
root = 'tupian'
path = root + '/' + url.split('.')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            print('文件保存成功')
    else:
        print('文件已经存在')
except:
    print('爬取失败')


