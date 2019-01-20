class Message:
    def __init__(self, user_id, user_name, text):
        self.user_id = str(user_id)
        self.user_name = user_name
        self.text = text

    def __str__(self):
        return self.user_id + "<---" + self.text