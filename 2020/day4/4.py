from sys import stdin

passports = []
in_passport = []

for line in stdin:
    if len(line.rstrip()) == 0:
        passports.append(in_passport)
        in_passport = []
    else:
        in_passport.append(line.rstrip())

if in_passport:
    passports.append(in_passport)

needed = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def part_1():

    def valid_passport(passport):

        has = set()

        for line in passport:
            fields = line.split(" ")
            
            for field in fields:

                key = field.split(":")[0]

                if key != "cid":
                    has.add(key)

        return len(has) >= len(needed)

    return sum([valid_passport(passport) for passport in passports])


def part_2():

    def valid_passport(passport):

        eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        valid = set()

        for line in passport:

            fields = line.split(" ")

            for field in fields:

                s = field.split(":")

                key, value = s[0], s[1]
                
                if key == "byr" and 1920 <= int(value) <= 2002:
                    valid.add(key)

                elif key == "iyr" and 2010 <= int(value) <= 2020:
                    valid.add(key)

                elif key == "eyr" and 2020 <= int(value) <= 2030:
                    valid.add(key)

                elif key == "hgt":
                    if "cm" in value and 150 <= int(value[:-2]) <= 193:
                        valid.add(key)

                    elif "in" in value and 59 <= int(value[:-2]) <= 76:
                        valid.add(key)
                
                elif key == "hcl" and value[0] == "#" and (all(x.isalnum() for x in value[1:])):
                    valid.add(key)
                
                elif key == "ecl" and value in eye_colors:
                    valid.add(key)
                
                elif key == "pid" and all(x.isdigit() for x in value) and len(value) == 9:
                    valid.add(key)

        return len(valid) >= len(needed)

    return sum([valid_passport(passport) for passport in passports])



print(part_1())
    
print(part_2())
