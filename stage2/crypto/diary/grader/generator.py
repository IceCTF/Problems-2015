from os import path
from hashlib import sha1

def xor(text, key):
    res = ""
    for c in text:
        res += chr(ord(c) ^ key)
    return 

def generate(random, pid, autogen_tools, n):
    """
    Generate an instance of the problem
    Needs to return a list of files to copy to particular instance.
    """

    #Get a random build path
    generator_path = autogen_tools.get_directory(__file__)

    rendered_template_path = path.join(generator_path, "encrypted")

    key = "xor_20134113"
    flag = "flag_" + sha1((str(n) + key).encode('utf-8')).hexdigest()
    text = xor(flag, random.randint(0x1,0xff)).decode("utf-8")

    out_file = open(rendered_template_path, 'w')
    out_file.write(text)
    out_file.close()

    encrypted_link = autogen_tools.generate_resource_link(pid, "encrypted", title="encrypted")
    source_link = autogen_tools.generate_resource_link(pid, "diary.py", static=True, title="script")

    return {
        "resource_files": {
            "public": [
                (rendered_template_path, "encrypted"),
            ],
        },
        "static_files": {
            "public": [
                (path.join(generator_path, "..", "static","diary.py"), "diary.py")
            ]
        },
        "problem_updates": {
        "description": "<p>A friend of yours has been using this %s to encrypt his diary. Being the nosy person you are, you must take a look! Can you decrypt it?</p><p>%s</p>" % (source_link, encrypted_link)
        }
    }
