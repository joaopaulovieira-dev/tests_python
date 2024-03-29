import tkinter as tk
import time


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frame = tk.Frame(self)
        self.frame.pack(side="top", fill="both", expand=True)

        self.label = tk.Label(self, text="Hello, world")
        button1 = tk.Button(self, text="Start to do something",
                            command=self.do_something)
        self.label.pack(in_=self.frame)
        button1.pack(in_=self.frame)

    def do_something(self):
        self.label.config(text="Wait till I'm done...")
        self.label.update_idletasks()
        time.sleep(2)
        print("end sleep")
        self.label.config(text="I'm done doing...")


def main():
    app = SampleApp()
    app.mainloop()
    return 0


if __name__ == '__main__':
    main()

# Fonte: https://stackoverflow.com/questions/31358139/how-to-show-a-loading-message-in-tkinter
