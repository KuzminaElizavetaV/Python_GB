# ✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
from file_handler import my_functions
from os import chdir, getcwd


my_functions.generic_names()
my_functions.write_rnd_nums_file(10)
my_functions.create_file_from_two_files()
my_functions.make_files_to_dir(r'many_files', txt=3, doc=4, docx=2, jpg=5, bmp=6, gif=2, png=3, avi=2, mov=3, mp4=2,
                               mp3=2, wav=3, aac=1, torrent=2, java=4, sh=2)
chdir('./many_files')
print(getcwd())
my_functions.sort_files_move_directories()
print(getcwd())
chdir('./many_files')
my_functions.rename_files(2, 'torrent', 'tor', [2, 5], end_filename="rename")

