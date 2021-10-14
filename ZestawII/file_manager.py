class FileManager:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name, 'r') as read:
            reading = read.readlines()
        return  reading

    def update_file(self, text_data):
        with open(self.file_name, 'a') as update:
            update.write(text_data)