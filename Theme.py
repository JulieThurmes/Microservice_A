import time

def main():
    while True:
        time.sleep(1)
        file = open("app_theme.txt", 'r')
        line = file.read()
        file.close()
        if str(line) == "dark mode":
            file = open("app_theme.txt", 'w')
            file.write(str("181818 212121 3d3d3d ffffff aaaaaa"))
            time.sleep(1)
            file.close()

        elif str(line) == "forest":
            file = open("app_theme.txt", 'w')
            file.write(str("1e5636 578c49 99be8f 8f8350 b6a576"))
            time.sleep(1)
            file.close()

        elif str(line) == "original":
            file = open("app_theme.txt", 'w')
            file.write("748a9e b5c9d5 beb8b1 4e5a65 aaaaaa")
            time.sleep(1)
            file.close()

if __name__ == "__main__":
    main()