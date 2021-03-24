import os
import requests
import sys


def get_file_name(url):
    url = url.split('/')[-1]
    return url.split('\n')[0]


def get_url_list(file):
    with open(file) as f:
        url_list = f.readlines()
        return url_list


def download_images(img_dir, urls):
    for url in urls:
        if url.strip():
            try:
                file_name = get_file_name(url)
                if not os.path.exists(os.path.join(img_dir, file_name)):
                    r = requests.get(url)
                    with open(os.path.join(img_dir, file_name), 'wb') as fout:
                        fout.write(r.content)
                else:
                    print("{}/{} already exists".format(img_dir,file_name))
            except requests.exceptions.RequestException as e:
                # print(e)
                print("Failed to download {} Not able to connect to: {}".format(file_name, url.strip()))


if __name__ == "__main__":
    url_file = sys.argv[1]
    if os.path.exists(url_file):
        image_save_dir = "images"
        if not os.path.exists('images'):
            os.makedirs('images')
        url_lst = get_url_list(url_file)
        download_images(image_save_dir, url_lst)
    else:
        print("Enter a valid file name")