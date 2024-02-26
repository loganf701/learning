import qrcode

data_input = 'https://www.bing.com/videos/riverview/relatedvideo?q=youtube+rick&mid=4E7B1C0F8E67E9F7B1364E7B1C0F8E67E9F7B136&FORM=VIRE'


#documentation
#qrcode: https://pypi.org/project/qrcode/

#setup base of QR code
qr = qrcode.QRCode(
                   version=10,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=4,
                   )

#add data from var data_input
qr.add_data(data_input)

#Compiles data into qrcode array
qr.make(fit=True)

#creates and saves qrcode
link = qr.make_image(fill_color="black", back_color="white")
link.save("qrcode.png")