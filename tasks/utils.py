import fnmatch
import os

from invoke import task


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


@task
def concat_python_files(c, output_file='concatenated_python_files.txt'):
    """
    Concatenate all Python files into a single, human-readable file.

    :param c: Invoke context
    :param output_file: The name of the output file (default: concatenated_python_files.txt)
    """
    with open(output_file, 'w') as outfile:
        for file_path in find_files('.', '*.py'):
            with open(file_path, 'r') as infile:
                outfile.write(f'########## {file_path} ##########\n')
                outfile.write(infile.read())
                outfile.write('\n\n')

    print(f'All nested Python files have been concatenated into {output_file}.')

    



