from os import path
from hashlib import sha1
from base64 import b64encode

def xor(text, key):
    res = []
    for c in text:
        res.append(ord(c) ^ key)
    return b64encode(bytes(res))

def generate(random, pid, autogen_tools, n):
    """
    Generate an instance of the problem
    Needs to return a list of files to copy to particular instance.
    """

    #Get a random build path
    generator_path = autogen_tools.get_directory(__file__)

    template_path = path.join(generator_path, "encrypted.template")
    rendered_template_path = path.join(generator_path, "encrypted")

    key = "xor_20134113"
    flag = "flag_" + sha1((str(n) + key).encode('utf-8')).hexdigest()
    text = xor(flag, random.randint(0x1,0xff))

    autogen_tools.replace_source_tokens(
        template_path,
        {"text": text},
        rendered_template_path
    )

    encrypted_link = autogen_tools.generate_resource_link(pid, "encrypted", title="encrypted")
    source_link = autogen_tools.generate_resource_link(pid, "diary.py", static=True, title="script")

    return {
        "resource_files": {
            "public": [
                (rendered_template_path, "encrypted"),
            ],
        },
        "static_files": {
        },
        "problem_updates": {
        "description": "<p>A friend of yours has been using this %s to encrypt his diary. Being the nosy person you are, you must take a look! Can you decrypt it?</p><p>%s</p>" % (source_link, encrypted_link)
        }
    }
