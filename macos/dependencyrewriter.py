from __future__ import print_function

import os
import re

from machotools import rewriter_factory


wx_sos = ["dist/CellProfiler.app/Contents/MacOS/wx._animate.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._aui.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._calendar.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._combo.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._controls_.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._core_.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._dataview.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._gdi_.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._gizmos.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._glcanvas.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._grid.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._html.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._html2.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._media.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._misc_.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._propgrid.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._richtext.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._stc.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._webkit.so",
    "dist/CellProfiler.app/Contents/MacOS/wx._windows_.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._wizard.so",
	"dist/CellProfiler.app/Contents/MacOS/wx._xrc.so"]

wx_sos_to_try = ["dist/CellProfiler.app/Contents/MacOS/wx._xrc.so"]

libs_to_replace = {"libwx_osx_cocoau_xrc-3.0.dylib":"libwx_osx_cocoau_xrc-3.0.0.4.0.dylib", 
	"libwx_osx_cocoau_webview-3.0.dylib":"libwx_osx_cocoau_webview-3.0.0.4.0.dylib",
	"libwx_osx_cocoau_html-3.0.dylib":"libwx_osx_cocoau_html-3.0.0.4.0.dylib",
	"libwx_osx_cocoau_qa-3.0.dylib":"libwx_osx_cocoau_qa-3.0.0.4.0.dylib",
	"libwx_osx_cocoau_adv-3.0.dylib":"libwx_osx_cocoau_adv-3.0.0.4.0.dylib",
	"libwx_osx_cocoau_core-3.0.dylib":"libwx_osx_cocoau_core-3.0.0.4.0.dylib",
	"libwx_baseu_xml-3.0.dylib":"libwx_baseu_xml-3.0.0.4.0.dylib",
	"libwx_baseu_net-3.0.dylib":"libwx_baseu_net-3.0.0.4.0.dylib",
	"libwx_baseu-3.0.dylib":"libwx_baseu-3.0.0.4.0.dylib",
	"libwx_osx_cocoau_stc-3.0.dylib":"libwx_osx_cocoau_stc-3.0.0.4.0.dylib",
	"/usr/local/Cellar/wxmac/3.0.4/lib":"@loader_path"}

libs_added = ["dist/CellProfiler.app/Contents/MacOS/libwx_osx_cocoau_xrc-3.0.0.4.0.dylib", 
	"dist/CellProfiler.app/Contents/MacOS/libwx_osx_cocoau_webview-3.0.0.4.0.dylib", 
	"dist/CellProfiler.app/Contents/MacOS/libwx_osx_cocoau_html-3.0.0.4.0.dylib",
	"dist/CellProfiler.app/Contents/MacOS/libwx_osx_cocoau_qa-3.0.0.4.0.dylib",
	"dist/CellProfiler.app/Contents/MacOS/libwx_osx_cocoau_adv-3.0.0.4.0.dylib",
	"dist/CellProfiler.app/Contents/MacOS/libwx_osx_cocoau_core-3.0.0.4.0.dylib",
	"dist/CellProfiler.app/Contents/MacOS/libwx_osx_cocoau_stc-3.0.0.4.0.dylib",
	"dist/CellProfiler.app/Contents/MacOS/libwx_baseu_xml-3.0.0.4.0.dylib",
	"dist/CellProfiler.app/Contents/MacOS/libwx_baseu_net-3.0.0.4.0.dylib",
	"dist/CellProfiler.app/Contents/MacOS/libwx_baseu-3.0.0.4.0.dylib"]

def update_path(libs_to_replace,oldpath):
	for each_replace in libs_to_replace.keys():
		oldpath = re.sub(each_replace, libs_to_replace[each_replace], oldpath)
	return(oldpath)

todo = wx_sos + libs_added

for lib in todo:
	rewriter = rewriter_factory(lib)
	deps = rewriter.dependencies
	#print(lib)
	[rewriter.change_dependency(dep,update_path(libs_to_replace,dep)) for dep in deps if 'wx'in dep]
	#print(rewriter.dependencies)
	rewriter.commit()
	#print(rewriter.dependencies)