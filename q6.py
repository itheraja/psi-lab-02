logs = ["INFO", "ERROR", "WARNING", "INFO", "ERROR", "INFO"]

count = {}

for log in logs:
    if log in count:
        count[log] += 1
    else:
        count[log] = 1

print("Occurrences:", count)

print("Log Types:", list(count.keys()))

most = max(count, key=count.get)

print("Most Frequent:", most)
