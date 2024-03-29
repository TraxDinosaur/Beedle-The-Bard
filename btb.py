import os
import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# Create an instance of the Updater class
updater = Updater(TOKEN, use_context=True)

def start(update, context):
    # Send the image and welcome message to the user
    context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://telegra.ph/file/cf1971b29914e094706d5.jpg', caption='🧙 Welcome to the Harry Potter Beedle the Bard stories bot! 📖 By @wizarding_worldss')

    # Set up the buttons with the names of the Beedle the Bard stories
    keyboard = [[InlineKeyboardButton("🧹 The Wizard and the Hopping Pot", callback_data='1'),
                 InlineKeyboardButton("🌟 The Fountain of Fair Fortune", callback_data='2')],
                [InlineKeyboardButton("🎃 The Warlock's Hairy Heart", callback_data='3'),
                 InlineKeyboardButton("🐰 Babbitty Rabbitty and her Cackling Stump", callback_data='4')],
                [InlineKeyboardButton("🌳 The Tale of the Three Brothers", callback_data='5')]]

    # Create an instance of the InlineKeyboardMarkup class
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the buttons to the user
    update.message.reply_text('Below are the stories ', reply_markup=reply_markup)

def button(update, context):
    # Get the data from the button click
    query = update.callback_query

    # Send the corresponding message based on the button click
    if query.data == '1':
        query.answer()
        query.edit_message_text(text="🧙‍♂️🍲🐸 Once upon a time, there was a powerful wizard who owned a magical 🍲 pot that could cook any dish imaginable. The pot was passed down through generations and was cherished by the wizard's family.\n 🧑‍🦱 However, the wizard was not known for his kindness, and he refused to share his pot with anyone. One day, a poor muggle came to his doorstep seeking help. The wizard, being cruel, slammed the door in his face.\n🐸 As he was about to turn away, the muggle noticed a 🐸 frog that had hopped out of the wizard's garden and into the pot. The pot began to shake and rattle, and out came a delicious stew that the muggle couldn't resist.\n🧙‍♂️ The wizard, furious at the muggle for stealing his stew, demanded to know how he had managed to get it. The muggle told the wizard about the hopping 🍲 pot and how it could cook any dish when a live creature was placed inside it.\n🧑‍🦱 The wizard, intrigued by the possibility of his pot being even more powerful, tried the trick himself. To his surprise, the pot produced a stew so tasty that it warmed the wizard's cold heart.\n🐸 From that day on, the wizard shared his pot with anyone who needed it, and the hopping pot became a symbol of generosity and kindness in the wizarding community. The muggle was rewarded for his honesty, and the wizard became a better person for learning the lesson of compassion.\n🌟 And they all lived happily ever after. 🌟")
    elif query.data == '2':
        query.answer()
        query.edit_message_text(text="📖 Once upon a time, there were four witches who traveled to a fountain called the Fountain of Fair Fortune. 🧙‍♀️🧙‍♀️🧙‍♀️🧙‍♀️ \n The first witch, Asha, had been poisoned by her stepmother and hoped the fountain would cure her. 👩‍🦱💀💊 \n The second witch, Altheda, had lost her wealth and status and wanted to regain her former life. 💰👑🙍‍♀️ \n The third witch, Amata, had been betrayed by her lover and wanted to forget her pain. 💔🤕😔 \n When they arrived at the fountain, they were told that only one of them could bathe in the fountain at a time. They agreed to help each other and draw lots to determine who would bathe first. 🤝🗳️🧺 \n Asha was chosen first and she bathed in the fountain, which cured her of her poisoning. 🛁💊🧪 \n Next, Altheda bathed in the fountain and was given a bag of gold, which allowed her to regain her wealth and status. 💰👑🎒 \n Then, Amata bathed in the fountain and forgot her pain, which allowed her to move on from her past. 🛁😌💆‍♀️ \n Finally, Sir Luckless bathed in the fountain and his curse was lifted, allowing him to have good fortune once again. 🛁🎉🍀\n In the end, they all realized that they didn't need the fountain to be happy and that their friendship was the true source of their good fortune. They left the fountain as friends and lived happily ever after. 🤝❤️🧙‍♀️🧙‍♀️🧙‍♀️🧙‍♀️🌈")
    elif query.data == '3':
        query.answer()
        query.edit_message_text(text="📖 Once upon a time, there was a powerful warlock 👨‍🦳 who believed that love was a weakness. He didn't want to fall in love, so he cast a spell to remove his heart and lock it away 🔒.\n Years passed, and the warlock became known for his dark magic and cold demeanor. But one day, he met a beautiful princess 👸, and despite his efforts, he began to fall in love with her.\n However, without his heart, the warlock's love was twisted and corrupted. He proposed to the princess, but she refused him, and he flew into a rage. He decided to retrieve his heart, but when he opened the chest, he found it had grown a thick layer of hair 🦁.\n The warlock, desperate to remove the hair and feel love again, consulted with many wise men and women, but no one could help him. Eventually, he cut open his chest and tried to rip out the hair himself, but he died in the process.\n The princess, hearing of the warlock's death, went to see the chest and found his heart, now covered in blood 💔. She realized that the warlock had loved her, but his fear and desire for power had led to his downfall.\n 👉 Moral of the story: Love is not a weakness, but denying it can lead to destruction.")
    elif query.data == '4':
        query.answer()
        query.edit_message_text(text="📖 Once upon a time, in a magical land 🧙‍♂️, there lived a kind-hearted washerwoman 🧺 named Babbitty Rabbitty 🐰. She had a special talent, she could talk to animals 🐦🐇🦊, and they loved her dearly.\n One day, the land was ruled by a foolish king 👑 who believed that only he could do magic 🧙‍♂️. He wanted to learn more magic and ordered his advisors to find him a teacher 👨‍🏫. But all the real wizards were afraid of the king's temper and refused to teach him.\n So, the king decided to trick the people of his kingdom into thinking that he had magic by building a huge statue of himself and ordering it to move 🗿. But the statue wouldn't budge, and the king became frustrated 😠.\n Then, he saw Babbitty talking to her animal friends and thought she was a real wizard. He demanded that she teach him magic or be executed 🗡️. Babbitty was scared, but she didn't want to give in to the king's demands.\n To prove her point, she used her magic to make a tree stump cackle like a witch 🌳🧙‍♀️. The king was impressed and demanded that she teach him the spell. But when Babbitty refused, the king ordered his advisors to find someone who could teach him the spell.\n In the end, the king realized the error of his ways and apologized to Babbitty. He learned that true magic comes from the heart, not from trickery or power. And Babbitty lived happily ever after with her animal friends 🐿️🐕🐇.\n 🎉 The end 🎉")
    elif query.data == '5':
        query.answer()
        query.edit_message_text(text="📖 Once upon a time, there were three brothers who were powerful wizards. They were skilled in the arts of magic and were able to conjure up incredible spells. One day, they set out on a journey together and came upon a river too dangerous to cross. 🌊 \n 🧙‍♂️ The eldest brother, who was arrogant and ambitious, decided to use his magic to create a bridge across the river. He crossed the bridge and continued on his journey alone. \n 🧙‍♂️ The second brother was also ambitious but more humble than his elder sibling. He conjured up a powerful spell to create a boat, and he sailed across the river.\n 🧙‍♂️ The third brother, who was the youngest and wisest of the three, did not rely on his magic to cross the river. He instead chose to ask Death for help, who appeared before him and offered him a gift. The brother asked for an unbeatable wand. 💫\n 🧙‍♂️ Death granted the brother's wish and gave him the Elder Wand, which could not be defeated in battle. The brother continued on his journey, but soon came upon a village where a wizard he had once angered lived. The wizard sought revenge and killed the brother in his sleep, taking the wand for himself. \n 🧙‍♂️ The second brother, who had also reached the village, was heartbroken to see his brother dead. He longed to bring him back to life, so he used his magic to create the Resurrection Stone. He summoned the spirit of his dead brother and they spoke, but the brother was not truly alive. \n 🧙‍♂️ The second brother eventually succumbed to the temptation of the stone and took his own life to join his brother in the afterlife. \n 🧙‍♂️ The third brother, who had foreseen the tragic fates of his brothers, hid the Invisibility Cloak, which he had also received from Death, and passed it down to his descendants. He lived a long and fulfilling life, knowing that he had outsmarted Death. \n 🔚 And that is the tale of the Three Brothers, each with their own ambitions and fates, and the gifts that they received from Death.")

# Create instances of the CommandHandler and CallbackQueryHandler classes
start_handler = CommandHandler('start', start)
button_handler = CallbackQueryHandler(button)

# Add the handlers to the updater
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(button_handler)

# Start the bot
updater.start_polling()
