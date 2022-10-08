# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = player_0 + " " + str(goal_0) + ", " + player_1 + " " + str(goal_1)

report = player_0 + ' scored in the ' + str(goal_0) + 'nd minute' + '\n' + player_1 + ' scored in the ' + str(goal_1) + 'th minute' 
print(report)

player = 'Ruud Gullit'
first_name = player[:player.find(" ")]
#print(first_name)
last_name_len = len(player[player.find(" "):-1])
#print(last_name_len)
name_short = player[:1] + "." + player[player.find(" "):]
#print(name_short)
chant =  (first_name + "! ") * len(player[:player.find(" ")])
chant = chant[:-1]
print(chant)
good_chant = chant[-1] != " "
print(good_chant)