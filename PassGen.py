import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip as pc


root = tk.Tk()
root.title('PassGen')
root.geometry('400x90+480+330')
pass_type_option1 = tk.Label(root, text="First, enter your required password length (6-20): ",
                             fg='black', font='Times 12')
pass_type_option1.grid(row=0, column=0)
pass_len_entry = tk.Entry(root, font='times 12', width=5, justify='center', relief='solid')
pass_len_entry.grid(row=0, column=1)
pass_type_option2 = tk.Label(root, text="Then, for a password with at least one uppercase,\n"
                                        "lowercase, digit and symbol, click All,\n for one without symbols, click WS.",
                             fg='black', font='Times 12')
pass_type_option2.grid(row=1, column=0)


class PassGen:
    def __init__(self, dice_number):
        """Main class that determines the random password's length
        :param dice_number: 3 for the password not to contain symbols, 4 to contain symbols
        :type dice_number: int
        :return: The length of the random password and it's requested characters types
        :raise LengthException: raises an exception if the password's length entered is invalid as decided"""
        self._new_pass = ""
        self._dice_number = dice_number
        try:
            self._pass_len = int(pass_len_entry.get())
            if self._pass_len > 20 or self._pass_len < 6:
                raise LengthException
        except ValueError:
            raise LengthException

    def genpass(self):
        """A method that generates the random characters for the password,
        at least one of each kind(upper, lower, digit and punctuation)
        and makes sure it doesn't have the same character twice by removing the used one from the specific list"""
        up_list = list(string.ascii_uppercase)
        lo_list = list(string.ascii_lowercase)
        dig_list = list(string.digits)
        punc_list = list(string.punctuation)
        for i in range(self._pass_len):
            dice = random.randint(1, self._dice_number)
            if dice == 1:
                upper_char = up_list[random.randint(0, len(up_list) - 1)]
                self._new_pass += upper_char
                up_list.remove(upper_char)
            elif dice == 2:
                lower_char = lo_list[random.randint(0, len(lo_list) - 1)]
                self._new_pass += lower_char
                lo_list.remove(lower_char)
            elif dice == 3:
                dig_char = dig_list[random.randint(0, len(dig_list) - 1)]
                self._new_pass += dig_char
                dig_list.remove(dig_char)
            elif dice == 4:
                punc_char = punc_list[random.randint(0, len(punc_list) - 1)]
                self._new_pass += punc_char
                punc_list.remove(punc_char)
        return self._new_pass


class LengthException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        messagebox.showerror(title="PassGen", message="You've entered an invalid password length, "
                                                      "please enter a valid length (6-20)")


def all_move_to_length():
    """A function to generate the required random password with the all the characters types and in the required length
    and allows the user to copy the password"""
    all_password = PassGen(4)
    pass_all = all_password.genpass()
    # A code to make sure there is at least one upper, lower, digit and punc in the password generated
    # else rerun the function
    if any(a in pass_all for a in list(string.ascii_uppercase)) and any(b in pass_all
                                                                        for b in list(string.ascii_lowercase))\
            and any(c in pass_all for c in list(string.digits)) and any(d in pass_all
                                                                        for d in list(string.punctuation)):
        pass_opt1 = messagebox.askquestion('PassGen', message='Your new password is: \n' + pass_all +
                                                              '\nWould you like to copy it?')
        if pass_opt1 == 'yes':
            pc.copy(pass_all)
        elif pass_opt1 == 'no':
            pass
    else:
        all_move_to_length()


def ws_move_to_length():
    """A function to generate the required random password without punctuation and in the required length
        and allows the user to copy the password"""
    ws_password = PassGen(3)
    pass_ws = ws_password.genpass()
    # A code to make sure there is at least one upper, lower and digit in the password generated
    # else rerun the function
    if any(a in pass_ws for a in list(string.ascii_uppercase)) and any(b in pass_ws
                                                                       for b in list(string.ascii_lowercase))\
            and any(c in pass_ws for c in list(string.digits)):
        pass_opt2 = messagebox.askquestion('PassGen', message='Your new password is: \n' + pass_ws +
                                                              '\nWould you like to copy it?')
        if pass_opt2 == 'yes':
            pc.copy(pass_ws)
        elif pass_opt2 == 'no':
            pass
    else:
        ws_move_to_length()


# The two buttons for activating the different password generators
tk.Button(root, text='All', command=all_move_to_length, width=4, font='times 12').grid(row=1, column=1)
tk.Button(root, text='WS', command=ws_move_to_length, width=4, font='times 12').grid(row=1, column=2)

if __name__ == "__main__":
    """Main function that runs the tkinter window"""
    root.mainloop()
