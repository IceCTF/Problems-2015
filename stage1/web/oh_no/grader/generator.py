from os import path
from hashlib import sha1

def generate(random, pid, autogen_tools, n):
    """
    Generate an instance of the problem
    Needs to return a list of files to copy to particular instance.
    """

    #Get a random build path
    generator_path = autogen_tools.get_directory(__file__)

    template_path = path.join(generator_path, "website.html.template")
    rendered_template_path = path.join(generator_path, "website.html")

    key = "oh_no_10236"
    flag = "flag_" + sha1((str(n) + key).encode('utf-8')).hexdigest()

    autogen_tools.replace_source_tokens(
        template_path,
        {"flag": flag},
        rendered_template_path
    )

    homepage_link = autogen_tools.generate_resource_link(pid, "flag.html", title="site")

    return {
        "resource_files": {
            "public": [
                (rendered_template_path, "flag.html"),
            ],
        },
        "static_files": {
        },
        "problem_updates": {
            "description": "We seem to have misplaced the flag! Sorry about that, but we swear it was left on this %s. Perhaps you can find it?" % homepage_link
        }
    }
