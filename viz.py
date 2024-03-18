import matplotlib.pyplot as plt
import io
import base64

def visualize_male_female_ratio_in_hero(male_count, female_count):
    # Plotting the data
    labels = ['Male', 'Female']
    counts = [male_count, female_count]

    plt.bar(labels, counts)
    plt.title('Male vs Female Ratio in Heroes')
    plt.xlabel('Gender')
    plt.ylabel('Count')

    # Save the plot to a BytesIO object
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    # Encode the plot image to base64
    img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')

    plt.close()  # Close the plot to free memory

    return img_base64