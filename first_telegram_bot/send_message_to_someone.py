import telegram
from telegram import ChatMember, ChatMemberUpdated

# create a bot instance
bot_token = 'your_bot_token'
bot = telegram.Bot(token=bot_token)

# get the chat_id of the group and user_id of the user to be added
chat_id = -1001534208076
user_id = 5131883098

# create a ChatMember object with the user_id
chat_member = ChatMember(user_id, None, None)

# add the user to the group
bot.add_chat_members(chat_id, chat_member)

# create a ChatMemberUpdated object to invite the user to the group
chat_member_updated = ChatMemberUpdated(None, chat_id, None, None, chat_member, None)

# invite the user to the group
bot.send_chat_action(chat_id, telegram.ChatAction.TYPING)
bot.send_chat_action(chat_id, telegram.ChatAction.INVITE)
bot.send_chat_action(chat_id, telegram.ChatAction.UPLOAD_PHOTO)
bot.send_chat_action(chat_id, telegram.ChatAction.UPLOAD_VIDEO)
bot.send_chat_action(chat_id, telegram.ChatAction.UPLOAD_AUDIO)
bot.send_chat_action(chat_id, telegram.ChatAction.UPLOAD_DOCUMENT)
bot.send_chat_action(chat_id, telegram.ChatAction.UPLOAD_VIDEO_NOTE)
bot.send_chat_action(chat_id, telegram.ChatAction.UPLOAD_VOICE)
bot.send_chat_action(chat_id, telegram.ChatAction.RECORD_AUDIO)
bot.send_chat_action(chat_id, telegram.ChatAction.FIND_LOCATION)
bot.send_chat_action(chat_id, telegram.ChatAction.RECORD_VIDEO)
bot.send_chat_action(chat_id, telegram.ChatAction.UPLOAD_STICKER)
bot.send_chat_action(chat_id, telegram.ChatAction.UPLOAD_VIDEO)
bot.send_chat_action(chat_id, telegram.ChatAction.UPLOAD_CONTACT)
bot.send_chat_action(chat_id, telegram.ChatAction.UPLOAD_POLL)
bot.send_chat_action(chat_id, telegram.ChatAction.TYPING)
bot.send_chat_action(chat_id, telegram.ChatAction.CHOOSE_CONTACT)
bot.send_chat_action(chat_id, telegram.ChatAction.GAME_PLAY)
bot.send_chat_member_updated(chat_member_updated)
