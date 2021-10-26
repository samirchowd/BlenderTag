import os
import urllib.request
from tqdm import tqdm

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

if __name__=='__main__':
    downloads = 'links.txt'
    urls = []
    with open(downloads, 'r') as f:
        for line in f:
            urls.append(line.strip())
            print('Added Link: ', line.strip())
    f.close()

    for url in tqdm(urls):
        model_name = url.split('/')[-2]
        model_ext = url.split('.')[-1]
        model_path = f'{model_name}/{model_name}.{model_ext}'
        if not os.path.isdir(model_name):
            os.mkdir(model_name)
        download_url(url,model_path)
    print('Downloading Models Completed!')
