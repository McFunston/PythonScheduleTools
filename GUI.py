import tkinter
from tkinter import filedialog
import CheckStatusByFiles
import CheckStatusByLog
result = "test"
class ScheduleToolsGUI(tkinter.Frame):

    def __init__(self, root):

        tkinter.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': tkinter.constants.BOTH, 'padx': 10, 'pady': 10}

        # define GUI
        tkinter.Button(self, text='Check Files In', command=self.check_files_in).pack(**button_opt)
        tkinter.Button(self, text='Check Proofs Out', command=self.check_proofs_out).pack(**button_opt)
        tkinter.Button(self, text='Check Proofs In', command=self.asksaveasfile).pack(**button_opt)
        self.l = tkinter.StringVar()
        self.l.set("test")
        self.results_box = tkinter.Text(self)
        tkinter.Label(self, textvariable=self.l).pack()
        self.results_box.insert(tkinter.END, "Results will go here")
        #self.results_box.config(state="disabled")
        self.results_box.pack(expand=True, fill="both")

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
        files_in.clear()
        dockets_files = CheckStatusByFiles.check_status_by_files('Printflow-ToDo1.xls', 2, 3, 'Files In', '/Volumes/Dockets', '/Production/Print')
        for dockets_file in dockets_files:
            files_in.append(dockets_file)        
        insite_files = CheckStatusByFiles.check_status_by_files('Printflow-ToDo1.xls', 2, 3, 'Files In', '/Volumes/AraxiVolume_PRINERGYEPM_J/Jobs', '/System/SubPages')
        for insite_file in insite_files:
            files_in.append(insite_file)
        self.l.set("it worked")
        self.results_box.config(state="normal")
        self.results_box.delete(1.0, tkinter.END)
        for file_in in files_in:
            if file_in:
                self.results_box.insert(tkinter.END, file_in)
                self.results_box.insert(tkinter.END, '\n\n')
        self.results_box.config(state="disabled")

    def check_proofs_out(self):
        proofs_out = list()
        proofs_out.clear()
        proofs_out=CheckStatusByLog.check_status_by_csv('Printflow-ToDo1.xls', 2, 3, 'Proof Out', 'ProofLog.csv')
        self.results_box.config(state="normal")
        self.results_box.delete(1.0, tkinter.END)
        for proof in proofs_out:
            self.results_box.insert(tkinter.END, proof)
            self.results_box.insert(tkinter.END, '\n\n')
        self.results_box.config(state="disabled")

    def asksaveasfile(self):

        """Returns an opened file in write mode."""

        return filedialog.asksaveasfile(mode='w', **self.file_opt)

if __name__=='__main__':
    root = tkinter.Tk()
    ScheduleToolsGUI(root).pack()
    root.mainloop()