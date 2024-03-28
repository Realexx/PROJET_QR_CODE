import qrcode

# Générer le code QR hôte
data_host = "Données HOST"
qr_host = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr_host.add_data(data_host)
qr_host.make(fit=True)

img_host = qr_host.make_image(fill='black', back_color='white')
img_host.save('../qrcodes/qrcode_host.png')


# Générer les codes qr à cacher
def generate_multiple_qrcode_to_hide(n):
    for i in range(n):
        if i == 0:
            data_hidden = "Données HIDE"
        else:
            data_hidden = f"Données HIDE{i}"

        qr_hidden = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr_hidden.add_data(data_hidden)
        qr_hidden.make(fit=True)

        img_hidden = qr_hidden.make_image(fill='black', back_color='white')
        img_hidden.save(f'../qrcodes/qrcode_hidden_{i}.png')


generate_multiple_qrcode_to_hide(5)
