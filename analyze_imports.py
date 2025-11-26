import ast
import os
import sys

# Standard library modules (approximate list for filtering)
STD_LIB = {
    'abc', 'argparse', 'ast', 'asyncio', 'base64', 'collections', 'contextlib', 'copy', 'csv', 
    'datetime', 'decimal', 'enum', 'functools', 'glob', 'hashlib', 'importlib', 'inspect', 'io', 
    'itertools', 'json', 'logging', 'math', 'multiprocessing', 'os', 'pathlib', 'pickle', 
    'platform', 'random', 're', 'shutil', 'signal', 'socket', 'sqlite3', 'string', 'subprocess', 
    'sys', 'tempfile', 'threading', 'time', 'traceback', 'typing', 'unittest', 'urllib', 'uuid', 
    'warnings', 'weakref', 'xml', 'zipfile'
}

def get_imports_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            tree = ast.parse(f.read())
        except Exception as e:
            print(f"Error parsing {filepath}: {e}", file=sys.stderr)
            return set()
            
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
    return imports

def main():
    src_dir = r'c:\Users\Fabrice\OneDrive\WSurfWSpaceGlobal\Projects\CoursLinkedin\src'
    all_imports = set()

    if not os.path.exists(src_dir):
        print(f"Directory not found: {src_dir}")
        return

    for filename in os.listdir(src_dir):
        if filename.endswith('.py'):
            filepath = os.path.join(src_dir, filename)
            file_imports = get_imports_from_file(filepath)
            print(f"File: {filename} -> Imports: {file_imports}")
            all_imports.update(file_imports)

    third_party_imports = sorted(list(all_imports - STD_LIB))
    
    print("--- DETECTED IMPORTS ---")
    for imp in third_party_imports:
        print(imp)

if __name__ == "__main__":
    main()
