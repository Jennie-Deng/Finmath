import base64
#Function to encode the image
def encode_image(data):
    if data.get("Image") !='':
        image_path='../dataset/'+data.get("Image")
        with open(image_path, 'rb') as image_file:
            base64_image=base64.b64encode(image_file.read()).decode('utf-8')
    else:
        base64_image=''
    if data.get("Share Image") !='':
        base64_share_image=[]
        for i in data.get("Share Image"):
            share_image_path='../dataset/'+i
            with open(share_image_path, 'rb') as image_file:
                base64_share_image.append(base64.b64encode(image_file.read()).decode('utf-8'))
    else:
        base64_share_image=''
    return base64_image,base64_share_image

