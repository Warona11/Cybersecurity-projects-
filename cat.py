import sys

def cat():
    if len(sys.argv) == 1:
        try:
            for line in sys.stdin:
                print(line, end='')
        except EOFError:
            pass  # Handle EOF gracefully
    else:
        for filename in sys.argv[1:]:
            try:
                with open(filename, 'r') as file:
                    for line in file:
                        print(line, end='')
            except FileNotFoundError:
                print(f"cat: {filename}: No such file or directory", file=sys.stderr)

if __name__ == "__main__":
    cat()
