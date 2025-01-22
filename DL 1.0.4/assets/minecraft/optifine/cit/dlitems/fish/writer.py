import fileinput
import glob
import sys
itemid = ['447','448', '446', '302', '303', '304', '305', '276', '277', '278', '279', '273', '310', '313', '312', '313', '256', '257', '258', '267', '292', '306', '307', '309', '298', '299', '300', '301', '283', '284', '285', '286', '294', '314', '315', '316', '317']
itemname = ['acacia_boat','dark_oak_boat', 'jungle_boat', 'chainmail_helmet', 'chainmail_chestplate', 'chainmail_leggings', 'chainmail_boots', 'diamond_sword', 'diamond_shovel', 'diamond_pickaxe', 'diamond_axe', 'diamond_hoe', 'diamond_helmet', 'diamond_chestplate', 'diamond_leggings', 'diamond_boots', 'iron_shovel', 'iron_pickaxe', 'iron_axe', 'iron_sword', 'iron_shovel', 'iron_helmet', 'iron_chestplate', 'iron_leggings', 'iron_boots', 'leather_helmet', 'leather_chestplate', 'leather_leggings', 'leather_boots', 'golden_sword', 'golden_shovel', 'golden_pickaxe', 'golden_axe', 'golden_axe', 'golden_helmet', 'golden_chestplate', 'golden_leggings', 'golden_boots']

for (a, b) in zip(itemid, itemname):
    for line in fileinput.input(glob.glob('*.properties'), inplace=True):
        sys.stdout.write(line.replace(a, b))





    

#for line in fileinput.input(glob.glob('*.properties'), inplace=True):
#    for i in list
#    sys.stdout.write(line.replace(itemid, itemname))
#print('done!')
