def local_settings(self):
    local_safe = open('settings.txt', 'r+')
    inhalt_local_safe = local_safe.read()
    inhalt_ready = inhalt_local_safe.splitlines()
    user_settings = inhalt_ready[0].split(",")
    self.username = user_settings[0]
    self.password = user_settings[1]
    self.host = inhalt_ready[1]
    self.database = inhalt_ready[2]
    self.database_login()