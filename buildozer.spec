[app]
title = MyApp
package.name = myapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait

[buildozer]

android.api = 33
android.ndk = 25b
android.accept_sdk_license = True
warn_on_root = 0
p4a.branch = master
