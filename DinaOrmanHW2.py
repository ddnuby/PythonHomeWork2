# Dina Orman - 34512568
# Download matplotlib for the IDE
import matplotlib.pyplot as plt
import time

f = open("data.txt", "r")
# Read the entire contents of the file into a single string
data = f.read()


# Split the string into a list of words
l1 = (data.split())
blank_List = []

for string in l1:
    blank_List.append(float(string))

blank_List2 = []

# Plot the raw data
plt.plot(blank_List)
plt.show()

# Start timer
start = time.time()

# Start bubblesort sorting algorithm
def bubbleSort(items):
    n = len(items)
    for i in range(n):
        for j in range (n-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items [j]
    return items
bubbleSort(blank_List)
# End timer
end = time.time()
sort1 = end - start
print("Time consumed in working:", sort1)

# Convert floats to integers for counting sort to work
for i in blank_List:
   blank_List2.append(int(i))


# Start timer
start = time.time()

# Start counting sort sorting algorithm
def countingSort(arr):
# Initialize array to store sorted elements
  sortedarr = [0] * len(arr)

# Loop over arr and count number of each elements' occurrences
  counts = {x: 0 for x in range(min(arr), max(arr)+1)}

  for num in arr:
    counts[num] += 1

# Loop over counts and add it to the corresponding index in the sorted array
  index = 0
  for num, ct in counts.items():
    for i in range(ct):
      sortedarr[index] = num
      index += 1

  return sortedarr

countingSort(blank_List2)
# End timer
end = time.time()
sort2 = end - start
print("Time consumed in working:", sort2)

# Plot the sorted data
plt.plot(blank_List2, range(len(blank_List2)))
plt.show()

# Find out the time complexity of both algorithms by using "if else" statement
if sort1 < sort2:
    print("O(n)")
    change_rate = (sort2/sort1) * 100
    print("O(k)")
else:
    print("O(n2)")
    change_rate = (sort1/sort2) * 100
    print("O(n)")

# Print the change rate
print(change_rate, "%")