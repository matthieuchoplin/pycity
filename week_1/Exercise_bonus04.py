'''
The Office for National Statistics projects population based on the following assumptions:
- One birth every 40 seconds
- One death every minute
- One new immigrant every 1 minute and 40 seconds
Here is a program to display the population for each of the next five years. Assume the
current population is 64,596,800 and one year has 365 days.
'''
print(64596800 + 365 * 24 * 60 * 60 // 40 - 365 * 24 * 60 * 60 // 60 + 365 * 24 * 60 * 60 // 100)
print(64596800 + 2 * 365 * 24 * 60 * 60 // 40 - 2 * 365 * 24 * 60 * 60 // 60 + 2 * 365 * 24 * 60 * 60 // 100)
print(64596800 + 3 * 365 * 24 * 60 * 60 // 40 - 3 * 365 * 24 * 60 * 60 // 60 + 3 * 365 * 24 * 60 * 60 // 100)
print(64596800 + 4 * 365 * 24 * 60 * 60 // 40 - 4 * 365 * 24 * 60 * 60 // 60 + 4 * 365 * 24 * 60 * 60 // 100)
print(64596800 + 5 * 365 * 24 * 60 * 60 // 40 - 5 * 365 * 24 * 60 * 60 // 60 + 5 * 365 * 24 * 60 * 60 // 100)
