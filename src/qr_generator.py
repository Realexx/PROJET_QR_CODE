import qrcode


# Générer le code QR hôte
def generate_host_qrcode():
    data_host = "Données HOST"
    qr_host = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr_host.add_data(data_host)
    qr_host.make(fit=True)

    img_host = qr_host.make_image(fill='black', back_color='white')
    img_host.save('../qrcodes/qrcode_host.png')


def generate_hidden_qrcode():
    data_hidden = "Données HIDE"
    qr_hidden = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr_hidden.add_data(data_hidden)
    qr_hidden.make(fit=True)

    img_hidden = qr_hidden.make_image(fill='black', back_color='white')
    img_hidden.save('../qrcodes/qrcode_hidden.png')


# Générer les codes qr à cacher pour l'insertion multiple
def generate_multiple_qrcode_to_hide(n):
    for i in range(n):
        data_hidden = f"Données HID{i}"

        qr_hidden = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr_hidden.add_data(data_hidden)
        qr_hidden.make(fit=True)

        img_hidden = qr_hidden.make_image(fill='black', back_color='white')
        img_hidden.save(f'../qrcodes/multiples/qrcode_hidden_{i}.png')


# Générer les codes qr à cacher pour l'insertion sécurisée
def generate_secure_qrcode_to_hide(n):
    for i in range(n):
        data_hidden = f"Données VOR{i}"

        qr_hidden = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr_hidden.add_data(data_hidden)
        qr_hidden.make(fit=True)

        img_hidden = qr_hidden.make_image(fill='black', back_color='white')
        img_hidden.save(f'../qrcodes/secured/qrcode_hidden_{i}.png')
