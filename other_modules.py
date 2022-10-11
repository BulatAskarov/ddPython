import filecmp
import os
import shutil
from pathlib import Path
import tempfile
import zipfile

files_dir = Path("files")

result = filecmp.cmp(
    files_dir / 'file.txt',
    files_dir / 'file2.txt'
)

print(result)

result2 = filecmp.cmpfiles("files", "files2", ["file3.txt"])
match, mismatch, errors = result2
print(match, mismatch, errors)

# удаление папок
# os.rmdir("files2") ошибка, т.к. папка не пустая
# shutil.rmtree("files2") удалит папку

# shutil.copytree('files', 'files2')
print(shutil.disk_usage('.'))

with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as temp_file:
    print(temp_file.name)
    with zipfile.ZipFile(temp_file.name, 'w') as zipfile:
        zipfile.write(files_dir / 'file.txt', "file.txt")
        zipfile.write(files_dir / 'file2.txt', "file2.txt")
