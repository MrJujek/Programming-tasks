import pandas as pd
import matplotlib.pyplot as plt

while True:
    try:
        filename = input("Enter the name of the file:")
        data = pd.read_csv(f'./{filename}.csv')
    except FileNotFoundError:
        print("File not found")
        continue
    break

plt.scatter(data[data.columns[0]], data[data.columns[1]])
plt.plot(data[data.columns[0]], data[data.columns[1]])
plt.xlabel(data.columns[0])
plt.ylabel(data.columns[1])
plt.title('y=A*sin(2π*t*f)*e^(-y*t)+aN')
plt.show()