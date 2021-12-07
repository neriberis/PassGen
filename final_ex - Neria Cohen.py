import sys


def check_id_valid(id_number):
    """Checks if the id entered is valid according to the conditions.
    :param id_number: id number entered by the user
    :type id_number: int
    :return: True if the sum of the id number after doubling the even indexed numbers divides by 10 without reminder
    :return type: bool"""
    if len(str(id_number)) == 9 and str(id_number).isdigit():
        try_list = list(str(id_number))
        # Doubles the even indexed number in the id given and creates a list
        check_id_list = [str(int(try_list[x]) * 2) if x % 2 == 1 else try_list[x] for x in range(len(try_list))]
        # Adds the two digit numbers in the new list
        check_ten = list(map(lambda x: int(x[0]) + int(x[1]) if len(str(x)) == 2 else int(x), check_id_list))
        # Checks if the sum of the newest list divides by 10 without reminder
        return True if sum(check_ten) % 10 == 0 else False


class IDIterator:
    """
    A class that creates an iterator of valid id's
    """
    def __init__(self, num=100000000):
        """An init method for IDIterator class and _id attribute with default _id"""
        self._id = num

    def __iter__(self):
        return self

    def __next__(self):
        """A next method for IDIterator class, creates an iterator of valid id numbers
        :raise: StopIteration: raises an Exception if id iterated is above 999999999
        :return: the next valid id number starting the first one after the entered id number
        :return type: iterator"""
        while self._id < 999999999:
            self._id += 1
            try:
                if self._id >= 999999999:
                    raise StopIteration
            except StopIteration:
                sys.exit("There are no more valid ID numbers")
            else:
                if check_id_valid(self._id):
                    return self._id


def id_gen(id_number):
    """Creates a generator of valid id numbers
    :param id_number: id number entered by the user
    :type id_number: int
    :raise: StopIteration: raises an Exception if id iterated is above 999999999
    :return: the next valid id number starting the first one after the entered id number
    :return type: generator"""
    while id_number < 999999999:
        id_number += 1
        try:
            if id_number == 999999999:
                raise StopIteration
        except StopIteration:
            sys.exit("There are no more valid ID numbers")
        else:
            if check_id_valid(id_number):
                yield id_number


def main():
    """Main function that returns 10 valid id's following the given ID
    :raise: ValueError: raises an Exception according to the valid id conditions"""
    try:
        id_given = int(input("Enter ID: "))
        if not str(id_given).isdigit() or len(str(id_given)) != 9:
            raise ValueError
    except ValueError:
        print("ID number entered is illegal, please try again")
        main()
    else:
        # Function diverges into two different options that lead to the same result, using generator or iterator
        gen_iter = input("Generator or Iterator? (gen/it)? ")
        if gen_iter == 'gen':
            generator_of_id = id_gen(id_given)
            for i in range(10):
                print(next(generator_of_id))
        elif gen_iter == 'it':
            id_iter = iter(IDIterator(id_given))
            for i in range(10):
                print(next(id_iter))


if __name__ == "__main__":
    main()
