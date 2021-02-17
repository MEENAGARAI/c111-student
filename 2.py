import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

mean1 = statistics.mean(data)
std_deviation1 = statistics.stdev(data)

print("mean of popultion:- ",mean1)
print("Standard deviation of popultion:- ",std_deviation1)

# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

# calculating mean and standard_deviation of the sampling distribution.
mean2 = statistics.mean(mean_list)
std_deviation2 = statistics.stdev(mean_list)
print("mean of sampling distribution:- ",mean2)
print("Standard deviation of sampling distribution:- ", std_deviation2)


fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean1, mean2], y=[0, 0.20], mode="lines", name="MEAN"))
fig.show()


