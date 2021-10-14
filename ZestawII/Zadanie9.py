from file_manager import FileManager

trying = FileManager('text_data.txt')
print(trying.read_file())
trying.update_file("wpythonie")
print(trying.read_file())