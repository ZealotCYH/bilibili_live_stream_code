# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main/bilibili_live_stream_code.py'],
    pathex=[],
    binaries=[],
    datas=[('main/B站图标.ico', '.'), ('main/partition.json', '.'), ('main/使用说明.txt', '.'), ('main/config.ini', '.')],
    hiddenimports=['PIL._tkinter_finder'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='B站推流码获取工具',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['main/B站图标.ico'],
)
app = BUNDLE(
    exe,
    name='B站推流码获取工具.app',
    icon='main/B站图标.ico',
    bundle_identifier=None,
)
