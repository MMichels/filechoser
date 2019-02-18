import os.path
from io import TextIOWrapper
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename, asksaveasfile


class FileChooser:
    def __init__(self):
        self._tk = Tk()

    def get_open_file_dir(self):
        self._tk.withdraw()
        return str(askopenfilename())

    def get_save_file_dir(self) -> str:
        self._tk.withdraw()
        file = asksaveasfilename(initialdir=self.get_fullpath('..\\arquivos\\'), title="Select file",
                                 filetypes=[("All Files", ".*")], defaultextension='cfg')
        return file

    def get_fullpath(self, path: str):
        self._tk.withdraw()
        return os.path.abspath(path)
