MAKEFLAGS += --warn-undefined-variables

SHELL := bash

.DEFAULT_GOAL := CellProfiler.dmg

.DELETE_ON_ERROR:

.SHELLFLAGS := -eu -o pipefail -c

.SUFFIXES:

identity = "Developer ID Application: Beth Cimini (27YQ9U45D9)"

CellProfiler:
	git clone https://github.com/CellProfiler/CellProfiler.git $@

	cd $@ && git checkout v3.1.9

.PHONY: dependencies
dependencies: CellProfiler
	pip2 install --upgrade cython
	pip2 install numpy==1.15.4

	pip2 install --editable "CellProfiler[build, test]" --upgrade

dist/CellProfiler.app: CellProfiler dependencies Info.plist
	pyinstaller --noconfirm --console CellProfiler.spec

	cp $(word 3, $^) $@/Contents

CellProfiler.dmg:
	hdiutil create                  		\
		-format UDRW                		\
		-fs HFS+                    		\
		-fsargs "-c c=64,a=16,e=16" 		\
		-size 900000k               		\
		-srcfolder dist/CellProfiler.app 	\
		-volname CellProfiler      			\
		CellProfiler.dmg

.PHONY: codesign
codesign:
	#codesign --deep --force --verbose --verify --sign "Developer ID Application: Beth Cimini (27YQ9U45D9)" --entitlements CellProfilerChild.entitlements dist/CellProfiler.app/Contents/MacOS/cp
	codesign -vvv --deep --force --verify --sign "Developer ID Application: Beth Cimini (27YQ9U45D9)" --entitlements CellProfiler.entitlements dist/CellProfiler.app
	#codesign --force --sign "Developer ID Application: Beth Cimini (27YQ9U45D9)" --entitlements CellProfilerParent.entitlements dist/CellProfiler.app

.PHONY: codesign-dmg
codesign-dmg:
	codesign --force --sign "3rd Party Mac Developer Application: Beth Cimini (27YQ9U45D9)" CellProfiler.dmg

.PHONY: productbuild
productbuild:
	productbuild 														     	\
		--component dist/CellProfiler.app /Applications							\
		dist/CellProfiler.pkg

.PHONY: clean
clean:
	if [ -d build ]; then rm -rf build; fi

	if [ -d dist ]; then rm -rf build; fi

	if [ CellProfiler.dmg ]; then rm -rf CellProfiler.dmg; fi
