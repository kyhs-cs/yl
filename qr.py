import random
import qrcode

for i in range(6):
    url = f'https://kyhs-cs.github.io/yl/{i}.html'
    qr = qrcode.QRCode(version=1, box_size=10)
    qr.add_data(url)
    qr.make()
    img = qr.make_image(fill='black', back_color='white')
    img.save(f'qr{i + 1}.png')