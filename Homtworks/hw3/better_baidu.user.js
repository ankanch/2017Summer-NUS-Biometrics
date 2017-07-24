// ==UserScript==
// @name         better_baidu
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  make baidu more clear to use.
// @author       HcNak
// @match        https://www.baidu.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
    var div_id = "s_mancard_main";
    var div = document.getElementById(div_id);
    div.parentNode.removeChild(div);
    var div2 = document.getElementById("bottom_container");
    div2.parentNode.removeChild(div2);
    document.getElementById("u_sp").innerHTML = "<p style='color:purple;'>Baidu Search Optimized by HcNak.</p>";
    document.getElementById("s_upfunc_menus").innerHTML = "better_baidu v0.1 @Tampermonkey";
    document.getElementById("head").style.minHeight = "500px";
})();