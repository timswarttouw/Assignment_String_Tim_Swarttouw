# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_1 = 'Ruud Gullit'
player_2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = player_1 + " " + str(goal_0) + ", " + player_2 + " " + str(goal_1)

report = player_1 + ' scored in the ' + str(goal_0) + 'nd minute' + '\n' + player_2 + ' scored in the ' + str(goal_1) + 'th minute' 
print(report)

player = 'Ruud Gullit'
first_name = player[0:4]
last_name_len = len(player[5:11])
name_short = player[:1] + ". " + player[5:11]
chant =  (first_name + "! ") * 3 + first_name + "!"
good_chant = chant[22:22] != " "
print(good_chant)
