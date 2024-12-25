import os
import sys
from datetime import datetime
# python create_project.py your_project_name


def create_project_structure(project_name):
    # 定义项目结构
    structure = {
        'config': {
            'config.yaml': '# Configuration settings\n'
        },
        'logs': {},
        'scripts': {},
        'docs': {
            'api.md': '# API Documentation\n',
            'guide.md': '# User Guide\n'
        },
        'tests': {
            '__init__.py': '',
            'test_main.py': 'def test_sample():\n    assert True'
        },
        project_name: {
            '__init__.py': '',
            'main.py': 'def main():\n    pass\n\nif __name__ == "__main__":\n    main()',
            'core': {
                '__init__.py': ''
            },
            'utils': {
                '__init__.py': ''
            }
        },
        'data': {
            'raw': {},
            'processed': {}
        },
        'web': {
                'public': {'index.html': ''},
                'package.json': '',
                'src': {
                    'compoents': {},
                    'index.js': ''
                    }
            },
        'logs': {},
        'config': {
            'config.yaml': '# Configuration settings\n'
        }
    }
    
    # 创建.gitignore文件内容
    gitignore_content = '''# Python 编译文件 / 优化文件 / DLL 文件
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Python 环境文件
.env
.venv/
env/
venv/
virtualenv/
ENV/

# 日志文件和数据库文件
logs/
*.log
*.db
*.sqlite3

# 数据目录（如果这些文件不是必须提交到版本控制系统）
data/raw/
data/processed/

# 构建输出文件
web/build/
web/node_modules/

# IDE 特定文件
.idea/
.vscode/
*.suo
*.swp
*.DS_Store

# 操作系统生成的文件
.DS_Store
.DS_Store?
ehthumbs.db
Thumbs.db

# Django 特定文件
db.sqlite3
media/
staticfiles/

# Flask 特定文件
instance/
*.ini

# 测试相关文件
.cache/
htmlcov/

# 其他常见文件
*.bak
*.tmp
*.sublime-project
*.sublime-workspace
*.ipynb_checkpoints/

# 项目结构特定的编译缓存文件
maintainhub/__pycache__/
tests/__pycache__/

# 忽略本地配置文件（如开发环境中的配置）
config/config.yaml.local

# 忽略测试数据或临时文件
tests/test_data/
'''
    
    # 创建requirements.txt内容
    requirements_content = '''# Add your project dependencies here
pytest
pyyaml
'''
    
    # 创建README.md内容
    readme_content = f'''# {project_name}

## Description
Add your project description here.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
from {project_name} import main
```

## License
MIT
'''

    # 创建setup.py内容
    setup_content = f'''from setuptools import setup, find_packages

setup(
    name="{project_name}",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
    ],
)

'''

    # 创建 renew_directory.py 内容，注意这里我们不再直接使用 root_dir_name
    renew_content = '''import os
from datetime import datetime

def generate_directory_tree(startpath, output_file, ignore_patterns=None):
    if ignore_patterns is None:
        ignore_patterns = [
            '__pycache__', 
            '.git', 
            '.idea', 
            '.vscode', 
            'venv', 
            'env',
            '.pytest_cache',
            '*.pyc',
            '*.pyo',
            '*.pyd',
            '.DS_Store'
        ]

    def should_ignore(path):
        for pattern in ignore_patterns:
            if pattern.startswith('*'):
                if path.endswith(pattern[1:]):
                    return True
            elif pattern in path:
                return True
        return False

    with open(output_file, 'w', encoding='utf-8') as f:
        # 不再直接使用 root_dir_name 变量，改为获取 startpath 的 basename
        root_dir_name = os.path.basename(os.path.abspath(startpath))
        f.write(f"# Project Directory Structure\\n")
        f.write(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n\\n")
        f.write("```\\n")  # 使用 markdown 代码块格式

        f.write(f"{root_dir_name}/\\n")

        for root, dirs, files in os.walk(startpath):
            # 过滤掉要忽略的目录和文件
            dirs[:] = [d for d in dirs if not should_ignore(d)]
            files = [file for file in files if not should_ignore(file)]

            # 计算当前路径相对于起始路径的层级
            level = root[len(startpath):].count(os.sep)
            indent = '    ' * level

            # 获取当前目录的相对路径
            if root != startpath:
                dir_name = os.path.basename(root)
                f.write(f"{indent}├── {dir_name}/\\n")

            subindent = '    ' * (level + 1)
            # 写入文件
            for file in sorted(files):
                if file != os.path.basename(output_file):  # 不包含输出文件本身
                    f.write(f"{subindent}├── {file}\\n")

        f.write("```\\n\\n")  # 结束 markdown 代码块

        # 添加说明信息
        f.write("## Notes\\n")
        f.write("* This directory tree was automatically generated.\\n")
        f.write("* Ignored patterns: " + ", ".join(ignore_patterns) + "\\n")
        f.write("* Some directories and files are excluded for clarity.\\n")

def main():
    # 当前目录作为起始路径
    start_path = os.getcwd()
    # 输出文件名
    output_file = "DIRECTORY_STRUCTURE.md"
    
    # 自定义要忽略的文件和目录模式
    ignore_patterns = [
        '__pycache__',
        '.git',
        '.idea',
        '.vscode',
        'venv',
        'env',
        '.pytest_cache',
        '*.pyc',
        '*.pyo',
        '*.pyd',
        '.DS_Store',
        '*.egg-info',
        'dist',
        'build',
        'node_modules'
    ]

    try:
        generate_directory_tree(start_path, output_file, ignore_patterns)
        print(f"Directory structure has been written to {output_file}")
        print(f"Location: {os.path.join(start_path, output_file)}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
'''



    def create_structure(base_path, structure):
        for name, contents in structure.items():
            path = os.path.join(base_path, name)
            
            if isinstance(contents, dict):
                os.makedirs(path, exist_ok=True)
                create_structure(path, contents)
            else:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(contents)

    # 创建项目根目录
    os.makedirs(project_name, exist_ok=True)
    
    # 创建项目结构
    create_structure(project_name, structure)
    
    # 创建根目录下的文件
    with open(os.path.join(project_name, '.gitignore'), 'w', encoding='utf-8') as f:
        f.write(gitignore_content)
    
    with open(os.path.join(project_name, 'requirements.txt'), 'w', encoding='utf-8') as f:
        f.write(requirements_content)
    
    with open(os.path.join(project_name, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    with open(os.path.join(project_name, 'setup.py'), 'w', encoding='utf-8') as f:
        f.write(setup_content)
    with open(os.path.join(project_name, 'renew_directory.py'), 'w', encoding='utf-8') as f:
        f.write(renew_content)

    print(f"Project '{project_name}' created successfully!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <project_name>")
        sys.exit(1)
    
    project_name = sys.argv[1]
    create_project_structure(project_name)
