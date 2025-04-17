# Script to generate AUTO_FILE_STRUCTURE.md and AUTO_BRANCH_README.md
import os

def generate_file_structure(path='src/app', output='AUTO_FILE_STRUCTURE.md'):
    with open(output, 'w') as f:
        for root, dirs, files in os.walk(path):
            level = root.replace(path, '').count(os.sep)
            indent = ' ' * 2 * level
            f.write(f"{indent}- {os.path.basename(root)}/\n")
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                f.write(f"{subindent}- {file}\n")

def generate_branch_readme(branch='main', output='AUTO_BRANCH_README.md'):
    with open(output, 'w') as f:
        f.write(f"# Changes in Branch: `{branch}`\n\n")
        f.write("<!-- Summarise key changes in this branch -->\n")

if __name__ == '__main__':
    generate_file_structure()
    generate_branch_readme()
