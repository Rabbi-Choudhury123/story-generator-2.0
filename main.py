import random
print("This is the random story generator ")

who = ["dog","cow","moose", "person", "dave"]
when = ["1977", "1888", "1432","1654","65 bc"]
where = ["toronto","montreal","new york", "california"]
what = ["eating", "partying", "swimming", "playing","working"]

random_choice = random.choice(who)

if len(random.choice(who)) > 3:
  print("The ", random_choice[0:3], " in ", random.choice(where), " was ", random.choice(what), " during ", random.choice(when))

else:
   print("The ", random.choice(who), " in ", random.choice(where), " was ", random.choice(what), " during ", random.choice(when))
