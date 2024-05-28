import os
import torch.nn.functional as F
import torch
from torchvision import transforms

test_path = os.path.join('', 'images_test')
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
mobilenet = torch.load('models/mobilenet.pth', map_location=torch.device(device))
vgg16 = torch.load('models/vgg16.pth', map_location=torch.device(device))

mobilenet.eval()
vgg16.eval()

def predict(img, model):
    img = transform(img)
    img = img.unsqueeze(0).to(device)
    with torch.no_grad():
        if model == "VGG16":
            output = vgg16(img)
        else:
            output = mobilenet(img)
        predicted_probabilities = F.softmax(output, dim=1)
        confidence_score, predicted_label = torch.max(predicted_probabilities, 1)
        predicted_label = predicted_label.item()

    return predicted_label,label_map[predicted_label]

label_map = {
    0: 'Bảo tàng Chứng tích Chiến tranh',
    1: 'Bảo tàng Hồ Chí Minh Hà Nội',
    2: 'Bảo tàng Mĩ thuật',
    3: 'Bến Nhà Rồng',
    4: 'Bitexco',
    5: 'Bưu điện Thành phố Hồ Chí Minh',
    6: 'Cầu Rồng',
    7: 'Cầu Vàng',
    8: 'Chợ Bến Thành',
    9: 'Chùa Bửu Long',
    10: 'Chùa Long Sơn',
    11: 'Chùa Một cột',
    12: 'Chùa Thiên Mụ',
    13: 'Chùa Trấn Quốc',
    14: 'Chùa Vĩnh Nghiêm',
    15: 'Dinh Độc lâp',
    16: 'Hồ con rùa',
    17: 'Hoàng thành Thăng Long',
    18: 'Kinh Thành Huế',
    19: 'Landmark81',
    20: 'Lăng Chủ tịch Hồ Chí Minh',
    21: 'Thánh địa Mỹ Sơn',
    22: 'Nhà hát lớn Hà Nội',
    23: 'Nhà thờ Đức Bà',
    24: 'Nhà thờ Giáo sứ Tân Định',
    25: 'Nhà thờ Lớn Hà Nội',
    26: 'Quảng trường Lâm Viên',
    27: 'Tháp bà Ponagar'
}
