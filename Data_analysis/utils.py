import pandas as pd
import google.generativeai as genai
from secret_key import google_api_key, pandasai_api_key
from pandasai import Agent, SmartDataframe
from pandasai.llm import OpenAI, GoogleGemini
import os

genai.configure(api_key=google_api_key)
os.environ["PANDASAI_API_KEY"] = pandasai_api_key
model = genai.GenerativeModel('gemini-pro')
llm = GoogleGemini(api_key=google_api_key)

def data_process(url):
    # Read the CSV file and set the index
    data = pd.read_csv(url, index_col=0)
    data['Date'] = pd.to_datetime(data['Date'])
    data['month'] = data['Date'].dt.month

    month_map = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    # Initialize counters for each age group
    teen_age = 0
    middle_age = 0
    old_age = 0

    # Initialize the data_visit DataFrame
    data_visit = pd.DataFrame(0, index=range(1, 13), columns=['Foreign', 'Domestic'])
    data_visit.index.name = 'Index'
    data_visit['month'] = data_visit.index.map(month_map)
    # Iterate over each row in the DataFrame
    for idx, row in data.iterrows():
        age = row["Age"]
        month_index = row['month']

        # Categorize based on age
        if age <= 22:
            teen_age += 1
        elif age <= 60:
            middle_age += 1
        else:
            old_age += 1

        # Count foreign and domestic visits
        if row['Is_foreign']:
            data_visit.loc[month_index, 'Foreign'] += 1
        else:
            data_visit.loc[month_index, 'Domestic'] += 1

    # Add month names to data_visit DataFrame

    # Calculate total visitors
    data_visit['total_visitors'] = data_visit['Foreign'] + data_visit['Domestic']

    # Reset index to be 1, 2, ..., n
    data_visit.reset_index(drop=True, inplace=True)
    data_visit.index += 1

    # Create data_age DataFrame
    data_age = pd.DataFrame({
        "age_group": ["teen_age", "middle_age", "old_age"],
        "count": [teen_age, middle_age, old_age]
    })
    return data_age, data_visit
def plot_data(data_visit, data_age, place, name):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import streamlit as st
    # Set the style to white background with grid
    sns.set_style("whitegrid")

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 10))

    # Set the figure background to be transparent
    fig.patch.set_alpha(0.0)

    # Plot for Monthly Visitors: Foreign, Domestic, and Total
    # Melting the DataFrame
    data_melted = data_visit.melt(id_vars='month', value_vars=['Domestic', 'Foreign'],
                                  var_name='Visitor Type', value_name='Count')

    # Creating the bar plot with white frame
    sns.barplot(ax=ax1, x='month', y='Count', hue='Visitor Type', data=data_melted, palette='viridis',
                edgecolor='white')

    # Adding a line plot for Total Visitors
    ax1.plot(data_visit['month'], data_visit['total_visitors'], color='white', marker='o', linestyle='-',
             label='Số lượng khách du lịch')

    # Adding labels and title with white color
    ax1.set_title(f'Khách du lịch hàng tháng tại {name}', color='white', fontsize=16)
    ax1.set_xlabel('Month', color='white', fontsize=14)
    ax1.set_ylabel('Số lượng khách du lich', color='white', fontsize=14)
    ax1.set_xticklabels(data_visit['month'], rotation=45, color='white', fontsize=12)
    ax1.legend()

    # Set the background of the first subplot to be transparent
    ax1.patch.set_alpha(0.0)

    # Plot for Age Group Distribution
    labels = ["Người trẻ < 22", "Người trưởng thành (23-60)", "Người lớn tuổi > 54"]
    colors = sns.color_palette("viridis", 3)
    ax2.pie(data_age['count'], labels=None, autopct='%1.1f%%', startangle=90, colors=colors)

    ax2.set_title('Phân phối nhóm tuổi', color='white', fontsize=16)
    ax2.legend(labels, loc='upper right')

    # Set the background of the second subplot to be transparent
    ax2.patch.set_alpha(0.0)

    # Set text color to white
    for text in ax2.texts:
        text.set_color('white')

    # Adjust layout
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot(fig)

def query_near_place(place):
    data = pd.read_csv('Data_analysis/dataset.csv', index_col=0)
    agent = SmartDataframe(data, config={"llm": llm, 'verbose': True, 'conversational': False, "seed": 123},
                           description="This dataset contains records of travel destinations, along with information about nearby hotels and restaurants.")
    hotels = agent.chat(
        f"Khách sạn nào gần địa điểm du lịch '{place}', nếu có hãy trả lời 'Các khách sạn gần đó là:' ?")
    restaurants = agent.chat(
        f"Nhà hàng nào gần địa điểm du lịch '{place}', nếu có hãy trả lời 'Các nhà hàng gần đó là:' ?")
    hotels = model.generate_content(f'Hãy chỉnh sửa hình thức câu trả lời này: {hotels} ')
    hotels = hotels.text.replace('•', '  *')
    restaurants = model.generate_content(f'Hãy chỉnh sửa hình thức câu trả lời này: {restaurants} ')
    restaurants = restaurants.text.replace('•', '  *')
    return hotels, restaurants

def describe(place):
    result = model.generate_content(f"Hãy viết một đoạn văn ngắn, khoảng 100 từ, mô tả về {place} bằng tiếng Việt")
    result = result.text.replace('•', '  *')
    return result
def analysis(place, name):
    data_age, data_visit = data_process(f'syn_data/syn_{place}.csv')
    plot_data(data_visit, data_age, place,name)
    agent_visit = SmartDataframe(data_visit, name="Visitor Data",
                                 description="This dataset contains monthly records of the number of foreign, domestic, and total visitors to a specific location."
                                 )
    agent_age = SmartDataframe(data_age, name="Age Distribution Data",
                               description="This dataset contains the number of visitors in each age group: ['người trẻ', 'người trưởng thành','người lớn tuổi'].")
    query_visit = "Based on the data, which are the at least two best months for traveling in terms of visitor numbers?"
    response_visit = agent_visit.chat(query_visit)
    query_age = "Which age groups are popular among visitors? If any two groups are slightly similar, return both?"
    response_age = agent_age.chat(query_age)
    response_visit = model.generate_content(f"Return result translated {response_visit} in vietnamese")
    response_age = model.generate_content(f"Return result translated {response_age} in vietnamese")
    return [response_visit.text, response_age.text]