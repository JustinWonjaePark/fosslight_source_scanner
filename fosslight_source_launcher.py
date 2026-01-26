# fosslight_source_launcher.py
import sys
import os

# src 폴더를 경로에 추가하여 패키지를 찾을 수 있게 함
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.insert(0, src_path)

from fosslight_source.cli import main

if __name__ == "__main__":
    main()
