# -*- coding: UTF-8 -*-
def custom_proc(request):
    main_link=[
              {'number':"1",'function':"二维码转换",'introductions':"可将文本转换为二维码",'hreflink':"qrcode_transform.html"},
              {'number':"2",'function':"json格式化",'introductions':"把json串变得更容易阅读",'hreflink':"json_formatting.html"},
              {'number':"3",'function':"宜定盈参数加密",'introductions':"宜定盈参数加密（by  耿猛）",'hreflink':"http://10.106.4.17:8080/yrdGZ/encrypt.jsp"},
              {'number':"4",'function':"http状态查询",'introductions':"Http状态查询工具说明，方便查阅一些常用的http返回码",'hreflink':"http_state.html"},
              {'number':"5",'function':"清除宜人贷注册信息",'introductions':"清除宜人贷注册信息，清除后可重新注册",'hreflink':"log_out.html"},
              {'number':"6",'function':"恢复一元鉴权",'introductions':"恢复某张银行卡的一元鉴权",'hreflink':"one_authentication.html"},
                   ]
    return { 'main_link' :  main_link }    