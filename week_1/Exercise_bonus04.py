'''
The Office for National Statistics projects population based on the following
assumptions:
- One birth every 40 seconds
- One death every minute
- One new immigrant every 1 minute and 40 seconds
Here is a program to display the population for each of the next five years.
Assume the current population is 64,596,800 and one year has 365 days.
'''
current_population = 64596800
birth_per_year = 365 * 24 * 60 * 60 // 40
death_per_year = 365 * 24 * 60 * 60 // 60
immigrant_per_year = 365 * 24 * 60 * 60 // 100
# population in 1 year
print(current_population +
      birth_per_year -
      death_per_year +
      immigrant_per_year)
# population in 2 year
print(current_population +
      2 * birth_per_year -
      2 * death_per_year +
      2 * immigrant_per_year)
# population in 3 year
print(current_population +
      3 * birth_per_year -
      3 * death_per_year +
      3 * immigrant_per_year)
# population in 4 year
print(current_population +
      4 * birth_per_year -
      4 * death_per_year +
      4 * immigrant_per_year)
# population in 5 year
print(current_population +
      5 * birth_per_year -
      5 * death_per_year +
      5 * immigrant_per_year)
