import colorama
colorama.init()

from nbck_input import read_line, read_char

if __name__ == "__main__":
    print("read_line: ")
    _ = read_line()
    print("\ninput: ", _)
    print("read_char: ")
    _ = read_char()
    print("\ninput: ", _)