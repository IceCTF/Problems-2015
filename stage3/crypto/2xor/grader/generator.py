from os import path
from hashlib import sha1
import codecs
import string

def xor(text, key1, key2):
    key1 = key1 * (len(text)//len(key1) + 1)
    key2 = key2 * (len(text)//len(key2) + 1)

    res = ""
    for i in range(len(text)):
        res += chr(ord(text[i]) ^ key1[i] ^ key2[i])
    return res

def random_string(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def generate(random, pid, autogen_tools, n):
    """
    Generate an instance of the problem
    Needs to return a list of files to copy to particular instance.
    """

    #Get a random build path
    generator_path = autogen_tools.get_directory(__file__)

    rendered_template_path = path.join(generator_path, "encrypted")

    key = "xor1123901@#$"
    flag = "flag_" + sha1((str(n) + key).encode('utf-8')).hexdigest()
    with open("plaintext.txt") as plain:
        text = xor(plain.read() + flag, random_string(random.randint(4,8)), random_string(random.randint(3,5)))

    with codecs.open(rendered_template_path, 'w', "utf-8") as out_file:
        out_file.write(text)

    encrypted_link = autogen_tools.generate_resource_link(pid, "encrypted", title="encrypted")
    source_link = autogen_tools.generate_resource_link(pid, "2x0r.py", static=True, title="script")

    return {
        "resource_files": {
            "public": [
                (rendered_template_path, "encrypted"),
            ],
        },
        "static_files": {
            "public": [
                (path.join(generator_path,"2x0r.py"), "2x0r.py")
            ]
        },
        "problem_updates": {
        "description": "<p>So it turns out that repeated XOR isn't exactly secure. After realizing this, Sadobe Corp decided to create a new standard, which it calls 2x0r.</p><p>Clearly, that must raise the computing power required exponentially! They provided a sample implementation here %s.</p><p>They also dared us to get the flag! Ofcourse, we take no such challenge lightly. Beat it out of them if you have to! %s</p>" % (source_link, encrypted_link)
        }
    }
