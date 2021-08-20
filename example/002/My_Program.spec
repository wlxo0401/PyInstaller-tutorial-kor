# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [ ("./test.ico", '.'),
                ("./image/*", './image')]
a = Analysis(['My_Program.py'],
            pathex=['C:\\Users\\wlxo0\\Documents\\Python\\PyInstaller\\example\\002'],
            binaries=[],
            datas=added_files,
            hiddenimports=[],
            hookspath=[],
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)
exe = EXE(pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='My_Test_Program',
        debug=True,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=True,
        uac_admin=True,
        icon='./test.ico')
coll = COLLECT(exe,
            a.binaries,
            a.zipfiles,
            a.datas,
            strip=False,
            upx=True,
            upx_exclude=[],
            name='Public_Program')