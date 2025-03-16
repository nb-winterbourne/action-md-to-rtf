import pypandoc
import pathlib

class File:
    def __init__(self, path):
        self.path = path.as_posix()
        self.name = self._extract_name()

    def _extract_name(self):
        name = self.path.split('.')[:-1]
        if len(name) > 1:
            name = ".".join(name)
        else:
            name = name[0]
        return name

def get_manu_files():
    files = []
    paths = pathlib.Path('manuscript')
    for path in paths.rglob('*'):
        if path.is_file():
            files.append(File(path))
    return files

def main():
	print('hello world!')
	files = get_manu_files()
	print(f'files names to convert: {f.name for f in files}')

main()