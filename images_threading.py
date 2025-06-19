import requests
import time
import concurrent.futures

images = [
    'https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d',  # Direct image URL
    'https://images.unsplash.com/photo-1518779578993-ec3579fee39f',
    'https://images.unsplash.com/photo-1523413651479-597eb2da0ad6'
]

t1 = time.perf_counter()

def download_img(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:  
        img_file.write(img_bytes)
        print(f'{img_name} has been downloaded')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_img, images)

t2 = time.perf_counter()
print(f"Finished in {round(t2 - t1, 2)} second(s)")
