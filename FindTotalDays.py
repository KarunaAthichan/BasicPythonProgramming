day = int(input("Enter the day: "))
month = int(input("Enter the month: "))

# Enter the total days for each month in a list
t_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Initialise total days as zero
totaldays = 0

# For iteration range as month - 1 (e.g. 3-1=2 so range taken as 0 & 1)
for i in range(month - 1):
    # add days for each iteration
    totaldays = totaldays + t_days[i]

# total days added with entered day of the month
totaldays = totaldays + day

print("Total days are : ", totaldays)