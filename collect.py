import sys

from git import Repo


def clone_repo(link: str):
    parts = link.split("/")
    name = parts[len(parts) - 1]
    print(name)
    Repo.clone_from(link, f"dataset/{name}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        repositories = "repos.txt"
    else:
        repositories = sys.argv[1]
    with open(repositories, "r") as f:
        data = f.read()
    lines = data.split()
    for rep in lines:
        clone_repo(rep)
