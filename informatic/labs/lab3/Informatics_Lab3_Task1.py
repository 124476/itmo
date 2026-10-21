# Author = Krahmalnikov Ilya Artemovich
# Group = P3119
# Date = 09.10.2026

import re

def func(text):
    reg = r"<[^<>]*>"
    d = re.findall(reg, text)
    ans = []
    for x in d:
        reg2 = r"(?<=id=[\"'”])[^\"'”]+(?=[\"'”])"
        ans += list(re.findall(reg2, x))
    return "\n".join(ans)

def test_1():
    text = """
<div id="gg1" id=”_next”>
<div class="panel-body">
<div class="panel-body">id="76"</div>
<div id="LEFT_CONTENT" 
class="panelno-border no-padding no-margin">
"""
    expected = "gg1\n_next\nLEFT_CONTENT"
    result = func(text)
    assert result == expected

def test_2():
    text = """
<button id="P1_EDIT_APPS" onclick="javascript:void(0);" class="btn btn-labeled edit-fav-apps btn-xs" type="button">
Настроить
</button>
"""
    expected = "P1_EDIT_APPS"
    result = func(text)
    assert result == expected

def test_3():
    text = """
<div id="root"></div>
"""
    expected = "root"
    result = func(text)
    assert result == expected

def test_4():
    text = """
<link type="text/css" rel="stylesheet" href="https://cdn.itmo.pro/itmoid/style/bg.css">
"""
    expected = ""
    result = func(text)
    assert result == expected

def test_5():
    text = """
<div id="APP_REPORT" class="panel no-border no-padding no-margin no-sticky" >
    <div class="panel-controls panel-padding-h clearfix">
    	<div class="btn-group pull-left panel-controls-left">
    		
    	</div>
    	<div class="btn-group pull-right panel-controls-right">
    		
    	</div>
    </div>
    <!-- /.panel-controls -->
    <div class="panel-body">
        <div id="report_866338507550298249_catch"><span class="nodatafound">Загрузка...</span>
</div>
"""
    expected = "APP_REPORT\nreport_866338507550298249_catch"
    result = func(text)
    assert result == expected


def test_6():
    text = """
.workPos {
    max-height: 55px; /* или нужная вам высота */
    margin-top: 3px;
/*    max-width: 480px;*/
    overflow-y: auto; /* вертикальная прокрутка */
    overflow-x: hidden; /* если не нужна горизонтальная прокрутка */
}

.workPos span {
    display: block;          /* каждый span с новой строки */
    white-space: nowrap;     /* текст не переносится */
    overflow: hidden;        /* скрываем выходящий текст */
    text-overflow: ellipsis; /* добавляем ... при обрезании */
    margin-top: 0px;
    margin-left:0px;
}
"""
    expected = ""
    result = func(text)
    assert result == expected

def test_7():
    text = """
<div id="init-text" class="init-loader"><i class="fa fa-cog fa-spin" style="font-size:12px;"></i> Инициализация ИСУ ...<style> .init-loader {padding:60px 5px 5px 5px;position:fixed;z-index:200000000;color:#1946BA;height:100%;width:100%;background:rgba(255, 255, 255, 0.2);font-size:10px;text-align:center;} body #wwvFlowForm { opacity:0.6; } </style></div>
"""
    expected = "init-text"
    result = func(text)
    assert result == expected

if __name__ == "__main__":
    for test in (test_1, test_2, test_3, test_4, test_5, test_6, test_7):
        try:
            test()
            print(f"{test.__name__}: OK")
        except AssertionError as e:
            print(f"{test.__name__}: FAIL")