import concurrent.futures
import time
from PIL import Image,ImageFilter

img_names = [
    'photo-150302334.jpg',
    'photo-151877957.jpg',
    'photo-152341365.jpg'
]

t1 = time.perf_counter()
size = (1200,1200)

def processImage(img_name):
    try:
        if not os.path.exists(img_name):
            print(f"File not found: {img_name}")
            return
        img = Image.open(img_name)
        img = img.filter(ImageFilter.GaussianBlur(15))
        img.thumbnail(size)
        os.makedirs('processed', exist_ok=True)
        img.save(f'processed/{img_name}')
        print(f'{img_name} has been processed')
    except Exception as e:
        print(f"Failed to process {img_name}: {e}")

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(processImage,img_names)

    t2 = time.perf_counter()

    print(f"Finished in {t2-t1} secs")