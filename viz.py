import matplotlib.pyplot as plt
from app import userHero


def visualize_male_female_ratio_in_hero():
  # Query the database to get the count of male and female heroes
  male_count = userHero.query.filter_by(gender='Male').count()
  female_count = userHero.query.filter_by(gender='Female').count()

  # Plotting the data
  labels = ['Male', 'Female']
  counts = [male_count, female_count]

  plt.bar(labels, counts)
  plt.title('Male vs Female Ratio in Heroes')
  plt.xlabel('Gender')
  plt.ylabel('Count')
  plt.show()
