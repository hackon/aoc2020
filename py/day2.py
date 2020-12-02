

def solve_part1(input):
  number_of_valid_passwords = 0
  for line in input.split('\n'):
    print(line)
    rule,password = line.split(': ')
    minmax, char = rule.split(' ')
    min_value, max_value = minmax.split('-')
    char_count = password.count(char)
    if char_count >= int(min_value) and char_count<= int(max_value):
      number_of_valid_passwords += 1
  return number_of_valid_passwords



def solve_part2(input):
  number_of_valid_passwords = 0
  for line in input.split('\n'):
    rule,password = line.split(': ')
    minmax, char = rule.split(' ')
    strindex1, strindex2 = minmax.split('-')
    i1 = int(strindex1)
    i2 = int(strindex2)
    char1 = password[i1-1]
    char2 = password[i2-1]

    if (char1 == char or char2 == char) and (char1 != char2) :
      number_of_valid_passwords +=1

  return number_of_valid_passwords
