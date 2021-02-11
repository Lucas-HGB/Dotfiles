from subprocess import run, PIPE
def get_current_config():
    result = run(["setxkbmap", "-query"], stdout=PIPE)
    return result

def change_config(lang):
    run(["setxkbmap", "-layout", f"{lang}"])

def change():
    config = str(get_current_config())
    if ("us" in config):
        change_config("br")
    elif ("br" in config):
        change_config("us")

if __name__ == "__main__":
    change()
