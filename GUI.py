import tkinter
from tkinter import filedialog
import CheckStatusByFiles
result = "test"
class filedialogExample(tkinter.Frame):


    def __init__(self, root):

        tkinter.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': tkinter.constants.BOTH, 'padx': 10, 'pady': 10}

        # define buttons
        tkinter.Button(self, text='Check Files In', command=self.check_files_in).pack(**button_opt)
        tkinter.Button(self, text='Check Proofs Out', command=self.askopenfilename).pack(**button_opt)
        tkinter.Button(self, text='Check Proofs In', command=self.asksaveasfile).pack(**button_opt)
        self.l = tkinter.StringVar()
        self.l.set("test")
        self.results_box = tkinter.Text(self)        
        tkinter.Label(self, textvariable=self.l).pack()
        self.results_box.config(state="disabled")
        self.results_box.pack()

        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = root
        options['title'] = 'This is a title'

        # This is only available on the Macintosh, and only when Navigation Services are installed.
        #options['message'] = 'message'

        # if you use the multiple file version of the module functions this option is set automatically.
        #options['multiple'] = 1

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'This is a title'

    def check_files_in(self):
        files_in = list()
        dockets_files = CheckStatusByFiles.check_status_by_files('Printflow-ToDo1.xls', 2, 3, 'Files In', '/Volumes/Dockets', '/Production/Print')
        files_in.append(dockets_files)
        insite_files = CheckStatusByFiles.check_status_by_files('Printflow-ToDo1.xls', 2, 3, 'Files In', '/Volumes/AraxiVolume_PRINERGYEPM_J/Jobs', '/System/SubPages')
        files_in.append(insite_files)
        self.l.set("it worked")
        self.results_box.delete(1.0, tkinter.END)
        self.results_box.config(state="normal")
        self.results_box.insert(tkinter.END, files_in)
        self.results_box.config(state="disabled")

    def askopenfile(self):

        """Returns an opened file in read mode."""

        return filedialog.askopenfile(mode='r', **self.file_opt)

    def askopenfilename(self):

        """Returns an opened file in read mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """

        # get filename
        filename = filedialog.askopenfilename(**self.file_opt)
        result = filename
        tkinter.Frame.update(self)

        # open file on your own
        if filename:
            return open(filename, 'r')

    def asksaveasfile(self):

        """Returns an opened file in write mode."""

        return filedialog.asksaveasfile(mode='w', **self.file_opt)

    def asksaveasfilename(self):

        """Returns an opened file in write mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """

        # get filename
        filename = filedialog.asksaveasfilename(**self.file_opt)

        # open file on your own
        if filename:
            return open(filename, 'w')

    def askdirectory(self):

        """Returns a selected directoryname."""

        return filedialog.askdirectory(**self.dir_opt)

if __name__=='__main__':
    root = tkinter.Tk()
    filedialogExample(root).pack()
    root.mainloop()