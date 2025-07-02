from functions.run_python import run_python_file


def test():
    result = run_python_file("calculator", "main.py")
    print("Result for current directory:")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result for 'pkg' directory:")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("Result for '/bin' directory:")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for '/bin' directory:")
    print(result)



if __name__ == "__main__":
    test()
