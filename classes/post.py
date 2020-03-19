from pyrogram import InputMediaPhoto

class Post:
    def __init__(self, text, file_id, file_ref):
        self.text     = text
        self.file_id  = file_id
        self.file_ref = file_ref
    
    def send_post(self, app, chat_id, kb):
        app.send_photo(
            chat_id      = chat_id, 
            photo        = self.file_id,
            file_ref     = self.file_ref,
            caption      = self.text,
            reply_markup = kb)
    
    def edit_post(self, app, chat_id, msg_id, kb):
        app.edit_message_media(
            chat_id      = chat_id,
            message_id   = msg_id,
            media        = InputMediaPhoto(
                                media    = self.file_id,
                                file_ref = self.file_ref,
                                caption  = self.text),
            reply_markup = kb)