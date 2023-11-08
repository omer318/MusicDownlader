import os

def get_links():
    """gets a link and folder name duo
    like link|folder

    Returns:
        _type_: _description_
    """
    with open('queries.txt') as f:
        return [row.split('|') for row in f.read().split('\n') if "#" not in row]

def download(link,out_dir):
    os.system(f'spotDL "{link}" --output="{out_dir}"')


def main():
    for link in get_links():
        download(*link)


if __name__ == "__main__":
    main()
