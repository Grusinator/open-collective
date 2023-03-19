import os
import fnmatch
from invoke import task

EXCLUDED_DIR = 'tasks'  # The directory to exclude


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        if EXCLUDED_DIR and EXCLUDED_DIR in dirs:
            dirs.remove(EXCLUDED_DIR)

        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


@task
def concat_python_files(c, directory='.', output_file='concatenated_python_files.txt', pattern='*.py'):
    """
    Concatenate all Python files into a single, human-readable file, excluding the Invoke tasks folder.

    :param pattern: The pattern to match (default: *.py)
    :param directory: where to scan from (default: current directory)
    :param c: Invoke context
    :param output_file: The name of the output file (default: concatenated_python_files.txt)
    """
    with open(output_file, 'w') as outfile:
        for file_path in find_files(directory, pattern):
            with open(file_path, 'r') as infile:
                outfile.write(f'########## {file_path} ##########\n')
                outfile.write(infile.read())
                outfile.write('\n\n')

    print(f'All nested Python files (excluding the Invoke tasks folder) have been concatenated into {output_file}.')


@task
def count_chars(c, file='concatenated_python_files.txt'):
    """
    Count the characters in a file. Defaults to 'concatenated_python_files.txt'.

    :param c: Invoke context
    :param file: The name of the file to count characters (default: concatenated_python_files.txt)
    """
    try:
        with open(file, 'r') as f:
            content = f.read()
            char_count = len(content)
            print(f'The file "{file}" contains {char_count} characters.')
    except FileNotFoundError:
        print(f'Error: The file "{file}" was not found.')
