import pandas as pd
import numpy as np
import random

def syn_0():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',  # Ngày Giải phóng miền Nam
        '2023-09-02',  # Quốc Khánh
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1, 6, 7, 8, 12]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.5,
        'adults': 0.3,
        'seniors': 0.2
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.3

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_0.csv', index=False)
    print('Created synthetic data 0')


def syn_1():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',  # Ngày Giải phóng miền Nam
        '2023-09-02',  # Quốc Khánh
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [4, 5, 9, 12]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.5,
        'adults': 0.18,
        'seniors': 0.32
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.3

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_1.csv', index=False)
    print('Created synthetic data 1')


def syn_2():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [9, 10, 11, 12, 1, 2, 3, 4]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.55,
        'adults': 0.13,
        'seniors': 0.32
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.1

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_2.csv', index=False)
    print('Created synthetic data 2')


def syn_3():
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',  # Ngày Giải phóng miền Nam
        '2023-05-01',
        '2023-09-02',  # Quốc Khánh
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1, 6, 7, 8, 12]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.6,
        'adults': 0.3,
        'seniors': 0.1
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.4

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_3.csv', index=False)
    print('Created synthetic data 3')


#'Bitexco': 4,
def syn_4():
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1,2,3,4,12]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.55,
        'adults': 0.25,
        'seniors': 0.2
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.275

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_4.csv', index=False)
    print('Created synthetic data 4')


def syn_5():
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',  # Ngày Giải phóng miền Nam
        '2023-05-01',
        '2023-09-02',  # Quốc Khánh
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1, 6, 7, 8, 12]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.5,
        'adults': 0.4,
        'seniors': 0.1
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.345

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_5.csv', index=False)
    print('Created synthetic data 5')


def syn_6():
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',  # Ngày Giải phóng miền Nam
        '2023-05-01',
        '2023-09-02',  # Quốc Khánh
        '2023-12-25', #marry christmas
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1, 6, 7, 8, 12]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.6,
        'adults': 0.35,
        'seniors': 0.05
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.5

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_6.csv', index=False)
    print('Created synthetic data 6')


def syn_7():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',  # Ngày Giải phóng miền Nam
        '2023-05-01',
        '2023-09-02',  # Quốc Khánh
        '2023-12-25', #marry christmas
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1, 6, 7, 8, 12]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.5,
        'adults': 0.45,
        'seniors': 0.05
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.4

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_7.csv', index=False)
    print('Created synthetic data 7')


def syn_8():
    # Danh sách các ngày lễ lớn
    holidays = [
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1, 2, 3, 4, 12]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.2,
        'adults': 0.6,
        'seniors': 0.2
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.6

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_8.csv', index=False)
    print('Created synthetic data 8')


def syn_9():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-08-30', #Lễ Vu Lan
        '2023-06-02', #Lễ Phật Đản
        '2023-02-05',  # Rằm tháng Giêng
        '2023-03-07',  # Rằm tháng 2
        '2023-04-05',  # Rằm tháng 3
        '2023-05-05',  # Rằm tháng 4
        '2023-06-03',  # Rằm tháng 5
        '2023-07-03',  # Rằm tháng 6
        '2023-08-01',  # Rằm tháng 7
        '2023-08-30',  # Rằm tháng 8
        '2023-09-29',  # Rằm tháng 9
        '2023-10-28',  # Rằm tháng 10
        '2023-11-26',  # Rằm tháng 11
        '2023-12-26',  # Rằm tháng Chạp
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1, 6, 8]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.05,
        'adults': 0.35,
        'seniors': 0.6
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.15

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_9.csv', index=False)
    print('Created synthetic data 9')


def syn_10():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-08-30', #Lễ Vu Lan
        '2023-06-02', #Lễ Phật Đản
        '2023-02-05',  # Rằm tháng Giêng
        '2023-03-07',  # Rằm tháng 2
        '2023-04-05',  # Rằm tháng 3
        '2023-05-05',  # Rằm tháng 4
        '2023-06-03',  # Rằm tháng 5
        '2023-07-03',  # Rằm tháng 6
        '2023-08-01',  # Rằm tháng 7
        '2023-08-30',  # Rằm tháng 8
        '2023-09-29',  # Rằm tháng 9
        '2023-10-28',  # Rằm tháng 10
        '2023-11-26',  # Rằm tháng 11
        '2023-12-26',  # Rằm tháng Chạp
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1, 6, 7, 8, 12]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.1,
        'adults': 0.2,
        'seniors': 0.7
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.3

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_10.csv', index=False)
    print('Created synthetic data 10')


def syn_11():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',  # Ngày Giải phóng miền Nam
        '2023-09-02',  # Quốc Khánh
        '2023-06-01' # Lễ thiếu nhi
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [2,3,4,9,10,11]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.6,
        'adults': 0.3,
        'seniors': 0.1
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.6

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_11.csv', index=False)
    print('Created synthetic data 11')


def syn_12():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-08-30', #Lễ Vu Lan
        '2023-06-02', #Lễ Phật Đản
        '2023-02-05',  # Rằm tháng Giêng
        '2023-03-07',  # Rằm tháng 2
        '2023-04-05',  # Rằm tháng 3
        '2023-05-05',  # Rằm tháng 4
        '2023-06-03',  # Rằm tháng 5
        '2023-07-03',  # Rằm tháng 6
        '2023-08-01',  # Rằm tháng 7
        '2023-08-30',  # Rằm tháng 8
        '2023-09-29',  # Rằm tháng 9
        '2023-10-28',  # Rằm tháng 10
        '2023-11-26',  # Rằm tháng 11
        '2023-12-26',  # Rằm tháng Chạp
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [4,6,9,10,11]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.2,
        'adults': 0.3,
        'seniors': 0.5
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.15

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_12.csv', index=False)
    print('Created synthetic data 12')


def syn_13():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-08-30', #Lễ Vu Lan
        '2023-06-02', #Lễ Phật Đản
        '2023-02-05',  # Rằm tháng Giêng
        '2023-03-07',  # Rằm tháng 2
        '2023-04-05',  # Rằm tháng 3
        '2023-05-05',  # Rằm tháng 4
        '2023-06-03',  # Rằm tháng 5
        '2023-07-03',  # Rằm tháng 6
        '2023-08-01',  # Rằm tháng 7
        '2023-08-30',  # Rằm tháng 8
        '2023-09-29',  # Rằm tháng 9
        '2023-10-28',  # Rằm tháng 10
        '2023-11-26',  # Rằm tháng 11
        '2023-12-26'  # Rằm tháng Chạp
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [5,6,7,8,10,11]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.1,
        'adults': 0.35,
        'seniors': 0.55
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.2

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_13.csv', index=False)
    print('Created synthetic data 13')


def syn_14():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-08-30', #Lễ Vu Lan
        '2023-06-02', #Lễ Phật Đản
        '2023-02-05',  # Rằm tháng Giêng
        '2023-03-07',  # Rằm tháng 2
        '2023-04-05',  # Rằm tháng 3
        '2023-05-05',  # Rằm tháng 4
        '2023-06-03',  # Rằm tháng 5
        '2023-07-03',  # Rằm tháng 6
        '2023-08-01',  # Rằm tháng 7
        '2023-08-30',  # Rằm tháng 8
        '2023-09-29',  # Rằm tháng 9
        '2023-10-28',  # Rằm tháng 10
        '2023-11-26',  # Rằm tháng 11
        '2023-12-26',  # Rằm tháng Chạp
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [2,3,4,9,10,11]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.1,
        'adults': 0.25,
        'seniors': 0.65
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.15

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_14.csv', index=False)
    print('Created synthetic data 14')


def syn_15():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',  # Ngày Giải phóng miền Nam
        '2023-09-02',  # Quốc Khánh
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1,2,3,4,12]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.5,
        'adults': 0.2,
        'seniors': 0.3
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.32

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_15.csv', index=False)
    print('Created synthetic data 15')


def syn_16():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',
        '2023-05-01'
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [4,5,6]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.7,
        'adults': 0.25,
        'seniors': 0.05
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.15

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_16.csv', index=False)
    print('Created synthetic data 16')


def syn_17():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22'  # Tết Nguyên Đán
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [4,5,9,10,11]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.5,
        'adults': 0.4,
        'seniors': 0.1
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.35

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_17.csv', index=False)
    print('Created synthetic data 17')


def syn_18():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',
        '2023-05-01'
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [9,10,11,1,2,3]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.2,
        'adults': 0.6,
        'seniors': 0.2
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.056

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_18.csv', index=False)
    print('Created synthetic data 18')


#'Landmark_81': 19
def syn_19():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',
        '2023-05-01',
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [4, 5, 9, 12]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.6,
        'adults': 0.28,
        'seniors': 0.12
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.1

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_19.csv', index=False)
    print('Created synthetic data 19')

def syn_20():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',
        '2023-05-01',
        '2023-05-19'
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1,2,3,4,9,10,11,12]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.6,
        'adults': 0.2,
        'seniors': 0.2
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.4

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_20.csv', index=False)
    print('Created synthetic data 20')


def syn_21():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',
        '2023-05-01'
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1,2,3,9,10,11]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.15,
        'adults': 0.7,
        'seniors': 0.15
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.58

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_21.csv', index=False)
    print('Created synthetic data 21')


def syn_22():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',
        '2023-05-01',
        '2023-04-29'
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1,2,3,4,9,10,11]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.10,
        'adults': 0.7,
        'seniors': 0.20
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.5

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_23.csv', index=False)
    print('Created synthetic data 23')


def syn_23():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',
        '2023-05-01',
        '2023-12-25'
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1,2,3,9,10,11]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.3,
        'adults': 0.6,
        'seniors': 0.1
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.3

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_23.csv', index=False)
    print('Created synthetic data 23')


def syn_24():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',
        '2023-05-01',
        '2023-12-30',
        '2023-01-01',
        '2023-12-25'
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1,2,3,9,10,11]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.1,
        'adults': 0.6,
        'seniors': 0.3
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.23

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_24.csv', index=False)
    print('Created synthetic data 24')


def syn_25():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',
        '2023-05-01',
        '2023-04-29'
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1,2,3,9,10,11]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.35,
        'adults': 0.5,
        'seniors': 0.15
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.25

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_25.csv', index=False)
    print('Created synthetic data 25')


# quang truong lam vien
def syn_26():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',
        '2023-05-01',
        '2023-12-15',
        '2023-12-22'
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [10, 11, 12, 1, 2, 3, 4]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.5,
        'adults': 0.3,
        'seniors': 0.2
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.26

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_26.csv', index=False)
    print('Created synthetic data 26')


def syn_27():
    # Danh sách các ngày lễ lớn
    holidays = [
        '2023-01-22',  # Tết Nguyên Đán
        '2023-04-30',
        '2023-05-01',
        '2023-02-28'
    ]

    # Thêm ngày cuối tuần trong năm 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    weekends = dates[dates.weekday >= 5]

    # Các tháng du lịch cao điểm
    peak_months = [1, 2, 3, 4, 9, 10, 11]

    # Tạo một dataframe chứa các ngày du lịch cao điểm
    peak_dates = dates[dates.month.isin(peak_months)]

    # Hợp nhất ngày lễ, cuối tuần và ngày cao điểm
    special_dates = pd.to_datetime(list(set(holidays) | set(weekends) | set(peak_dates)))

    # Tạo dữ liệu tổng hợp
    data = []

    # ID bắt đầu từ 1
    id_counter = 1

    # Các nhóm tuổi khác nhau
    age_groups = {
        'students': (12, 22),  # Học sinh, sinh viên
        'adults': (23, 60),  # Người trưởng thành
        'seniors': (61, 80)  # Người lớn tuổi
    }

    # Xác suất cho mỗi nhóm tuổi
    age_group_probs = {
        'students': 0.5,
        'adults': 0.3,
        'seniors': 0.2
    }

    # Tỷ lệ khách quốc tế
    foreign_prob = 0.43

    for date in special_dates:
        # Xác định số lượng khách trong một ngày, có thể ngẫu nhiên từ 50 đến 200
        num_visitors = random.randint(50, 300)

        for _ in range(num_visitors):
            age_group = np.random.choice(list(age_groups.keys()), p=list(age_group_probs.values()))
            age_range = age_groups[age_group]
            age = random.randint(age_range[0], age_range[1])
            is_foreign = np.random.choice([0, 1], p=[1 - foreign_prob, foreign_prob])

            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Tạo dataframe từ dữ liệu
    df = pd.DataFrame(data, columns=['Id_person', 'Is_foreign', 'Age', 'Date'])

    # Lưu dữ liệu vào file CSV
    df.to_csv('syn_data/syn_27.csv', index=False)
    print('Created synthetic data 27')


if __name__ == '__main__':
    for i in range(0, 28):
        globals()[f"syn_{i}"]()
