import os

gitzip_txt = "gitzip.txt"
output_dir = os.getcwd()


def main():
    with open(gitzip_txt, "r", encoding="UTF-8") as gitzip:
        line = gitzip.readline()
        while True:
            if line:
                mode, path = line.split()
            else:
                break
            if mode == "---FOLDER":
                os.makedirs(os.path.join(output_dir, path))
                line = gitzip.readline()
            elif mode == "---FILE":
                with open(os.path.join(output_dir, path), "w", encoding="UTF-8") as f:
                    line = gitzip.readline()
                    while line and not line.startswith("---"):
                        f.write(line)
                        line = gitzip.readline()


main()
