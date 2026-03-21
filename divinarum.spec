# -*- mode: python ; coding: utf-8 -*-

import os
import sys

block_cipher = None
repo_root = SPECPATH
entry_script = os.path.join(repo_root, 'divinarum', 'main.py')

# UPX frequently breaks codesigning on macOS, so it's skipped
use_upx = sys.platform != 'darwin'

a = Analysis(
    [entry_script],
    pathex=[os.path.join(repo_root, 'divinarum')],
    binaries=[],
    datas=[
        (
            os.path.join(repo_root, 'divinarum', 'data', 'texts.json'),
            'divinarum/data'
        ),
        (
            os.path.join(repo_root, 'divinarum', 'txt_files', 'license.txt'),
            'divinarum/txt_files'
        ),
        (
            os.path.join(repo_root, 'divinarum', 'txt_files', 'namegen_sources.txt'),
            'divinarum/txt_files'
        ),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Divinarum',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=use_upx,
    console=True,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=use_upx,
    upx_exclude=[],
    name='Divinarum',
)