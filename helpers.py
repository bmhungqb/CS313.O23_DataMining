import os
import torch.nn.functional as F
import torch
import torchvision
from torchvision import transforms
import torch.nn as nn

os.environ['OPENAI_API_KEY'] = 'sk-proj-AzokoANVUeddZTtLVTlET3BlbkFJV0QXYkqQl5yybJOmlrxr'
data_dir = ''
test_path = os.path.join(data_dir, 'images_test')
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

model = torchvision.models.mobilenet_v2()
num_ftrs = model.classifier[1].in_features
model.classifier[1] = nn.Linear(num_ftrs, 31)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# Send model to device
model = model.to(device)
model.load_state_dict(torch.load('pretrained/weight_5.pth', map_location=torch.device(device)))
model.eval()


def get_full_place(place):
    destination = {
        "thành phố Hồ Chí Minh": ["Bảo tàng Chứng tích Chiến tranh", "Chợ Bến Thành", "Nhà thờ Đức Bà",
                                  "Bảo tàng Mĩ thuật", "Bitexco", "Bưu điện Thành phố Hồ Chí Minh",
                                  "Chùa Bửu Long", "Crescent Mall", "Landmark 81",
                                  "Ủy ban Nhân dân Thành phố Hồ Chí Minh", "Emart Sala",
                                  "Hồ con rùa", "Nhà thờ Giáo sứ Tân Định", "Bến Nhà Rồng", "Dinh Độc lập",
                                  "Chùa Vĩnh Nghiêm"],
        "thành phố Đà Nẵng": ["Cầu Rồng", "Cầu Vàng"],
        "thành phố Hà Nội": ["Lăng Chủ tịch Hồ Chí Minh", "Bảo tàng Hồ Chí Minh Hà Nội", "Nhà thờ Lớn Hà Nội",
                             "Chùa Một cột", "Chùa Trấn Quốc", "Hoàng thành Thăng Long", "Nhà hát lớn Hà Nội"],
        "tỉnh Thừa Thiên-Huế": ["Chùa Thiên Mụ", "Kinh Thành Huế"],
        "tỉnh Khánh Hòa": ["Chùa Long Sơn", "Tháp bà Ponagar"],
        "tỉnh Quảng Nam": ["Thánh Địa Mỹ Sơn"],
        "tỉnh Lâm Đồng": ["Quảng trường Lâm Viên"]
    }
    temp = [key for key, value in destination.items() if place in value][0]
    return place + ", " + temp

def predict(img):
    img = transform(img)
    img = img.unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(img)
        predicted_probabilities = F.softmax(output, dim=1)
        confidence_score, predicted_label = torch.max(predicted_probabilities, 1)
        predicted_label = predicted_label.item()

    # Get the label names
    predicted_label_id = map_to_id[predicted_label]
    predicted_label_name = label_map[predicted_label_id]
    return predicted_label_name


map_to_id = {
    0: 1,
    1: 10,
    2: 11,
    3: 12,
    4: 13,
    5: 14,
    6: 15,
    7: 16,
    8: 17,
    9: 18,
    10: 19,
    11: 2,
    12: 20,
    13: 21,
    14: 22,
    15: 23,
    16: 24,
    17: 25,
    18: 26,
    19: 27,
    20: 27,
    21: 27,
    22: 3,
    23: 30,
    24: 31,
    25: 4,
    26: 5,
    27: 6,
    28: 7,
    29: 8,
    30: 9
}

label_map = {
    1: 'Bảo tàng Chứng tích Chiến tranh',  #
    2: 'Bảo tàng Hồ Chí Minh Hà Nội',  #
    3: 'Bảo tàng Mĩ thuật',  #
    4: 'Bến Nhà Rồng',  #
    5: 'Bitexco',  #
    6: 'Bưu điện Thành phố Hồ Chí Minh',  #
    7: 'Cầu Rồng',  #
    8: 'Cầu Vàng',  #
    9: 'Chợ Bến Thành',  #
    10: 'Chùa Bửu Long',  #
    11: 'Chùa Long Sơn',  #
    12: 'Chùa Một cột',  #
    13: 'Chùa Thiên Mụ',  #
    14: 'Chùa Trấn Quốc',  #
    15: 'Chùa Vĩnh Nghiêm',  #
    16: 'Cresent Mall',  #
    17: 'Dinh Độc lâp',  #
    18: 'Emart Sala',  #
    19: 'Hồ con rùa',  #
    20: 'Hoàng thành Thăng Long',  #
    21: 'Kinh Thành Huế',  #
    22: 'Landmark81',  #
    23: 'Lăng Chủ tịch Hồ Chí Minh',  #
    24: 'Thánh địa Mỹ Sơn',  #
    25: 'Nhà hát lớn Hà Nội',  #
    26: 'Nhà thờ Đức Bà',  #
    27: 'Nhà thờ Giáo sứ Tân Định',  #
    28: 'Nhà thờ Lớn Hà Nội',  #
    29: 'Quảng trường Lâm Viên',  #
    30: 'Tháp bà Ponagar',  #
    31: 'Ủy ban Nhân dân Thành phố Hồ Chí Minh'  #
}
label_index = {
    'Bảo tàng Chứng tích Chiến tranh': 1,
    'Bảo tàng Hồ Chí Minh Hà Nội': 2,
    'Bảo tàng Mĩ thuật': 3,
    'Bến Nhà Rồng': 4,
    'Bitexco': 5,
    'Bưu điện Thành phố Hồ Chí Minh': 6,
    'Cầu Rồng': 7,
    'Cầu Vàng': 8,
    'Chợ Bến Thành': 9,
    'Chùa Bửu Long': 10,
    'Chùa Long Sơn': 11,
    'Chùa Một cột': 12,
    'Chùa Thiên Mụ': 13,
    'Chùa Trấn Quốc': 14,
    'Chùa Vĩnh Nghiêm': 15,
    'Cresent Mall': 16,
    'Dinh Độc lâp': 17,
    'Emart Sala': 18,
    'Hồ con rùa': 19,
    'Hoàng thành Thăng Long': 20,
    'Kinh Thành Huế': 21,
    'Landmark81': 22,
    'Lăng Chủ tịch Hồ Chí Minh': 23,
    'Thánh địa Mỹ Sơn': 24,
    'Nhà hát lớn Hà Nội': 25,
    'Nhà thờ Đức Bà': 26,
    'Nhà thờ Giáo sứ Tân Định': 27,
    'Nhà thờ Lớn Hà Nội': 28,
    'Quảng trường Lâm Viên': 29,
    'Tháp bà Ponagar': 30,
    'Ủy ban Nhân dân Thành phố Hồ Chí Minh': 31
}
