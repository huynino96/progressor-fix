import re
from instance import Token
from classes.file import File
from classes.helpers import generate_dates


def count_comment(repository_endpoint):
    token = Token()
    token.repository_endpoint = repository_endpoint
    repo = token.get_repository()
    contents = repo.get_contents("")

    # Counter
    javascript = 0
    python = 0
    java = 0
    php = 0

    while contents:
        file_content = contents.pop(0)
        if file_content.type == 'dir':
            contents.extend(repo.get_contents(file_content.path))
        else:
            fileName = file_content.name
            file = File(fileName)
            if file.is_python() or file.is_java() or file.is_php() or file.is_javascript():
                decoded_content = file_content.decoded_content
                inside_content = decoded_content.decode('utf-8')
                length = len(re.findall(r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/', inside_content))

                if length > 0:
                    if file.is_javascript():  # Javascript
                        javascript += length
                    elif file.is_python():  # Python
                        python += length
                    elif file.is_java():  # Java
                        java += length
                    elif file.is_php():  # PHP
                        php += length

    return generate_dates(javascript, java, python, php)
