from datetime import datetime
from random import randint

# Emoji variables to use in your project
world = print ('🌍🌎🌏')
python = 'Python 🐍'
fire = '🔥'

# Emojis to copy and paste into your code:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Useful characters :',()*_/.#

# Function definitions

# Put code to run under here
print('hello, world')
print('welcome to',python)
print(python, 'is very good at maths')
print(230*5782**2/23781)
print(2*45)
print('the date and time is', datetime.now())

def roll_dice():
    max = input('How many sides??:')
    print('That\'s a D', max)
    roll = randint(1, int(max))
    print('You rolled a', roll, fire * roll)

roll_dice()

print('I ❤...')
print('... makes me 😀')
print('I\'d like to make silly things with', python)