[app]
title = StableApp
package.name = stableapp
package.domain = org.example

source.dir = .
source.include_exts = py

version = 1.0

requirements = python3,kivy

orientation = portrait

[buildozer]

android.api = 33
android.ndk = 25b
android.accept_sdk_license = True

# 防 root 提示
warn_on_root = 0

# 防止乱升级
p4a.branch = master
