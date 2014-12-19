



<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" >
 
 <meta name="ROBOTS" content="NOARCHIVE">
 
 <link rel="icon" type="image/vnd.microsoft.icon" href="http://www.gstatic.com/codesite/ph/images/phosting.ico">
 
 
 <script type="text/javascript">
 
 
 
 
 var codesite_token = null;
 
 
 var CS_env = {"loggedInUserEmail": null, "relativeBaseUrl": "", "assetHostPath": "http://www.gstatic.com/codesite/ph", "domainName": null, "profileUrl": null, "assetVersionPath": "http://www.gstatic.com/codesite/ph/10868592318973270098", "projectHomeUrl": "/p/windows-privesc-check", "token": null, "projectName": "windows-privesc-check"};
 var _gaq = _gaq || [];
 _gaq.push(
 ['siteTracker._setAccount', 'UA-18071-1'],
 ['siteTracker._trackPageview']);
 
 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
 })();
 
 </script>
 
 
 <title>windows-privesc-check.py - 
 windows-privesc-check -
 
 
 Standalone Executable to check for simple privilege escalation vectors on Windows systems - Google Project Hosting
 </title>
 <link type="text/css" rel="stylesheet" href="http://www.gstatic.com/codesite/ph/10868592318973270098/css/core.css">
 
 <link type="text/css" rel="stylesheet" href="http://www.gstatic.com/codesite/ph/10868592318973270098/css/ph_detail.css" >
 
 
 <link type="text/css" rel="stylesheet" href="http://www.gstatic.com/codesite/ph/10868592318973270098/css/d_sb.css" >
 
 
 
<!--[if IE]>
 <link type="text/css" rel="stylesheet" href="http://www.gstatic.com/codesite/ph/10868592318973270098/css/d_ie.css" >
<![endif]-->
 <style type="text/css">
 .menuIcon.off { background: no-repeat url(http://www.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -42px }
 .menuIcon.on { background: no-repeat url(http://www.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -28px }
 .menuIcon.down { background: no-repeat url(http://www.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 0; }
 
 
 
  tr.inline_comment {
 background: #fff;
 vertical-align: top;
 }
 div.draft, div.published {
 padding: .3em;
 border: 1px solid #999; 
 margin-bottom: .1em;
 font-family: arial, sans-serif;
 max-width: 60em;
 }
 div.draft {
 background: #ffa;
 } 
 div.published {
 background: #e5ecf9;
 }
 div.published .body, div.draft .body {
 padding: .5em .1em .1em .1em;
 max-width: 60em;
 white-space: pre-wrap;
 white-space: -moz-pre-wrap;
 white-space: -pre-wrap;
 white-space: -o-pre-wrap;
 word-wrap: break-word;
 font-size: 1em;
 }
 div.draft .actions {
 margin-left: 1em;
 font-size: 90%;
 }
 div.draft form {
 padding: .5em .5em .5em 0;
 }
 div.draft textarea, div.published textarea {
 width: 95%;
 height: 10em;
 font-family: arial, sans-serif;
 margin-bottom: .5em;
 }

 
 .nocursor, .nocursor td, .cursor_hidden, .cursor_hidden td {
 background-color: white;
 height: 2px;
 }
 .cursor, .cursor td {
 background-color: darkblue;
 height: 2px;
 display: '';
 }
 
 
.list {
 border: 1px solid white;
 border-bottom: 0;
}

 
 </style>
</head>
<body class="t4">
<script type="text/javascript">
 window.___gcfg = {lang: 'en'};
 (function() 
 {var po = document.createElement("script");
 po.type = "text/javascript"; po.async = true;po.src = "https://apis.google.com/js/plusone.js";
 var s = document.getElementsByTagName("script")[0];
 s.parentNode.insertBefore(po, s);
 })();
</script>
<div class="headbg">

 <div id="gaia">
 

 <span>
 
 
 <a href="#" id="projects-dropdown" onclick="return false;"><u>My favorites</u> <small>&#9660;</small></a>
 | <a href="https://www.google.com/accounts/ServiceLogin?service=code&amp;ltmpl=phosting&amp;continue=http%3A%2F%2Fcode.google.com%2Fp%2Fwindows-privesc-check%2Fsource%2Fbrowse%2Ftrunk%2Fwindows-privesc-check.py&amp;followup=http%3A%2F%2Fcode.google.com%2Fp%2Fwindows-privesc-check%2Fsource%2Fbrowse%2Ftrunk%2Fwindows-privesc-check.py" onclick="_CS_click('/gb/ph/signin');"><u>Sign in</u></a>
 
 </span>

 </div>

 <div class="gbh" style="left: 0pt;"></div>
 <div class="gbh" style="right: 0pt;"></div>
 
 
 <div style="height: 1px"></div>
<!--[if lte IE 7]>
<div style="text-align:center;">
Your version of Internet Explorer is not supported. Try a browser that
contributes to open source, such as <a href="http://www.firefox.com">Firefox</a>,
<a href="http://www.google.com/chrome">Google Chrome</a>, or
<a href="http://code.google.com/chrome/chromeframe/">Google Chrome Frame</a>.
</div>
<![endif]-->



 <table style="padding:0px; margin: 0px 0px 10px 0px; width:100%" cellpadding="0" cellspacing="0"
 itemscope itemtype="http://schema.org/CreativeWork">
 <tr style="height: 58px;">
 
 
 
 <td id="plogo">
 <link itemprop="url" href="/p/windows-privesc-check">
 <a href="/p/windows-privesc-check/">
 
 <img src="http://www.gstatic.com/codesite/ph/images/defaultlogo.png" alt="Logo" itemprop="image">
 
 </a>
 </td>
 
 <td style="padding-left: 0.5em">
 
 <div id="pname">
 <a href="/p/windows-privesc-check/"><span itemprop="name">windows-privesc-check</span></a>
 </div>
 
 <div id="psum">
 <a id="project_summary_link"
 href="/p/windows-privesc-check/"><span itemprop="description">Standalone Executable to check for simple privilege escalation vectors on Windows systems</span></a>
 
 </div>
 
 
 </td>
 <td style="white-space:nowrap;text-align:right; vertical-align:bottom;">
 
 <form action="/hosting/search">
 <input size="30" name="q" value="" type="text">
 
 <input type="submit" name="projectsearch" value="Search projects" >
 </form>
 
 </tr>
 </table>

</div>

 
<div id="mt" class="gtb"> 
 <a href="/p/windows-privesc-check/" class="tab ">Project&nbsp;Home</a>
 
 
 
 
 
 
 <a href="/p/windows-privesc-check/w/list" class="tab ">Wiki</a>
 
 
 
 
 
 <a href="/p/windows-privesc-check/issues/list"
 class="tab ">Issues</a>
 
 
 
 
 
 <a href="/p/windows-privesc-check/source/checkout"
 class="tab active">Source</a>
 
 
 
 
 
 
 
 
 <div class=gtbc></div>
</div>
<table cellspacing="0" cellpadding="0" width="100%" align="center" border="0" class="st">
 <tr>
 
 
 
 
 
 
 <td class="subt">
 <div class="st2">
 <div class="isf">
 
 


 <span class="inst1"><a href="/p/windows-privesc-check/source/checkout">Checkout</a></span> &nbsp;
 <span class="inst2"><a href="/p/windows-privesc-check/source/browse/">Browse</a></span> &nbsp;
 <span class="inst3"><a href="/p/windows-privesc-check/source/list">Changes</a></span> &nbsp;
 
 
 
 
 
 
 
 </form>
 <script type="text/javascript">
 
 function codesearchQuery(form) {
 var query = document.getElementById('q').value;
 if (query) { form.action += '%20' + query; }
 }
 </script>
 </div>
</div>

 </td>
 
 
 
 <td align="right" valign="top" class="bevel-right"></td>
 </tr>
</table>


<script type="text/javascript">
 var cancelBubble = false;
 function _go(url) { document.location = url; }
</script>
<div id="maincol"
 
>

 




<div class="expand">
<div id="colcontrol">
<style type="text/css">
 #file_flipper { white-space: nowrap; padding-right: 2em; }
 #file_flipper.hidden { display: none; }
 #file_flipper .pagelink { color: #0000CC; text-decoration: underline; }
 #file_flipper #visiblefiles { padding-left: 0.5em; padding-right: 0.5em; }
</style>
<table id="nav_and_rev" class="list"
 cellpadding="0" cellspacing="0" width="100%">
 <tr>
 
 <td nowrap="nowrap" class="src_crumbs src_nav" width="33%">
 <strong class="src_nav">Source path:&nbsp;</strong>
 <span id="crumb_root">
 
 <a href="/p/windows-privesc-check/source/browse/">svn</a>/&nbsp;</span>
 <span id="crumb_links" class="ifClosed"><a href="/p/windows-privesc-check/source/browse/trunk/">trunk</a><span class="sp">/&nbsp;</span>windows-privesc-check.py</span>
 
 


 </td>
 
 
 <td nowrap="nowrap" width="33%" align="right">
 <table cellpadding="0" cellspacing="0" style="font-size: 100%"><tr>
 
 
 <td class="flipper">
 <ul class="leftside">
 
 <li><a href="/p/windows-privesc-check/source/browse/trunk/windows-privesc-check.py?r=23" title="Previous">&lsaquo;r23</a></li>
 
 </ul>
 </td>
 
 <td class="flipper"><b>r139</b></td>
 
 </tr></table>
 </td> 
 </tr>
</table>

<div class="fc">
 
 
 
<style type="text/css">
.undermouse span {
 background-image: url(http://www.gstatic.com/codesite/ph/images/comments.gif); }
</style>
<table class="opened" id="review_comment_area"
><tr>
<td id="nums">
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
<pre><table width="100%" id="nums_table_0"><tr id="gr_svn139_1"

><td id="1"><a href="#1">1</a></td></tr
><tr id="gr_svn139_2"

><td id="2"><a href="#2">2</a></td></tr
><tr id="gr_svn139_3"

><td id="3"><a href="#3">3</a></td></tr
><tr id="gr_svn139_4"

><td id="4"><a href="#4">4</a></td></tr
><tr id="gr_svn139_5"

><td id="5"><a href="#5">5</a></td></tr
><tr id="gr_svn139_6"

><td id="6"><a href="#6">6</a></td></tr
><tr id="gr_svn139_7"

><td id="7"><a href="#7">7</a></td></tr
><tr id="gr_svn139_8"

><td id="8"><a href="#8">8</a></td></tr
><tr id="gr_svn139_9"

><td id="9"><a href="#9">9</a></td></tr
><tr id="gr_svn139_10"

><td id="10"><a href="#10">10</a></td></tr
><tr id="gr_svn139_11"

><td id="11"><a href="#11">11</a></td></tr
><tr id="gr_svn139_12"

><td id="12"><a href="#12">12</a></td></tr
><tr id="gr_svn139_13"

><td id="13"><a href="#13">13</a></td></tr
><tr id="gr_svn139_14"

><td id="14"><a href="#14">14</a></td></tr
><tr id="gr_svn139_15"

><td id="15"><a href="#15">15</a></td></tr
><tr id="gr_svn139_16"

><td id="16"><a href="#16">16</a></td></tr
><tr id="gr_svn139_17"

><td id="17"><a href="#17">17</a></td></tr
><tr id="gr_svn139_18"

><td id="18"><a href="#18">18</a></td></tr
><tr id="gr_svn139_19"

><td id="19"><a href="#19">19</a></td></tr
><tr id="gr_svn139_20"

><td id="20"><a href="#20">20</a></td></tr
><tr id="gr_svn139_21"

><td id="21"><a href="#21">21</a></td></tr
><tr id="gr_svn139_22"

><td id="22"><a href="#22">22</a></td></tr
><tr id="gr_svn139_23"

><td id="23"><a href="#23">23</a></td></tr
><tr id="gr_svn139_24"

><td id="24"><a href="#24">24</a></td></tr
><tr id="gr_svn139_25"

><td id="25"><a href="#25">25</a></td></tr
><tr id="gr_svn139_26"

><td id="26"><a href="#26">26</a></td></tr
><tr id="gr_svn139_27"

><td id="27"><a href="#27">27</a></td></tr
><tr id="gr_svn139_28"

><td id="28"><a href="#28">28</a></td></tr
><tr id="gr_svn139_29"

><td id="29"><a href="#29">29</a></td></tr
><tr id="gr_svn139_30"

><td id="30"><a href="#30">30</a></td></tr
><tr id="gr_svn139_31"

><td id="31"><a href="#31">31</a></td></tr
><tr id="gr_svn139_32"

><td id="32"><a href="#32">32</a></td></tr
><tr id="gr_svn139_33"

><td id="33"><a href="#33">33</a></td></tr
><tr id="gr_svn139_34"

><td id="34"><a href="#34">34</a></td></tr
><tr id="gr_svn139_35"

><td id="35"><a href="#35">35</a></td></tr
><tr id="gr_svn139_36"

><td id="36"><a href="#36">36</a></td></tr
><tr id="gr_svn139_37"

><td id="37"><a href="#37">37</a></td></tr
><tr id="gr_svn139_38"

><td id="38"><a href="#38">38</a></td></tr
><tr id="gr_svn139_39"

><td id="39"><a href="#39">39</a></td></tr
><tr id="gr_svn139_40"

><td id="40"><a href="#40">40</a></td></tr
><tr id="gr_svn139_41"

><td id="41"><a href="#41">41</a></td></tr
><tr id="gr_svn139_42"

><td id="42"><a href="#42">42</a></td></tr
><tr id="gr_svn139_43"

><td id="43"><a href="#43">43</a></td></tr
><tr id="gr_svn139_44"

><td id="44"><a href="#44">44</a></td></tr
><tr id="gr_svn139_45"

><td id="45"><a href="#45">45</a></td></tr
><tr id="gr_svn139_46"

><td id="46"><a href="#46">46</a></td></tr
><tr id="gr_svn139_47"

><td id="47"><a href="#47">47</a></td></tr
><tr id="gr_svn139_48"

><td id="48"><a href="#48">48</a></td></tr
><tr id="gr_svn139_49"

><td id="49"><a href="#49">49</a></td></tr
><tr id="gr_svn139_50"

><td id="50"><a href="#50">50</a></td></tr
><tr id="gr_svn139_51"

><td id="51"><a href="#51">51</a></td></tr
><tr id="gr_svn139_52"

><td id="52"><a href="#52">52</a></td></tr
><tr id="gr_svn139_53"

><td id="53"><a href="#53">53</a></td></tr
><tr id="gr_svn139_54"

><td id="54"><a href="#54">54</a></td></tr
><tr id="gr_svn139_55"

><td id="55"><a href="#55">55</a></td></tr
><tr id="gr_svn139_56"

><td id="56"><a href="#56">56</a></td></tr
><tr id="gr_svn139_57"

><td id="57"><a href="#57">57</a></td></tr
><tr id="gr_svn139_58"

><td id="58"><a href="#58">58</a></td></tr
><tr id="gr_svn139_59"

><td id="59"><a href="#59">59</a></td></tr
><tr id="gr_svn139_60"

><td id="60"><a href="#60">60</a></td></tr
><tr id="gr_svn139_61"

><td id="61"><a href="#61">61</a></td></tr
><tr id="gr_svn139_62"

><td id="62"><a href="#62">62</a></td></tr
><tr id="gr_svn139_63"

><td id="63"><a href="#63">63</a></td></tr
><tr id="gr_svn139_64"

><td id="64"><a href="#64">64</a></td></tr
><tr id="gr_svn139_65"

><td id="65"><a href="#65">65</a></td></tr
><tr id="gr_svn139_66"

><td id="66"><a href="#66">66</a></td></tr
><tr id="gr_svn139_67"

><td id="67"><a href="#67">67</a></td></tr
><tr id="gr_svn139_68"

><td id="68"><a href="#68">68</a></td></tr
><tr id="gr_svn139_69"

><td id="69"><a href="#69">69</a></td></tr
><tr id="gr_svn139_70"

><td id="70"><a href="#70">70</a></td></tr
><tr id="gr_svn139_71"

><td id="71"><a href="#71">71</a></td></tr
><tr id="gr_svn139_72"

><td id="72"><a href="#72">72</a></td></tr
><tr id="gr_svn139_73"

><td id="73"><a href="#73">73</a></td></tr
><tr id="gr_svn139_74"

><td id="74"><a href="#74">74</a></td></tr
><tr id="gr_svn139_75"

><td id="75"><a href="#75">75</a></td></tr
><tr id="gr_svn139_76"

><td id="76"><a href="#76">76</a></td></tr
><tr id="gr_svn139_77"

><td id="77"><a href="#77">77</a></td></tr
><tr id="gr_svn139_78"

><td id="78"><a href="#78">78</a></td></tr
><tr id="gr_svn139_79"

><td id="79"><a href="#79">79</a></td></tr
><tr id="gr_svn139_80"

><td id="80"><a href="#80">80</a></td></tr
><tr id="gr_svn139_81"

><td id="81"><a href="#81">81</a></td></tr
><tr id="gr_svn139_82"

><td id="82"><a href="#82">82</a></td></tr
><tr id="gr_svn139_83"

><td id="83"><a href="#83">83</a></td></tr
><tr id="gr_svn139_84"

><td id="84"><a href="#84">84</a></td></tr
><tr id="gr_svn139_85"

><td id="85"><a href="#85">85</a></td></tr
><tr id="gr_svn139_86"

><td id="86"><a href="#86">86</a></td></tr
><tr id="gr_svn139_87"

><td id="87"><a href="#87">87</a></td></tr
><tr id="gr_svn139_88"

><td id="88"><a href="#88">88</a></td></tr
><tr id="gr_svn139_89"

><td id="89"><a href="#89">89</a></td></tr
><tr id="gr_svn139_90"

><td id="90"><a href="#90">90</a></td></tr
><tr id="gr_svn139_91"

><td id="91"><a href="#91">91</a></td></tr
><tr id="gr_svn139_92"

><td id="92"><a href="#92">92</a></td></tr
><tr id="gr_svn139_93"

><td id="93"><a href="#93">93</a></td></tr
><tr id="gr_svn139_94"

><td id="94"><a href="#94">94</a></td></tr
><tr id="gr_svn139_95"

><td id="95"><a href="#95">95</a></td></tr
><tr id="gr_svn139_96"

><td id="96"><a href="#96">96</a></td></tr
><tr id="gr_svn139_97"

><td id="97"><a href="#97">97</a></td></tr
><tr id="gr_svn139_98"

><td id="98"><a href="#98">98</a></td></tr
><tr id="gr_svn139_99"

><td id="99"><a href="#99">99</a></td></tr
><tr id="gr_svn139_100"

><td id="100"><a href="#100">100</a></td></tr
><tr id="gr_svn139_101"

><td id="101"><a href="#101">101</a></td></tr
><tr id="gr_svn139_102"

><td id="102"><a href="#102">102</a></td></tr
><tr id="gr_svn139_103"

><td id="103"><a href="#103">103</a></td></tr
><tr id="gr_svn139_104"

><td id="104"><a href="#104">104</a></td></tr
><tr id="gr_svn139_105"

><td id="105"><a href="#105">105</a></td></tr
><tr id="gr_svn139_106"

><td id="106"><a href="#106">106</a></td></tr
><tr id="gr_svn139_107"

><td id="107"><a href="#107">107</a></td></tr
><tr id="gr_svn139_108"

><td id="108"><a href="#108">108</a></td></tr
><tr id="gr_svn139_109"

><td id="109"><a href="#109">109</a></td></tr
><tr id="gr_svn139_110"

><td id="110"><a href="#110">110</a></td></tr
><tr id="gr_svn139_111"

><td id="111"><a href="#111">111</a></td></tr
><tr id="gr_svn139_112"

><td id="112"><a href="#112">112</a></td></tr
><tr id="gr_svn139_113"

><td id="113"><a href="#113">113</a></td></tr
><tr id="gr_svn139_114"

><td id="114"><a href="#114">114</a></td></tr
><tr id="gr_svn139_115"

><td id="115"><a href="#115">115</a></td></tr
><tr id="gr_svn139_116"

><td id="116"><a href="#116">116</a></td></tr
><tr id="gr_svn139_117"

><td id="117"><a href="#117">117</a></td></tr
><tr id="gr_svn139_118"

><td id="118"><a href="#118">118</a></td></tr
><tr id="gr_svn139_119"

><td id="119"><a href="#119">119</a></td></tr
><tr id="gr_svn139_120"

><td id="120"><a href="#120">120</a></td></tr
><tr id="gr_svn139_121"

><td id="121"><a href="#121">121</a></td></tr
><tr id="gr_svn139_122"

><td id="122"><a href="#122">122</a></td></tr
><tr id="gr_svn139_123"

><td id="123"><a href="#123">123</a></td></tr
><tr id="gr_svn139_124"

><td id="124"><a href="#124">124</a></td></tr
><tr id="gr_svn139_125"

><td id="125"><a href="#125">125</a></td></tr
><tr id="gr_svn139_126"

><td id="126"><a href="#126">126</a></td></tr
><tr id="gr_svn139_127"

><td id="127"><a href="#127">127</a></td></tr
><tr id="gr_svn139_128"

><td id="128"><a href="#128">128</a></td></tr
><tr id="gr_svn139_129"

><td id="129"><a href="#129">129</a></td></tr
><tr id="gr_svn139_130"

><td id="130"><a href="#130">130</a></td></tr
><tr id="gr_svn139_131"

><td id="131"><a href="#131">131</a></td></tr
><tr id="gr_svn139_132"

><td id="132"><a href="#132">132</a></td></tr
><tr id="gr_svn139_133"

><td id="133"><a href="#133">133</a></td></tr
><tr id="gr_svn139_134"

><td id="134"><a href="#134">134</a></td></tr
><tr id="gr_svn139_135"

><td id="135"><a href="#135">135</a></td></tr
><tr id="gr_svn139_136"

><td id="136"><a href="#136">136</a></td></tr
><tr id="gr_svn139_137"

><td id="137"><a href="#137">137</a></td></tr
><tr id="gr_svn139_138"

><td id="138"><a href="#138">138</a></td></tr
><tr id="gr_svn139_139"

><td id="139"><a href="#139">139</a></td></tr
><tr id="gr_svn139_140"

><td id="140"><a href="#140">140</a></td></tr
><tr id="gr_svn139_141"

><td id="141"><a href="#141">141</a></td></tr
><tr id="gr_svn139_142"

><td id="142"><a href="#142">142</a></td></tr
><tr id="gr_svn139_143"

><td id="143"><a href="#143">143</a></td></tr
><tr id="gr_svn139_144"

><td id="144"><a href="#144">144</a></td></tr
><tr id="gr_svn139_145"

><td id="145"><a href="#145">145</a></td></tr
><tr id="gr_svn139_146"

><td id="146"><a href="#146">146</a></td></tr
><tr id="gr_svn139_147"

><td id="147"><a href="#147">147</a></td></tr
><tr id="gr_svn139_148"

><td id="148"><a href="#148">148</a></td></tr
><tr id="gr_svn139_149"

><td id="149"><a href="#149">149</a></td></tr
><tr id="gr_svn139_150"

><td id="150"><a href="#150">150</a></td></tr
><tr id="gr_svn139_151"

><td id="151"><a href="#151">151</a></td></tr
><tr id="gr_svn139_152"

><td id="152"><a href="#152">152</a></td></tr
><tr id="gr_svn139_153"

><td id="153"><a href="#153">153</a></td></tr
><tr id="gr_svn139_154"

><td id="154"><a href="#154">154</a></td></tr
><tr id="gr_svn139_155"

><td id="155"><a href="#155">155</a></td></tr
><tr id="gr_svn139_156"

><td id="156"><a href="#156">156</a></td></tr
><tr id="gr_svn139_157"

><td id="157"><a href="#157">157</a></td></tr
><tr id="gr_svn139_158"

><td id="158"><a href="#158">158</a></td></tr
><tr id="gr_svn139_159"

><td id="159"><a href="#159">159</a></td></tr
><tr id="gr_svn139_160"

><td id="160"><a href="#160">160</a></td></tr
><tr id="gr_svn139_161"

><td id="161"><a href="#161">161</a></td></tr
><tr id="gr_svn139_162"

><td id="162"><a href="#162">162</a></td></tr
><tr id="gr_svn139_163"

><td id="163"><a href="#163">163</a></td></tr
><tr id="gr_svn139_164"

><td id="164"><a href="#164">164</a></td></tr
><tr id="gr_svn139_165"

><td id="165"><a href="#165">165</a></td></tr
><tr id="gr_svn139_166"

><td id="166"><a href="#166">166</a></td></tr
><tr id="gr_svn139_167"

><td id="167"><a href="#167">167</a></td></tr
><tr id="gr_svn139_168"

><td id="168"><a href="#168">168</a></td></tr
><tr id="gr_svn139_169"

><td id="169"><a href="#169">169</a></td></tr
><tr id="gr_svn139_170"

><td id="170"><a href="#170">170</a></td></tr
><tr id="gr_svn139_171"

><td id="171"><a href="#171">171</a></td></tr
><tr id="gr_svn139_172"

><td id="172"><a href="#172">172</a></td></tr
><tr id="gr_svn139_173"

><td id="173"><a href="#173">173</a></td></tr
><tr id="gr_svn139_174"

><td id="174"><a href="#174">174</a></td></tr
><tr id="gr_svn139_175"

><td id="175"><a href="#175">175</a></td></tr
><tr id="gr_svn139_176"

><td id="176"><a href="#176">176</a></td></tr
><tr id="gr_svn139_177"

><td id="177"><a href="#177">177</a></td></tr
><tr id="gr_svn139_178"

><td id="178"><a href="#178">178</a></td></tr
><tr id="gr_svn139_179"

><td id="179"><a href="#179">179</a></td></tr
><tr id="gr_svn139_180"

><td id="180"><a href="#180">180</a></td></tr
><tr id="gr_svn139_181"

><td id="181"><a href="#181">181</a></td></tr
><tr id="gr_svn139_182"

><td id="182"><a href="#182">182</a></td></tr
><tr id="gr_svn139_183"

><td id="183"><a href="#183">183</a></td></tr
><tr id="gr_svn139_184"

><td id="184"><a href="#184">184</a></td></tr
><tr id="gr_svn139_185"

><td id="185"><a href="#185">185</a></td></tr
><tr id="gr_svn139_186"

><td id="186"><a href="#186">186</a></td></tr
><tr id="gr_svn139_187"

><td id="187"><a href="#187">187</a></td></tr
><tr id="gr_svn139_188"

><td id="188"><a href="#188">188</a></td></tr
><tr id="gr_svn139_189"

><td id="189"><a href="#189">189</a></td></tr
><tr id="gr_svn139_190"

><td id="190"><a href="#190">190</a></td></tr
><tr id="gr_svn139_191"

><td id="191"><a href="#191">191</a></td></tr
><tr id="gr_svn139_192"

><td id="192"><a href="#192">192</a></td></tr
><tr id="gr_svn139_193"

><td id="193"><a href="#193">193</a></td></tr
><tr id="gr_svn139_194"

><td id="194"><a href="#194">194</a></td></tr
><tr id="gr_svn139_195"

><td id="195"><a href="#195">195</a></td></tr
><tr id="gr_svn139_196"

><td id="196"><a href="#196">196</a></td></tr
><tr id="gr_svn139_197"

><td id="197"><a href="#197">197</a></td></tr
><tr id="gr_svn139_198"

><td id="198"><a href="#198">198</a></td></tr
><tr id="gr_svn139_199"

><td id="199"><a href="#199">199</a></td></tr
><tr id="gr_svn139_200"

><td id="200"><a href="#200">200</a></td></tr
><tr id="gr_svn139_201"

><td id="201"><a href="#201">201</a></td></tr
><tr id="gr_svn139_202"

><td id="202"><a href="#202">202</a></td></tr
><tr id="gr_svn139_203"

><td id="203"><a href="#203">203</a></td></tr
><tr id="gr_svn139_204"

><td id="204"><a href="#204">204</a></td></tr
><tr id="gr_svn139_205"

><td id="205"><a href="#205">205</a></td></tr
><tr id="gr_svn139_206"

><td id="206"><a href="#206">206</a></td></tr
><tr id="gr_svn139_207"

><td id="207"><a href="#207">207</a></td></tr
><tr id="gr_svn139_208"

><td id="208"><a href="#208">208</a></td></tr
><tr id="gr_svn139_209"

><td id="209"><a href="#209">209</a></td></tr
><tr id="gr_svn139_210"

><td id="210"><a href="#210">210</a></td></tr
><tr id="gr_svn139_211"

><td id="211"><a href="#211">211</a></td></tr
><tr id="gr_svn139_212"

><td id="212"><a href="#212">212</a></td></tr
><tr id="gr_svn139_213"

><td id="213"><a href="#213">213</a></td></tr
><tr id="gr_svn139_214"

><td id="214"><a href="#214">214</a></td></tr
><tr id="gr_svn139_215"

><td id="215"><a href="#215">215</a></td></tr
><tr id="gr_svn139_216"

><td id="216"><a href="#216">216</a></td></tr
><tr id="gr_svn139_217"

><td id="217"><a href="#217">217</a></td></tr
><tr id="gr_svn139_218"

><td id="218"><a href="#218">218</a></td></tr
><tr id="gr_svn139_219"

><td id="219"><a href="#219">219</a></td></tr
><tr id="gr_svn139_220"

><td id="220"><a href="#220">220</a></td></tr
><tr id="gr_svn139_221"

><td id="221"><a href="#221">221</a></td></tr
><tr id="gr_svn139_222"

><td id="222"><a href="#222">222</a></td></tr
><tr id="gr_svn139_223"

><td id="223"><a href="#223">223</a></td></tr
><tr id="gr_svn139_224"

><td id="224"><a href="#224">224</a></td></tr
><tr id="gr_svn139_225"

><td id="225"><a href="#225">225</a></td></tr
><tr id="gr_svn139_226"

><td id="226"><a href="#226">226</a></td></tr
><tr id="gr_svn139_227"

><td id="227"><a href="#227">227</a></td></tr
><tr id="gr_svn139_228"

><td id="228"><a href="#228">228</a></td></tr
><tr id="gr_svn139_229"

><td id="229"><a href="#229">229</a></td></tr
><tr id="gr_svn139_230"

><td id="230"><a href="#230">230</a></td></tr
><tr id="gr_svn139_231"

><td id="231"><a href="#231">231</a></td></tr
><tr id="gr_svn139_232"

><td id="232"><a href="#232">232</a></td></tr
><tr id="gr_svn139_233"

><td id="233"><a href="#233">233</a></td></tr
><tr id="gr_svn139_234"

><td id="234"><a href="#234">234</a></td></tr
><tr id="gr_svn139_235"

><td id="235"><a href="#235">235</a></td></tr
><tr id="gr_svn139_236"

><td id="236"><a href="#236">236</a></td></tr
><tr id="gr_svn139_237"

><td id="237"><a href="#237">237</a></td></tr
><tr id="gr_svn139_238"

><td id="238"><a href="#238">238</a></td></tr
><tr id="gr_svn139_239"

><td id="239"><a href="#239">239</a></td></tr
><tr id="gr_svn139_240"

><td id="240"><a href="#240">240</a></td></tr
><tr id="gr_svn139_241"

><td id="241"><a href="#241">241</a></td></tr
><tr id="gr_svn139_242"

><td id="242"><a href="#242">242</a></td></tr
><tr id="gr_svn139_243"

><td id="243"><a href="#243">243</a></td></tr
><tr id="gr_svn139_244"

><td id="244"><a href="#244">244</a></td></tr
><tr id="gr_svn139_245"

><td id="245"><a href="#245">245</a></td></tr
><tr id="gr_svn139_246"

><td id="246"><a href="#246">246</a></td></tr
><tr id="gr_svn139_247"

><td id="247"><a href="#247">247</a></td></tr
><tr id="gr_svn139_248"

><td id="248"><a href="#248">248</a></td></tr
><tr id="gr_svn139_249"

><td id="249"><a href="#249">249</a></td></tr
><tr id="gr_svn139_250"

><td id="250"><a href="#250">250</a></td></tr
><tr id="gr_svn139_251"

><td id="251"><a href="#251">251</a></td></tr
><tr id="gr_svn139_252"

><td id="252"><a href="#252">252</a></td></tr
><tr id="gr_svn139_253"

><td id="253"><a href="#253">253</a></td></tr
><tr id="gr_svn139_254"

><td id="254"><a href="#254">254</a></td></tr
><tr id="gr_svn139_255"

><td id="255"><a href="#255">255</a></td></tr
><tr id="gr_svn139_256"

><td id="256"><a href="#256">256</a></td></tr
><tr id="gr_svn139_257"

><td id="257"><a href="#257">257</a></td></tr
><tr id="gr_svn139_258"

><td id="258"><a href="#258">258</a></td></tr
><tr id="gr_svn139_259"

><td id="259"><a href="#259">259</a></td></tr
><tr id="gr_svn139_260"

><td id="260"><a href="#260">260</a></td></tr
><tr id="gr_svn139_261"

><td id="261"><a href="#261">261</a></td></tr
><tr id="gr_svn139_262"

><td id="262"><a href="#262">262</a></td></tr
><tr id="gr_svn139_263"

><td id="263"><a href="#263">263</a></td></tr
><tr id="gr_svn139_264"

><td id="264"><a href="#264">264</a></td></tr
><tr id="gr_svn139_265"

><td id="265"><a href="#265">265</a></td></tr
><tr id="gr_svn139_266"

><td id="266"><a href="#266">266</a></td></tr
><tr id="gr_svn139_267"

><td id="267"><a href="#267">267</a></td></tr
><tr id="gr_svn139_268"

><td id="268"><a href="#268">268</a></td></tr
><tr id="gr_svn139_269"

><td id="269"><a href="#269">269</a></td></tr
><tr id="gr_svn139_270"

><td id="270"><a href="#270">270</a></td></tr
><tr id="gr_svn139_271"

><td id="271"><a href="#271">271</a></td></tr
><tr id="gr_svn139_272"

><td id="272"><a href="#272">272</a></td></tr
><tr id="gr_svn139_273"

><td id="273"><a href="#273">273</a></td></tr
><tr id="gr_svn139_274"

><td id="274"><a href="#274">274</a></td></tr
><tr id="gr_svn139_275"

><td id="275"><a href="#275">275</a></td></tr
><tr id="gr_svn139_276"

><td id="276"><a href="#276">276</a></td></tr
><tr id="gr_svn139_277"

><td id="277"><a href="#277">277</a></td></tr
><tr id="gr_svn139_278"

><td id="278"><a href="#278">278</a></td></tr
><tr id="gr_svn139_279"

><td id="279"><a href="#279">279</a></td></tr
><tr id="gr_svn139_280"

><td id="280"><a href="#280">280</a></td></tr
><tr id="gr_svn139_281"

><td id="281"><a href="#281">281</a></td></tr
><tr id="gr_svn139_282"

><td id="282"><a href="#282">282</a></td></tr
><tr id="gr_svn139_283"

><td id="283"><a href="#283">283</a></td></tr
><tr id="gr_svn139_284"

><td id="284"><a href="#284">284</a></td></tr
><tr id="gr_svn139_285"

><td id="285"><a href="#285">285</a></td></tr
><tr id="gr_svn139_286"

><td id="286"><a href="#286">286</a></td></tr
><tr id="gr_svn139_287"

><td id="287"><a href="#287">287</a></td></tr
><tr id="gr_svn139_288"

><td id="288"><a href="#288">288</a></td></tr
><tr id="gr_svn139_289"

><td id="289"><a href="#289">289</a></td></tr
><tr id="gr_svn139_290"

><td id="290"><a href="#290">290</a></td></tr
><tr id="gr_svn139_291"

><td id="291"><a href="#291">291</a></td></tr
><tr id="gr_svn139_292"

><td id="292"><a href="#292">292</a></td></tr
><tr id="gr_svn139_293"

><td id="293"><a href="#293">293</a></td></tr
><tr id="gr_svn139_294"

><td id="294"><a href="#294">294</a></td></tr
><tr id="gr_svn139_295"

><td id="295"><a href="#295">295</a></td></tr
><tr id="gr_svn139_296"

><td id="296"><a href="#296">296</a></td></tr
><tr id="gr_svn139_297"

><td id="297"><a href="#297">297</a></td></tr
><tr id="gr_svn139_298"

><td id="298"><a href="#298">298</a></td></tr
><tr id="gr_svn139_299"

><td id="299"><a href="#299">299</a></td></tr
><tr id="gr_svn139_300"

><td id="300"><a href="#300">300</a></td></tr
><tr id="gr_svn139_301"

><td id="301"><a href="#301">301</a></td></tr
><tr id="gr_svn139_302"

><td id="302"><a href="#302">302</a></td></tr
><tr id="gr_svn139_303"

><td id="303"><a href="#303">303</a></td></tr
><tr id="gr_svn139_304"

><td id="304"><a href="#304">304</a></td></tr
><tr id="gr_svn139_305"

><td id="305"><a href="#305">305</a></td></tr
><tr id="gr_svn139_306"

><td id="306"><a href="#306">306</a></td></tr
><tr id="gr_svn139_307"

><td id="307"><a href="#307">307</a></td></tr
><tr id="gr_svn139_308"

><td id="308"><a href="#308">308</a></td></tr
><tr id="gr_svn139_309"

><td id="309"><a href="#309">309</a></td></tr
><tr id="gr_svn139_310"

><td id="310"><a href="#310">310</a></td></tr
><tr id="gr_svn139_311"

><td id="311"><a href="#311">311</a></td></tr
><tr id="gr_svn139_312"

><td id="312"><a href="#312">312</a></td></tr
><tr id="gr_svn139_313"

><td id="313"><a href="#313">313</a></td></tr
><tr id="gr_svn139_314"

><td id="314"><a href="#314">314</a></td></tr
><tr id="gr_svn139_315"

><td id="315"><a href="#315">315</a></td></tr
><tr id="gr_svn139_316"

><td id="316"><a href="#316">316</a></td></tr
><tr id="gr_svn139_317"

><td id="317"><a href="#317">317</a></td></tr
><tr id="gr_svn139_318"

><td id="318"><a href="#318">318</a></td></tr
><tr id="gr_svn139_319"

><td id="319"><a href="#319">319</a></td></tr
><tr id="gr_svn139_320"

><td id="320"><a href="#320">320</a></td></tr
><tr id="gr_svn139_321"

><td id="321"><a href="#321">321</a></td></tr
><tr id="gr_svn139_322"

><td id="322"><a href="#322">322</a></td></tr
><tr id="gr_svn139_323"

><td id="323"><a href="#323">323</a></td></tr
><tr id="gr_svn139_324"

><td id="324"><a href="#324">324</a></td></tr
><tr id="gr_svn139_325"

><td id="325"><a href="#325">325</a></td></tr
><tr id="gr_svn139_326"

><td id="326"><a href="#326">326</a></td></tr
><tr id="gr_svn139_327"

><td id="327"><a href="#327">327</a></td></tr
><tr id="gr_svn139_328"

><td id="328"><a href="#328">328</a></td></tr
><tr id="gr_svn139_329"

><td id="329"><a href="#329">329</a></td></tr
><tr id="gr_svn139_330"

><td id="330"><a href="#330">330</a></td></tr
><tr id="gr_svn139_331"

><td id="331"><a href="#331">331</a></td></tr
><tr id="gr_svn139_332"

><td id="332"><a href="#332">332</a></td></tr
><tr id="gr_svn139_333"

><td id="333"><a href="#333">333</a></td></tr
><tr id="gr_svn139_334"

><td id="334"><a href="#334">334</a></td></tr
><tr id="gr_svn139_335"

><td id="335"><a href="#335">335</a></td></tr
><tr id="gr_svn139_336"

><td id="336"><a href="#336">336</a></td></tr
><tr id="gr_svn139_337"

><td id="337"><a href="#337">337</a></td></tr
><tr id="gr_svn139_338"

><td id="338"><a href="#338">338</a></td></tr
><tr id="gr_svn139_339"

><td id="339"><a href="#339">339</a></td></tr
><tr id="gr_svn139_340"

><td id="340"><a href="#340">340</a></td></tr
><tr id="gr_svn139_341"

><td id="341"><a href="#341">341</a></td></tr
><tr id="gr_svn139_342"

><td id="342"><a href="#342">342</a></td></tr
><tr id="gr_svn139_343"

><td id="343"><a href="#343">343</a></td></tr
><tr id="gr_svn139_344"

><td id="344"><a href="#344">344</a></td></tr
><tr id="gr_svn139_345"

><td id="345"><a href="#345">345</a></td></tr
><tr id="gr_svn139_346"

><td id="346"><a href="#346">346</a></td></tr
><tr id="gr_svn139_347"

><td id="347"><a href="#347">347</a></td></tr
><tr id="gr_svn139_348"

><td id="348"><a href="#348">348</a></td></tr
><tr id="gr_svn139_349"

><td id="349"><a href="#349">349</a></td></tr
><tr id="gr_svn139_350"

><td id="350"><a href="#350">350</a></td></tr
><tr id="gr_svn139_351"

><td id="351"><a href="#351">351</a></td></tr
><tr id="gr_svn139_352"

><td id="352"><a href="#352">352</a></td></tr
><tr id="gr_svn139_353"

><td id="353"><a href="#353">353</a></td></tr
><tr id="gr_svn139_354"

><td id="354"><a href="#354">354</a></td></tr
><tr id="gr_svn139_355"

><td id="355"><a href="#355">355</a></td></tr
><tr id="gr_svn139_356"

><td id="356"><a href="#356">356</a></td></tr
><tr id="gr_svn139_357"

><td id="357"><a href="#357">357</a></td></tr
><tr id="gr_svn139_358"

><td id="358"><a href="#358">358</a></td></tr
><tr id="gr_svn139_359"

><td id="359"><a href="#359">359</a></td></tr
><tr id="gr_svn139_360"

><td id="360"><a href="#360">360</a></td></tr
><tr id="gr_svn139_361"

><td id="361"><a href="#361">361</a></td></tr
><tr id="gr_svn139_362"

><td id="362"><a href="#362">362</a></td></tr
><tr id="gr_svn139_363"

><td id="363"><a href="#363">363</a></td></tr
><tr id="gr_svn139_364"

><td id="364"><a href="#364">364</a></td></tr
><tr id="gr_svn139_365"

><td id="365"><a href="#365">365</a></td></tr
><tr id="gr_svn139_366"

><td id="366"><a href="#366">366</a></td></tr
><tr id="gr_svn139_367"

><td id="367"><a href="#367">367</a></td></tr
><tr id="gr_svn139_368"

><td id="368"><a href="#368">368</a></td></tr
><tr id="gr_svn139_369"

><td id="369"><a href="#369">369</a></td></tr
><tr id="gr_svn139_370"

><td id="370"><a href="#370">370</a></td></tr
><tr id="gr_svn139_371"

><td id="371"><a href="#371">371</a></td></tr
><tr id="gr_svn139_372"

><td id="372"><a href="#372">372</a></td></tr
><tr id="gr_svn139_373"

><td id="373"><a href="#373">373</a></td></tr
><tr id="gr_svn139_374"

><td id="374"><a href="#374">374</a></td></tr
><tr id="gr_svn139_375"

><td id="375"><a href="#375">375</a></td></tr
><tr id="gr_svn139_376"

><td id="376"><a href="#376">376</a></td></tr
><tr id="gr_svn139_377"

><td id="377"><a href="#377">377</a></td></tr
><tr id="gr_svn139_378"

><td id="378"><a href="#378">378</a></td></tr
><tr id="gr_svn139_379"

><td id="379"><a href="#379">379</a></td></tr
><tr id="gr_svn139_380"

><td id="380"><a href="#380">380</a></td></tr
><tr id="gr_svn139_381"

><td id="381"><a href="#381">381</a></td></tr
><tr id="gr_svn139_382"

><td id="382"><a href="#382">382</a></td></tr
><tr id="gr_svn139_383"

><td id="383"><a href="#383">383</a></td></tr
><tr id="gr_svn139_384"

><td id="384"><a href="#384">384</a></td></tr
><tr id="gr_svn139_385"

><td id="385"><a href="#385">385</a></td></tr
><tr id="gr_svn139_386"

><td id="386"><a href="#386">386</a></td></tr
><tr id="gr_svn139_387"

><td id="387"><a href="#387">387</a></td></tr
><tr id="gr_svn139_388"

><td id="388"><a href="#388">388</a></td></tr
><tr id="gr_svn139_389"

><td id="389"><a href="#389">389</a></td></tr
><tr id="gr_svn139_390"

><td id="390"><a href="#390">390</a></td></tr
><tr id="gr_svn139_391"

><td id="391"><a href="#391">391</a></td></tr
><tr id="gr_svn139_392"

><td id="392"><a href="#392">392</a></td></tr
><tr id="gr_svn139_393"

><td id="393"><a href="#393">393</a></td></tr
><tr id="gr_svn139_394"

><td id="394"><a href="#394">394</a></td></tr
><tr id="gr_svn139_395"

><td id="395"><a href="#395">395</a></td></tr
><tr id="gr_svn139_396"

><td id="396"><a href="#396">396</a></td></tr
><tr id="gr_svn139_397"

><td id="397"><a href="#397">397</a></td></tr
><tr id="gr_svn139_398"

><td id="398"><a href="#398">398</a></td></tr
><tr id="gr_svn139_399"

><td id="399"><a href="#399">399</a></td></tr
><tr id="gr_svn139_400"

><td id="400"><a href="#400">400</a></td></tr
><tr id="gr_svn139_401"

><td id="401"><a href="#401">401</a></td></tr
><tr id="gr_svn139_402"

><td id="402"><a href="#402">402</a></td></tr
><tr id="gr_svn139_403"

><td id="403"><a href="#403">403</a></td></tr
><tr id="gr_svn139_404"

><td id="404"><a href="#404">404</a></td></tr
><tr id="gr_svn139_405"

><td id="405"><a href="#405">405</a></td></tr
><tr id="gr_svn139_406"

><td id="406"><a href="#406">406</a></td></tr
><tr id="gr_svn139_407"

><td id="407"><a href="#407">407</a></td></tr
><tr id="gr_svn139_408"

><td id="408"><a href="#408">408</a></td></tr
><tr id="gr_svn139_409"

><td id="409"><a href="#409">409</a></td></tr
><tr id="gr_svn139_410"

><td id="410"><a href="#410">410</a></td></tr
><tr id="gr_svn139_411"

><td id="411"><a href="#411">411</a></td></tr
><tr id="gr_svn139_412"

><td id="412"><a href="#412">412</a></td></tr
><tr id="gr_svn139_413"

><td id="413"><a href="#413">413</a></td></tr
><tr id="gr_svn139_414"

><td id="414"><a href="#414">414</a></td></tr
><tr id="gr_svn139_415"

><td id="415"><a href="#415">415</a></td></tr
><tr id="gr_svn139_416"

><td id="416"><a href="#416">416</a></td></tr
><tr id="gr_svn139_417"

><td id="417"><a href="#417">417</a></td></tr
><tr id="gr_svn139_418"

><td id="418"><a href="#418">418</a></td></tr
><tr id="gr_svn139_419"

><td id="419"><a href="#419">419</a></td></tr
><tr id="gr_svn139_420"

><td id="420"><a href="#420">420</a></td></tr
><tr id="gr_svn139_421"

><td id="421"><a href="#421">421</a></td></tr
><tr id="gr_svn139_422"

><td id="422"><a href="#422">422</a></td></tr
><tr id="gr_svn139_423"

><td id="423"><a href="#423">423</a></td></tr
><tr id="gr_svn139_424"

><td id="424"><a href="#424">424</a></td></tr
><tr id="gr_svn139_425"

><td id="425"><a href="#425">425</a></td></tr
><tr id="gr_svn139_426"

><td id="426"><a href="#426">426</a></td></tr
><tr id="gr_svn139_427"

><td id="427"><a href="#427">427</a></td></tr
><tr id="gr_svn139_428"

><td id="428"><a href="#428">428</a></td></tr
><tr id="gr_svn139_429"

><td id="429"><a href="#429">429</a></td></tr
><tr id="gr_svn139_430"

><td id="430"><a href="#430">430</a></td></tr
><tr id="gr_svn139_431"

><td id="431"><a href="#431">431</a></td></tr
><tr id="gr_svn139_432"

><td id="432"><a href="#432">432</a></td></tr
><tr id="gr_svn139_433"

><td id="433"><a href="#433">433</a></td></tr
><tr id="gr_svn139_434"

><td id="434"><a href="#434">434</a></td></tr
><tr id="gr_svn139_435"

><td id="435"><a href="#435">435</a></td></tr
><tr id="gr_svn139_436"

><td id="436"><a href="#436">436</a></td></tr
><tr id="gr_svn139_437"

><td id="437"><a href="#437">437</a></td></tr
><tr id="gr_svn139_438"

><td id="438"><a href="#438">438</a></td></tr
><tr id="gr_svn139_439"

><td id="439"><a href="#439">439</a></td></tr
><tr id="gr_svn139_440"

><td id="440"><a href="#440">440</a></td></tr
><tr id="gr_svn139_441"

><td id="441"><a href="#441">441</a></td></tr
><tr id="gr_svn139_442"

><td id="442"><a href="#442">442</a></td></tr
><tr id="gr_svn139_443"

><td id="443"><a href="#443">443</a></td></tr
><tr id="gr_svn139_444"

><td id="444"><a href="#444">444</a></td></tr
><tr id="gr_svn139_445"

><td id="445"><a href="#445">445</a></td></tr
><tr id="gr_svn139_446"

><td id="446"><a href="#446">446</a></td></tr
><tr id="gr_svn139_447"

><td id="447"><a href="#447">447</a></td></tr
><tr id="gr_svn139_448"

><td id="448"><a href="#448">448</a></td></tr
><tr id="gr_svn139_449"

><td id="449"><a href="#449">449</a></td></tr
><tr id="gr_svn139_450"

><td id="450"><a href="#450">450</a></td></tr
><tr id="gr_svn139_451"

><td id="451"><a href="#451">451</a></td></tr
><tr id="gr_svn139_452"

><td id="452"><a href="#452">452</a></td></tr
><tr id="gr_svn139_453"

><td id="453"><a href="#453">453</a></td></tr
><tr id="gr_svn139_454"

><td id="454"><a href="#454">454</a></td></tr
><tr id="gr_svn139_455"

><td id="455"><a href="#455">455</a></td></tr
><tr id="gr_svn139_456"

><td id="456"><a href="#456">456</a></td></tr
><tr id="gr_svn139_457"

><td id="457"><a href="#457">457</a></td></tr
><tr id="gr_svn139_458"

><td id="458"><a href="#458">458</a></td></tr
><tr id="gr_svn139_459"

><td id="459"><a href="#459">459</a></td></tr
><tr id="gr_svn139_460"

><td id="460"><a href="#460">460</a></td></tr
><tr id="gr_svn139_461"

><td id="461"><a href="#461">461</a></td></tr
><tr id="gr_svn139_462"

><td id="462"><a href="#462">462</a></td></tr
><tr id="gr_svn139_463"

><td id="463"><a href="#463">463</a></td></tr
><tr id="gr_svn139_464"

><td id="464"><a href="#464">464</a></td></tr
><tr id="gr_svn139_465"

><td id="465"><a href="#465">465</a></td></tr
><tr id="gr_svn139_466"

><td id="466"><a href="#466">466</a></td></tr
><tr id="gr_svn139_467"

><td id="467"><a href="#467">467</a></td></tr
><tr id="gr_svn139_468"

><td id="468"><a href="#468">468</a></td></tr
><tr id="gr_svn139_469"

><td id="469"><a href="#469">469</a></td></tr
><tr id="gr_svn139_470"

><td id="470"><a href="#470">470</a></td></tr
><tr id="gr_svn139_471"

><td id="471"><a href="#471">471</a></td></tr
><tr id="gr_svn139_472"

><td id="472"><a href="#472">472</a></td></tr
><tr id="gr_svn139_473"

><td id="473"><a href="#473">473</a></td></tr
><tr id="gr_svn139_474"

><td id="474"><a href="#474">474</a></td></tr
><tr id="gr_svn139_475"

><td id="475"><a href="#475">475</a></td></tr
><tr id="gr_svn139_476"

><td id="476"><a href="#476">476</a></td></tr
><tr id="gr_svn139_477"

><td id="477"><a href="#477">477</a></td></tr
><tr id="gr_svn139_478"

><td id="478"><a href="#478">478</a></td></tr
><tr id="gr_svn139_479"

><td id="479"><a href="#479">479</a></td></tr
><tr id="gr_svn139_480"

><td id="480"><a href="#480">480</a></td></tr
><tr id="gr_svn139_481"

><td id="481"><a href="#481">481</a></td></tr
><tr id="gr_svn139_482"

><td id="482"><a href="#482">482</a></td></tr
><tr id="gr_svn139_483"

><td id="483"><a href="#483">483</a></td></tr
><tr id="gr_svn139_484"

><td id="484"><a href="#484">484</a></td></tr
><tr id="gr_svn139_485"

><td id="485"><a href="#485">485</a></td></tr
><tr id="gr_svn139_486"

><td id="486"><a href="#486">486</a></td></tr
><tr id="gr_svn139_487"

><td id="487"><a href="#487">487</a></td></tr
><tr id="gr_svn139_488"

><td id="488"><a href="#488">488</a></td></tr
><tr id="gr_svn139_489"

><td id="489"><a href="#489">489</a></td></tr
><tr id="gr_svn139_490"

><td id="490"><a href="#490">490</a></td></tr
><tr id="gr_svn139_491"

><td id="491"><a href="#491">491</a></td></tr
><tr id="gr_svn139_492"

><td id="492"><a href="#492">492</a></td></tr
><tr id="gr_svn139_493"

><td id="493"><a href="#493">493</a></td></tr
><tr id="gr_svn139_494"

><td id="494"><a href="#494">494</a></td></tr
><tr id="gr_svn139_495"

><td id="495"><a href="#495">495</a></td></tr
><tr id="gr_svn139_496"

><td id="496"><a href="#496">496</a></td></tr
><tr id="gr_svn139_497"

><td id="497"><a href="#497">497</a></td></tr
><tr id="gr_svn139_498"

><td id="498"><a href="#498">498</a></td></tr
><tr id="gr_svn139_499"

><td id="499"><a href="#499">499</a></td></tr
><tr id="gr_svn139_500"

><td id="500"><a href="#500">500</a></td></tr
><tr id="gr_svn139_501"

><td id="501"><a href="#501">501</a></td></tr
><tr id="gr_svn139_502"

><td id="502"><a href="#502">502</a></td></tr
><tr id="gr_svn139_503"

><td id="503"><a href="#503">503</a></td></tr
><tr id="gr_svn139_504"

><td id="504"><a href="#504">504</a></td></tr
><tr id="gr_svn139_505"

><td id="505"><a href="#505">505</a></td></tr
><tr id="gr_svn139_506"

><td id="506"><a href="#506">506</a></td></tr
><tr id="gr_svn139_507"

><td id="507"><a href="#507">507</a></td></tr
><tr id="gr_svn139_508"

><td id="508"><a href="#508">508</a></td></tr
><tr id="gr_svn139_509"

><td id="509"><a href="#509">509</a></td></tr
><tr id="gr_svn139_510"

><td id="510"><a href="#510">510</a></td></tr
><tr id="gr_svn139_511"

><td id="511"><a href="#511">511</a></td></tr
><tr id="gr_svn139_512"

><td id="512"><a href="#512">512</a></td></tr
><tr id="gr_svn139_513"

><td id="513"><a href="#513">513</a></td></tr
><tr id="gr_svn139_514"

><td id="514"><a href="#514">514</a></td></tr
><tr id="gr_svn139_515"

><td id="515"><a href="#515">515</a></td></tr
><tr id="gr_svn139_516"

><td id="516"><a href="#516">516</a></td></tr
><tr id="gr_svn139_517"

><td id="517"><a href="#517">517</a></td></tr
><tr id="gr_svn139_518"

><td id="518"><a href="#518">518</a></td></tr
><tr id="gr_svn139_519"

><td id="519"><a href="#519">519</a></td></tr
><tr id="gr_svn139_520"

><td id="520"><a href="#520">520</a></td></tr
><tr id="gr_svn139_521"

><td id="521"><a href="#521">521</a></td></tr
><tr id="gr_svn139_522"

><td id="522"><a href="#522">522</a></td></tr
><tr id="gr_svn139_523"

><td id="523"><a href="#523">523</a></td></tr
><tr id="gr_svn139_524"

><td id="524"><a href="#524">524</a></td></tr
><tr id="gr_svn139_525"

><td id="525"><a href="#525">525</a></td></tr
><tr id="gr_svn139_526"

><td id="526"><a href="#526">526</a></td></tr
><tr id="gr_svn139_527"

><td id="527"><a href="#527">527</a></td></tr
><tr id="gr_svn139_528"

><td id="528"><a href="#528">528</a></td></tr
><tr id="gr_svn139_529"

><td id="529"><a href="#529">529</a></td></tr
><tr id="gr_svn139_530"

><td id="530"><a href="#530">530</a></td></tr
><tr id="gr_svn139_531"

><td id="531"><a href="#531">531</a></td></tr
><tr id="gr_svn139_532"

><td id="532"><a href="#532">532</a></td></tr
><tr id="gr_svn139_533"

><td id="533"><a href="#533">533</a></td></tr
><tr id="gr_svn139_534"

><td id="534"><a href="#534">534</a></td></tr
><tr id="gr_svn139_535"

><td id="535"><a href="#535">535</a></td></tr
><tr id="gr_svn139_536"

><td id="536"><a href="#536">536</a></td></tr
><tr id="gr_svn139_537"

><td id="537"><a href="#537">537</a></td></tr
><tr id="gr_svn139_538"

><td id="538"><a href="#538">538</a></td></tr
><tr id="gr_svn139_539"

><td id="539"><a href="#539">539</a></td></tr
><tr id="gr_svn139_540"

><td id="540"><a href="#540">540</a></td></tr
><tr id="gr_svn139_541"

><td id="541"><a href="#541">541</a></td></tr
><tr id="gr_svn139_542"

><td id="542"><a href="#542">542</a></td></tr
><tr id="gr_svn139_543"

><td id="543"><a href="#543">543</a></td></tr
><tr id="gr_svn139_544"

><td id="544"><a href="#544">544</a></td></tr
><tr id="gr_svn139_545"

><td id="545"><a href="#545">545</a></td></tr
><tr id="gr_svn139_546"

><td id="546"><a href="#546">546</a></td></tr
><tr id="gr_svn139_547"

><td id="547"><a href="#547">547</a></td></tr
><tr id="gr_svn139_548"

><td id="548"><a href="#548">548</a></td></tr
><tr id="gr_svn139_549"

><td id="549"><a href="#549">549</a></td></tr
><tr id="gr_svn139_550"

><td id="550"><a href="#550">550</a></td></tr
><tr id="gr_svn139_551"

><td id="551"><a href="#551">551</a></td></tr
><tr id="gr_svn139_552"

><td id="552"><a href="#552">552</a></td></tr
><tr id="gr_svn139_553"

><td id="553"><a href="#553">553</a></td></tr
><tr id="gr_svn139_554"

><td id="554"><a href="#554">554</a></td></tr
><tr id="gr_svn139_555"

><td id="555"><a href="#555">555</a></td></tr
><tr id="gr_svn139_556"

><td id="556"><a href="#556">556</a></td></tr
><tr id="gr_svn139_557"

><td id="557"><a href="#557">557</a></td></tr
><tr id="gr_svn139_558"

><td id="558"><a href="#558">558</a></td></tr
><tr id="gr_svn139_559"

><td id="559"><a href="#559">559</a></td></tr
><tr id="gr_svn139_560"

><td id="560"><a href="#560">560</a></td></tr
><tr id="gr_svn139_561"

><td id="561"><a href="#561">561</a></td></tr
><tr id="gr_svn139_562"

><td id="562"><a href="#562">562</a></td></tr
><tr id="gr_svn139_563"

><td id="563"><a href="#563">563</a></td></tr
><tr id="gr_svn139_564"

><td id="564"><a href="#564">564</a></td></tr
><tr id="gr_svn139_565"

><td id="565"><a href="#565">565</a></td></tr
><tr id="gr_svn139_566"

><td id="566"><a href="#566">566</a></td></tr
><tr id="gr_svn139_567"

><td id="567"><a href="#567">567</a></td></tr
><tr id="gr_svn139_568"

><td id="568"><a href="#568">568</a></td></tr
><tr id="gr_svn139_569"

><td id="569"><a href="#569">569</a></td></tr
><tr id="gr_svn139_570"

><td id="570"><a href="#570">570</a></td></tr
><tr id="gr_svn139_571"

><td id="571"><a href="#571">571</a></td></tr
><tr id="gr_svn139_572"

><td id="572"><a href="#572">572</a></td></tr
><tr id="gr_svn139_573"

><td id="573"><a href="#573">573</a></td></tr
><tr id="gr_svn139_574"

><td id="574"><a href="#574">574</a></td></tr
><tr id="gr_svn139_575"

><td id="575"><a href="#575">575</a></td></tr
><tr id="gr_svn139_576"

><td id="576"><a href="#576">576</a></td></tr
><tr id="gr_svn139_577"

><td id="577"><a href="#577">577</a></td></tr
><tr id="gr_svn139_578"

><td id="578"><a href="#578">578</a></td></tr
><tr id="gr_svn139_579"

><td id="579"><a href="#579">579</a></td></tr
><tr id="gr_svn139_580"

><td id="580"><a href="#580">580</a></td></tr
><tr id="gr_svn139_581"

><td id="581"><a href="#581">581</a></td></tr
><tr id="gr_svn139_582"

><td id="582"><a href="#582">582</a></td></tr
><tr id="gr_svn139_583"

><td id="583"><a href="#583">583</a></td></tr
><tr id="gr_svn139_584"

><td id="584"><a href="#584">584</a></td></tr
><tr id="gr_svn139_585"

><td id="585"><a href="#585">585</a></td></tr
><tr id="gr_svn139_586"

><td id="586"><a href="#586">586</a></td></tr
><tr id="gr_svn139_587"

><td id="587"><a href="#587">587</a></td></tr
><tr id="gr_svn139_588"

><td id="588"><a href="#588">588</a></td></tr
><tr id="gr_svn139_589"

><td id="589"><a href="#589">589</a></td></tr
><tr id="gr_svn139_590"

><td id="590"><a href="#590">590</a></td></tr
><tr id="gr_svn139_591"

><td id="591"><a href="#591">591</a></td></tr
><tr id="gr_svn139_592"

><td id="592"><a href="#592">592</a></td></tr
><tr id="gr_svn139_593"

><td id="593"><a href="#593">593</a></td></tr
><tr id="gr_svn139_594"

><td id="594"><a href="#594">594</a></td></tr
><tr id="gr_svn139_595"

><td id="595"><a href="#595">595</a></td></tr
><tr id="gr_svn139_596"

><td id="596"><a href="#596">596</a></td></tr
><tr id="gr_svn139_597"

><td id="597"><a href="#597">597</a></td></tr
><tr id="gr_svn139_598"

><td id="598"><a href="#598">598</a></td></tr
><tr id="gr_svn139_599"

><td id="599"><a href="#599">599</a></td></tr
><tr id="gr_svn139_600"

><td id="600"><a href="#600">600</a></td></tr
><tr id="gr_svn139_601"

><td id="601"><a href="#601">601</a></td></tr
><tr id="gr_svn139_602"

><td id="602"><a href="#602">602</a></td></tr
><tr id="gr_svn139_603"

><td id="603"><a href="#603">603</a></td></tr
><tr id="gr_svn139_604"

><td id="604"><a href="#604">604</a></td></tr
><tr id="gr_svn139_605"

><td id="605"><a href="#605">605</a></td></tr
><tr id="gr_svn139_606"

><td id="606"><a href="#606">606</a></td></tr
><tr id="gr_svn139_607"

><td id="607"><a href="#607">607</a></td></tr
><tr id="gr_svn139_608"

><td id="608"><a href="#608">608</a></td></tr
><tr id="gr_svn139_609"

><td id="609"><a href="#609">609</a></td></tr
><tr id="gr_svn139_610"

><td id="610"><a href="#610">610</a></td></tr
><tr id="gr_svn139_611"

><td id="611"><a href="#611">611</a></td></tr
><tr id="gr_svn139_612"

><td id="612"><a href="#612">612</a></td></tr
><tr id="gr_svn139_613"

><td id="613"><a href="#613">613</a></td></tr
><tr id="gr_svn139_614"

><td id="614"><a href="#614">614</a></td></tr
><tr id="gr_svn139_615"

><td id="615"><a href="#615">615</a></td></tr
><tr id="gr_svn139_616"

><td id="616"><a href="#616">616</a></td></tr
><tr id="gr_svn139_617"

><td id="617"><a href="#617">617</a></td></tr
><tr id="gr_svn139_618"

><td id="618"><a href="#618">618</a></td></tr
><tr id="gr_svn139_619"

><td id="619"><a href="#619">619</a></td></tr
><tr id="gr_svn139_620"

><td id="620"><a href="#620">620</a></td></tr
><tr id="gr_svn139_621"

><td id="621"><a href="#621">621</a></td></tr
><tr id="gr_svn139_622"

><td id="622"><a href="#622">622</a></td></tr
><tr id="gr_svn139_623"

><td id="623"><a href="#623">623</a></td></tr
><tr id="gr_svn139_624"

><td id="624"><a href="#624">624</a></td></tr
><tr id="gr_svn139_625"

><td id="625"><a href="#625">625</a></td></tr
><tr id="gr_svn139_626"

><td id="626"><a href="#626">626</a></td></tr
><tr id="gr_svn139_627"

><td id="627"><a href="#627">627</a></td></tr
><tr id="gr_svn139_628"

><td id="628"><a href="#628">628</a></td></tr
><tr id="gr_svn139_629"

><td id="629"><a href="#629">629</a></td></tr
><tr id="gr_svn139_630"

><td id="630"><a href="#630">630</a></td></tr
><tr id="gr_svn139_631"

><td id="631"><a href="#631">631</a></td></tr
><tr id="gr_svn139_632"

><td id="632"><a href="#632">632</a></td></tr
><tr id="gr_svn139_633"

><td id="633"><a href="#633">633</a></td></tr
><tr id="gr_svn139_634"

><td id="634"><a href="#634">634</a></td></tr
><tr id="gr_svn139_635"

><td id="635"><a href="#635">635</a></td></tr
><tr id="gr_svn139_636"

><td id="636"><a href="#636">636</a></td></tr
><tr id="gr_svn139_637"

><td id="637"><a href="#637">637</a></td></tr
><tr id="gr_svn139_638"

><td id="638"><a href="#638">638</a></td></tr
><tr id="gr_svn139_639"

><td id="639"><a href="#639">639</a></td></tr
><tr id="gr_svn139_640"

><td id="640"><a href="#640">640</a></td></tr
><tr id="gr_svn139_641"

><td id="641"><a href="#641">641</a></td></tr
><tr id="gr_svn139_642"

><td id="642"><a href="#642">642</a></td></tr
><tr id="gr_svn139_643"

><td id="643"><a href="#643">643</a></td></tr
><tr id="gr_svn139_644"

><td id="644"><a href="#644">644</a></td></tr
><tr id="gr_svn139_645"

><td id="645"><a href="#645">645</a></td></tr
><tr id="gr_svn139_646"

><td id="646"><a href="#646">646</a></td></tr
><tr id="gr_svn139_647"

><td id="647"><a href="#647">647</a></td></tr
><tr id="gr_svn139_648"

><td id="648"><a href="#648">648</a></td></tr
><tr id="gr_svn139_649"

><td id="649"><a href="#649">649</a></td></tr
><tr id="gr_svn139_650"

><td id="650"><a href="#650">650</a></td></tr
><tr id="gr_svn139_651"

><td id="651"><a href="#651">651</a></td></tr
><tr id="gr_svn139_652"

><td id="652"><a href="#652">652</a></td></tr
><tr id="gr_svn139_653"

><td id="653"><a href="#653">653</a></td></tr
><tr id="gr_svn139_654"

><td id="654"><a href="#654">654</a></td></tr
><tr id="gr_svn139_655"

><td id="655"><a href="#655">655</a></td></tr
><tr id="gr_svn139_656"

><td id="656"><a href="#656">656</a></td></tr
><tr id="gr_svn139_657"

><td id="657"><a href="#657">657</a></td></tr
><tr id="gr_svn139_658"

><td id="658"><a href="#658">658</a></td></tr
><tr id="gr_svn139_659"

><td id="659"><a href="#659">659</a></td></tr
><tr id="gr_svn139_660"

><td id="660"><a href="#660">660</a></td></tr
><tr id="gr_svn139_661"

><td id="661"><a href="#661">661</a></td></tr
><tr id="gr_svn139_662"

><td id="662"><a href="#662">662</a></td></tr
><tr id="gr_svn139_663"

><td id="663"><a href="#663">663</a></td></tr
><tr id="gr_svn139_664"

><td id="664"><a href="#664">664</a></td></tr
><tr id="gr_svn139_665"

><td id="665"><a href="#665">665</a></td></tr
><tr id="gr_svn139_666"

><td id="666"><a href="#666">666</a></td></tr
><tr id="gr_svn139_667"

><td id="667"><a href="#667">667</a></td></tr
><tr id="gr_svn139_668"

><td id="668"><a href="#668">668</a></td></tr
><tr id="gr_svn139_669"

><td id="669"><a href="#669">669</a></td></tr
><tr id="gr_svn139_670"

><td id="670"><a href="#670">670</a></td></tr
><tr id="gr_svn139_671"

><td id="671"><a href="#671">671</a></td></tr
><tr id="gr_svn139_672"

><td id="672"><a href="#672">672</a></td></tr
><tr id="gr_svn139_673"

><td id="673"><a href="#673">673</a></td></tr
><tr id="gr_svn139_674"

><td id="674"><a href="#674">674</a></td></tr
><tr id="gr_svn139_675"

><td id="675"><a href="#675">675</a></td></tr
><tr id="gr_svn139_676"

><td id="676"><a href="#676">676</a></td></tr
><tr id="gr_svn139_677"

><td id="677"><a href="#677">677</a></td></tr
><tr id="gr_svn139_678"

><td id="678"><a href="#678">678</a></td></tr
><tr id="gr_svn139_679"

><td id="679"><a href="#679">679</a></td></tr
><tr id="gr_svn139_680"

><td id="680"><a href="#680">680</a></td></tr
><tr id="gr_svn139_681"

><td id="681"><a href="#681">681</a></td></tr
><tr id="gr_svn139_682"

><td id="682"><a href="#682">682</a></td></tr
><tr id="gr_svn139_683"

><td id="683"><a href="#683">683</a></td></tr
><tr id="gr_svn139_684"

><td id="684"><a href="#684">684</a></td></tr
><tr id="gr_svn139_685"

><td id="685"><a href="#685">685</a></td></tr
><tr id="gr_svn139_686"

><td id="686"><a href="#686">686</a></td></tr
><tr id="gr_svn139_687"

><td id="687"><a href="#687">687</a></td></tr
><tr id="gr_svn139_688"

><td id="688"><a href="#688">688</a></td></tr
><tr id="gr_svn139_689"

><td id="689"><a href="#689">689</a></td></tr
><tr id="gr_svn139_690"

><td id="690"><a href="#690">690</a></td></tr
><tr id="gr_svn139_691"

><td id="691"><a href="#691">691</a></td></tr
><tr id="gr_svn139_692"

><td id="692"><a href="#692">692</a></td></tr
><tr id="gr_svn139_693"

><td id="693"><a href="#693">693</a></td></tr
><tr id="gr_svn139_694"

><td id="694"><a href="#694">694</a></td></tr
><tr id="gr_svn139_695"

><td id="695"><a href="#695">695</a></td></tr
><tr id="gr_svn139_696"

><td id="696"><a href="#696">696</a></td></tr
><tr id="gr_svn139_697"

><td id="697"><a href="#697">697</a></td></tr
><tr id="gr_svn139_698"

><td id="698"><a href="#698">698</a></td></tr
><tr id="gr_svn139_699"

><td id="699"><a href="#699">699</a></td></tr
><tr id="gr_svn139_700"

><td id="700"><a href="#700">700</a></td></tr
><tr id="gr_svn139_701"

><td id="701"><a href="#701">701</a></td></tr
><tr id="gr_svn139_702"

><td id="702"><a href="#702">702</a></td></tr
><tr id="gr_svn139_703"

><td id="703"><a href="#703">703</a></td></tr
><tr id="gr_svn139_704"

><td id="704"><a href="#704">704</a></td></tr
><tr id="gr_svn139_705"

><td id="705"><a href="#705">705</a></td></tr
><tr id="gr_svn139_706"

><td id="706"><a href="#706">706</a></td></tr
><tr id="gr_svn139_707"

><td id="707"><a href="#707">707</a></td></tr
><tr id="gr_svn139_708"

><td id="708"><a href="#708">708</a></td></tr
><tr id="gr_svn139_709"

><td id="709"><a href="#709">709</a></td></tr
><tr id="gr_svn139_710"

><td id="710"><a href="#710">710</a></td></tr
><tr id="gr_svn139_711"

><td id="711"><a href="#711">711</a></td></tr
><tr id="gr_svn139_712"

><td id="712"><a href="#712">712</a></td></tr
><tr id="gr_svn139_713"

><td id="713"><a href="#713">713</a></td></tr
><tr id="gr_svn139_714"

><td id="714"><a href="#714">714</a></td></tr
><tr id="gr_svn139_715"

><td id="715"><a href="#715">715</a></td></tr
><tr id="gr_svn139_716"

><td id="716"><a href="#716">716</a></td></tr
><tr id="gr_svn139_717"

><td id="717"><a href="#717">717</a></td></tr
><tr id="gr_svn139_718"

><td id="718"><a href="#718">718</a></td></tr
><tr id="gr_svn139_719"

><td id="719"><a href="#719">719</a></td></tr
><tr id="gr_svn139_720"

><td id="720"><a href="#720">720</a></td></tr
><tr id="gr_svn139_721"

><td id="721"><a href="#721">721</a></td></tr
><tr id="gr_svn139_722"

><td id="722"><a href="#722">722</a></td></tr
><tr id="gr_svn139_723"

><td id="723"><a href="#723">723</a></td></tr
><tr id="gr_svn139_724"

><td id="724"><a href="#724">724</a></td></tr
><tr id="gr_svn139_725"

><td id="725"><a href="#725">725</a></td></tr
><tr id="gr_svn139_726"

><td id="726"><a href="#726">726</a></td></tr
><tr id="gr_svn139_727"

><td id="727"><a href="#727">727</a></td></tr
><tr id="gr_svn139_728"

><td id="728"><a href="#728">728</a></td></tr
><tr id="gr_svn139_729"

><td id="729"><a href="#729">729</a></td></tr
><tr id="gr_svn139_730"

><td id="730"><a href="#730">730</a></td></tr
><tr id="gr_svn139_731"

><td id="731"><a href="#731">731</a></td></tr
><tr id="gr_svn139_732"

><td id="732"><a href="#732">732</a></td></tr
><tr id="gr_svn139_733"

><td id="733"><a href="#733">733</a></td></tr
><tr id="gr_svn139_734"

><td id="734"><a href="#734">734</a></td></tr
><tr id="gr_svn139_735"

><td id="735"><a href="#735">735</a></td></tr
><tr id="gr_svn139_736"

><td id="736"><a href="#736">736</a></td></tr
><tr id="gr_svn139_737"

><td id="737"><a href="#737">737</a></td></tr
><tr id="gr_svn139_738"

><td id="738"><a href="#738">738</a></td></tr
><tr id="gr_svn139_739"

><td id="739"><a href="#739">739</a></td></tr
><tr id="gr_svn139_740"

><td id="740"><a href="#740">740</a></td></tr
><tr id="gr_svn139_741"

><td id="741"><a href="#741">741</a></td></tr
><tr id="gr_svn139_742"

><td id="742"><a href="#742">742</a></td></tr
><tr id="gr_svn139_743"

><td id="743"><a href="#743">743</a></td></tr
><tr id="gr_svn139_744"

><td id="744"><a href="#744">744</a></td></tr
><tr id="gr_svn139_745"

><td id="745"><a href="#745">745</a></td></tr
><tr id="gr_svn139_746"

><td id="746"><a href="#746">746</a></td></tr
><tr id="gr_svn139_747"

><td id="747"><a href="#747">747</a></td></tr
><tr id="gr_svn139_748"

><td id="748"><a href="#748">748</a></td></tr
><tr id="gr_svn139_749"

><td id="749"><a href="#749">749</a></td></tr
><tr id="gr_svn139_750"

><td id="750"><a href="#750">750</a></td></tr
><tr id="gr_svn139_751"

><td id="751"><a href="#751">751</a></td></tr
><tr id="gr_svn139_752"

><td id="752"><a href="#752">752</a></td></tr
><tr id="gr_svn139_753"

><td id="753"><a href="#753">753</a></td></tr
><tr id="gr_svn139_754"

><td id="754"><a href="#754">754</a></td></tr
><tr id="gr_svn139_755"

><td id="755"><a href="#755">755</a></td></tr
><tr id="gr_svn139_756"

><td id="756"><a href="#756">756</a></td></tr
><tr id="gr_svn139_757"

><td id="757"><a href="#757">757</a></td></tr
><tr id="gr_svn139_758"

><td id="758"><a href="#758">758</a></td></tr
><tr id="gr_svn139_759"

><td id="759"><a href="#759">759</a></td></tr
><tr id="gr_svn139_760"

><td id="760"><a href="#760">760</a></td></tr
><tr id="gr_svn139_761"

><td id="761"><a href="#761">761</a></td></tr
><tr id="gr_svn139_762"

><td id="762"><a href="#762">762</a></td></tr
><tr id="gr_svn139_763"

><td id="763"><a href="#763">763</a></td></tr
><tr id="gr_svn139_764"

><td id="764"><a href="#764">764</a></td></tr
><tr id="gr_svn139_765"

><td id="765"><a href="#765">765</a></td></tr
><tr id="gr_svn139_766"

><td id="766"><a href="#766">766</a></td></tr
><tr id="gr_svn139_767"

><td id="767"><a href="#767">767</a></td></tr
><tr id="gr_svn139_768"

><td id="768"><a href="#768">768</a></td></tr
><tr id="gr_svn139_769"

><td id="769"><a href="#769">769</a></td></tr
><tr id="gr_svn139_770"

><td id="770"><a href="#770">770</a></td></tr
><tr id="gr_svn139_771"

><td id="771"><a href="#771">771</a></td></tr
><tr id="gr_svn139_772"

><td id="772"><a href="#772">772</a></td></tr
><tr id="gr_svn139_773"

><td id="773"><a href="#773">773</a></td></tr
><tr id="gr_svn139_774"

><td id="774"><a href="#774">774</a></td></tr
><tr id="gr_svn139_775"

><td id="775"><a href="#775">775</a></td></tr
><tr id="gr_svn139_776"

><td id="776"><a href="#776">776</a></td></tr
><tr id="gr_svn139_777"

><td id="777"><a href="#777">777</a></td></tr
><tr id="gr_svn139_778"

><td id="778"><a href="#778">778</a></td></tr
><tr id="gr_svn139_779"

><td id="779"><a href="#779">779</a></td></tr
><tr id="gr_svn139_780"

><td id="780"><a href="#780">780</a></td></tr
><tr id="gr_svn139_781"

><td id="781"><a href="#781">781</a></td></tr
><tr id="gr_svn139_782"

><td id="782"><a href="#782">782</a></td></tr
><tr id="gr_svn139_783"

><td id="783"><a href="#783">783</a></td></tr
><tr id="gr_svn139_784"

><td id="784"><a href="#784">784</a></td></tr
><tr id="gr_svn139_785"

><td id="785"><a href="#785">785</a></td></tr
><tr id="gr_svn139_786"

><td id="786"><a href="#786">786</a></td></tr
><tr id="gr_svn139_787"

><td id="787"><a href="#787">787</a></td></tr
><tr id="gr_svn139_788"

><td id="788"><a href="#788">788</a></td></tr
><tr id="gr_svn139_789"

><td id="789"><a href="#789">789</a></td></tr
><tr id="gr_svn139_790"

><td id="790"><a href="#790">790</a></td></tr
><tr id="gr_svn139_791"

><td id="791"><a href="#791">791</a></td></tr
><tr id="gr_svn139_792"

><td id="792"><a href="#792">792</a></td></tr
><tr id="gr_svn139_793"

><td id="793"><a href="#793">793</a></td></tr
><tr id="gr_svn139_794"

><td id="794"><a href="#794">794</a></td></tr
><tr id="gr_svn139_795"

><td id="795"><a href="#795">795</a></td></tr
><tr id="gr_svn139_796"

><td id="796"><a href="#796">796</a></td></tr
><tr id="gr_svn139_797"

><td id="797"><a href="#797">797</a></td></tr
><tr id="gr_svn139_798"

><td id="798"><a href="#798">798</a></td></tr
><tr id="gr_svn139_799"

><td id="799"><a href="#799">799</a></td></tr
><tr id="gr_svn139_800"

><td id="800"><a href="#800">800</a></td></tr
><tr id="gr_svn139_801"

><td id="801"><a href="#801">801</a></td></tr
><tr id="gr_svn139_802"

><td id="802"><a href="#802">802</a></td></tr
><tr id="gr_svn139_803"

><td id="803"><a href="#803">803</a></td></tr
><tr id="gr_svn139_804"

><td id="804"><a href="#804">804</a></td></tr
><tr id="gr_svn139_805"

><td id="805"><a href="#805">805</a></td></tr
><tr id="gr_svn139_806"

><td id="806"><a href="#806">806</a></td></tr
><tr id="gr_svn139_807"

><td id="807"><a href="#807">807</a></td></tr
><tr id="gr_svn139_808"

><td id="808"><a href="#808">808</a></td></tr
><tr id="gr_svn139_809"

><td id="809"><a href="#809">809</a></td></tr
><tr id="gr_svn139_810"

><td id="810"><a href="#810">810</a></td></tr
><tr id="gr_svn139_811"

><td id="811"><a href="#811">811</a></td></tr
><tr id="gr_svn139_812"

><td id="812"><a href="#812">812</a></td></tr
><tr id="gr_svn139_813"

><td id="813"><a href="#813">813</a></td></tr
><tr id="gr_svn139_814"

><td id="814"><a href="#814">814</a></td></tr
><tr id="gr_svn139_815"

><td id="815"><a href="#815">815</a></td></tr
><tr id="gr_svn139_816"

><td id="816"><a href="#816">816</a></td></tr
><tr id="gr_svn139_817"

><td id="817"><a href="#817">817</a></td></tr
><tr id="gr_svn139_818"

><td id="818"><a href="#818">818</a></td></tr
><tr id="gr_svn139_819"

><td id="819"><a href="#819">819</a></td></tr
><tr id="gr_svn139_820"

><td id="820"><a href="#820">820</a></td></tr
><tr id="gr_svn139_821"

><td id="821"><a href="#821">821</a></td></tr
><tr id="gr_svn139_822"

><td id="822"><a href="#822">822</a></td></tr
><tr id="gr_svn139_823"

><td id="823"><a href="#823">823</a></td></tr
><tr id="gr_svn139_824"

><td id="824"><a href="#824">824</a></td></tr
><tr id="gr_svn139_825"

><td id="825"><a href="#825">825</a></td></tr
><tr id="gr_svn139_826"

><td id="826"><a href="#826">826</a></td></tr
><tr id="gr_svn139_827"

><td id="827"><a href="#827">827</a></td></tr
><tr id="gr_svn139_828"

><td id="828"><a href="#828">828</a></td></tr
><tr id="gr_svn139_829"

><td id="829"><a href="#829">829</a></td></tr
><tr id="gr_svn139_830"

><td id="830"><a href="#830">830</a></td></tr
><tr id="gr_svn139_831"

><td id="831"><a href="#831">831</a></td></tr
><tr id="gr_svn139_832"

><td id="832"><a href="#832">832</a></td></tr
><tr id="gr_svn139_833"

><td id="833"><a href="#833">833</a></td></tr
><tr id="gr_svn139_834"

><td id="834"><a href="#834">834</a></td></tr
><tr id="gr_svn139_835"

><td id="835"><a href="#835">835</a></td></tr
><tr id="gr_svn139_836"

><td id="836"><a href="#836">836</a></td></tr
><tr id="gr_svn139_837"

><td id="837"><a href="#837">837</a></td></tr
><tr id="gr_svn139_838"

><td id="838"><a href="#838">838</a></td></tr
><tr id="gr_svn139_839"

><td id="839"><a href="#839">839</a></td></tr
><tr id="gr_svn139_840"

><td id="840"><a href="#840">840</a></td></tr
><tr id="gr_svn139_841"

><td id="841"><a href="#841">841</a></td></tr
><tr id="gr_svn139_842"

><td id="842"><a href="#842">842</a></td></tr
><tr id="gr_svn139_843"

><td id="843"><a href="#843">843</a></td></tr
><tr id="gr_svn139_844"

><td id="844"><a href="#844">844</a></td></tr
><tr id="gr_svn139_845"

><td id="845"><a href="#845">845</a></td></tr
><tr id="gr_svn139_846"

><td id="846"><a href="#846">846</a></td></tr
><tr id="gr_svn139_847"

><td id="847"><a href="#847">847</a></td></tr
><tr id="gr_svn139_848"

><td id="848"><a href="#848">848</a></td></tr
><tr id="gr_svn139_849"

><td id="849"><a href="#849">849</a></td></tr
><tr id="gr_svn139_850"

><td id="850"><a href="#850">850</a></td></tr
><tr id="gr_svn139_851"

><td id="851"><a href="#851">851</a></td></tr
><tr id="gr_svn139_852"

><td id="852"><a href="#852">852</a></td></tr
><tr id="gr_svn139_853"

><td id="853"><a href="#853">853</a></td></tr
><tr id="gr_svn139_854"

><td id="854"><a href="#854">854</a></td></tr
><tr id="gr_svn139_855"

><td id="855"><a href="#855">855</a></td></tr
><tr id="gr_svn139_856"

><td id="856"><a href="#856">856</a></td></tr
><tr id="gr_svn139_857"

><td id="857"><a href="#857">857</a></td></tr
><tr id="gr_svn139_858"

><td id="858"><a href="#858">858</a></td></tr
><tr id="gr_svn139_859"

><td id="859"><a href="#859">859</a></td></tr
><tr id="gr_svn139_860"

><td id="860"><a href="#860">860</a></td></tr
><tr id="gr_svn139_861"

><td id="861"><a href="#861">861</a></td></tr
><tr id="gr_svn139_862"

><td id="862"><a href="#862">862</a></td></tr
><tr id="gr_svn139_863"

><td id="863"><a href="#863">863</a></td></tr
><tr id="gr_svn139_864"

><td id="864"><a href="#864">864</a></td></tr
><tr id="gr_svn139_865"

><td id="865"><a href="#865">865</a></td></tr
><tr id="gr_svn139_866"

><td id="866"><a href="#866">866</a></td></tr
><tr id="gr_svn139_867"

><td id="867"><a href="#867">867</a></td></tr
><tr id="gr_svn139_868"

><td id="868"><a href="#868">868</a></td></tr
><tr id="gr_svn139_869"

><td id="869"><a href="#869">869</a></td></tr
><tr id="gr_svn139_870"

><td id="870"><a href="#870">870</a></td></tr
><tr id="gr_svn139_871"

><td id="871"><a href="#871">871</a></td></tr
><tr id="gr_svn139_872"

><td id="872"><a href="#872">872</a></td></tr
><tr id="gr_svn139_873"

><td id="873"><a href="#873">873</a></td></tr
><tr id="gr_svn139_874"

><td id="874"><a href="#874">874</a></td></tr
><tr id="gr_svn139_875"

><td id="875"><a href="#875">875</a></td></tr
><tr id="gr_svn139_876"

><td id="876"><a href="#876">876</a></td></tr
><tr id="gr_svn139_877"

><td id="877"><a href="#877">877</a></td></tr
><tr id="gr_svn139_878"

><td id="878"><a href="#878">878</a></td></tr
><tr id="gr_svn139_879"

><td id="879"><a href="#879">879</a></td></tr
><tr id="gr_svn139_880"

><td id="880"><a href="#880">880</a></td></tr
><tr id="gr_svn139_881"

><td id="881"><a href="#881">881</a></td></tr
><tr id="gr_svn139_882"

><td id="882"><a href="#882">882</a></td></tr
><tr id="gr_svn139_883"

><td id="883"><a href="#883">883</a></td></tr
><tr id="gr_svn139_884"

><td id="884"><a href="#884">884</a></td></tr
><tr id="gr_svn139_885"

><td id="885"><a href="#885">885</a></td></tr
><tr id="gr_svn139_886"

><td id="886"><a href="#886">886</a></td></tr
><tr id="gr_svn139_887"

><td id="887"><a href="#887">887</a></td></tr
><tr id="gr_svn139_888"

><td id="888"><a href="#888">888</a></td></tr
><tr id="gr_svn139_889"

><td id="889"><a href="#889">889</a></td></tr
><tr id="gr_svn139_890"

><td id="890"><a href="#890">890</a></td></tr
><tr id="gr_svn139_891"

><td id="891"><a href="#891">891</a></td></tr
><tr id="gr_svn139_892"

><td id="892"><a href="#892">892</a></td></tr
><tr id="gr_svn139_893"

><td id="893"><a href="#893">893</a></td></tr
><tr id="gr_svn139_894"

><td id="894"><a href="#894">894</a></td></tr
><tr id="gr_svn139_895"

><td id="895"><a href="#895">895</a></td></tr
><tr id="gr_svn139_896"

><td id="896"><a href="#896">896</a></td></tr
><tr id="gr_svn139_897"

><td id="897"><a href="#897">897</a></td></tr
><tr id="gr_svn139_898"

><td id="898"><a href="#898">898</a></td></tr
><tr id="gr_svn139_899"

><td id="899"><a href="#899">899</a></td></tr
><tr id="gr_svn139_900"

><td id="900"><a href="#900">900</a></td></tr
><tr id="gr_svn139_901"

><td id="901"><a href="#901">901</a></td></tr
><tr id="gr_svn139_902"

><td id="902"><a href="#902">902</a></td></tr
><tr id="gr_svn139_903"

><td id="903"><a href="#903">903</a></td></tr
><tr id="gr_svn139_904"

><td id="904"><a href="#904">904</a></td></tr
><tr id="gr_svn139_905"

><td id="905"><a href="#905">905</a></td></tr
><tr id="gr_svn139_906"

><td id="906"><a href="#906">906</a></td></tr
><tr id="gr_svn139_907"

><td id="907"><a href="#907">907</a></td></tr
><tr id="gr_svn139_908"

><td id="908"><a href="#908">908</a></td></tr
><tr id="gr_svn139_909"

><td id="909"><a href="#909">909</a></td></tr
><tr id="gr_svn139_910"

><td id="910"><a href="#910">910</a></td></tr
><tr id="gr_svn139_911"

><td id="911"><a href="#911">911</a></td></tr
><tr id="gr_svn139_912"

><td id="912"><a href="#912">912</a></td></tr
><tr id="gr_svn139_913"

><td id="913"><a href="#913">913</a></td></tr
><tr id="gr_svn139_914"

><td id="914"><a href="#914">914</a></td></tr
><tr id="gr_svn139_915"

><td id="915"><a href="#915">915</a></td></tr
><tr id="gr_svn139_916"

><td id="916"><a href="#916">916</a></td></tr
><tr id="gr_svn139_917"

><td id="917"><a href="#917">917</a></td></tr
><tr id="gr_svn139_918"

><td id="918"><a href="#918">918</a></td></tr
><tr id="gr_svn139_919"

><td id="919"><a href="#919">919</a></td></tr
><tr id="gr_svn139_920"

><td id="920"><a href="#920">920</a></td></tr
><tr id="gr_svn139_921"

><td id="921"><a href="#921">921</a></td></tr
><tr id="gr_svn139_922"

><td id="922"><a href="#922">922</a></td></tr
><tr id="gr_svn139_923"

><td id="923"><a href="#923">923</a></td></tr
><tr id="gr_svn139_924"

><td id="924"><a href="#924">924</a></td></tr
><tr id="gr_svn139_925"

><td id="925"><a href="#925">925</a></td></tr
><tr id="gr_svn139_926"

><td id="926"><a href="#926">926</a></td></tr
><tr id="gr_svn139_927"

><td id="927"><a href="#927">927</a></td></tr
><tr id="gr_svn139_928"

><td id="928"><a href="#928">928</a></td></tr
><tr id="gr_svn139_929"

><td id="929"><a href="#929">929</a></td></tr
><tr id="gr_svn139_930"

><td id="930"><a href="#930">930</a></td></tr
><tr id="gr_svn139_931"

><td id="931"><a href="#931">931</a></td></tr
><tr id="gr_svn139_932"

><td id="932"><a href="#932">932</a></td></tr
><tr id="gr_svn139_933"

><td id="933"><a href="#933">933</a></td></tr
><tr id="gr_svn139_934"

><td id="934"><a href="#934">934</a></td></tr
><tr id="gr_svn139_935"

><td id="935"><a href="#935">935</a></td></tr
><tr id="gr_svn139_936"

><td id="936"><a href="#936">936</a></td></tr
><tr id="gr_svn139_937"

><td id="937"><a href="#937">937</a></td></tr
><tr id="gr_svn139_938"

><td id="938"><a href="#938">938</a></td></tr
><tr id="gr_svn139_939"

><td id="939"><a href="#939">939</a></td></tr
><tr id="gr_svn139_940"

><td id="940"><a href="#940">940</a></td></tr
><tr id="gr_svn139_941"

><td id="941"><a href="#941">941</a></td></tr
><tr id="gr_svn139_942"

><td id="942"><a href="#942">942</a></td></tr
><tr id="gr_svn139_943"

><td id="943"><a href="#943">943</a></td></tr
><tr id="gr_svn139_944"

><td id="944"><a href="#944">944</a></td></tr
><tr id="gr_svn139_945"

><td id="945"><a href="#945">945</a></td></tr
><tr id="gr_svn139_946"

><td id="946"><a href="#946">946</a></td></tr
><tr id="gr_svn139_947"

><td id="947"><a href="#947">947</a></td></tr
><tr id="gr_svn139_948"

><td id="948"><a href="#948">948</a></td></tr
><tr id="gr_svn139_949"

><td id="949"><a href="#949">949</a></td></tr
><tr id="gr_svn139_950"

><td id="950"><a href="#950">950</a></td></tr
><tr id="gr_svn139_951"

><td id="951"><a href="#951">951</a></td></tr
><tr id="gr_svn139_952"

><td id="952"><a href="#952">952</a></td></tr
><tr id="gr_svn139_953"

><td id="953"><a href="#953">953</a></td></tr
><tr id="gr_svn139_954"

><td id="954"><a href="#954">954</a></td></tr
><tr id="gr_svn139_955"

><td id="955"><a href="#955">955</a></td></tr
><tr id="gr_svn139_956"

><td id="956"><a href="#956">956</a></td></tr
><tr id="gr_svn139_957"

><td id="957"><a href="#957">957</a></td></tr
><tr id="gr_svn139_958"

><td id="958"><a href="#958">958</a></td></tr
><tr id="gr_svn139_959"

><td id="959"><a href="#959">959</a></td></tr
><tr id="gr_svn139_960"

><td id="960"><a href="#960">960</a></td></tr
><tr id="gr_svn139_961"

><td id="961"><a href="#961">961</a></td></tr
><tr id="gr_svn139_962"

><td id="962"><a href="#962">962</a></td></tr
><tr id="gr_svn139_963"

><td id="963"><a href="#963">963</a></td></tr
><tr id="gr_svn139_964"

><td id="964"><a href="#964">964</a></td></tr
><tr id="gr_svn139_965"

><td id="965"><a href="#965">965</a></td></tr
><tr id="gr_svn139_966"

><td id="966"><a href="#966">966</a></td></tr
><tr id="gr_svn139_967"

><td id="967"><a href="#967">967</a></td></tr
><tr id="gr_svn139_968"

><td id="968"><a href="#968">968</a></td></tr
><tr id="gr_svn139_969"

><td id="969"><a href="#969">969</a></td></tr
><tr id="gr_svn139_970"

><td id="970"><a href="#970">970</a></td></tr
><tr id="gr_svn139_971"

><td id="971"><a href="#971">971</a></td></tr
><tr id="gr_svn139_972"

><td id="972"><a href="#972">972</a></td></tr
><tr id="gr_svn139_973"

><td id="973"><a href="#973">973</a></td></tr
><tr id="gr_svn139_974"

><td id="974"><a href="#974">974</a></td></tr
><tr id="gr_svn139_975"

><td id="975"><a href="#975">975</a></td></tr
><tr id="gr_svn139_976"

><td id="976"><a href="#976">976</a></td></tr
><tr id="gr_svn139_977"

><td id="977"><a href="#977">977</a></td></tr
><tr id="gr_svn139_978"

><td id="978"><a href="#978">978</a></td></tr
><tr id="gr_svn139_979"

><td id="979"><a href="#979">979</a></td></tr
><tr id="gr_svn139_980"

><td id="980"><a href="#980">980</a></td></tr
><tr id="gr_svn139_981"

><td id="981"><a href="#981">981</a></td></tr
><tr id="gr_svn139_982"

><td id="982"><a href="#982">982</a></td></tr
><tr id="gr_svn139_983"

><td id="983"><a href="#983">983</a></td></tr
><tr id="gr_svn139_984"

><td id="984"><a href="#984">984</a></td></tr
><tr id="gr_svn139_985"

><td id="985"><a href="#985">985</a></td></tr
><tr id="gr_svn139_986"

><td id="986"><a href="#986">986</a></td></tr
><tr id="gr_svn139_987"

><td id="987"><a href="#987">987</a></td></tr
><tr id="gr_svn139_988"

><td id="988"><a href="#988">988</a></td></tr
><tr id="gr_svn139_989"

><td id="989"><a href="#989">989</a></td></tr
><tr id="gr_svn139_990"

><td id="990"><a href="#990">990</a></td></tr
><tr id="gr_svn139_991"

><td id="991"><a href="#991">991</a></td></tr
><tr id="gr_svn139_992"

><td id="992"><a href="#992">992</a></td></tr
><tr id="gr_svn139_993"

><td id="993"><a href="#993">993</a></td></tr
><tr id="gr_svn139_994"

><td id="994"><a href="#994">994</a></td></tr
><tr id="gr_svn139_995"

><td id="995"><a href="#995">995</a></td></tr
><tr id="gr_svn139_996"

><td id="996"><a href="#996">996</a></td></tr
><tr id="gr_svn139_997"

><td id="997"><a href="#997">997</a></td></tr
><tr id="gr_svn139_998"

><td id="998"><a href="#998">998</a></td></tr
><tr id="gr_svn139_999"

><td id="999"><a href="#999">999</a></td></tr
><tr id="gr_svn139_1000"

><td id="1000"><a href="#1000">1000</a></td></tr
><tr id="gr_svn139_1001"

><td id="1001"><a href="#1001">1001</a></td></tr
><tr id="gr_svn139_1002"

><td id="1002"><a href="#1002">1002</a></td></tr
><tr id="gr_svn139_1003"

><td id="1003"><a href="#1003">1003</a></td></tr
><tr id="gr_svn139_1004"

><td id="1004"><a href="#1004">1004</a></td></tr
><tr id="gr_svn139_1005"

><td id="1005"><a href="#1005">1005</a></td></tr
><tr id="gr_svn139_1006"

><td id="1006"><a href="#1006">1006</a></td></tr
><tr id="gr_svn139_1007"

><td id="1007"><a href="#1007">1007</a></td></tr
><tr id="gr_svn139_1008"

><td id="1008"><a href="#1008">1008</a></td></tr
><tr id="gr_svn139_1009"

><td id="1009"><a href="#1009">1009</a></td></tr
><tr id="gr_svn139_1010"

><td id="1010"><a href="#1010">1010</a></td></tr
><tr id="gr_svn139_1011"

><td id="1011"><a href="#1011">1011</a></td></tr
><tr id="gr_svn139_1012"

><td id="1012"><a href="#1012">1012</a></td></tr
><tr id="gr_svn139_1013"

><td id="1013"><a href="#1013">1013</a></td></tr
><tr id="gr_svn139_1014"

><td id="1014"><a href="#1014">1014</a></td></tr
><tr id="gr_svn139_1015"

><td id="1015"><a href="#1015">1015</a></td></tr
><tr id="gr_svn139_1016"

><td id="1016"><a href="#1016">1016</a></td></tr
><tr id="gr_svn139_1017"

><td id="1017"><a href="#1017">1017</a></td></tr
><tr id="gr_svn139_1018"

><td id="1018"><a href="#1018">1018</a></td></tr
><tr id="gr_svn139_1019"

><td id="1019"><a href="#1019">1019</a></td></tr
><tr id="gr_svn139_1020"

><td id="1020"><a href="#1020">1020</a></td></tr
><tr id="gr_svn139_1021"

><td id="1021"><a href="#1021">1021</a></td></tr
><tr id="gr_svn139_1022"

><td id="1022"><a href="#1022">1022</a></td></tr
><tr id="gr_svn139_1023"

><td id="1023"><a href="#1023">1023</a></td></tr
><tr id="gr_svn139_1024"

><td id="1024"><a href="#1024">1024</a></td></tr
><tr id="gr_svn139_1025"

><td id="1025"><a href="#1025">1025</a></td></tr
><tr id="gr_svn139_1026"

><td id="1026"><a href="#1026">1026</a></td></tr
><tr id="gr_svn139_1027"

><td id="1027"><a href="#1027">1027</a></td></tr
><tr id="gr_svn139_1028"

><td id="1028"><a href="#1028">1028</a></td></tr
><tr id="gr_svn139_1029"

><td id="1029"><a href="#1029">1029</a></td></tr
><tr id="gr_svn139_1030"

><td id="1030"><a href="#1030">1030</a></td></tr
><tr id="gr_svn139_1031"

><td id="1031"><a href="#1031">1031</a></td></tr
><tr id="gr_svn139_1032"

><td id="1032"><a href="#1032">1032</a></td></tr
><tr id="gr_svn139_1033"

><td id="1033"><a href="#1033">1033</a></td></tr
><tr id="gr_svn139_1034"

><td id="1034"><a href="#1034">1034</a></td></tr
><tr id="gr_svn139_1035"

><td id="1035"><a href="#1035">1035</a></td></tr
><tr id="gr_svn139_1036"

><td id="1036"><a href="#1036">1036</a></td></tr
><tr id="gr_svn139_1037"

><td id="1037"><a href="#1037">1037</a></td></tr
><tr id="gr_svn139_1038"

><td id="1038"><a href="#1038">1038</a></td></tr
><tr id="gr_svn139_1039"

><td id="1039"><a href="#1039">1039</a></td></tr
><tr id="gr_svn139_1040"

><td id="1040"><a href="#1040">1040</a></td></tr
><tr id="gr_svn139_1041"

><td id="1041"><a href="#1041">1041</a></td></tr
><tr id="gr_svn139_1042"

><td id="1042"><a href="#1042">1042</a></td></tr
><tr id="gr_svn139_1043"

><td id="1043"><a href="#1043">1043</a></td></tr
><tr id="gr_svn139_1044"

><td id="1044"><a href="#1044">1044</a></td></tr
><tr id="gr_svn139_1045"

><td id="1045"><a href="#1045">1045</a></td></tr
><tr id="gr_svn139_1046"

><td id="1046"><a href="#1046">1046</a></td></tr
><tr id="gr_svn139_1047"

><td id="1047"><a href="#1047">1047</a></td></tr
><tr id="gr_svn139_1048"

><td id="1048"><a href="#1048">1048</a></td></tr
><tr id="gr_svn139_1049"

><td id="1049"><a href="#1049">1049</a></td></tr
><tr id="gr_svn139_1050"

><td id="1050"><a href="#1050">1050</a></td></tr
><tr id="gr_svn139_1051"

><td id="1051"><a href="#1051">1051</a></td></tr
><tr id="gr_svn139_1052"

><td id="1052"><a href="#1052">1052</a></td></tr
><tr id="gr_svn139_1053"

><td id="1053"><a href="#1053">1053</a></td></tr
><tr id="gr_svn139_1054"

><td id="1054"><a href="#1054">1054</a></td></tr
><tr id="gr_svn139_1055"

><td id="1055"><a href="#1055">1055</a></td></tr
><tr id="gr_svn139_1056"

><td id="1056"><a href="#1056">1056</a></td></tr
><tr id="gr_svn139_1057"

><td id="1057"><a href="#1057">1057</a></td></tr
><tr id="gr_svn139_1058"

><td id="1058"><a href="#1058">1058</a></td></tr
><tr id="gr_svn139_1059"

><td id="1059"><a href="#1059">1059</a></td></tr
><tr id="gr_svn139_1060"

><td id="1060"><a href="#1060">1060</a></td></tr
><tr id="gr_svn139_1061"

><td id="1061"><a href="#1061">1061</a></td></tr
><tr id="gr_svn139_1062"

><td id="1062"><a href="#1062">1062</a></td></tr
><tr id="gr_svn139_1063"

><td id="1063"><a href="#1063">1063</a></td></tr
><tr id="gr_svn139_1064"

><td id="1064"><a href="#1064">1064</a></td></tr
><tr id="gr_svn139_1065"

><td id="1065"><a href="#1065">1065</a></td></tr
><tr id="gr_svn139_1066"

><td id="1066"><a href="#1066">1066</a></td></tr
><tr id="gr_svn139_1067"

><td id="1067"><a href="#1067">1067</a></td></tr
><tr id="gr_svn139_1068"

><td id="1068"><a href="#1068">1068</a></td></tr
><tr id="gr_svn139_1069"

><td id="1069"><a href="#1069">1069</a></td></tr
><tr id="gr_svn139_1070"

><td id="1070"><a href="#1070">1070</a></td></tr
><tr id="gr_svn139_1071"

><td id="1071"><a href="#1071">1071</a></td></tr
><tr id="gr_svn139_1072"

><td id="1072"><a href="#1072">1072</a></td></tr
><tr id="gr_svn139_1073"

><td id="1073"><a href="#1073">1073</a></td></tr
><tr id="gr_svn139_1074"

><td id="1074"><a href="#1074">1074</a></td></tr
><tr id="gr_svn139_1075"

><td id="1075"><a href="#1075">1075</a></td></tr
><tr id="gr_svn139_1076"

><td id="1076"><a href="#1076">1076</a></td></tr
><tr id="gr_svn139_1077"

><td id="1077"><a href="#1077">1077</a></td></tr
><tr id="gr_svn139_1078"

><td id="1078"><a href="#1078">1078</a></td></tr
><tr id="gr_svn139_1079"

><td id="1079"><a href="#1079">1079</a></td></tr
><tr id="gr_svn139_1080"

><td id="1080"><a href="#1080">1080</a></td></tr
><tr id="gr_svn139_1081"

><td id="1081"><a href="#1081">1081</a></td></tr
><tr id="gr_svn139_1082"

><td id="1082"><a href="#1082">1082</a></td></tr
><tr id="gr_svn139_1083"

><td id="1083"><a href="#1083">1083</a></td></tr
><tr id="gr_svn139_1084"

><td id="1084"><a href="#1084">1084</a></td></tr
><tr id="gr_svn139_1085"

><td id="1085"><a href="#1085">1085</a></td></tr
><tr id="gr_svn139_1086"

><td id="1086"><a href="#1086">1086</a></td></tr
><tr id="gr_svn139_1087"

><td id="1087"><a href="#1087">1087</a></td></tr
><tr id="gr_svn139_1088"

><td id="1088"><a href="#1088">1088</a></td></tr
><tr id="gr_svn139_1089"

><td id="1089"><a href="#1089">1089</a></td></tr
><tr id="gr_svn139_1090"

><td id="1090"><a href="#1090">1090</a></td></tr
><tr id="gr_svn139_1091"

><td id="1091"><a href="#1091">1091</a></td></tr
><tr id="gr_svn139_1092"

><td id="1092"><a href="#1092">1092</a></td></tr
><tr id="gr_svn139_1093"

><td id="1093"><a href="#1093">1093</a></td></tr
><tr id="gr_svn139_1094"

><td id="1094"><a href="#1094">1094</a></td></tr
><tr id="gr_svn139_1095"

><td id="1095"><a href="#1095">1095</a></td></tr
><tr id="gr_svn139_1096"

><td id="1096"><a href="#1096">1096</a></td></tr
><tr id="gr_svn139_1097"

><td id="1097"><a href="#1097">1097</a></td></tr
><tr id="gr_svn139_1098"

><td id="1098"><a href="#1098">1098</a></td></tr
><tr id="gr_svn139_1099"

><td id="1099"><a href="#1099">1099</a></td></tr
><tr id="gr_svn139_1100"

><td id="1100"><a href="#1100">1100</a></td></tr
><tr id="gr_svn139_1101"

><td id="1101"><a href="#1101">1101</a></td></tr
><tr id="gr_svn139_1102"

><td id="1102"><a href="#1102">1102</a></td></tr
><tr id="gr_svn139_1103"

><td id="1103"><a href="#1103">1103</a></td></tr
><tr id="gr_svn139_1104"

><td id="1104"><a href="#1104">1104</a></td></tr
><tr id="gr_svn139_1105"

><td id="1105"><a href="#1105">1105</a></td></tr
><tr id="gr_svn139_1106"

><td id="1106"><a href="#1106">1106</a></td></tr
><tr id="gr_svn139_1107"

><td id="1107"><a href="#1107">1107</a></td></tr
><tr id="gr_svn139_1108"

><td id="1108"><a href="#1108">1108</a></td></tr
><tr id="gr_svn139_1109"

><td id="1109"><a href="#1109">1109</a></td></tr
><tr id="gr_svn139_1110"

><td id="1110"><a href="#1110">1110</a></td></tr
><tr id="gr_svn139_1111"

><td id="1111"><a href="#1111">1111</a></td></tr
><tr id="gr_svn139_1112"

><td id="1112"><a href="#1112">1112</a></td></tr
><tr id="gr_svn139_1113"

><td id="1113"><a href="#1113">1113</a></td></tr
><tr id="gr_svn139_1114"

><td id="1114"><a href="#1114">1114</a></td></tr
><tr id="gr_svn139_1115"

><td id="1115"><a href="#1115">1115</a></td></tr
><tr id="gr_svn139_1116"

><td id="1116"><a href="#1116">1116</a></td></tr
><tr id="gr_svn139_1117"

><td id="1117"><a href="#1117">1117</a></td></tr
><tr id="gr_svn139_1118"

><td id="1118"><a href="#1118">1118</a></td></tr
><tr id="gr_svn139_1119"

><td id="1119"><a href="#1119">1119</a></td></tr
><tr id="gr_svn139_1120"

><td id="1120"><a href="#1120">1120</a></td></tr
><tr id="gr_svn139_1121"

><td id="1121"><a href="#1121">1121</a></td></tr
><tr id="gr_svn139_1122"

><td id="1122"><a href="#1122">1122</a></td></tr
><tr id="gr_svn139_1123"

><td id="1123"><a href="#1123">1123</a></td></tr
><tr id="gr_svn139_1124"

><td id="1124"><a href="#1124">1124</a></td></tr
><tr id="gr_svn139_1125"

><td id="1125"><a href="#1125">1125</a></td></tr
><tr id="gr_svn139_1126"

><td id="1126"><a href="#1126">1126</a></td></tr
><tr id="gr_svn139_1127"

><td id="1127"><a href="#1127">1127</a></td></tr
><tr id="gr_svn139_1128"

><td id="1128"><a href="#1128">1128</a></td></tr
><tr id="gr_svn139_1129"

><td id="1129"><a href="#1129">1129</a></td></tr
><tr id="gr_svn139_1130"

><td id="1130"><a href="#1130">1130</a></td></tr
><tr id="gr_svn139_1131"

><td id="1131"><a href="#1131">1131</a></td></tr
><tr id="gr_svn139_1132"

><td id="1132"><a href="#1132">1132</a></td></tr
><tr id="gr_svn139_1133"

><td id="1133"><a href="#1133">1133</a></td></tr
><tr id="gr_svn139_1134"

><td id="1134"><a href="#1134">1134</a></td></tr
><tr id="gr_svn139_1135"

><td id="1135"><a href="#1135">1135</a></td></tr
><tr id="gr_svn139_1136"

><td id="1136"><a href="#1136">1136</a></td></tr
><tr id="gr_svn139_1137"

><td id="1137"><a href="#1137">1137</a></td></tr
><tr id="gr_svn139_1138"

><td id="1138"><a href="#1138">1138</a></td></tr
><tr id="gr_svn139_1139"

><td id="1139"><a href="#1139">1139</a></td></tr
><tr id="gr_svn139_1140"

><td id="1140"><a href="#1140">1140</a></td></tr
><tr id="gr_svn139_1141"

><td id="1141"><a href="#1141">1141</a></td></tr
><tr id="gr_svn139_1142"

><td id="1142"><a href="#1142">1142</a></td></tr
><tr id="gr_svn139_1143"

><td id="1143"><a href="#1143">1143</a></td></tr
><tr id="gr_svn139_1144"

><td id="1144"><a href="#1144">1144</a></td></tr
><tr id="gr_svn139_1145"

><td id="1145"><a href="#1145">1145</a></td></tr
><tr id="gr_svn139_1146"

><td id="1146"><a href="#1146">1146</a></td></tr
><tr id="gr_svn139_1147"

><td id="1147"><a href="#1147">1147</a></td></tr
><tr id="gr_svn139_1148"

><td id="1148"><a href="#1148">1148</a></td></tr
><tr id="gr_svn139_1149"

><td id="1149"><a href="#1149">1149</a></td></tr
><tr id="gr_svn139_1150"

><td id="1150"><a href="#1150">1150</a></td></tr
><tr id="gr_svn139_1151"

><td id="1151"><a href="#1151">1151</a></td></tr
><tr id="gr_svn139_1152"

><td id="1152"><a href="#1152">1152</a></td></tr
><tr id="gr_svn139_1153"

><td id="1153"><a href="#1153">1153</a></td></tr
><tr id="gr_svn139_1154"

><td id="1154"><a href="#1154">1154</a></td></tr
><tr id="gr_svn139_1155"

><td id="1155"><a href="#1155">1155</a></td></tr
><tr id="gr_svn139_1156"

><td id="1156"><a href="#1156">1156</a></td></tr
><tr id="gr_svn139_1157"

><td id="1157"><a href="#1157">1157</a></td></tr
><tr id="gr_svn139_1158"

><td id="1158"><a href="#1158">1158</a></td></tr
><tr id="gr_svn139_1159"

><td id="1159"><a href="#1159">1159</a></td></tr
><tr id="gr_svn139_1160"

><td id="1160"><a href="#1160">1160</a></td></tr
><tr id="gr_svn139_1161"

><td id="1161"><a href="#1161">1161</a></td></tr
><tr id="gr_svn139_1162"

><td id="1162"><a href="#1162">1162</a></td></tr
><tr id="gr_svn139_1163"

><td id="1163"><a href="#1163">1163</a></td></tr
><tr id="gr_svn139_1164"

><td id="1164"><a href="#1164">1164</a></td></tr
><tr id="gr_svn139_1165"

><td id="1165"><a href="#1165">1165</a></td></tr
><tr id="gr_svn139_1166"

><td id="1166"><a href="#1166">1166</a></td></tr
><tr id="gr_svn139_1167"

><td id="1167"><a href="#1167">1167</a></td></tr
><tr id="gr_svn139_1168"

><td id="1168"><a href="#1168">1168</a></td></tr
><tr id="gr_svn139_1169"

><td id="1169"><a href="#1169">1169</a></td></tr
><tr id="gr_svn139_1170"

><td id="1170"><a href="#1170">1170</a></td></tr
><tr id="gr_svn139_1171"

><td id="1171"><a href="#1171">1171</a></td></tr
><tr id="gr_svn139_1172"

><td id="1172"><a href="#1172">1172</a></td></tr
><tr id="gr_svn139_1173"

><td id="1173"><a href="#1173">1173</a></td></tr
><tr id="gr_svn139_1174"

><td id="1174"><a href="#1174">1174</a></td></tr
><tr id="gr_svn139_1175"

><td id="1175"><a href="#1175">1175</a></td></tr
><tr id="gr_svn139_1176"

><td id="1176"><a href="#1176">1176</a></td></tr
><tr id="gr_svn139_1177"

><td id="1177"><a href="#1177">1177</a></td></tr
><tr id="gr_svn139_1178"

><td id="1178"><a href="#1178">1178</a></td></tr
><tr id="gr_svn139_1179"

><td id="1179"><a href="#1179">1179</a></td></tr
><tr id="gr_svn139_1180"

><td id="1180"><a href="#1180">1180</a></td></tr
><tr id="gr_svn139_1181"

><td id="1181"><a href="#1181">1181</a></td></tr
><tr id="gr_svn139_1182"

><td id="1182"><a href="#1182">1182</a></td></tr
><tr id="gr_svn139_1183"

><td id="1183"><a href="#1183">1183</a></td></tr
><tr id="gr_svn139_1184"

><td id="1184"><a href="#1184">1184</a></td></tr
><tr id="gr_svn139_1185"

><td id="1185"><a href="#1185">1185</a></td></tr
><tr id="gr_svn139_1186"

><td id="1186"><a href="#1186">1186</a></td></tr
><tr id="gr_svn139_1187"

><td id="1187"><a href="#1187">1187</a></td></tr
><tr id="gr_svn139_1188"

><td id="1188"><a href="#1188">1188</a></td></tr
><tr id="gr_svn139_1189"

><td id="1189"><a href="#1189">1189</a></td></tr
><tr id="gr_svn139_1190"

><td id="1190"><a href="#1190">1190</a></td></tr
><tr id="gr_svn139_1191"

><td id="1191"><a href="#1191">1191</a></td></tr
><tr id="gr_svn139_1192"

><td id="1192"><a href="#1192">1192</a></td></tr
><tr id="gr_svn139_1193"

><td id="1193"><a href="#1193">1193</a></td></tr
><tr id="gr_svn139_1194"

><td id="1194"><a href="#1194">1194</a></td></tr
><tr id="gr_svn139_1195"

><td id="1195"><a href="#1195">1195</a></td></tr
><tr id="gr_svn139_1196"

><td id="1196"><a href="#1196">1196</a></td></tr
><tr id="gr_svn139_1197"

><td id="1197"><a href="#1197">1197</a></td></tr
><tr id="gr_svn139_1198"

><td id="1198"><a href="#1198">1198</a></td></tr
><tr id="gr_svn139_1199"

><td id="1199"><a href="#1199">1199</a></td></tr
><tr id="gr_svn139_1200"

><td id="1200"><a href="#1200">1200</a></td></tr
><tr id="gr_svn139_1201"

><td id="1201"><a href="#1201">1201</a></td></tr
><tr id="gr_svn139_1202"

><td id="1202"><a href="#1202">1202</a></td></tr
><tr id="gr_svn139_1203"

><td id="1203"><a href="#1203">1203</a></td></tr
><tr id="gr_svn139_1204"

><td id="1204"><a href="#1204">1204</a></td></tr
><tr id="gr_svn139_1205"

><td id="1205"><a href="#1205">1205</a></td></tr
><tr id="gr_svn139_1206"

><td id="1206"><a href="#1206">1206</a></td></tr
><tr id="gr_svn139_1207"

><td id="1207"><a href="#1207">1207</a></td></tr
><tr id="gr_svn139_1208"

><td id="1208"><a href="#1208">1208</a></td></tr
><tr id="gr_svn139_1209"

><td id="1209"><a href="#1209">1209</a></td></tr
><tr id="gr_svn139_1210"

><td id="1210"><a href="#1210">1210</a></td></tr
><tr id="gr_svn139_1211"

><td id="1211"><a href="#1211">1211</a></td></tr
><tr id="gr_svn139_1212"

><td id="1212"><a href="#1212">1212</a></td></tr
><tr id="gr_svn139_1213"

><td id="1213"><a href="#1213">1213</a></td></tr
><tr id="gr_svn139_1214"

><td id="1214"><a href="#1214">1214</a></td></tr
><tr id="gr_svn139_1215"

><td id="1215"><a href="#1215">1215</a></td></tr
><tr id="gr_svn139_1216"

><td id="1216"><a href="#1216">1216</a></td></tr
><tr id="gr_svn139_1217"

><td id="1217"><a href="#1217">1217</a></td></tr
><tr id="gr_svn139_1218"

><td id="1218"><a href="#1218">1218</a></td></tr
><tr id="gr_svn139_1219"

><td id="1219"><a href="#1219">1219</a></td></tr
><tr id="gr_svn139_1220"

><td id="1220"><a href="#1220">1220</a></td></tr
><tr id="gr_svn139_1221"

><td id="1221"><a href="#1221">1221</a></td></tr
><tr id="gr_svn139_1222"

><td id="1222"><a href="#1222">1222</a></td></tr
><tr id="gr_svn139_1223"

><td id="1223"><a href="#1223">1223</a></td></tr
><tr id="gr_svn139_1224"

><td id="1224"><a href="#1224">1224</a></td></tr
><tr id="gr_svn139_1225"

><td id="1225"><a href="#1225">1225</a></td></tr
><tr id="gr_svn139_1226"

><td id="1226"><a href="#1226">1226</a></td></tr
><tr id="gr_svn139_1227"

><td id="1227"><a href="#1227">1227</a></td></tr
><tr id="gr_svn139_1228"

><td id="1228"><a href="#1228">1228</a></td></tr
><tr id="gr_svn139_1229"

><td id="1229"><a href="#1229">1229</a></td></tr
><tr id="gr_svn139_1230"

><td id="1230"><a href="#1230">1230</a></td></tr
><tr id="gr_svn139_1231"

><td id="1231"><a href="#1231">1231</a></td></tr
><tr id="gr_svn139_1232"

><td id="1232"><a href="#1232">1232</a></td></tr
><tr id="gr_svn139_1233"

><td id="1233"><a href="#1233">1233</a></td></tr
><tr id="gr_svn139_1234"

><td id="1234"><a href="#1234">1234</a></td></tr
><tr id="gr_svn139_1235"

><td id="1235"><a href="#1235">1235</a></td></tr
><tr id="gr_svn139_1236"

><td id="1236"><a href="#1236">1236</a></td></tr
><tr id="gr_svn139_1237"

><td id="1237"><a href="#1237">1237</a></td></tr
><tr id="gr_svn139_1238"

><td id="1238"><a href="#1238">1238</a></td></tr
><tr id="gr_svn139_1239"

><td id="1239"><a href="#1239">1239</a></td></tr
><tr id="gr_svn139_1240"

><td id="1240"><a href="#1240">1240</a></td></tr
><tr id="gr_svn139_1241"

><td id="1241"><a href="#1241">1241</a></td></tr
><tr id="gr_svn139_1242"

><td id="1242"><a href="#1242">1242</a></td></tr
><tr id="gr_svn139_1243"

><td id="1243"><a href="#1243">1243</a></td></tr
><tr id="gr_svn139_1244"

><td id="1244"><a href="#1244">1244</a></td></tr
><tr id="gr_svn139_1245"

><td id="1245"><a href="#1245">1245</a></td></tr
><tr id="gr_svn139_1246"

><td id="1246"><a href="#1246">1246</a></td></tr
><tr id="gr_svn139_1247"

><td id="1247"><a href="#1247">1247</a></td></tr
><tr id="gr_svn139_1248"

><td id="1248"><a href="#1248">1248</a></td></tr
><tr id="gr_svn139_1249"

><td id="1249"><a href="#1249">1249</a></td></tr
><tr id="gr_svn139_1250"

><td id="1250"><a href="#1250">1250</a></td></tr
><tr id="gr_svn139_1251"

><td id="1251"><a href="#1251">1251</a></td></tr
><tr id="gr_svn139_1252"

><td id="1252"><a href="#1252">1252</a></td></tr
><tr id="gr_svn139_1253"

><td id="1253"><a href="#1253">1253</a></td></tr
><tr id="gr_svn139_1254"

><td id="1254"><a href="#1254">1254</a></td></tr
><tr id="gr_svn139_1255"

><td id="1255"><a href="#1255">1255</a></td></tr
><tr id="gr_svn139_1256"

><td id="1256"><a href="#1256">1256</a></td></tr
><tr id="gr_svn139_1257"

><td id="1257"><a href="#1257">1257</a></td></tr
><tr id="gr_svn139_1258"

><td id="1258"><a href="#1258">1258</a></td></tr
><tr id="gr_svn139_1259"

><td id="1259"><a href="#1259">1259</a></td></tr
><tr id="gr_svn139_1260"

><td id="1260"><a href="#1260">1260</a></td></tr
><tr id="gr_svn139_1261"

><td id="1261"><a href="#1261">1261</a></td></tr
><tr id="gr_svn139_1262"

><td id="1262"><a href="#1262">1262</a></td></tr
><tr id="gr_svn139_1263"

><td id="1263"><a href="#1263">1263</a></td></tr
><tr id="gr_svn139_1264"

><td id="1264"><a href="#1264">1264</a></td></tr
><tr id="gr_svn139_1265"

><td id="1265"><a href="#1265">1265</a></td></tr
><tr id="gr_svn139_1266"

><td id="1266"><a href="#1266">1266</a></td></tr
><tr id="gr_svn139_1267"

><td id="1267"><a href="#1267">1267</a></td></tr
><tr id="gr_svn139_1268"

><td id="1268"><a href="#1268">1268</a></td></tr
><tr id="gr_svn139_1269"

><td id="1269"><a href="#1269">1269</a></td></tr
><tr id="gr_svn139_1270"

><td id="1270"><a href="#1270">1270</a></td></tr
><tr id="gr_svn139_1271"

><td id="1271"><a href="#1271">1271</a></td></tr
><tr id="gr_svn139_1272"

><td id="1272"><a href="#1272">1272</a></td></tr
><tr id="gr_svn139_1273"

><td id="1273"><a href="#1273">1273</a></td></tr
><tr id="gr_svn139_1274"

><td id="1274"><a href="#1274">1274</a></td></tr
><tr id="gr_svn139_1275"

><td id="1275"><a href="#1275">1275</a></td></tr
><tr id="gr_svn139_1276"

><td id="1276"><a href="#1276">1276</a></td></tr
><tr id="gr_svn139_1277"

><td id="1277"><a href="#1277">1277</a></td></tr
><tr id="gr_svn139_1278"

><td id="1278"><a href="#1278">1278</a></td></tr
><tr id="gr_svn139_1279"

><td id="1279"><a href="#1279">1279</a></td></tr
><tr id="gr_svn139_1280"

><td id="1280"><a href="#1280">1280</a></td></tr
><tr id="gr_svn139_1281"

><td id="1281"><a href="#1281">1281</a></td></tr
><tr id="gr_svn139_1282"

><td id="1282"><a href="#1282">1282</a></td></tr
><tr id="gr_svn139_1283"

><td id="1283"><a href="#1283">1283</a></td></tr
><tr id="gr_svn139_1284"

><td id="1284"><a href="#1284">1284</a></td></tr
><tr id="gr_svn139_1285"

><td id="1285"><a href="#1285">1285</a></td></tr
><tr id="gr_svn139_1286"

><td id="1286"><a href="#1286">1286</a></td></tr
><tr id="gr_svn139_1287"

><td id="1287"><a href="#1287">1287</a></td></tr
><tr id="gr_svn139_1288"

><td id="1288"><a href="#1288">1288</a></td></tr
><tr id="gr_svn139_1289"

><td id="1289"><a href="#1289">1289</a></td></tr
><tr id="gr_svn139_1290"

><td id="1290"><a href="#1290">1290</a></td></tr
><tr id="gr_svn139_1291"

><td id="1291"><a href="#1291">1291</a></td></tr
><tr id="gr_svn139_1292"

><td id="1292"><a href="#1292">1292</a></td></tr
><tr id="gr_svn139_1293"

><td id="1293"><a href="#1293">1293</a></td></tr
><tr id="gr_svn139_1294"

><td id="1294"><a href="#1294">1294</a></td></tr
><tr id="gr_svn139_1295"

><td id="1295"><a href="#1295">1295</a></td></tr
><tr id="gr_svn139_1296"

><td id="1296"><a href="#1296">1296</a></td></tr
><tr id="gr_svn139_1297"

><td id="1297"><a href="#1297">1297</a></td></tr
><tr id="gr_svn139_1298"

><td id="1298"><a href="#1298">1298</a></td></tr
><tr id="gr_svn139_1299"

><td id="1299"><a href="#1299">1299</a></td></tr
><tr id="gr_svn139_1300"

><td id="1300"><a href="#1300">1300</a></td></tr
><tr id="gr_svn139_1301"

><td id="1301"><a href="#1301">1301</a></td></tr
><tr id="gr_svn139_1302"

><td id="1302"><a href="#1302">1302</a></td></tr
><tr id="gr_svn139_1303"

><td id="1303"><a href="#1303">1303</a></td></tr
><tr id="gr_svn139_1304"

><td id="1304"><a href="#1304">1304</a></td></tr
><tr id="gr_svn139_1305"

><td id="1305"><a href="#1305">1305</a></td></tr
><tr id="gr_svn139_1306"

><td id="1306"><a href="#1306">1306</a></td></tr
><tr id="gr_svn139_1307"

><td id="1307"><a href="#1307">1307</a></td></tr
><tr id="gr_svn139_1308"

><td id="1308"><a href="#1308">1308</a></td></tr
><tr id="gr_svn139_1309"

><td id="1309"><a href="#1309">1309</a></td></tr
><tr id="gr_svn139_1310"

><td id="1310"><a href="#1310">1310</a></td></tr
><tr id="gr_svn139_1311"

><td id="1311"><a href="#1311">1311</a></td></tr
><tr id="gr_svn139_1312"

><td id="1312"><a href="#1312">1312</a></td></tr
><tr id="gr_svn139_1313"

><td id="1313"><a href="#1313">1313</a></td></tr
><tr id="gr_svn139_1314"

><td id="1314"><a href="#1314">1314</a></td></tr
><tr id="gr_svn139_1315"

><td id="1315"><a href="#1315">1315</a></td></tr
><tr id="gr_svn139_1316"

><td id="1316"><a href="#1316">1316</a></td></tr
><tr id="gr_svn139_1317"

><td id="1317"><a href="#1317">1317</a></td></tr
><tr id="gr_svn139_1318"

><td id="1318"><a href="#1318">1318</a></td></tr
><tr id="gr_svn139_1319"

><td id="1319"><a href="#1319">1319</a></td></tr
><tr id="gr_svn139_1320"

><td id="1320"><a href="#1320">1320</a></td></tr
><tr id="gr_svn139_1321"

><td id="1321"><a href="#1321">1321</a></td></tr
><tr id="gr_svn139_1322"

><td id="1322"><a href="#1322">1322</a></td></tr
><tr id="gr_svn139_1323"

><td id="1323"><a href="#1323">1323</a></td></tr
><tr id="gr_svn139_1324"

><td id="1324"><a href="#1324">1324</a></td></tr
><tr id="gr_svn139_1325"

><td id="1325"><a href="#1325">1325</a></td></tr
><tr id="gr_svn139_1326"

><td id="1326"><a href="#1326">1326</a></td></tr
><tr id="gr_svn139_1327"

><td id="1327"><a href="#1327">1327</a></td></tr
><tr id="gr_svn139_1328"

><td id="1328"><a href="#1328">1328</a></td></tr
><tr id="gr_svn139_1329"

><td id="1329"><a href="#1329">1329</a></td></tr
><tr id="gr_svn139_1330"

><td id="1330"><a href="#1330">1330</a></td></tr
><tr id="gr_svn139_1331"

><td id="1331"><a href="#1331">1331</a></td></tr
><tr id="gr_svn139_1332"

><td id="1332"><a href="#1332">1332</a></td></tr
><tr id="gr_svn139_1333"

><td id="1333"><a href="#1333">1333</a></td></tr
><tr id="gr_svn139_1334"

><td id="1334"><a href="#1334">1334</a></td></tr
><tr id="gr_svn139_1335"

><td id="1335"><a href="#1335">1335</a></td></tr
><tr id="gr_svn139_1336"

><td id="1336"><a href="#1336">1336</a></td></tr
><tr id="gr_svn139_1337"

><td id="1337"><a href="#1337">1337</a></td></tr
><tr id="gr_svn139_1338"

><td id="1338"><a href="#1338">1338</a></td></tr
><tr id="gr_svn139_1339"

><td id="1339"><a href="#1339">1339</a></td></tr
><tr id="gr_svn139_1340"

><td id="1340"><a href="#1340">1340</a></td></tr
><tr id="gr_svn139_1341"

><td id="1341"><a href="#1341">1341</a></td></tr
><tr id="gr_svn139_1342"

><td id="1342"><a href="#1342">1342</a></td></tr
><tr id="gr_svn139_1343"

><td id="1343"><a href="#1343">1343</a></td></tr
><tr id="gr_svn139_1344"

><td id="1344"><a href="#1344">1344</a></td></tr
><tr id="gr_svn139_1345"

><td id="1345"><a href="#1345">1345</a></td></tr
><tr id="gr_svn139_1346"

><td id="1346"><a href="#1346">1346</a></td></tr
><tr id="gr_svn139_1347"

><td id="1347"><a href="#1347">1347</a></td></tr
><tr id="gr_svn139_1348"

><td id="1348"><a href="#1348">1348</a></td></tr
><tr id="gr_svn139_1349"

><td id="1349"><a href="#1349">1349</a></td></tr
><tr id="gr_svn139_1350"

><td id="1350"><a href="#1350">1350</a></td></tr
><tr id="gr_svn139_1351"

><td id="1351"><a href="#1351">1351</a></td></tr
><tr id="gr_svn139_1352"

><td id="1352"><a href="#1352">1352</a></td></tr
><tr id="gr_svn139_1353"

><td id="1353"><a href="#1353">1353</a></td></tr
><tr id="gr_svn139_1354"

><td id="1354"><a href="#1354">1354</a></td></tr
><tr id="gr_svn139_1355"

><td id="1355"><a href="#1355">1355</a></td></tr
><tr id="gr_svn139_1356"

><td id="1356"><a href="#1356">1356</a></td></tr
><tr id="gr_svn139_1357"

><td id="1357"><a href="#1357">1357</a></td></tr
><tr id="gr_svn139_1358"

><td id="1358"><a href="#1358">1358</a></td></tr
><tr id="gr_svn139_1359"

><td id="1359"><a href="#1359">1359</a></td></tr
><tr id="gr_svn139_1360"

><td id="1360"><a href="#1360">1360</a></td></tr
><tr id="gr_svn139_1361"

><td id="1361"><a href="#1361">1361</a></td></tr
><tr id="gr_svn139_1362"

><td id="1362"><a href="#1362">1362</a></td></tr
><tr id="gr_svn139_1363"

><td id="1363"><a href="#1363">1363</a></td></tr
><tr id="gr_svn139_1364"

><td id="1364"><a href="#1364">1364</a></td></tr
><tr id="gr_svn139_1365"

><td id="1365"><a href="#1365">1365</a></td></tr
><tr id="gr_svn139_1366"

><td id="1366"><a href="#1366">1366</a></td></tr
><tr id="gr_svn139_1367"

><td id="1367"><a href="#1367">1367</a></td></tr
><tr id="gr_svn139_1368"

><td id="1368"><a href="#1368">1368</a></td></tr
><tr id="gr_svn139_1369"

><td id="1369"><a href="#1369">1369</a></td></tr
><tr id="gr_svn139_1370"

><td id="1370"><a href="#1370">1370</a></td></tr
><tr id="gr_svn139_1371"

><td id="1371"><a href="#1371">1371</a></td></tr
><tr id="gr_svn139_1372"

><td id="1372"><a href="#1372">1372</a></td></tr
><tr id="gr_svn139_1373"

><td id="1373"><a href="#1373">1373</a></td></tr
><tr id="gr_svn139_1374"

><td id="1374"><a href="#1374">1374</a></td></tr
><tr id="gr_svn139_1375"

><td id="1375"><a href="#1375">1375</a></td></tr
><tr id="gr_svn139_1376"

><td id="1376"><a href="#1376">1376</a></td></tr
><tr id="gr_svn139_1377"

><td id="1377"><a href="#1377">1377</a></td></tr
><tr id="gr_svn139_1378"

><td id="1378"><a href="#1378">1378</a></td></tr
><tr id="gr_svn139_1379"

><td id="1379"><a href="#1379">1379</a></td></tr
><tr id="gr_svn139_1380"

><td id="1380"><a href="#1380">1380</a></td></tr
><tr id="gr_svn139_1381"

><td id="1381"><a href="#1381">1381</a></td></tr
><tr id="gr_svn139_1382"

><td id="1382"><a href="#1382">1382</a></td></tr
><tr id="gr_svn139_1383"

><td id="1383"><a href="#1383">1383</a></td></tr
><tr id="gr_svn139_1384"

><td id="1384"><a href="#1384">1384</a></td></tr
><tr id="gr_svn139_1385"

><td id="1385"><a href="#1385">1385</a></td></tr
><tr id="gr_svn139_1386"

><td id="1386"><a href="#1386">1386</a></td></tr
><tr id="gr_svn139_1387"

><td id="1387"><a href="#1387">1387</a></td></tr
><tr id="gr_svn139_1388"

><td id="1388"><a href="#1388">1388</a></td></tr
><tr id="gr_svn139_1389"

><td id="1389"><a href="#1389">1389</a></td></tr
><tr id="gr_svn139_1390"

><td id="1390"><a href="#1390">1390</a></td></tr
><tr id="gr_svn139_1391"

><td id="1391"><a href="#1391">1391</a></td></tr
><tr id="gr_svn139_1392"

><td id="1392"><a href="#1392">1392</a></td></tr
><tr id="gr_svn139_1393"

><td id="1393"><a href="#1393">1393</a></td></tr
><tr id="gr_svn139_1394"

><td id="1394"><a href="#1394">1394</a></td></tr
><tr id="gr_svn139_1395"

><td id="1395"><a href="#1395">1395</a></td></tr
><tr id="gr_svn139_1396"

><td id="1396"><a href="#1396">1396</a></td></tr
><tr id="gr_svn139_1397"

><td id="1397"><a href="#1397">1397</a></td></tr
><tr id="gr_svn139_1398"

><td id="1398"><a href="#1398">1398</a></td></tr
><tr id="gr_svn139_1399"

><td id="1399"><a href="#1399">1399</a></td></tr
><tr id="gr_svn139_1400"

><td id="1400"><a href="#1400">1400</a></td></tr
><tr id="gr_svn139_1401"

><td id="1401"><a href="#1401">1401</a></td></tr
><tr id="gr_svn139_1402"

><td id="1402"><a href="#1402">1402</a></td></tr
><tr id="gr_svn139_1403"

><td id="1403"><a href="#1403">1403</a></td></tr
><tr id="gr_svn139_1404"

><td id="1404"><a href="#1404">1404</a></td></tr
><tr id="gr_svn139_1405"

><td id="1405"><a href="#1405">1405</a></td></tr
><tr id="gr_svn139_1406"

><td id="1406"><a href="#1406">1406</a></td></tr
><tr id="gr_svn139_1407"

><td id="1407"><a href="#1407">1407</a></td></tr
><tr id="gr_svn139_1408"

><td id="1408"><a href="#1408">1408</a></td></tr
><tr id="gr_svn139_1409"

><td id="1409"><a href="#1409">1409</a></td></tr
><tr id="gr_svn139_1410"

><td id="1410"><a href="#1410">1410</a></td></tr
><tr id="gr_svn139_1411"

><td id="1411"><a href="#1411">1411</a></td></tr
><tr id="gr_svn139_1412"

><td id="1412"><a href="#1412">1412</a></td></tr
><tr id="gr_svn139_1413"

><td id="1413"><a href="#1413">1413</a></td></tr
><tr id="gr_svn139_1414"

><td id="1414"><a href="#1414">1414</a></td></tr
><tr id="gr_svn139_1415"

><td id="1415"><a href="#1415">1415</a></td></tr
><tr id="gr_svn139_1416"

><td id="1416"><a href="#1416">1416</a></td></tr
><tr id="gr_svn139_1417"

><td id="1417"><a href="#1417">1417</a></td></tr
><tr id="gr_svn139_1418"

><td id="1418"><a href="#1418">1418</a></td></tr
><tr id="gr_svn139_1419"

><td id="1419"><a href="#1419">1419</a></td></tr
><tr id="gr_svn139_1420"

><td id="1420"><a href="#1420">1420</a></td></tr
><tr id="gr_svn139_1421"

><td id="1421"><a href="#1421">1421</a></td></tr
><tr id="gr_svn139_1422"

><td id="1422"><a href="#1422">1422</a></td></tr
><tr id="gr_svn139_1423"

><td id="1423"><a href="#1423">1423</a></td></tr
><tr id="gr_svn139_1424"

><td id="1424"><a href="#1424">1424</a></td></tr
><tr id="gr_svn139_1425"

><td id="1425"><a href="#1425">1425</a></td></tr
><tr id="gr_svn139_1426"

><td id="1426"><a href="#1426">1426</a></td></tr
><tr id="gr_svn139_1427"

><td id="1427"><a href="#1427">1427</a></td></tr
><tr id="gr_svn139_1428"

><td id="1428"><a href="#1428">1428</a></td></tr
><tr id="gr_svn139_1429"

><td id="1429"><a href="#1429">1429</a></td></tr
><tr id="gr_svn139_1430"

><td id="1430"><a href="#1430">1430</a></td></tr
><tr id="gr_svn139_1431"

><td id="1431"><a href="#1431">1431</a></td></tr
><tr id="gr_svn139_1432"

><td id="1432"><a href="#1432">1432</a></td></tr
><tr id="gr_svn139_1433"

><td id="1433"><a href="#1433">1433</a></td></tr
><tr id="gr_svn139_1434"

><td id="1434"><a href="#1434">1434</a></td></tr
><tr id="gr_svn139_1435"

><td id="1435"><a href="#1435">1435</a></td></tr
><tr id="gr_svn139_1436"

><td id="1436"><a href="#1436">1436</a></td></tr
><tr id="gr_svn139_1437"

><td id="1437"><a href="#1437">1437</a></td></tr
><tr id="gr_svn139_1438"

><td id="1438"><a href="#1438">1438</a></td></tr
><tr id="gr_svn139_1439"

><td id="1439"><a href="#1439">1439</a></td></tr
><tr id="gr_svn139_1440"

><td id="1440"><a href="#1440">1440</a></td></tr
><tr id="gr_svn139_1441"

><td id="1441"><a href="#1441">1441</a></td></tr
><tr id="gr_svn139_1442"

><td id="1442"><a href="#1442">1442</a></td></tr
><tr id="gr_svn139_1443"

><td id="1443"><a href="#1443">1443</a></td></tr
><tr id="gr_svn139_1444"

><td id="1444"><a href="#1444">1444</a></td></tr
><tr id="gr_svn139_1445"

><td id="1445"><a href="#1445">1445</a></td></tr
><tr id="gr_svn139_1446"

><td id="1446"><a href="#1446">1446</a></td></tr
><tr id="gr_svn139_1447"

><td id="1447"><a href="#1447">1447</a></td></tr
><tr id="gr_svn139_1448"

><td id="1448"><a href="#1448">1448</a></td></tr
><tr id="gr_svn139_1449"

><td id="1449"><a href="#1449">1449</a></td></tr
><tr id="gr_svn139_1450"

><td id="1450"><a href="#1450">1450</a></td></tr
><tr id="gr_svn139_1451"

><td id="1451"><a href="#1451">1451</a></td></tr
><tr id="gr_svn139_1452"

><td id="1452"><a href="#1452">1452</a></td></tr
><tr id="gr_svn139_1453"

><td id="1453"><a href="#1453">1453</a></td></tr
><tr id="gr_svn139_1454"

><td id="1454"><a href="#1454">1454</a></td></tr
><tr id="gr_svn139_1455"

><td id="1455"><a href="#1455">1455</a></td></tr
><tr id="gr_svn139_1456"

><td id="1456"><a href="#1456">1456</a></td></tr
><tr id="gr_svn139_1457"

><td id="1457"><a href="#1457">1457</a></td></tr
><tr id="gr_svn139_1458"

><td id="1458"><a href="#1458">1458</a></td></tr
><tr id="gr_svn139_1459"

><td id="1459"><a href="#1459">1459</a></td></tr
><tr id="gr_svn139_1460"

><td id="1460"><a href="#1460">1460</a></td></tr
><tr id="gr_svn139_1461"

><td id="1461"><a href="#1461">1461</a></td></tr
><tr id="gr_svn139_1462"

><td id="1462"><a href="#1462">1462</a></td></tr
><tr id="gr_svn139_1463"

><td id="1463"><a href="#1463">1463</a></td></tr
><tr id="gr_svn139_1464"

><td id="1464"><a href="#1464">1464</a></td></tr
><tr id="gr_svn139_1465"

><td id="1465"><a href="#1465">1465</a></td></tr
><tr id="gr_svn139_1466"

><td id="1466"><a href="#1466">1466</a></td></tr
><tr id="gr_svn139_1467"

><td id="1467"><a href="#1467">1467</a></td></tr
><tr id="gr_svn139_1468"

><td id="1468"><a href="#1468">1468</a></td></tr
><tr id="gr_svn139_1469"

><td id="1469"><a href="#1469">1469</a></td></tr
><tr id="gr_svn139_1470"

><td id="1470"><a href="#1470">1470</a></td></tr
><tr id="gr_svn139_1471"

><td id="1471"><a href="#1471">1471</a></td></tr
><tr id="gr_svn139_1472"

><td id="1472"><a href="#1472">1472</a></td></tr
><tr id="gr_svn139_1473"

><td id="1473"><a href="#1473">1473</a></td></tr
><tr id="gr_svn139_1474"

><td id="1474"><a href="#1474">1474</a></td></tr
><tr id="gr_svn139_1475"

><td id="1475"><a href="#1475">1475</a></td></tr
><tr id="gr_svn139_1476"

><td id="1476"><a href="#1476">1476</a></td></tr
><tr id="gr_svn139_1477"

><td id="1477"><a href="#1477">1477</a></td></tr
><tr id="gr_svn139_1478"

><td id="1478"><a href="#1478">1478</a></td></tr
><tr id="gr_svn139_1479"

><td id="1479"><a href="#1479">1479</a></td></tr
><tr id="gr_svn139_1480"

><td id="1480"><a href="#1480">1480</a></td></tr
><tr id="gr_svn139_1481"

><td id="1481"><a href="#1481">1481</a></td></tr
><tr id="gr_svn139_1482"

><td id="1482"><a href="#1482">1482</a></td></tr
><tr id="gr_svn139_1483"

><td id="1483"><a href="#1483">1483</a></td></tr
><tr id="gr_svn139_1484"

><td id="1484"><a href="#1484">1484</a></td></tr
><tr id="gr_svn139_1485"

><td id="1485"><a href="#1485">1485</a></td></tr
><tr id="gr_svn139_1486"

><td id="1486"><a href="#1486">1486</a></td></tr
><tr id="gr_svn139_1487"

><td id="1487"><a href="#1487">1487</a></td></tr
><tr id="gr_svn139_1488"

><td id="1488"><a href="#1488">1488</a></td></tr
><tr id="gr_svn139_1489"

><td id="1489"><a href="#1489">1489</a></td></tr
><tr id="gr_svn139_1490"

><td id="1490"><a href="#1490">1490</a></td></tr
><tr id="gr_svn139_1491"

><td id="1491"><a href="#1491">1491</a></td></tr
><tr id="gr_svn139_1492"

><td id="1492"><a href="#1492">1492</a></td></tr
><tr id="gr_svn139_1493"

><td id="1493"><a href="#1493">1493</a></td></tr
><tr id="gr_svn139_1494"

><td id="1494"><a href="#1494">1494</a></td></tr
><tr id="gr_svn139_1495"

><td id="1495"><a href="#1495">1495</a></td></tr
><tr id="gr_svn139_1496"

><td id="1496"><a href="#1496">1496</a></td></tr
><tr id="gr_svn139_1497"

><td id="1497"><a href="#1497">1497</a></td></tr
><tr id="gr_svn139_1498"

><td id="1498"><a href="#1498">1498</a></td></tr
><tr id="gr_svn139_1499"

><td id="1499"><a href="#1499">1499</a></td></tr
><tr id="gr_svn139_1500"

><td id="1500"><a href="#1500">1500</a></td></tr
><tr id="gr_svn139_1501"

><td id="1501"><a href="#1501">1501</a></td></tr
><tr id="gr_svn139_1502"

><td id="1502"><a href="#1502">1502</a></td></tr
><tr id="gr_svn139_1503"

><td id="1503"><a href="#1503">1503</a></td></tr
><tr id="gr_svn139_1504"

><td id="1504"><a href="#1504">1504</a></td></tr
><tr id="gr_svn139_1505"

><td id="1505"><a href="#1505">1505</a></td></tr
><tr id="gr_svn139_1506"

><td id="1506"><a href="#1506">1506</a></td></tr
><tr id="gr_svn139_1507"

><td id="1507"><a href="#1507">1507</a></td></tr
><tr id="gr_svn139_1508"

><td id="1508"><a href="#1508">1508</a></td></tr
><tr id="gr_svn139_1509"

><td id="1509"><a href="#1509">1509</a></td></tr
><tr id="gr_svn139_1510"

><td id="1510"><a href="#1510">1510</a></td></tr
><tr id="gr_svn139_1511"

><td id="1511"><a href="#1511">1511</a></td></tr
><tr id="gr_svn139_1512"

><td id="1512"><a href="#1512">1512</a></td></tr
><tr id="gr_svn139_1513"

><td id="1513"><a href="#1513">1513</a></td></tr
><tr id="gr_svn139_1514"

><td id="1514"><a href="#1514">1514</a></td></tr
><tr id="gr_svn139_1515"

><td id="1515"><a href="#1515">1515</a></td></tr
><tr id="gr_svn139_1516"

><td id="1516"><a href="#1516">1516</a></td></tr
><tr id="gr_svn139_1517"

><td id="1517"><a href="#1517">1517</a></td></tr
><tr id="gr_svn139_1518"

><td id="1518"><a href="#1518">1518</a></td></tr
><tr id="gr_svn139_1519"

><td id="1519"><a href="#1519">1519</a></td></tr
><tr id="gr_svn139_1520"

><td id="1520"><a href="#1520">1520</a></td></tr
><tr id="gr_svn139_1521"

><td id="1521"><a href="#1521">1521</a></td></tr
><tr id="gr_svn139_1522"

><td id="1522"><a href="#1522">1522</a></td></tr
><tr id="gr_svn139_1523"

><td id="1523"><a href="#1523">1523</a></td></tr
><tr id="gr_svn139_1524"

><td id="1524"><a href="#1524">1524</a></td></tr
><tr id="gr_svn139_1525"

><td id="1525"><a href="#1525">1525</a></td></tr
><tr id="gr_svn139_1526"

><td id="1526"><a href="#1526">1526</a></td></tr
><tr id="gr_svn139_1527"

><td id="1527"><a href="#1527">1527</a></td></tr
><tr id="gr_svn139_1528"

><td id="1528"><a href="#1528">1528</a></td></tr
><tr id="gr_svn139_1529"

><td id="1529"><a href="#1529">1529</a></td></tr
><tr id="gr_svn139_1530"

><td id="1530"><a href="#1530">1530</a></td></tr
><tr id="gr_svn139_1531"

><td id="1531"><a href="#1531">1531</a></td></tr
><tr id="gr_svn139_1532"

><td id="1532"><a href="#1532">1532</a></td></tr
><tr id="gr_svn139_1533"

><td id="1533"><a href="#1533">1533</a></td></tr
><tr id="gr_svn139_1534"

><td id="1534"><a href="#1534">1534</a></td></tr
><tr id="gr_svn139_1535"

><td id="1535"><a href="#1535">1535</a></td></tr
><tr id="gr_svn139_1536"

><td id="1536"><a href="#1536">1536</a></td></tr
><tr id="gr_svn139_1537"

><td id="1537"><a href="#1537">1537</a></td></tr
><tr id="gr_svn139_1538"

><td id="1538"><a href="#1538">1538</a></td></tr
><tr id="gr_svn139_1539"

><td id="1539"><a href="#1539">1539</a></td></tr
><tr id="gr_svn139_1540"

><td id="1540"><a href="#1540">1540</a></td></tr
><tr id="gr_svn139_1541"

><td id="1541"><a href="#1541">1541</a></td></tr
><tr id="gr_svn139_1542"

><td id="1542"><a href="#1542">1542</a></td></tr
><tr id="gr_svn139_1543"

><td id="1543"><a href="#1543">1543</a></td></tr
><tr id="gr_svn139_1544"

><td id="1544"><a href="#1544">1544</a></td></tr
><tr id="gr_svn139_1545"

><td id="1545"><a href="#1545">1545</a></td></tr
><tr id="gr_svn139_1546"

><td id="1546"><a href="#1546">1546</a></td></tr
><tr id="gr_svn139_1547"

><td id="1547"><a href="#1547">1547</a></td></tr
><tr id="gr_svn139_1548"

><td id="1548"><a href="#1548">1548</a></td></tr
><tr id="gr_svn139_1549"

><td id="1549"><a href="#1549">1549</a></td></tr
><tr id="gr_svn139_1550"

><td id="1550"><a href="#1550">1550</a></td></tr
><tr id="gr_svn139_1551"

><td id="1551"><a href="#1551">1551</a></td></tr
><tr id="gr_svn139_1552"

><td id="1552"><a href="#1552">1552</a></td></tr
><tr id="gr_svn139_1553"

><td id="1553"><a href="#1553">1553</a></td></tr
><tr id="gr_svn139_1554"

><td id="1554"><a href="#1554">1554</a></td></tr
><tr id="gr_svn139_1555"

><td id="1555"><a href="#1555">1555</a></td></tr
><tr id="gr_svn139_1556"

><td id="1556"><a href="#1556">1556</a></td></tr
><tr id="gr_svn139_1557"

><td id="1557"><a href="#1557">1557</a></td></tr
><tr id="gr_svn139_1558"

><td id="1558"><a href="#1558">1558</a></td></tr
><tr id="gr_svn139_1559"

><td id="1559"><a href="#1559">1559</a></td></tr
><tr id="gr_svn139_1560"

><td id="1560"><a href="#1560">1560</a></td></tr
><tr id="gr_svn139_1561"

><td id="1561"><a href="#1561">1561</a></td></tr
><tr id="gr_svn139_1562"

><td id="1562"><a href="#1562">1562</a></td></tr
><tr id="gr_svn139_1563"

><td id="1563"><a href="#1563">1563</a></td></tr
><tr id="gr_svn139_1564"

><td id="1564"><a href="#1564">1564</a></td></tr
><tr id="gr_svn139_1565"

><td id="1565"><a href="#1565">1565</a></td></tr
><tr id="gr_svn139_1566"

><td id="1566"><a href="#1566">1566</a></td></tr
><tr id="gr_svn139_1567"

><td id="1567"><a href="#1567">1567</a></td></tr
><tr id="gr_svn139_1568"

><td id="1568"><a href="#1568">1568</a></td></tr
><tr id="gr_svn139_1569"

><td id="1569"><a href="#1569">1569</a></td></tr
><tr id="gr_svn139_1570"

><td id="1570"><a href="#1570">1570</a></td></tr
><tr id="gr_svn139_1571"

><td id="1571"><a href="#1571">1571</a></td></tr
><tr id="gr_svn139_1572"

><td id="1572"><a href="#1572">1572</a></td></tr
><tr id="gr_svn139_1573"

><td id="1573"><a href="#1573">1573</a></td></tr
><tr id="gr_svn139_1574"

><td id="1574"><a href="#1574">1574</a></td></tr
><tr id="gr_svn139_1575"

><td id="1575"><a href="#1575">1575</a></td></tr
><tr id="gr_svn139_1576"

><td id="1576"><a href="#1576">1576</a></td></tr
><tr id="gr_svn139_1577"

><td id="1577"><a href="#1577">1577</a></td></tr
><tr id="gr_svn139_1578"

><td id="1578"><a href="#1578">1578</a></td></tr
><tr id="gr_svn139_1579"

><td id="1579"><a href="#1579">1579</a></td></tr
><tr id="gr_svn139_1580"

><td id="1580"><a href="#1580">1580</a></td></tr
><tr id="gr_svn139_1581"

><td id="1581"><a href="#1581">1581</a></td></tr
><tr id="gr_svn139_1582"

><td id="1582"><a href="#1582">1582</a></td></tr
><tr id="gr_svn139_1583"

><td id="1583"><a href="#1583">1583</a></td></tr
><tr id="gr_svn139_1584"

><td id="1584"><a href="#1584">1584</a></td></tr
><tr id="gr_svn139_1585"

><td id="1585"><a href="#1585">1585</a></td></tr
><tr id="gr_svn139_1586"

><td id="1586"><a href="#1586">1586</a></td></tr
><tr id="gr_svn139_1587"

><td id="1587"><a href="#1587">1587</a></td></tr
><tr id="gr_svn139_1588"

><td id="1588"><a href="#1588">1588</a></td></tr
><tr id="gr_svn139_1589"

><td id="1589"><a href="#1589">1589</a></td></tr
><tr id="gr_svn139_1590"

><td id="1590"><a href="#1590">1590</a></td></tr
><tr id="gr_svn139_1591"

><td id="1591"><a href="#1591">1591</a></td></tr
><tr id="gr_svn139_1592"

><td id="1592"><a href="#1592">1592</a></td></tr
><tr id="gr_svn139_1593"

><td id="1593"><a href="#1593">1593</a></td></tr
><tr id="gr_svn139_1594"

><td id="1594"><a href="#1594">1594</a></td></tr
><tr id="gr_svn139_1595"

><td id="1595"><a href="#1595">1595</a></td></tr
><tr id="gr_svn139_1596"

><td id="1596"><a href="#1596">1596</a></td></tr
><tr id="gr_svn139_1597"

><td id="1597"><a href="#1597">1597</a></td></tr
><tr id="gr_svn139_1598"

><td id="1598"><a href="#1598">1598</a></td></tr
><tr id="gr_svn139_1599"

><td id="1599"><a href="#1599">1599</a></td></tr
><tr id="gr_svn139_1600"

><td id="1600"><a href="#1600">1600</a></td></tr
><tr id="gr_svn139_1601"

><td id="1601"><a href="#1601">1601</a></td></tr
><tr id="gr_svn139_1602"

><td id="1602"><a href="#1602">1602</a></td></tr
><tr id="gr_svn139_1603"

><td id="1603"><a href="#1603">1603</a></td></tr
><tr id="gr_svn139_1604"

><td id="1604"><a href="#1604">1604</a></td></tr
><tr id="gr_svn139_1605"

><td id="1605"><a href="#1605">1605</a></td></tr
><tr id="gr_svn139_1606"

><td id="1606"><a href="#1606">1606</a></td></tr
><tr id="gr_svn139_1607"

><td id="1607"><a href="#1607">1607</a></td></tr
><tr id="gr_svn139_1608"

><td id="1608"><a href="#1608">1608</a></td></tr
><tr id="gr_svn139_1609"

><td id="1609"><a href="#1609">1609</a></td></tr
><tr id="gr_svn139_1610"

><td id="1610"><a href="#1610">1610</a></td></tr
><tr id="gr_svn139_1611"

><td id="1611"><a href="#1611">1611</a></td></tr
><tr id="gr_svn139_1612"

><td id="1612"><a href="#1612">1612</a></td></tr
><tr id="gr_svn139_1613"

><td id="1613"><a href="#1613">1613</a></td></tr
><tr id="gr_svn139_1614"

><td id="1614"><a href="#1614">1614</a></td></tr
><tr id="gr_svn139_1615"

><td id="1615"><a href="#1615">1615</a></td></tr
><tr id="gr_svn139_1616"

><td id="1616"><a href="#1616">1616</a></td></tr
><tr id="gr_svn139_1617"

><td id="1617"><a href="#1617">1617</a></td></tr
><tr id="gr_svn139_1618"

><td id="1618"><a href="#1618">1618</a></td></tr
><tr id="gr_svn139_1619"

><td id="1619"><a href="#1619">1619</a></td></tr
><tr id="gr_svn139_1620"

><td id="1620"><a href="#1620">1620</a></td></tr
><tr id="gr_svn139_1621"

><td id="1621"><a href="#1621">1621</a></td></tr
><tr id="gr_svn139_1622"

><td id="1622"><a href="#1622">1622</a></td></tr
><tr id="gr_svn139_1623"

><td id="1623"><a href="#1623">1623</a></td></tr
><tr id="gr_svn139_1624"

><td id="1624"><a href="#1624">1624</a></td></tr
><tr id="gr_svn139_1625"

><td id="1625"><a href="#1625">1625</a></td></tr
><tr id="gr_svn139_1626"

><td id="1626"><a href="#1626">1626</a></td></tr
><tr id="gr_svn139_1627"

><td id="1627"><a href="#1627">1627</a></td></tr
><tr id="gr_svn139_1628"

><td id="1628"><a href="#1628">1628</a></td></tr
><tr id="gr_svn139_1629"

><td id="1629"><a href="#1629">1629</a></td></tr
><tr id="gr_svn139_1630"

><td id="1630"><a href="#1630">1630</a></td></tr
><tr id="gr_svn139_1631"

><td id="1631"><a href="#1631">1631</a></td></tr
><tr id="gr_svn139_1632"

><td id="1632"><a href="#1632">1632</a></td></tr
><tr id="gr_svn139_1633"

><td id="1633"><a href="#1633">1633</a></td></tr
><tr id="gr_svn139_1634"

><td id="1634"><a href="#1634">1634</a></td></tr
><tr id="gr_svn139_1635"

><td id="1635"><a href="#1635">1635</a></td></tr
><tr id="gr_svn139_1636"

><td id="1636"><a href="#1636">1636</a></td></tr
><tr id="gr_svn139_1637"

><td id="1637"><a href="#1637">1637</a></td></tr
><tr id="gr_svn139_1638"

><td id="1638"><a href="#1638">1638</a></td></tr
><tr id="gr_svn139_1639"

><td id="1639"><a href="#1639">1639</a></td></tr
><tr id="gr_svn139_1640"

><td id="1640"><a href="#1640">1640</a></td></tr
><tr id="gr_svn139_1641"

><td id="1641"><a href="#1641">1641</a></td></tr
><tr id="gr_svn139_1642"

><td id="1642"><a href="#1642">1642</a></td></tr
><tr id="gr_svn139_1643"

><td id="1643"><a href="#1643">1643</a></td></tr
><tr id="gr_svn139_1644"

><td id="1644"><a href="#1644">1644</a></td></tr
><tr id="gr_svn139_1645"

><td id="1645"><a href="#1645">1645</a></td></tr
><tr id="gr_svn139_1646"

><td id="1646"><a href="#1646">1646</a></td></tr
><tr id="gr_svn139_1647"

><td id="1647"><a href="#1647">1647</a></td></tr
><tr id="gr_svn139_1648"

><td id="1648"><a href="#1648">1648</a></td></tr
><tr id="gr_svn139_1649"

><td id="1649"><a href="#1649">1649</a></td></tr
><tr id="gr_svn139_1650"

><td id="1650"><a href="#1650">1650</a></td></tr
><tr id="gr_svn139_1651"

><td id="1651"><a href="#1651">1651</a></td></tr
><tr id="gr_svn139_1652"

><td id="1652"><a href="#1652">1652</a></td></tr
><tr id="gr_svn139_1653"

><td id="1653"><a href="#1653">1653</a></td></tr
><tr id="gr_svn139_1654"

><td id="1654"><a href="#1654">1654</a></td></tr
><tr id="gr_svn139_1655"

><td id="1655"><a href="#1655">1655</a></td></tr
><tr id="gr_svn139_1656"

><td id="1656"><a href="#1656">1656</a></td></tr
><tr id="gr_svn139_1657"

><td id="1657"><a href="#1657">1657</a></td></tr
><tr id="gr_svn139_1658"

><td id="1658"><a href="#1658">1658</a></td></tr
><tr id="gr_svn139_1659"

><td id="1659"><a href="#1659">1659</a></td></tr
><tr id="gr_svn139_1660"

><td id="1660"><a href="#1660">1660</a></td></tr
><tr id="gr_svn139_1661"

><td id="1661"><a href="#1661">1661</a></td></tr
><tr id="gr_svn139_1662"

><td id="1662"><a href="#1662">1662</a></td></tr
><tr id="gr_svn139_1663"

><td id="1663"><a href="#1663">1663</a></td></tr
><tr id="gr_svn139_1664"

><td id="1664"><a href="#1664">1664</a></td></tr
><tr id="gr_svn139_1665"

><td id="1665"><a href="#1665">1665</a></td></tr
><tr id="gr_svn139_1666"

><td id="1666"><a href="#1666">1666</a></td></tr
><tr id="gr_svn139_1667"

><td id="1667"><a href="#1667">1667</a></td></tr
><tr id="gr_svn139_1668"

><td id="1668"><a href="#1668">1668</a></td></tr
><tr id="gr_svn139_1669"

><td id="1669"><a href="#1669">1669</a></td></tr
><tr id="gr_svn139_1670"

><td id="1670"><a href="#1670">1670</a></td></tr
><tr id="gr_svn139_1671"

><td id="1671"><a href="#1671">1671</a></td></tr
><tr id="gr_svn139_1672"

><td id="1672"><a href="#1672">1672</a></td></tr
><tr id="gr_svn139_1673"

><td id="1673"><a href="#1673">1673</a></td></tr
><tr id="gr_svn139_1674"

><td id="1674"><a href="#1674">1674</a></td></tr
><tr id="gr_svn139_1675"

><td id="1675"><a href="#1675">1675</a></td></tr
><tr id="gr_svn139_1676"

><td id="1676"><a href="#1676">1676</a></td></tr
><tr id="gr_svn139_1677"

><td id="1677"><a href="#1677">1677</a></td></tr
><tr id="gr_svn139_1678"

><td id="1678"><a href="#1678">1678</a></td></tr
><tr id="gr_svn139_1679"

><td id="1679"><a href="#1679">1679</a></td></tr
><tr id="gr_svn139_1680"

><td id="1680"><a href="#1680">1680</a></td></tr
><tr id="gr_svn139_1681"

><td id="1681"><a href="#1681">1681</a></td></tr
><tr id="gr_svn139_1682"

><td id="1682"><a href="#1682">1682</a></td></tr
><tr id="gr_svn139_1683"

><td id="1683"><a href="#1683">1683</a></td></tr
><tr id="gr_svn139_1684"

><td id="1684"><a href="#1684">1684</a></td></tr
><tr id="gr_svn139_1685"

><td id="1685"><a href="#1685">1685</a></td></tr
><tr id="gr_svn139_1686"

><td id="1686"><a href="#1686">1686</a></td></tr
><tr id="gr_svn139_1687"

><td id="1687"><a href="#1687">1687</a></td></tr
><tr id="gr_svn139_1688"

><td id="1688"><a href="#1688">1688</a></td></tr
><tr id="gr_svn139_1689"

><td id="1689"><a href="#1689">1689</a></td></tr
><tr id="gr_svn139_1690"

><td id="1690"><a href="#1690">1690</a></td></tr
><tr id="gr_svn139_1691"

><td id="1691"><a href="#1691">1691</a></td></tr
><tr id="gr_svn139_1692"

><td id="1692"><a href="#1692">1692</a></td></tr
><tr id="gr_svn139_1693"

><td id="1693"><a href="#1693">1693</a></td></tr
><tr id="gr_svn139_1694"

><td id="1694"><a href="#1694">1694</a></td></tr
><tr id="gr_svn139_1695"

><td id="1695"><a href="#1695">1695</a></td></tr
><tr id="gr_svn139_1696"

><td id="1696"><a href="#1696">1696</a></td></tr
><tr id="gr_svn139_1697"

><td id="1697"><a href="#1697">1697</a></td></tr
><tr id="gr_svn139_1698"

><td id="1698"><a href="#1698">1698</a></td></tr
><tr id="gr_svn139_1699"

><td id="1699"><a href="#1699">1699</a></td></tr
><tr id="gr_svn139_1700"

><td id="1700"><a href="#1700">1700</a></td></tr
><tr id="gr_svn139_1701"

><td id="1701"><a href="#1701">1701</a></td></tr
><tr id="gr_svn139_1702"

><td id="1702"><a href="#1702">1702</a></td></tr
><tr id="gr_svn139_1703"

><td id="1703"><a href="#1703">1703</a></td></tr
><tr id="gr_svn139_1704"

><td id="1704"><a href="#1704">1704</a></td></tr
><tr id="gr_svn139_1705"

><td id="1705"><a href="#1705">1705</a></td></tr
><tr id="gr_svn139_1706"

><td id="1706"><a href="#1706">1706</a></td></tr
><tr id="gr_svn139_1707"

><td id="1707"><a href="#1707">1707</a></td></tr
><tr id="gr_svn139_1708"

><td id="1708"><a href="#1708">1708</a></td></tr
><tr id="gr_svn139_1709"

><td id="1709"><a href="#1709">1709</a></td></tr
><tr id="gr_svn139_1710"

><td id="1710"><a href="#1710">1710</a></td></tr
><tr id="gr_svn139_1711"

><td id="1711"><a href="#1711">1711</a></td></tr
><tr id="gr_svn139_1712"

><td id="1712"><a href="#1712">1712</a></td></tr
><tr id="gr_svn139_1713"

><td id="1713"><a href="#1713">1713</a></td></tr
><tr id="gr_svn139_1714"

><td id="1714"><a href="#1714">1714</a></td></tr
><tr id="gr_svn139_1715"

><td id="1715"><a href="#1715">1715</a></td></tr
><tr id="gr_svn139_1716"

><td id="1716"><a href="#1716">1716</a></td></tr
><tr id="gr_svn139_1717"

><td id="1717"><a href="#1717">1717</a></td></tr
><tr id="gr_svn139_1718"

><td id="1718"><a href="#1718">1718</a></td></tr
><tr id="gr_svn139_1719"

><td id="1719"><a href="#1719">1719</a></td></tr
><tr id="gr_svn139_1720"

><td id="1720"><a href="#1720">1720</a></td></tr
><tr id="gr_svn139_1721"

><td id="1721"><a href="#1721">1721</a></td></tr
><tr id="gr_svn139_1722"

><td id="1722"><a href="#1722">1722</a></td></tr
><tr id="gr_svn139_1723"

><td id="1723"><a href="#1723">1723</a></td></tr
><tr id="gr_svn139_1724"

><td id="1724"><a href="#1724">1724</a></td></tr
><tr id="gr_svn139_1725"

><td id="1725"><a href="#1725">1725</a></td></tr
><tr id="gr_svn139_1726"

><td id="1726"><a href="#1726">1726</a></td></tr
><tr id="gr_svn139_1727"

><td id="1727"><a href="#1727">1727</a></td></tr
><tr id="gr_svn139_1728"

><td id="1728"><a href="#1728">1728</a></td></tr
><tr id="gr_svn139_1729"

><td id="1729"><a href="#1729">1729</a></td></tr
><tr id="gr_svn139_1730"

><td id="1730"><a href="#1730">1730</a></td></tr
><tr id="gr_svn139_1731"

><td id="1731"><a href="#1731">1731</a></td></tr
><tr id="gr_svn139_1732"

><td id="1732"><a href="#1732">1732</a></td></tr
><tr id="gr_svn139_1733"

><td id="1733"><a href="#1733">1733</a></td></tr
><tr id="gr_svn139_1734"

><td id="1734"><a href="#1734">1734</a></td></tr
><tr id="gr_svn139_1735"

><td id="1735"><a href="#1735">1735</a></td></tr
><tr id="gr_svn139_1736"

><td id="1736"><a href="#1736">1736</a></td></tr
><tr id="gr_svn139_1737"

><td id="1737"><a href="#1737">1737</a></td></tr
><tr id="gr_svn139_1738"

><td id="1738"><a href="#1738">1738</a></td></tr
><tr id="gr_svn139_1739"

><td id="1739"><a href="#1739">1739</a></td></tr
><tr id="gr_svn139_1740"

><td id="1740"><a href="#1740">1740</a></td></tr
><tr id="gr_svn139_1741"

><td id="1741"><a href="#1741">1741</a></td></tr
><tr id="gr_svn139_1742"

><td id="1742"><a href="#1742">1742</a></td></tr
><tr id="gr_svn139_1743"

><td id="1743"><a href="#1743">1743</a></td></tr
><tr id="gr_svn139_1744"

><td id="1744"><a href="#1744">1744</a></td></tr
><tr id="gr_svn139_1745"

><td id="1745"><a href="#1745">1745</a></td></tr
><tr id="gr_svn139_1746"

><td id="1746"><a href="#1746">1746</a></td></tr
><tr id="gr_svn139_1747"

><td id="1747"><a href="#1747">1747</a></td></tr
><tr id="gr_svn139_1748"

><td id="1748"><a href="#1748">1748</a></td></tr
><tr id="gr_svn139_1749"

><td id="1749"><a href="#1749">1749</a></td></tr
><tr id="gr_svn139_1750"

><td id="1750"><a href="#1750">1750</a></td></tr
><tr id="gr_svn139_1751"

><td id="1751"><a href="#1751">1751</a></td></tr
><tr id="gr_svn139_1752"

><td id="1752"><a href="#1752">1752</a></td></tr
><tr id="gr_svn139_1753"

><td id="1753"><a href="#1753">1753</a></td></tr
><tr id="gr_svn139_1754"

><td id="1754"><a href="#1754">1754</a></td></tr
><tr id="gr_svn139_1755"

><td id="1755"><a href="#1755">1755</a></td></tr
><tr id="gr_svn139_1756"

><td id="1756"><a href="#1756">1756</a></td></tr
><tr id="gr_svn139_1757"

><td id="1757"><a href="#1757">1757</a></td></tr
><tr id="gr_svn139_1758"

><td id="1758"><a href="#1758">1758</a></td></tr
><tr id="gr_svn139_1759"

><td id="1759"><a href="#1759">1759</a></td></tr
><tr id="gr_svn139_1760"

><td id="1760"><a href="#1760">1760</a></td></tr
><tr id="gr_svn139_1761"

><td id="1761"><a href="#1761">1761</a></td></tr
><tr id="gr_svn139_1762"

><td id="1762"><a href="#1762">1762</a></td></tr
><tr id="gr_svn139_1763"

><td id="1763"><a href="#1763">1763</a></td></tr
><tr id="gr_svn139_1764"

><td id="1764"><a href="#1764">1764</a></td></tr
><tr id="gr_svn139_1765"

><td id="1765"><a href="#1765">1765</a></td></tr
><tr id="gr_svn139_1766"

><td id="1766"><a href="#1766">1766</a></td></tr
><tr id="gr_svn139_1767"

><td id="1767"><a href="#1767">1767</a></td></tr
><tr id="gr_svn139_1768"

><td id="1768"><a href="#1768">1768</a></td></tr
><tr id="gr_svn139_1769"

><td id="1769"><a href="#1769">1769</a></td></tr
><tr id="gr_svn139_1770"

><td id="1770"><a href="#1770">1770</a></td></tr
><tr id="gr_svn139_1771"

><td id="1771"><a href="#1771">1771</a></td></tr
><tr id="gr_svn139_1772"

><td id="1772"><a href="#1772">1772</a></td></tr
><tr id="gr_svn139_1773"

><td id="1773"><a href="#1773">1773</a></td></tr
><tr id="gr_svn139_1774"

><td id="1774"><a href="#1774">1774</a></td></tr
><tr id="gr_svn139_1775"

><td id="1775"><a href="#1775">1775</a></td></tr
><tr id="gr_svn139_1776"

><td id="1776"><a href="#1776">1776</a></td></tr
><tr id="gr_svn139_1777"

><td id="1777"><a href="#1777">1777</a></td></tr
><tr id="gr_svn139_1778"

><td id="1778"><a href="#1778">1778</a></td></tr
><tr id="gr_svn139_1779"

><td id="1779"><a href="#1779">1779</a></td></tr
><tr id="gr_svn139_1780"

><td id="1780"><a href="#1780">1780</a></td></tr
><tr id="gr_svn139_1781"

><td id="1781"><a href="#1781">1781</a></td></tr
><tr id="gr_svn139_1782"

><td id="1782"><a href="#1782">1782</a></td></tr
><tr id="gr_svn139_1783"

><td id="1783"><a href="#1783">1783</a></td></tr
><tr id="gr_svn139_1784"

><td id="1784"><a href="#1784">1784</a></td></tr
><tr id="gr_svn139_1785"

><td id="1785"><a href="#1785">1785</a></td></tr
><tr id="gr_svn139_1786"

><td id="1786"><a href="#1786">1786</a></td></tr
><tr id="gr_svn139_1787"

><td id="1787"><a href="#1787">1787</a></td></tr
><tr id="gr_svn139_1788"

><td id="1788"><a href="#1788">1788</a></td></tr
><tr id="gr_svn139_1789"

><td id="1789"><a href="#1789">1789</a></td></tr
><tr id="gr_svn139_1790"

><td id="1790"><a href="#1790">1790</a></td></tr
><tr id="gr_svn139_1791"

><td id="1791"><a href="#1791">1791</a></td></tr
><tr id="gr_svn139_1792"

><td id="1792"><a href="#1792">1792</a></td></tr
><tr id="gr_svn139_1793"

><td id="1793"><a href="#1793">1793</a></td></tr
><tr id="gr_svn139_1794"

><td id="1794"><a href="#1794">1794</a></td></tr
><tr id="gr_svn139_1795"

><td id="1795"><a href="#1795">1795</a></td></tr
><tr id="gr_svn139_1796"

><td id="1796"><a href="#1796">1796</a></td></tr
><tr id="gr_svn139_1797"

><td id="1797"><a href="#1797">1797</a></td></tr
><tr id="gr_svn139_1798"

><td id="1798"><a href="#1798">1798</a></td></tr
><tr id="gr_svn139_1799"

><td id="1799"><a href="#1799">1799</a></td></tr
><tr id="gr_svn139_1800"

><td id="1800"><a href="#1800">1800</a></td></tr
><tr id="gr_svn139_1801"

><td id="1801"><a href="#1801">1801</a></td></tr
><tr id="gr_svn139_1802"

><td id="1802"><a href="#1802">1802</a></td></tr
><tr id="gr_svn139_1803"

><td id="1803"><a href="#1803">1803</a></td></tr
><tr id="gr_svn139_1804"

><td id="1804"><a href="#1804">1804</a></td></tr
><tr id="gr_svn139_1805"

><td id="1805"><a href="#1805">1805</a></td></tr
><tr id="gr_svn139_1806"

><td id="1806"><a href="#1806">1806</a></td></tr
><tr id="gr_svn139_1807"

><td id="1807"><a href="#1807">1807</a></td></tr
><tr id="gr_svn139_1808"

><td id="1808"><a href="#1808">1808</a></td></tr
><tr id="gr_svn139_1809"

><td id="1809"><a href="#1809">1809</a></td></tr
><tr id="gr_svn139_1810"

><td id="1810"><a href="#1810">1810</a></td></tr
><tr id="gr_svn139_1811"

><td id="1811"><a href="#1811">1811</a></td></tr
><tr id="gr_svn139_1812"

><td id="1812"><a href="#1812">1812</a></td></tr
><tr id="gr_svn139_1813"

><td id="1813"><a href="#1813">1813</a></td></tr
><tr id="gr_svn139_1814"

><td id="1814"><a href="#1814">1814</a></td></tr
><tr id="gr_svn139_1815"

><td id="1815"><a href="#1815">1815</a></td></tr
><tr id="gr_svn139_1816"

><td id="1816"><a href="#1816">1816</a></td></tr
><tr id="gr_svn139_1817"

><td id="1817"><a href="#1817">1817</a></td></tr
><tr id="gr_svn139_1818"

><td id="1818"><a href="#1818">1818</a></td></tr
><tr id="gr_svn139_1819"

><td id="1819"><a href="#1819">1819</a></td></tr
><tr id="gr_svn139_1820"

><td id="1820"><a href="#1820">1820</a></td></tr
><tr id="gr_svn139_1821"

><td id="1821"><a href="#1821">1821</a></td></tr
><tr id="gr_svn139_1822"

><td id="1822"><a href="#1822">1822</a></td></tr
><tr id="gr_svn139_1823"

><td id="1823"><a href="#1823">1823</a></td></tr
><tr id="gr_svn139_1824"

><td id="1824"><a href="#1824">1824</a></td></tr
><tr id="gr_svn139_1825"

><td id="1825"><a href="#1825">1825</a></td></tr
><tr id="gr_svn139_1826"

><td id="1826"><a href="#1826">1826</a></td></tr
><tr id="gr_svn139_1827"

><td id="1827"><a href="#1827">1827</a></td></tr
><tr id="gr_svn139_1828"

><td id="1828"><a href="#1828">1828</a></td></tr
><tr id="gr_svn139_1829"

><td id="1829"><a href="#1829">1829</a></td></tr
><tr id="gr_svn139_1830"

><td id="1830"><a href="#1830">1830</a></td></tr
><tr id="gr_svn139_1831"

><td id="1831"><a href="#1831">1831</a></td></tr
><tr id="gr_svn139_1832"

><td id="1832"><a href="#1832">1832</a></td></tr
><tr id="gr_svn139_1833"

><td id="1833"><a href="#1833">1833</a></td></tr
><tr id="gr_svn139_1834"

><td id="1834"><a href="#1834">1834</a></td></tr
><tr id="gr_svn139_1835"

><td id="1835"><a href="#1835">1835</a></td></tr
><tr id="gr_svn139_1836"

><td id="1836"><a href="#1836">1836</a></td></tr
><tr id="gr_svn139_1837"

><td id="1837"><a href="#1837">1837</a></td></tr
><tr id="gr_svn139_1838"

><td id="1838"><a href="#1838">1838</a></td></tr
><tr id="gr_svn139_1839"

><td id="1839"><a href="#1839">1839</a></td></tr
><tr id="gr_svn139_1840"

><td id="1840"><a href="#1840">1840</a></td></tr
><tr id="gr_svn139_1841"

><td id="1841"><a href="#1841">1841</a></td></tr
><tr id="gr_svn139_1842"

><td id="1842"><a href="#1842">1842</a></td></tr
><tr id="gr_svn139_1843"

><td id="1843"><a href="#1843">1843</a></td></tr
><tr id="gr_svn139_1844"

><td id="1844"><a href="#1844">1844</a></td></tr
><tr id="gr_svn139_1845"

><td id="1845"><a href="#1845">1845</a></td></tr
><tr id="gr_svn139_1846"

><td id="1846"><a href="#1846">1846</a></td></tr
><tr id="gr_svn139_1847"

><td id="1847"><a href="#1847">1847</a></td></tr
><tr id="gr_svn139_1848"

><td id="1848"><a href="#1848">1848</a></td></tr
><tr id="gr_svn139_1849"

><td id="1849"><a href="#1849">1849</a></td></tr
><tr id="gr_svn139_1850"

><td id="1850"><a href="#1850">1850</a></td></tr
><tr id="gr_svn139_1851"

><td id="1851"><a href="#1851">1851</a></td></tr
><tr id="gr_svn139_1852"

><td id="1852"><a href="#1852">1852</a></td></tr
><tr id="gr_svn139_1853"

><td id="1853"><a href="#1853">1853</a></td></tr
><tr id="gr_svn139_1854"

><td id="1854"><a href="#1854">1854</a></td></tr
><tr id="gr_svn139_1855"

><td id="1855"><a href="#1855">1855</a></td></tr
><tr id="gr_svn139_1856"

><td id="1856"><a href="#1856">1856</a></td></tr
><tr id="gr_svn139_1857"

><td id="1857"><a href="#1857">1857</a></td></tr
><tr id="gr_svn139_1858"

><td id="1858"><a href="#1858">1858</a></td></tr
><tr id="gr_svn139_1859"

><td id="1859"><a href="#1859">1859</a></td></tr
><tr id="gr_svn139_1860"

><td id="1860"><a href="#1860">1860</a></td></tr
><tr id="gr_svn139_1861"

><td id="1861"><a href="#1861">1861</a></td></tr
><tr id="gr_svn139_1862"

><td id="1862"><a href="#1862">1862</a></td></tr
><tr id="gr_svn139_1863"

><td id="1863"><a href="#1863">1863</a></td></tr
><tr id="gr_svn139_1864"

><td id="1864"><a href="#1864">1864</a></td></tr
><tr id="gr_svn139_1865"

><td id="1865"><a href="#1865">1865</a></td></tr
><tr id="gr_svn139_1866"

><td id="1866"><a href="#1866">1866</a></td></tr
><tr id="gr_svn139_1867"

><td id="1867"><a href="#1867">1867</a></td></tr
><tr id="gr_svn139_1868"

><td id="1868"><a href="#1868">1868</a></td></tr
><tr id="gr_svn139_1869"

><td id="1869"><a href="#1869">1869</a></td></tr
><tr id="gr_svn139_1870"

><td id="1870"><a href="#1870">1870</a></td></tr
><tr id="gr_svn139_1871"

><td id="1871"><a href="#1871">1871</a></td></tr
><tr id="gr_svn139_1872"

><td id="1872"><a href="#1872">1872</a></td></tr
><tr id="gr_svn139_1873"

><td id="1873"><a href="#1873">1873</a></td></tr
><tr id="gr_svn139_1874"

><td id="1874"><a href="#1874">1874</a></td></tr
><tr id="gr_svn139_1875"

><td id="1875"><a href="#1875">1875</a></td></tr
><tr id="gr_svn139_1876"

><td id="1876"><a href="#1876">1876</a></td></tr
><tr id="gr_svn139_1877"

><td id="1877"><a href="#1877">1877</a></td></tr
><tr id="gr_svn139_1878"

><td id="1878"><a href="#1878">1878</a></td></tr
><tr id="gr_svn139_1879"

><td id="1879"><a href="#1879">1879</a></td></tr
><tr id="gr_svn139_1880"

><td id="1880"><a href="#1880">1880</a></td></tr
><tr id="gr_svn139_1881"

><td id="1881"><a href="#1881">1881</a></td></tr
><tr id="gr_svn139_1882"

><td id="1882"><a href="#1882">1882</a></td></tr
><tr id="gr_svn139_1883"

><td id="1883"><a href="#1883">1883</a></td></tr
><tr id="gr_svn139_1884"

><td id="1884"><a href="#1884">1884</a></td></tr
><tr id="gr_svn139_1885"

><td id="1885"><a href="#1885">1885</a></td></tr
><tr id="gr_svn139_1886"

><td id="1886"><a href="#1886">1886</a></td></tr
><tr id="gr_svn139_1887"

><td id="1887"><a href="#1887">1887</a></td></tr
><tr id="gr_svn139_1888"

><td id="1888"><a href="#1888">1888</a></td></tr
><tr id="gr_svn139_1889"

><td id="1889"><a href="#1889">1889</a></td></tr
><tr id="gr_svn139_1890"

><td id="1890"><a href="#1890">1890</a></td></tr
><tr id="gr_svn139_1891"

><td id="1891"><a href="#1891">1891</a></td></tr
><tr id="gr_svn139_1892"

><td id="1892"><a href="#1892">1892</a></td></tr
><tr id="gr_svn139_1893"

><td id="1893"><a href="#1893">1893</a></td></tr
><tr id="gr_svn139_1894"

><td id="1894"><a href="#1894">1894</a></td></tr
><tr id="gr_svn139_1895"

><td id="1895"><a href="#1895">1895</a></td></tr
><tr id="gr_svn139_1896"

><td id="1896"><a href="#1896">1896</a></td></tr
><tr id="gr_svn139_1897"

><td id="1897"><a href="#1897">1897</a></td></tr
><tr id="gr_svn139_1898"

><td id="1898"><a href="#1898">1898</a></td></tr
><tr id="gr_svn139_1899"

><td id="1899"><a href="#1899">1899</a></td></tr
><tr id="gr_svn139_1900"

><td id="1900"><a href="#1900">1900</a></td></tr
><tr id="gr_svn139_1901"

><td id="1901"><a href="#1901">1901</a></td></tr
><tr id="gr_svn139_1902"

><td id="1902"><a href="#1902">1902</a></td></tr
><tr id="gr_svn139_1903"

><td id="1903"><a href="#1903">1903</a></td></tr
><tr id="gr_svn139_1904"

><td id="1904"><a href="#1904">1904</a></td></tr
><tr id="gr_svn139_1905"

><td id="1905"><a href="#1905">1905</a></td></tr
><tr id="gr_svn139_1906"

><td id="1906"><a href="#1906">1906</a></td></tr
><tr id="gr_svn139_1907"

><td id="1907"><a href="#1907">1907</a></td></tr
><tr id="gr_svn139_1908"

><td id="1908"><a href="#1908">1908</a></td></tr
><tr id="gr_svn139_1909"

><td id="1909"><a href="#1909">1909</a></td></tr
><tr id="gr_svn139_1910"

><td id="1910"><a href="#1910">1910</a></td></tr
><tr id="gr_svn139_1911"

><td id="1911"><a href="#1911">1911</a></td></tr
><tr id="gr_svn139_1912"

><td id="1912"><a href="#1912">1912</a></td></tr
><tr id="gr_svn139_1913"

><td id="1913"><a href="#1913">1913</a></td></tr
><tr id="gr_svn139_1914"

><td id="1914"><a href="#1914">1914</a></td></tr
><tr id="gr_svn139_1915"

><td id="1915"><a href="#1915">1915</a></td></tr
><tr id="gr_svn139_1916"

><td id="1916"><a href="#1916">1916</a></td></tr
><tr id="gr_svn139_1917"

><td id="1917"><a href="#1917">1917</a></td></tr
><tr id="gr_svn139_1918"

><td id="1918"><a href="#1918">1918</a></td></tr
><tr id="gr_svn139_1919"

><td id="1919"><a href="#1919">1919</a></td></tr
><tr id="gr_svn139_1920"

><td id="1920"><a href="#1920">1920</a></td></tr
><tr id="gr_svn139_1921"

><td id="1921"><a href="#1921">1921</a></td></tr
><tr id="gr_svn139_1922"

><td id="1922"><a href="#1922">1922</a></td></tr
><tr id="gr_svn139_1923"

><td id="1923"><a href="#1923">1923</a></td></tr
><tr id="gr_svn139_1924"

><td id="1924"><a href="#1924">1924</a></td></tr
><tr id="gr_svn139_1925"

><td id="1925"><a href="#1925">1925</a></td></tr
><tr id="gr_svn139_1926"

><td id="1926"><a href="#1926">1926</a></td></tr
><tr id="gr_svn139_1927"

><td id="1927"><a href="#1927">1927</a></td></tr
><tr id="gr_svn139_1928"

><td id="1928"><a href="#1928">1928</a></td></tr
><tr id="gr_svn139_1929"

><td id="1929"><a href="#1929">1929</a></td></tr
><tr id="gr_svn139_1930"

><td id="1930"><a href="#1930">1930</a></td></tr
><tr id="gr_svn139_1931"

><td id="1931"><a href="#1931">1931</a></td></tr
><tr id="gr_svn139_1932"

><td id="1932"><a href="#1932">1932</a></td></tr
><tr id="gr_svn139_1933"

><td id="1933"><a href="#1933">1933</a></td></tr
><tr id="gr_svn139_1934"

><td id="1934"><a href="#1934">1934</a></td></tr
><tr id="gr_svn139_1935"

><td id="1935"><a href="#1935">1935</a></td></tr
><tr id="gr_svn139_1936"

><td id="1936"><a href="#1936">1936</a></td></tr
><tr id="gr_svn139_1937"

><td id="1937"><a href="#1937">1937</a></td></tr
><tr id="gr_svn139_1938"

><td id="1938"><a href="#1938">1938</a></td></tr
><tr id="gr_svn139_1939"

><td id="1939"><a href="#1939">1939</a></td></tr
><tr id="gr_svn139_1940"

><td id="1940"><a href="#1940">1940</a></td></tr
><tr id="gr_svn139_1941"

><td id="1941"><a href="#1941">1941</a></td></tr
><tr id="gr_svn139_1942"

><td id="1942"><a href="#1942">1942</a></td></tr
><tr id="gr_svn139_1943"

><td id="1943"><a href="#1943">1943</a></td></tr
><tr id="gr_svn139_1944"

><td id="1944"><a href="#1944">1944</a></td></tr
><tr id="gr_svn139_1945"

><td id="1945"><a href="#1945">1945</a></td></tr
><tr id="gr_svn139_1946"

><td id="1946"><a href="#1946">1946</a></td></tr
><tr id="gr_svn139_1947"

><td id="1947"><a href="#1947">1947</a></td></tr
><tr id="gr_svn139_1948"

><td id="1948"><a href="#1948">1948</a></td></tr
><tr id="gr_svn139_1949"

><td id="1949"><a href="#1949">1949</a></td></tr
><tr id="gr_svn139_1950"

><td id="1950"><a href="#1950">1950</a></td></tr
><tr id="gr_svn139_1951"

><td id="1951"><a href="#1951">1951</a></td></tr
><tr id="gr_svn139_1952"

><td id="1952"><a href="#1952">1952</a></td></tr
><tr id="gr_svn139_1953"

><td id="1953"><a href="#1953">1953</a></td></tr
><tr id="gr_svn139_1954"

><td id="1954"><a href="#1954">1954</a></td></tr
><tr id="gr_svn139_1955"

><td id="1955"><a href="#1955">1955</a></td></tr
><tr id="gr_svn139_1956"

><td id="1956"><a href="#1956">1956</a></td></tr
><tr id="gr_svn139_1957"

><td id="1957"><a href="#1957">1957</a></td></tr
><tr id="gr_svn139_1958"

><td id="1958"><a href="#1958">1958</a></td></tr
><tr id="gr_svn139_1959"

><td id="1959"><a href="#1959">1959</a></td></tr
><tr id="gr_svn139_1960"

><td id="1960"><a href="#1960">1960</a></td></tr
><tr id="gr_svn139_1961"

><td id="1961"><a href="#1961">1961</a></td></tr
><tr id="gr_svn139_1962"

><td id="1962"><a href="#1962">1962</a></td></tr
><tr id="gr_svn139_1963"

><td id="1963"><a href="#1963">1963</a></td></tr
><tr id="gr_svn139_1964"

><td id="1964"><a href="#1964">1964</a></td></tr
><tr id="gr_svn139_1965"

><td id="1965"><a href="#1965">1965</a></td></tr
><tr id="gr_svn139_1966"

><td id="1966"><a href="#1966">1966</a></td></tr
><tr id="gr_svn139_1967"

><td id="1967"><a href="#1967">1967</a></td></tr
><tr id="gr_svn139_1968"

><td id="1968"><a href="#1968">1968</a></td></tr
><tr id="gr_svn139_1969"

><td id="1969"><a href="#1969">1969</a></td></tr
><tr id="gr_svn139_1970"

><td id="1970"><a href="#1970">1970</a></td></tr
><tr id="gr_svn139_1971"

><td id="1971"><a href="#1971">1971</a></td></tr
><tr id="gr_svn139_1972"

><td id="1972"><a href="#1972">1972</a></td></tr
><tr id="gr_svn139_1973"

><td id="1973"><a href="#1973">1973</a></td></tr
><tr id="gr_svn139_1974"

><td id="1974"><a href="#1974">1974</a></td></tr
><tr id="gr_svn139_1975"

><td id="1975"><a href="#1975">1975</a></td></tr
><tr id="gr_svn139_1976"

><td id="1976"><a href="#1976">1976</a></td></tr
><tr id="gr_svn139_1977"

><td id="1977"><a href="#1977">1977</a></td></tr
><tr id="gr_svn139_1978"

><td id="1978"><a href="#1978">1978</a></td></tr
><tr id="gr_svn139_1979"

><td id="1979"><a href="#1979">1979</a></td></tr
><tr id="gr_svn139_1980"

><td id="1980"><a href="#1980">1980</a></td></tr
><tr id="gr_svn139_1981"

><td id="1981"><a href="#1981">1981</a></td></tr
><tr id="gr_svn139_1982"

><td id="1982"><a href="#1982">1982</a></td></tr
><tr id="gr_svn139_1983"

><td id="1983"><a href="#1983">1983</a></td></tr
><tr id="gr_svn139_1984"

><td id="1984"><a href="#1984">1984</a></td></tr
><tr id="gr_svn139_1985"

><td id="1985"><a href="#1985">1985</a></td></tr
><tr id="gr_svn139_1986"

><td id="1986"><a href="#1986">1986</a></td></tr
><tr id="gr_svn139_1987"

><td id="1987"><a href="#1987">1987</a></td></tr
><tr id="gr_svn139_1988"

><td id="1988"><a href="#1988">1988</a></td></tr
><tr id="gr_svn139_1989"

><td id="1989"><a href="#1989">1989</a></td></tr
><tr id="gr_svn139_1990"

><td id="1990"><a href="#1990">1990</a></td></tr
><tr id="gr_svn139_1991"

><td id="1991"><a href="#1991">1991</a></td></tr
><tr id="gr_svn139_1992"

><td id="1992"><a href="#1992">1992</a></td></tr
><tr id="gr_svn139_1993"

><td id="1993"><a href="#1993">1993</a></td></tr
><tr id="gr_svn139_1994"

><td id="1994"><a href="#1994">1994</a></td></tr
><tr id="gr_svn139_1995"

><td id="1995"><a href="#1995">1995</a></td></tr
><tr id="gr_svn139_1996"

><td id="1996"><a href="#1996">1996</a></td></tr
><tr id="gr_svn139_1997"

><td id="1997"><a href="#1997">1997</a></td></tr
><tr id="gr_svn139_1998"

><td id="1998"><a href="#1998">1998</a></td></tr
><tr id="gr_svn139_1999"

><td id="1999"><a href="#1999">1999</a></td></tr
><tr id="gr_svn139_2000"

><td id="2000"><a href="#2000">2000</a></td></tr
><tr id="gr_svn139_2001"

><td id="2001"><a href="#2001">2001</a></td></tr
><tr id="gr_svn139_2002"

><td id="2002"><a href="#2002">2002</a></td></tr
><tr id="gr_svn139_2003"

><td id="2003"><a href="#2003">2003</a></td></tr
><tr id="gr_svn139_2004"

><td id="2004"><a href="#2004">2004</a></td></tr
><tr id="gr_svn139_2005"

><td id="2005"><a href="#2005">2005</a></td></tr
><tr id="gr_svn139_2006"

><td id="2006"><a href="#2006">2006</a></td></tr
><tr id="gr_svn139_2007"

><td id="2007"><a href="#2007">2007</a></td></tr
><tr id="gr_svn139_2008"

><td id="2008"><a href="#2008">2008</a></td></tr
><tr id="gr_svn139_2009"

><td id="2009"><a href="#2009">2009</a></td></tr
><tr id="gr_svn139_2010"

><td id="2010"><a href="#2010">2010</a></td></tr
><tr id="gr_svn139_2011"

><td id="2011"><a href="#2011">2011</a></td></tr
><tr id="gr_svn139_2012"

><td id="2012"><a href="#2012">2012</a></td></tr
><tr id="gr_svn139_2013"

><td id="2013"><a href="#2013">2013</a></td></tr
><tr id="gr_svn139_2014"

><td id="2014"><a href="#2014">2014</a></td></tr
><tr id="gr_svn139_2015"

><td id="2015"><a href="#2015">2015</a></td></tr
><tr id="gr_svn139_2016"

><td id="2016"><a href="#2016">2016</a></td></tr
><tr id="gr_svn139_2017"

><td id="2017"><a href="#2017">2017</a></td></tr
><tr id="gr_svn139_2018"

><td id="2018"><a href="#2018">2018</a></td></tr
><tr id="gr_svn139_2019"

><td id="2019"><a href="#2019">2019</a></td></tr
><tr id="gr_svn139_2020"

><td id="2020"><a href="#2020">2020</a></td></tr
><tr id="gr_svn139_2021"

><td id="2021"><a href="#2021">2021</a></td></tr
><tr id="gr_svn139_2022"

><td id="2022"><a href="#2022">2022</a></td></tr
><tr id="gr_svn139_2023"

><td id="2023"><a href="#2023">2023</a></td></tr
><tr id="gr_svn139_2024"

><td id="2024"><a href="#2024">2024</a></td></tr
><tr id="gr_svn139_2025"

><td id="2025"><a href="#2025">2025</a></td></tr
><tr id="gr_svn139_2026"

><td id="2026"><a href="#2026">2026</a></td></tr
><tr id="gr_svn139_2027"

><td id="2027"><a href="#2027">2027</a></td></tr
><tr id="gr_svn139_2028"

><td id="2028"><a href="#2028">2028</a></td></tr
><tr id="gr_svn139_2029"

><td id="2029"><a href="#2029">2029</a></td></tr
><tr id="gr_svn139_2030"

><td id="2030"><a href="#2030">2030</a></td></tr
><tr id="gr_svn139_2031"

><td id="2031"><a href="#2031">2031</a></td></tr
><tr id="gr_svn139_2032"

><td id="2032"><a href="#2032">2032</a></td></tr
><tr id="gr_svn139_2033"

><td id="2033"><a href="#2033">2033</a></td></tr
><tr id="gr_svn139_2034"

><td id="2034"><a href="#2034">2034</a></td></tr
><tr id="gr_svn139_2035"

><td id="2035"><a href="#2035">2035</a></td></tr
><tr id="gr_svn139_2036"

><td id="2036"><a href="#2036">2036</a></td></tr
><tr id="gr_svn139_2037"

><td id="2037"><a href="#2037">2037</a></td></tr
><tr id="gr_svn139_2038"

><td id="2038"><a href="#2038">2038</a></td></tr
><tr id="gr_svn139_2039"

><td id="2039"><a href="#2039">2039</a></td></tr
><tr id="gr_svn139_2040"

><td id="2040"><a href="#2040">2040</a></td></tr
><tr id="gr_svn139_2041"

><td id="2041"><a href="#2041">2041</a></td></tr
><tr id="gr_svn139_2042"

><td id="2042"><a href="#2042">2042</a></td></tr
><tr id="gr_svn139_2043"

><td id="2043"><a href="#2043">2043</a></td></tr
><tr id="gr_svn139_2044"

><td id="2044"><a href="#2044">2044</a></td></tr
><tr id="gr_svn139_2045"

><td id="2045"><a href="#2045">2045</a></td></tr
><tr id="gr_svn139_2046"

><td id="2046"><a href="#2046">2046</a></td></tr
><tr id="gr_svn139_2047"

><td id="2047"><a href="#2047">2047</a></td></tr
><tr id="gr_svn139_2048"

><td id="2048"><a href="#2048">2048</a></td></tr
><tr id="gr_svn139_2049"

><td id="2049"><a href="#2049">2049</a></td></tr
><tr id="gr_svn139_2050"

><td id="2050"><a href="#2050">2050</a></td></tr
><tr id="gr_svn139_2051"

><td id="2051"><a href="#2051">2051</a></td></tr
><tr id="gr_svn139_2052"

><td id="2052"><a href="#2052">2052</a></td></tr
><tr id="gr_svn139_2053"

><td id="2053"><a href="#2053">2053</a></td></tr
><tr id="gr_svn139_2054"

><td id="2054"><a href="#2054">2054</a></td></tr
><tr id="gr_svn139_2055"

><td id="2055"><a href="#2055">2055</a></td></tr
><tr id="gr_svn139_2056"

><td id="2056"><a href="#2056">2056</a></td></tr
><tr id="gr_svn139_2057"

><td id="2057"><a href="#2057">2057</a></td></tr
><tr id="gr_svn139_2058"

><td id="2058"><a href="#2058">2058</a></td></tr
><tr id="gr_svn139_2059"

><td id="2059"><a href="#2059">2059</a></td></tr
><tr id="gr_svn139_2060"

><td id="2060"><a href="#2060">2060</a></td></tr
><tr id="gr_svn139_2061"

><td id="2061"><a href="#2061">2061</a></td></tr
><tr id="gr_svn139_2062"

><td id="2062"><a href="#2062">2062</a></td></tr
><tr id="gr_svn139_2063"

><td id="2063"><a href="#2063">2063</a></td></tr
><tr id="gr_svn139_2064"

><td id="2064"><a href="#2064">2064</a></td></tr
><tr id="gr_svn139_2065"

><td id="2065"><a href="#2065">2065</a></td></tr
><tr id="gr_svn139_2066"

><td id="2066"><a href="#2066">2066</a></td></tr
><tr id="gr_svn139_2067"

><td id="2067"><a href="#2067">2067</a></td></tr
><tr id="gr_svn139_2068"

><td id="2068"><a href="#2068">2068</a></td></tr
><tr id="gr_svn139_2069"

><td id="2069"><a href="#2069">2069</a></td></tr
><tr id="gr_svn139_2070"

><td id="2070"><a href="#2070">2070</a></td></tr
><tr id="gr_svn139_2071"

><td id="2071"><a href="#2071">2071</a></td></tr
><tr id="gr_svn139_2072"

><td id="2072"><a href="#2072">2072</a></td></tr
><tr id="gr_svn139_2073"

><td id="2073"><a href="#2073">2073</a></td></tr
><tr id="gr_svn139_2074"

><td id="2074"><a href="#2074">2074</a></td></tr
><tr id="gr_svn139_2075"

><td id="2075"><a href="#2075">2075</a></td></tr
><tr id="gr_svn139_2076"

><td id="2076"><a href="#2076">2076</a></td></tr
><tr id="gr_svn139_2077"

><td id="2077"><a href="#2077">2077</a></td></tr
><tr id="gr_svn139_2078"

><td id="2078"><a href="#2078">2078</a></td></tr
><tr id="gr_svn139_2079"

><td id="2079"><a href="#2079">2079</a></td></tr
><tr id="gr_svn139_2080"

><td id="2080"><a href="#2080">2080</a></td></tr
><tr id="gr_svn139_2081"

><td id="2081"><a href="#2081">2081</a></td></tr
><tr id="gr_svn139_2082"

><td id="2082"><a href="#2082">2082</a></td></tr
><tr id="gr_svn139_2083"

><td id="2083"><a href="#2083">2083</a></td></tr
><tr id="gr_svn139_2084"

><td id="2084"><a href="#2084">2084</a></td></tr
><tr id="gr_svn139_2085"

><td id="2085"><a href="#2085">2085</a></td></tr
><tr id="gr_svn139_2086"

><td id="2086"><a href="#2086">2086</a></td></tr
><tr id="gr_svn139_2087"

><td id="2087"><a href="#2087">2087</a></td></tr
><tr id="gr_svn139_2088"

><td id="2088"><a href="#2088">2088</a></td></tr
><tr id="gr_svn139_2089"

><td id="2089"><a href="#2089">2089</a></td></tr
><tr id="gr_svn139_2090"

><td id="2090"><a href="#2090">2090</a></td></tr
><tr id="gr_svn139_2091"

><td id="2091"><a href="#2091">2091</a></td></tr
><tr id="gr_svn139_2092"

><td id="2092"><a href="#2092">2092</a></td></tr
><tr id="gr_svn139_2093"

><td id="2093"><a href="#2093">2093</a></td></tr
><tr id="gr_svn139_2094"

><td id="2094"><a href="#2094">2094</a></td></tr
><tr id="gr_svn139_2095"

><td id="2095"><a href="#2095">2095</a></td></tr
><tr id="gr_svn139_2096"

><td id="2096"><a href="#2096">2096</a></td></tr
><tr id="gr_svn139_2097"

><td id="2097"><a href="#2097">2097</a></td></tr
><tr id="gr_svn139_2098"

><td id="2098"><a href="#2098">2098</a></td></tr
><tr id="gr_svn139_2099"

><td id="2099"><a href="#2099">2099</a></td></tr
><tr id="gr_svn139_2100"

><td id="2100"><a href="#2100">2100</a></td></tr
><tr id="gr_svn139_2101"

><td id="2101"><a href="#2101">2101</a></td></tr
><tr id="gr_svn139_2102"

><td id="2102"><a href="#2102">2102</a></td></tr
><tr id="gr_svn139_2103"

><td id="2103"><a href="#2103">2103</a></td></tr
><tr id="gr_svn139_2104"

><td id="2104"><a href="#2104">2104</a></td></tr
><tr id="gr_svn139_2105"

><td id="2105"><a href="#2105">2105</a></td></tr
><tr id="gr_svn139_2106"

><td id="2106"><a href="#2106">2106</a></td></tr
><tr id="gr_svn139_2107"

><td id="2107"><a href="#2107">2107</a></td></tr
><tr id="gr_svn139_2108"

><td id="2108"><a href="#2108">2108</a></td></tr
><tr id="gr_svn139_2109"

><td id="2109"><a href="#2109">2109</a></td></tr
><tr id="gr_svn139_2110"

><td id="2110"><a href="#2110">2110</a></td></tr
><tr id="gr_svn139_2111"

><td id="2111"><a href="#2111">2111</a></td></tr
><tr id="gr_svn139_2112"

><td id="2112"><a href="#2112">2112</a></td></tr
><tr id="gr_svn139_2113"

><td id="2113"><a href="#2113">2113</a></td></tr
><tr id="gr_svn139_2114"

><td id="2114"><a href="#2114">2114</a></td></tr
><tr id="gr_svn139_2115"

><td id="2115"><a href="#2115">2115</a></td></tr
><tr id="gr_svn139_2116"

><td id="2116"><a href="#2116">2116</a></td></tr
><tr id="gr_svn139_2117"

><td id="2117"><a href="#2117">2117</a></td></tr
><tr id="gr_svn139_2118"

><td id="2118"><a href="#2118">2118</a></td></tr
><tr id="gr_svn139_2119"

><td id="2119"><a href="#2119">2119</a></td></tr
><tr id="gr_svn139_2120"

><td id="2120"><a href="#2120">2120</a></td></tr
><tr id="gr_svn139_2121"

><td id="2121"><a href="#2121">2121</a></td></tr
><tr id="gr_svn139_2122"

><td id="2122"><a href="#2122">2122</a></td></tr
><tr id="gr_svn139_2123"

><td id="2123"><a href="#2123">2123</a></td></tr
><tr id="gr_svn139_2124"

><td id="2124"><a href="#2124">2124</a></td></tr
><tr id="gr_svn139_2125"

><td id="2125"><a href="#2125">2125</a></td></tr
><tr id="gr_svn139_2126"

><td id="2126"><a href="#2126">2126</a></td></tr
><tr id="gr_svn139_2127"

><td id="2127"><a href="#2127">2127</a></td></tr
><tr id="gr_svn139_2128"

><td id="2128"><a href="#2128">2128</a></td></tr
><tr id="gr_svn139_2129"

><td id="2129"><a href="#2129">2129</a></td></tr
><tr id="gr_svn139_2130"

><td id="2130"><a href="#2130">2130</a></td></tr
><tr id="gr_svn139_2131"

><td id="2131"><a href="#2131">2131</a></td></tr
><tr id="gr_svn139_2132"

><td id="2132"><a href="#2132">2132</a></td></tr
><tr id="gr_svn139_2133"

><td id="2133"><a href="#2133">2133</a></td></tr
><tr id="gr_svn139_2134"

><td id="2134"><a href="#2134">2134</a></td></tr
><tr id="gr_svn139_2135"

><td id="2135"><a href="#2135">2135</a></td></tr
><tr id="gr_svn139_2136"

><td id="2136"><a href="#2136">2136</a></td></tr
><tr id="gr_svn139_2137"

><td id="2137"><a href="#2137">2137</a></td></tr
><tr id="gr_svn139_2138"

><td id="2138"><a href="#2138">2138</a></td></tr
><tr id="gr_svn139_2139"

><td id="2139"><a href="#2139">2139</a></td></tr
><tr id="gr_svn139_2140"

><td id="2140"><a href="#2140">2140</a></td></tr
><tr id="gr_svn139_2141"

><td id="2141"><a href="#2141">2141</a></td></tr
><tr id="gr_svn139_2142"

><td id="2142"><a href="#2142">2142</a></td></tr
><tr id="gr_svn139_2143"

><td id="2143"><a href="#2143">2143</a></td></tr
><tr id="gr_svn139_2144"

><td id="2144"><a href="#2144">2144</a></td></tr
><tr id="gr_svn139_2145"

><td id="2145"><a href="#2145">2145</a></td></tr
><tr id="gr_svn139_2146"

><td id="2146"><a href="#2146">2146</a></td></tr
><tr id="gr_svn139_2147"

><td id="2147"><a href="#2147">2147</a></td></tr
><tr id="gr_svn139_2148"

><td id="2148"><a href="#2148">2148</a></td></tr
><tr id="gr_svn139_2149"

><td id="2149"><a href="#2149">2149</a></td></tr
><tr id="gr_svn139_2150"

><td id="2150"><a href="#2150">2150</a></td></tr
><tr id="gr_svn139_2151"

><td id="2151"><a href="#2151">2151</a></td></tr
><tr id="gr_svn139_2152"

><td id="2152"><a href="#2152">2152</a></td></tr
><tr id="gr_svn139_2153"

><td id="2153"><a href="#2153">2153</a></td></tr
><tr id="gr_svn139_2154"

><td id="2154"><a href="#2154">2154</a></td></tr
><tr id="gr_svn139_2155"

><td id="2155"><a href="#2155">2155</a></td></tr
><tr id="gr_svn139_2156"

><td id="2156"><a href="#2156">2156</a></td></tr
><tr id="gr_svn139_2157"

><td id="2157"><a href="#2157">2157</a></td></tr
><tr id="gr_svn139_2158"

><td id="2158"><a href="#2158">2158</a></td></tr
><tr id="gr_svn139_2159"

><td id="2159"><a href="#2159">2159</a></td></tr
><tr id="gr_svn139_2160"

><td id="2160"><a href="#2160">2160</a></td></tr
><tr id="gr_svn139_2161"

><td id="2161"><a href="#2161">2161</a></td></tr
><tr id="gr_svn139_2162"

><td id="2162"><a href="#2162">2162</a></td></tr
><tr id="gr_svn139_2163"

><td id="2163"><a href="#2163">2163</a></td></tr
><tr id="gr_svn139_2164"

><td id="2164"><a href="#2164">2164</a></td></tr
><tr id="gr_svn139_2165"

><td id="2165"><a href="#2165">2165</a></td></tr
><tr id="gr_svn139_2166"

><td id="2166"><a href="#2166">2166</a></td></tr
><tr id="gr_svn139_2167"

><td id="2167"><a href="#2167">2167</a></td></tr
><tr id="gr_svn139_2168"

><td id="2168"><a href="#2168">2168</a></td></tr
><tr id="gr_svn139_2169"

><td id="2169"><a href="#2169">2169</a></td></tr
><tr id="gr_svn139_2170"

><td id="2170"><a href="#2170">2170</a></td></tr
><tr id="gr_svn139_2171"

><td id="2171"><a href="#2171">2171</a></td></tr
><tr id="gr_svn139_2172"

><td id="2172"><a href="#2172">2172</a></td></tr
><tr id="gr_svn139_2173"

><td id="2173"><a href="#2173">2173</a></td></tr
><tr id="gr_svn139_2174"

><td id="2174"><a href="#2174">2174</a></td></tr
><tr id="gr_svn139_2175"

><td id="2175"><a href="#2175">2175</a></td></tr
><tr id="gr_svn139_2176"

><td id="2176"><a href="#2176">2176</a></td></tr
><tr id="gr_svn139_2177"

><td id="2177"><a href="#2177">2177</a></td></tr
><tr id="gr_svn139_2178"

><td id="2178"><a href="#2178">2178</a></td></tr
><tr id="gr_svn139_2179"

><td id="2179"><a href="#2179">2179</a></td></tr
><tr id="gr_svn139_2180"

><td id="2180"><a href="#2180">2180</a></td></tr
><tr id="gr_svn139_2181"

><td id="2181"><a href="#2181">2181</a></td></tr
><tr id="gr_svn139_2182"

><td id="2182"><a href="#2182">2182</a></td></tr
><tr id="gr_svn139_2183"

><td id="2183"><a href="#2183">2183</a></td></tr
><tr id="gr_svn139_2184"

><td id="2184"><a href="#2184">2184</a></td></tr
><tr id="gr_svn139_2185"

><td id="2185"><a href="#2185">2185</a></td></tr
><tr id="gr_svn139_2186"

><td id="2186"><a href="#2186">2186</a></td></tr
><tr id="gr_svn139_2187"

><td id="2187"><a href="#2187">2187</a></td></tr
><tr id="gr_svn139_2188"

><td id="2188"><a href="#2188">2188</a></td></tr
><tr id="gr_svn139_2189"

><td id="2189"><a href="#2189">2189</a></td></tr
><tr id="gr_svn139_2190"

><td id="2190"><a href="#2190">2190</a></td></tr
><tr id="gr_svn139_2191"

><td id="2191"><a href="#2191">2191</a></td></tr
><tr id="gr_svn139_2192"

><td id="2192"><a href="#2192">2192</a></td></tr
><tr id="gr_svn139_2193"

><td id="2193"><a href="#2193">2193</a></td></tr
><tr id="gr_svn139_2194"

><td id="2194"><a href="#2194">2194</a></td></tr
><tr id="gr_svn139_2195"

><td id="2195"><a href="#2195">2195</a></td></tr
><tr id="gr_svn139_2196"

><td id="2196"><a href="#2196">2196</a></td></tr
><tr id="gr_svn139_2197"

><td id="2197"><a href="#2197">2197</a></td></tr
><tr id="gr_svn139_2198"

><td id="2198"><a href="#2198">2198</a></td></tr
><tr id="gr_svn139_2199"

><td id="2199"><a href="#2199">2199</a></td></tr
><tr id="gr_svn139_2200"

><td id="2200"><a href="#2200">2200</a></td></tr
><tr id="gr_svn139_2201"

><td id="2201"><a href="#2201">2201</a></td></tr
><tr id="gr_svn139_2202"

><td id="2202"><a href="#2202">2202</a></td></tr
><tr id="gr_svn139_2203"

><td id="2203"><a href="#2203">2203</a></td></tr
><tr id="gr_svn139_2204"

><td id="2204"><a href="#2204">2204</a></td></tr
><tr id="gr_svn139_2205"

><td id="2205"><a href="#2205">2205</a></td></tr
><tr id="gr_svn139_2206"

><td id="2206"><a href="#2206">2206</a></td></tr
><tr id="gr_svn139_2207"

><td id="2207"><a href="#2207">2207</a></td></tr
><tr id="gr_svn139_2208"

><td id="2208"><a href="#2208">2208</a></td></tr
><tr id="gr_svn139_2209"

><td id="2209"><a href="#2209">2209</a></td></tr
><tr id="gr_svn139_2210"

><td id="2210"><a href="#2210">2210</a></td></tr
><tr id="gr_svn139_2211"

><td id="2211"><a href="#2211">2211</a></td></tr
><tr id="gr_svn139_2212"

><td id="2212"><a href="#2212">2212</a></td></tr
><tr id="gr_svn139_2213"

><td id="2213"><a href="#2213">2213</a></td></tr
><tr id="gr_svn139_2214"

><td id="2214"><a href="#2214">2214</a></td></tr
><tr id="gr_svn139_2215"

><td id="2215"><a href="#2215">2215</a></td></tr
><tr id="gr_svn139_2216"

><td id="2216"><a href="#2216">2216</a></td></tr
><tr id="gr_svn139_2217"

><td id="2217"><a href="#2217">2217</a></td></tr
><tr id="gr_svn139_2218"

><td id="2218"><a href="#2218">2218</a></td></tr
><tr id="gr_svn139_2219"

><td id="2219"><a href="#2219">2219</a></td></tr
><tr id="gr_svn139_2220"

><td id="2220"><a href="#2220">2220</a></td></tr
><tr id="gr_svn139_2221"

><td id="2221"><a href="#2221">2221</a></td></tr
><tr id="gr_svn139_2222"

><td id="2222"><a href="#2222">2222</a></td></tr
><tr id="gr_svn139_2223"

><td id="2223"><a href="#2223">2223</a></td></tr
><tr id="gr_svn139_2224"

><td id="2224"><a href="#2224">2224</a></td></tr
><tr id="gr_svn139_2225"

><td id="2225"><a href="#2225">2225</a></td></tr
><tr id="gr_svn139_2226"

><td id="2226"><a href="#2226">2226</a></td></tr
><tr id="gr_svn139_2227"

><td id="2227"><a href="#2227">2227</a></td></tr
><tr id="gr_svn139_2228"

><td id="2228"><a href="#2228">2228</a></td></tr
><tr id="gr_svn139_2229"

><td id="2229"><a href="#2229">2229</a></td></tr
><tr id="gr_svn139_2230"

><td id="2230"><a href="#2230">2230</a></td></tr
><tr id="gr_svn139_2231"

><td id="2231"><a href="#2231">2231</a></td></tr
><tr id="gr_svn139_2232"

><td id="2232"><a href="#2232">2232</a></td></tr
><tr id="gr_svn139_2233"

><td id="2233"><a href="#2233">2233</a></td></tr
><tr id="gr_svn139_2234"

><td id="2234"><a href="#2234">2234</a></td></tr
><tr id="gr_svn139_2235"

><td id="2235"><a href="#2235">2235</a></td></tr
><tr id="gr_svn139_2236"

><td id="2236"><a href="#2236">2236</a></td></tr
><tr id="gr_svn139_2237"

><td id="2237"><a href="#2237">2237</a></td></tr
><tr id="gr_svn139_2238"

><td id="2238"><a href="#2238">2238</a></td></tr
><tr id="gr_svn139_2239"

><td id="2239"><a href="#2239">2239</a></td></tr
><tr id="gr_svn139_2240"

><td id="2240"><a href="#2240">2240</a></td></tr
><tr id="gr_svn139_2241"

><td id="2241"><a href="#2241">2241</a></td></tr
><tr id="gr_svn139_2242"

><td id="2242"><a href="#2242">2242</a></td></tr
><tr id="gr_svn139_2243"

><td id="2243"><a href="#2243">2243</a></td></tr
><tr id="gr_svn139_2244"

><td id="2244"><a href="#2244">2244</a></td></tr
><tr id="gr_svn139_2245"

><td id="2245"><a href="#2245">2245</a></td></tr
><tr id="gr_svn139_2246"

><td id="2246"><a href="#2246">2246</a></td></tr
><tr id="gr_svn139_2247"

><td id="2247"><a href="#2247">2247</a></td></tr
><tr id="gr_svn139_2248"

><td id="2248"><a href="#2248">2248</a></td></tr
><tr id="gr_svn139_2249"

><td id="2249"><a href="#2249">2249</a></td></tr
><tr id="gr_svn139_2250"

><td id="2250"><a href="#2250">2250</a></td></tr
><tr id="gr_svn139_2251"

><td id="2251"><a href="#2251">2251</a></td></tr
><tr id="gr_svn139_2252"

><td id="2252"><a href="#2252">2252</a></td></tr
><tr id="gr_svn139_2253"

><td id="2253"><a href="#2253">2253</a></td></tr
><tr id="gr_svn139_2254"

><td id="2254"><a href="#2254">2254</a></td></tr
><tr id="gr_svn139_2255"

><td id="2255"><a href="#2255">2255</a></td></tr
><tr id="gr_svn139_2256"

><td id="2256"><a href="#2256">2256</a></td></tr
><tr id="gr_svn139_2257"

><td id="2257"><a href="#2257">2257</a></td></tr
><tr id="gr_svn139_2258"

><td id="2258"><a href="#2258">2258</a></td></tr
><tr id="gr_svn139_2259"

><td id="2259"><a href="#2259">2259</a></td></tr
><tr id="gr_svn139_2260"

><td id="2260"><a href="#2260">2260</a></td></tr
><tr id="gr_svn139_2261"

><td id="2261"><a href="#2261">2261</a></td></tr
><tr id="gr_svn139_2262"

><td id="2262"><a href="#2262">2262</a></td></tr
><tr id="gr_svn139_2263"

><td id="2263"><a href="#2263">2263</a></td></tr
><tr id="gr_svn139_2264"

><td id="2264"><a href="#2264">2264</a></td></tr
><tr id="gr_svn139_2265"

><td id="2265"><a href="#2265">2265</a></td></tr
><tr id="gr_svn139_2266"

><td id="2266"><a href="#2266">2266</a></td></tr
><tr id="gr_svn139_2267"

><td id="2267"><a href="#2267">2267</a></td></tr
><tr id="gr_svn139_2268"

><td id="2268"><a href="#2268">2268</a></td></tr
><tr id="gr_svn139_2269"

><td id="2269"><a href="#2269">2269</a></td></tr
><tr id="gr_svn139_2270"

><td id="2270"><a href="#2270">2270</a></td></tr
><tr id="gr_svn139_2271"

><td id="2271"><a href="#2271">2271</a></td></tr
><tr id="gr_svn139_2272"

><td id="2272"><a href="#2272">2272</a></td></tr
><tr id="gr_svn139_2273"

><td id="2273"><a href="#2273">2273</a></td></tr
><tr id="gr_svn139_2274"

><td id="2274"><a href="#2274">2274</a></td></tr
><tr id="gr_svn139_2275"

><td id="2275"><a href="#2275">2275</a></td></tr
><tr id="gr_svn139_2276"

><td id="2276"><a href="#2276">2276</a></td></tr
><tr id="gr_svn139_2277"

><td id="2277"><a href="#2277">2277</a></td></tr
><tr id="gr_svn139_2278"

><td id="2278"><a href="#2278">2278</a></td></tr
><tr id="gr_svn139_2279"

><td id="2279"><a href="#2279">2279</a></td></tr
><tr id="gr_svn139_2280"

><td id="2280"><a href="#2280">2280</a></td></tr
><tr id="gr_svn139_2281"

><td id="2281"><a href="#2281">2281</a></td></tr
><tr id="gr_svn139_2282"

><td id="2282"><a href="#2282">2282</a></td></tr
><tr id="gr_svn139_2283"

><td id="2283"><a href="#2283">2283</a></td></tr
><tr id="gr_svn139_2284"

><td id="2284"><a href="#2284">2284</a></td></tr
><tr id="gr_svn139_2285"

><td id="2285"><a href="#2285">2285</a></td></tr
><tr id="gr_svn139_2286"

><td id="2286"><a href="#2286">2286</a></td></tr
><tr id="gr_svn139_2287"

><td id="2287"><a href="#2287">2287</a></td></tr
><tr id="gr_svn139_2288"

><td id="2288"><a href="#2288">2288</a></td></tr
><tr id="gr_svn139_2289"

><td id="2289"><a href="#2289">2289</a></td></tr
><tr id="gr_svn139_2290"

><td id="2290"><a href="#2290">2290</a></td></tr
><tr id="gr_svn139_2291"

><td id="2291"><a href="#2291">2291</a></td></tr
><tr id="gr_svn139_2292"

><td id="2292"><a href="#2292">2292</a></td></tr
><tr id="gr_svn139_2293"

><td id="2293"><a href="#2293">2293</a></td></tr
><tr id="gr_svn139_2294"

><td id="2294"><a href="#2294">2294</a></td></tr
><tr id="gr_svn139_2295"

><td id="2295"><a href="#2295">2295</a></td></tr
><tr id="gr_svn139_2296"

><td id="2296"><a href="#2296">2296</a></td></tr
><tr id="gr_svn139_2297"

><td id="2297"><a href="#2297">2297</a></td></tr
><tr id="gr_svn139_2298"

><td id="2298"><a href="#2298">2298</a></td></tr
><tr id="gr_svn139_2299"

><td id="2299"><a href="#2299">2299</a></td></tr
><tr id="gr_svn139_2300"

><td id="2300"><a href="#2300">2300</a></td></tr
><tr id="gr_svn139_2301"

><td id="2301"><a href="#2301">2301</a></td></tr
><tr id="gr_svn139_2302"

><td id="2302"><a href="#2302">2302</a></td></tr
><tr id="gr_svn139_2303"

><td id="2303"><a href="#2303">2303</a></td></tr
><tr id="gr_svn139_2304"

><td id="2304"><a href="#2304">2304</a></td></tr
><tr id="gr_svn139_2305"

><td id="2305"><a href="#2305">2305</a></td></tr
><tr id="gr_svn139_2306"

><td id="2306"><a href="#2306">2306</a></td></tr
><tr id="gr_svn139_2307"

><td id="2307"><a href="#2307">2307</a></td></tr
><tr id="gr_svn139_2308"

><td id="2308"><a href="#2308">2308</a></td></tr
><tr id="gr_svn139_2309"

><td id="2309"><a href="#2309">2309</a></td></tr
><tr id="gr_svn139_2310"

><td id="2310"><a href="#2310">2310</a></td></tr
><tr id="gr_svn139_2311"

><td id="2311"><a href="#2311">2311</a></td></tr
><tr id="gr_svn139_2312"

><td id="2312"><a href="#2312">2312</a></td></tr
><tr id="gr_svn139_2313"

><td id="2313"><a href="#2313">2313</a></td></tr
><tr id="gr_svn139_2314"

><td id="2314"><a href="#2314">2314</a></td></tr
><tr id="gr_svn139_2315"

><td id="2315"><a href="#2315">2315</a></td></tr
><tr id="gr_svn139_2316"

><td id="2316"><a href="#2316">2316</a></td></tr
><tr id="gr_svn139_2317"

><td id="2317"><a href="#2317">2317</a></td></tr
><tr id="gr_svn139_2318"

><td id="2318"><a href="#2318">2318</a></td></tr
><tr id="gr_svn139_2319"

><td id="2319"><a href="#2319">2319</a></td></tr
><tr id="gr_svn139_2320"

><td id="2320"><a href="#2320">2320</a></td></tr
><tr id="gr_svn139_2321"

><td id="2321"><a href="#2321">2321</a></td></tr
><tr id="gr_svn139_2322"

><td id="2322"><a href="#2322">2322</a></td></tr
><tr id="gr_svn139_2323"

><td id="2323"><a href="#2323">2323</a></td></tr
><tr id="gr_svn139_2324"

><td id="2324"><a href="#2324">2324</a></td></tr
><tr id="gr_svn139_2325"

><td id="2325"><a href="#2325">2325</a></td></tr
><tr id="gr_svn139_2326"

><td id="2326"><a href="#2326">2326</a></td></tr
><tr id="gr_svn139_2327"

><td id="2327"><a href="#2327">2327</a></td></tr
><tr id="gr_svn139_2328"

><td id="2328"><a href="#2328">2328</a></td></tr
><tr id="gr_svn139_2329"

><td id="2329"><a href="#2329">2329</a></td></tr
><tr id="gr_svn139_2330"

><td id="2330"><a href="#2330">2330</a></td></tr
><tr id="gr_svn139_2331"

><td id="2331"><a href="#2331">2331</a></td></tr
><tr id="gr_svn139_2332"

><td id="2332"><a href="#2332">2332</a></td></tr
><tr id="gr_svn139_2333"

><td id="2333"><a href="#2333">2333</a></td></tr
><tr id="gr_svn139_2334"

><td id="2334"><a href="#2334">2334</a></td></tr
><tr id="gr_svn139_2335"

><td id="2335"><a href="#2335">2335</a></td></tr
><tr id="gr_svn139_2336"

><td id="2336"><a href="#2336">2336</a></td></tr
><tr id="gr_svn139_2337"

><td id="2337"><a href="#2337">2337</a></td></tr
><tr id="gr_svn139_2338"

><td id="2338"><a href="#2338">2338</a></td></tr
><tr id="gr_svn139_2339"

><td id="2339"><a href="#2339">2339</a></td></tr
><tr id="gr_svn139_2340"

><td id="2340"><a href="#2340">2340</a></td></tr
><tr id="gr_svn139_2341"

><td id="2341"><a href="#2341">2341</a></td></tr
><tr id="gr_svn139_2342"

><td id="2342"><a href="#2342">2342</a></td></tr
><tr id="gr_svn139_2343"

><td id="2343"><a href="#2343">2343</a></td></tr
><tr id="gr_svn139_2344"

><td id="2344"><a href="#2344">2344</a></td></tr
><tr id="gr_svn139_2345"

><td id="2345"><a href="#2345">2345</a></td></tr
><tr id="gr_svn139_2346"

><td id="2346"><a href="#2346">2346</a></td></tr
><tr id="gr_svn139_2347"

><td id="2347"><a href="#2347">2347</a></td></tr
><tr id="gr_svn139_2348"

><td id="2348"><a href="#2348">2348</a></td></tr
><tr id="gr_svn139_2349"

><td id="2349"><a href="#2349">2349</a></td></tr
><tr id="gr_svn139_2350"

><td id="2350"><a href="#2350">2350</a></td></tr
><tr id="gr_svn139_2351"

><td id="2351"><a href="#2351">2351</a></td></tr
><tr id="gr_svn139_2352"

><td id="2352"><a href="#2352">2352</a></td></tr
><tr id="gr_svn139_2353"

><td id="2353"><a href="#2353">2353</a></td></tr
><tr id="gr_svn139_2354"

><td id="2354"><a href="#2354">2354</a></td></tr
><tr id="gr_svn139_2355"

><td id="2355"><a href="#2355">2355</a></td></tr
><tr id="gr_svn139_2356"

><td id="2356"><a href="#2356">2356</a></td></tr
><tr id="gr_svn139_2357"

><td id="2357"><a href="#2357">2357</a></td></tr
><tr id="gr_svn139_2358"

><td id="2358"><a href="#2358">2358</a></td></tr
><tr id="gr_svn139_2359"

><td id="2359"><a href="#2359">2359</a></td></tr
><tr id="gr_svn139_2360"

><td id="2360"><a href="#2360">2360</a></td></tr
><tr id="gr_svn139_2361"

><td id="2361"><a href="#2361">2361</a></td></tr
><tr id="gr_svn139_2362"

><td id="2362"><a href="#2362">2362</a></td></tr
><tr id="gr_svn139_2363"

><td id="2363"><a href="#2363">2363</a></td></tr
><tr id="gr_svn139_2364"

><td id="2364"><a href="#2364">2364</a></td></tr
><tr id="gr_svn139_2365"

><td id="2365"><a href="#2365">2365</a></td></tr
><tr id="gr_svn139_2366"

><td id="2366"><a href="#2366">2366</a></td></tr
><tr id="gr_svn139_2367"

><td id="2367"><a href="#2367">2367</a></td></tr
><tr id="gr_svn139_2368"

><td id="2368"><a href="#2368">2368</a></td></tr
><tr id="gr_svn139_2369"

><td id="2369"><a href="#2369">2369</a></td></tr
><tr id="gr_svn139_2370"

><td id="2370"><a href="#2370">2370</a></td></tr
><tr id="gr_svn139_2371"

><td id="2371"><a href="#2371">2371</a></td></tr
><tr id="gr_svn139_2372"

><td id="2372"><a href="#2372">2372</a></td></tr
><tr id="gr_svn139_2373"

><td id="2373"><a href="#2373">2373</a></td></tr
><tr id="gr_svn139_2374"

><td id="2374"><a href="#2374">2374</a></td></tr
><tr id="gr_svn139_2375"

><td id="2375"><a href="#2375">2375</a></td></tr
><tr id="gr_svn139_2376"

><td id="2376"><a href="#2376">2376</a></td></tr
><tr id="gr_svn139_2377"

><td id="2377"><a href="#2377">2377</a></td></tr
><tr id="gr_svn139_2378"

><td id="2378"><a href="#2378">2378</a></td></tr
><tr id="gr_svn139_2379"

><td id="2379"><a href="#2379">2379</a></td></tr
><tr id="gr_svn139_2380"

><td id="2380"><a href="#2380">2380</a></td></tr
><tr id="gr_svn139_2381"

><td id="2381"><a href="#2381">2381</a></td></tr
><tr id="gr_svn139_2382"

><td id="2382"><a href="#2382">2382</a></td></tr
><tr id="gr_svn139_2383"

><td id="2383"><a href="#2383">2383</a></td></tr
><tr id="gr_svn139_2384"

><td id="2384"><a href="#2384">2384</a></td></tr
><tr id="gr_svn139_2385"

><td id="2385"><a href="#2385">2385</a></td></tr
><tr id="gr_svn139_2386"

><td id="2386"><a href="#2386">2386</a></td></tr
><tr id="gr_svn139_2387"

><td id="2387"><a href="#2387">2387</a></td></tr
><tr id="gr_svn139_2388"

><td id="2388"><a href="#2388">2388</a></td></tr
><tr id="gr_svn139_2389"

><td id="2389"><a href="#2389">2389</a></td></tr
><tr id="gr_svn139_2390"

><td id="2390"><a href="#2390">2390</a></td></tr
><tr id="gr_svn139_2391"

><td id="2391"><a href="#2391">2391</a></td></tr
><tr id="gr_svn139_2392"

><td id="2392"><a href="#2392">2392</a></td></tr
><tr id="gr_svn139_2393"

><td id="2393"><a href="#2393">2393</a></td></tr
><tr id="gr_svn139_2394"

><td id="2394"><a href="#2394">2394</a></td></tr
><tr id="gr_svn139_2395"

><td id="2395"><a href="#2395">2395</a></td></tr
><tr id="gr_svn139_2396"

><td id="2396"><a href="#2396">2396</a></td></tr
><tr id="gr_svn139_2397"

><td id="2397"><a href="#2397">2397</a></td></tr
><tr id="gr_svn139_2398"

><td id="2398"><a href="#2398">2398</a></td></tr
><tr id="gr_svn139_2399"

><td id="2399"><a href="#2399">2399</a></td></tr
><tr id="gr_svn139_2400"

><td id="2400"><a href="#2400">2400</a></td></tr
><tr id="gr_svn139_2401"

><td id="2401"><a href="#2401">2401</a></td></tr
><tr id="gr_svn139_2402"

><td id="2402"><a href="#2402">2402</a></td></tr
><tr id="gr_svn139_2403"

><td id="2403"><a href="#2403">2403</a></td></tr
><tr id="gr_svn139_2404"

><td id="2404"><a href="#2404">2404</a></td></tr
><tr id="gr_svn139_2405"

><td id="2405"><a href="#2405">2405</a></td></tr
><tr id="gr_svn139_2406"

><td id="2406"><a href="#2406">2406</a></td></tr
><tr id="gr_svn139_2407"

><td id="2407"><a href="#2407">2407</a></td></tr
><tr id="gr_svn139_2408"

><td id="2408"><a href="#2408">2408</a></td></tr
><tr id="gr_svn139_2409"

><td id="2409"><a href="#2409">2409</a></td></tr
><tr id="gr_svn139_2410"

><td id="2410"><a href="#2410">2410</a></td></tr
><tr id="gr_svn139_2411"

><td id="2411"><a href="#2411">2411</a></td></tr
><tr id="gr_svn139_2412"

><td id="2412"><a href="#2412">2412</a></td></tr
><tr id="gr_svn139_2413"

><td id="2413"><a href="#2413">2413</a></td></tr
><tr id="gr_svn139_2414"

><td id="2414"><a href="#2414">2414</a></td></tr
><tr id="gr_svn139_2415"

><td id="2415"><a href="#2415">2415</a></td></tr
><tr id="gr_svn139_2416"

><td id="2416"><a href="#2416">2416</a></td></tr
><tr id="gr_svn139_2417"

><td id="2417"><a href="#2417">2417</a></td></tr
><tr id="gr_svn139_2418"

><td id="2418"><a href="#2418">2418</a></td></tr
><tr id="gr_svn139_2419"

><td id="2419"><a href="#2419">2419</a></td></tr
><tr id="gr_svn139_2420"

><td id="2420"><a href="#2420">2420</a></td></tr
><tr id="gr_svn139_2421"

><td id="2421"><a href="#2421">2421</a></td></tr
><tr id="gr_svn139_2422"

><td id="2422"><a href="#2422">2422</a></td></tr
><tr id="gr_svn139_2423"

><td id="2423"><a href="#2423">2423</a></td></tr
><tr id="gr_svn139_2424"

><td id="2424"><a href="#2424">2424</a></td></tr
><tr id="gr_svn139_2425"

><td id="2425"><a href="#2425">2425</a></td></tr
><tr id="gr_svn139_2426"

><td id="2426"><a href="#2426">2426</a></td></tr
><tr id="gr_svn139_2427"

><td id="2427"><a href="#2427">2427</a></td></tr
><tr id="gr_svn139_2428"

><td id="2428"><a href="#2428">2428</a></td></tr
><tr id="gr_svn139_2429"

><td id="2429"><a href="#2429">2429</a></td></tr
><tr id="gr_svn139_2430"

><td id="2430"><a href="#2430">2430</a></td></tr
><tr id="gr_svn139_2431"

><td id="2431"><a href="#2431">2431</a></td></tr
><tr id="gr_svn139_2432"

><td id="2432"><a href="#2432">2432</a></td></tr
><tr id="gr_svn139_2433"

><td id="2433"><a href="#2433">2433</a></td></tr
><tr id="gr_svn139_2434"

><td id="2434"><a href="#2434">2434</a></td></tr
><tr id="gr_svn139_2435"

><td id="2435"><a href="#2435">2435</a></td></tr
><tr id="gr_svn139_2436"

><td id="2436"><a href="#2436">2436</a></td></tr
><tr id="gr_svn139_2437"

><td id="2437"><a href="#2437">2437</a></td></tr
><tr id="gr_svn139_2438"

><td id="2438"><a href="#2438">2438</a></td></tr
><tr id="gr_svn139_2439"

><td id="2439"><a href="#2439">2439</a></td></tr
><tr id="gr_svn139_2440"

><td id="2440"><a href="#2440">2440</a></td></tr
><tr id="gr_svn139_2441"

><td id="2441"><a href="#2441">2441</a></td></tr
><tr id="gr_svn139_2442"

><td id="2442"><a href="#2442">2442</a></td></tr
><tr id="gr_svn139_2443"

><td id="2443"><a href="#2443">2443</a></td></tr
><tr id="gr_svn139_2444"

><td id="2444"><a href="#2444">2444</a></td></tr
><tr id="gr_svn139_2445"

><td id="2445"><a href="#2445">2445</a></td></tr
><tr id="gr_svn139_2446"

><td id="2446"><a href="#2446">2446</a></td></tr
><tr id="gr_svn139_2447"

><td id="2447"><a href="#2447">2447</a></td></tr
><tr id="gr_svn139_2448"

><td id="2448"><a href="#2448">2448</a></td></tr
><tr id="gr_svn139_2449"

><td id="2449"><a href="#2449">2449</a></td></tr
><tr id="gr_svn139_2450"

><td id="2450"><a href="#2450">2450</a></td></tr
><tr id="gr_svn139_2451"

><td id="2451"><a href="#2451">2451</a></td></tr
><tr id="gr_svn139_2452"

><td id="2452"><a href="#2452">2452</a></td></tr
><tr id="gr_svn139_2453"

><td id="2453"><a href="#2453">2453</a></td></tr
><tr id="gr_svn139_2454"

><td id="2454"><a href="#2454">2454</a></td></tr
><tr id="gr_svn139_2455"

><td id="2455"><a href="#2455">2455</a></td></tr
><tr id="gr_svn139_2456"

><td id="2456"><a href="#2456">2456</a></td></tr
><tr id="gr_svn139_2457"

><td id="2457"><a href="#2457">2457</a></td></tr
><tr id="gr_svn139_2458"

><td id="2458"><a href="#2458">2458</a></td></tr
><tr id="gr_svn139_2459"

><td id="2459"><a href="#2459">2459</a></td></tr
><tr id="gr_svn139_2460"

><td id="2460"><a href="#2460">2460</a></td></tr
><tr id="gr_svn139_2461"

><td id="2461"><a href="#2461">2461</a></td></tr
><tr id="gr_svn139_2462"

><td id="2462"><a href="#2462">2462</a></td></tr
><tr id="gr_svn139_2463"

><td id="2463"><a href="#2463">2463</a></td></tr
><tr id="gr_svn139_2464"

><td id="2464"><a href="#2464">2464</a></td></tr
><tr id="gr_svn139_2465"

><td id="2465"><a href="#2465">2465</a></td></tr
><tr id="gr_svn139_2466"

><td id="2466"><a href="#2466">2466</a></td></tr
><tr id="gr_svn139_2467"

><td id="2467"><a href="#2467">2467</a></td></tr
><tr id="gr_svn139_2468"

><td id="2468"><a href="#2468">2468</a></td></tr
><tr id="gr_svn139_2469"

><td id="2469"><a href="#2469">2469</a></td></tr
><tr id="gr_svn139_2470"

><td id="2470"><a href="#2470">2470</a></td></tr
><tr id="gr_svn139_2471"

><td id="2471"><a href="#2471">2471</a></td></tr
><tr id="gr_svn139_2472"

><td id="2472"><a href="#2472">2472</a></td></tr
><tr id="gr_svn139_2473"

><td id="2473"><a href="#2473">2473</a></td></tr
><tr id="gr_svn139_2474"

><td id="2474"><a href="#2474">2474</a></td></tr
><tr id="gr_svn139_2475"

><td id="2475"><a href="#2475">2475</a></td></tr
><tr id="gr_svn139_2476"

><td id="2476"><a href="#2476">2476</a></td></tr
><tr id="gr_svn139_2477"

><td id="2477"><a href="#2477">2477</a></td></tr
><tr id="gr_svn139_2478"

><td id="2478"><a href="#2478">2478</a></td></tr
><tr id="gr_svn139_2479"

><td id="2479"><a href="#2479">2479</a></td></tr
><tr id="gr_svn139_2480"

><td id="2480"><a href="#2480">2480</a></td></tr
><tr id="gr_svn139_2481"

><td id="2481"><a href="#2481">2481</a></td></tr
><tr id="gr_svn139_2482"

><td id="2482"><a href="#2482">2482</a></td></tr
><tr id="gr_svn139_2483"

><td id="2483"><a href="#2483">2483</a></td></tr
><tr id="gr_svn139_2484"

><td id="2484"><a href="#2484">2484</a></td></tr
><tr id="gr_svn139_2485"

><td id="2485"><a href="#2485">2485</a></td></tr
><tr id="gr_svn139_2486"

><td id="2486"><a href="#2486">2486</a></td></tr
><tr id="gr_svn139_2487"

><td id="2487"><a href="#2487">2487</a></td></tr
><tr id="gr_svn139_2488"

><td id="2488"><a href="#2488">2488</a></td></tr
><tr id="gr_svn139_2489"

><td id="2489"><a href="#2489">2489</a></td></tr
><tr id="gr_svn139_2490"

><td id="2490"><a href="#2490">2490</a></td></tr
><tr id="gr_svn139_2491"

><td id="2491"><a href="#2491">2491</a></td></tr
><tr id="gr_svn139_2492"

><td id="2492"><a href="#2492">2492</a></td></tr
><tr id="gr_svn139_2493"

><td id="2493"><a href="#2493">2493</a></td></tr
><tr id="gr_svn139_2494"

><td id="2494"><a href="#2494">2494</a></td></tr
><tr id="gr_svn139_2495"

><td id="2495"><a href="#2495">2495</a></td></tr
><tr id="gr_svn139_2496"

><td id="2496"><a href="#2496">2496</a></td></tr
><tr id="gr_svn139_2497"

><td id="2497"><a href="#2497">2497</a></td></tr
><tr id="gr_svn139_2498"

><td id="2498"><a href="#2498">2498</a></td></tr
><tr id="gr_svn139_2499"

><td id="2499"><a href="#2499">2499</a></td></tr
><tr id="gr_svn139_2500"

><td id="2500"><a href="#2500">2500</a></td></tr
><tr id="gr_svn139_2501"

><td id="2501"><a href="#2501">2501</a></td></tr
><tr id="gr_svn139_2502"

><td id="2502"><a href="#2502">2502</a></td></tr
><tr id="gr_svn139_2503"

><td id="2503"><a href="#2503">2503</a></td></tr
><tr id="gr_svn139_2504"

><td id="2504"><a href="#2504">2504</a></td></tr
><tr id="gr_svn139_2505"

><td id="2505"><a href="#2505">2505</a></td></tr
><tr id="gr_svn139_2506"

><td id="2506"><a href="#2506">2506</a></td></tr
><tr id="gr_svn139_2507"

><td id="2507"><a href="#2507">2507</a></td></tr
><tr id="gr_svn139_2508"

><td id="2508"><a href="#2508">2508</a></td></tr
><tr id="gr_svn139_2509"

><td id="2509"><a href="#2509">2509</a></td></tr
><tr id="gr_svn139_2510"

><td id="2510"><a href="#2510">2510</a></td></tr
><tr id="gr_svn139_2511"

><td id="2511"><a href="#2511">2511</a></td></tr
><tr id="gr_svn139_2512"

><td id="2512"><a href="#2512">2512</a></td></tr
><tr id="gr_svn139_2513"

><td id="2513"><a href="#2513">2513</a></td></tr
><tr id="gr_svn139_2514"

><td id="2514"><a href="#2514">2514</a></td></tr
><tr id="gr_svn139_2515"

><td id="2515"><a href="#2515">2515</a></td></tr
><tr id="gr_svn139_2516"

><td id="2516"><a href="#2516">2516</a></td></tr
><tr id="gr_svn139_2517"

><td id="2517"><a href="#2517">2517</a></td></tr
><tr id="gr_svn139_2518"

><td id="2518"><a href="#2518">2518</a></td></tr
><tr id="gr_svn139_2519"

><td id="2519"><a href="#2519">2519</a></td></tr
><tr id="gr_svn139_2520"

><td id="2520"><a href="#2520">2520</a></td></tr
><tr id="gr_svn139_2521"

><td id="2521"><a href="#2521">2521</a></td></tr
><tr id="gr_svn139_2522"

><td id="2522"><a href="#2522">2522</a></td></tr
><tr id="gr_svn139_2523"

><td id="2523"><a href="#2523">2523</a></td></tr
><tr id="gr_svn139_2524"

><td id="2524"><a href="#2524">2524</a></td></tr
><tr id="gr_svn139_2525"

><td id="2525"><a href="#2525">2525</a></td></tr
><tr id="gr_svn139_2526"

><td id="2526"><a href="#2526">2526</a></td></tr
><tr id="gr_svn139_2527"

><td id="2527"><a href="#2527">2527</a></td></tr
><tr id="gr_svn139_2528"

><td id="2528"><a href="#2528">2528</a></td></tr
><tr id="gr_svn139_2529"

><td id="2529"><a href="#2529">2529</a></td></tr
><tr id="gr_svn139_2530"

><td id="2530"><a href="#2530">2530</a></td></tr
><tr id="gr_svn139_2531"

><td id="2531"><a href="#2531">2531</a></td></tr
><tr id="gr_svn139_2532"

><td id="2532"><a href="#2532">2532</a></td></tr
><tr id="gr_svn139_2533"

><td id="2533"><a href="#2533">2533</a></td></tr
><tr id="gr_svn139_2534"

><td id="2534"><a href="#2534">2534</a></td></tr
><tr id="gr_svn139_2535"

><td id="2535"><a href="#2535">2535</a></td></tr
><tr id="gr_svn139_2536"

><td id="2536"><a href="#2536">2536</a></td></tr
><tr id="gr_svn139_2537"

><td id="2537"><a href="#2537">2537</a></td></tr
><tr id="gr_svn139_2538"

><td id="2538"><a href="#2538">2538</a></td></tr
><tr id="gr_svn139_2539"

><td id="2539"><a href="#2539">2539</a></td></tr
><tr id="gr_svn139_2540"

><td id="2540"><a href="#2540">2540</a></td></tr
><tr id="gr_svn139_2541"

><td id="2541"><a href="#2541">2541</a></td></tr
><tr id="gr_svn139_2542"

><td id="2542"><a href="#2542">2542</a></td></tr
><tr id="gr_svn139_2543"

><td id="2543"><a href="#2543">2543</a></td></tr
><tr id="gr_svn139_2544"

><td id="2544"><a href="#2544">2544</a></td></tr
><tr id="gr_svn139_2545"

><td id="2545"><a href="#2545">2545</a></td></tr
><tr id="gr_svn139_2546"

><td id="2546"><a href="#2546">2546</a></td></tr
><tr id="gr_svn139_2547"

><td id="2547"><a href="#2547">2547</a></td></tr
><tr id="gr_svn139_2548"

><td id="2548"><a href="#2548">2548</a></td></tr
><tr id="gr_svn139_2549"

><td id="2549"><a href="#2549">2549</a></td></tr
><tr id="gr_svn139_2550"

><td id="2550"><a href="#2550">2550</a></td></tr
><tr id="gr_svn139_2551"

><td id="2551"><a href="#2551">2551</a></td></tr
><tr id="gr_svn139_2552"

><td id="2552"><a href="#2552">2552</a></td></tr
><tr id="gr_svn139_2553"

><td id="2553"><a href="#2553">2553</a></td></tr
><tr id="gr_svn139_2554"

><td id="2554"><a href="#2554">2554</a></td></tr
><tr id="gr_svn139_2555"

><td id="2555"><a href="#2555">2555</a></td></tr
><tr id="gr_svn139_2556"

><td id="2556"><a href="#2556">2556</a></td></tr
><tr id="gr_svn139_2557"

><td id="2557"><a href="#2557">2557</a></td></tr
><tr id="gr_svn139_2558"

><td id="2558"><a href="#2558">2558</a></td></tr
><tr id="gr_svn139_2559"

><td id="2559"><a href="#2559">2559</a></td></tr
><tr id="gr_svn139_2560"

><td id="2560"><a href="#2560">2560</a></td></tr
><tr id="gr_svn139_2561"

><td id="2561"><a href="#2561">2561</a></td></tr
><tr id="gr_svn139_2562"

><td id="2562"><a href="#2562">2562</a></td></tr
><tr id="gr_svn139_2563"

><td id="2563"><a href="#2563">2563</a></td></tr
><tr id="gr_svn139_2564"

><td id="2564"><a href="#2564">2564</a></td></tr
><tr id="gr_svn139_2565"

><td id="2565"><a href="#2565">2565</a></td></tr
><tr id="gr_svn139_2566"

><td id="2566"><a href="#2566">2566</a></td></tr
><tr id="gr_svn139_2567"

><td id="2567"><a href="#2567">2567</a></td></tr
><tr id="gr_svn139_2568"

><td id="2568"><a href="#2568">2568</a></td></tr
><tr id="gr_svn139_2569"

><td id="2569"><a href="#2569">2569</a></td></tr
><tr id="gr_svn139_2570"

><td id="2570"><a href="#2570">2570</a></td></tr
><tr id="gr_svn139_2571"

><td id="2571"><a href="#2571">2571</a></td></tr
><tr id="gr_svn139_2572"

><td id="2572"><a href="#2572">2572</a></td></tr
><tr id="gr_svn139_2573"

><td id="2573"><a href="#2573">2573</a></td></tr
><tr id="gr_svn139_2574"

><td id="2574"><a href="#2574">2574</a></td></tr
><tr id="gr_svn139_2575"

><td id="2575"><a href="#2575">2575</a></td></tr
><tr id="gr_svn139_2576"

><td id="2576"><a href="#2576">2576</a></td></tr
><tr id="gr_svn139_2577"

><td id="2577"><a href="#2577">2577</a></td></tr
><tr id="gr_svn139_2578"

><td id="2578"><a href="#2578">2578</a></td></tr
><tr id="gr_svn139_2579"

><td id="2579"><a href="#2579">2579</a></td></tr
><tr id="gr_svn139_2580"

><td id="2580"><a href="#2580">2580</a></td></tr
><tr id="gr_svn139_2581"

><td id="2581"><a href="#2581">2581</a></td></tr
><tr id="gr_svn139_2582"

><td id="2582"><a href="#2582">2582</a></td></tr
><tr id="gr_svn139_2583"

><td id="2583"><a href="#2583">2583</a></td></tr
><tr id="gr_svn139_2584"

><td id="2584"><a href="#2584">2584</a></td></tr
><tr id="gr_svn139_2585"

><td id="2585"><a href="#2585">2585</a></td></tr
><tr id="gr_svn139_2586"

><td id="2586"><a href="#2586">2586</a></td></tr
><tr id="gr_svn139_2587"

><td id="2587"><a href="#2587">2587</a></td></tr
><tr id="gr_svn139_2588"

><td id="2588"><a href="#2588">2588</a></td></tr
><tr id="gr_svn139_2589"

><td id="2589"><a href="#2589">2589</a></td></tr
><tr id="gr_svn139_2590"

><td id="2590"><a href="#2590">2590</a></td></tr
><tr id="gr_svn139_2591"

><td id="2591"><a href="#2591">2591</a></td></tr
><tr id="gr_svn139_2592"

><td id="2592"><a href="#2592">2592</a></td></tr
><tr id="gr_svn139_2593"

><td id="2593"><a href="#2593">2593</a></td></tr
><tr id="gr_svn139_2594"

><td id="2594"><a href="#2594">2594</a></td></tr
><tr id="gr_svn139_2595"

><td id="2595"><a href="#2595">2595</a></td></tr
><tr id="gr_svn139_2596"

><td id="2596"><a href="#2596">2596</a></td></tr
><tr id="gr_svn139_2597"

><td id="2597"><a href="#2597">2597</a></td></tr
><tr id="gr_svn139_2598"

><td id="2598"><a href="#2598">2598</a></td></tr
><tr id="gr_svn139_2599"

><td id="2599"><a href="#2599">2599</a></td></tr
><tr id="gr_svn139_2600"

><td id="2600"><a href="#2600">2600</a></td></tr
><tr id="gr_svn139_2601"

><td id="2601"><a href="#2601">2601</a></td></tr
><tr id="gr_svn139_2602"

><td id="2602"><a href="#2602">2602</a></td></tr
><tr id="gr_svn139_2603"

><td id="2603"><a href="#2603">2603</a></td></tr
><tr id="gr_svn139_2604"

><td id="2604"><a href="#2604">2604</a></td></tr
><tr id="gr_svn139_2605"

><td id="2605"><a href="#2605">2605</a></td></tr
><tr id="gr_svn139_2606"

><td id="2606"><a href="#2606">2606</a></td></tr
><tr id="gr_svn139_2607"

><td id="2607"><a href="#2607">2607</a></td></tr
><tr id="gr_svn139_2608"

><td id="2608"><a href="#2608">2608</a></td></tr
><tr id="gr_svn139_2609"

><td id="2609"><a href="#2609">2609</a></td></tr
><tr id="gr_svn139_2610"

><td id="2610"><a href="#2610">2610</a></td></tr
><tr id="gr_svn139_2611"

><td id="2611"><a href="#2611">2611</a></td></tr
><tr id="gr_svn139_2612"

><td id="2612"><a href="#2612">2612</a></td></tr
><tr id="gr_svn139_2613"

><td id="2613"><a href="#2613">2613</a></td></tr
><tr id="gr_svn139_2614"

><td id="2614"><a href="#2614">2614</a></td></tr
><tr id="gr_svn139_2615"

><td id="2615"><a href="#2615">2615</a></td></tr
><tr id="gr_svn139_2616"

><td id="2616"><a href="#2616">2616</a></td></tr
><tr id="gr_svn139_2617"

><td id="2617"><a href="#2617">2617</a></td></tr
><tr id="gr_svn139_2618"

><td id="2618"><a href="#2618">2618</a></td></tr
><tr id="gr_svn139_2619"

><td id="2619"><a href="#2619">2619</a></td></tr
><tr id="gr_svn139_2620"

><td id="2620"><a href="#2620">2620</a></td></tr
><tr id="gr_svn139_2621"

><td id="2621"><a href="#2621">2621</a></td></tr
><tr id="gr_svn139_2622"

><td id="2622"><a href="#2622">2622</a></td></tr
><tr id="gr_svn139_2623"

><td id="2623"><a href="#2623">2623</a></td></tr
><tr id="gr_svn139_2624"

><td id="2624"><a href="#2624">2624</a></td></tr
><tr id="gr_svn139_2625"

><td id="2625"><a href="#2625">2625</a></td></tr
><tr id="gr_svn139_2626"

><td id="2626"><a href="#2626">2626</a></td></tr
><tr id="gr_svn139_2627"

><td id="2627"><a href="#2627">2627</a></td></tr
><tr id="gr_svn139_2628"

><td id="2628"><a href="#2628">2628</a></td></tr
><tr id="gr_svn139_2629"

><td id="2629"><a href="#2629">2629</a></td></tr
><tr id="gr_svn139_2630"

><td id="2630"><a href="#2630">2630</a></td></tr
><tr id="gr_svn139_2631"

><td id="2631"><a href="#2631">2631</a></td></tr
><tr id="gr_svn139_2632"

><td id="2632"><a href="#2632">2632</a></td></tr
><tr id="gr_svn139_2633"

><td id="2633"><a href="#2633">2633</a></td></tr
><tr id="gr_svn139_2634"

><td id="2634"><a href="#2634">2634</a></td></tr
><tr id="gr_svn139_2635"

><td id="2635"><a href="#2635">2635</a></td></tr
><tr id="gr_svn139_2636"

><td id="2636"><a href="#2636">2636</a></td></tr
><tr id="gr_svn139_2637"

><td id="2637"><a href="#2637">2637</a></td></tr
><tr id="gr_svn139_2638"

><td id="2638"><a href="#2638">2638</a></td></tr
><tr id="gr_svn139_2639"

><td id="2639"><a href="#2639">2639</a></td></tr
><tr id="gr_svn139_2640"

><td id="2640"><a href="#2640">2640</a></td></tr
><tr id="gr_svn139_2641"

><td id="2641"><a href="#2641">2641</a></td></tr
><tr id="gr_svn139_2642"

><td id="2642"><a href="#2642">2642</a></td></tr
><tr id="gr_svn139_2643"

><td id="2643"><a href="#2643">2643</a></td></tr
><tr id="gr_svn139_2644"

><td id="2644"><a href="#2644">2644</a></td></tr
><tr id="gr_svn139_2645"

><td id="2645"><a href="#2645">2645</a></td></tr
><tr id="gr_svn139_2646"

><td id="2646"><a href="#2646">2646</a></td></tr
><tr id="gr_svn139_2647"

><td id="2647"><a href="#2647">2647</a></td></tr
><tr id="gr_svn139_2648"

><td id="2648"><a href="#2648">2648</a></td></tr
><tr id="gr_svn139_2649"

><td id="2649"><a href="#2649">2649</a></td></tr
><tr id="gr_svn139_2650"

><td id="2650"><a href="#2650">2650</a></td></tr
><tr id="gr_svn139_2651"

><td id="2651"><a href="#2651">2651</a></td></tr
><tr id="gr_svn139_2652"

><td id="2652"><a href="#2652">2652</a></td></tr
><tr id="gr_svn139_2653"

><td id="2653"><a href="#2653">2653</a></td></tr
><tr id="gr_svn139_2654"

><td id="2654"><a href="#2654">2654</a></td></tr
><tr id="gr_svn139_2655"

><td id="2655"><a href="#2655">2655</a></td></tr
><tr id="gr_svn139_2656"

><td id="2656"><a href="#2656">2656</a></td></tr
><tr id="gr_svn139_2657"

><td id="2657"><a href="#2657">2657</a></td></tr
><tr id="gr_svn139_2658"

><td id="2658"><a href="#2658">2658</a></td></tr
><tr id="gr_svn139_2659"

><td id="2659"><a href="#2659">2659</a></td></tr
><tr id="gr_svn139_2660"

><td id="2660"><a href="#2660">2660</a></td></tr
><tr id="gr_svn139_2661"

><td id="2661"><a href="#2661">2661</a></td></tr
><tr id="gr_svn139_2662"

><td id="2662"><a href="#2662">2662</a></td></tr
><tr id="gr_svn139_2663"

><td id="2663"><a href="#2663">2663</a></td></tr
><tr id="gr_svn139_2664"

><td id="2664"><a href="#2664">2664</a></td></tr
><tr id="gr_svn139_2665"

><td id="2665"><a href="#2665">2665</a></td></tr
><tr id="gr_svn139_2666"

><td id="2666"><a href="#2666">2666</a></td></tr
><tr id="gr_svn139_2667"

><td id="2667"><a href="#2667">2667</a></td></tr
><tr id="gr_svn139_2668"

><td id="2668"><a href="#2668">2668</a></td></tr
><tr id="gr_svn139_2669"

><td id="2669"><a href="#2669">2669</a></td></tr
><tr id="gr_svn139_2670"

><td id="2670"><a href="#2670">2670</a></td></tr
><tr id="gr_svn139_2671"

><td id="2671"><a href="#2671">2671</a></td></tr
><tr id="gr_svn139_2672"

><td id="2672"><a href="#2672">2672</a></td></tr
><tr id="gr_svn139_2673"

><td id="2673"><a href="#2673">2673</a></td></tr
><tr id="gr_svn139_2674"

><td id="2674"><a href="#2674">2674</a></td></tr
><tr id="gr_svn139_2675"

><td id="2675"><a href="#2675">2675</a></td></tr
><tr id="gr_svn139_2676"

><td id="2676"><a href="#2676">2676</a></td></tr
><tr id="gr_svn139_2677"

><td id="2677"><a href="#2677">2677</a></td></tr
><tr id="gr_svn139_2678"

><td id="2678"><a href="#2678">2678</a></td></tr
><tr id="gr_svn139_2679"

><td id="2679"><a href="#2679">2679</a></td></tr
><tr id="gr_svn139_2680"

><td id="2680"><a href="#2680">2680</a></td></tr
><tr id="gr_svn139_2681"

><td id="2681"><a href="#2681">2681</a></td></tr
><tr id="gr_svn139_2682"

><td id="2682"><a href="#2682">2682</a></td></tr
><tr id="gr_svn139_2683"

><td id="2683"><a href="#2683">2683</a></td></tr
><tr id="gr_svn139_2684"

><td id="2684"><a href="#2684">2684</a></td></tr
><tr id="gr_svn139_2685"

><td id="2685"><a href="#2685">2685</a></td></tr
><tr id="gr_svn139_2686"

><td id="2686"><a href="#2686">2686</a></td></tr
><tr id="gr_svn139_2687"

><td id="2687"><a href="#2687">2687</a></td></tr
><tr id="gr_svn139_2688"

><td id="2688"><a href="#2688">2688</a></td></tr
><tr id="gr_svn139_2689"

><td id="2689"><a href="#2689">2689</a></td></tr
><tr id="gr_svn139_2690"

><td id="2690"><a href="#2690">2690</a></td></tr
><tr id="gr_svn139_2691"

><td id="2691"><a href="#2691">2691</a></td></tr
><tr id="gr_svn139_2692"

><td id="2692"><a href="#2692">2692</a></td></tr
><tr id="gr_svn139_2693"

><td id="2693"><a href="#2693">2693</a></td></tr
><tr id="gr_svn139_2694"

><td id="2694"><a href="#2694">2694</a></td></tr
><tr id="gr_svn139_2695"

><td id="2695"><a href="#2695">2695</a></td></tr
><tr id="gr_svn139_2696"

><td id="2696"><a href="#2696">2696</a></td></tr
><tr id="gr_svn139_2697"

><td id="2697"><a href="#2697">2697</a></td></tr
><tr id="gr_svn139_2698"

><td id="2698"><a href="#2698">2698</a></td></tr
><tr id="gr_svn139_2699"

><td id="2699"><a href="#2699">2699</a></td></tr
><tr id="gr_svn139_2700"

><td id="2700"><a href="#2700">2700</a></td></tr
><tr id="gr_svn139_2701"

><td id="2701"><a href="#2701">2701</a></td></tr
><tr id="gr_svn139_2702"

><td id="2702"><a href="#2702">2702</a></td></tr
><tr id="gr_svn139_2703"

><td id="2703"><a href="#2703">2703</a></td></tr
><tr id="gr_svn139_2704"

><td id="2704"><a href="#2704">2704</a></td></tr
><tr id="gr_svn139_2705"

><td id="2705"><a href="#2705">2705</a></td></tr
><tr id="gr_svn139_2706"

><td id="2706"><a href="#2706">2706</a></td></tr
><tr id="gr_svn139_2707"

><td id="2707"><a href="#2707">2707</a></td></tr
><tr id="gr_svn139_2708"

><td id="2708"><a href="#2708">2708</a></td></tr
><tr id="gr_svn139_2709"

><td id="2709"><a href="#2709">2709</a></td></tr
><tr id="gr_svn139_2710"

><td id="2710"><a href="#2710">2710</a></td></tr
><tr id="gr_svn139_2711"

><td id="2711"><a href="#2711">2711</a></td></tr
><tr id="gr_svn139_2712"

><td id="2712"><a href="#2712">2712</a></td></tr
><tr id="gr_svn139_2713"

><td id="2713"><a href="#2713">2713</a></td></tr
><tr id="gr_svn139_2714"

><td id="2714"><a href="#2714">2714</a></td></tr
><tr id="gr_svn139_2715"

><td id="2715"><a href="#2715">2715</a></td></tr
><tr id="gr_svn139_2716"

><td id="2716"><a href="#2716">2716</a></td></tr
><tr id="gr_svn139_2717"

><td id="2717"><a href="#2717">2717</a></td></tr
><tr id="gr_svn139_2718"

><td id="2718"><a href="#2718">2718</a></td></tr
><tr id="gr_svn139_2719"

><td id="2719"><a href="#2719">2719</a></td></tr
><tr id="gr_svn139_2720"

><td id="2720"><a href="#2720">2720</a></td></tr
><tr id="gr_svn139_2721"

><td id="2721"><a href="#2721">2721</a></td></tr
><tr id="gr_svn139_2722"

><td id="2722"><a href="#2722">2722</a></td></tr
><tr id="gr_svn139_2723"

><td id="2723"><a href="#2723">2723</a></td></tr
><tr id="gr_svn139_2724"

><td id="2724"><a href="#2724">2724</a></td></tr
><tr id="gr_svn139_2725"

><td id="2725"><a href="#2725">2725</a></td></tr
><tr id="gr_svn139_2726"

><td id="2726"><a href="#2726">2726</a></td></tr
><tr id="gr_svn139_2727"

><td id="2727"><a href="#2727">2727</a></td></tr
><tr id="gr_svn139_2728"

><td id="2728"><a href="#2728">2728</a></td></tr
><tr id="gr_svn139_2729"

><td id="2729"><a href="#2729">2729</a></td></tr
><tr id="gr_svn139_2730"

><td id="2730"><a href="#2730">2730</a></td></tr
><tr id="gr_svn139_2731"

><td id="2731"><a href="#2731">2731</a></td></tr
><tr id="gr_svn139_2732"

><td id="2732"><a href="#2732">2732</a></td></tr
><tr id="gr_svn139_2733"

><td id="2733"><a href="#2733">2733</a></td></tr
><tr id="gr_svn139_2734"

><td id="2734"><a href="#2734">2734</a></td></tr
><tr id="gr_svn139_2735"

><td id="2735"><a href="#2735">2735</a></td></tr
><tr id="gr_svn139_2736"

><td id="2736"><a href="#2736">2736</a></td></tr
><tr id="gr_svn139_2737"

><td id="2737"><a href="#2737">2737</a></td></tr
><tr id="gr_svn139_2738"

><td id="2738"><a href="#2738">2738</a></td></tr
><tr id="gr_svn139_2739"

><td id="2739"><a href="#2739">2739</a></td></tr
><tr id="gr_svn139_2740"

><td id="2740"><a href="#2740">2740</a></td></tr
><tr id="gr_svn139_2741"

><td id="2741"><a href="#2741">2741</a></td></tr
><tr id="gr_svn139_2742"

><td id="2742"><a href="#2742">2742</a></td></tr
><tr id="gr_svn139_2743"

><td id="2743"><a href="#2743">2743</a></td></tr
><tr id="gr_svn139_2744"

><td id="2744"><a href="#2744">2744</a></td></tr
><tr id="gr_svn139_2745"

><td id="2745"><a href="#2745">2745</a></td></tr
><tr id="gr_svn139_2746"

><td id="2746"><a href="#2746">2746</a></td></tr
><tr id="gr_svn139_2747"

><td id="2747"><a href="#2747">2747</a></td></tr
><tr id="gr_svn139_2748"

><td id="2748"><a href="#2748">2748</a></td></tr
><tr id="gr_svn139_2749"

><td id="2749"><a href="#2749">2749</a></td></tr
><tr id="gr_svn139_2750"

><td id="2750"><a href="#2750">2750</a></td></tr
><tr id="gr_svn139_2751"

><td id="2751"><a href="#2751">2751</a></td></tr
><tr id="gr_svn139_2752"

><td id="2752"><a href="#2752">2752</a></td></tr
><tr id="gr_svn139_2753"

><td id="2753"><a href="#2753">2753</a></td></tr
><tr id="gr_svn139_2754"

><td id="2754"><a href="#2754">2754</a></td></tr
><tr id="gr_svn139_2755"

><td id="2755"><a href="#2755">2755</a></td></tr
><tr id="gr_svn139_2756"

><td id="2756"><a href="#2756">2756</a></td></tr
><tr id="gr_svn139_2757"

><td id="2757"><a href="#2757">2757</a></td></tr
><tr id="gr_svn139_2758"

><td id="2758"><a href="#2758">2758</a></td></tr
><tr id="gr_svn139_2759"

><td id="2759"><a href="#2759">2759</a></td></tr
><tr id="gr_svn139_2760"

><td id="2760"><a href="#2760">2760</a></td></tr
><tr id="gr_svn139_2761"

><td id="2761"><a href="#2761">2761</a></td></tr
><tr id="gr_svn139_2762"

><td id="2762"><a href="#2762">2762</a></td></tr
><tr id="gr_svn139_2763"

><td id="2763"><a href="#2763">2763</a></td></tr
><tr id="gr_svn139_2764"

><td id="2764"><a href="#2764">2764</a></td></tr
><tr id="gr_svn139_2765"

><td id="2765"><a href="#2765">2765</a></td></tr
><tr id="gr_svn139_2766"

><td id="2766"><a href="#2766">2766</a></td></tr
><tr id="gr_svn139_2767"

><td id="2767"><a href="#2767">2767</a></td></tr
><tr id="gr_svn139_2768"

><td id="2768"><a href="#2768">2768</a></td></tr
><tr id="gr_svn139_2769"

><td id="2769"><a href="#2769">2769</a></td></tr
><tr id="gr_svn139_2770"

><td id="2770"><a href="#2770">2770</a></td></tr
><tr id="gr_svn139_2771"

><td id="2771"><a href="#2771">2771</a></td></tr
><tr id="gr_svn139_2772"

><td id="2772"><a href="#2772">2772</a></td></tr
><tr id="gr_svn139_2773"

><td id="2773"><a href="#2773">2773</a></td></tr
><tr id="gr_svn139_2774"

><td id="2774"><a href="#2774">2774</a></td></tr
><tr id="gr_svn139_2775"

><td id="2775"><a href="#2775">2775</a></td></tr
><tr id="gr_svn139_2776"

><td id="2776"><a href="#2776">2776</a></td></tr
><tr id="gr_svn139_2777"

><td id="2777"><a href="#2777">2777</a></td></tr
><tr id="gr_svn139_2778"

><td id="2778"><a href="#2778">2778</a></td></tr
><tr id="gr_svn139_2779"

><td id="2779"><a href="#2779">2779</a></td></tr
><tr id="gr_svn139_2780"

><td id="2780"><a href="#2780">2780</a></td></tr
><tr id="gr_svn139_2781"

><td id="2781"><a href="#2781">2781</a></td></tr
><tr id="gr_svn139_2782"

><td id="2782"><a href="#2782">2782</a></td></tr
><tr id="gr_svn139_2783"

><td id="2783"><a href="#2783">2783</a></td></tr
><tr id="gr_svn139_2784"

><td id="2784"><a href="#2784">2784</a></td></tr
><tr id="gr_svn139_2785"

><td id="2785"><a href="#2785">2785</a></td></tr
><tr id="gr_svn139_2786"

><td id="2786"><a href="#2786">2786</a></td></tr
><tr id="gr_svn139_2787"

><td id="2787"><a href="#2787">2787</a></td></tr
><tr id="gr_svn139_2788"

><td id="2788"><a href="#2788">2788</a></td></tr
><tr id="gr_svn139_2789"

><td id="2789"><a href="#2789">2789</a></td></tr
><tr id="gr_svn139_2790"

><td id="2790"><a href="#2790">2790</a></td></tr
><tr id="gr_svn139_2791"

><td id="2791"><a href="#2791">2791</a></td></tr
><tr id="gr_svn139_2792"

><td id="2792"><a href="#2792">2792</a></td></tr
><tr id="gr_svn139_2793"

><td id="2793"><a href="#2793">2793</a></td></tr
><tr id="gr_svn139_2794"

><td id="2794"><a href="#2794">2794</a></td></tr
><tr id="gr_svn139_2795"

><td id="2795"><a href="#2795">2795</a></td></tr
><tr id="gr_svn139_2796"

><td id="2796"><a href="#2796">2796</a></td></tr
><tr id="gr_svn139_2797"

><td id="2797"><a href="#2797">2797</a></td></tr
><tr id="gr_svn139_2798"

><td id="2798"><a href="#2798">2798</a></td></tr
><tr id="gr_svn139_2799"

><td id="2799"><a href="#2799">2799</a></td></tr
><tr id="gr_svn139_2800"

><td id="2800"><a href="#2800">2800</a></td></tr
><tr id="gr_svn139_2801"

><td id="2801"><a href="#2801">2801</a></td></tr
><tr id="gr_svn139_2802"

><td id="2802"><a href="#2802">2802</a></td></tr
><tr id="gr_svn139_2803"

><td id="2803"><a href="#2803">2803</a></td></tr
><tr id="gr_svn139_2804"

><td id="2804"><a href="#2804">2804</a></td></tr
><tr id="gr_svn139_2805"

><td id="2805"><a href="#2805">2805</a></td></tr
><tr id="gr_svn139_2806"

><td id="2806"><a href="#2806">2806</a></td></tr
><tr id="gr_svn139_2807"

><td id="2807"><a href="#2807">2807</a></td></tr
><tr id="gr_svn139_2808"

><td id="2808"><a href="#2808">2808</a></td></tr
><tr id="gr_svn139_2809"

><td id="2809"><a href="#2809">2809</a></td></tr
><tr id="gr_svn139_2810"

><td id="2810"><a href="#2810">2810</a></td></tr
><tr id="gr_svn139_2811"

><td id="2811"><a href="#2811">2811</a></td></tr
><tr id="gr_svn139_2812"

><td id="2812"><a href="#2812">2812</a></td></tr
><tr id="gr_svn139_2813"

><td id="2813"><a href="#2813">2813</a></td></tr
><tr id="gr_svn139_2814"

><td id="2814"><a href="#2814">2814</a></td></tr
><tr id="gr_svn139_2815"

><td id="2815"><a href="#2815">2815</a></td></tr
><tr id="gr_svn139_2816"

><td id="2816"><a href="#2816">2816</a></td></tr
><tr id="gr_svn139_2817"

><td id="2817"><a href="#2817">2817</a></td></tr
><tr id="gr_svn139_2818"

><td id="2818"><a href="#2818">2818</a></td></tr
><tr id="gr_svn139_2819"

><td id="2819"><a href="#2819">2819</a></td></tr
><tr id="gr_svn139_2820"

><td id="2820"><a href="#2820">2820</a></td></tr
><tr id="gr_svn139_2821"

><td id="2821"><a href="#2821">2821</a></td></tr
><tr id="gr_svn139_2822"

><td id="2822"><a href="#2822">2822</a></td></tr
><tr id="gr_svn139_2823"

><td id="2823"><a href="#2823">2823</a></td></tr
><tr id="gr_svn139_2824"

><td id="2824"><a href="#2824">2824</a></td></tr
><tr id="gr_svn139_2825"

><td id="2825"><a href="#2825">2825</a></td></tr
><tr id="gr_svn139_2826"

><td id="2826"><a href="#2826">2826</a></td></tr
><tr id="gr_svn139_2827"

><td id="2827"><a href="#2827">2827</a></td></tr
><tr id="gr_svn139_2828"

><td id="2828"><a href="#2828">2828</a></td></tr
><tr id="gr_svn139_2829"

><td id="2829"><a href="#2829">2829</a></td></tr
><tr id="gr_svn139_2830"

><td id="2830"><a href="#2830">2830</a></td></tr
><tr id="gr_svn139_2831"

><td id="2831"><a href="#2831">2831</a></td></tr
><tr id="gr_svn139_2832"

><td id="2832"><a href="#2832">2832</a></td></tr
><tr id="gr_svn139_2833"

><td id="2833"><a href="#2833">2833</a></td></tr
><tr id="gr_svn139_2834"

><td id="2834"><a href="#2834">2834</a></td></tr
><tr id="gr_svn139_2835"

><td id="2835"><a href="#2835">2835</a></td></tr
><tr id="gr_svn139_2836"

><td id="2836"><a href="#2836">2836</a></td></tr
><tr id="gr_svn139_2837"

><td id="2837"><a href="#2837">2837</a></td></tr
><tr id="gr_svn139_2838"

><td id="2838"><a href="#2838">2838</a></td></tr
><tr id="gr_svn139_2839"

><td id="2839"><a href="#2839">2839</a></td></tr
><tr id="gr_svn139_2840"

><td id="2840"><a href="#2840">2840</a></td></tr
><tr id="gr_svn139_2841"

><td id="2841"><a href="#2841">2841</a></td></tr
><tr id="gr_svn139_2842"

><td id="2842"><a href="#2842">2842</a></td></tr
><tr id="gr_svn139_2843"

><td id="2843"><a href="#2843">2843</a></td></tr
><tr id="gr_svn139_2844"

><td id="2844"><a href="#2844">2844</a></td></tr
><tr id="gr_svn139_2845"

><td id="2845"><a href="#2845">2845</a></td></tr
><tr id="gr_svn139_2846"

><td id="2846"><a href="#2846">2846</a></td></tr
><tr id="gr_svn139_2847"

><td id="2847"><a href="#2847">2847</a></td></tr
><tr id="gr_svn139_2848"

><td id="2848"><a href="#2848">2848</a></td></tr
><tr id="gr_svn139_2849"

><td id="2849"><a href="#2849">2849</a></td></tr
><tr id="gr_svn139_2850"

><td id="2850"><a href="#2850">2850</a></td></tr
><tr id="gr_svn139_2851"

><td id="2851"><a href="#2851">2851</a></td></tr
><tr id="gr_svn139_2852"

><td id="2852"><a href="#2852">2852</a></td></tr
><tr id="gr_svn139_2853"

><td id="2853"><a href="#2853">2853</a></td></tr
><tr id="gr_svn139_2854"

><td id="2854"><a href="#2854">2854</a></td></tr
><tr id="gr_svn139_2855"

><td id="2855"><a href="#2855">2855</a></td></tr
><tr id="gr_svn139_2856"

><td id="2856"><a href="#2856">2856</a></td></tr
><tr id="gr_svn139_2857"

><td id="2857"><a href="#2857">2857</a></td></tr
><tr id="gr_svn139_2858"

><td id="2858"><a href="#2858">2858</a></td></tr
><tr id="gr_svn139_2859"

><td id="2859"><a href="#2859">2859</a></td></tr
><tr id="gr_svn139_2860"

><td id="2860"><a href="#2860">2860</a></td></tr
><tr id="gr_svn139_2861"

><td id="2861"><a href="#2861">2861</a></td></tr
><tr id="gr_svn139_2862"

><td id="2862"><a href="#2862">2862</a></td></tr
><tr id="gr_svn139_2863"

><td id="2863"><a href="#2863">2863</a></td></tr
><tr id="gr_svn139_2864"

><td id="2864"><a href="#2864">2864</a></td></tr
><tr id="gr_svn139_2865"

><td id="2865"><a href="#2865">2865</a></td></tr
><tr id="gr_svn139_2866"

><td id="2866"><a href="#2866">2866</a></td></tr
><tr id="gr_svn139_2867"

><td id="2867"><a href="#2867">2867</a></td></tr
><tr id="gr_svn139_2868"

><td id="2868"><a href="#2868">2868</a></td></tr
><tr id="gr_svn139_2869"

><td id="2869"><a href="#2869">2869</a></td></tr
><tr id="gr_svn139_2870"

><td id="2870"><a href="#2870">2870</a></td></tr
><tr id="gr_svn139_2871"

><td id="2871"><a href="#2871">2871</a></td></tr
><tr id="gr_svn139_2872"

><td id="2872"><a href="#2872">2872</a></td></tr
><tr id="gr_svn139_2873"

><td id="2873"><a href="#2873">2873</a></td></tr
><tr id="gr_svn139_2874"

><td id="2874"><a href="#2874">2874</a></td></tr
><tr id="gr_svn139_2875"

><td id="2875"><a href="#2875">2875</a></td></tr
><tr id="gr_svn139_2876"

><td id="2876"><a href="#2876">2876</a></td></tr
><tr id="gr_svn139_2877"

><td id="2877"><a href="#2877">2877</a></td></tr
><tr id="gr_svn139_2878"

><td id="2878"><a href="#2878">2878</a></td></tr
><tr id="gr_svn139_2879"

><td id="2879"><a href="#2879">2879</a></td></tr
><tr id="gr_svn139_2880"

><td id="2880"><a href="#2880">2880</a></td></tr
><tr id="gr_svn139_2881"

><td id="2881"><a href="#2881">2881</a></td></tr
><tr id="gr_svn139_2882"

><td id="2882"><a href="#2882">2882</a></td></tr
><tr id="gr_svn139_2883"

><td id="2883"><a href="#2883">2883</a></td></tr
><tr id="gr_svn139_2884"

><td id="2884"><a href="#2884">2884</a></td></tr
><tr id="gr_svn139_2885"

><td id="2885"><a href="#2885">2885</a></td></tr
><tr id="gr_svn139_2886"

><td id="2886"><a href="#2886">2886</a></td></tr
><tr id="gr_svn139_2887"

><td id="2887"><a href="#2887">2887</a></td></tr
><tr id="gr_svn139_2888"

><td id="2888"><a href="#2888">2888</a></td></tr
><tr id="gr_svn139_2889"

><td id="2889"><a href="#2889">2889</a></td></tr
><tr id="gr_svn139_2890"

><td id="2890"><a href="#2890">2890</a></td></tr
><tr id="gr_svn139_2891"

><td id="2891"><a href="#2891">2891</a></td></tr
><tr id="gr_svn139_2892"

><td id="2892"><a href="#2892">2892</a></td></tr
><tr id="gr_svn139_2893"

><td id="2893"><a href="#2893">2893</a></td></tr
><tr id="gr_svn139_2894"

><td id="2894"><a href="#2894">2894</a></td></tr
><tr id="gr_svn139_2895"

><td id="2895"><a href="#2895">2895</a></td></tr
><tr id="gr_svn139_2896"

><td id="2896"><a href="#2896">2896</a></td></tr
><tr id="gr_svn139_2897"

><td id="2897"><a href="#2897">2897</a></td></tr
><tr id="gr_svn139_2898"

><td id="2898"><a href="#2898">2898</a></td></tr
><tr id="gr_svn139_2899"

><td id="2899"><a href="#2899">2899</a></td></tr
><tr id="gr_svn139_2900"

><td id="2900"><a href="#2900">2900</a></td></tr
><tr id="gr_svn139_2901"

><td id="2901"><a href="#2901">2901</a></td></tr
><tr id="gr_svn139_2902"

><td id="2902"><a href="#2902">2902</a></td></tr
><tr id="gr_svn139_2903"

><td id="2903"><a href="#2903">2903</a></td></tr
><tr id="gr_svn139_2904"

><td id="2904"><a href="#2904">2904</a></td></tr
><tr id="gr_svn139_2905"

><td id="2905"><a href="#2905">2905</a></td></tr
><tr id="gr_svn139_2906"

><td id="2906"><a href="#2906">2906</a></td></tr
><tr id="gr_svn139_2907"

><td id="2907"><a href="#2907">2907</a></td></tr
><tr id="gr_svn139_2908"

><td id="2908"><a href="#2908">2908</a></td></tr
><tr id="gr_svn139_2909"

><td id="2909"><a href="#2909">2909</a></td></tr
><tr id="gr_svn139_2910"

><td id="2910"><a href="#2910">2910</a></td></tr
><tr id="gr_svn139_2911"

><td id="2911"><a href="#2911">2911</a></td></tr
><tr id="gr_svn139_2912"

><td id="2912"><a href="#2912">2912</a></td></tr
><tr id="gr_svn139_2913"

><td id="2913"><a href="#2913">2913</a></td></tr
><tr id="gr_svn139_2914"

><td id="2914"><a href="#2914">2914</a></td></tr
><tr id="gr_svn139_2915"

><td id="2915"><a href="#2915">2915</a></td></tr
><tr id="gr_svn139_2916"

><td id="2916"><a href="#2916">2916</a></td></tr
><tr id="gr_svn139_2917"

><td id="2917"><a href="#2917">2917</a></td></tr
><tr id="gr_svn139_2918"

><td id="2918"><a href="#2918">2918</a></td></tr
><tr id="gr_svn139_2919"

><td id="2919"><a href="#2919">2919</a></td></tr
><tr id="gr_svn139_2920"

><td id="2920"><a href="#2920">2920</a></td></tr
><tr id="gr_svn139_2921"

><td id="2921"><a href="#2921">2921</a></td></tr
><tr id="gr_svn139_2922"

><td id="2922"><a href="#2922">2922</a></td></tr
><tr id="gr_svn139_2923"

><td id="2923"><a href="#2923">2923</a></td></tr
><tr id="gr_svn139_2924"

><td id="2924"><a href="#2924">2924</a></td></tr
><tr id="gr_svn139_2925"

><td id="2925"><a href="#2925">2925</a></td></tr
><tr id="gr_svn139_2926"

><td id="2926"><a href="#2926">2926</a></td></tr
><tr id="gr_svn139_2927"

><td id="2927"><a href="#2927">2927</a></td></tr
><tr id="gr_svn139_2928"

><td id="2928"><a href="#2928">2928</a></td></tr
><tr id="gr_svn139_2929"

><td id="2929"><a href="#2929">2929</a></td></tr
><tr id="gr_svn139_2930"

><td id="2930"><a href="#2930">2930</a></td></tr
><tr id="gr_svn139_2931"

><td id="2931"><a href="#2931">2931</a></td></tr
><tr id="gr_svn139_2932"

><td id="2932"><a href="#2932">2932</a></td></tr
><tr id="gr_svn139_2933"

><td id="2933"><a href="#2933">2933</a></td></tr
><tr id="gr_svn139_2934"

><td id="2934"><a href="#2934">2934</a></td></tr
><tr id="gr_svn139_2935"

><td id="2935"><a href="#2935">2935</a></td></tr
><tr id="gr_svn139_2936"

><td id="2936"><a href="#2936">2936</a></td></tr
><tr id="gr_svn139_2937"

><td id="2937"><a href="#2937">2937</a></td></tr
><tr id="gr_svn139_2938"

><td id="2938"><a href="#2938">2938</a></td></tr
><tr id="gr_svn139_2939"

><td id="2939"><a href="#2939">2939</a></td></tr
><tr id="gr_svn139_2940"

><td id="2940"><a href="#2940">2940</a></td></tr
><tr id="gr_svn139_2941"

><td id="2941"><a href="#2941">2941</a></td></tr
><tr id="gr_svn139_2942"

><td id="2942"><a href="#2942">2942</a></td></tr
><tr id="gr_svn139_2943"

><td id="2943"><a href="#2943">2943</a></td></tr
><tr id="gr_svn139_2944"

><td id="2944"><a href="#2944">2944</a></td></tr
><tr id="gr_svn139_2945"

><td id="2945"><a href="#2945">2945</a></td></tr
><tr id="gr_svn139_2946"

><td id="2946"><a href="#2946">2946</a></td></tr
><tr id="gr_svn139_2947"

><td id="2947"><a href="#2947">2947</a></td></tr
><tr id="gr_svn139_2948"

><td id="2948"><a href="#2948">2948</a></td></tr
><tr id="gr_svn139_2949"

><td id="2949"><a href="#2949">2949</a></td></tr
><tr id="gr_svn139_2950"

><td id="2950"><a href="#2950">2950</a></td></tr
><tr id="gr_svn139_2951"

><td id="2951"><a href="#2951">2951</a></td></tr
><tr id="gr_svn139_2952"

><td id="2952"><a href="#2952">2952</a></td></tr
><tr id="gr_svn139_2953"

><td id="2953"><a href="#2953">2953</a></td></tr
><tr id="gr_svn139_2954"

><td id="2954"><a href="#2954">2954</a></td></tr
><tr id="gr_svn139_2955"

><td id="2955"><a href="#2955">2955</a></td></tr
><tr id="gr_svn139_2956"

><td id="2956"><a href="#2956">2956</a></td></tr
><tr id="gr_svn139_2957"

><td id="2957"><a href="#2957">2957</a></td></tr
><tr id="gr_svn139_2958"

><td id="2958"><a href="#2958">2958</a></td></tr
><tr id="gr_svn139_2959"

><td id="2959"><a href="#2959">2959</a></td></tr
><tr id="gr_svn139_2960"

><td id="2960"><a href="#2960">2960</a></td></tr
><tr id="gr_svn139_2961"

><td id="2961"><a href="#2961">2961</a></td></tr
><tr id="gr_svn139_2962"

><td id="2962"><a href="#2962">2962</a></td></tr
><tr id="gr_svn139_2963"

><td id="2963"><a href="#2963">2963</a></td></tr
><tr id="gr_svn139_2964"

><td id="2964"><a href="#2964">2964</a></td></tr
><tr id="gr_svn139_2965"

><td id="2965"><a href="#2965">2965</a></td></tr
><tr id="gr_svn139_2966"

><td id="2966"><a href="#2966">2966</a></td></tr
><tr id="gr_svn139_2967"

><td id="2967"><a href="#2967">2967</a></td></tr
><tr id="gr_svn139_2968"

><td id="2968"><a href="#2968">2968</a></td></tr
><tr id="gr_svn139_2969"

><td id="2969"><a href="#2969">2969</a></td></tr
><tr id="gr_svn139_2970"

><td id="2970"><a href="#2970">2970</a></td></tr
><tr id="gr_svn139_2971"

><td id="2971"><a href="#2971">2971</a></td></tr
><tr id="gr_svn139_2972"

><td id="2972"><a href="#2972">2972</a></td></tr
><tr id="gr_svn139_2973"

><td id="2973"><a href="#2973">2973</a></td></tr
><tr id="gr_svn139_2974"

><td id="2974"><a href="#2974">2974</a></td></tr
><tr id="gr_svn139_2975"

><td id="2975"><a href="#2975">2975</a></td></tr
><tr id="gr_svn139_2976"

><td id="2976"><a href="#2976">2976</a></td></tr
><tr id="gr_svn139_2977"

><td id="2977"><a href="#2977">2977</a></td></tr
><tr id="gr_svn139_2978"

><td id="2978"><a href="#2978">2978</a></td></tr
><tr id="gr_svn139_2979"

><td id="2979"><a href="#2979">2979</a></td></tr
><tr id="gr_svn139_2980"

><td id="2980"><a href="#2980">2980</a></td></tr
><tr id="gr_svn139_2981"

><td id="2981"><a href="#2981">2981</a></td></tr
><tr id="gr_svn139_2982"

><td id="2982"><a href="#2982">2982</a></td></tr
><tr id="gr_svn139_2983"

><td id="2983"><a href="#2983">2983</a></td></tr
><tr id="gr_svn139_2984"

><td id="2984"><a href="#2984">2984</a></td></tr
><tr id="gr_svn139_2985"

><td id="2985"><a href="#2985">2985</a></td></tr
><tr id="gr_svn139_2986"

><td id="2986"><a href="#2986">2986</a></td></tr
><tr id="gr_svn139_2987"

><td id="2987"><a href="#2987">2987</a></td></tr
><tr id="gr_svn139_2988"

><td id="2988"><a href="#2988">2988</a></td></tr
><tr id="gr_svn139_2989"

><td id="2989"><a href="#2989">2989</a></td></tr
><tr id="gr_svn139_2990"

><td id="2990"><a href="#2990">2990</a></td></tr
><tr id="gr_svn139_2991"

><td id="2991"><a href="#2991">2991</a></td></tr
><tr id="gr_svn139_2992"

><td id="2992"><a href="#2992">2992</a></td></tr
><tr id="gr_svn139_2993"

><td id="2993"><a href="#2993">2993</a></td></tr
><tr id="gr_svn139_2994"

><td id="2994"><a href="#2994">2994</a></td></tr
><tr id="gr_svn139_2995"

><td id="2995"><a href="#2995">2995</a></td></tr
><tr id="gr_svn139_2996"

><td id="2996"><a href="#2996">2996</a></td></tr
><tr id="gr_svn139_2997"

><td id="2997"><a href="#2997">2997</a></td></tr
><tr id="gr_svn139_2998"

><td id="2998"><a href="#2998">2998</a></td></tr
><tr id="gr_svn139_2999"

><td id="2999"><a href="#2999">2999</a></td></tr
><tr id="gr_svn139_3000"

><td id="3000"><a href="#3000">3000</a></td></tr
><tr id="gr_svn139_3001"

><td id="3001"><a href="#3001">3001</a></td></tr
><tr id="gr_svn139_3002"

><td id="3002"><a href="#3002">3002</a></td></tr
><tr id="gr_svn139_3003"

><td id="3003"><a href="#3003">3003</a></td></tr
><tr id="gr_svn139_3004"

><td id="3004"><a href="#3004">3004</a></td></tr
><tr id="gr_svn139_3005"

><td id="3005"><a href="#3005">3005</a></td></tr
><tr id="gr_svn139_3006"

><td id="3006"><a href="#3006">3006</a></td></tr
><tr id="gr_svn139_3007"

><td id="3007"><a href="#3007">3007</a></td></tr
><tr id="gr_svn139_3008"

><td id="3008"><a href="#3008">3008</a></td></tr
><tr id="gr_svn139_3009"

><td id="3009"><a href="#3009">3009</a></td></tr
><tr id="gr_svn139_3010"

><td id="3010"><a href="#3010">3010</a></td></tr
><tr id="gr_svn139_3011"

><td id="3011"><a href="#3011">3011</a></td></tr
><tr id="gr_svn139_3012"

><td id="3012"><a href="#3012">3012</a></td></tr
><tr id="gr_svn139_3013"

><td id="3013"><a href="#3013">3013</a></td></tr
><tr id="gr_svn139_3014"

><td id="3014"><a href="#3014">3014</a></td></tr
><tr id="gr_svn139_3015"

><td id="3015"><a href="#3015">3015</a></td></tr
><tr id="gr_svn139_3016"

><td id="3016"><a href="#3016">3016</a></td></tr
><tr id="gr_svn139_3017"

><td id="3017"><a href="#3017">3017</a></td></tr
><tr id="gr_svn139_3018"

><td id="3018"><a href="#3018">3018</a></td></tr
><tr id="gr_svn139_3019"

><td id="3019"><a href="#3019">3019</a></td></tr
><tr id="gr_svn139_3020"

><td id="3020"><a href="#3020">3020</a></td></tr
><tr id="gr_svn139_3021"

><td id="3021"><a href="#3021">3021</a></td></tr
><tr id="gr_svn139_3022"

><td id="3022"><a href="#3022">3022</a></td></tr
><tr id="gr_svn139_3023"

><td id="3023"><a href="#3023">3023</a></td></tr
><tr id="gr_svn139_3024"

><td id="3024"><a href="#3024">3024</a></td></tr
><tr id="gr_svn139_3025"

><td id="3025"><a href="#3025">3025</a></td></tr
><tr id="gr_svn139_3026"

><td id="3026"><a href="#3026">3026</a></td></tr
><tr id="gr_svn139_3027"

><td id="3027"><a href="#3027">3027</a></td></tr
><tr id="gr_svn139_3028"

><td id="3028"><a href="#3028">3028</a></td></tr
><tr id="gr_svn139_3029"

><td id="3029"><a href="#3029">3029</a></td></tr
><tr id="gr_svn139_3030"

><td id="3030"><a href="#3030">3030</a></td></tr
><tr id="gr_svn139_3031"

><td id="3031"><a href="#3031">3031</a></td></tr
><tr id="gr_svn139_3032"

><td id="3032"><a href="#3032">3032</a></td></tr
><tr id="gr_svn139_3033"

><td id="3033"><a href="#3033">3033</a></td></tr
><tr id="gr_svn139_3034"

><td id="3034"><a href="#3034">3034</a></td></tr
><tr id="gr_svn139_3035"

><td id="3035"><a href="#3035">3035</a></td></tr
><tr id="gr_svn139_3036"

><td id="3036"><a href="#3036">3036</a></td></tr
><tr id="gr_svn139_3037"

><td id="3037"><a href="#3037">3037</a></td></tr
><tr id="gr_svn139_3038"

><td id="3038"><a href="#3038">3038</a></td></tr
><tr id="gr_svn139_3039"

><td id="3039"><a href="#3039">3039</a></td></tr
><tr id="gr_svn139_3040"

><td id="3040"><a href="#3040">3040</a></td></tr
><tr id="gr_svn139_3041"

><td id="3041"><a href="#3041">3041</a></td></tr
><tr id="gr_svn139_3042"

><td id="3042"><a href="#3042">3042</a></td></tr
><tr id="gr_svn139_3043"

><td id="3043"><a href="#3043">3043</a></td></tr
><tr id="gr_svn139_3044"

><td id="3044"><a href="#3044">3044</a></td></tr
><tr id="gr_svn139_3045"

><td id="3045"><a href="#3045">3045</a></td></tr
><tr id="gr_svn139_3046"

><td id="3046"><a href="#3046">3046</a></td></tr
><tr id="gr_svn139_3047"

><td id="3047"><a href="#3047">3047</a></td></tr
><tr id="gr_svn139_3048"

><td id="3048"><a href="#3048">3048</a></td></tr
><tr id="gr_svn139_3049"

><td id="3049"><a href="#3049">3049</a></td></tr
><tr id="gr_svn139_3050"

><td id="3050"><a href="#3050">3050</a></td></tr
><tr id="gr_svn139_3051"

><td id="3051"><a href="#3051">3051</a></td></tr
><tr id="gr_svn139_3052"

><td id="3052"><a href="#3052">3052</a></td></tr
><tr id="gr_svn139_3053"

><td id="3053"><a href="#3053">3053</a></td></tr
><tr id="gr_svn139_3054"

><td id="3054"><a href="#3054">3054</a></td></tr
><tr id="gr_svn139_3055"

><td id="3055"><a href="#3055">3055</a></td></tr
><tr id="gr_svn139_3056"

><td id="3056"><a href="#3056">3056</a></td></tr
><tr id="gr_svn139_3057"

><td id="3057"><a href="#3057">3057</a></td></tr
><tr id="gr_svn139_3058"

><td id="3058"><a href="#3058">3058</a></td></tr
><tr id="gr_svn139_3059"

><td id="3059"><a href="#3059">3059</a></td></tr
><tr id="gr_svn139_3060"

><td id="3060"><a href="#3060">3060</a></td></tr
><tr id="gr_svn139_3061"

><td id="3061"><a href="#3061">3061</a></td></tr
><tr id="gr_svn139_3062"

><td id="3062"><a href="#3062">3062</a></td></tr
><tr id="gr_svn139_3063"

><td id="3063"><a href="#3063">3063</a></td></tr
><tr id="gr_svn139_3064"

><td id="3064"><a href="#3064">3064</a></td></tr
><tr id="gr_svn139_3065"

><td id="3065"><a href="#3065">3065</a></td></tr
><tr id="gr_svn139_3066"

><td id="3066"><a href="#3066">3066</a></td></tr
><tr id="gr_svn139_3067"

><td id="3067"><a href="#3067">3067</a></td></tr
><tr id="gr_svn139_3068"

><td id="3068"><a href="#3068">3068</a></td></tr
><tr id="gr_svn139_3069"

><td id="3069"><a href="#3069">3069</a></td></tr
><tr id="gr_svn139_3070"

><td id="3070"><a href="#3070">3070</a></td></tr
><tr id="gr_svn139_3071"

><td id="3071"><a href="#3071">3071</a></td></tr
><tr id="gr_svn139_3072"

><td id="3072"><a href="#3072">3072</a></td></tr
><tr id="gr_svn139_3073"

><td id="3073"><a href="#3073">3073</a></td></tr
><tr id="gr_svn139_3074"

><td id="3074"><a href="#3074">3074</a></td></tr
><tr id="gr_svn139_3075"

><td id="3075"><a href="#3075">3075</a></td></tr
><tr id="gr_svn139_3076"

><td id="3076"><a href="#3076">3076</a></td></tr
><tr id="gr_svn139_3077"

><td id="3077"><a href="#3077">3077</a></td></tr
><tr id="gr_svn139_3078"

><td id="3078"><a href="#3078">3078</a></td></tr
><tr id="gr_svn139_3079"

><td id="3079"><a href="#3079">3079</a></td></tr
><tr id="gr_svn139_3080"

><td id="3080"><a href="#3080">3080</a></td></tr
><tr id="gr_svn139_3081"

><td id="3081"><a href="#3081">3081</a></td></tr
><tr id="gr_svn139_3082"

><td id="3082"><a href="#3082">3082</a></td></tr
><tr id="gr_svn139_3083"

><td id="3083"><a href="#3083">3083</a></td></tr
><tr id="gr_svn139_3084"

><td id="3084"><a href="#3084">3084</a></td></tr
><tr id="gr_svn139_3085"

><td id="3085"><a href="#3085">3085</a></td></tr
><tr id="gr_svn139_3086"

><td id="3086"><a href="#3086">3086</a></td></tr
><tr id="gr_svn139_3087"

><td id="3087"><a href="#3087">3087</a></td></tr
><tr id="gr_svn139_3088"

><td id="3088"><a href="#3088">3088</a></td></tr
><tr id="gr_svn139_3089"

><td id="3089"><a href="#3089">3089</a></td></tr
><tr id="gr_svn139_3090"

><td id="3090"><a href="#3090">3090</a></td></tr
><tr id="gr_svn139_3091"

><td id="3091"><a href="#3091">3091</a></td></tr
><tr id="gr_svn139_3092"

><td id="3092"><a href="#3092">3092</a></td></tr
><tr id="gr_svn139_3093"

><td id="3093"><a href="#3093">3093</a></td></tr
><tr id="gr_svn139_3094"

><td id="3094"><a href="#3094">3094</a></td></tr
><tr id="gr_svn139_3095"

><td id="3095"><a href="#3095">3095</a></td></tr
><tr id="gr_svn139_3096"

><td id="3096"><a href="#3096">3096</a></td></tr
><tr id="gr_svn139_3097"

><td id="3097"><a href="#3097">3097</a></td></tr
><tr id="gr_svn139_3098"

><td id="3098"><a href="#3098">3098</a></td></tr
><tr id="gr_svn139_3099"

><td id="3099"><a href="#3099">3099</a></td></tr
><tr id="gr_svn139_3100"

><td id="3100"><a href="#3100">3100</a></td></tr
><tr id="gr_svn139_3101"

><td id="3101"><a href="#3101">3101</a></td></tr
><tr id="gr_svn139_3102"

><td id="3102"><a href="#3102">3102</a></td></tr
><tr id="gr_svn139_3103"

><td id="3103"><a href="#3103">3103</a></td></tr
><tr id="gr_svn139_3104"

><td id="3104"><a href="#3104">3104</a></td></tr
><tr id="gr_svn139_3105"

><td id="3105"><a href="#3105">3105</a></td></tr
><tr id="gr_svn139_3106"

><td id="3106"><a href="#3106">3106</a></td></tr
><tr id="gr_svn139_3107"

><td id="3107"><a href="#3107">3107</a></td></tr
><tr id="gr_svn139_3108"

><td id="3108"><a href="#3108">3108</a></td></tr
><tr id="gr_svn139_3109"

><td id="3109"><a href="#3109">3109</a></td></tr
><tr id="gr_svn139_3110"

><td id="3110"><a href="#3110">3110</a></td></tr
><tr id="gr_svn139_3111"

><td id="3111"><a href="#3111">3111</a></td></tr
><tr id="gr_svn139_3112"

><td id="3112"><a href="#3112">3112</a></td></tr
><tr id="gr_svn139_3113"

><td id="3113"><a href="#3113">3113</a></td></tr
><tr id="gr_svn139_3114"

><td id="3114"><a href="#3114">3114</a></td></tr
><tr id="gr_svn139_3115"

><td id="3115"><a href="#3115">3115</a></td></tr
><tr id="gr_svn139_3116"

><td id="3116"><a href="#3116">3116</a></td></tr
><tr id="gr_svn139_3117"

><td id="3117"><a href="#3117">3117</a></td></tr
><tr id="gr_svn139_3118"

><td id="3118"><a href="#3118">3118</a></td></tr
><tr id="gr_svn139_3119"

><td id="3119"><a href="#3119">3119</a></td></tr
><tr id="gr_svn139_3120"

><td id="3120"><a href="#3120">3120</a></td></tr
><tr id="gr_svn139_3121"

><td id="3121"><a href="#3121">3121</a></td></tr
><tr id="gr_svn139_3122"

><td id="3122"><a href="#3122">3122</a></td></tr
><tr id="gr_svn139_3123"

><td id="3123"><a href="#3123">3123</a></td></tr
><tr id="gr_svn139_3124"

><td id="3124"><a href="#3124">3124</a></td></tr
><tr id="gr_svn139_3125"

><td id="3125"><a href="#3125">3125</a></td></tr
><tr id="gr_svn139_3126"

><td id="3126"><a href="#3126">3126</a></td></tr
><tr id="gr_svn139_3127"

><td id="3127"><a href="#3127">3127</a></td></tr
><tr id="gr_svn139_3128"

><td id="3128"><a href="#3128">3128</a></td></tr
><tr id="gr_svn139_3129"

><td id="3129"><a href="#3129">3129</a></td></tr
><tr id="gr_svn139_3130"

><td id="3130"><a href="#3130">3130</a></td></tr
><tr id="gr_svn139_3131"

><td id="3131"><a href="#3131">3131</a></td></tr
><tr id="gr_svn139_3132"

><td id="3132"><a href="#3132">3132</a></td></tr
><tr id="gr_svn139_3133"

><td id="3133"><a href="#3133">3133</a></td></tr
><tr id="gr_svn139_3134"

><td id="3134"><a href="#3134">3134</a></td></tr
><tr id="gr_svn139_3135"

><td id="3135"><a href="#3135">3135</a></td></tr
><tr id="gr_svn139_3136"

><td id="3136"><a href="#3136">3136</a></td></tr
><tr id="gr_svn139_3137"

><td id="3137"><a href="#3137">3137</a></td></tr
><tr id="gr_svn139_3138"

><td id="3138"><a href="#3138">3138</a></td></tr
><tr id="gr_svn139_3139"

><td id="3139"><a href="#3139">3139</a></td></tr
><tr id="gr_svn139_3140"

><td id="3140"><a href="#3140">3140</a></td></tr
><tr id="gr_svn139_3141"

><td id="3141"><a href="#3141">3141</a></td></tr
><tr id="gr_svn139_3142"

><td id="3142"><a href="#3142">3142</a></td></tr
><tr id="gr_svn139_3143"

><td id="3143"><a href="#3143">3143</a></td></tr
><tr id="gr_svn139_3144"

><td id="3144"><a href="#3144">3144</a></td></tr
><tr id="gr_svn139_3145"

><td id="3145"><a href="#3145">3145</a></td></tr
><tr id="gr_svn139_3146"

><td id="3146"><a href="#3146">3146</a></td></tr
><tr id="gr_svn139_3147"

><td id="3147"><a href="#3147">3147</a></td></tr
><tr id="gr_svn139_3148"

><td id="3148"><a href="#3148">3148</a></td></tr
><tr id="gr_svn139_3149"

><td id="3149"><a href="#3149">3149</a></td></tr
><tr id="gr_svn139_3150"

><td id="3150"><a href="#3150">3150</a></td></tr
><tr id="gr_svn139_3151"

><td id="3151"><a href="#3151">3151</a></td></tr
><tr id="gr_svn139_3152"

><td id="3152"><a href="#3152">3152</a></td></tr
><tr id="gr_svn139_3153"

><td id="3153"><a href="#3153">3153</a></td></tr
><tr id="gr_svn139_3154"

><td id="3154"><a href="#3154">3154</a></td></tr
><tr id="gr_svn139_3155"

><td id="3155"><a href="#3155">3155</a></td></tr
><tr id="gr_svn139_3156"

><td id="3156"><a href="#3156">3156</a></td></tr
><tr id="gr_svn139_3157"

><td id="3157"><a href="#3157">3157</a></td></tr
><tr id="gr_svn139_3158"

><td id="3158"><a href="#3158">3158</a></td></tr
><tr id="gr_svn139_3159"

><td id="3159"><a href="#3159">3159</a></td></tr
><tr id="gr_svn139_3160"

><td id="3160"><a href="#3160">3160</a></td></tr
><tr id="gr_svn139_3161"

><td id="3161"><a href="#3161">3161</a></td></tr
><tr id="gr_svn139_3162"

><td id="3162"><a href="#3162">3162</a></td></tr
><tr id="gr_svn139_3163"

><td id="3163"><a href="#3163">3163</a></td></tr
><tr id="gr_svn139_3164"

><td id="3164"><a href="#3164">3164</a></td></tr
><tr id="gr_svn139_3165"

><td id="3165"><a href="#3165">3165</a></td></tr
><tr id="gr_svn139_3166"

><td id="3166"><a href="#3166">3166</a></td></tr
><tr id="gr_svn139_3167"

><td id="3167"><a href="#3167">3167</a></td></tr
><tr id="gr_svn139_3168"

><td id="3168"><a href="#3168">3168</a></td></tr
><tr id="gr_svn139_3169"

><td id="3169"><a href="#3169">3169</a></td></tr
><tr id="gr_svn139_3170"

><td id="3170"><a href="#3170">3170</a></td></tr
><tr id="gr_svn139_3171"

><td id="3171"><a href="#3171">3171</a></td></tr
><tr id="gr_svn139_3172"

><td id="3172"><a href="#3172">3172</a></td></tr
><tr id="gr_svn139_3173"

><td id="3173"><a href="#3173">3173</a></td></tr
><tr id="gr_svn139_3174"

><td id="3174"><a href="#3174">3174</a></td></tr
><tr id="gr_svn139_3175"

><td id="3175"><a href="#3175">3175</a></td></tr
><tr id="gr_svn139_3176"

><td id="3176"><a href="#3176">3176</a></td></tr
><tr id="gr_svn139_3177"

><td id="3177"><a href="#3177">3177</a></td></tr
><tr id="gr_svn139_3178"

><td id="3178"><a href="#3178">3178</a></td></tr
><tr id="gr_svn139_3179"

><td id="3179"><a href="#3179">3179</a></td></tr
><tr id="gr_svn139_3180"

><td id="3180"><a href="#3180">3180</a></td></tr
><tr id="gr_svn139_3181"

><td id="3181"><a href="#3181">3181</a></td></tr
><tr id="gr_svn139_3182"

><td id="3182"><a href="#3182">3182</a></td></tr
><tr id="gr_svn139_3183"

><td id="3183"><a href="#3183">3183</a></td></tr
><tr id="gr_svn139_3184"

><td id="3184"><a href="#3184">3184</a></td></tr
><tr id="gr_svn139_3185"

><td id="3185"><a href="#3185">3185</a></td></tr
><tr id="gr_svn139_3186"

><td id="3186"><a href="#3186">3186</a></td></tr
><tr id="gr_svn139_3187"

><td id="3187"><a href="#3187">3187</a></td></tr
><tr id="gr_svn139_3188"

><td id="3188"><a href="#3188">3188</a></td></tr
><tr id="gr_svn139_3189"

><td id="3189"><a href="#3189">3189</a></td></tr
><tr id="gr_svn139_3190"

><td id="3190"><a href="#3190">3190</a></td></tr
><tr id="gr_svn139_3191"

><td id="3191"><a href="#3191">3191</a></td></tr
><tr id="gr_svn139_3192"

><td id="3192"><a href="#3192">3192</a></td></tr
><tr id="gr_svn139_3193"

><td id="3193"><a href="#3193">3193</a></td></tr
><tr id="gr_svn139_3194"

><td id="3194"><a href="#3194">3194</a></td></tr
><tr id="gr_svn139_3195"

><td id="3195"><a href="#3195">3195</a></td></tr
><tr id="gr_svn139_3196"

><td id="3196"><a href="#3196">3196</a></td></tr
><tr id="gr_svn139_3197"

><td id="3197"><a href="#3197">3197</a></td></tr
><tr id="gr_svn139_3198"

><td id="3198"><a href="#3198">3198</a></td></tr
><tr id="gr_svn139_3199"

><td id="3199"><a href="#3199">3199</a></td></tr
><tr id="gr_svn139_3200"

><td id="3200"><a href="#3200">3200</a></td></tr
><tr id="gr_svn139_3201"

><td id="3201"><a href="#3201">3201</a></td></tr
><tr id="gr_svn139_3202"

><td id="3202"><a href="#3202">3202</a></td></tr
><tr id="gr_svn139_3203"

><td id="3203"><a href="#3203">3203</a></td></tr
><tr id="gr_svn139_3204"

><td id="3204"><a href="#3204">3204</a></td></tr
><tr id="gr_svn139_3205"

><td id="3205"><a href="#3205">3205</a></td></tr
><tr id="gr_svn139_3206"

><td id="3206"><a href="#3206">3206</a></td></tr
><tr id="gr_svn139_3207"

><td id="3207"><a href="#3207">3207</a></td></tr
><tr id="gr_svn139_3208"

><td id="3208"><a href="#3208">3208</a></td></tr
></table></pre>
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
</td>
<td id="lines">
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
<pre ><table id="src_table_0"><tr
id=sl_svn139_1

><td class="source"># Licence<br></td></tr
><tr
id=sl_svn139_2

><td class="source"># =======<br></td></tr
><tr
id=sl_svn139_3

><td class="source"># <br></td></tr
><tr
id=sl_svn139_4

><td class="source"># windows-privesc-check - Security Auditing Tool For Windows<br></td></tr
><tr
id=sl_svn139_5

><td class="source"># Copyright (C) 2010  pentestmonkey@pentestmonkey.net<br></td></tr
><tr
id=sl_svn139_6

><td class="source">#                     http://pentestmonkey.net/windows-privesc-check<br></td></tr
><tr
id=sl_svn139_7

><td class="source"># <br></td></tr
><tr
id=sl_svn139_8

><td class="source"># This tool may be used for legal purposes only.  Users take full responsibility<br></td></tr
><tr
id=sl_svn139_9

><td class="source"># for any actions performed using this tool.  The author accepts no liability for<br></td></tr
><tr
id=sl_svn139_10

><td class="source"># damage caused by this tool.  If these terms are not acceptable to you, then you  <br></td></tr
><tr
id=sl_svn139_11

><td class="source"># may not use this tool.<br></td></tr
><tr
id=sl_svn139_12

><td class="source">#<br></td></tr
><tr
id=sl_svn139_13

><td class="source"># In all other respects the GPL version 2 applies.<br></td></tr
><tr
id=sl_svn139_14

><td class="source"># <br></td></tr
><tr
id=sl_svn139_15

><td class="source"># This program is free software; you can redistribute it and/or modify<br></td></tr
><tr
id=sl_svn139_16

><td class="source"># it under the terms of the GNU General Public License as published by<br></td></tr
><tr
id=sl_svn139_17

><td class="source"># the Free Software Foundation; either version 2 of the License, or<br></td></tr
><tr
id=sl_svn139_18

><td class="source"># (at your option) any later version.<br></td></tr
><tr
id=sl_svn139_19

><td class="source"># <br></td></tr
><tr
id=sl_svn139_20

><td class="source"># This program is distributed in the hope that it will be useful,<br></td></tr
><tr
id=sl_svn139_21

><td class="source"># but WITHOUT ANY WARRANTY; without even the implied warranty of<br></td></tr
><tr
id=sl_svn139_22

><td class="source"># MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the<br></td></tr
><tr
id=sl_svn139_23

><td class="source"># GNU General Public License for more details.<br></td></tr
><tr
id=sl_svn139_24

><td class="source"># <br></td></tr
><tr
id=sl_svn139_25

><td class="source"># You should have received a copy of the GNU General Public License along<br></td></tr
><tr
id=sl_svn139_26

><td class="source"># with this program; if not, write to the Free Software Foundation, Inc.,<br></td></tr
><tr
id=sl_svn139_27

><td class="source"># 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.<br></td></tr
><tr
id=sl_svn139_28

><td class="source"><br></td></tr
><tr
id=sl_svn139_29

><td class="source"># TODO List<br></td></tr
><tr
id=sl_svn139_30

><td class="source"># =========<br></td></tr
><tr
id=sl_svn139_31

><td class="source">#<br></td></tr
><tr
id=sl_svn139_32

><td class="source"># TODO review &quot;read&quot; perms.  should probably ignore these.<br></td></tr
><tr
id=sl_svn139_33

><td class="source"># TODO explaination of what various permissions mean<br></td></tr
><tr
id=sl_svn139_34

><td class="source"># TODO Audit: Process listing, full paths and perms of all processes<br></td></tr
><tr
id=sl_svn139_35

><td class="source"># TODO dlls used by programs (for all checks)<br></td></tr
><tr
id=sl_svn139_36

><td class="source"># TODO find web roots and check for write access<br></td></tr
><tr
id=sl_svn139_37

><td class="source"># TODO support remote server (remote file, reg keys, unc paths for file, remote resolving of sids)<br></td></tr
><tr
id=sl_svn139_38

><td class="source"># TODO task scheduler<br></td></tr
><tr
id=sl_svn139_39

><td class="source"># TODO alert if lanman hashes are being stored (for post-exploitation)<br></td></tr
><tr
id=sl_svn139_40

><td class="source"># TODO alert if named local/domain service accounts are being used (for post-exploitation)<br></td></tr
><tr
id=sl_svn139_41

><td class="source"># TODO Alert if really important patches are missing.  These are metasploitable:<br></td></tr
><tr
id=sl_svn139_42

><td class="source">#  MS10_015 977165 Vulnerabilities in Windows Kernel Could Allow Elevation of Privilege (kitrap0d - meterpreter &quot;getsystem&quot;)<br></td></tr
><tr
id=sl_svn139_43

><td class="source">#  MS03_049 828749 Microsoft Workstation Service NetAddAlternateComputerName Overflow (netapi)     <br></td></tr
><tr
id=sl_svn139_44

><td class="source">#  MS04_007 828028 Microsoft ASN.1 Library Bitstring Heap Overflow (killbill)      <br></td></tr
><tr
id=sl_svn139_45

><td class="source">#  MS04_011 835732 Microsoft LSASS Service DsRolerUpgradeDownlevelServer Overflow (lsass)    <br></td></tr
><tr
id=sl_svn139_46

><td class="source">#  MS04_031 841533 Microsoft NetDDE Service Overflow (netdde)<br></td></tr
><tr
id=sl_svn139_47

><td class="source">#  MS05_039 899588 Microsoft Plug and Play Service Overflow (pnp)<br></td></tr
><tr
id=sl_svn139_48

><td class="source">#  MS06_025 911280 Microsoft RRAS Service RASMAN Registry Overflow (rasmans_reg)<br></td></tr
><tr
id=sl_svn139_49

><td class="source">#  MS06_025 911280 Microsoft RRAS Service Overflow (rras)<br></td></tr
><tr
id=sl_svn139_50

><td class="source">#  MS06_040 921883 Microsoft Server Service NetpwPathCanonicalize Overflow (netapi)<br></td></tr
><tr
id=sl_svn139_51

><td class="source">#  MS06_066 923980 Microsoft Services MS06-066 nwapi32.dll (nwapi)<br></td></tr
><tr
id=sl_svn139_52

><td class="source">#  MS06_066 923980 Microsoft Services MS06-066 nwwks.dll (nwwks)<br></td></tr
><tr
id=sl_svn139_53

><td class="source">#  MS06_070 924270 Microsoft Workstation Service NetpManageIPCConnect Overflow (wkssvc)<br></td></tr
><tr
id=sl_svn139_54

><td class="source">#  MS07_029 935966 Microsoft DNS RPC Service extractQuotedChar() Overflow (SMB) (msdns_zonename)<br></td></tr
><tr
id=sl_svn139_55

><td class="source">#  MS08_067 958644 Microsoft Server Service Relative Path Stack Corruption (netapi)<br></td></tr
><tr
id=sl_svn139_56

><td class="source">#  MS09_050 975517 Microsoft SRV2.SYS SMB Negotiate ProcessID Function Table Dereference (smb2_negotiate_func_index)<br></td></tr
><tr
id=sl_svn139_57

><td class="source">#  MS03_026 823980 Microsoft RPC DCOM Interface Overflow<br></td></tr
><tr
id=sl_svn139_58

><td class="source">#  MS05_017 892944 Microsoft Message Queueing Service Path Overflow<br></td></tr
><tr
id=sl_svn139_59

><td class="source">#  MS07_065 937894 Microsoft Message Queueing Service DNS Name Path Overflow<br></td></tr
><tr
id=sl_svn139_60

><td class="source"># TODO registry key checks for windows services<br></td></tr
><tr
id=sl_svn139_61

><td class="source"># TODO per-user checks including perms on home dirs and startup folders + default user and all users<br></td></tr
><tr
id=sl_svn139_62

><td class="source"># TODO need to be able to order issues more logically.  Maybe group by section?<br></td></tr
><tr
id=sl_svn139_63

><td class="source"><br></td></tr
><tr
id=sl_svn139_64

><td class="source"># Building an Executable<br></td></tr
><tr
id=sl_svn139_65

><td class="source"># ======================<br></td></tr
><tr
id=sl_svn139_66

><td class="source">#<br></td></tr
><tr
id=sl_svn139_67

><td class="source"># This script should be converted to an exe before it is used for<br></td></tr
><tr
id=sl_svn139_68

><td class="source"># auditing - otherwise you&#39;d have to install loads of dependencies<br></td></tr
><tr
id=sl_svn139_69

><td class="source"># on the target system.<br></td></tr
><tr
id=sl_svn139_70

><td class="source">#<br></td></tr
><tr
id=sl_svn139_71

><td class="source"># Download pyinstaller: http://www.pyinstaller.org/changeset/latest/trunk?old_path=%2F&amp;format=zip<br></td></tr
><tr
id=sl_svn139_72

><td class="source"># Read the docs: http://www.pyinstaller.org/export/latest/tags/1.4/doc/Manual.html?format=raw<br></td></tr
><tr
id=sl_svn139_73

><td class="source">#<br></td></tr
><tr
id=sl_svn139_74

><td class="source"># Unzip to c:\pyinstaller (say)<br></td></tr
><tr
id=sl_svn139_75

><td class="source"># cd c:\pyinstaller<br></td></tr
><tr
id=sl_svn139_76

><td class="source"># python Configure.py<br></td></tr
><tr
id=sl_svn139_77

><td class="source"># python Makespec.py --onefile c:\somepath\wpc.py<br></td></tr
><tr
id=sl_svn139_78

><td class="source"># python Build.py wpc\wpc.spec<br></td></tr
><tr
id=sl_svn139_79

><td class="source"># wpc\dist\wpc.exe<br></td></tr
><tr
id=sl_svn139_80

><td class="source">#<br></td></tr
><tr
id=sl_svn139_81

><td class="source"># Alternative to pyinstaller is cxfreeze.  This doesn&#39;t always work, though:<br></td></tr
><tr
id=sl_svn139_82

><td class="source"># \Python26\Scripts\cxfreeze wpc.py --target-dir dist<br></td></tr
><tr
id=sl_svn139_83

><td class="source"># zip -r wpc.zip dist<br></td></tr
><tr
id=sl_svn139_84

><td class="source"># <br></td></tr
><tr
id=sl_svn139_85

><td class="source"># You then need to copy wpc.zip to the target and unzip it.  The exe therein<br></td></tr
><tr
id=sl_svn139_86

><td class="source"># should then run because all the dependencies are in the current (dist) directory.<br></td></tr
><tr
id=sl_svn139_87

><td class="source"><br></td></tr
><tr
id=sl_svn139_88

><td class="source"># 64-bit vs 32-bit<br></td></tr
><tr
id=sl_svn139_89

><td class="source"># ================<br></td></tr
><tr
id=sl_svn139_90

><td class="source">#<br></td></tr
><tr
id=sl_svn139_91

><td class="source"># If we run a 32-bit version of this script on a 64-bit box we have (at least) the <br></td></tr
><tr
id=sl_svn139_92

><td class="source"># following problems:<br></td></tr
><tr
id=sl_svn139_93

><td class="source"># * Registry:  We CAN&#39;T see the whole 64-bit registry.  This seems insurmountable.<br></td></tr
><tr
id=sl_svn139_94

><td class="source"># * Files:     It&#39;s harder to see in system32.  This can be worked round.<br></td></tr
><tr
id=sl_svn139_95

><td class="source"><br></td></tr
><tr
id=sl_svn139_96

><td class="source"># What types of object have permissions?<br></td></tr
><tr
id=sl_svn139_97

><td class="source"># ======================================<br></td></tr
><tr
id=sl_svn139_98

><td class="source">#<br></td></tr
><tr
id=sl_svn139_99

><td class="source"># Files, directories and registry keys are the obvious candidates.  There are several others too...<br></td></tr
><tr
id=sl_svn139_100

><td class="source">#<br></td></tr
><tr
id=sl_svn139_101

><td class="source"># This provides a good summary: http://msdn.microsoft.com/en-us/library/aa379557%28v=VS.85%29.aspx<br></td></tr
><tr
id=sl_svn139_102

><td class="source">#<br></td></tr
><tr
id=sl_svn139_103

><td class="source"># Files or directories on an NTFS file system	GetNamedSecurityInfo, SetNamedSecurityInfo, GetSecurityInfo, SetSecurityInfo<br></td></tr
><tr
id=sl_svn139_104

><td class="source"># Named pipes<br></td></tr
><tr
id=sl_svn139_105

><td class="source"># Anonymous pipes<br></td></tr
><tr
id=sl_svn139_106

><td class="source"># Processes<br></td></tr
><tr
id=sl_svn139_107

><td class="source"># Threads<br></td></tr
><tr
id=sl_svn139_108

><td class="source"># File-mapping objects	<br></td></tr
><tr
id=sl_svn139_109

><td class="source"># Access tokens	<br></td></tr
><tr
id=sl_svn139_110

><td class="source"># Window-management objects (window stations and desktops)<br></td></tr
><tr
id=sl_svn139_111

><td class="source"># Registry keys	<br></td></tr
><tr
id=sl_svn139_112

><td class="source"># Windows services<br></td></tr
><tr
id=sl_svn139_113

><td class="source"># Local or remote printers	<br></td></tr
><tr
id=sl_svn139_114

><td class="source"># Network shares	<br></td></tr
><tr
id=sl_svn139_115

><td class="source"># Interprocess synchronization objects <br></td></tr
><tr
id=sl_svn139_116

><td class="source"># Directory service objects	<br></td></tr
><tr
id=sl_svn139_117

><td class="source">#<br></td></tr
><tr
id=sl_svn139_118

><td class="source"># This provides a good description of how Access Tokens interact with the Security Descriptors on Securable Objects: http://msdn.microsoft.com/en-us/library/aa374876%28v=VS.85%29.aspx<br></td></tr
><tr
id=sl_svn139_119

><td class="source">#<br></td></tr
><tr
id=sl_svn139_120

><td class="source"># http://msdn.microsoft.com/en-us/library/aa379593(VS.85).aspx<br></td></tr
><tr
id=sl_svn139_121

><td class="source">#  win32security.SE_UNKNOWN_OBJECT_TYPE - n/a<br></td></tr
><tr
id=sl_svn139_122

><td class="source">#  win32security.SE_FILE_OBJECT - poc working<br></td></tr
><tr
id=sl_svn139_123

><td class="source">#  win32security.SE_SERVICE - poc working<br></td></tr
><tr
id=sl_svn139_124

><td class="source">#  win32security.SE_PRINTER - TODO Indicates a printer. A printer object can be a local printer, such as PrinterName, or a remote printer, such as <br></td></tr
><tr
id=sl_svn139_125

><td class="source">#                      \\ComputerName\PrinterName.<br></td></tr
><tr
id=sl_svn139_126

><td class="source">#  win32security.SE_REGISTRY_KEY - TODO<br></td></tr
><tr
id=sl_svn139_127

><td class="source">#     Indicates a registry key. A registry key object can be in the local registry, such as CLASSES_ROOT\SomePath or in a remote registry, <br></td></tr
><tr
id=sl_svn139_128

><td class="source">#     such as \\ComputerName\CLASSES_ROOT\SomePath.<br></td></tr
><tr
id=sl_svn139_129

><td class="source">#     The names of registry keys must use the following literal strings to identify the predefined registry keys: <br></td></tr
><tr
id=sl_svn139_130

><td class="source">#     &quot;CLASSES_ROOT&quot;, &quot;CURRENT_USER&quot;, &quot;MACHINE&quot;, and &quot;USERS&quot;.<br></td></tr
><tr
id=sl_svn139_131

><td class="source">#     perms: http://msdn.microsoft.com/en-us/library/ms724878(VS.85).aspx<br></td></tr
><tr
id=sl_svn139_132

><td class="source">#  win32security.SE_LMSHARE - TODO Indicates a network share. A share object can be local, such as ShareName, or remote, such as \\ComputerName\ShareName.<br></td></tr
><tr
id=sl_svn139_133

><td class="source">#  win32security.SE_KERNEL_OBJECT - TODO<br></td></tr
><tr
id=sl_svn139_134

><td class="source">#        Indicates a local  kernel object.<br></td></tr
><tr
id=sl_svn139_135

><td class="source">#        The GetSecurityInfo and SetSecurityInfo functions support all types of kernel objects. <br></td></tr
><tr
id=sl_svn139_136

><td class="source">#        The GetNamedSecurityInfo and SetNamedSecurityInfo functions work only with the following kernel objects: <br></td></tr
><tr
id=sl_svn139_137

><td class="source">#        semaphore, event, mutex, waitable timer, and file mapping.<br></td></tr
><tr
id=sl_svn139_138

><td class="source">#  win32security.SE_WINDOW_OBJECT - TODO Indicates a window station or desktop object on the local computer. <br></td></tr
><tr
id=sl_svn139_139

><td class="source">#                    You cannot use GetNamedSecurityInfo and SetNamedSecurityInfo with these objects because the names of window stations or desktops are not unique.<br></td></tr
><tr
id=sl_svn139_140

><td class="source">#  win32security.SE_DS_OBJECT - TODO - Active Directory object<br></td></tr
><tr
id=sl_svn139_141

><td class="source">#                 Indicates a directory service object or a property set or property of a directory service object. <br></td></tr
><tr
id=sl_svn139_142

><td class="source">#                 The name string for a directory service object must be in  X.500 form, for example:<br></td></tr
><tr
id=sl_svn139_143

><td class="source">#                 CN=SomeObject,OU=ou2,OU=ou1,DC=DomainName,DC=CompanyName,DC=com,O=internet<br></td></tr
><tr
id=sl_svn139_144

><td class="source">#					perm list: http://msdn.microsoft.com/en-us/library/aa772285(VS.85).aspx<br></td></tr
><tr
id=sl_svn139_145

><td class="source">#  win32security.SE_DS_OBJECT_ALL - TODO <br></td></tr
><tr
id=sl_svn139_146

><td class="source">#             Indicates a directory service object and all of its property sets and properties. <br></td></tr
><tr
id=sl_svn139_147

><td class="source">#  win32security.SE_PROVIDER_DEFINED_OBJECT - TODO Indicates a provider-defined object. <br></td></tr
><tr
id=sl_svn139_148

><td class="source">#  win32security.SE_WMIGUID_OBJECT - TODO Indicates a WMI object.<br></td></tr
><tr
id=sl_svn139_149

><td class="source">#  win32security.SE_REGISTRY_WOW64_32KEY - TODO Indicates an object for a registry entry under WOW64. <br></td></tr
><tr
id=sl_svn139_150

><td class="source"><br></td></tr
><tr
id=sl_svn139_151

><td class="source"># What sort of privileges can be granted on Windows?<br></td></tr
><tr
id=sl_svn139_152

><td class="source"># ==================================================<br></td></tr
><tr
id=sl_svn139_153

><td class="source">#<br></td></tr
><tr
id=sl_svn139_154

><td class="source"># These are bit like Capabilities on Linux.<br></td></tr
><tr
id=sl_svn139_155

><td class="source"># http://msdn.microsoft.com/en-us/library/bb530716(VS.85).aspx<br></td></tr
><tr
id=sl_svn139_156

><td class="source"># http://msdn.microsoft.com/en-us/library/bb545671(VS.85).aspx<br></td></tr
><tr
id=sl_svn139_157

><td class="source">#<br></td></tr
><tr
id=sl_svn139_158

><td class="source"># These privs sound like they might allow the holder to gain admin rights:<br></td></tr
><tr
id=sl_svn139_159

><td class="source">#<br></td></tr
><tr
id=sl_svn139_160

><td class="source"># SE_ASSIGNPRIMARYTOKEN_NAME TEXT(&quot;SeAssignPrimaryTokenPrivilege&quot;) Required to assign the primary token of a process. User Right: Replace a process-level token.<br></td></tr
><tr
id=sl_svn139_161

><td class="source"># SE_BACKUP_NAME TEXT(&quot;SeBackupPrivilege&quot;) Required to perform backup operations. This privilege causes the system to grant all read access control to any file, regardless of the access control list (ACL) specified for the file. Any access request other than read is still evaluated with the ACL. This privilege is required by the RegSaveKey and RegSaveKeyExfunctions. The following access rights are granted if this privilege is held: READ_CONTROL ACCESS_SYSTEM_SECURITY FILE_GENERIC_READ FILE_TRAVERSE User Right: Back up files and directories.<br></td></tr
><tr
id=sl_svn139_162

><td class="source"># SE_CREATE_PAGEFILE_NAME TEXT(&quot;SeCreatePagefilePrivilege&quot;) Required to create a paging file. User Right: Create a pagefile.<br></td></tr
><tr
id=sl_svn139_163

><td class="source"># SE_CREATE_TOKEN_NAME TEXT(&quot;SeCreateTokenPrivilege&quot;) Required to create a primary token. User Right: Create a token object.<br></td></tr
><tr
id=sl_svn139_164

><td class="source"># SE_DEBUG_NAME TEXT(&quot;SeDebugPrivilege&quot;) Required to debug and adjust the memory of a process owned by another account. User Right: Debug programs.<br></td></tr
><tr
id=sl_svn139_165

><td class="source"># SE_ENABLE_DELEGATION_NAME TEXT(&quot;SeEnableDelegationPrivilege&quot;) Required to mark user and computer accounts as trusted for delegation. User Right: Enable computer and user accounts to be trusted for delegation.<br></td></tr
><tr
id=sl_svn139_166

><td class="source"># SE_LOAD_DRIVER_NAME TEXT(&quot;SeLoadDriverPrivilege&quot;) Required to load or unload a device driver. User Right: Load and unload device drivers.<br></td></tr
><tr
id=sl_svn139_167

><td class="source"># SE_MACHINE_ACCOUNT_NAME TEXT(&quot;SeMachineAccountPrivilege&quot;) Required to create a computer account. User Right: Add workstations to domain.<br></td></tr
><tr
id=sl_svn139_168

><td class="source"># SE_MANAGE_VOLUME_NAME TEXT(&quot;SeManageVolumePrivilege&quot;) Required to enable volume management privileges. User Right: Manage the files on a volume.<br></td></tr
><tr
id=sl_svn139_169

><td class="source"># SE_RELABEL_NAME TEXT(&quot;SeRelabelPrivilege&quot;) Required to modify the mandatory integrity level of an object. User Right: Modify an object label.<br></td></tr
><tr
id=sl_svn139_170

><td class="source"># SE_RESTORE_NAME TEXT(&quot;SeRestorePrivilege&quot;) Required to perform restore operations. This privilege causes the system to grant all write access control to any file, regardless of the ACL specified for the file. Any access request other than write is still evaluated with the ACL. Additionally, this privilege enables you to set any valid user or group SID as the owner of a file. This privilege is required by the RegLoadKey function. The following access rights are granted if this privilege is held: WRITE_DAC WRITE_OWNER ACCESS_SYSTEM_SECURITY FILE_GENERIC_WRITE FILE_ADD_FILE FILE_ADD_SUBDIRECTORY DELETE User Right: Restore files and directories.<br></td></tr
><tr
id=sl_svn139_171

><td class="source"># SE_SHUTDOWN_NAME TEXT(&quot;SeShutdownPrivilege&quot;) Required to shut down a local system. User Right: Shut down the system.<br></td></tr
><tr
id=sl_svn139_172

><td class="source"># SE_SYNC_AGENT_NAME TEXT(&quot;SeSyncAgentPrivilege&quot;) Required for a domain controller to use the LDAP directory synchronization services. This privilege enables the holder to read all objects and properties in the directory, regardless of the protection on the objects and properties. By default, it is assigned to the Administrator and LocalSystem accounts on domain controllers. User Right: Synchronize directory service data.<br></td></tr
><tr
id=sl_svn139_173

><td class="source"># SE_TAKE_OWNERSHIP_NAME TEXT(&quot;SeTakeOwnershipPrivilege&quot;) Required to take ownership of an object without being granted discretionary access. This privilege allows the owner value to be set only to those values that the holder may legitimately assign as the owner of an object. User Right: Take ownership of files or other objects.<br></td></tr
><tr
id=sl_svn139_174

><td class="source"># SE_TCB_NAME TEXT(&quot;SeTcbPrivilege&quot;) This privilege identifies its holder as part of the trusted computer base. Some trusted protected subsystems are granted this privilege. User Right: Act as part of the operating system.<br></td></tr
><tr
id=sl_svn139_175

><td class="source"># SE_TRUSTED_CREDMAN_ACCESS_NAME TEXT(&quot;SeTrustedCredManAccessPrivilege&quot;) Required to access Credential Manager as a trusted caller. User Right: Access Credential Manager as a trusted caller.<br></td></tr
><tr
id=sl_svn139_176

><td class="source">#<br></td></tr
><tr
id=sl_svn139_177

><td class="source"># These sound like they could be troublesome in the wrong hands:<br></td></tr
><tr
id=sl_svn139_178

><td class="source">#<br></td></tr
><tr
id=sl_svn139_179

><td class="source"># SE_SECURITY_NAME TEXT(&quot;SeSecurityPrivilege&quot;) Required to perform a number of security-related functions, such as controlling and viewing audit messages. This privilege identifies its holder as a security operator. User Right: Manage auditing and security log.<br></td></tr
><tr
id=sl_svn139_180

><td class="source"># SE_REMOTE_SHUTDOWN_NAME TEXT(&quot;SeRemoteShutdownPrivilege&quot;) Required to shut down a system using a network request. User Right: Force shutdown from a remote system.<br></td></tr
><tr
id=sl_svn139_181

><td class="source"># SE_PROF_SINGLE_PROCESS_NAME TEXT(&quot;SeProfileSingleProcessPrivilege&quot;) Required to gather profiling information for a single process. User Right: Profile single process.<br></td></tr
><tr
id=sl_svn139_182

><td class="source"># SE_AUDIT_NAME TEXT(&quot;SeAuditPrivilege&quot;) Required to generate audit-log entries. Give this privilege to secure servers.User Right: Generate security audits.<br></td></tr
><tr
id=sl_svn139_183

><td class="source"># SE_INC_BASE_PRIORITY_NAME TEXT(&quot;SeIncreaseBasePriorityPrivilege&quot;) Required to increase the base priority of a process. User Right: Increase scheduling priority.<br></td></tr
><tr
id=sl_svn139_184

><td class="source"># SE_INC_WORKING_SET_NAME TEXT(&quot;SeIncreaseWorkingSetPrivilege&quot;) Required to allocate more memory for applications that run in the context of users. User Right: Increase a process working set.<br></td></tr
><tr
id=sl_svn139_185

><td class="source"># SE_INCREASE_QUOTA_NAME TEXT(&quot;SeIncreaseQuotaPrivilege&quot;) Required to increase the quota assigned to a process. User Right: Adjust memory quotas for a process.<br></td></tr
><tr
id=sl_svn139_186

><td class="source"># SE_LOCK_MEMORY_NAME TEXT(&quot;SeLockMemoryPrivilege&quot;) Required to lock physical pages in memory. User Right: Lock pages in memory.<br></td></tr
><tr
id=sl_svn139_187

><td class="source"># SE_SYSTEM_ENVIRONMENT_NAME TEXT(&quot;SeSystemEnvironmentPrivilege&quot;) Required to modify the nonvolatile RAM of systems that use this type of memory to store configuration information. User Right: Modify firmware environment values.<br></td></tr
><tr
id=sl_svn139_188

><td class="source">#<br></td></tr
><tr
id=sl_svn139_189

><td class="source"># These sound less interesting:<br></td></tr
><tr
id=sl_svn139_190

><td class="source">#<br></td></tr
><tr
id=sl_svn139_191

><td class="source"># SE_CHANGE_NOTIFY_NAME TEXT(&quot;SeChangeNotifyPrivilege&quot;) Required to receive notifications of changes to files or directories. This privilege also causes the system to skip all traversal access checks. It is enabled by default for all users. User Right: Bypass traverse checking.<br></td></tr
><tr
id=sl_svn139_192

><td class="source"># SE_CREATE_GLOBAL_NAME TEXT(&quot;SeCreateGlobalPrivilege&quot;) Required to create named file mapping objects in the global namespace during Terminal Services sessions. This privilege is enabled by default for administrators, services, and the local system account.User Right: Create global objects. Windows XP/2000:  This privilege is not supported. Note that this value is supported starting with Windows Server 2003, Windows XP with SP2, and Windows 2000 with SP4.<br></td></tr
><tr
id=sl_svn139_193

><td class="source"># SE_CREATE_PERMANENT_NAME TEXT(&quot;SeCreatePermanentPrivilege&quot;) Required to create a permanent object. User Right: Create permanent shared objects.<br></td></tr
><tr
id=sl_svn139_194

><td class="source"># SE_CREATE_SYMBOLIC_LINK_NAME TEXT(&quot;SeCreateSymbolicLinkPrivilege&quot;) Required to create a symbolic link. User Right: Create symbolic links.<br></td></tr
><tr
id=sl_svn139_195

><td class="source"># SE_IMPERSONATE_NAME TEXT(&quot;SeImpersonatePrivilege&quot;) Required to impersonate. User Right: Impersonate a client after authentication.    Windows XP/2000:  This privilege is not supported. Note that this value is supported starting with Windows Server 2003, Windows XP with SP2, and Windows 2000 with SP4.<br></td></tr
><tr
id=sl_svn139_196

><td class="source"># SE_SYSTEM_PROFILE_NAME TEXT(&quot;SeSystemProfilePrivilege&quot;) Required to gather profiling information for the entire system. User Right: Profile system performance.<br></td></tr
><tr
id=sl_svn139_197

><td class="source"># SE_SYSTEMTIME_NAME TEXT(&quot;SeSystemtimePrivilege&quot;) Required to modify the system time. User Right: Change the system time.<br></td></tr
><tr
id=sl_svn139_198

><td class="source"># SE_TIME_ZONE_NAME TEXT(&quot;SeTimeZonePrivilege&quot;) Required to adjust the time zone associated with the computer&#39;s internal clock. User Right: Change the time zone.<br></td></tr
><tr
id=sl_svn139_199

><td class="source"># SE_UNDOCK_NAME TEXT(&quot;SeUndockPrivilege&quot;) Required to undock a laptop. User Right: Remove computer from docking station.<br></td></tr
><tr
id=sl_svn139_200

><td class="source"># SE_UNSOLICITED_INPUT_NAME TEXT(&quot;SeUnsolicitedInputPrivilege&quot;) Required to read unsolicited input from a terminal device. User Right: Not applicable.<br></td></tr
><tr
id=sl_svn139_201

><td class="source"><br></td></tr
><tr
id=sl_svn139_202

><td class="source"># These are from ntsecapi.h:<br></td></tr
><tr
id=sl_svn139_203

><td class="source">#<br></td></tr
><tr
id=sl_svn139_204

><td class="source"># SE_BATCH_LOGON_NAME TEXT(&quot;SeBatchLogonRight&quot;) Required for an account to log on using the batch logon type.<br></td></tr
><tr
id=sl_svn139_205

><td class="source"># SE_DENY_BATCH_LOGON_NAME TEXT(&quot;SeDenyBatchLogonRight&quot;) Explicitly denies an account the right to log on using the batch logon type.<br></td></tr
><tr
id=sl_svn139_206

><td class="source"># SE_DENY_INTERACTIVE_LOGON_NAME TEXT(&quot;SeDenyInteractiveLogonRight&quot;) Explicitly denies an account the right to log on using the interactive logon type.<br></td></tr
><tr
id=sl_svn139_207

><td class="source"># SE_DENY_NETWORK_LOGON_NAME TEXT(&quot;SeDenyNetworkLogonRight&quot;) Explicitly denies an account the right to log on using the network logon type.<br></td></tr
><tr
id=sl_svn139_208

><td class="source"># SE_DENY_REMOTE_INTERACTIVE_LOGON_NAME TEXT(&quot;SeDenyRemoteInteractiveLogonRight&quot;) Explicitly denies an account the right to log on remotely using the interactive logon type.<br></td></tr
><tr
id=sl_svn139_209

><td class="source"># SE_DENY_SERVICE_LOGON_NAME TEXT(&quot;SeDenyServiceLogonRight&quot;) Explicitly denies an account the right to log on using the service logon type.<br></td></tr
><tr
id=sl_svn139_210

><td class="source"># SE_INTERACTIVE_LOGON_NAME TEXT(&quot;SeInteractiveLogonRight&quot;) Required for an account to log on using the interactive logon type.<br></td></tr
><tr
id=sl_svn139_211

><td class="source"># SE_NETWORK_LOGON_NAME TEXT(&quot;SeNetworkLogonRight&quot;) Required for an account to log on using the network logon type.<br></td></tr
><tr
id=sl_svn139_212

><td class="source"># SE_REMOTE_INTERACTIVE_LOGON_NAME TEXT(&quot;SeRemoteInteractiveLogonRight&quot;) Required for an account to log on remotely using the interactive logon type.<br></td></tr
><tr
id=sl_svn139_213

><td class="source"># SE_SERVICE_LOGON_NAME TEXT(&quot;SeServiceLogonRight&quot;) Required for an account to log on using the service logon type.<br></td></tr
><tr
id=sl_svn139_214

><td class="source"><br></td></tr
><tr
id=sl_svn139_215

><td class="source">#import pythoncom, sys, os, time, win32api<br></td></tr
><tr
id=sl_svn139_216

><td class="source">#from win32com.taskscheduler import taskscheduler<br></td></tr
><tr
id=sl_svn139_217

><td class="source">import glob<br></td></tr
><tr
id=sl_svn139_218

><td class="source">import datetime<br></td></tr
><tr
id=sl_svn139_219

><td class="source">import socket<br></td></tr
><tr
id=sl_svn139_220

><td class="source">import os, sys<br></td></tr
><tr
id=sl_svn139_221

><td class="source">import win32process<br></td></tr
><tr
id=sl_svn139_222

><td class="source">import re<br></td></tr
><tr
id=sl_svn139_223

><td class="source">import win32security, ntsecuritycon, win32api, win32con, win32file<br></td></tr
><tr
id=sl_svn139_224

><td class="source">import win32service<br></td></tr
><tr
id=sl_svn139_225

><td class="source">import pywintypes # doesn&#39;t play well with molebox pro - why did we need this anyway?<br></td></tr
><tr
id=sl_svn139_226

><td class="source">import win32net<br></td></tr
><tr
id=sl_svn139_227

><td class="source">import ctypes<br></td></tr
><tr
id=sl_svn139_228

><td class="source">import getopt<br></td></tr
><tr
id=sl_svn139_229

><td class="source">import _winreg<br></td></tr
><tr
id=sl_svn139_230

><td class="source">import win32netcon<br></td></tr
><tr
id=sl_svn139_231

><td class="source">from subprocess import Popen, PIPE, STDOUT<br></td></tr
><tr
id=sl_svn139_232

><td class="source"># from winapi import *<br></td></tr
><tr
id=sl_svn139_233

><td class="source">from ntsecuritycon import TokenSessionId, TokenSandBoxInert, TokenType, TokenImpersonationLevel, TokenVirtualizationEnabled, TokenVirtualizationAllowed, TokenHasRestrictions, TokenElevationType, TokenUIAccess, TokenUser, TokenOwner, TokenGroups, TokenRestrictedSids, TokenPrivileges, TokenPrimaryGroup, TokenSource, TokenDefaultDacl, TokenStatistics, TokenOrigin, TokenLinkedToken, TokenLogonSid, TokenElevation, TokenIntegrityLevel, TokenMandatoryPolicy, SE_ASSIGNPRIMARYTOKEN_NAME, SE_BACKUP_NAME, SE_CREATE_PAGEFILE_NAME, SE_CREATE_TOKEN_NAME, SE_DEBUG_NAME, SE_LOAD_DRIVER_NAME, SE_MACHINE_ACCOUNT_NAME, SE_RESTORE_NAME, SE_SHUTDOWN_NAME, SE_TAKE_OWNERSHIP_NAME, SE_TCB_NAME<br></td></tr
><tr
id=sl_svn139_234

><td class="source"># Need: SE_ENABLE_DELEGATION_NAME, SE_MANAGE_VOLUME_NAME, SE_RELABEL_NAME, SE_SYNC_AGENT_NAME, SE_TRUSTED_CREDMAN_ACCESS_NAME<br></td></tr
><tr
id=sl_svn139_235

><td class="source">k32 = ctypes.windll.kernel32<br></td></tr
><tr
id=sl_svn139_236

><td class="source">wow64 = ctypes.c_long( 0 )<br></td></tr
><tr
id=sl_svn139_237

><td class="source">on64bitwindows = 1<br></td></tr
><tr
id=sl_svn139_238

><td class="source">remote_server = None<br></td></tr
><tr
id=sl_svn139_239

><td class="source">remote_username = None<br></td></tr
><tr
id=sl_svn139_240

><td class="source">remote_password = None<br></td></tr
><tr
id=sl_svn139_241

><td class="source">remote_domain = None<br></td></tr
><tr
id=sl_svn139_242

><td class="source">local_ips = socket.gethostbyname_ex(socket.gethostname())[2] # have to do this before Wow64DisableWow64FsRedirection<br></td></tr
><tr
id=sl_svn139_243

><td class="source"><br></td></tr
><tr
id=sl_svn139_244

><td class="source">version = &quot;1.0&quot;<br></td></tr
><tr
id=sl_svn139_245

><td class="source">svnversion=&quot;$Revision$&quot; # Don&#39;t change this line.  Auto-updated.<br></td></tr
><tr
id=sl_svn139_246

><td class="source">svnnum=re.sub(&#39;[^0-9]&#39;, &#39;&#39;, svnversion)<br></td></tr
><tr
id=sl_svn139_247

><td class="source">if svnnum:<br></td></tr
><tr
id=sl_svn139_248

><td class="source">	version = version + &quot;svn&quot; + svnnum<br></td></tr
><tr
id=sl_svn139_249

><td class="source"><br></td></tr
><tr
id=sl_svn139_250

><td class="source">all_checks       = 0<br></td></tr
><tr
id=sl_svn139_251

><td class="source">registry_checks  = 0<br></td></tr
><tr
id=sl_svn139_252

><td class="source">path_checks      = 0<br></td></tr
><tr
id=sl_svn139_253

><td class="source">service_checks   = 0<br></td></tr
><tr
id=sl_svn139_254

><td class="source">service_audit    = 0<br></td></tr
><tr
id=sl_svn139_255

><td class="source">drive_checks     = 0<br></td></tr
><tr
id=sl_svn139_256

><td class="source">eventlog_checks  = 0<br></td></tr
><tr
id=sl_svn139_257

><td class="source">progfiles_checks = 0<br></td></tr
><tr
id=sl_svn139_258

><td class="source">process_checks   = 0<br></td></tr
><tr
id=sl_svn139_259

><td class="source">share_checks     = 0<br></td></tr
><tr
id=sl_svn139_260

><td class="source">passpol_audit    = 0<br></td></tr
><tr
id=sl_svn139_261

><td class="source">user_group_audit = 0<br></td></tr
><tr
id=sl_svn139_262

><td class="source">logged_in_audit  = 0<br></td></tr
><tr
id=sl_svn139_263

><td class="source">process_audit    = 0<br></td></tr
><tr
id=sl_svn139_264

><td class="source">admin_users_audit= 0<br></td></tr
><tr
id=sl_svn139_265

><td class="source">host_info_audit  = 0<br></td></tr
><tr
id=sl_svn139_266

><td class="source">ignore_trusted   = 0<br></td></tr
><tr
id=sl_svn139_267

><td class="source">owner_info       = 0<br></td></tr
><tr
id=sl_svn139_268

><td class="source">weak_perms_only  = 0<br></td></tr
><tr
id=sl_svn139_269

><td class="source">host_info_audit     = 0<br></td></tr
><tr
id=sl_svn139_270

><td class="source">patch_checks     = 0<br></td></tr
><tr
id=sl_svn139_271

><td class="source">verbose          = 0<br></td></tr
><tr
id=sl_svn139_272

><td class="source">report_file_name = None<br></td></tr
><tr
id=sl_svn139_273

><td class="source"><br></td></tr
><tr
id=sl_svn139_274

><td class="source">kb_nos = {<br></td></tr
><tr
id=sl_svn139_275

><td class="source">        &#39;977165&#39;: &#39;MS10_015 Vulnerabilities in Windows Kernel Could Allow Elevation of Privilege (kitrap0d - meterpreter &quot;getsystem&quot;)&#39;,<br></td></tr
><tr
id=sl_svn139_276

><td class="source">        &#39;828749&#39;: &#39;MS03_049 Microsoft Workstation Service NetAddAlternateComputerName Overflow (netapi)     &#39;,<br></td></tr
><tr
id=sl_svn139_277

><td class="source">        &#39;828028&#39;: &#39;MS04_007 Microsoft ASN.1 Library Bitstring Heap Overflow (killbill)      &#39;,<br></td></tr
><tr
id=sl_svn139_278

><td class="source">        &#39;835732&#39;: &#39;MS04_011 Microsoft LSASS Service DsRolerUpgradeDownlevelServer Overflow (lsass)    &#39;,<br></td></tr
><tr
id=sl_svn139_279

><td class="source">        &#39;841533&#39;: &#39;MS04_031 Microsoft NetDDE Service Overflow (netdde)&#39;,<br></td></tr
><tr
id=sl_svn139_280

><td class="source">        &#39;899588&#39;: &#39;MS05_039 Microsoft Plug and Play Service Overflow (pnp)&#39;,<br></td></tr
><tr
id=sl_svn139_281

><td class="source">        &#39;911280&#39;: &#39;MS06_025 Microsoft RRAS Service RASMAN Registry Overflow (rasmans_reg)&#39;,<br></td></tr
><tr
id=sl_svn139_282

><td class="source">        &#39;911280&#39;: &#39;MS06_025 Microsoft RRAS Service Overflow (rras)&#39;,<br></td></tr
><tr
id=sl_svn139_283

><td class="source">        &#39;921883&#39;: &#39;MS06_040 Microsoft Server Service NetpwPathCanonicalize Overflow (netapi)&#39;,<br></td></tr
><tr
id=sl_svn139_284

><td class="source">        &#39;923980&#39;: &#39;MS06_066 Microsoft Services MS06-066 nwapi32.dll (nwapi)&#39;,<br></td></tr
><tr
id=sl_svn139_285

><td class="source">        &#39;923980&#39;: &#39;MS06_066 Microsoft Services MS06-066 nwwks.dll (nwwks)&#39;,<br></td></tr
><tr
id=sl_svn139_286

><td class="source">        &#39;924270&#39;: &#39;MS06_070 Microsoft Workstation Service NetpManageIPCConnect Overflow (wkssvc)&#39;,<br></td></tr
><tr
id=sl_svn139_287

><td class="source">        &#39;935966&#39;: &#39;MS07_029 Microsoft DNS RPC Service extractQuotedChar() Overflow (SMB) (msdns_zonename)&#39;,<br></td></tr
><tr
id=sl_svn139_288

><td class="source">        &#39;958644&#39;: &#39;MS08_067 Microsoft Server Service Relative Path Stack Corruption (netapi)&#39;,<br></td></tr
><tr
id=sl_svn139_289

><td class="source">        &#39;975517&#39;: &#39;MS09_050 Microsoft SRV2.SYS SMB Negotiate ProcessID Function Table Dereference (smb2_negotiate_func_index)&#39;,<br></td></tr
><tr
id=sl_svn139_290

><td class="source">        &#39;823980&#39;: &#39;MS03_026 Microsoft RPC DCOM Interface Overflow&#39;,<br></td></tr
><tr
id=sl_svn139_291

><td class="source">        &#39;892944&#39;: &#39;MS05_017 Microsoft Message Queueing Service Path Overflow&#39;,<br></td></tr
><tr
id=sl_svn139_292

><td class="source">        &#39;937894&#39;: &#39;MS07_065 Microsoft Message Queueing Service DNS Name Path Overflow&#39;<br></td></tr
><tr
id=sl_svn139_293

><td class="source">}<br></td></tr
><tr
id=sl_svn139_294

><td class="source"><br></td></tr
><tr
id=sl_svn139_295

><td class="source">reg_paths = (<br></td></tr
><tr
id=sl_svn139_296

><td class="source">	&#39;HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services&#39;,<br></td></tr
><tr
id=sl_svn139_297

><td class="source">	&#39;HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run&#39;,<br></td></tr
><tr
id=sl_svn139_298

><td class="source">	&#39;HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run&#39;,<br></td></tr
><tr
id=sl_svn139_299

><td class="source">	&#39;HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce&#39;,<br></td></tr
><tr
id=sl_svn139_300

><td class="source">	&#39;HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run&#39;,<br></td></tr
><tr
id=sl_svn139_301

><td class="source">	&#39;HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell&#39;,<br></td></tr
><tr
id=sl_svn139_302

><td class="source">	&#39;HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit&#39;,<br></td></tr
><tr
id=sl_svn139_303

><td class="source">	&#39;HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce&#39;,<br></td></tr
><tr
id=sl_svn139_304

><td class="source">	&#39;HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce&#39;,<br></td></tr
><tr
id=sl_svn139_305

><td class="source">	&#39;HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServices&#39;,<br></td></tr
><tr
id=sl_svn139_306

><td class="source">	&#39;HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce&#39;,<br></td></tr
><tr
id=sl_svn139_307

><td class="source">	&#39;HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServices&#39;,<br></td></tr
><tr
id=sl_svn139_308

><td class="source">	&#39;HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce&#39;,<br></td></tr
><tr
id=sl_svn139_309

><td class="source">	&#39;HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows&#39;,<br></td></tr
><tr
id=sl_svn139_310

><td class="source">)<br></td></tr
><tr
id=sl_svn139_311

><td class="source"><br></td></tr
><tr
id=sl_svn139_312

><td class="source"># We don&#39;t care if some users / groups hold dangerous permission because they&#39;re trusted<br></td></tr
><tr
id=sl_svn139_313

><td class="source"># These have fully qualified names:<br></td></tr
><tr
id=sl_svn139_314

><td class="source">trusted_principles_fq = (<br></td></tr
><tr
id=sl_svn139_315

><td class="source">	&quot;BUILTIN\\Administrators&quot;,<br></td></tr
><tr
id=sl_svn139_316

><td class="source">	&quot;NT SERVICE\\TrustedInstaller&quot;,<br></td></tr
><tr
id=sl_svn139_317

><td class="source">	&quot;NT AUTHORITY\\SYSTEM&quot;<br></td></tr
><tr
id=sl_svn139_318

><td class="source">)<br></td></tr
><tr
id=sl_svn139_319

><td class="source"><br></td></tr
><tr
id=sl_svn139_320

><td class="source"># We may temporarily regard a user as trusted (e.g. if we&#39;re looking for writable<br></td></tr
><tr
id=sl_svn139_321

><td class="source"># files in a user&#39;s path, we do not care that he can write to his own path)<br></td></tr
><tr
id=sl_svn139_322

><td class="source">tmp_trusted_principles_fq = (<br></td></tr
><tr
id=sl_svn139_323

><td class="source">)<br></td></tr
><tr
id=sl_svn139_324

><td class="source"><br></td></tr
><tr
id=sl_svn139_325

><td class="source">eventlog_key_hklm = &#39;SYSTEM\CurrentControlSet\Services\Eventlog&#39;<br></td></tr
><tr
id=sl_svn139_326

><td class="source"><br></td></tr
><tr
id=sl_svn139_327

><td class="source"># We don&#39;t care if members of these groups hold dangerous permission because they&#39;re trusted<br></td></tr
><tr
id=sl_svn139_328

><td class="source"># These have names without a domain:<br></td></tr
><tr
id=sl_svn139_329

><td class="source">trusted_principles = (<br></td></tr
><tr
id=sl_svn139_330

><td class="source">	&quot;Administrators&quot;,<br></td></tr
><tr
id=sl_svn139_331

><td class="source">	&quot;Domain Admins&quot;,<br></td></tr
><tr
id=sl_svn139_332

><td class="source">	&quot;Enterprise Admins&quot;,<br></td></tr
><tr
id=sl_svn139_333

><td class="source">)<br></td></tr
><tr
id=sl_svn139_334

><td class="source"><br></td></tr
><tr
id=sl_svn139_335

><td class="source"># Windows privileges from <br></td></tr
><tr
id=sl_svn139_336

><td class="source">windows_privileges = (<br></td></tr
><tr
id=sl_svn139_337

><td class="source">        &quot;SeAssignPrimaryTokenPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_338

><td class="source">        &quot;SeBackupPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_339

><td class="source">        &quot;SeCreatePagefilePrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_340

><td class="source">        &quot;SeCreateTokenPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_341

><td class="source">        &quot;SeDebugPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_342

><td class="source">        &quot;SeEnableDelegationPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_343

><td class="source">        &quot;SeLoadDriverPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_344

><td class="source">        &quot;SeMachineAccountPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_345

><td class="source">        &quot;SeManageVolumePrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_346

><td class="source">        &quot;SeRelabelPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_347

><td class="source">        &quot;SeRestorePrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_348

><td class="source">        &quot;SeShutdownPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_349

><td class="source">        &quot;SeSyncAgentPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_350

><td class="source">        &quot;SeTakeOwnershipPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_351

><td class="source">        &quot;SeTcbPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_352

><td class="source">        &quot;SeTrustedCredManAccessPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_353

><td class="source">        &quot;SeSecurityPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_354

><td class="source">        &quot;SeRemoteShutdownPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_355

><td class="source">        &quot;SeProfileSingleProcessPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_356

><td class="source">        &quot;SeAuditPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_357

><td class="source">        &quot;SeIncreaseBasePriorityPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_358

><td class="source">        &quot;SeIncreaseWorkingSetPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_359

><td class="source">        &quot;SeIncreaseQuotaPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_360

><td class="source">        &quot;SeLockMemoryPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_361

><td class="source">        &quot;SeSystemEnvironmentPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_362

><td class="source">        &quot;SeChangeNotifyPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_363

><td class="source">        &quot;SeCreateGlobalPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_364

><td class="source">        &quot;SeCreatePermanentPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_365

><td class="source">        &quot;SeCreateSymbolicLinkPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_366

><td class="source">        &quot;SeImpersonatePrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_367

><td class="source">        &quot;SeSystemProfilePrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_368

><td class="source">        &quot;SeSystemtimePrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_369

><td class="source">        &quot;SeTimeZonePrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_370

><td class="source">        &quot;SeUndockPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_371

><td class="source">        &quot;SeUnsolicitedInputPrivilege&quot;,<br></td></tr
><tr
id=sl_svn139_372

><td class="source">        &quot;SeBatchLogonRight&quot;,<br></td></tr
><tr
id=sl_svn139_373

><td class="source">        &quot;SeDenyBatchLogonRight&quot;,<br></td></tr
><tr
id=sl_svn139_374

><td class="source">        &quot;SeDenyInteractiveLogonRight&quot;,<br></td></tr
><tr
id=sl_svn139_375

><td class="source">        &quot;SeDenyNetworkLogonRight&quot;,<br></td></tr
><tr
id=sl_svn139_376

><td class="source">        &quot;SeDenyRemoteInteractiveLogonRight&quot;,<br></td></tr
><tr
id=sl_svn139_377

><td class="source">        &quot;SeDenyServiceLogonRight&quot;,<br></td></tr
><tr
id=sl_svn139_378

><td class="source">        &quot;SeInteractiveLogonRight&quot;,<br></td></tr
><tr
id=sl_svn139_379

><td class="source">        &quot;SeNetworkLogonRight&quot;,<br></td></tr
><tr
id=sl_svn139_380

><td class="source">        &quot;SeRemoteInteractiveLogonRight&quot;,<br></td></tr
><tr
id=sl_svn139_381

><td class="source">        &quot;SeServiceLogonRight&quot;<br></td></tr
><tr
id=sl_svn139_382

><td class="source">)<br></td></tr
><tr
id=sl_svn139_383

><td class="source"><br></td></tr
><tr
id=sl_svn139_384

><td class="source">share_types = (<br></td></tr
><tr
id=sl_svn139_385

><td class="source">	&quot;STYPE_IPC&quot;,<br></td></tr
><tr
id=sl_svn139_386

><td class="source">	&quot;STYPE_DISKTREE&quot;,<br></td></tr
><tr
id=sl_svn139_387

><td class="source">	&quot;STYPE_PRINTQ&quot;,<br></td></tr
><tr
id=sl_svn139_388

><td class="source">	&quot;STYPE_DEVICE&quot;,<br></td></tr
><tr
id=sl_svn139_389

><td class="source">)<br></td></tr
><tr
id=sl_svn139_390

><td class="source">	<br></td></tr
><tr
id=sl_svn139_391

><td class="source">sv_types = (<br></td></tr
><tr
id=sl_svn139_392

><td class="source">        &quot;SV_TYPE_WORKSTATION&quot;,<br></td></tr
><tr
id=sl_svn139_393

><td class="source">        &quot;SV_TYPE_SERVER&quot;,<br></td></tr
><tr
id=sl_svn139_394

><td class="source">        &quot;SV_TYPE_SQLSERVER&quot;,<br></td></tr
><tr
id=sl_svn139_395

><td class="source">        &quot;SV_TYPE_DOMAIN_CTRL&quot;,<br></td></tr
><tr
id=sl_svn139_396

><td class="source">        &quot;SV_TYPE_DOMAIN_BAKCTRL&quot;,<br></td></tr
><tr
id=sl_svn139_397

><td class="source">        &quot;SV_TYPE_TIME_SOURCE&quot;,<br></td></tr
><tr
id=sl_svn139_398

><td class="source">        &quot;SV_TYPE_AFP&quot;,<br></td></tr
><tr
id=sl_svn139_399

><td class="source">        &quot;SV_TYPE_NOVELL&quot;,<br></td></tr
><tr
id=sl_svn139_400

><td class="source">        &quot;SV_TYPE_DOMAIN_MEMBER&quot;,<br></td></tr
><tr
id=sl_svn139_401

><td class="source">        &quot;SV_TYPE_PRINTQ_SERVER&quot;,<br></td></tr
><tr
id=sl_svn139_402

><td class="source">        &quot;SV_TYPE_DIALIN_SERVER&quot;,<br></td></tr
><tr
id=sl_svn139_403

><td class="source">        &quot;SV_TYPE_XENIX_SERVER&quot;,<br></td></tr
><tr
id=sl_svn139_404

><td class="source">        &quot;SV_TYPE_NT&quot;,<br></td></tr
><tr
id=sl_svn139_405

><td class="source">        &quot;SV_TYPE_WFW&quot;,<br></td></tr
><tr
id=sl_svn139_406

><td class="source">        &quot;SV_TYPE_SERVER_MFPN&quot;,<br></td></tr
><tr
id=sl_svn139_407

><td class="source">        &quot;SV_TYPE_SERVER_NT&quot;,<br></td></tr
><tr
id=sl_svn139_408

><td class="source">        &quot;SV_TYPE_POTENTIAL_BROWSER&quot;,<br></td></tr
><tr
id=sl_svn139_409

><td class="source">        &quot;SV_TYPE_BACKUP_BROWSER&quot;,<br></td></tr
><tr
id=sl_svn139_410

><td class="source">        &quot;SV_TYPE_MASTER_BROWSER&quot;,<br></td></tr
><tr
id=sl_svn139_411

><td class="source">        &quot;SV_TYPE_DOMAIN_MASTER&quot;,<br></td></tr
><tr
id=sl_svn139_412

><td class="source">        &quot;SV_TYPE_SERVER_OSF&quot;,<br></td></tr
><tr
id=sl_svn139_413

><td class="source">        &quot;SV_TYPE_SERVER_VMS&quot;,<br></td></tr
><tr
id=sl_svn139_414

><td class="source">        &quot;SV_TYPE_WINDOWS&quot;,<br></td></tr
><tr
id=sl_svn139_415

><td class="source">        &quot;SV_TYPE_DFS&quot;,<br></td></tr
><tr
id=sl_svn139_416

><td class="source">        &quot;SV_TYPE_CLUSTER_NT&quot;,<br></td></tr
><tr
id=sl_svn139_417

><td class="source">        &quot;SV_TYPE_TERMINALSERVER&quot;, # missing from win32netcon.py<br></td></tr
><tr
id=sl_svn139_418

><td class="source">        #&quot;SV_TYPE_CLUSTER_VS_NT&quot;, # missing from win32netcon.py<br></td></tr
><tr
id=sl_svn139_419

><td class="source">        &quot;SV_TYPE_DCE&quot;,<br></td></tr
><tr
id=sl_svn139_420

><td class="source">        &quot;SV_TYPE_ALTERNATE_XPORT&quot;,<br></td></tr
><tr
id=sl_svn139_421

><td class="source">        &quot;SV_TYPE_LOCAL_LIST_ONLY&quot;,<br></td></tr
><tr
id=sl_svn139_422

><td class="source">        &quot;SV_TYPE_DOMAIN_ENUM&quot;<br></td></tr
><tr
id=sl_svn139_423

><td class="source">)<br></td></tr
><tr
id=sl_svn139_424

><td class="source"><br></td></tr
><tr
id=sl_svn139_425

><td class="source">win32netcon.SV_TYPE_TERMINALSERVER = 0x2000000 <br></td></tr
><tr
id=sl_svn139_426

><td class="source"><br></td></tr
><tr
id=sl_svn139_427

><td class="source">dangerous_perms_write = {<br></td></tr
><tr
id=sl_svn139_428

><td class="source">	# http://www.tek-tips.com/faqs.cfm?fid<br></td></tr
><tr
id=sl_svn139_429

><td class="source">	&#39;share&#39;: {<br></td></tr
><tr
id=sl_svn139_430

><td class="source">		ntsecuritycon: (<br></td></tr
><tr
id=sl_svn139_431

><td class="source">			&quot;FILE_READ_DATA&quot;, #<br></td></tr
><tr
id=sl_svn139_432

><td class="source">			&quot;FILE_WRITE_DATA&quot;,<br></td></tr
><tr
id=sl_svn139_433

><td class="source">			&quot;FILE_APPEND_DATA&quot;,<br></td></tr
><tr
id=sl_svn139_434

><td class="source">			&quot;FILE_READ_EA&quot;, #<br></td></tr
><tr
id=sl_svn139_435

><td class="source">			&quot;FILE_WRITE_EA&quot;,<br></td></tr
><tr
id=sl_svn139_436

><td class="source">			&quot;FILE_EXECUTE&quot;, #<br></td></tr
><tr
id=sl_svn139_437

><td class="source">			&quot;FILE_READ_ATTRIBUTES&quot;, #<br></td></tr
><tr
id=sl_svn139_438

><td class="source">			&quot;FILE_WRITE_ATTRIBUTES&quot;,<br></td></tr
><tr
id=sl_svn139_439

><td class="source">			&quot;DELETE&quot;,<br></td></tr
><tr
id=sl_svn139_440

><td class="source">			&quot;READ_CONTROL&quot;, #<br></td></tr
><tr
id=sl_svn139_441

><td class="source">			&quot;WRITE_DAC&quot;,<br></td></tr
><tr
id=sl_svn139_442

><td class="source">			&quot;WRITE_OWNER&quot;,<br></td></tr
><tr
id=sl_svn139_443

><td class="source">			&quot;SYNCHRONIZE&quot;, #<br></td></tr
><tr
id=sl_svn139_444

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_445

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_446

><td class="source">	&#39;file&#39;: {<br></td></tr
><tr
id=sl_svn139_447

><td class="source">		ntsecuritycon: (<br></td></tr
><tr
id=sl_svn139_448

><td class="source">			#&quot;FILE_READ_DATA&quot;,<br></td></tr
><tr
id=sl_svn139_449

><td class="source">			&quot;FILE_WRITE_DATA&quot;,<br></td></tr
><tr
id=sl_svn139_450

><td class="source">			&quot;FILE_APPEND_DATA&quot;,<br></td></tr
><tr
id=sl_svn139_451

><td class="source">			#&quot;FILE_READ_EA&quot;,<br></td></tr
><tr
id=sl_svn139_452

><td class="source">			&quot;FILE_WRITE_EA&quot;,<br></td></tr
><tr
id=sl_svn139_453

><td class="source">			#&quot;FILE_EXECUTE&quot;,<br></td></tr
><tr
id=sl_svn139_454

><td class="source">			#&quot;FILE_READ_ATTRIBUTES&quot;,<br></td></tr
><tr
id=sl_svn139_455

><td class="source">			&quot;FILE_WRITE_ATTRIBUTES&quot;,<br></td></tr
><tr
id=sl_svn139_456

><td class="source">			&quot;DELETE&quot;,<br></td></tr
><tr
id=sl_svn139_457

><td class="source">			#&quot;READ_CONTROL&quot;,<br></td></tr
><tr
id=sl_svn139_458

><td class="source">			&quot;WRITE_DAC&quot;,<br></td></tr
><tr
id=sl_svn139_459

><td class="source">			&quot;WRITE_OWNER&quot;,<br></td></tr
><tr
id=sl_svn139_460

><td class="source">			#&quot;SYNCHRONIZE&quot;,<br></td></tr
><tr
id=sl_svn139_461

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_462

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_463

><td class="source">	# http://msdn.microsoft.com/en-us/library/ms724878(VS.85).aspx<br></td></tr
><tr
id=sl_svn139_464

><td class="source">	# KEY_ALL_ACCESS: STANDARD_RIGHTS_REQUIRED KEY_QUERY_VALUE KEY_SET_VALUE KEY_CREATE_SUB_KEY KEY_ENUMERATE_SUB_KEYS KEY_NOTIFY KEY_CREATE_LINK<br></td></tr
><tr
id=sl_svn139_465

><td class="source">	# KEY_CREATE_LINK (0x0020) Reserved for system use.<br></td></tr
><tr
id=sl_svn139_466

><td class="source">	# KEY_CREATE_SUB_KEY (0x0004)	Required to create a subkey of a registry key.<br></td></tr
><tr
id=sl_svn139_467

><td class="source">	# KEY_ENUMERATE_SUB_KEYS (0x0008)	Required to enumerate the subkeys of a registry key.<br></td></tr
><tr
id=sl_svn139_468

><td class="source">	# KEY_EXECUTE (0x20019)	Equivalent to KEY_READ.<br></td></tr
><tr
id=sl_svn139_469

><td class="source">	# KEY_NOTIFY (0x0010)	Required to request change notifications for a registry key or for subkeys of a registry key.<br></td></tr
><tr
id=sl_svn139_470

><td class="source">	# KEY_QUERY_VALUE (0x0001)	Required to query the values of a registry key.<br></td></tr
><tr
id=sl_svn139_471

><td class="source">	# KEY_READ (0x20019)	Combines the STANDARD_RIGHTS_READ, KEY_QUERY_VALUE, KEY_ENUMERATE_SUB_KEYS, and KEY_NOTIFY values.<br></td></tr
><tr
id=sl_svn139_472

><td class="source">	# KEY_SET_VALUE (0x0002)	Required to create, delete, or set a registry value.<br></td></tr
><tr
id=sl_svn139_473

><td class="source">	# KEY_WOW64_32KEY (0x0200)	Indicates that an application on 64-bit Windows should operate on the 32-bit registry view. For more information, see Accessing an Alternate Registry View.	This flag must be combined using the OR operator with the other flags in this table that either query or access registry values.<br></td></tr
><tr
id=sl_svn139_474

><td class="source">	# Windows 2000:  This flag is not supported.<br></td></tr
><tr
id=sl_svn139_475

><td class="source">	# KEY_WOW64_64KEY (0x0100)	Indicates that an application on 64-bit Windows should operate on the 64-bit registry view. For more information, see Accessing an Alternate Registry View.<br></td></tr
><tr
id=sl_svn139_476

><td class="source">	# This flag must be combined using the OR operator with the other flags in this table that either query or access registry values.<br></td></tr
><tr
id=sl_svn139_477

><td class="source">	# Windows 2000:  This flag is not supported.<br></td></tr
><tr
id=sl_svn139_478

><td class="source">	# KEY_WRITE (0x20006)	Combines the STANDARD_RIGHTS_WRITE, KEY_SET_VALUE, and KEY_CREATE_SUB_KEY access rights.<br></td></tr
><tr
id=sl_svn139_479

><td class="source">	# &quot;STANDARD_RIGHTS_REQUIRED&quot;,<br></td></tr
><tr
id=sl_svn139_480

><td class="source">	# &quot;STANDARD_RIGHTS_WRITE&quot;,<br></td></tr
><tr
id=sl_svn139_481

><td class="source">	# &quot;STANDARD_RIGHTS_READ&quot;,<br></td></tr
><tr
id=sl_svn139_482

><td class="source">	# &quot;DELETE&quot;,<br></td></tr
><tr
id=sl_svn139_483

><td class="source">	# &quot;READ_CONTROL&quot;,<br></td></tr
><tr
id=sl_svn139_484

><td class="source">	# &quot;WRITE_DAC&quot;,<br></td></tr
><tr
id=sl_svn139_485

><td class="source">	#&quot;WRITE_OWNER&quot;,<br></td></tr
><tr
id=sl_svn139_486

><td class="source">	&#39;reg&#39;: {		<br></td></tr
><tr
id=sl_svn139_487

><td class="source">		_winreg: (<br></td></tr
><tr
id=sl_svn139_488

><td class="source">			#&quot;KEY_ALL_ACCESS&quot;, # Combines the STANDARD_RIGHTS_REQUIRED, KEY_QUERY_VALUE, KEY_SET_VALUE, KEY_CREATE_SUB_KEY, KEY_ENUMERATE_SUB_KEYS, KEY_NOTIFY, and KEY_CREATE_LINK access rights.<br></td></tr
><tr
id=sl_svn139_489

><td class="source">			#&quot;KEY_QUERY_VALUE&quot;, # GUI &quot;Query Value&quot;<br></td></tr
><tr
id=sl_svn139_490

><td class="source">			&quot;KEY_SET_VALUE&quot;, # GUI &quot;Set Value&quot;.  Required to create, delete, or set a registry value.<br></td></tr
><tr
id=sl_svn139_491

><td class="source">			&quot;KEY_CREATE_LINK&quot;, # GUI &quot;Create Link&quot;.  Reserved for system use.<br></td></tr
><tr
id=sl_svn139_492

><td class="source">			&quot;KEY_CREATE_SUB_KEY&quot;, # GUI &quot;Create subkey&quot;<br></td></tr
><tr
id=sl_svn139_493

><td class="source">			# &quot;KEY_ENUMERATE_SUB_KEYS&quot;, # GUI &quot;Create subkeys&quot;<br></td></tr
><tr
id=sl_svn139_494

><td class="source">			# &quot;KEY_NOTIFY&quot;, # GUI &quot;Notify&quot;<br></td></tr
><tr
id=sl_svn139_495

><td class="source">			#&quot;KEY_EXECUTE&quot;, # same as KEY_READ<br></td></tr
><tr
id=sl_svn139_496

><td class="source">			#&quot;KEY_READ&quot;,<br></td></tr
><tr
id=sl_svn139_497

><td class="source">			#&quot;KEY_WOW64_32KEY&quot;,<br></td></tr
><tr
id=sl_svn139_498

><td class="source">			#&quot;KEY_WOW64_64KEY&quot;,<br></td></tr
><tr
id=sl_svn139_499

><td class="source">			# &quot;KEY_WRITE&quot;, # Combines the STANDARD_RIGHTS_WRITE, KEY_SET_VALUE, and KEY_CREATE_SUB_KEY access rights.<br></td></tr
><tr
id=sl_svn139_500

><td class="source">		),<br></td></tr
><tr
id=sl_svn139_501

><td class="source">		ntsecuritycon: (<br></td></tr
><tr
id=sl_svn139_502

><td class="source">			&quot;DELETE&quot;, # GUI &quot;Delete&quot;<br></td></tr
><tr
id=sl_svn139_503

><td class="source">			# &quot;READ_CONTROL&quot;, # GUI &quot;Read Control&quot; - read security descriptor<br></td></tr
><tr
id=sl_svn139_504

><td class="source">			&quot;WRITE_DAC&quot;, # GUI &quot;Write DAC&quot;<br></td></tr
><tr
id=sl_svn139_505

><td class="source">			&quot;WRITE_OWNER&quot;, # GUI &quot;Write Owner&quot;<br></td></tr
><tr
id=sl_svn139_506

><td class="source">			#&quot;STANDARD_RIGHTS_REQUIRED&quot;,<br></td></tr
><tr
id=sl_svn139_507

><td class="source">			#&quot;STANDARD_RIGHTS_WRITE&quot;,<br></td></tr
><tr
id=sl_svn139_508

><td class="source">			#&quot;STANDARD_RIGHTS_READ&quot;,<br></td></tr
><tr
id=sl_svn139_509

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_510

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_511

><td class="source">	&#39;directory&#39;: {<br></td></tr
><tr
id=sl_svn139_512

><td class="source">		ntsecuritycon: (<br></td></tr
><tr
id=sl_svn139_513

><td class="source">			#&quot;FILE_LIST_DIRECTORY&quot;,<br></td></tr
><tr
id=sl_svn139_514

><td class="source">			&quot;FILE_ADD_FILE&quot;,<br></td></tr
><tr
id=sl_svn139_515

><td class="source">			&quot;FILE_ADD_SUBDIRECTORY&quot;,<br></td></tr
><tr
id=sl_svn139_516

><td class="source">			#&quot;FILE_READ_EA&quot;,<br></td></tr
><tr
id=sl_svn139_517

><td class="source">			&quot;FILE_WRITE_EA&quot;,<br></td></tr
><tr
id=sl_svn139_518

><td class="source">			#&quot;FILE_TRAVERSE&quot;,<br></td></tr
><tr
id=sl_svn139_519

><td class="source">			&quot;FILE_DELETE_CHILD&quot;,<br></td></tr
><tr
id=sl_svn139_520

><td class="source">			#&quot;FILE_READ_ATTRIBUTES&quot;,<br></td></tr
><tr
id=sl_svn139_521

><td class="source">			&quot;FILE_WRITE_ATTRIBUTES&quot;,<br></td></tr
><tr
id=sl_svn139_522

><td class="source">			&quot;DELETE&quot;,<br></td></tr
><tr
id=sl_svn139_523

><td class="source">			#&quot;READ_CONTROL&quot;,<br></td></tr
><tr
id=sl_svn139_524

><td class="source">			&quot;WRITE_DAC&quot;,<br></td></tr
><tr
id=sl_svn139_525

><td class="source">			&quot;WRITE_OWNER&quot;,<br></td></tr
><tr
id=sl_svn139_526

><td class="source">			#&quot;SYNCHRONIZE&quot;,<br></td></tr
><tr
id=sl_svn139_527

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_528

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_529

><td class="source">	&#39;service_manager&#39;: {<br></td></tr
><tr
id=sl_svn139_530

><td class="source">		# For service manager<br></td></tr
><tr
id=sl_svn139_531

><td class="source">		# http://msdn.microsoft.com/en-us/library/ms685981(VS.85).aspx<br></td></tr
><tr
id=sl_svn139_532

><td class="source">		# SC_MANAGER_ALL_ACCESS (0xF003F)	Includes STANDARD_RIGHTS_REQUIRED, in addition to all access rights in this table.<br></td></tr
><tr
id=sl_svn139_533

><td class="source">		# SC_MANAGER_CREATE_SERVICE (0x0002)	Required to call the CreateService function to create a service object and add it to the database.<br></td></tr
><tr
id=sl_svn139_534

><td class="source">		# SC_MANAGER_CONNECT (0x0001)	Required to connect to the service control manager.<br></td></tr
><tr
id=sl_svn139_535

><td class="source">		# SC_MANAGER_ENUMERATE_SERVICE (0x0004)	Required to call the EnumServicesStatusEx function to list the services that are in the database.<br></td></tr
><tr
id=sl_svn139_536

><td class="source">		# SC_MANAGER_LOCK (0x0008)	Required to call the LockServiceDatabase function to acquire a lock on the database.<br></td></tr
><tr
id=sl_svn139_537

><td class="source">		# SC_MANAGER_MODIFY_BOOT_CONFIG (0x0020)	Required to call the NotifyBootConfigStatus function.<br></td></tr
><tr
id=sl_svn139_538

><td class="source">		# SC_MANAGER_QUERY_LOCK_STATUS (0x0010)Required to call the  QueryServiceLockStatus function to retrieve the lock status information for the database.<br></td></tr
><tr
id=sl_svn139_539

><td class="source">		win32service: (<br></td></tr
><tr
id=sl_svn139_540

><td class="source">			&quot;SC_MANAGER_ALL_ACCESS&quot;,<br></td></tr
><tr
id=sl_svn139_541

><td class="source">			&quot;SC_MANAGER_CREATE_SERVICE&quot;,<br></td></tr
><tr
id=sl_svn139_542

><td class="source">			&quot;SC_MANAGER_CONNECT&quot;,<br></td></tr
><tr
id=sl_svn139_543

><td class="source">			&quot;SC_MANAGER_ENUMERATE_SERVICE&quot;,<br></td></tr
><tr
id=sl_svn139_544

><td class="source">			&quot;SC_MANAGER_LOCK&quot;,<br></td></tr
><tr
id=sl_svn139_545

><td class="source">			&quot;SC_MANAGER_MODIFY_BOOT_CONFIG&quot;,<br></td></tr
><tr
id=sl_svn139_546

><td class="source">			&quot;SC_MANAGER_QUERY_LOCK_STATUS&quot;,<br></td></tr
><tr
id=sl_svn139_547

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_548

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_549

><td class="source">	&#39;service&#39;: {<br></td></tr
><tr
id=sl_svn139_550

><td class="source">		# For services:<br></td></tr
><tr
id=sl_svn139_551

><td class="source">		# http://msdn.microsoft.com/en-us/library/ms685981(VS.85).aspx<br></td></tr
><tr
id=sl_svn139_552

><td class="source">		# SERVICE_ALL_ACCESS (0xF01FF)	Includes STANDARD_RIGHTS_REQUIRED in addition to all access rights in this table.<br></td></tr
><tr
id=sl_svn139_553

><td class="source">		# SERVICE_CHANGE_CONFIG (0x0002)	Required to call the ChangeServiceConfig or ChangeServiceConfig2 function to change the service configuration. Because 	this grants the caller the right to change the executable file that the system runs, it should be granted only to administrators.<br></td></tr
><tr
id=sl_svn139_554

><td class="source">		# SERVICE_ENUMERATE_DEPENDENTS (0x0008)	Required to call the EnumDependentServices function to enumerate all the services dependent on the service.<br></td></tr
><tr
id=sl_svn139_555

><td class="source">		# SERVICE_INTERROGATE (0x0080)	Required to call the ControlService function to ask the service to report its status immediately.<br></td></tr
><tr
id=sl_svn139_556

><td class="source">		# SERVICE_PAUSE_CONTINUE (0x0040)	Required to call the ControlService function to pause or continue the service.<br></td></tr
><tr
id=sl_svn139_557

><td class="source">		# SERVICE_QUERY_CONFIG (0x0001)	Required to call the QueryServiceConfig and QueryServiceConfig2 functions to query the service configuration.<br></td></tr
><tr
id=sl_svn139_558

><td class="source">		# SERVICE_QUERY_STATUS (0x0004)	Required to call the QueryServiceStatusEx function to ask the service control manager about the status of the service.<br></td></tr
><tr
id=sl_svn139_559

><td class="source">		# SERVICE_START (0x0010)	Required to call the StartService function to start the service.<br></td></tr
><tr
id=sl_svn139_560

><td class="source">		# SERVICE_STOP (0x0020)	Required to call the ControlService function to stop the service.<br></td></tr
><tr
id=sl_svn139_561

><td class="source">		# SERVICE_USER_DEFINED_CONTROL(0x0100)	Required to call the ControlService function to specify a user-defined control code.<br></td></tr
><tr
id=sl_svn139_562

><td class="source">		win32service: (<br></td></tr
><tr
id=sl_svn139_563

><td class="source">			# &quot;SERVICE_INTERROGATE&quot;,<br></td></tr
><tr
id=sl_svn139_564

><td class="source">			# &quot;SERVICE_QUERY_STATUS&quot;,<br></td></tr
><tr
id=sl_svn139_565

><td class="source">			# &quot;SERVICE_ENUMERATE_DEPENDENTS&quot;,<br></td></tr
><tr
id=sl_svn139_566

><td class="source">			&quot;SERVICE_ALL_ACCESS&quot;,<br></td></tr
><tr
id=sl_svn139_567

><td class="source">			&quot;SERVICE_CHANGE_CONFIG&quot;,<br></td></tr
><tr
id=sl_svn139_568

><td class="source">			&quot;SERVICE_PAUSE_CONTINUE&quot;,<br></td></tr
><tr
id=sl_svn139_569

><td class="source">			# &quot;SERVICE_QUERY_CONFIG&quot;,<br></td></tr
><tr
id=sl_svn139_570

><td class="source">			&quot;SERVICE_START&quot;,<br></td></tr
><tr
id=sl_svn139_571

><td class="source">			&quot;SERVICE_STOP&quot;,<br></td></tr
><tr
id=sl_svn139_572

><td class="source">			# &quot;SERVICE_USER_DEFINED_CONTROL&quot;, # TODO this is granted most of the time.  Double check that&#39;s not a bad thing.<br></td></tr
><tr
id=sl_svn139_573

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_574

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_575

><td class="source">}<br></td></tr
><tr
id=sl_svn139_576

><td class="source"><br></td></tr
><tr
id=sl_svn139_577

><td class="source">all_perms = {<br></td></tr
><tr
id=sl_svn139_578

><td class="source">	&#39;share&#39;: {<br></td></tr
><tr
id=sl_svn139_579

><td class="source">		ntsecuritycon: (<br></td></tr
><tr
id=sl_svn139_580

><td class="source">			&quot;FILE_READ_DATA&quot;, #<br></td></tr
><tr
id=sl_svn139_581

><td class="source">			&quot;FILE_WRITE_DATA&quot;,<br></td></tr
><tr
id=sl_svn139_582

><td class="source">			&quot;FILE_APPEND_DATA&quot;,<br></td></tr
><tr
id=sl_svn139_583

><td class="source">			&quot;FILE_READ_EA&quot;, #<br></td></tr
><tr
id=sl_svn139_584

><td class="source">			&quot;FILE_WRITE_EA&quot;,<br></td></tr
><tr
id=sl_svn139_585

><td class="source">			&quot;FILE_EXECUTE&quot;, #<br></td></tr
><tr
id=sl_svn139_586

><td class="source">			&quot;FILE_READ_ATTRIBUTES&quot;, #<br></td></tr
><tr
id=sl_svn139_587

><td class="source">			&quot;FILE_WRITE_ATTRIBUTES&quot;,<br></td></tr
><tr
id=sl_svn139_588

><td class="source">			&quot;DELETE&quot;,<br></td></tr
><tr
id=sl_svn139_589

><td class="source">			&quot;READ_CONTROL&quot;, #<br></td></tr
><tr
id=sl_svn139_590

><td class="source">			&quot;WRITE_DAC&quot;,<br></td></tr
><tr
id=sl_svn139_591

><td class="source">			&quot;WRITE_OWNER&quot;,<br></td></tr
><tr
id=sl_svn139_592

><td class="source">			&quot;SYNCHRONIZE&quot;, #<br></td></tr
><tr
id=sl_svn139_593

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_594

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_595

><td class="source">	&#39;file&#39;: {<br></td></tr
><tr
id=sl_svn139_596

><td class="source">		ntsecuritycon: (<br></td></tr
><tr
id=sl_svn139_597

><td class="source">			&quot;FILE_READ_DATA&quot;,<br></td></tr
><tr
id=sl_svn139_598

><td class="source">			&quot;FILE_WRITE_DATA&quot;,<br></td></tr
><tr
id=sl_svn139_599

><td class="source">			&quot;FILE_APPEND_DATA&quot;,<br></td></tr
><tr
id=sl_svn139_600

><td class="source">			&quot;FILE_READ_EA&quot;,<br></td></tr
><tr
id=sl_svn139_601

><td class="source">			&quot;FILE_WRITE_EA&quot;,<br></td></tr
><tr
id=sl_svn139_602

><td class="source">			&quot;FILE_EXECUTE&quot;,<br></td></tr
><tr
id=sl_svn139_603

><td class="source">			&quot;FILE_READ_ATTRIBUTES&quot;,<br></td></tr
><tr
id=sl_svn139_604

><td class="source">			&quot;FILE_WRITE_ATTRIBUTES&quot;,<br></td></tr
><tr
id=sl_svn139_605

><td class="source">			&quot;DELETE&quot;,<br></td></tr
><tr
id=sl_svn139_606

><td class="source">			&quot;READ_CONTROL&quot;,<br></td></tr
><tr
id=sl_svn139_607

><td class="source">			&quot;WRITE_DAC&quot;,<br></td></tr
><tr
id=sl_svn139_608

><td class="source">			&quot;WRITE_OWNER&quot;,<br></td></tr
><tr
id=sl_svn139_609

><td class="source">			&quot;SYNCHRONIZE&quot;,<br></td></tr
><tr
id=sl_svn139_610

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_611

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_612

><td class="source">	&#39;reg&#39;: {		<br></td></tr
><tr
id=sl_svn139_613

><td class="source">		_winreg: (<br></td></tr
><tr
id=sl_svn139_614

><td class="source">			&quot;KEY_ALL_ACCESS&quot;,<br></td></tr
><tr
id=sl_svn139_615

><td class="source">			&quot;KEY_CREATE_LINK&quot;,<br></td></tr
><tr
id=sl_svn139_616

><td class="source">			&quot;KEY_CREATE_SUB_KEY&quot;,<br></td></tr
><tr
id=sl_svn139_617

><td class="source">			&quot;KEY_ENUMERATE_SUB_KEYS&quot;,<br></td></tr
><tr
id=sl_svn139_618

><td class="source">			&quot;KEY_EXECUTE&quot;,<br></td></tr
><tr
id=sl_svn139_619

><td class="source">			&quot;KEY_NOTIFY&quot;,<br></td></tr
><tr
id=sl_svn139_620

><td class="source">			&quot;KEY_QUERY_VALUE&quot;,<br></td></tr
><tr
id=sl_svn139_621

><td class="source">			&quot;KEY_READ&quot;,<br></td></tr
><tr
id=sl_svn139_622

><td class="source">			&quot;KEY_SET_VALUE&quot;,<br></td></tr
><tr
id=sl_svn139_623

><td class="source">			&quot;KEY_WOW64_32KEY&quot;,<br></td></tr
><tr
id=sl_svn139_624

><td class="source">			&quot;KEY_WOW64_64KEY&quot;,<br></td></tr
><tr
id=sl_svn139_625

><td class="source">			&quot;KEY_WRITE&quot;,<br></td></tr
><tr
id=sl_svn139_626

><td class="source">		),<br></td></tr
><tr
id=sl_svn139_627

><td class="source">		ntsecuritycon: (<br></td></tr
><tr
id=sl_svn139_628

><td class="source">			&quot;DELETE&quot;,<br></td></tr
><tr
id=sl_svn139_629

><td class="source">			&quot;READ_CONTROL&quot;,<br></td></tr
><tr
id=sl_svn139_630

><td class="source">			&quot;WRITE_DAC&quot;,<br></td></tr
><tr
id=sl_svn139_631

><td class="source">			&quot;WRITE_OWNER&quot;,<br></td></tr
><tr
id=sl_svn139_632

><td class="source">			&quot;STANDARD_RIGHTS_REQUIRED&quot;,<br></td></tr
><tr
id=sl_svn139_633

><td class="source">			&quot;STANDARD_RIGHTS_WRITE&quot;,<br></td></tr
><tr
id=sl_svn139_634

><td class="source">			&quot;STANDARD_RIGHTS_READ&quot;,<br></td></tr
><tr
id=sl_svn139_635

><td class="source">			&quot;SYNCHRONIZE&quot;,<br></td></tr
><tr
id=sl_svn139_636

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_637

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_638

><td class="source">	&#39;directory&#39;: {<br></td></tr
><tr
id=sl_svn139_639

><td class="source">		ntsecuritycon: (<br></td></tr
><tr
id=sl_svn139_640

><td class="source">			&quot;FILE_LIST_DIRECTORY&quot;,<br></td></tr
><tr
id=sl_svn139_641

><td class="source">			&quot;FILE_ADD_FILE&quot;,<br></td></tr
><tr
id=sl_svn139_642

><td class="source">			&quot;FILE_ADD_SUBDIRECTORY&quot;,<br></td></tr
><tr
id=sl_svn139_643

><td class="source">			&quot;FILE_READ_EA&quot;,<br></td></tr
><tr
id=sl_svn139_644

><td class="source">			&quot;FILE_WRITE_EA&quot;,<br></td></tr
><tr
id=sl_svn139_645

><td class="source">			&quot;FILE_TRAVERSE&quot;,<br></td></tr
><tr
id=sl_svn139_646

><td class="source">			&quot;FILE_DELETE_CHILD&quot;,<br></td></tr
><tr
id=sl_svn139_647

><td class="source">			&quot;FILE_READ_ATTRIBUTES&quot;,<br></td></tr
><tr
id=sl_svn139_648

><td class="source">			&quot;FILE_WRITE_ATTRIBUTES&quot;,<br></td></tr
><tr
id=sl_svn139_649

><td class="source">			&quot;DELETE&quot;,<br></td></tr
><tr
id=sl_svn139_650

><td class="source">			&quot;READ_CONTROL&quot;,<br></td></tr
><tr
id=sl_svn139_651

><td class="source">			&quot;WRITE_DAC&quot;,<br></td></tr
><tr
id=sl_svn139_652

><td class="source">			&quot;WRITE_OWNER&quot;,<br></td></tr
><tr
id=sl_svn139_653

><td class="source">			&quot;SYNCHRONIZE&quot;,<br></td></tr
><tr
id=sl_svn139_654

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_655

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_656

><td class="source">	&#39;service_manager&#39;: {<br></td></tr
><tr
id=sl_svn139_657

><td class="source">		win32service: (<br></td></tr
><tr
id=sl_svn139_658

><td class="source">			&quot;SC_MANAGER_ALL_ACCESS&quot;,<br></td></tr
><tr
id=sl_svn139_659

><td class="source">			&quot;SC_MANAGER_CREATE_SERVICE&quot;,<br></td></tr
><tr
id=sl_svn139_660

><td class="source">			&quot;SC_MANAGER_CONNECT&quot;,<br></td></tr
><tr
id=sl_svn139_661

><td class="source">			&quot;SC_MANAGER_ENUMERATE_SERVICE&quot;,<br></td></tr
><tr
id=sl_svn139_662

><td class="source">			&quot;SC_MANAGER_LOCK&quot;,<br></td></tr
><tr
id=sl_svn139_663

><td class="source">			&quot;SC_MANAGER_MODIFY_BOOT_CONFIG&quot;,<br></td></tr
><tr
id=sl_svn139_664

><td class="source">			&quot;SC_MANAGER_QUERY_LOCK_STATUS&quot;,<br></td></tr
><tr
id=sl_svn139_665

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_666

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_667

><td class="source">	&#39;service&#39;: {<br></td></tr
><tr
id=sl_svn139_668

><td class="source">		win32service: (<br></td></tr
><tr
id=sl_svn139_669

><td class="source">			&quot;SERVICE_INTERROGATE&quot;,<br></td></tr
><tr
id=sl_svn139_670

><td class="source">			&quot;SERVICE_QUERY_STATUS&quot;,<br></td></tr
><tr
id=sl_svn139_671

><td class="source">			&quot;SERVICE_ENUMERATE_DEPENDENTS&quot;,<br></td></tr
><tr
id=sl_svn139_672

><td class="source">			&quot;SERVICE_ALL_ACCESS&quot;,<br></td></tr
><tr
id=sl_svn139_673

><td class="source">			&quot;SERVICE_CHANGE_CONFIG&quot;,<br></td></tr
><tr
id=sl_svn139_674

><td class="source">			&quot;SERVICE_PAUSE_CONTINUE&quot;,<br></td></tr
><tr
id=sl_svn139_675

><td class="source">			&quot;SERVICE_QUERY_CONFIG&quot;,<br></td></tr
><tr
id=sl_svn139_676

><td class="source">			&quot;SERVICE_START&quot;,<br></td></tr
><tr
id=sl_svn139_677

><td class="source">			&quot;SERVICE_STOP&quot;,<br></td></tr
><tr
id=sl_svn139_678

><td class="source">			&quot;SERVICE_USER_DEFINED_CONTROL&quot;, # TODO this is granted most of the time.  Double check that&#39;s not a bad thing.<br></td></tr
><tr
id=sl_svn139_679

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_680

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_681

><td class="source">	&#39;process&#39;: {<br></td></tr
><tr
id=sl_svn139_682

><td class="source">		win32con: (<br></td></tr
><tr
id=sl_svn139_683

><td class="source">			&quot;PROCESS_TERMINATE&quot;,<br></td></tr
><tr
id=sl_svn139_684

><td class="source">			&quot;PROCESS_CREATE_THREAD&quot;,<br></td></tr
><tr
id=sl_svn139_685

><td class="source">			&quot;PROCESS_VM_OPERATION&quot;,<br></td></tr
><tr
id=sl_svn139_686

><td class="source">			&quot;PROCESS_VM_READ&quot;,<br></td></tr
><tr
id=sl_svn139_687

><td class="source">			&quot;PROCESS_VM_WRITE&quot;,<br></td></tr
><tr
id=sl_svn139_688

><td class="source">			&quot;PROCESS_DUP_HANDLE&quot;,<br></td></tr
><tr
id=sl_svn139_689

><td class="source">			&quot;PROCESS_CREATE_PROCESS&quot;,<br></td></tr
><tr
id=sl_svn139_690

><td class="source">			&quot;PROCESS_SET_QUOTA&quot;,<br></td></tr
><tr
id=sl_svn139_691

><td class="source">			&quot;PROCESS_SET_INFORMATION&quot;,<br></td></tr
><tr
id=sl_svn139_692

><td class="source">			&quot;PROCESS_QUERY_INFORMATION&quot;,<br></td></tr
><tr
id=sl_svn139_693

><td class="source">			&quot;PROCESS_ALL_ACCESS&quot;<br></td></tr
><tr
id=sl_svn139_694

><td class="source">		),<br></td></tr
><tr
id=sl_svn139_695

><td class="source">		ntsecuritycon: (<br></td></tr
><tr
id=sl_svn139_696

><td class="source">			&quot;DELETE&quot;,<br></td></tr
><tr
id=sl_svn139_697

><td class="source">			&quot;READ_CONTROL&quot;,<br></td></tr
><tr
id=sl_svn139_698

><td class="source">			&quot;WRITE_DAC&quot;,<br></td></tr
><tr
id=sl_svn139_699

><td class="source">			&quot;WRITE_OWNER&quot;,<br></td></tr
><tr
id=sl_svn139_700

><td class="source">			&quot;SYNCHRONIZE&quot;,<br></td></tr
><tr
id=sl_svn139_701

><td class="source">			&quot;STANDARD_RIGHTS_REQUIRED&quot;,<br></td></tr
><tr
id=sl_svn139_702

><td class="source">			&quot;STANDARD_RIGHTS_READ&quot;,<br></td></tr
><tr
id=sl_svn139_703

><td class="source">			&quot;STANDARD_RIGHTS_WRITE&quot;,<br></td></tr
><tr
id=sl_svn139_704

><td class="source">			&quot;STANDARD_RIGHTS_EXECUTE&quot;,<br></td></tr
><tr
id=sl_svn139_705

><td class="source">			&quot;STANDARD_RIGHTS_ALL&quot;,<br></td></tr
><tr
id=sl_svn139_706

><td class="source">			&quot;SPECIFIC_RIGHTS_ALL&quot;,<br></td></tr
><tr
id=sl_svn139_707

><td class="source">			&quot;ACCESS_SYSTEM_SECURITY&quot;,<br></td></tr
><tr
id=sl_svn139_708

><td class="source">			&quot;MAXIMUM_ALLOWED&quot;,<br></td></tr
><tr
id=sl_svn139_709

><td class="source">			&quot;GENERIC_READ&quot;,<br></td></tr
><tr
id=sl_svn139_710

><td class="source">			&quot;GENERIC_WRITE&quot;,<br></td></tr
><tr
id=sl_svn139_711

><td class="source">			&quot;GENERIC_EXECUTE&quot;,<br></td></tr
><tr
id=sl_svn139_712

><td class="source">			&quot;GENERIC_ALL&quot;<br></td></tr
><tr
id=sl_svn139_713

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_714

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_715

><td class="source">	&#39;thread&#39;: {<br></td></tr
><tr
id=sl_svn139_716

><td class="source">		win32con: (<br></td></tr
><tr
id=sl_svn139_717

><td class="source">			&quot;THREAD_TERMINATE&quot;,<br></td></tr
><tr
id=sl_svn139_718

><td class="source">			&quot;THREAD_SUSPEND_RESUME&quot;,<br></td></tr
><tr
id=sl_svn139_719

><td class="source">			&quot;THREAD_GET_CONTEXT&quot;,<br></td></tr
><tr
id=sl_svn139_720

><td class="source">			&quot;THREAD_SET_CONTEXT&quot;,<br></td></tr
><tr
id=sl_svn139_721

><td class="source">			&quot;THREAD_SET_INFORMATION&quot;,<br></td></tr
><tr
id=sl_svn139_722

><td class="source">			&quot;THREAD_QUERY_INFORMATION&quot;,<br></td></tr
><tr
id=sl_svn139_723

><td class="source">			&quot;THREAD_SET_THREAD_TOKEN&quot;,<br></td></tr
><tr
id=sl_svn139_724

><td class="source">			&quot;THREAD_IMPERSONATE&quot;,<br></td></tr
><tr
id=sl_svn139_725

><td class="source">			&quot;THREAD_DIRECT_IMPERSONATION&quot;,<br></td></tr
><tr
id=sl_svn139_726

><td class="source">			&quot;THREAD_ALL_ACCESS&quot;,<br></td></tr
><tr
id=sl_svn139_727

><td class="source">			&quot;THREAD_QUERY_LIMITED_INFORMATION&quot;,<br></td></tr
><tr
id=sl_svn139_728

><td class="source">			&quot;THREAD_SET_LIMITED_INFORMATION&quot;<br></td></tr
><tr
id=sl_svn139_729

><td class="source">		),<br></td></tr
><tr
id=sl_svn139_730

><td class="source">		ntsecuritycon: (<br></td></tr
><tr
id=sl_svn139_731

><td class="source">			&quot;DELETE&quot;,<br></td></tr
><tr
id=sl_svn139_732

><td class="source">			&quot;READ_CONTROL&quot;,<br></td></tr
><tr
id=sl_svn139_733

><td class="source">			&quot;WRITE_DAC&quot;,<br></td></tr
><tr
id=sl_svn139_734

><td class="source">			&quot;WRITE_OWNER&quot;,<br></td></tr
><tr
id=sl_svn139_735

><td class="source">			&quot;SYNCHRONIZE&quot;,<br></td></tr
><tr
id=sl_svn139_736

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_737

><td class="source">	},<br></td></tr
><tr
id=sl_svn139_738

><td class="source">}<br></td></tr
><tr
id=sl_svn139_739

><td class="source"><br></td></tr
><tr
id=sl_svn139_740

><td class="source"># Used to store a data structure representing the issues we&#39;ve found<br></td></tr
><tr
id=sl_svn139_741

><td class="source"># We use this to generate the report<br></td></tr
><tr
id=sl_svn139_742

><td class="source">issues = {}<br></td></tr
><tr
id=sl_svn139_743

><td class="source"><br></td></tr
><tr
id=sl_svn139_744

><td class="source">issue_template = {<br></td></tr
><tr
id=sl_svn139_745

><td class="source">    &#39;WPC001&#39;: {<br></td></tr
><tr
id=sl_svn139_746

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions on Program Files&quot;,<br></td></tr
><tr
id=sl_svn139_747

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some of the programs in %ProgramFiles% and/or %ProgramFiles(x86)% could be changed by non-administrative users.<br></td></tr
><tr
id=sl_svn139_748

><td class="source"><br></td></tr
><tr
id=sl_svn139_749

><td class="source">This could allow certain users on the system to place malicious code into certain key directories, or to replace programs with malicious ones.  A malicious local user could use this technique to hijack the privileges of other local users, running commands with their privileges.<br></td></tr
><tr
id=sl_svn139_750

><td class="source">&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_751

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Programs run by multiple users should only be changable only by administrative users.  The directories containing these programs should only be changable only by administrators too.  Revoke write privileges for non-administrative users from the above programs and directories.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_752

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_753

><td class="source">          &#39;writable_progs&#39;: {<br></td></tr
><tr
id=sl_svn139_754

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_755

><td class="source">             &#39;preamble&#39;: &quot;The programs below can be modified by non-administrative users:&quot;,<br></td></tr
><tr
id=sl_svn139_756

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_757

><td class="source">          &#39;writable_dirs&#39;: {<br></td></tr
><tr
id=sl_svn139_758

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_759

><td class="source">             &#39;preamble&#39;: &quot;The directories below can be changed by non-administrative users:&quot;,<br></td></tr
><tr
id=sl_svn139_760

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_761

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_762

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_763

><td class="source">	<br></td></tr
><tr
id=sl_svn139_764

><td class="source">    &#39;WPC002&#39;: {<br></td></tr
><tr
id=sl_svn139_765

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions on Files and Directories in Path (OBSELETE ISSUE)&quot;,<br></td></tr
><tr
id=sl_svn139_766

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some of the programs and directories in the %PATH% variable could be changed by non-administrative users.<br></td></tr
><tr
id=sl_svn139_767

><td class="source"><br></td></tr
><tr
id=sl_svn139_768

><td class="source">This could allow certain users on the system to place malicious code into certain key directories, or to replace programs with malicious ones.  A malicious local user could use this technique to hijack the privileges of other local users, running commands with their privileges.<br></td></tr
><tr
id=sl_svn139_769

><td class="source">&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_770

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Programs run by multiple users should only be changable only by administrative users.  The directories containing these programs should only be changable only by administrators too.  Revoke write privileges for non-administrative users from the above programs and directories.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_771

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_772

><td class="source">          &#39;writable_progs&#39;: {<br></td></tr
><tr
id=sl_svn139_773

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_774

><td class="source">             &#39;preamble&#39;: &quot;The programs below are in the path of the user used to carry out this audit.  Each one can be changed by non-administrative users:&quot;,<br></td></tr
><tr
id=sl_svn139_775

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_776

><td class="source">          &#39;writable_dirs&#39;: {<br></td></tr
><tr
id=sl_svn139_777

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_778

><td class="source">             &#39;preamble&#39;: &quot;The directories below are in the path of the user used to carry out this audit.  Each one can be changed by non-administrative users:&quot;,<br></td></tr
><tr
id=sl_svn139_779

><td class="source">          }<br></td></tr
><tr
id=sl_svn139_780

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_781

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_782

><td class="source">	<br></td></tr
><tr
id=sl_svn139_783

><td class="source">    &#39;WPC003&#39;: {<br></td></tr
><tr
id=sl_svn139_784

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions In Windows Registry&quot;,<br></td></tr
><tr
id=sl_svn139_785

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some registry keys that hold the names of programs run by other users were checked and found to have insecure permissions.  It would be possible for non-administrative users to modify the registry to cause a different programs to be run.  This weakness could be abused by low-privileged users to run commands of their choosing with higher privileges.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_786

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Modify the permissions on the above registry keys to allow only administrators write access.  Revoke write access from low-privileged users.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_787

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_788

><td class="source">          &#39;writable_reg_paths&#39;: {<br></td></tr
><tr
id=sl_svn139_789

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_790

><td class="source">             &#39;preamble&#39;: &quot;The registry keys below could be changed by non-administrative users:&quot;,<br></td></tr
><tr
id=sl_svn139_791

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_792

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_793

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_794

><td class="source">	<br></td></tr
><tr
id=sl_svn139_795

><td class="source">    &#39;WPC004&#39;: {<br></td></tr
><tr
id=sl_svn139_796

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions On Windows Service Executables&quot;,<br></td></tr
><tr
id=sl_svn139_797

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some of the programs that are run when Windows Services start were found to have weak file permissions.  It is possible for non-administrative local users to replace some of the Windows Service executables with malicious programs.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_798

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Modify the permissions on the above programs to allow only administrators write access.  Revoke write access from low-privileged users.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_799

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_800

><td class="source">          &#39;writable_progs&#39;: {<br></td></tr
><tr
id=sl_svn139_801

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_802

><td class="source">             &#39;preamble&#39;: &quot;The programs below could be changed by non-administrative users:&quot;,<br></td></tr
><tr
id=sl_svn139_803

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_804

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_805

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_806

><td class="source">	<br></td></tr
><tr
id=sl_svn139_807

><td class="source">    &#39;WPC005&#39;: {<br></td></tr
><tr
id=sl_svn139_808

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions On Windows Service Registry Keys (NOT IMPLEMENTED YET)&quot;,<br></td></tr
><tr
id=sl_svn139_809

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some registry keys that hold the names of programs that are run when Windows Services start were found to have weak file permissions.  They could be changed by non-administrative users to cause malicious programs to be run instead of the intended Windows Service Executable.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_810

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Modify the permissions on the above programs to allow only administrators write access.  Revoke write access from low-privileged users.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_811

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_812

><td class="source">          &#39;writable_reg_paths&#39;: {<br></td></tr
><tr
id=sl_svn139_813

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_814

><td class="source">             &#39;preamble&#39;: &quot;The registry keys below could be changed by non-administrative users:&quot;,<br></td></tr
><tr
id=sl_svn139_815

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_816

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_817

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_818

><td class="source"><br></td></tr
><tr
id=sl_svn139_819

><td class="source">	&#39;WPC007&#39;: {<br></td></tr
><tr
id=sl_svn139_820

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions On Event Log File&quot;,<br></td></tr
><tr
id=sl_svn139_821

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some of the Event Log files could be changed by non-administrative users.  This may allow attackers to cover their tracks.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_822

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Modify the permissions on the above files to allow only administrators write access.  Revoke write access from low-privileged users.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_823

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_824

><td class="source">          &#39;writable_eventlog_file&#39;: {<br></td></tr
><tr
id=sl_svn139_825

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_826

><td class="source">             &#39;preamble&#39;: &quot;The files below could be changed by non-administrative users:&quot;,<br></td></tr
><tr
id=sl_svn139_827

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_828

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_829

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_830

><td class="source"><br></td></tr
><tr
id=sl_svn139_831

><td class="source">    &#39;WPC008&#39;: {<br></td></tr
><tr
id=sl_svn139_832

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions On Event Log DLL&quot;,<br></td></tr
><tr
id=sl_svn139_833

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some DLL files used by Event Viewer to display logs could be changed by non-administrative users.  It may be possible to replace these with a view to having code run when an administrative user next views log files.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_834

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Modify the permissions on the above DLLs to allow only administrators write access.  Revoke write access from low-privileged users.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_835

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_836

><td class="source">          &#39;writable_eventlog_dll&#39;: {<br></td></tr
><tr
id=sl_svn139_837

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_838

><td class="source">             &#39;preamble&#39;: &quot;The DLL files below could be changed by non-administrative users:&quot;,<br></td></tr
><tr
id=sl_svn139_839

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_840

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_841

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_842

><td class="source"><br></td></tr
><tr
id=sl_svn139_843

><td class="source">    &#39;WPC009&#39;: {<br></td></tr
><tr
id=sl_svn139_844

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions On Event Log Registry Key (NOT IMPLMENTED YET)&quot;,<br></td></tr
><tr
id=sl_svn139_845

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some registry keys that hold the names of DLLs used by Event Viewer and the location of Log Files are writable by non-administrative users.  It may be possible to maliciouly alter the registry to change the location of log files or run malicious code.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_846

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Modify the permissions on the above programs to allow only administrators write access.  Revoke write access from low-privileged users.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_847

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_848

><td class="source">          &#39;writable_eventlog_key&#39;: {<br></td></tr
><tr
id=sl_svn139_849

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_850

><td class="source">             &#39;preamble&#39;: &quot;The registry keys below could be changed by non-administrative users:&quot;,<br></td></tr
><tr
id=sl_svn139_851

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_852

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_853

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_854

><td class="source"><br></td></tr
><tr
id=sl_svn139_855

><td class="source">    &#39;WPC010&#39;: {<br></td></tr
><tr
id=sl_svn139_856

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions On Drive Root&quot;,<br></td></tr
><tr
id=sl_svn139_857

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some of the local drive roots allow non-administrative users to create files and folders.  This could allow malicious files to be placed in on the server in the hope that they&#39;ll allow a local user to escalate privileges (e.g. create program.exe which might get accidentally launched by another user).&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_858

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Modify the permissions on the drive roots to only allow administrators write access.  Revoke write access from low-privileged users.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_859

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_860

><td class="source">          &#39;writable_drive_root&#39;: {<br></td></tr
><tr
id=sl_svn139_861

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_862

><td class="source">             &#39;preamble&#39;: &quot;The following drives allow non-administrative users to write to their root directory:&quot;,<br></td></tr
><tr
id=sl_svn139_863

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_864

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_865

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_866

><td class="source"><br></td></tr
><tr
id=sl_svn139_867

><td class="source">    &#39;WPC011&#39;: {<br></td></tr
><tr
id=sl_svn139_868

><td class="source">       &#39;title&#39;: &quot;Insecure (Non-NTFS) File System Used&quot;,<br></td></tr
><tr
id=sl_svn139_869

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some local drives use Non-NTFS file systems.  These drive therefore don&#39;t allow secure file permissions to be used.  Any local user can change any data on these drives.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_870

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Use NTFS filesystems instead of FAT.  Ensure that strong file permissions are set - NTFS file permissions are insecure by default after FAT file systems are converted.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_871

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_872

><td class="source">          &#39;fat_fs_drives&#39;: {<br></td></tr
><tr
id=sl_svn139_873

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_874

><td class="source">             &#39;preamble&#39;: &quot;The following drives use Non-NTFS file systems:&quot;,<br></td></tr
><tr
id=sl_svn139_875

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_876

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_877

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_878

><td class="source"><br></td></tr
><tr
id=sl_svn139_879

><td class="source">    &#39;WPC012&#39;: {<br></td></tr
><tr
id=sl_svn139_880

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions On Windows Services&quot;,<br></td></tr
><tr
id=sl_svn139_881

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some of the Windows Services installed have weak permissions.  This could allow non-administrators to manipulate services to their own advantage.  The impact depends on the permissions granted, but can include starting services, stopping service or even reconfiguring them to run a different program.  This can lead to denial of service or even privilege escalation if the service is running as a user with more privilege than a malicious local user.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_882

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Review the permissions that have been granted to non-administrative users and revoke access where possible.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_883

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_884

><td class="source">          &#39;weak_service_perms&#39;: {<br></td></tr
><tr
id=sl_svn139_885

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_886

><td class="source">             &#39;preamble&#39;: &quot;Some Windows Services can be manipulated by non-administrator users:&quot;,<br></td></tr
><tr
id=sl_svn139_887

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_888

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_889

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_890

><td class="source">    &#39;WPC013&#39;: {<br></td></tr
><tr
id=sl_svn139_891

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions On Files / Directories In System PATH&quot;,<br></td></tr
><tr
id=sl_svn139_892

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some programs/directories in the system path have weak permissions.  TODO which user are affected by this issue?&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_893

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Review the permissions that have been granted to non-administrative users and revoke access where possible.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_894

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_895

><td class="source">          &#39;weak_perms_exe&#39;: {<br></td></tr
><tr
id=sl_svn139_896

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_897

><td class="source">             &#39;preamble&#39;: &quot;The following programs/DLLs in the system PATH can be manipulated by non-administrator users:&quot;,<br></td></tr
><tr
id=sl_svn139_898

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_899

><td class="source">          &#39;weak_perms_dir&#39;: {<br></td></tr
><tr
id=sl_svn139_900

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_901

><td class="source">             &#39;preamble&#39;: &quot;The following directories in the system PATH can be manipulated by non-administrator users:&quot;,<br></td></tr
><tr
id=sl_svn139_902

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_903

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_904

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_905

><td class="source">    &#39;WPC014&#39;: {<br></td></tr
><tr
id=sl_svn139_906

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions On Files / Directories In Current User&#39;s PATH&quot;,<br></td></tr
><tr
id=sl_svn139_907

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some programs/directories in the path of the user used to perform this audit have weak permissions.  TODO which user was used to perform this audit?&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_908

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Review the permissions that have been granted to non-administrative users and revoke access where possible.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_909

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_910

><td class="source">          &#39;weak_perms_exe&#39;: {<br></td></tr
><tr
id=sl_svn139_911

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_912

><td class="source">             &#39;preamble&#39;: &quot;The following programs/DLLs in current user&#39;s PATH can be manipulated by non-administrator users:&quot;,<br></td></tr
><tr
id=sl_svn139_913

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_914

><td class="source">          &#39;weak_perms_dir&#39;: {<br></td></tr
><tr
id=sl_svn139_915

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_916

><td class="source">             &#39;preamble&#39;: &quot;The following directories in the current user&#39;s PATH can be manipulated by non-administrator users:&quot;,<br></td></tr
><tr
id=sl_svn139_917

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_918

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_919

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_920

><td class="source">	<br></td></tr
><tr
id=sl_svn139_921

><td class="source">    &#39;WPC015&#39;: {<br></td></tr
><tr
id=sl_svn139_922

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions On Files / Directories In Users&#39; PATHs (NEED TO CHECK THIS WORKS)&quot;,<br></td></tr
><tr
id=sl_svn139_923

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some programs/directories in the paths of users on this system have weak permissions.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_924

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Review the permissions that have been granted to non-administrative users and revoke access where possible.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_925

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_926

><td class="source">          &#39;weak_perms_exe&#39;: {<br></td></tr
><tr
id=sl_svn139_927

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_928

><td class="source">             &#39;preamble&#39;: &quot;The following programs/DLLs in users&#39; PATHs can be manipulated by non-administrator users:&quot;,<br></td></tr
><tr
id=sl_svn139_929

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_930

><td class="source">          &#39;weak_perms_dir&#39;: {<br></td></tr
><tr
id=sl_svn139_931

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_932

><td class="source">             &#39;preamble&#39;: &quot;The following directories in users&#39; PATHs can be manipulated by non-administrator users:&quot;,<br></td></tr
><tr
id=sl_svn139_933

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_934

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_935

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_936

><td class="source">    &#39;WPC016&#39;: {<br></td></tr
><tr
id=sl_svn139_937

><td class="source">       &#39;title&#39;: &quot;Insecure Permissions On Running Programs&quot;,<br></td></tr
><tr
id=sl_svn139_938

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;Some programs running at the time of the audit have weak file permissions.  The corresponding programs could be altered by non-administrator users.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_939

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Review the permissions that have been granted to non-administrative users and revoke access where possible.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_940

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_941

><td class="source">          &#39;weak_perms_exes&#39;: {<br></td></tr
><tr
id=sl_svn139_942

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_943

><td class="source">             &#39;preamble&#39;: &quot;The following programs were running at the time of the audit, but could be changed on-disk by non-administrator users:&quot;,<br></td></tr
><tr
id=sl_svn139_944

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_945

><td class="source">          &#39;weak_perms_dlls&#39;: {<br></td></tr
><tr
id=sl_svn139_946

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_947

><td class="source">             &#39;preamble&#39;: &quot;The following DLLs are used by program which were running at the time of the audit.  These DLLs can be changed on-disk by non-administrator users:&quot;,<br></td></tr
><tr
id=sl_svn139_948

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_949

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_950

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_951

><td class="source">    &#39;WPC017&#39;: {<br></td></tr
><tr
id=sl_svn139_952

><td class="source">       &#39;title&#39;: &quot;Shares Accessible By Non-Admin Users&quot;,<br></td></tr
><tr
id=sl_svn139_953

><td class="source">       &#39;description&#39;: &#39;&#39;&#39;The share-level permissions on some Windows file shares allows access by non-administrative users.  This can often be desirable, in which case this issue can be ignored.  However, sometimes it can allow data to be stolen or programs to be malciously modified.  NB: Setting strong NTFS permissions can sometimes mean that data which seems to be exposed on a share actually isn&#39;t accessible.&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_954

><td class="source">       &#39;recommendation&#39;: &#39;&#39;&#39;Review the share-level permissions that have been granted to non-administrative users and revoke access where possible.  Share-level permissions can be viewed in Windows Explorer: Right-click folder | Sharing and Security | &quot;Sharing&quot; tab | &quot;Permissions&quot; button (for XP - other OSs may vary slightly).&#39;&#39;&#39;,<br></td></tr
><tr
id=sl_svn139_955

><td class="source">       &#39;supporting_data&#39;: {<br></td></tr
><tr
id=sl_svn139_956

><td class="source">          &#39;non_admin_shares&#39;: {<br></td></tr
><tr
id=sl_svn139_957

><td class="source">             &#39;section&#39;: &quot;description&quot;,<br></td></tr
><tr
id=sl_svn139_958

><td class="source">             &#39;preamble&#39;: &quot;The following shares are accessible by non-administrative users:&quot;,<br></td></tr
><tr
id=sl_svn139_959

><td class="source">          },<br></td></tr
><tr
id=sl_svn139_960

><td class="source">       }<br></td></tr
><tr
id=sl_svn139_961

><td class="source">    },<br></td></tr
><tr
id=sl_svn139_962

><td class="source">}<br></td></tr
><tr
id=sl_svn139_963

><td class="source"><br></td></tr
><tr
id=sl_svn139_964

><td class="source">issue_template_html = &#39;&#39;&#39;<br></td></tr
><tr
id=sl_svn139_965

><td class="source">&lt;h3&gt;REPLACE_TITLE&lt;/h3&gt;<br></td></tr
><tr
id=sl_svn139_966

><td class="source"><br></td></tr
><tr
id=sl_svn139_967

><td class="source">&lt;table&gt;<br></td></tr
><tr
id=sl_svn139_968

><td class="source">&lt;tr&gt;<br></td></tr
><tr
id=sl_svn139_969

><td class="source">&lt;td&gt;<br></td></tr
><tr
id=sl_svn139_970

><td class="source">&lt;b&gt;Description&lt;/b&gt;<br></td></tr
><tr
id=sl_svn139_971

><td class="source">&lt;/td&gt;<br></td></tr
><tr
id=sl_svn139_972

><td class="source">&lt;td&gt;<br></td></tr
><tr
id=sl_svn139_973

><td class="source">REPLACE_DESCRIPTION<br></td></tr
><tr
id=sl_svn139_974

><td class="source">REPLACE_DESCRIPTION_DATA<br></td></tr
><tr
id=sl_svn139_975

><td class="source">&lt;/td&gt;<br></td></tr
><tr
id=sl_svn139_976

><td class="source">&lt;/tr&gt;<br></td></tr
><tr
id=sl_svn139_977

><td class="source"><br></td></tr
><tr
id=sl_svn139_978

><td class="source">&lt;tr&gt;<br></td></tr
><tr
id=sl_svn139_979

><td class="source">&lt;td&gt;<br></td></tr
><tr
id=sl_svn139_980

><td class="source">&lt;b&gt;Recommendation&lt;/b&gt;<br></td></tr
><tr
id=sl_svn139_981

><td class="source">&lt;/td&gt;<br></td></tr
><tr
id=sl_svn139_982

><td class="source">&lt;td&gt;<br></td></tr
><tr
id=sl_svn139_983

><td class="source">REPLACE_RECOMMENDATION<br></td></tr
><tr
id=sl_svn139_984

><td class="source">REPLACE_RECOMMENDATION_DATA<br></td></tr
><tr
id=sl_svn139_985

><td class="source">&lt;/td&gt;<br></td></tr
><tr
id=sl_svn139_986

><td class="source">&lt;/tr&gt;<br></td></tr
><tr
id=sl_svn139_987

><td class="source">&lt;/table&gt;<br></td></tr
><tr
id=sl_svn139_988

><td class="source">&#39;&#39;&#39;<br></td></tr
><tr
id=sl_svn139_989

><td class="source"><br></td></tr
><tr
id=sl_svn139_990

><td class="source">issue_list_html =&#39;&#39;&#39;<br></td></tr
><tr
id=sl_svn139_991

><td class="source">REPLACE_PREAMBLE<br></td></tr
><tr
id=sl_svn139_992

><td class="source">&lt;ul&gt;<br></td></tr
><tr
id=sl_svn139_993

><td class="source">REPLACE_ITEM<br></td></tr
><tr
id=sl_svn139_994

><td class="source">&lt;/ul&gt;<br></td></tr
><tr
id=sl_svn139_995

><td class="source">&#39;&#39;&#39;<br></td></tr
><tr
id=sl_svn139_996

><td class="source"><br></td></tr
><tr
id=sl_svn139_997

><td class="source"># TODO nice looking css, internal links, risk ratings<br></td></tr
><tr
id=sl_svn139_998

><td class="source"># TODO record group members for audit user, separate date and time; os and sp<br></td></tr
><tr
id=sl_svn139_999

><td class="source">overview_template_html = &#39;&#39;&#39;<br></td></tr
><tr
id=sl_svn139_1000

><td class="source">&lt;html&gt;<br></td></tr
><tr
id=sl_svn139_1001

><td class="source">&lt;head&gt;<br></td></tr
><tr
id=sl_svn139_1002

><td class="source">&lt;style type=&quot;text/css&quot;&gt;<br></td></tr
><tr
id=sl_svn139_1003

><td class="source">body {color:black}<br></td></tr
><tr
id=sl_svn139_1004

><td class="source">td<br></td></tr
><tr
id=sl_svn139_1005

><td class="source">{<br></td></tr
><tr
id=sl_svn139_1006

><td class="source">vertical-align:top;<br></td></tr
><tr
id=sl_svn139_1007

><td class="source">}<br></td></tr
><tr
id=sl_svn139_1008

><td class="source">h1 {font-size: 300%; text-align:center}<br></td></tr
><tr
id=sl_svn139_1009

><td class="source">h2 {font-size: 200%; margin-top: 25px; margin-bottom: 0px; padding: 5px; background-color: #CCCCCC;}<br></td></tr
><tr
id=sl_svn139_1010

><td class="source">h3 {font-size: 150%; font-weight: normal; padding: 5px; background-color: #EEEEEE; margin-top: 10px;}<br></td></tr
><tr
id=sl_svn139_1011

><td class="source">#frontpage {height: 270px; background-color: #F3F3F3;}<br></td></tr
><tr
id=sl_svn139_1012

><td class="source">p.ex {color:rgb(0,0,255)}<br></td></tr
><tr
id=sl_svn139_1013

><td class="source"><br></td></tr
><tr
id=sl_svn139_1014

><td class="source">#customers<br></td></tr
><tr
id=sl_svn139_1015

><td class="source">{<br></td></tr
><tr
id=sl_svn139_1016

><td class="source">font-family:&quot;Trebuchet MS&quot;, Arial, Helvetica, sans-serif;<br></td></tr
><tr
id=sl_svn139_1017

><td class="source">/* width:100%; */<br></td></tr
><tr
id=sl_svn139_1018

><td class="source">padding:10px 0px 0px 0px;<br></td></tr
><tr
id=sl_svn139_1019

><td class="source">border-collapse:collapse;<br></td></tr
><tr
id=sl_svn139_1020

><td class="source">}<br></td></tr
><tr
id=sl_svn139_1021

><td class="source">#customers td, #customers th <br></td></tr
><tr
id=sl_svn139_1022

><td class="source">{<br></td></tr
><tr
id=sl_svn139_1023

><td class="source">font-size:1em;<br></td></tr
><tr
id=sl_svn139_1024

><td class="source">border:1px solid #989898;<br></td></tr
><tr
id=sl_svn139_1025

><td class="source">padding:3px 7px 2px 7px;<br></td></tr
><tr
id=sl_svn139_1026

><td class="source">}<br></td></tr
><tr
id=sl_svn139_1027

><td class="source">#customers th <br></td></tr
><tr
id=sl_svn139_1028

><td class="source">{<br></td></tr
><tr
id=sl_svn139_1029

><td class="source">font-size:1.1em;<br></td></tr
><tr
id=sl_svn139_1030

><td class="source">text-align:left;<br></td></tr
><tr
id=sl_svn139_1031

><td class="source">padding-top:5px;<br></td></tr
><tr
id=sl_svn139_1032

><td class="source">padding-bottom:4px;<br></td></tr
><tr
id=sl_svn139_1033

><td class="source">background-color:#A7C942;<br></td></tr
><tr
id=sl_svn139_1034

><td class="source">color:#ffffff;<br></td></tr
><tr
id=sl_svn139_1035

><td class="source">}<br></td></tr
><tr
id=sl_svn139_1036

><td class="source">#customers tr.alt td <br></td></tr
><tr
id=sl_svn139_1037

><td class="source">{<br></td></tr
><tr
id=sl_svn139_1038

><td class="source">color:#000000;<br></td></tr
><tr
id=sl_svn139_1039

><td class="source">background-color:#EAF2D3;<br></td></tr
><tr
id=sl_svn139_1040

><td class="source">}<br></td></tr
><tr
id=sl_svn139_1041

><td class="source">&lt;/style&gt;<br></td></tr
><tr
id=sl_svn139_1042

><td class="source">&lt;/head&gt;<br></td></tr
><tr
id=sl_svn139_1043

><td class="source">&lt;div id=&quot;frontpage&quot;&gt;<br></td></tr
><tr
id=sl_svn139_1044

><td class="source">&lt;h1&gt;&lt;p&gt;windows-privesc-check&lt;/p&gt; &lt;p&gt;Audit of Host: &lt;/p&gt;&lt;p&gt;REPLACE_HOSTNAME&lt;/p&gt;&lt;/h1&gt;<br></td></tr
><tr
id=sl_svn139_1045

><td class="source">&lt;/div&gt;<br></td></tr
><tr
id=sl_svn139_1046

><td class="source"><br></td></tr
><tr
id=sl_svn139_1047

><td class="source">&lt;h2&gt;Contents&lt;/h2&gt;<br></td></tr
><tr
id=sl_svn139_1048

><td class="source">REPLACE_CONTENTS<br></td></tr
><tr
id=sl_svn139_1049

><td class="source">&lt;h2&gt;Information about this Audit&lt;/h2&gt;<br></td></tr
><tr
id=sl_svn139_1050

><td class="source">&lt;p&gt;This report was generated on REPLACE_DATETIME by vREPLACE_VERSION of &lt;a href=&quot;http://pentestmonkey.net/windows-privesc-check&quot;&gt;windows-privesc-check&lt;/a&gt;.&lt;/p&gt;<br></td></tr
><tr
id=sl_svn139_1051

><td class="source"><br></td></tr
><tr
id=sl_svn139_1052

><td class="source">&lt;p&gt;The audit was run as the user REPLACE_AUDIT_USER.&lt;/p&gt;<br></td></tr
><tr
id=sl_svn139_1053

><td class="source"><br></td></tr
><tr
id=sl_svn139_1054

><td class="source">&lt;p&gt;The following table provides information about this audit:&lt;/p&gt;<br></td></tr
><tr
id=sl_svn139_1055

><td class="source"><br></td></tr
><tr
id=sl_svn139_1056

><td class="source">&lt;table id=&quot;customers&quot; border=&quot;1&quot;&gt;<br></td></tr
><tr
id=sl_svn139_1057

><td class="source">&lt;tr&gt;<br></td></tr
><tr
id=sl_svn139_1058

><td class="source">&lt;td&gt;Hostname&lt;/td&gt;<br></td></tr
><tr
id=sl_svn139_1059

><td class="source">&lt;td&gt;REPLACE_HOSTNAME&lt;/td&gt;<br></td></tr
><tr
id=sl_svn139_1060

><td class="source">&lt;/tr&gt;<br></td></tr
><tr
id=sl_svn139_1061

><td class="source"><br></td></tr
><tr
id=sl_svn139_1062

><td class="source">&lt;tr class=&quot;alt&quot;&gt;<br></td></tr
><tr
id=sl_svn139_1063

><td class="source">&lt;td&gt;Domain/Workgroup&lt;/td&gt;<br></td></tr
><tr
id=sl_svn139_1064

><td class="source">&lt;td&gt;REPLACE_DOMWKG&lt;/td&gt;<br></td></tr
><tr
id=sl_svn139_1065

><td class="source">&lt;/tr&gt;<br></td></tr
><tr
id=sl_svn139_1066

><td class="source"><br></td></tr
><tr
id=sl_svn139_1067

><td class="source">&lt;tr&gt;<br></td></tr
><tr
id=sl_svn139_1068

><td class="source">&lt;td&gt;Operating System&lt;/td&gt;<br></td></tr
><tr
id=sl_svn139_1069

><td class="source">&lt;td&gt;REPLACE_OS&lt;/td&gt;<br></td></tr
><tr
id=sl_svn139_1070

><td class="source">&lt;/tr&gt;<br></td></tr
><tr
id=sl_svn139_1071

><td class="source"><br></td></tr
><tr
id=sl_svn139_1072

><td class="source">&lt;tr class=&quot;alt&quot;&gt;<br></td></tr
><tr
id=sl_svn139_1073

><td class="source">&lt;td&gt;IP Addresses&lt;/td&gt;<br></td></tr
><tr
id=sl_svn139_1074

><td class="source">&lt;td&gt;&lt;ul&gt;REPLACE_IPS&lt;/ul&gt;&lt;/td&gt;<br></td></tr
><tr
id=sl_svn139_1075

><td class="source">&lt;/tr&gt;<br></td></tr
><tr
id=sl_svn139_1076

><td class="source"><br></td></tr
><tr
id=sl_svn139_1077

><td class="source">&lt;/table&gt; <br></td></tr
><tr
id=sl_svn139_1078

><td class="source">&lt;h2&gt;Escalation Vectors&lt;/h2&gt;<br></td></tr
><tr
id=sl_svn139_1079

><td class="source">REPLACE_ISSUES<br></td></tr
><tr
id=sl_svn139_1080

><td class="source"><br></td></tr
><tr
id=sl_svn139_1081

><td class="source">&lt;h2&gt;Scan Parameters&lt;/h2&gt;<br></td></tr
><tr
id=sl_svn139_1082

><td class="source">For the purposes of the audit the following users were considered to be trusted.  Any privileges assigned to them have not been considered as potential attack vectors:<br></td></tr
><tr
id=sl_svn139_1083

><td class="source">&lt;ul&gt;<br></td></tr
><tr
id=sl_svn139_1084

><td class="source">REPLACE_TRUSTED_USERS<br></td></tr
><tr
id=sl_svn139_1085

><td class="source">&lt;/ul&gt;<br></td></tr
><tr
id=sl_svn139_1086

><td class="source"><br></td></tr
><tr
id=sl_svn139_1087

><td class="source">Additionally members of the following groups were considered trusted:<br></td></tr
><tr
id=sl_svn139_1088

><td class="source">&lt;ul&gt;<br></td></tr
><tr
id=sl_svn139_1089

><td class="source">REPLACE_TRUSTED_GROUPS<br></td></tr
><tr
id=sl_svn139_1090

><td class="source">&lt;/ul&gt;<br></td></tr
><tr
id=sl_svn139_1091

><td class="source"><br></td></tr
><tr
id=sl_svn139_1092

><td class="source">The following file/directory/registry permissions were considered to be potentially dangerous.  This audit exclusively searched for instances of these permissions:<br></td></tr
><tr
id=sl_svn139_1093

><td class="source">&lt;ul&gt;<br></td></tr
><tr
id=sl_svn139_1094

><td class="source">REPLACE_DANGEROUS_PERMS<br></td></tr
><tr
id=sl_svn139_1095

><td class="source">&lt;/ul&gt;<br></td></tr
><tr
id=sl_svn139_1096

><td class="source">&lt;/html&gt;<br></td></tr
><tr
id=sl_svn139_1097

><td class="source">&#39;&#39;&#39;<br></td></tr
><tr
id=sl_svn139_1098

><td class="source"><br></td></tr
><tr
id=sl_svn139_1099

><td class="source">def usage():<br></td></tr
><tr
id=sl_svn139_1100

><td class="source">	print &quot;Usage: windows-privesc-check [options] checks&quot;<br></td></tr
><tr
id=sl_svn139_1101

><td class="source">	print &quot;&quot;<br></td></tr
><tr
id=sl_svn139_1102

><td class="source">	print &quot;checks must be at least one of:&quot;<br></td></tr
><tr
id=sl_svn139_1103

><td class="source">	print &quot;  -a|--all_checks        Run all security checks (see below)&quot;<br></td></tr
><tr
id=sl_svn139_1104

><td class="source">	print &quot;  -r|--registry_checks   Check RunOnce and other critical keys&quot;<br></td></tr
><tr
id=sl_svn139_1105

><td class="source">	print &quot;  -t|--path_checks       Check %PATH% for insecure permissions&quot;<br></td></tr
><tr
id=sl_svn139_1106

><td class="source">	print &quot;  -S|--service_checks    Check Windows services for insecure permissions&quot;<br></td></tr
><tr
id=sl_svn139_1107

><td class="source">	print &quot;  -d|--drive_checks      Check for FAT filesystems and weak perms in root dir&quot;<br></td></tr
><tr
id=sl_svn139_1108

><td class="source">	print &quot;  -E|--eventlog_checks   Check Event Logs for insecure permissions&quot;<br></td></tr
><tr
id=sl_svn139_1109

><td class="source">	print &quot;  -F|--progfiles_checks  Check Program Files directories for insecure perms&quot;<br></td></tr
><tr
id=sl_svn139_1110

><td class="source">	print &quot;  -R|--process_checks    Check Running Processes for insecure permissions&quot;<br></td></tr
><tr
id=sl_svn139_1111

><td class="source">	print &quot;  -H|--share_checks      Check shares for insecure permissions&quot;<br></td></tr
><tr
id=sl_svn139_1112

><td class="source">	#print &quot;  -T|--patch_checks      Check some important patches&quot;<br></td></tr
><tr
id=sl_svn139_1113

><td class="source">	print &quot;  -U|--user_groups       Dump users, groups and privileges (no HTML yet)&quot;<br></td></tr
><tr
id=sl_svn139_1114

><td class="source">	print &quot;  -A|--admin_users       Dump admin users / high priv users (no HTML yet)&quot;<br></td></tr
><tr
id=sl_svn139_1115

><td class="source">	print &quot;  -O|--processes         Dump process info (no HTML yet)&quot;<br></td></tr
><tr
id=sl_svn139_1116

><td class="source">	print &quot;  -P|--passpol           Dump password policy (no HTML yet)&quot;<br></td></tr
><tr
id=sl_svn139_1117

><td class="source">	print &quot;  -i|--host_info         Dump host info - OS, domain controller, ... (no HTML yet)&quot;<br></td></tr
><tr
id=sl_svn139_1118

><td class="source">	print &quot;  -e|--services          Dump service info (no HTML yet)&quot;<br></td></tr
><tr
id=sl_svn139_1119

><td class="source"># TODO options to flag a user/group as trusted<br></td></tr
><tr
id=sl_svn139_1120

><td class="source">	print &quot;&quot;<br></td></tr
><tr
id=sl_svn139_1121

><td class="source">	print &quot;options are:&quot;<br></td></tr
><tr
id=sl_svn139_1122

><td class="source">	print &quot;  -h|--help              This help message&quot;<br></td></tr
><tr
id=sl_svn139_1123

><td class="source">	print &quot;  -w|--write_perms_only  Only list write perms (dump opts only)&quot;<br></td></tr
><tr
id=sl_svn139_1124

><td class="source">	print &quot;  -I|--ignore_trusted    Ignore trusted users, empty groups (dump opts only)&quot;<br></td></tr
><tr
id=sl_svn139_1125

><td class="source">	print &quot;  -W|--owner_info        Owner, Group info (dump opts only)&quot;<br></td></tr
><tr
id=sl_svn139_1126

><td class="source">	print &quot;  -v|--verbose           More detail output (use with -U)&quot;<br></td></tr
><tr
id=sl_svn139_1127

><td class="source">	print &quot;  -o|--report_file file  Report filename.  Default privesc-report-[host].html&quot;<br></td></tr
><tr
id=sl_svn139_1128

><td class="source">	print &quot;  -s|--server host       Remote server name.  Only works with -u!&quot;<br></td></tr
><tr
id=sl_svn139_1129

><td class="source">	print &quot;  -u|--username arg      Remote username.  Only works with -u!&quot;<br></td></tr
><tr
id=sl_svn139_1130

><td class="source">	print &quot;  -p|--password arg      Remote password.  Only works with -u!&quot;<br></td></tr
><tr
id=sl_svn139_1131

><td class="source">	print &quot;  -d|--domain arg        Remote domain.  Only works with -u!&quot;<br></td></tr
><tr
id=sl_svn139_1132

><td class="source">	print &quot;&quot;<br></td></tr
><tr
id=sl_svn139_1133

><td class="source">	sys.exit(0)<br></td></tr
><tr
id=sl_svn139_1134

><td class="source"><br></td></tr
><tr
id=sl_svn139_1135

><td class="source">#<br></td></tr
><tr
id=sl_svn139_1136

><td class="source"># Reporting functions<br></td></tr
><tr
id=sl_svn139_1137

><td class="source">#<br></td></tr
><tr
id=sl_svn139_1138

><td class="source"><br></td></tr
><tr
id=sl_svn139_1139

><td class="source">def format_issues(format, issue_template, issue_data):<br></td></tr
><tr
id=sl_svn139_1140

><td class="source">	report = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_1141

><td class="source">	toc = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_1142

><td class="source">	overview = overview_template_html<br></td></tr
><tr
id=sl_svn139_1143

><td class="source">	overview = overview.replace(&#39;REPLACE_HOSTNAME&#39;, audit_data[&#39;hostname&#39;])<br></td></tr
><tr
id=sl_svn139_1144

><td class="source">	overview = overview.replace(&#39;REPLACE_DOMWKG&#39;, audit_data[&#39;domwkg&#39;])<br></td></tr
><tr
id=sl_svn139_1145

><td class="source">	# overview = overview.replace(&#39;REPLACE_IPS&#39;, &quot;&lt;li&gt;&quot; + &quot;&lt;/li&gt;&lt;li&gt;&quot;.join(audit_data[&#39;ips&#39;]) + &quot;&lt;/li&gt;&quot;)<br></td></tr
><tr
id=sl_svn139_1146

><td class="source">	for item in audit_data[&#39;ips&#39;]:<br></td></tr
><tr
id=sl_svn139_1147

><td class="source">		overview = overview.replace(&#39;REPLACE_IPS&#39;, list_item(&quot;REPLACE_IPS&quot;, item))<br></td></tr
><tr
id=sl_svn139_1148

><td class="source">	overview = overview.replace(&#39;REPLACE_IPS&#39;, &#39;&#39;)<br></td></tr
><tr
id=sl_svn139_1149

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1150

><td class="source">	overview = overview.replace(&#39;REPLACE_OS&#39;, audit_data[&#39;os_name&#39;] + &quot; (&quot; + audit_data[&#39;os_version&#39;] + &quot;)&quot;)<br></td></tr
><tr
id=sl_svn139_1151

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1152

><td class="source">	overview = overview.replace(&#39;REPLACE_VERSION&#39;, audit_data[&#39;version&#39;])<br></td></tr
><tr
id=sl_svn139_1153

><td class="source">	overview = overview.replace(&#39;REPLACE_DATETIME&#39;, audit_data[&#39;datetime&#39;])<br></td></tr
><tr
id=sl_svn139_1154

><td class="source">	overview = overview.replace(&#39;REPLACE_AUDIT_USER&#39;, audit_data[&#39;audit_user&#39;])<br></td></tr
><tr
id=sl_svn139_1155

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1156

><td class="source">	for item in audit_data[&#39;trusted_users&#39;]:<br></td></tr
><tr
id=sl_svn139_1157

><td class="source">		overview = overview.replace(&#39;REPLACE_TRUSTED_USERS&#39;, list_item(&quot;REPLACE_TRUSTED_USERS&quot;, item))<br></td></tr
><tr
id=sl_svn139_1158

><td class="source">	overview = overview.replace(&#39;REPLACE_TRUSTED_USERS&#39;, &#39;&#39;)<br></td></tr
><tr
id=sl_svn139_1159

><td class="source">				<br></td></tr
><tr
id=sl_svn139_1160

><td class="source">	for item in audit_data[&#39;trusted_groups&#39;]:<br></td></tr
><tr
id=sl_svn139_1161

><td class="source">		overview = overview.replace(&#39;REPLACE_TRUSTED_GROUPS&#39;, list_item(&quot;REPLACE_TRUSTED_GROUPS&quot;, item))<br></td></tr
><tr
id=sl_svn139_1162

><td class="source">	overview = overview.replace(&#39;REPLACE_TRUSTED_GROUPS&#39;, &#39;&#39;)<br></td></tr
><tr
id=sl_svn139_1163

><td class="source"><br></td></tr
><tr
id=sl_svn139_1164

><td class="source">	permlist = &#39;&#39;<br></td></tr
><tr
id=sl_svn139_1165

><td class="source">	for permtype in dangerous_perms_write.keys():<br></td></tr
><tr
id=sl_svn139_1166

><td class="source">		permlist += &quot;Permission type &#39;&quot; + permtype + &quot;&#39;&lt;p&gt;&quot;<br></td></tr
><tr
id=sl_svn139_1167

><td class="source">		permlist += &quot;&lt;ul&gt;&quot;<br></td></tr
><tr
id=sl_svn139_1168

><td class="source">		for location in dangerous_perms_write[permtype].keys():<br></td></tr
><tr
id=sl_svn139_1169

><td class="source">			for item in dangerous_perms_write[permtype][location]:<br></td></tr
><tr
id=sl_svn139_1170

><td class="source">				permlist += &quot;\t&lt;li&gt;&quot; + item + &quot;&lt;/li&gt;&quot;<br></td></tr
><tr
id=sl_svn139_1171

><td class="source">		permlist += &quot;&lt;/ul&gt;&quot;<br></td></tr
><tr
id=sl_svn139_1172

><td class="source">				<br></td></tr
><tr
id=sl_svn139_1173

><td class="source">	#for item in audit_data[&#39;dangerous_privs&#39;]:<br></td></tr
><tr
id=sl_svn139_1174

><td class="source">	#	overview = overview.replace(&#39;REPLACE_DANGEROUS_PERM&#39;, list_item(&quot;REPLACE_DANGEROUS_PERM&quot;, item))<br></td></tr
><tr
id=sl_svn139_1175

><td class="source">	#overview = overview.replace(&#39;REPLACE_DANGEROUS_PERM&#39;, &#39;&#39;)<br></td></tr
><tr
id=sl_svn139_1176

><td class="source">	overview = overview.replace(&#39;REPLACE_DANGEROUS_PERMS&#39;, permlist)<br></td></tr
><tr
id=sl_svn139_1177

><td class="source"><br></td></tr
><tr
id=sl_svn139_1178

><td class="source">	for item in audit_data[&#39;ips&#39;]:<br></td></tr
><tr
id=sl_svn139_1179

><td class="source">		overview = overview.replace(&#39;REPLACE_IP&#39;, list_item(&quot;REPLACE_IPS&quot;, item))<br></td></tr
><tr
id=sl_svn139_1180

><td class="source">	overview = overview.replace(&#39;REPLACE_IP&#39;, &#39;&#39;)<br></td></tr
><tr
id=sl_svn139_1181

><td class="source"><br></td></tr
><tr
id=sl_svn139_1182

><td class="source">	for issue_no in issue_data:<br></td></tr
><tr
id=sl_svn139_1183

><td class="source">		# print &quot;[V] Processing issue issue_no\n&quot;<br></td></tr
><tr
id=sl_svn139_1184

><td class="source">		report = report + format_issue(format, issue_no, issue_data, issue_template)<br></td></tr
><tr
id=sl_svn139_1185

><td class="source">		toc = toc + &#39;&lt;a href=&quot;#&#39; + issue_template[issue_no][&#39;title&#39;] + &#39;&quot;&gt;&#39; + issue_template[issue_no][&#39;title&#39;] + &quot;&lt;/a&gt;&lt;p&gt;&quot;<br></td></tr
><tr
id=sl_svn139_1186

><td class="source"><br></td></tr
><tr
id=sl_svn139_1187

><td class="source">	if report:<br></td></tr
><tr
id=sl_svn139_1188

><td class="source">		overview = overview.replace(&#39;REPLACE_ISSUES&#39;, report)<br></td></tr
><tr
id=sl_svn139_1189

><td class="source">		overview = overview.replace(&#39;REPLACE_CONTENTS&#39;, toc)<br></td></tr
><tr
id=sl_svn139_1190

><td class="source">	else:<br></td></tr
><tr
id=sl_svn139_1191

><td class="source">		overview = overview.replace(&#39;REPLACE_ISSUES&#39;, &quot;No issues found&quot;)<br></td></tr
><tr
id=sl_svn139_1192

><td class="source">		overview = overview.replace(&#39;REPLACE_CONTENTS&#39;, &quot;No issues found&quot;)<br></td></tr
><tr
id=sl_svn139_1193

><td class="source"><br></td></tr
><tr
id=sl_svn139_1194

><td class="source">	return overview<br></td></tr
><tr
id=sl_svn139_1195

><td class="source"><br></td></tr
><tr
id=sl_svn139_1196

><td class="source">def list_item(tag, item):<br></td></tr
><tr
id=sl_svn139_1197

><td class="source">	return &quot;&lt;li&gt;&quot; + item + &quot;&lt;/li&gt;\n&quot; + tag<br></td></tr
><tr
id=sl_svn139_1198

><td class="source"><br></td></tr
><tr
id=sl_svn139_1199

><td class="source">def format_issue(format, issue_no, issue_data, issue_template): # $format is xml, html, or text<br></td></tr
><tr
id=sl_svn139_1200

><td class="source">	if not issue_no in issue_template:<br></td></tr
><tr
id=sl_svn139_1201

><td class="source">		print &quot;[E] Can&#39;t find an issue template for issue number issue_no.  Bug!&quot;<br></td></tr
><tr
id=sl_svn139_1202

><td class="source">		sys.exit(1)<br></td></tr
><tr
id=sl_svn139_1203

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1204

><td class="source">	issue = issue_template_html<br></td></tr
><tr
id=sl_svn139_1205

><td class="source">	issue = issue.replace(&#39;REPLACE_TITLE&#39;, &#39;&lt;a name=&quot;&#39; + issue_template[issue_no][&#39;title&#39;] + &#39;&quot;&gt;&#39; + issue_template[issue_no][&#39;title&#39;] + &#39;&lt;/a&gt;&#39;)<br></td></tr
><tr
id=sl_svn139_1206

><td class="source">	description = issue_template[issue_no][&#39;description&#39;]<br></td></tr
><tr
id=sl_svn139_1207

><td class="source">	description = description.replace(&#39;\n\n+&#39;, &quot;&lt;p&gt;\n&quot;)<br></td></tr
><tr
id=sl_svn139_1208

><td class="source">	for key in issue_data[issue_no]:<br></td></tr
><tr
id=sl_svn139_1209

><td class="source">		#print &quot;[D] Processing data for %s&quot; % key<br></td></tr
><tr
id=sl_svn139_1210

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1211

><td class="source">		# print &quot;[D] $key has type issue_data[issue_no][&#39;$key&#39;][&#39;type&#39;]\n&quot;<br></td></tr
><tr
id=sl_svn139_1212

><td class="source">		#if issue_data[issue_no][key][&#39;type&#39;] == &quot;list&quot;:<br></td></tr
><tr
id=sl_svn139_1213

><td class="source">		# TODO alter data structre to include type<br></td></tr
><tr
id=sl_svn139_1214

><td class="source">		#section = issue_template[issue_no][&#39;supporting_data&#39;][key][&#39;section&#39;]<br></td></tr
><tr
id=sl_svn139_1215

><td class="source">		# print &quot;[D] Data belongs to section section\n&quot;<br></td></tr
><tr
id=sl_svn139_1216

><td class="source">		#if (section == &quot;description&quot;):<br></td></tr
><tr
id=sl_svn139_1217

><td class="source">		preamble = issue_template[issue_no][&#39;supporting_data&#39;][key][&#39;preamble&#39;]<br></td></tr
><tr
id=sl_svn139_1218

><td class="source">		data = issue_list_html<br></td></tr
><tr
id=sl_svn139_1219

><td class="source">		data = data.replace(&#39;REPLACE_PREAMBLE&#39;, preamble)<br></td></tr
><tr
id=sl_svn139_1220

><td class="source">		for item in issue_data[issue_no][key]:<br></td></tr
><tr
id=sl_svn139_1221

><td class="source">			# TODO alter data structure to include data<br></td></tr
><tr
id=sl_svn139_1222

><td class="source">			# print &quot;Processing item &quot; + item<br></td></tr
><tr
id=sl_svn139_1223

><td class="source">			perm_string = &quot; &quot;.join(issue_data[issue_no][key][item])<br></td></tr
><tr
id=sl_svn139_1224

><td class="source">			data = data.replace(&#39;REPLACE_ITEM&#39;, list_item(&quot;REPLACE_ITEM&quot;, item + &quot;: &quot; + perm_string))<br></td></tr
><tr
id=sl_svn139_1225

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1226

><td class="source">		data = data.replace(&#39;REPLACE_ITEM&#39;, &#39;&#39;)<br></td></tr
><tr
id=sl_svn139_1227

><td class="source">		issue = issue.replace(&#39;REPLACE_DESCRIPTION_DATA&#39;, data + &quot;\nREPLACE_DESCRIPTION_DATA&quot;)<br></td></tr
><tr
id=sl_svn139_1228

><td class="source">		#elif section == &quot;recommendation&quot;:<br></td></tr
><tr
id=sl_svn139_1229

><td class="source">		#	pass<br></td></tr
><tr
id=sl_svn139_1230

><td class="source">			#issue = issue.replace(&#39;REPLACE_RECOMMENDATION_DATA&#39;, &quot;data\nREPLACE_DESCRIPTION_DATA&#39;, <br></td></tr
><tr
id=sl_svn139_1231

><td class="source"><br></td></tr
><tr
id=sl_svn139_1232

><td class="source">	issue = issue.replace(&#39;REPLACE_RECOMMENDATION_DATA&#39;, &#39;&#39;)<br></td></tr
><tr
id=sl_svn139_1233

><td class="source">	issue = issue.replace(&#39;REPLACE_DESCRIPTION_DATA&#39;, &#39;&#39;)<br></td></tr
><tr
id=sl_svn139_1234

><td class="source">	issue = issue.replace(&#39;REPLACE_DESCRIPTION&#39;, description + &quot;&lt;p&gt;\n&quot;)<br></td></tr
><tr
id=sl_svn139_1235

><td class="source">	recommendation = issue_template[issue_no][&#39;recommendation&#39;]<br></td></tr
><tr
id=sl_svn139_1236

><td class="source">	issue = issue.replace(&#39;REPLACE_RECOMMENDATION&#39;, recommendation + &quot;&lt;p&gt;\n&quot;)<br></td></tr
><tr
id=sl_svn139_1237

><td class="source">	recommendation = recommendation.replace(&#39;\n\n+&#39;, &#39;&lt;p&gt;\n&#39;)<br></td></tr
><tr
id=sl_svn139_1238

><td class="source">	return issue<br></td></tr
><tr
id=sl_svn139_1239

><td class="source"><br></td></tr
><tr
id=sl_svn139_1240

><td class="source">def format_audit_data(format, audit_data): # $format is xml, html, or text<br></td></tr
><tr
id=sl_svn139_1241

><td class="source">	print &quot;format_audit_data not implemented yet&quot;<br></td></tr
><tr
id=sl_svn139_1242

><td class="source"><br></td></tr
><tr
id=sl_svn139_1243

><td class="source"># Inputs:<br></td></tr
><tr
id=sl_svn139_1244

><td class="source">#   string: issue_name<br></td></tr
><tr
id=sl_svn139_1245

><td class="source">#   array:  weak_perms<br></td></tr
><tr
id=sl_svn139_1246

><td class="source">def save_issue(issue_name, data_type, weak_perms):<br></td></tr
><tr
id=sl_svn139_1247

><td class="source">	#print weak_perms<br></td></tr
><tr
id=sl_svn139_1248

><td class="source">	global issues<br></td></tr
><tr
id=sl_svn139_1249

><td class="source">	if not issue_name in issues:<br></td></tr
><tr
id=sl_svn139_1250

><td class="source">		issues[issue_name] = {}<br></td></tr
><tr
id=sl_svn139_1251

><td class="source">	#if not &#39;supporting_data&#39; in issues[issue_name]:<br></td></tr
><tr
id=sl_svn139_1252

><td class="source">	#	issues[issue_name][&#39;supporting_data&#39;] = {}<br></td></tr
><tr
id=sl_svn139_1253

><td class="source">	for weak_perm in weak_perms:<br></td></tr
><tr
id=sl_svn139_1254

><td class="source">		object = weak_perm[0]<br></td></tr
><tr
id=sl_svn139_1255

><td class="source">		domain = weak_perm[1]<br></td></tr
><tr
id=sl_svn139_1256

><td class="source">		name = weak_perm[2]<br></td></tr
><tr
id=sl_svn139_1257

><td class="source">		permission = weak_perm[3]<br></td></tr
><tr
id=sl_svn139_1258

><td class="source">		key = object + &quot; has the following permissions granted for &quot; + domain + &quot;\\&quot; + name<br></td></tr
><tr
id=sl_svn139_1259

><td class="source">		if not data_type in issues[issue_name]:<br></td></tr
><tr
id=sl_svn139_1260

><td class="source">			issues[issue_name][data_type]= {}<br></td></tr
><tr
id=sl_svn139_1261

><td class="source">		if not key in issues[issue_name][data_type]:<br></td></tr
><tr
id=sl_svn139_1262

><td class="source">			issues[issue_name][data_type][key] = []<br></td></tr
><tr
id=sl_svn139_1263

><td class="source">		issues[issue_name][data_type][key].append(permission)<br></td></tr
><tr
id=sl_svn139_1264

><td class="source">		issues[issue_name][data_type][key] = list(set(issues[issue_name][data_type][key])) # dedup<br></td></tr
><tr
id=sl_svn139_1265

><td class="source"><br></td></tr
><tr
id=sl_svn139_1266

><td class="source">def save_issue_string(issue_name, data_type, issue_string):<br></td></tr
><tr
id=sl_svn139_1267

><td class="source">	#print weak_perms<br></td></tr
><tr
id=sl_svn139_1268

><td class="source">	global issues<br></td></tr
><tr
id=sl_svn139_1269

><td class="source">	if not issue_name in issues:<br></td></tr
><tr
id=sl_svn139_1270

><td class="source">		issues[issue_name] = {}<br></td></tr
><tr
id=sl_svn139_1271

><td class="source">	if not data_type in issues[issue_name]:<br></td></tr
><tr
id=sl_svn139_1272

><td class="source">		issues[issue_name][data_type]= {}<br></td></tr
><tr
id=sl_svn139_1273

><td class="source">	if not issue_string in issues[issue_name][data_type]:<br></td></tr
><tr
id=sl_svn139_1274

><td class="source">		issues[issue_name][data_type][issue_string] = []<br></td></tr
><tr
id=sl_svn139_1275

><td class="source"><br></td></tr
><tr
id=sl_svn139_1276

><td class="source"># args: string, string<br></td></tr
><tr
id=sl_svn139_1277

><td class="source"># Returns 1 if the principle provided is trusted (admin / system / user-definted trusted principle)<br></td></tr
><tr
id=sl_svn139_1278

><td class="source"># Returns 0 otherwise<br></td></tr
><tr
id=sl_svn139_1279

><td class="source">def principle_is_trusted(principle, domain):<br></td></tr
><tr
id=sl_svn139_1280

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1281

><td class="source">	if domain + &quot;\\&quot; + principle in trusted_principles_fq:<br></td></tr
><tr
id=sl_svn139_1282

><td class="source">		return 1<br></td></tr
><tr
id=sl_svn139_1283

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1284

><td class="source">	if principle in trusted_principles:<br></td></tr
><tr
id=sl_svn139_1285

><td class="source">		return 1<br></td></tr
><tr
id=sl_svn139_1286

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1287

><td class="source">	global tmp_trusted_principles_fq<br></td></tr
><tr
id=sl_svn139_1288

><td class="source">	if domain + &quot;\\&quot; + principle in tmp_trusted_principles_fq:<br></td></tr
><tr
id=sl_svn139_1289

><td class="source">		return 1<br></td></tr
><tr
id=sl_svn139_1290

><td class="source"><br></td></tr
><tr
id=sl_svn139_1291

><td class="source">	# Consider groups with zero members to be trusted too<br></td></tr
><tr
id=sl_svn139_1292

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_1293

><td class="source">		memberdict, total, rh = win32net.NetLocalGroupGetMembers(remote_server, principle , 1 , 0 , 100000 )<br></td></tr
><tr
id=sl_svn139_1294

><td class="source">		if len(memberdict) == 0:<br></td></tr
><tr
id=sl_svn139_1295

><td class="source">			return 1<br></td></tr
><tr
id=sl_svn139_1296

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_1297

><td class="source">		# If a user is a member of a trusted group (like administrators), then they are trusted<br></td></tr
><tr
id=sl_svn139_1298

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_1299

><td class="source">			group_attrs = win32net.NetUserGetLocalGroups(remote_server, principle)<br></td></tr
><tr
id=sl_svn139_1300

><td class="source">			if set(group_attrs).intersection(set(trusted_principles)):<br></td></tr
><tr
id=sl_svn139_1301

><td class="source">				return 1<br></td></tr
><tr
id=sl_svn139_1302

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_1303

><td class="source">			pass<br></td></tr
><tr
id=sl_svn139_1304

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1305

><td class="source">	return 0<br></td></tr
><tr
id=sl_svn139_1306

><td class="source"><br></td></tr
><tr
id=sl_svn139_1307

><td class="source">#	for memberinfo in memberdict:<br></td></tr
><tr
id=sl_svn139_1308

><td class="source">#		print &quot;\t&quot; + memberinfo[&#39;name&#39;] + &quot; (&quot; + win32security.ConvertSidToStringSid(memberinfo[&#39;sid&#39;]) + &quot;)&quot;<br></td></tr
><tr
id=sl_svn139_1309

><td class="source"># TODO ignore groups that only contain administrators<br></td></tr
><tr
id=sl_svn139_1310

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1311

><td class="source"># There are all possible objects.  SE_OBJECT_TYPE (http://msdn.microsoft.com/en-us/library/aa379593(VS.85).aspx):<br></td></tr
><tr
id=sl_svn139_1312

><td class="source">#  win32security.SE_UNKNOWN_OBJECT_TYPE<br></td></tr
><tr
id=sl_svn139_1313

><td class="source">#  win32security.SE_FILE_OBJECT<br></td></tr
><tr
id=sl_svn139_1314

><td class="source">#  win32security.SE_SERVICE<br></td></tr
><tr
id=sl_svn139_1315

><td class="source">#  win32security.SE_PRINTER<br></td></tr
><tr
id=sl_svn139_1316

><td class="source">#  win32security.SE_REGISTRY_KEY<br></td></tr
><tr
id=sl_svn139_1317

><td class="source">#  win32security.SE_LMSHARE<br></td></tr
><tr
id=sl_svn139_1318

><td class="source">#  win32security.SE_KERNEL_OBJECT<br></td></tr
><tr
id=sl_svn139_1319

><td class="source">#  win32security.SE_WINDOW_OBJECT<br></td></tr
><tr
id=sl_svn139_1320

><td class="source">#  win32security.SE_DS_OBJECT<br></td></tr
><tr
id=sl_svn139_1321

><td class="source">#  win32security.SE_DS_OBJECT_ALL<br></td></tr
><tr
id=sl_svn139_1322

><td class="source">#  win32security.SE_PROVIDER_DEFINED_OBJECT<br></td></tr
><tr
id=sl_svn139_1323

><td class="source">#  win32security.SE_WMIGUID_OBJECT<br></td></tr
><tr
id=sl_svn139_1324

><td class="source">#  win32security.SE_REGISTRY_WOW64_32KEY<br></td></tr
><tr
id=sl_svn139_1325

><td class="source"># object_type_s is one of<br></td></tr
><tr
id=sl_svn139_1326

><td class="source">#  service<br></td></tr
><tr
id=sl_svn139_1327

><td class="source">#  file<br></td></tr
><tr
id=sl_svn139_1328

><td class="source">#  dir<br></td></tr
><tr
id=sl_svn139_1329

><td class="source">def check_weak_perms(object_name, object_type_s, perms):<br></td></tr
><tr
id=sl_svn139_1330

><td class="source">	object_type = None<br></td></tr
><tr
id=sl_svn139_1331

><td class="source">	if object_type_s == &#39;file&#39;:<br></td></tr
><tr
id=sl_svn139_1332

><td class="source">		object_type = win32security.SE_FILE_OBJECT<br></td></tr
><tr
id=sl_svn139_1333

><td class="source">	if object_type_s == &#39;directory&#39;:<br></td></tr
><tr
id=sl_svn139_1334

><td class="source">		object_type = win32security.SE_FILE_OBJECT<br></td></tr
><tr
id=sl_svn139_1335

><td class="source">	if object_type_s == &#39;service&#39;:<br></td></tr
><tr
id=sl_svn139_1336

><td class="source">		object_type = win32security.SE_SERVICE<br></td></tr
><tr
id=sl_svn139_1337

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1338

><td class="source">	if object_type == win32security.SE_FILE_OBJECT:<br></td></tr
><tr
id=sl_svn139_1339

><td class="source">#		if not os.path.exists(object_name):<br></td></tr
><tr
id=sl_svn139_1340

><td class="source">#			print &quot;WARNING: %s doesn&#39;t exist&quot; % object_name<br></td></tr
><tr
id=sl_svn139_1341

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1342

><td class="source">		if os.path.isfile(object_name):<br></td></tr
><tr
id=sl_svn139_1343

><td class="source">			object_type_s = &#39;file&#39;<br></td></tr
><tr
id=sl_svn139_1344

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_1345

><td class="source">			object_type_s = &#39;directory&#39;<br></td></tr
><tr
id=sl_svn139_1346

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1347

><td class="source">	if object_type == None:<br></td></tr
><tr
id=sl_svn139_1348

><td class="source">		print &quot;ERROR: Unknown object type %s&quot; % object_type_s<br></td></tr
><tr
id=sl_svn139_1349

><td class="source">		exit(1)<br></td></tr
><tr
id=sl_svn139_1350

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1351

><td class="source">	try: <br></td></tr
><tr
id=sl_svn139_1352

><td class="source">		sd = win32security.GetNamedSecurityInfo (<br></td></tr
><tr
id=sl_svn139_1353

><td class="source">			object_name,<br></td></tr
><tr
id=sl_svn139_1354

><td class="source">			object_type,<br></td></tr
><tr
id=sl_svn139_1355

><td class="source">			win32security.OWNER_SECURITY_INFORMATION | win32security.DACL_SECURITY_INFORMATION<br></td></tr
><tr
id=sl_svn139_1356

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_1357

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_1358

><td class="source">		# print &quot;WARNING: Can&#39;t get security descriptor for &quot; + object_name + &quot;.  skipping.  (&quot; + details[2] + &quot;)&quot;<br></td></tr
><tr
id=sl_svn139_1359

><td class="source">		return []<br></td></tr
><tr
id=sl_svn139_1360

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1361

><td class="source">	return check_weak_perms_sd(object_name, object_type_s, sd, perms)<br></td></tr
><tr
id=sl_svn139_1362

><td class="source"><br></td></tr
><tr
id=sl_svn139_1363

><td class="source">def check_weak_write_perms_by_sd(object_name, object_type_s, sd):<br></td></tr
><tr
id=sl_svn139_1364

><td class="source">	return check_weak_perms_sd(object_name, object_type_s, sd, dangerous_perms_write)<br></td></tr
><tr
id=sl_svn139_1365

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1366

><td class="source">def check_weak_perms_sd(object_name, object_type_s, sd, perms):<br></td></tr
><tr
id=sl_svn139_1367

><td class="source">	dacl= sd.GetSecurityDescriptorDacl()<br></td></tr
><tr
id=sl_svn139_1368

><td class="source">	if dacl == None:<br></td></tr
><tr
id=sl_svn139_1369

><td class="source">		print &quot;No Discretionary ACL&quot;<br></td></tr
><tr
id=sl_svn139_1370

><td class="source">		return []<br></td></tr
><tr
id=sl_svn139_1371

><td class="source"><br></td></tr
><tr
id=sl_svn139_1372

><td class="source">	owner_sid = sd.GetSecurityDescriptorOwner()<br></td></tr
><tr
id=sl_svn139_1373

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_1374

><td class="source">		owner_name, owner_domain, type = win32security.LookupAccountSid(remote_server, owner_sid)<br></td></tr
><tr
id=sl_svn139_1375

><td class="source">		owner_fq = owner_domain + &quot;\\&quot; + owner_name<br></td></tr
><tr
id=sl_svn139_1376

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_1377

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_1378

><td class="source">			owner_fq = owner_name = win32security.ConvertSidToStringSid(owner_sid)<br></td></tr
><tr
id=sl_svn139_1379

><td class="source">			owner_domain = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_1380

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_1381

><td class="source">			owner_domain = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_1382

><td class="source">			owner_fq = owner_name = &quot;INVALIDSID!&quot;<br></td></tr
><tr
id=sl_svn139_1383

><td class="source"><br></td></tr
><tr
id=sl_svn139_1384

><td class="source">	weak_perms = []<br></td></tr
><tr
id=sl_svn139_1385

><td class="source">	for ace_no in range(0, dacl.GetAceCount()):<br></td></tr
><tr
id=sl_svn139_1386

><td class="source">		#print &quot;[D] ACE #%d&quot; % ace_no<br></td></tr
><tr
id=sl_svn139_1387

><td class="source">		ace = dacl.GetAce(ace_no)<br></td></tr
><tr
id=sl_svn139_1388

><td class="source">		flags = ace[0][1]<br></td></tr
><tr
id=sl_svn139_1389

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1390

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_1391

><td class="source">			principle, domain, type = win32security.LookupAccountSid(remote_server, ace[2])<br></td></tr
><tr
id=sl_svn139_1392

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_1393

><td class="source">			principle = win32security.ConvertSidToStringSid(ace[2])<br></td></tr
><tr
id=sl_svn139_1394

><td class="source">			domain = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_1395

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1396

><td class="source">		#print &quot;[D] ACE is for %s\\%s&quot; % (principle, domain)<br></td></tr
><tr
id=sl_svn139_1397

><td class="source">		#print &quot;[D] ACE Perm mask: &quot; + int2bin(ace[1])<br></td></tr
><tr
id=sl_svn139_1398

><td class="source">		#print &quot;[D] ace_type: &quot; + str(ace[0][0])<br></td></tr
><tr
id=sl_svn139_1399

><td class="source">		#print &quot;[D] DACL: &quot; + win32security.ConvertSecurityDescriptorToStringSecurityDescriptor(sd, win32security.SDDL_REVISION_1, win32security.DACL_SECURITY_INFORMATION)<br></td></tr
><tr
id=sl_svn139_1400

><td class="source">		if principle_is_trusted(principle, domain):<br></td></tr
><tr
id=sl_svn139_1401

><td class="source">			#print &quot;[D] Ignoring trusted principle %s\\%s&quot; % (principle, domain)<br></td></tr
><tr
id=sl_svn139_1402

><td class="source">			continue<br></td></tr
><tr
id=sl_svn139_1403

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1404

><td class="source">		if principle == &quot;CREATOR OWNER&quot;:<br></td></tr
><tr
id=sl_svn139_1405

><td class="source">			if principle_is_trusted(owner_name, owner_domain):<br></td></tr
><tr
id=sl_svn139_1406

><td class="source">				continue<br></td></tr
><tr
id=sl_svn139_1407

><td class="source">			else:<br></td></tr
><tr
id=sl_svn139_1408

><td class="source">				principle = &quot;CREATOR OWNER [%s]&quot; % owner_fq<br></td></tr
><tr
id=sl_svn139_1409

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1410

><td class="source">		for i in (&quot;ACCESS_ALLOWED_ACE_TYPE&quot;, &quot;ACCESS_DENIED_ACE_TYPE&quot;, &quot;SYSTEM_AUDIT_ACE_TYPE&quot;, &quot;SYSTEM_ALARM_ACE_TYPE&quot;):<br></td></tr
><tr
id=sl_svn139_1411

><td class="source">			if getattr(ntsecuritycon, i) == ace[0][0]:<br></td></tr
><tr
id=sl_svn139_1412

><td class="source">				ace_type_s = i<br></td></tr
><tr
id=sl_svn139_1413

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1414

><td class="source">		if not ace_type_s == &quot;ACCESS_ALLOWED_ACE_TYPE&quot;:<br></td></tr
><tr
id=sl_svn139_1415

><td class="source">			vprint(&quot;WARNING: Unimplmented ACE type encountered: &quot; + ace_type_s + &quot;.  skipping.&quot;)<br></td></tr
><tr
id=sl_svn139_1416

><td class="source">			continue<br></td></tr
><tr
id=sl_svn139_1417

><td class="source"><br></td></tr
><tr
id=sl_svn139_1418

><td class="source">		for mod, perms_tuple in perms[object_type_s].iteritems():<br></td></tr
><tr
id=sl_svn139_1419

><td class="source">			for perm in perms_tuple:<br></td></tr
><tr
id=sl_svn139_1420

><td class="source">				if getattr(mod, perm) &amp; ace[1] == getattr(mod, perm):<br></td></tr
><tr
id=sl_svn139_1421

><td class="source">					weak_perms.append([object_name, domain, principle, perm])<br></td></tr
><tr
id=sl_svn139_1422

><td class="source">	return weak_perms<br></td></tr
><tr
id=sl_svn139_1423

><td class="source"><br></td></tr
><tr
id=sl_svn139_1424

><td class="source">def dump_perms(object_name, object_type_s, options={}):<br></td></tr
><tr
id=sl_svn139_1425

><td class="source">	object_type = None<br></td></tr
><tr
id=sl_svn139_1426

><td class="source">	if object_type_s == &#39;file&#39;:<br></td></tr
><tr
id=sl_svn139_1427

><td class="source">		object_type = win32security.SE_FILE_OBJECT<br></td></tr
><tr
id=sl_svn139_1428

><td class="source">	if object_type_s == &#39;directory&#39;:<br></td></tr
><tr
id=sl_svn139_1429

><td class="source">		object_type = win32security.SE_FILE_OBJECT<br></td></tr
><tr
id=sl_svn139_1430

><td class="source">	if object_type_s == &#39;service&#39;:<br></td></tr
><tr
id=sl_svn139_1431

><td class="source">		object_type = win32security.SE_SERVICE<br></td></tr
><tr
id=sl_svn139_1432

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1433

><td class="source">	if object_type == win32security.SE_FILE_OBJECT:<br></td></tr
><tr
id=sl_svn139_1434

><td class="source">#		if not os.path.exists(object_name):<br></td></tr
><tr
id=sl_svn139_1435

><td class="source">#			print &quot;WARNING: %s doesn&#39;t exist&quot; % object_name<br></td></tr
><tr
id=sl_svn139_1436

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1437

><td class="source">		if os.path.isfile(object_name):<br></td></tr
><tr
id=sl_svn139_1438

><td class="source">			object_type_s = &#39;file&#39;<br></td></tr
><tr
id=sl_svn139_1439

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_1440

><td class="source">			object_type_s = &#39;directory&#39;<br></td></tr
><tr
id=sl_svn139_1441

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1442

><td class="source">	if object_type == None:<br></td></tr
><tr
id=sl_svn139_1443

><td class="source">		print &quot;ERROR: Unknown object type %s&quot; % object_type_s<br></td></tr
><tr
id=sl_svn139_1444

><td class="source">		exit(1)<br></td></tr
><tr
id=sl_svn139_1445

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1446

><td class="source">	try: <br></td></tr
><tr
id=sl_svn139_1447

><td class="source">		sd = win32security.GetNamedSecurityInfo (<br></td></tr
><tr
id=sl_svn139_1448

><td class="source">			object_name,<br></td></tr
><tr
id=sl_svn139_1449

><td class="source">			object_type,<br></td></tr
><tr
id=sl_svn139_1450

><td class="source">			win32security.OWNER_SECURITY_INFORMATION | win32security.DACL_SECURITY_INFORMATION<br></td></tr
><tr
id=sl_svn139_1451

><td class="source">		)<br></td></tr
><tr
id=sl_svn139_1452

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_1453

><td class="source">		# print &quot;WARNING: Can&#39;t get security descriptor for &quot; + object_name + &quot;.  skipping.  (&quot; + details[2] + &quot;)&quot;<br></td></tr
><tr
id=sl_svn139_1454

><td class="source">		return []<br></td></tr
><tr
id=sl_svn139_1455

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1456

><td class="source">	return dump_sd(object_name, object_type_s, sd, options)<br></td></tr
><tr
id=sl_svn139_1457

><td class="source"><br></td></tr
><tr
id=sl_svn139_1458

><td class="source">def dump_sd(object_name, object_type_s, sd, options={}):<br></td></tr
><tr
id=sl_svn139_1459

><td class="source">	perms = all_perms<br></td></tr
><tr
id=sl_svn139_1460

><td class="source">	if not sd:<br></td></tr
><tr
id=sl_svn139_1461

><td class="source">		return <br></td></tr
><tr
id=sl_svn139_1462

><td class="source">	dacl = sd.GetSecurityDescriptorDacl()<br></td></tr
><tr
id=sl_svn139_1463

><td class="source">	if dacl == None:<br></td></tr
><tr
id=sl_svn139_1464

><td class="source">		print &quot;No Discretionary ACL&quot;<br></td></tr
><tr
id=sl_svn139_1465

><td class="source">		return []<br></td></tr
><tr
id=sl_svn139_1466

><td class="source"><br></td></tr
><tr
id=sl_svn139_1467

><td class="source">	owner_sid = sd.GetSecurityDescriptorOwner()<br></td></tr
><tr
id=sl_svn139_1468

><td class="source"><br></td></tr
><tr
id=sl_svn139_1469

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_1470

><td class="source">		owner_name, owner_domain, type = win32security.LookupAccountSid(remote_server, owner_sid)<br></td></tr
><tr
id=sl_svn139_1471

><td class="source">		owner_fq = owner_domain + &quot;\\&quot; + owner_name<br></td></tr
><tr
id=sl_svn139_1472

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_1473

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_1474

><td class="source">			owner_fq = owner_name = win32security.ConvertSidToStringSid(owner_sid)<br></td></tr
><tr
id=sl_svn139_1475

><td class="source">			owner_domain = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_1476

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_1477

><td class="source">			owner_domain = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_1478

><td class="source">			owner_fq = owner_name = None<br></td></tr
><tr
id=sl_svn139_1479

><td class="source"><br></td></tr
><tr
id=sl_svn139_1480

><td class="source">	group_sid = sd.GetSecurityDescriptorGroup()<br></td></tr
><tr
id=sl_svn139_1481

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_1482

><td class="source">		group_name, group_domain, type = win32security.LookupAccountSid(remote_server, group_sid)<br></td></tr
><tr
id=sl_svn139_1483

><td class="source">		group_fq = group_domain + &quot;\\&quot; + group_name<br></td></tr
><tr
id=sl_svn139_1484

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_1485

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_1486

><td class="source">			group_fq = group_name = win32security.ConvertSidToStringSid(group_sid)<br></td></tr
><tr
id=sl_svn139_1487

><td class="source">			group_domain = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_1488

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_1489

><td class="source">			group_domain = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_1490

><td class="source">			group_fq = group_name = &quot;[none]&quot;<br></td></tr
><tr
id=sl_svn139_1491

><td class="source"><br></td></tr
><tr
id=sl_svn139_1492

><td class="source">	if owner_info:<br></td></tr
><tr
id=sl_svn139_1493

><td class="source">		print &quot;\tOwner: &quot; + str(owner_fq)<br></td></tr
><tr
id=sl_svn139_1494

><td class="source">		print &quot;\tGroup: &quot; + str(group_fq)<br></td></tr
><tr
id=sl_svn139_1495

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1496

><td class="source">	weak_perms = []<br></td></tr
><tr
id=sl_svn139_1497

><td class="source">	dump_acl(object_name, object_type_s, dacl, options)<br></td></tr
><tr
id=sl_svn139_1498

><td class="source">	return<br></td></tr
><tr
id=sl_svn139_1499

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1500

><td class="source">def dump_acl(object_name, object_type_s, sd, options={}):<br></td></tr
><tr
id=sl_svn139_1501

><td class="source">	dacl = sd<br></td></tr
><tr
id=sl_svn139_1502

><td class="source">	if dacl == None:<br></td></tr
><tr
id=sl_svn139_1503

><td class="source">		print &quot;No Discretionary ACL&quot;<br></td></tr
><tr
id=sl_svn139_1504

><td class="source">		return []<br></td></tr
><tr
id=sl_svn139_1505

><td class="source"><br></td></tr
><tr
id=sl_svn139_1506

><td class="source">	weak_perms = []<br></td></tr
><tr
id=sl_svn139_1507

><td class="source">	for ace_no in range(0, dacl.GetAceCount()):<br></td></tr
><tr
id=sl_svn139_1508

><td class="source">		# print &quot;[D] ACE #%d&quot; % ace_no<br></td></tr
><tr
id=sl_svn139_1509

><td class="source">		ace = dacl.GetAce(ace_no)<br></td></tr
><tr
id=sl_svn139_1510

><td class="source">		flags = ace[0][1]<br></td></tr
><tr
id=sl_svn139_1511

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1512

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_1513

><td class="source">			principle, domain, type = win32security.LookupAccountSid(remote_server, ace[2])<br></td></tr
><tr
id=sl_svn139_1514

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_1515

><td class="source">			principle = win32security.ConvertSidToStringSid(ace[2])<br></td></tr
><tr
id=sl_svn139_1516

><td class="source">			domain = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_1517

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1518

><td class="source">		mask = ace[1]<br></td></tr
><tr
id=sl_svn139_1519

><td class="source">		if ace[1] &lt; 0:<br></td></tr
><tr
id=sl_svn139_1520

><td class="source">			mask = ace[1] + 2**32<br></td></tr
><tr
id=sl_svn139_1521

><td class="source"><br></td></tr
><tr
id=sl_svn139_1522

><td class="source">		if ignore_trusted and principle_is_trusted(principle, domain):<br></td></tr
><tr
id=sl_svn139_1523

><td class="source">			# print &quot;[D] Ignoring trusted principle %s\\%s&quot; % (principle, domain)<br></td></tr
><tr
id=sl_svn139_1524

><td class="source">			continue<br></td></tr
><tr
id=sl_svn139_1525

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1526

><td class="source">		if principle == &quot;CREATOR OWNER&quot;:<br></td></tr
><tr
id=sl_svn139_1527

><td class="source">			if ignore_trusted and principle_is_trusted(owner_name, owner_domain):<br></td></tr
><tr
id=sl_svn139_1528

><td class="source">				#print &quot;[D] Ignoring trusted principle (creator owner) %s\\%s&quot; % (principle, domain)<br></td></tr
><tr
id=sl_svn139_1529

><td class="source">				continue<br></td></tr
><tr
id=sl_svn139_1530

><td class="source">			else:<br></td></tr
><tr
id=sl_svn139_1531

><td class="source">				principle = &quot;CREATOR OWNER [%s\%s]&quot; % (domain, principle)<br></td></tr
><tr
id=sl_svn139_1532

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1533

><td class="source">		for i in (&quot;ACCESS_ALLOWED_ACE_TYPE&quot;, &quot;ACCESS_DENIED_ACE_TYPE&quot;, &quot;SYSTEM_AUDIT_ACE_TYPE&quot;, &quot;SYSTEM_ALARM_ACE_TYPE&quot;):<br></td></tr
><tr
id=sl_svn139_1534

><td class="source">			if getattr(ntsecuritycon, i) == ace[0][0]:<br></td></tr
><tr
id=sl_svn139_1535

><td class="source">				ace_type_s = i<br></td></tr
><tr
id=sl_svn139_1536

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1537

><td class="source">		ace_type_short = ace_type_s<br></td></tr
><tr
id=sl_svn139_1538

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1539

><td class="source">		if ace_type_s == &quot;ACCESS_DENIED_ACE_TYPE&quot;:<br></td></tr
><tr
id=sl_svn139_1540

><td class="source">			ace_type_short = &quot;DENY&quot;<br></td></tr
><tr
id=sl_svn139_1541

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1542

><td class="source">		if ace_type_s == &quot;ACCESS_ALLOWED_ACE_TYPE&quot;:<br></td></tr
><tr
id=sl_svn139_1543

><td class="source">			ace_type_short = &quot;ALLOW&quot;<br></td></tr
><tr
id=sl_svn139_1544

><td class="source"><br></td></tr
><tr
id=sl_svn139_1545

><td class="source">		if weak_perms_only:<br></td></tr
><tr
id=sl_svn139_1546

><td class="source">			perms = dangerous_perms_write<br></td></tr
><tr
id=sl_svn139_1547

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_1548

><td class="source">			perms = all_perms<br></td></tr
><tr
id=sl_svn139_1549

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1550

><td class="source">		for mod, perms_tuple in perms[object_type_s].iteritems():<br></td></tr
><tr
id=sl_svn139_1551

><td class="source">			for perm in perms_tuple:<br></td></tr
><tr
id=sl_svn139_1552

><td class="source">				#print &quot;Checking for perm %s in ACE %s&quot; % (perm, mask)<br></td></tr
><tr
id=sl_svn139_1553

><td class="source">				if getattr(mod, perm) &amp; mask == getattr(mod, perm):<br></td></tr
><tr
id=sl_svn139_1554

><td class="source">					weak_perms.append([object_name, domain, principle, perm, ace_type_short])<br></td></tr
><tr
id=sl_svn139_1555

><td class="source">	print_weak_perms(object_type_s, weak_perms, options)<br></td></tr
><tr
id=sl_svn139_1556

><td class="source"><br></td></tr
><tr
id=sl_svn139_1557

><td class="source">def check_weak_write_perms(object_name, object_type_s):<br></td></tr
><tr
id=sl_svn139_1558

><td class="source">	return check_weak_perms(object_name, object_type_s, dangerous_perms_write)<br></td></tr
><tr
id=sl_svn139_1559

><td class="source"><br></td></tr
><tr
id=sl_svn139_1560

><td class="source">def check_registry():<br></td></tr
><tr
id=sl_svn139_1561

><td class="source">	for key_string in reg_paths:<br></td></tr
><tr
id=sl_svn139_1562

><td class="source">		parts = key_string.split(&quot;\\&quot;)<br></td></tr
><tr
id=sl_svn139_1563

><td class="source">		hive = parts[0]<br></td></tr
><tr
id=sl_svn139_1564

><td class="source">		key_string = &quot;\\&quot;.join(parts[1:])<br></td></tr
><tr
id=sl_svn139_1565

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_1566

><td class="source">			keyh = win32api.RegOpenKeyEx(getattr(win32con, hive), key_string, 0, win32con.KEY_ENUMERATE_SUB_KEYS | win32con.KEY_QUERY_VALUE | win32con.KEY_READ)<br></td></tr
><tr
id=sl_svn139_1567

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_1568

><td class="source">			#print &quot;Can&#39;t open: &quot; + hive + &quot;\\&quot; + key_string<br></td></tr
><tr
id=sl_svn139_1569

><td class="source">			continue<br></td></tr
><tr
id=sl_svn139_1570

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1571

><td class="source">		sd = win32api.RegGetKeySecurity(keyh, win32security.DACL_SECURITY_INFORMATION | win32security.OWNER_SECURITY_INFORMATION)<br></td></tr
><tr
id=sl_svn139_1572

><td class="source">		weak_perms = check_weak_write_perms_by_sd(hive + &quot;\\&quot; + key_string, &#39;reg&#39;, sd)<br></td></tr
><tr
id=sl_svn139_1573

><td class="source">		if weak_perms:<br></td></tr
><tr
id=sl_svn139_1574

><td class="source">			vprint(hive + &quot;\\&quot; + key_string)<br></td></tr
><tr
id=sl_svn139_1575

><td class="source">			#print weak_perms<br></td></tr
><tr
id=sl_svn139_1576

><td class="source">			if verbose == 0:<br></td></tr
><tr
id=sl_svn139_1577

><td class="source">				sys.stdout.write(&quot;.&quot;)<br></td></tr
><tr
id=sl_svn139_1578

><td class="source">			save_issue(&quot;WPC003&quot;, &quot;writable_reg_paths&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_1579

><td class="source">			# print_weak_perms(&quot;x&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_1580

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_1581

><td class="source"><br></td></tr
><tr
id=sl_svn139_1582

><td class="source"># TODO save_issue(&quot;WPC009&quot;, &quot;writable_eventlog_key&quot;, weak_perms)  # weak perms on event log reg key<br></td></tr
><tr
id=sl_svn139_1583

><td class="source">def check_event_logs():<br></td></tr
><tr
id=sl_svn139_1584

><td class="source">	key_string = &quot;HKEY_LOCAL_MACHINE\\&quot; + eventlog_key_hklm<br></td></tr
><tr
id=sl_svn139_1585

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_1586

><td class="source">		keyh = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, eventlog_key_hklm , 0, win32con.KEY_ENUMERATE_SUB_KEYS | win32con.KEY_QUERY_VALUE | win32con.KEY_READ)<br></td></tr
><tr
id=sl_svn139_1587

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_1588

><td class="source">		print &quot;Can&#39;t open: &quot; + key_string<br></td></tr
><tr
id=sl_svn139_1589

><td class="source">		return 0<br></td></tr
><tr
id=sl_svn139_1590

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1591

><td class="source">	subkeys = win32api.RegEnumKeyEx(keyh)<br></td></tr
><tr
id=sl_svn139_1592

><td class="source">	for subkey in subkeys:<br></td></tr
><tr
id=sl_svn139_1593

><td class="source">		# print key_string + &quot;\\&quot; + subkey[0]<br></td></tr
><tr
id=sl_svn139_1594

><td class="source">		sys.stdout.write(&quot;.&quot;)<br></td></tr
><tr
id=sl_svn139_1595

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_1596

><td class="source">			subkeyh = win32api.RegOpenKeyEx(keyh, subkey[0] , 0, win32con.KEY_ENUMERATE_SUB_KEYS | win32con.KEY_QUERY_VALUE | win32con.KEY_READ)<br></td></tr
><tr
id=sl_svn139_1597

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_1598

><td class="source">			print &quot;Can&#39;t open: &quot; + key_string<br></td></tr
><tr
id=sl_svn139_1599

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_1600

><td class="source">			subkey_count, value_count, mod_time = win32api.RegQueryInfoKey(subkeyh)<br></td></tr
><tr
id=sl_svn139_1601

><td class="source">			# print &quot;\tChild Nodes: %s subkeys, %s values&quot; % (subkey_count, value_count)<br></td></tr
><tr
id=sl_svn139_1602

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1603

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_1604

><td class="source">				filename, type = win32api.RegQueryValueEx(subkeyh, &quot;DisplayNameFile&quot;)<br></td></tr
><tr
id=sl_svn139_1605

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1606

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_1607

><td class="source">			else:<br></td></tr
><tr
id=sl_svn139_1608

><td class="source">				weak_perms = check_weak_write_perms(os.path.expandvars(filename), &#39;file&#39;)<br></td></tr
><tr
id=sl_svn139_1609

><td class="source">				if weak_perms:<br></td></tr
><tr
id=sl_svn139_1610

><td class="source">					# print &quot;------------------------------------------------&quot;<br></td></tr
><tr
id=sl_svn139_1611

><td class="source">					# print &quot;Weak permissions found on event log display DLL:&quot;<br></td></tr
><tr
id=sl_svn139_1612

><td class="source">					# print_weak_perms(&quot;File&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_1613

><td class="source">					sys.stdout.write(&quot;!&quot;)<br></td></tr
><tr
id=sl_svn139_1614

><td class="source">					save_issue(&quot;WPC008&quot;, &quot;writable_eventlog_dll&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_1615

><td class="source">				<br></td></tr
><tr
id=sl_svn139_1616

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_1617

><td class="source">				filename, type = win32api.RegQueryValueEx(subkeyh, &quot;File&quot;)<br></td></tr
><tr
id=sl_svn139_1618

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1619

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_1620

><td class="source">			else:<br></td></tr
><tr
id=sl_svn139_1621

><td class="source">				weak_perms = check_weak_write_perms(os.path.expandvars(filename), &#39;file&#39;)<br></td></tr
><tr
id=sl_svn139_1622

><td class="source">				if weak_perms:<br></td></tr
><tr
id=sl_svn139_1623

><td class="source">					# print &quot;------------------------------------------------&quot;<br></td></tr
><tr
id=sl_svn139_1624

><td class="source">					# print &quot;Weak permissions found on event log file:&quot;<br></td></tr
><tr
id=sl_svn139_1625

><td class="source">					# print_weak_perms(&quot;File&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_1626

><td class="source">					sys.stdout.write(&quot;!&quot;)<br></td></tr
><tr
id=sl_svn139_1627

><td class="source">					save_issue(&quot;WPC007&quot;, &quot;writable_eventlog_file&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_1628

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_1629

><td class="source">		#sd = win32api.RegGetKeySecurity(subkeyh, win32security.DACL_SECURITY_INFORMATION) # TODO: get owner too?<br></td></tr
><tr
id=sl_svn139_1630

><td class="source">		#print &quot;\tDACL: &quot; + win32security.ConvertSecurityDescriptorToStringSecurityDescriptor(sd, win32security.SDDL_REVISION_1, win32security.DACL_SECURITY_INFORMATION)<br></td></tr
><tr
id=sl_svn139_1631

><td class="source"><br></td></tr
><tr
id=sl_svn139_1632

><td class="source">def get_extra_privs():<br></td></tr
><tr
id=sl_svn139_1633

><td class="source">	# Try to give ourselves some extra privs (only works if we&#39;re admin):<br></td></tr
><tr
id=sl_svn139_1634

><td class="source">	# SeBackupPrivilege   - so we can read anything<br></td></tr
><tr
id=sl_svn139_1635

><td class="source">	# SeDebugPrivilege    - so we can find out about other processes (otherwise OpenProcess will fail for some)<br></td></tr
><tr
id=sl_svn139_1636

><td class="source">	# SeSecurityPrivilege - ??? what does this do?<br></td></tr
><tr
id=sl_svn139_1637

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1638

><td class="source">	# Problem: Vista+ support &quot;Protected&quot; processes, e.g. audiodg.exe.  We can&#39;t see info about these.<br></td></tr
><tr
id=sl_svn139_1639

><td class="source">	# Interesting post on why Protected Process aren&#39;t really secure anyway: http://www.alex-ionescu.com/?p=34<br></td></tr
><tr
id=sl_svn139_1640

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1641

><td class="source">	th = win32security.OpenProcessToken(win32api.GetCurrentProcess(), win32con.TOKEN_ADJUST_PRIVILEGES | win32con.TOKEN_QUERY)<br></td></tr
><tr
id=sl_svn139_1642

><td class="source">	privs = win32security.GetTokenInformation(th, TokenPrivileges)<br></td></tr
><tr
id=sl_svn139_1643

><td class="source">	newprivs = []<br></td></tr
><tr
id=sl_svn139_1644

><td class="source">	for privtuple in privs:<br></td></tr
><tr
id=sl_svn139_1645

><td class="source">		if privtuple[0] == win32security.LookupPrivilegeValue(remote_server, &quot;SeBackupPrivilege&quot;) or privtuple[0] == win32security.LookupPrivilegeValue(remote_server, &quot;SeDebugPrivilege&quot;) or privtuple[0] == win32security.LookupPrivilegeValue(remote_server, &quot;SeSecurityPrivilege&quot;):<br></td></tr
><tr
id=sl_svn139_1646

><td class="source">			print &quot;Added privilege &quot; + str(privtuple[0])<br></td></tr
><tr
id=sl_svn139_1647

><td class="source">			# privtuple[1] = 2 # tuples are immutable.  WHY?!<br></td></tr
><tr
id=sl_svn139_1648

><td class="source">			newprivs.append((privtuple[0], 2)) # SE_PRIVILEGE_ENABLED<br></td></tr
><tr
id=sl_svn139_1649

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_1650

><td class="source">			newprivs.append((privtuple[0], privtuple[1]))<br></td></tr
><tr
id=sl_svn139_1651

><td class="source">				<br></td></tr
><tr
id=sl_svn139_1652

><td class="source">	# Adjust privs<br></td></tr
><tr
id=sl_svn139_1653

><td class="source">	privs = tuple(newprivs)<br></td></tr
><tr
id=sl_svn139_1654

><td class="source">	str(win32security.AdjustTokenPrivileges(th, False , privs))<br></td></tr
><tr
id=sl_svn139_1655

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1656

><td class="source">def audit_processes():<br></td></tr
><tr
id=sl_svn139_1657

><td class="source">	get_extra_privs()<br></td></tr
><tr
id=sl_svn139_1658

><td class="source">	# Things we might want to know about a process:<br></td></tr
><tr
id=sl_svn139_1659

><td class="source">	# TCP/UDP/Local sockets<br></td></tr
><tr
id=sl_svn139_1660

><td class="source">	# Treads - and the tokens of each (API doesn&#39;t support getting a thread handle!)<br></td></tr
><tr
id=sl_svn139_1661

><td class="source">	# Shared memory<br></td></tr
><tr
id=sl_svn139_1662

><td class="source">	<br></td></tr
><tr
id=sl_svn139_1663

><td class="source">	pids = win32process.EnumProcesses()<br></td></tr
><tr
id=sl_svn139_1664

><td class="source">	for pid in sorted(pids):<br></td></tr
><tr
id=sl_svn139_1665

><td class="source">		print &quot;---------------------------------------------------------&quot;<br></td></tr
><tr
id=sl_svn139_1666

><td class="source">		print &quot;PID: %s&quot; % pid<br></td></tr
><tr
id=sl_svn139_1667

><td class="source">		# TODO there&#39;s a security descriptor for each process accessible via GetSecurityInfo according to http://msdn.microsoft.com/en-us/library/ms684880%28VS.85%29.aspx<br></td></tr
><tr
id=sl_svn139_1668

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1669

><td class="source">		ph = 0<br></td></tr
><tr
id=sl_svn139_1670

><td class="source">		gotph = 0<br></td></tr
><tr
id=sl_svn139_1671

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_1672

><td class="source">			# PROCESS_VM_READ is required to list modules (DLLs, EXE)<br></td></tr
><tr
id=sl_svn139_1673

><td class="source">			ph = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid)<br></td></tr
><tr
id=sl_svn139_1674

><td class="source">			gotph = 1<br></td></tr
><tr
id=sl_svn139_1675

><td class="source">			vprint(&quot;OpenProcess with VM_READ and PROCESS_QUERY_INFORMATION: Success&quot;)<br></td></tr
><tr
id=sl_svn139_1676

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_1677

><td class="source">			print(&quot;OpenProcess with VM_READ and PROCESS_QUERY_INFORMATION: Failed&quot;)<br></td></tr
><tr
id=sl_svn139_1678

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_1679

><td class="source">				# We can still get some info without PROCESS_VM_READ<br></td></tr
><tr
id=sl_svn139_1680

><td class="source">				ph = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION , False, pid)<br></td></tr
><tr
id=sl_svn139_1681

><td class="source">				gotph = 1<br></td></tr
><tr
id=sl_svn139_1682

><td class="source">				vprint(&quot;OpenProcess with PROCESS_QUERY_INFORMATION: Success&quot;)<br></td></tr
><tr
id=sl_svn139_1683

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1684

><td class="source">				print &quot;OpenProcess with PROCESS_QUERY_INFORMATION: Failed&quot;<br></td></tr
><tr
id=sl_svn139_1685

><td class="source">				try:<br></td></tr
><tr
id=sl_svn139_1686

><td class="source">					# If we have to resort to using PROCESS_QUERY_LIMITED_INFORMATION, the process is protected.<br></td></tr
><tr
id=sl_svn139_1687

><td class="source">					# There&#39;s no point trying PROCESS_VM_READ<br></td></tr
><tr
id=sl_svn139_1688

><td class="source">					ph = win32api.OpenProcess(win32con.PROCESS_QUERY_LIMITED_INFORMATION , False, pid)<br></td></tr
><tr
id=sl_svn139_1689

><td class="source">					gotph = 1<br></td></tr
><tr
id=sl_svn139_1690

><td class="source">					vprint(&quot;OpenProcess with PROCESS_QUERY_LIMITED_INFORMATION: Success&quot;)<br></td></tr
><tr
id=sl_svn139_1691

><td class="source">				except:<br></td></tr
><tr
id=sl_svn139_1692

><td class="source">					print &quot;OpenProcess with PROCESS_QUERY_LIMITED_INFORMATION: Failed&quot;<br></td></tr
><tr
id=sl_svn139_1693

><td class="source">					# Move onto the next process.  We don&#39;t have a process handle!<br></td></tr
><tr
id=sl_svn139_1694

><td class="source">					<br></td></tr
><tr
id=sl_svn139_1695

><td class="source">		exe = &quot;[unknown]&quot;	<br></td></tr
><tr
id=sl_svn139_1696

><td class="source">		gotexe = 0<br></td></tr
><tr
id=sl_svn139_1697

><td class="source">		mhs = 0<br></td></tr
><tr
id=sl_svn139_1698

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_1699

><td class="source">			mhs = win32process.EnumProcessModules(ph)<br></td></tr
><tr
id=sl_svn139_1700

><td class="source">			mhs = list(mhs)<br></td></tr
><tr
id=sl_svn139_1701

><td class="source">			exe = win32process.GetModuleFileNameEx(ph, mhs.pop(0))<br></td></tr
><tr
id=sl_svn139_1702

><td class="source">			gotexe = 1<br></td></tr
><tr
id=sl_svn139_1703

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_1704

><td class="source">			pass<br></td></tr
><tr
id=sl_svn139_1705

><td class="source">		print &quot;Filename: %s&quot; % exe<br></td></tr
><tr
id=sl_svn139_1706

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1707

><td class="source">		gottokenh = 0<br></td></tr
><tr
id=sl_svn139_1708

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1709

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_1710

><td class="source">			tokenh = win32security.OpenProcessToken(ph, win32con.TOKEN_QUERY)<br></td></tr
><tr
id=sl_svn139_1711

><td class="source">			gottokenh = 1<br></td></tr
><tr
id=sl_svn139_1712

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1713

><td class="source">			sidObj, intVal = win32security.GetTokenInformation(tokenh, TokenUser)<br></td></tr
><tr
id=sl_svn139_1714

><td class="source">			if sidObj:<br></td></tr
><tr
id=sl_svn139_1715

><td class="source">				accountName, domainName, accountTypeInt = win32security.LookupAccountSid(remote_server, sidObj)<br></td></tr
><tr
id=sl_svn139_1716

><td class="source">				print &quot;TokenUser: %s\%s (type %s)&quot; % (domainName, accountName, accountTypeInt) <br></td></tr
><tr
id=sl_svn139_1717

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1718

><td class="source">			sidObj =  win32security.GetTokenInformation(tokenh, TokenOwner)<br></td></tr
><tr
id=sl_svn139_1719

><td class="source">			if sidObj:<br></td></tr
><tr
id=sl_svn139_1720

><td class="source">				accountName, domainName, accountTypeInt = win32security.LookupAccountSid(remote_server, sidObj)<br></td></tr
><tr
id=sl_svn139_1721

><td class="source">				print &quot;TokenOwner: %s\%s (type %s)&quot; % (domainName, accountName, accountTypeInt) <br></td></tr
><tr
id=sl_svn139_1722

><td class="source">				<br></td></tr
><tr
id=sl_svn139_1723

><td class="source">			sidObj =  win32security.GetTokenInformation(tokenh, TokenPrimaryGroup)<br></td></tr
><tr
id=sl_svn139_1724

><td class="source">			if sidObj:<br></td></tr
><tr
id=sl_svn139_1725

><td class="source">				accountName, domainName, accountTypeInt = win32security.LookupAccountSid(remote_server, sidObj)<br></td></tr
><tr
id=sl_svn139_1726

><td class="source">				print &quot;TokenPrimaryGroup: %s\%s (type %s)&quot; % (domainName, accountName, accountTypeInt) <br></td></tr
><tr
id=sl_svn139_1727

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_1728

><td class="source">			print &quot;OpenProcessToken with TOKEN_QUERY: Failed&quot;<br></td></tr
><tr
id=sl_svn139_1729

><td class="source">			print &quot;TokenUser: Unknown&quot;<br></td></tr
><tr
id=sl_svn139_1730

><td class="source">			print &quot;TokenOwner: Unknown&quot;<br></td></tr
><tr
id=sl_svn139_1731

><td class="source">			print &quot;TokenPrimaryGroup: Unknown&quot;<br></td></tr
><tr
id=sl_svn139_1732

><td class="source">			pass<br></td></tr
><tr
id=sl_svn139_1733

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1734

><td class="source">		user = &quot;unknown\\unknown&quot;<br></td></tr
><tr
id=sl_svn139_1735

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1736

><td class="source">		# TODO I&#39;m not sure how to interogate threads.<br></td></tr
><tr
id=sl_svn139_1737

><td class="source">		# There&#39;s no OpenThread() in win32api.  I need a thread handle before I can get Thread Tokens.<br></td></tr
><tr
id=sl_svn139_1738

><td class="source">		# The code below lists threadid&#39;s, be we can&#39;t use the handle (it&#39;s not a PyHandle)<br></td></tr
><tr
id=sl_svn139_1739

><td class="source">		#<br></td></tr
><tr
id=sl_svn139_1740

><td class="source">		# hThreadSnap = CreateToolhelp32Snapshot (TH32CS_SNAPTHREAD, pid)<br></td></tr
><tr
id=sl_svn139_1741

><td class="source">		# if hThreadSnap == INVALID_HANDLE_VALUE:<br></td></tr
><tr
id=sl_svn139_1742

><td class="source">			# print &quot;Failed to get Thread snapshot&quot;<br></td></tr
><tr
id=sl_svn139_1743

><td class="source">		# else:<br></td></tr
><tr
id=sl_svn139_1744

><td class="source">			# te32 = Thread32First (hThreadSnap)<br></td></tr
><tr
id=sl_svn139_1745

><td class="source">			# if te32:<br></td></tr
><tr
id=sl_svn139_1746

><td class="source">				# while True:<br></td></tr
><tr
id=sl_svn139_1747

><td class="source">					# if te32.th32OwnerProcessID == pid:<br></td></tr
><tr
id=sl_svn139_1748

><td class="source">						# hThread = OpenThread (win32con.THREAD_QUERY_INFORMATION, FALSE, te32.th32ThreadID)<br></td></tr
><tr
id=sl_svn139_1749

><td class="source">						# print &quot;PID %s, ThreadID %s&quot; % (pid, te32.th32ThreadID)<br></td></tr
><tr
id=sl_svn139_1750

><td class="source">						# print &quot;Priority: &quot; + str(win32process.GetThreadPriority(hThread))<br></td></tr
><tr
id=sl_svn139_1751

><td class="source">						# CloseHandle (hThread)<br></td></tr
><tr
id=sl_svn139_1752

><td class="source">					# te32 = Thread32Next (hThreadSnap)<br></td></tr
><tr
id=sl_svn139_1753

><td class="source">					# if not te32:<br></td></tr
><tr
id=sl_svn139_1754

><td class="source">						 # break<br></td></tr
><tr
id=sl_svn139_1755

><td class="source">			# CloseHandle (hThreadSnap)<br></td></tr
><tr
id=sl_svn139_1756

><td class="source"><br></td></tr
><tr
id=sl_svn139_1757

><td class="source">#		except:<br></td></tr
><tr
id=sl_svn139_1758

><td class="source">#			print &quot;EnumProcessModules: Failed&quot;<br></td></tr
><tr
id=sl_svn139_1759

><td class="source">			# continue<br></td></tr
><tr
id=sl_svn139_1760

><td class="source">		# print &quot;EnumProcessModules: Success&quot;<br></td></tr
><tr
id=sl_svn139_1761

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1762

><td class="source">		if ph:<br></td></tr
><tr
id=sl_svn139_1763

><td class="source">			print &quot;IsWow64 Process: %s&quot; % win32process.IsWow64Process(ph)<br></td></tr
><tr
id=sl_svn139_1764

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1765

><td class="source">		if gottokenh:<br></td></tr
><tr
id=sl_svn139_1766

><td class="source">			vprint(&quot;OpenProcessToken with TOKEN_QUERY: Success&quot;)<br></td></tr
><tr
id=sl_svn139_1767

><td class="source">			imp_levels = {<br></td></tr
><tr
id=sl_svn139_1768

><td class="source">				&quot;SecurityAnonymous&quot;: 0,<br></td></tr
><tr
id=sl_svn139_1769

><td class="source">				&quot;SecurityIdentification&quot;: 1,<br></td></tr
><tr
id=sl_svn139_1770

><td class="source">				&quot;SecurityImpersonation&quot;: 2,<br></td></tr
><tr
id=sl_svn139_1771

><td class="source">				&quot;SecurityDelegation&quot;: 3<br></td></tr
><tr
id=sl_svn139_1772

><td class="source">			}<br></td></tr
><tr
id=sl_svn139_1773

><td class="source">			#for ilevel in imp_levels.keys():<br></td></tr
><tr
id=sl_svn139_1774

><td class="source">				#sys.stdout.write(&quot;Trying DuplicateToken with &quot; + ilevel)<br></td></tr
><tr
id=sl_svn139_1775

><td class="source">				#try:<br></td></tr
><tr
id=sl_svn139_1776

><td class="source">					#win32security.DuplicateToken(tokenh, imp_levels[ilevel])<br></td></tr
><tr
id=sl_svn139_1777

><td class="source">					#print &quot;success&quot;<br></td></tr
><tr
id=sl_svn139_1778

><td class="source">				#except:<br></td></tr
><tr
id=sl_svn139_1779

><td class="source">					#print &quot;failed&quot;<br></td></tr
><tr
id=sl_svn139_1780

><td class="source">			tokentype =  win32security.GetTokenInformation(tokenh, TokenType)<br></td></tr
><tr
id=sl_svn139_1781

><td class="source">			tokentype_str = &quot;TokenImpersonation&quot;<br></td></tr
><tr
id=sl_svn139_1782

><td class="source">			if tokentype == 1:<br></td></tr
><tr
id=sl_svn139_1783

><td class="source">				tokentype_str = &quot;TokenPrimary&quot;<br></td></tr
><tr
id=sl_svn139_1784

><td class="source">			print &quot;Token Type: &quot; + tokentype_str<br></td></tr
><tr
id=sl_svn139_1785

><td class="source">			print &quot;Logon Session ID: &quot; + str(win32security.GetTokenInformation(tokenh, TokenOrigin))<br></td></tr
><tr
id=sl_svn139_1786

><td class="source">			try: <br></td></tr
><tr
id=sl_svn139_1787

><td class="source">				source = win32security.GetTokenInformation(tokenh, TokenSource)<br></td></tr
><tr
id=sl_svn139_1788

><td class="source">				print &quot;Token Source: &quot; + source<br></td></tr
><tr
id=sl_svn139_1789

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1790

><td class="source">				print &quot;Token Source: Unknown (Access Denied)&quot;<br></td></tr
><tr
id=sl_svn139_1791

><td class="source">				<br></td></tr
><tr
id=sl_svn139_1792

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_1793

><td class="source">				print &quot;TokenImpersonationLevel: %s&quot; % win32security.GetTokenInformation(tokenh, TokenImpersonationLevel) # doesn&#39;t work on xp<br></td></tr
><tr
id=sl_svn139_1794

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1795

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_1796

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1797

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_1798

><td class="source">				r = win32security.GetTokenInformation(tokenh, TokenHasRestrictions) # doesn&#39;t work on xp<br></td></tr
><tr
id=sl_svn139_1799

><td class="source">				if r == 0:<br></td></tr
><tr
id=sl_svn139_1800

><td class="source">					print &quot;TokenHasRestrictions: 0 (not filtered)&quot;<br></td></tr
><tr
id=sl_svn139_1801

><td class="source">				else:<br></td></tr
><tr
id=sl_svn139_1802

><td class="source">					print &quot;TokenHasRestrictions: %s (token has been filtered)&quot; % r<br></td></tr
><tr
id=sl_svn139_1803

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1804

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_1805

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1806

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_1807

><td class="source">				e = win32security.GetTokenInformation(tokenh, TokenElevationType) # vista<br></td></tr
><tr
id=sl_svn139_1808

><td class="source">				if e == 1:<br></td></tr
><tr
id=sl_svn139_1809

><td class="source">					print &quot;TokenElevationType: TokenElevationTypeDefault&quot;<br></td></tr
><tr
id=sl_svn139_1810

><td class="source">				elif e == 2:<br></td></tr
><tr
id=sl_svn139_1811

><td class="source">					print &quot;TokenElevationType: TokenElevationTypeFull&quot;<br></td></tr
><tr
id=sl_svn139_1812

><td class="source">				elif e == 3:<br></td></tr
><tr
id=sl_svn139_1813

><td class="source">					print &quot;TokenElevationType: TokenElevationTypeLimited&quot;<br></td></tr
><tr
id=sl_svn139_1814

><td class="source">				else:<br></td></tr
><tr
id=sl_svn139_1815

><td class="source">					print &quot;TokenElevationType: Unknown (%s)&quot; % e<br></td></tr
><tr
id=sl_svn139_1816

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1817

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_1818

><td class="source">				<br></td></tr
><tr
id=sl_svn139_1819

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_1820

><td class="source">				print &quot;TokenUIAccess: %s&quot; % win32security.GetTokenInformation(tokenh, TokenUIAccess) # doesn&#39;t work on xp<br></td></tr
><tr
id=sl_svn139_1821

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1822

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_1823

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1824

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_1825

><td class="source">				print &quot;TokenLinkedToken: %s&quot; % win32security.GetTokenInformation(tokenh, TokenLinkedToken) # vista<br></td></tr
><tr
id=sl_svn139_1826

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1827

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_1828

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1829

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_1830

><td class="source">				print &quot;TokenLogonSid: %s&quot; % win32security.GetTokenInformation(tokenh, TokenLogonSid) # doesn&#39;t work on xp<br></td></tr
><tr
id=sl_svn139_1831

><td class="source">				print &quot;TokenElevation: %s&quot; % win32security.GetTokenInformation(tokenh, TokenElevation) # vista<br></td></tr
><tr
id=sl_svn139_1832

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1833

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_1834

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1835

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_1836

><td class="source">				sid, i =  win32security.GetTokenInformation(tokenh, TokenIntegrityLevel) # vista<br></td></tr
><tr
id=sl_svn139_1837

><td class="source">				try:<br></td></tr
><tr
id=sl_svn139_1838

><td class="source">					accountName, domainName, accountTypeInt = win32security.LookupAccountSid(None, sid)<br></td></tr
><tr
id=sl_svn139_1839

><td class="source">					user = domainName + &quot;\\&quot; + accountName + &quot; (&quot; + win32security.ConvertSidToStringSid(sid) + &quot;)&quot;<br></td></tr
><tr
id=sl_svn139_1840

><td class="source">				except:<br></td></tr
><tr
id=sl_svn139_1841

><td class="source">					user = win32security.ConvertSidToStringSid(sid)<br></td></tr
><tr
id=sl_svn139_1842

><td class="source">				print &quot;TokenIntegrityLevel: %s %s&quot; % (user, i)<br></td></tr
><tr
id=sl_svn139_1843

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1844

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_1845

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1846

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_1847

><td class="source">				m = win32security.GetTokenInformation(tokenh, TokenMandatoryPolicy) # vista<br></td></tr
><tr
id=sl_svn139_1848

><td class="source">				if m == 0:<br></td></tr
><tr
id=sl_svn139_1849

><td class="source">					print &quot;TokenMandatoryPolicy: OFF&quot;<br></td></tr
><tr
id=sl_svn139_1850

><td class="source">				elif m == 1:<br></td></tr
><tr
id=sl_svn139_1851

><td class="source">					print &quot;TokenMandatoryPolicy: NO_WRITE_UP&quot;<br></td></tr
><tr
id=sl_svn139_1852

><td class="source">				elif m == 2:<br></td></tr
><tr
id=sl_svn139_1853

><td class="source">					print &quot;TokenMandatoryPolicy: NEW_PROCESS_MIN&quot;<br></td></tr
><tr
id=sl_svn139_1854

><td class="source">				elif m == 3:<br></td></tr
><tr
id=sl_svn139_1855

><td class="source">					print &quot;TokenMandatoryPolicy: POLICY_VALID_MASK&quot;<br></td></tr
><tr
id=sl_svn139_1856

><td class="source">				else:<br></td></tr
><tr
id=sl_svn139_1857

><td class="source">					print &quot;TokenMandatoryPolicy: %s&quot; % m<br></td></tr
><tr
id=sl_svn139_1858

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1859

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_1860

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1861

><td class="source">			print &quot;Token Resitrcted Sids: &quot; + str(win32security.GetTokenInformation(tokenh, TokenRestrictedSids))<br></td></tr
><tr
id=sl_svn139_1862

><td class="source">			print &quot;IsTokenRestricted: &quot; + str(win32security.IsTokenRestricted(tokenh))<br></td></tr
><tr
id=sl_svn139_1863

><td class="source">			print &quot;\nToken Groups: &quot;<br></td></tr
><tr
id=sl_svn139_1864

><td class="source">			for tup in win32security.GetTokenInformation(tokenh, TokenGroups):<br></td></tr
><tr
id=sl_svn139_1865

><td class="source">				sid = tup[0]<br></td></tr
><tr
id=sl_svn139_1866

><td class="source">				attr = tup[1]<br></td></tr
><tr
id=sl_svn139_1867

><td class="source">				attr_str = attr<br></td></tr
><tr
id=sl_svn139_1868

><td class="source">				if attr &lt; 0:<br></td></tr
><tr
id=sl_svn139_1869

><td class="source">					attr = 2**32 + attr<br></td></tr
><tr
id=sl_svn139_1870

><td class="source">				attr_str_a = []<br></td></tr
><tr
id=sl_svn139_1871

><td class="source">				if attr &amp; 1:<br></td></tr
><tr
id=sl_svn139_1872

><td class="source">					# attr_str_a.append(&quot;SE_GROUP_MANDATORY&quot;)<br></td></tr
><tr
id=sl_svn139_1873

><td class="source">					attr_str_a.append(&quot;MANDATORY&quot;)<br></td></tr
><tr
id=sl_svn139_1874

><td class="source">				if attr &amp; 2:<br></td></tr
><tr
id=sl_svn139_1875

><td class="source">					# attr_str_a.append(&quot;SE_GROUP_ENABLED_BY_DEFAULT&quot;)<br></td></tr
><tr
id=sl_svn139_1876

><td class="source">					attr_str_a.append(&quot;ENABLED_BY_DEFAULT&quot;)<br></td></tr
><tr
id=sl_svn139_1877

><td class="source">				if attr &amp; 4:<br></td></tr
><tr
id=sl_svn139_1878

><td class="source">					# attr_str_a.append(&quot;SE_GROUP_ENABLED&quot;)<br></td></tr
><tr
id=sl_svn139_1879

><td class="source">					attr_str_a.append(&quot;ENABLED&quot;)<br></td></tr
><tr
id=sl_svn139_1880

><td class="source">				if attr &amp; 8:<br></td></tr
><tr
id=sl_svn139_1881

><td class="source">					# attr_str_a.append(&quot;SE_GROUP_OWNER&quot;)<br></td></tr
><tr
id=sl_svn139_1882

><td class="source">					attr_str_a.append(&quot;OWNER&quot;)<br></td></tr
><tr
id=sl_svn139_1883

><td class="source">				if attr &amp; 0x40000000:<br></td></tr
><tr
id=sl_svn139_1884

><td class="source">					# attr_str_a.append(&quot;SE_GROUP_LOGON_ID&quot;)<br></td></tr
><tr
id=sl_svn139_1885

><td class="source">					attr_str_a.append(&quot;LOGON_ID&quot;)<br></td></tr
><tr
id=sl_svn139_1886

><td class="source">				attr_str = (&quot;|&quot;.join(attr_str_a))<br></td></tr
><tr
id=sl_svn139_1887

><td class="source">				try:<br></td></tr
><tr
id=sl_svn139_1888

><td class="source">					accountName, domainName, accountTypeInt = win32security.LookupAccountSid(remote_server, sid)<br></td></tr
><tr
id=sl_svn139_1889

><td class="source">					user = domainName + &quot;\\&quot; + accountName + &quot; (&quot; + win32security.ConvertSidToStringSid(sid) + &quot;)&quot;<br></td></tr
><tr
id=sl_svn139_1890

><td class="source">				except:<br></td></tr
><tr
id=sl_svn139_1891

><td class="source">					user = win32security.ConvertSidToStringSid(sid)<br></td></tr
><tr
id=sl_svn139_1892

><td class="source">				print &quot;\t%s: %s&quot; % (user, attr_str)<br></td></tr
><tr
id=sl_svn139_1893

><td class="source">			# Link that explains how privs are added / removed from tokens:<br></td></tr
><tr
id=sl_svn139_1894

><td class="source">			# http://support.microsoft.com/kb/326256<br></td></tr
><tr
id=sl_svn139_1895

><td class="source">			print &quot;\nToken Privileges:&quot;<br></td></tr
><tr
id=sl_svn139_1896

><td class="source">			privs = win32security.GetTokenInformation(tokenh, TokenPrivileges)<br></td></tr
><tr
id=sl_svn139_1897

><td class="source">			for priv_tuple in privs:<br></td></tr
><tr
id=sl_svn139_1898

><td class="source">				priv_val = priv_tuple[0]<br></td></tr
><tr
id=sl_svn139_1899

><td class="source">				attr = priv_tuple[1]<br></td></tr
><tr
id=sl_svn139_1900

><td class="source">				attr_str = &quot;unknown_attr(&quot; + str(attr) + &quot;)&quot;<br></td></tr
><tr
id=sl_svn139_1901

><td class="source">				attr_str_a = []<br></td></tr
><tr
id=sl_svn139_1902

><td class="source">				if attr == 0:<br></td></tr
><tr
id=sl_svn139_1903

><td class="source">					attr_str_a.append(&quot;[disabled but not removed]&quot;)<br></td></tr
><tr
id=sl_svn139_1904

><td class="source">				if attr &amp; 1:<br></td></tr
><tr
id=sl_svn139_1905

><td class="source">					# attr_str_a.append(&quot;SE_PRIVILEGE_ENABLED_BY_DEFAULT&quot;)<br></td></tr
><tr
id=sl_svn139_1906

><td class="source">					attr_str_a.append(&quot;ENABLED_BY_DEFAULT&quot;)<br></td></tr
><tr
id=sl_svn139_1907

><td class="source">				if attr &amp; 2:<br></td></tr
><tr
id=sl_svn139_1908

><td class="source">					# attr_str_a.append(&quot;SE_PRIVILEGE_ENABLED&quot;)<br></td></tr
><tr
id=sl_svn139_1909

><td class="source">					attr_str_a.append(&quot;ENABLED&quot;)<br></td></tr
><tr
id=sl_svn139_1910

><td class="source">				if attr &amp; 0x80000000:<br></td></tr
><tr
id=sl_svn139_1911

><td class="source">					# attr_str_a.append(&quot;SE_PRIVILEGE_USED_FOR_ACCESS&quot;)<br></td></tr
><tr
id=sl_svn139_1912

><td class="source">					attr_str_a.append(&quot;USED_FOR_ACCESS&quot;)<br></td></tr
><tr
id=sl_svn139_1913

><td class="source">				if attr &amp; 4:<br></td></tr
><tr
id=sl_svn139_1914

><td class="source">					# attr_str_a.append(&quot;SE_PRIVILEGE_REMOVED&quot;)<br></td></tr
><tr
id=sl_svn139_1915

><td class="source">					attr_str_a.append(&quot;REMOVED&quot;)<br></td></tr
><tr
id=sl_svn139_1916

><td class="source">				if attr_str_a:<br></td></tr
><tr
id=sl_svn139_1917

><td class="source">					attr_str = (&quot;|&quot;).join(attr_str_a)<br></td></tr
><tr
id=sl_svn139_1918

><td class="source">				print &quot;\t%s: %s&quot; % (win32security.LookupPrivilegeName(remote_server, priv_val), attr_str)<br></td></tr
><tr
id=sl_svn139_1919

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1920

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1921

><td class="source">			#print &quot;\nProcess ACL (buggy - probably wrong):&quot;<br></td></tr
><tr
id=sl_svn139_1922

><td class="source">			#dump_acl(pid, &#39;process&#39;, win32security.GetTokenInformation(tokenh, TokenDefaultDacl), {&#39;brief&#39;: 1}) # TODO can&#39;t understand ACL<br></td></tr
><tr
id=sl_svn139_1923

><td class="source">			# sidObj = win32security.GetTokenInformation(tokenh, TokenOwner) # Owner returns &quot;Administrators&quot; instead of SYSTEM.  It&#39;s not what we want.<br></td></tr
><tr
id=sl_svn139_1924

><td class="source">			# if sidObj:<br></td></tr
><tr
id=sl_svn139_1925

><td class="source">				# accountName, domainName, accountTypeInt = win32security.LookupAccountSid(remote_server, sidObj)<br></td></tr
><tr
id=sl_svn139_1926

><td class="source">				# print &quot;User: %s\%s (type %s)&quot; % (domainName, accountName, accountTypeInt) 				<br></td></tr
><tr
id=sl_svn139_1927

><td class="source">		if gotexe:<br></td></tr
><tr
id=sl_svn139_1928

><td class="source">			print &quot;\nFile permissions on %s:&quot; % exe<br></td></tr
><tr
id=sl_svn139_1929

><td class="source">			dump_perms(exe, &#39;file&#39;, {&#39;brief&#39;: 1})<br></td></tr
><tr
id=sl_svn139_1930

><td class="source">			print<br></td></tr
><tr
id=sl_svn139_1931

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1932

><td class="source">		if mhs and ph:	<br></td></tr
><tr
id=sl_svn139_1933

><td class="source">			for mh in mhs:<br></td></tr
><tr
id=sl_svn139_1934

><td class="source">				dll = win32process.GetModuleFileNameEx(ph, mh)<br></td></tr
><tr
id=sl_svn139_1935

><td class="source">				print &quot;Loaded module: %s&quot; % dll<br></td></tr
><tr
id=sl_svn139_1936

><td class="source">				dump_perms(dll, &#39;file&#39;, {&#39;brief&#39;: 1})<br></td></tr
><tr
id=sl_svn139_1937

><td class="source"><br></td></tr
><tr
id=sl_svn139_1938

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_1939

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1940

><td class="source">		<br></td></tr
><tr
id=sl_svn139_1941

><td class="source">def check_processes():<br></td></tr
><tr
id=sl_svn139_1942

><td class="source">	pids = win32process.EnumProcesses()<br></td></tr
><tr
id=sl_svn139_1943

><td class="source">	# TODO also check out WMI.  It might not be running, but it could help if it is:  <br></td></tr
><tr
id=sl_svn139_1944

><td class="source">	#      http://groups.google.com/group/comp.lang.python/browse_thread/thread/1f50065064173ccb<br></td></tr
><tr
id=sl_svn139_1945

><td class="source">	# TODO process explorer can find quite a lot more information than this script.  This script has several problems:<br></td></tr
><tr
id=sl_svn139_1946

><td class="source">	# TODO I can&#39;t open 64-bit processes for a 32-bit app.  I get this error:<br></td></tr
><tr
id=sl_svn139_1947

><td class="source">	# ERROR: can&#39;t open 6100: 299 EnumProcessModules, Only part of a ReadProcessMemory<br></td></tr
><tr
id=sl_svn139_1948

><td class="source">	#        or WriteProcessMemory request was completed.<br></td></tr
><tr
id=sl_svn139_1949

><td class="source">	# TODO I can&#39;t seem to get the name of elevated processes (user running as me, but with admin privs)<br></td></tr
><tr
id=sl_svn139_1950

><td class="source">	# TODO I can&#39;t get details of certain processes runnign as SYSTEM on xp (e.g. pid 4 &quot;system&quot;, csrss.exe)<br></td></tr
><tr
id=sl_svn139_1951

><td class="source">	# TODO should be able to find name (and threads?) for all processes.  Not necessarily path.<br></td></tr
><tr
id=sl_svn139_1952

><td class="source"><br></td></tr
><tr
id=sl_svn139_1953

><td class="source">	for pid in sorted(pids):<br></td></tr
><tr
id=sl_svn139_1954

><td class="source">		# TODO there&#39;s a security descriptor for each process accessible via GetSecurityInfo according to http://msdn.microsoft.com/en-us/library/ms684880%28VS.85%29.aspx<br></td></tr
><tr
id=sl_svn139_1955

><td class="source">		# TODO could we connect with PROCESS_QUERY_LIMITED_INFORMATION instead on Vista+<br></td></tr
><tr
id=sl_svn139_1956

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_1957

><td class="source">			ph = win32api.OpenProcess(win32con.PROCESS_VM_READ | win32con.PROCESS_QUERY_INFORMATION , False, pid)<br></td></tr
><tr
id=sl_svn139_1958

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_1959

><td class="source">			# print &quot;ERROR: can&#39;t connected to PID &quot; + str(pid)<br></td></tr
><tr
id=sl_svn139_1960

><td class="source">			sys.stdout.write(&quot;?&quot;)<br></td></tr
><tr
id=sl_svn139_1961

><td class="source">			continue<br></td></tr
><tr
id=sl_svn139_1962

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_1963

><td class="source">			user = &quot;unknown\\unknown&quot;<br></td></tr
><tr
id=sl_svn139_1964

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_1965

><td class="source">				tokenh = win32security.OpenProcessToken(ph, win32con.TOKEN_QUERY)<br></td></tr
><tr
id=sl_svn139_1966

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1967

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_1968

><td class="source">			else:<br></td></tr
><tr
id=sl_svn139_1969

><td class="source">				sidObj, intVal = win32security.GetTokenInformation(tokenh, TokenUser)<br></td></tr
><tr
id=sl_svn139_1970

><td class="source">				#source = win32security.GetTokenInformation(tokenh, TokenSource)<br></td></tr
><tr
id=sl_svn139_1971

><td class="source">				if sidObj:<br></td></tr
><tr
id=sl_svn139_1972

><td class="source">					accountName, domainName, accountTypeInt = win32security.LookupAccountSid(remote_server, sidObj)<br></td></tr
><tr
id=sl_svn139_1973

><td class="source">					# print &quot;pid=%d accountname=%s domainname=%s wow64=%s&quot; % (pid, accountName, domainName, win32process.IsWow64Process(ph))<br></td></tr
><tr
id=sl_svn139_1974

><td class="source">					user = domainName + &quot;\\&quot; + accountName<br></td></tr
><tr
id=sl_svn139_1975

><td class="source"><br></td></tr
><tr
id=sl_svn139_1976

><td class="source">			# print &quot;PID %d is running as %s&quot; % (pid, user)<br></td></tr
><tr
id=sl_svn139_1977

><td class="source">			sys.stdout.write(&quot;.&quot;)<br></td></tr
><tr
id=sl_svn139_1978

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_1979

><td class="source">				mhs = win32process.EnumProcessModules(ph)<br></td></tr
><tr
id=sl_svn139_1980

><td class="source">				# print mhs<br></td></tr
><tr
id=sl_svn139_1981

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_1982

><td class="source">				continue<br></td></tr
><tr
id=sl_svn139_1983

><td class="source">			<br></td></tr
><tr
id=sl_svn139_1984

><td class="source">			mhs = list(mhs)<br></td></tr
><tr
id=sl_svn139_1985

><td class="source">			exe = win32process.GetModuleFileNameEx(ph, mhs.pop(0))<br></td></tr
><tr
id=sl_svn139_1986

><td class="source">			weak_perms = check_weak_write_perms(exe, &#39;file&#39;)<br></td></tr
><tr
id=sl_svn139_1987

><td class="source">			# print_weak_perms(&quot;PID &quot; + str(pid) + &quot; running as &quot; + user + &quot;:&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_1988

><td class="source">			if weak_perms:<br></td></tr
><tr
id=sl_svn139_1989

><td class="source">				save_issue(&quot;WPC016&quot;, &quot;weak_perms_exes&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_1990

><td class="source">				sys.stdout.write(&quot;!&quot;)<br></td></tr
><tr
id=sl_svn139_1991

><td class="source">				<br></td></tr
><tr
id=sl_svn139_1992

><td class="source">			for mh in mhs:<br></td></tr
><tr
id=sl_svn139_1993

><td class="source">				# print &quot;PID %d (%s) has loaded module: %s&quot; % (pid, exe, win32process.GetModuleFileNameEx(ph, mh))<br></td></tr
><tr
id=sl_svn139_1994

><td class="source">				dll = win32process.GetModuleFileNameEx(ph, mh)<br></td></tr
><tr
id=sl_svn139_1995

><td class="source">				weak_perms = check_weak_write_perms(dll, &#39;file&#39;)<br></td></tr
><tr
id=sl_svn139_1996

><td class="source">				# print_weak_perms(&quot;DLL used by PID &quot; + str(pid) + &quot; running as &quot; + user + &quot; (&quot; + exe + &quot;):&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_1997

><td class="source">				if weak_perms:<br></td></tr
><tr
id=sl_svn139_1998

><td class="source">					save_issue(&quot;WPC016&quot;, &quot;weak_perms_dlls&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_1999

><td class="source">					sys.stdout.write(&quot;!&quot;)<br></td></tr
><tr
id=sl_svn139_2000

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2001

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2002

><td class="source">def check_services():<br></td></tr
><tr
id=sl_svn139_2003

><td class="source">	sch = win32service.OpenSCManager(remote_server, None, win32service.SC_MANAGER_ENUMERATE_SERVICE )<br></td></tr
><tr
id=sl_svn139_2004

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2005

><td class="source">		# TODO Haven&#39;t seen this work - even when running as SYSTEM<br></td></tr
><tr
id=sl_svn139_2006

><td class="source">		sd = win32service.QueryServiceObjectSecurity(sch, win32security.OWNER_SECURITY_INFORMATION | win32security.DACL_SECURITY_INFORMATION)<br></td></tr
><tr
id=sl_svn139_2007

><td class="source">		print check_weak_write_perms_by_sd(&quot;Service Manager&quot;, &#39;service_manager&#39;, sd)<br></td></tr
><tr
id=sl_svn139_2008

><td class="source">	except: <br></td></tr
><tr
id=sl_svn139_2009

><td class="source">		pass<br></td></tr
><tr
id=sl_svn139_2010

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2011

><td class="source">	# Need to connect to service (OpenService) with minimum privs to read DACL.  Here are our options:<br></td></tr
><tr
id=sl_svn139_2012

><td class="source">	#<br></td></tr
><tr
id=sl_svn139_2013

><td class="source">	# http://www.pinvoke.net/default.aspx/advapi32/OpenSCManager.html?diff=y<br></td></tr
><tr
id=sl_svn139_2014

><td class="source">	# SC_MANAGER_ALL_ACCESS (0xF003F)	Includes STANDARD_RIGHTS_REQUIRED, in addition to all access rights in this table.<br></td></tr
><tr
id=sl_svn139_2015

><td class="source">	# SC_MANAGER_CREATE_SERVICE (0x0002)	Required to call the CreateService function to create a service object and add it to the database.<br></td></tr
><tr
id=sl_svn139_2016

><td class="source">	# SC_MANAGER_CONNECT (0x0001)	Required to connect to the service control manager.<br></td></tr
><tr
id=sl_svn139_2017

><td class="source">	# SC_MANAGER_ENUMERATE_SERVICE (0x0004)	Required to call the EnumServicesStatusEx function to list the services that are in the database.<br></td></tr
><tr
id=sl_svn139_2018

><td class="source">	# SC_MANAGER_LOCK (0x0008)	Required to call the LockServiceDatabase function to acquire a lock on the database.<br></td></tr
><tr
id=sl_svn139_2019

><td class="source">	# SC_MANAGER_MODIFY_BOOT_CONFIG (0x0020)	Required to call the NotifyBootConfigStatus function.<br></td></tr
><tr
id=sl_svn139_2020

><td class="source">	# SC_MANAGER_QUERY_LOCK_STATUS (0x0010)Required to call the  QueryServiceLockStatus function to retrieve the lock status information for the database.<br></td></tr
><tr
id=sl_svn139_2021

><td class="source">	# GENERIC_READ<br></td></tr
><tr
id=sl_svn139_2022

><td class="source">	# GENERIC_WRITE<br></td></tr
><tr
id=sl_svn139_2023

><td class="source">	# GENERIC_EXECUTE<br></td></tr
><tr
id=sl_svn139_2024

><td class="source">	# GENERIC_ALL<br></td></tr
><tr
id=sl_svn139_2025

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2026

><td class="source">	services = win32service.EnumServicesStatus(sch, win32service.SERVICE_WIN32, win32service.SERVICE_STATE_ALL )<br></td></tr
><tr
id=sl_svn139_2027

><td class="source">	for service in services:<br></td></tr
><tr
id=sl_svn139_2028

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_2029

><td class="source">			sh = win32service.OpenService(sch, service[0] , win32service.SC_MANAGER_CONNECT )<br></td></tr
><tr
id=sl_svn139_2030

><td class="source">			service_info = win32service.QueryServiceConfig(sh)<br></td></tr
><tr
id=sl_svn139_2031

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_2032

><td class="source">			print &quot;WARNING: Can&#39;t open service &quot; + service[0]<br></td></tr
><tr
id=sl_svn139_2033

><td class="source">			continue<br></td></tr
><tr
id=sl_svn139_2034

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2035

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_2036

><td class="source">			sh = win32service.OpenService(sch, service[0] , win32con.GENERIC_READ )<br></td></tr
><tr
id=sl_svn139_2037

><td class="source">			sd = win32service.QueryServiceObjectSecurity(sh, win32security.OWNER_SECURITY_INFORMATION | win32security.DACL_SECURITY_INFORMATION)<br></td></tr
><tr
id=sl_svn139_2038

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_2039

><td class="source">			# print &quot;Service Perms: Unknown (Access Denied)&quot;<br></td></tr
><tr
id=sl_svn139_2040

><td class="source">			continue<br></td></tr
><tr
id=sl_svn139_2041

><td class="source"><br></td></tr
><tr
id=sl_svn139_2042

><td class="source">		weak_perms = check_weak_write_perms_by_sd(&quot;Service \&quot;&quot; + service[1] + &quot;\&quot; (&quot; + service[0] + &quot;) which runs as user \&quot;&quot; + service_info[7] + &quot;\&quot;&quot;, &#39;service&#39;, sd)<br></td></tr
><tr
id=sl_svn139_2043

><td class="source">		binary = None<br></td></tr
><tr
id=sl_svn139_2044

><td class="source">		weak_perms_binary = []<br></td></tr
><tr
id=sl_svn139_2045

><td class="source">		if not remote_server:<br></td></tr
><tr
id=sl_svn139_2046

><td class="source">			binary = get_binary(service_info[3])<br></td></tr
><tr
id=sl_svn139_2047

><td class="source">			if binary:<br></td></tr
><tr
id=sl_svn139_2048

><td class="source">				weak_perms_binary = check_weak_write_perms(binary, &#39;file&#39;)<br></td></tr
><tr
id=sl_svn139_2049

><td class="source">				<br></td></tr
><tr
id=sl_svn139_2050

><td class="source"><br></td></tr
><tr
id=sl_svn139_2051

><td class="source">		if weak_perms or weak_perms_binary:<br></td></tr
><tr
id=sl_svn139_2052

><td class="source">			vprint(&quot;---------------------------------------&quot;)<br></td></tr
><tr
id=sl_svn139_2053

><td class="source">			vprint(&quot;Service:        &quot; + service[0])<br></td></tr
><tr
id=sl_svn139_2054

><td class="source">			vprint(&quot;Description:    &quot; + service[1])<br></td></tr
><tr
id=sl_svn139_2055

><td class="source">			vprint(&quot;Binary:         &quot; + service_info[3])<br></td></tr
><tr
id=sl_svn139_2056

><td class="source">			if binary:<br></td></tr
><tr
id=sl_svn139_2057

><td class="source">				vprint(&quot;Binary (clean): &quot; + binary)<br></td></tr
><tr
id=sl_svn139_2058

><td class="source">			else:<br></td></tr
><tr
id=sl_svn139_2059

><td class="source">				vprint(&quot;Binary (clean): [Missing Binary]&quot;)<br></td></tr
><tr
id=sl_svn139_2060

><td class="source">			vprint(&quot;Run as:         &quot; + service_info[7])<br></td></tr
><tr
id=sl_svn139_2061

><td class="source">			vprint(&quot;Weak Perms: &quot;)<br></td></tr
><tr
id=sl_svn139_2062

><td class="source">			# service_info = win32service.QueryServiceConfig2(sh, win32service.SERVICE_CONFIG_DESCRIPTION) # long description of service.  not interesting.<br></td></tr
><tr
id=sl_svn139_2063

><td class="source">			# print &quot;Service Perms: &quot; + win32security.ConvertSecurityDescriptorToStringSecurityDescriptor(sd, win32security.SDDL_REVISION_1, 	win32security.DACL_SECURITY_INFORMATION)<br></td></tr
><tr
id=sl_svn139_2064

><td class="source">			print_weak_perms(&quot;file&quot;, weak_perms_binary)<br></td></tr
><tr
id=sl_svn139_2065

><td class="source">			if weak_perms_binary:<br></td></tr
><tr
id=sl_svn139_2066

><td class="source">				save_issue(&quot;WPC004&quot;, &quot;writable_progs&quot;, weak_perms_binary)<br></td></tr
><tr
id=sl_svn139_2067

><td class="source">					<br></td></tr
><tr
id=sl_svn139_2068

><td class="source">		print_weak_perms(&quot;service&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_2069

><td class="source">		if weak_perms:<br></td></tr
><tr
id=sl_svn139_2070

><td class="source">			save_issue(&quot;WPC012&quot;, &quot;weak_service_perms&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_2071

><td class="source">			if verbose == 0:<br></td></tr
><tr
id=sl_svn139_2072

><td class="source">				sys.stdout.write(&quot;!&quot;)<br></td></tr
><tr
id=sl_svn139_2073

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_2074

><td class="source">			if verbose == 0:<br></td></tr
><tr
id=sl_svn139_2075

><td class="source">				sys.stdout.write(&quot;.&quot;)<br></td></tr
><tr
id=sl_svn139_2076

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2077

><td class="source"><br></td></tr
><tr
id=sl_svn139_2078

><td class="source">def audit_services():<br></td></tr
><tr
id=sl_svn139_2079

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2080

><td class="source">	sch = win32service.OpenSCManager(remote_server, None, win32service.SC_MANAGER_ENUMERATE_SERVICE )<br></td></tr
><tr
id=sl_svn139_2081

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2082

><td class="source">		# TODO Haven&#39;t seen this work - even when running as SYSTEM<br></td></tr
><tr
id=sl_svn139_2083

><td class="source">		sd = win32service.QueryServiceObjectSecurity(sch, win32security.OWNER_SECURITY_INFORMATION | win32security.DACL_SECURITY_INFORMATION)<br></td></tr
><tr
id=sl_svn139_2084

><td class="source">		print check_weak_write_perms_by_sd(&quot;Service Manager&quot;, &#39;service_manager&#39;, sd)<br></td></tr
><tr
id=sl_svn139_2085

><td class="source">	except: <br></td></tr
><tr
id=sl_svn139_2086

><td class="source">		#print &quot;ERROR: Can&#39;t get security descriptor for service manager&quot;<br></td></tr
><tr
id=sl_svn139_2087

><td class="source">		pass<br></td></tr
><tr
id=sl_svn139_2088

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2089

><td class="source">	# Need to connect to service (OpenService) with minimum privs to read DACL.  Here are our options:<br></td></tr
><tr
id=sl_svn139_2090

><td class="source">	#<br></td></tr
><tr
id=sl_svn139_2091

><td class="source">	# http://www.pinvoke.net/default.aspx/advapi32/OpenSCManager.html?diff=y<br></td></tr
><tr
id=sl_svn139_2092

><td class="source">	# SC_MANAGER_ALL_ACCESS (0xF003F)	Includes STANDARD_RIGHTS_REQUIRED, in addition to all access rights in this table.<br></td></tr
><tr
id=sl_svn139_2093

><td class="source">	# SC_MANAGER_CREATE_SERVICE (0x0002)	Required to call the CreateService function to create a service object and add it to the database.<br></td></tr
><tr
id=sl_svn139_2094

><td class="source">	# SC_MANAGER_CONNECT (0x0001)	Required to connect to the service control manager.<br></td></tr
><tr
id=sl_svn139_2095

><td class="source">	# SC_MANAGER_ENUMERATE_SERVICE (0x0004)	Required to call the EnumServicesStatusEx function to list the services that are in the database.<br></td></tr
><tr
id=sl_svn139_2096

><td class="source">	# SC_MANAGER_LOCK (0x0008)	Required to call the LockServiceDatabase function to acquire a lock on the database.<br></td></tr
><tr
id=sl_svn139_2097

><td class="source">	# SC_MANAGER_MODIFY_BOOT_CONFIG (0x0020)	Required to call the NotifyBootConfigStatus function.<br></td></tr
><tr
id=sl_svn139_2098

><td class="source">	# SC_MANAGER_QUERY_LOCK_STATUS (0x0010)Required to call the  QueryServiceLockStatus function to retrieve the lock status information for the database.<br></td></tr
><tr
id=sl_svn139_2099

><td class="source">	# GENERIC_READ<br></td></tr
><tr
id=sl_svn139_2100

><td class="source">	# GENERIC_WRITE<br></td></tr
><tr
id=sl_svn139_2101

><td class="source">	# GENERIC_EXECUTE<br></td></tr
><tr
id=sl_svn139_2102

><td class="source">	# GENERIC_ALL<br></td></tr
><tr
id=sl_svn139_2103

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2104

><td class="source">	services = win32service.EnumServicesStatus(sch, win32service.SERVICE_WIN32, win32service.SERVICE_STATE_ALL )<br></td></tr
><tr
id=sl_svn139_2105

><td class="source">	for service in services:<br></td></tr
><tr
id=sl_svn139_2106

><td class="source">		sh = win32service.OpenService(sch, service[0] , win32service.SC_MANAGER_CONNECT )<br></td></tr
><tr
id=sl_svn139_2107

><td class="source">		service_info = win32service.QueryServiceConfig(sh)<br></td></tr
><tr
id=sl_svn139_2108

><td class="source">		binary = None<br></td></tr
><tr
id=sl_svn139_2109

><td class="source">		if remote_server:<br></td></tr
><tr
id=sl_svn139_2110

><td class="source">			print &quot;WARNING: Running agianst remote server.  Checking perms of .exe not implemented.&quot;<br></td></tr
><tr
id=sl_svn139_2111

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_2112

><td class="source">			binary = get_binary(service_info[3])<br></td></tr
><tr
id=sl_svn139_2113

><td class="source">		print &quot;---------------------------------------------------------------&quot;<br></td></tr
><tr
id=sl_svn139_2114

><td class="source">		print(&quot;Service:        &quot; + service[0])<br></td></tr
><tr
id=sl_svn139_2115

><td class="source">		print(&quot;Description:    &quot; + service[1])<br></td></tr
><tr
id=sl_svn139_2116

><td class="source">		print(&quot;Binary:         &quot; + service_info[3])<br></td></tr
><tr
id=sl_svn139_2117

><td class="source">		if binary:<br></td></tr
><tr
id=sl_svn139_2118

><td class="source">			print(&quot;Binary (clean): &quot; + binary)<br></td></tr
><tr
id=sl_svn139_2119

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_2120

><td class="source">			if remote_server:<br></td></tr
><tr
id=sl_svn139_2121

><td class="source">				print(&quot;Binary (clean): [N/A Running remotely]&quot;)<br></td></tr
><tr
id=sl_svn139_2122

><td class="source">			else:<br></td></tr
><tr
id=sl_svn139_2123

><td class="source">				print(&quot;Binary (clean): [Missing Binary/Remote]&quot;)<br></td></tr
><tr
id=sl_svn139_2124

><td class="source">		print(&quot;Run as:         &quot; + service_info[7])<br></td></tr
><tr
id=sl_svn139_2125

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2126

><td class="source">		print &quot;\nFile Permissions on executable %s:&quot; % binary<br></td></tr
><tr
id=sl_svn139_2127

><td class="source">		if binary:<br></td></tr
><tr
id=sl_svn139_2128

><td class="source">			dump_perms(binary, &#39;file&#39;, {&#39;brief&#39;: 1})<br></td></tr
><tr
id=sl_svn139_2129

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_2130

><td class="source">			print &quot;WARNING: Can&#39;t get full path of binary.  Skipping.&quot;<br></td></tr
><tr
id=sl_svn139_2131

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2132

><td class="source">		print &quot;\nPermissions on service:&quot;<br></td></tr
><tr
id=sl_svn139_2133

><td class="source"><br></td></tr
><tr
id=sl_svn139_2134

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_2135

><td class="source">			sh = win32service.OpenService(sch, service[0] , win32con.GENERIC_READ )<br></td></tr
><tr
id=sl_svn139_2136

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_2137

><td class="source">			print &quot;ERROR: OpenService failed&quot;<br></td></tr
><tr
id=sl_svn139_2138

><td class="source"><br></td></tr
><tr
id=sl_svn139_2139

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_2140

><td class="source">			sd = win32service.QueryServiceObjectSecurity(sh, win32security.OWNER_SECURITY_INFORMATION | win32security.DACL_SECURITY_INFORMATION)<br></td></tr
><tr
id=sl_svn139_2141

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_2142

><td class="source">			print &quot;ERROR: QueryServiceObjectSecurity didn&#39;t get security descriptor for service&quot;<br></td></tr
><tr
id=sl_svn139_2143

><td class="source"><br></td></tr
><tr
id=sl_svn139_2144

><td class="source">		dump_sd(&quot;Service \&quot;&quot; + service[1] + &quot;\&quot; (&quot; + service[0] + &quot;) which runs as user \&quot;&quot; + service_info[7] + &quot;\&quot;&quot;, &#39;service&#39;, sd, {&#39;brief&#39;: 1})<br></td></tr
><tr
id=sl_svn139_2145

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2146

><td class="source">		print &quot;\nPermissions on registry data:&quot;<br></td></tr
><tr
id=sl_svn139_2147

><td class="source">		print &quot;WARNING: Not implmented yet&quot;<br></td></tr
><tr
id=sl_svn139_2148

><td class="source">		# service_info = win32service.QueryServiceConfig2(sh, win32service.SERVICE_CONFIG_DESCRIPTION) # long description of service.  not interesting.<br></td></tr
><tr
id=sl_svn139_2149

><td class="source">		# print &quot;Service Perms: &quot; + win32security.ConvertSecurityDescriptorToStringSecurityDescriptor(sd, win32security.SDDL_REVISION_1, win32security.DACL_SECURITY_INFORMATION)					<br></td></tr
><tr
id=sl_svn139_2150

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2151

><td class="source"><br></td></tr
><tr
id=sl_svn139_2152

><td class="source">def vprint(string):<br></td></tr
><tr
id=sl_svn139_2153

><td class="source">	if (verbose):<br></td></tr
><tr
id=sl_svn139_2154

><td class="source">		print string<br></td></tr
><tr
id=sl_svn139_2155

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2156

><td class="source">def get_binary(binary_dirty):<br></td></tr
><tr
id=sl_svn139_2157

><td class="source">	m = re.search(&#39;^[\s]*?&quot;([^&quot;]+)&quot;&#39;, binary_dirty)<br></td></tr
><tr
id=sl_svn139_2158

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2159

><td class="source">	if m and os.path.exists(m.group(1)):<br></td></tr
><tr
id=sl_svn139_2160

><td class="source">		return m.group(1)<br></td></tr
><tr
id=sl_svn139_2161

><td class="source">	else:<br></td></tr
><tr
id=sl_svn139_2162

><td class="source">		if m:<br></td></tr
><tr
id=sl_svn139_2163

><td class="source">			binary_dirty = m.group(1)<br></td></tr
><tr
id=sl_svn139_2164

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2165

><td class="source">	chunks = binary_dirty.split(&quot; &quot;)<br></td></tr
><tr
id=sl_svn139_2166

><td class="source">	candidate = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_2167

><td class="source">	for chunk in chunks:<br></td></tr
><tr
id=sl_svn139_2168

><td class="source">		if candidate:<br></td></tr
><tr
id=sl_svn139_2169

><td class="source">			candidate = candidate + &quot; &quot;<br></td></tr
><tr
id=sl_svn139_2170

><td class="source">		candidate = candidate + chunk<br></td></tr
><tr
id=sl_svn139_2171

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2172

><td class="source">		if os.path.exists(candidate) and os.path.isfile(candidate):<br></td></tr
><tr
id=sl_svn139_2173

><td class="source">			return candidate<br></td></tr
><tr
id=sl_svn139_2174

><td class="source">		if os.path.exists(candidate + &quot;.exe&quot;) and os.path.isfile(candidate + &quot;.exe&quot;):<br></td></tr
><tr
id=sl_svn139_2175

><td class="source">			return candidate + &quot;.exe&quot;<br></td></tr
><tr
id=sl_svn139_2176

><td class="source">		global on64bitwindows<br></td></tr
><tr
id=sl_svn139_2177

><td class="source">		if on64bitwindows:<br></td></tr
><tr
id=sl_svn139_2178

><td class="source">			candidate2 = candidate.replace(&quot;system32&quot;, &quot;syswow64&quot;)<br></td></tr
><tr
id=sl_svn139_2179

><td class="source">			if os.path.exists(candidate2) and os.path.isfile(candidate2):<br></td></tr
><tr
id=sl_svn139_2180

><td class="source">				return candidate2<br></td></tr
><tr
id=sl_svn139_2181

><td class="source">			if os.path.exists(candidate2 + &quot;.exe&quot;) and os.path.isfile(candidate2 + &quot;.exe&quot;):<br></td></tr
><tr
id=sl_svn139_2182

><td class="source">				return candidate2 + &quot;.exe&quot;<br></td></tr
><tr
id=sl_svn139_2183

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2184

><td class="source">	return None<br></td></tr
><tr
id=sl_svn139_2185

><td class="source"><br></td></tr
><tr
id=sl_svn139_2186

><td class="source">def print_weak_perms(type, weak_perms, options={}):<br></td></tr
><tr
id=sl_svn139_2187

><td class="source">	brief = 0<br></td></tr
><tr
id=sl_svn139_2188

><td class="source">	if options:<br></td></tr
><tr
id=sl_svn139_2189

><td class="source">		if options[&#39;brief&#39;]:<br></td></tr
><tr
id=sl_svn139_2190

><td class="source">			brief = 1<br></td></tr
><tr
id=sl_svn139_2191

><td class="source">	for perms in weak_perms:<br></td></tr
><tr
id=sl_svn139_2192

><td class="source">		object_name = perms[0]	<br></td></tr
><tr
id=sl_svn139_2193

><td class="source">		domain = perms[1]<br></td></tr
><tr
id=sl_svn139_2194

><td class="source">		principle = perms[2]<br></td></tr
><tr
id=sl_svn139_2195

><td class="source">		perm = perms[3]<br></td></tr
><tr
id=sl_svn139_2196

><td class="source">		if len(perms) == 5:<br></td></tr
><tr
id=sl_svn139_2197

><td class="source">			acl_type = perms[4]<br></td></tr
><tr
id=sl_svn139_2198

><td class="source">			if acl_type == &quot;ALLOW&quot;:<br></td></tr
><tr
id=sl_svn139_2199

><td class="source">				acl_type = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_2200

><td class="source">			else:<br></td></tr
><tr
id=sl_svn139_2201

><td class="source">				acl_type = acl_type + &quot; &quot;<br></td></tr
><tr
id=sl_svn139_2202

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_2203

><td class="source">			acl_type = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_2204

><td class="source">		slash = &quot;\\&quot;<br></td></tr
><tr
id=sl_svn139_2205

><td class="source">		if domain == &quot;&quot;:<br></td></tr
><tr
id=sl_svn139_2206

><td class="source">			slash = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_2207

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2208

><td class="source">		if brief:<br></td></tr
><tr
id=sl_svn139_2209

><td class="source">			print &quot;\t%s%s%s%s: %s&quot; % (acl_type, domain, slash, principle, perm)<br></td></tr
><tr
id=sl_svn139_2210

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_2211

><td class="source">			print &quot;\t%s%s%s%s has permission %s on %s %s&quot; % (acl_type, domain, slash, principle, perm, type, object_name)<br></td></tr
><tr
id=sl_svn139_2212

><td class="source">			<br></td></tr
><tr
id=sl_svn139_2213

><td class="source">def check_path(path, issue_no):<br></td></tr
><tr
id=sl_svn139_2214

><td class="source">	dirs = set(path.split(&#39;;&#39;))<br></td></tr
><tr
id=sl_svn139_2215

><td class="source">	exts = (&#39;exe&#39;, &#39;com&#39;, &#39;bat&#39;, &#39;dll&#39;) # TODO pl, rb, py, php, inc, asp, aspx, ocx, vbs, more?<br></td></tr
><tr
id=sl_svn139_2216

><td class="source">	for dir in dirs:<br></td></tr
><tr
id=sl_svn139_2217

><td class="source">		weak_flag = 0<br></td></tr
><tr
id=sl_svn139_2218

><td class="source">		weak_perms = check_weak_write_perms(dir, &#39;directory&#39;)<br></td></tr
><tr
id=sl_svn139_2219

><td class="source">		if weak_perms:<br></td></tr
><tr
id=sl_svn139_2220

><td class="source">			save_issue(issue_no, &quot;weak_perms_dir&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_2221

><td class="source">			print_weak_perms(&quot;Directory&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_2222

><td class="source">			weak_flag = 1<br></td></tr
><tr
id=sl_svn139_2223

><td class="source">		for ext in exts:<br></td></tr
><tr
id=sl_svn139_2224

><td class="source">			for file in glob.glob(dir + &#39;\*.&#39; + ext):<br></td></tr
><tr
id=sl_svn139_2225

><td class="source">				#print &quot;Processing &quot; + file<br></td></tr
><tr
id=sl_svn139_2226

><td class="source">				weak_perms = check_weak_write_perms(file, &#39;file&#39;)<br></td></tr
><tr
id=sl_svn139_2227

><td class="source">				if weak_perms:<br></td></tr
><tr
id=sl_svn139_2228

><td class="source">					save_issue(issue_no, &quot;weak_perms_exe&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_2229

><td class="source">					print_weak_perms(&quot;File&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_2230

><td class="source">					weak_flag = 1<br></td></tr
><tr
id=sl_svn139_2231

><td class="source">		if weak_flag == 1:<br></td></tr
><tr
id=sl_svn139_2232

><td class="source">			sys.stdout.write(&quot;!&quot;)<br></td></tr
><tr
id=sl_svn139_2233

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_2234

><td class="source">			sys.stdout.write(&quot;.&quot;)<br></td></tr
><tr
id=sl_svn139_2235

><td class="source"><br></td></tr
><tr
id=sl_svn139_2236

><td class="source">def get_user_paths():<br></td></tr
><tr
id=sl_svn139_2237

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2238

><td class="source">		keyh = win32api.RegOpenKeyEx(win32con.HKEY_USERS, None , 0, win32con.KEY_ENUMERATE_SUB_KEYS | win32con.KEY_QUERY_VALUE | win32con.KEY_READ)<br></td></tr
><tr
id=sl_svn139_2239

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_2240

><td class="source">		return 0<br></td></tr
><tr
id=sl_svn139_2241

><td class="source">	paths = []<br></td></tr
><tr
id=sl_svn139_2242

><td class="source">	subkeys = win32api.RegEnumKeyEx(keyh)<br></td></tr
><tr
id=sl_svn139_2243

><td class="source">	for subkey in subkeys:<br></td></tr
><tr
id=sl_svn139_2244

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_2245

><td class="source">			subkeyh = win32api.RegOpenKeyEx(keyh, subkey[0] + &quot;\\Environment&quot; , 0, win32con.KEY_ENUMERATE_SUB_KEYS | win32con.KEY_QUERY_VALUE | win32con.KEY_READ)<br></td></tr
><tr
id=sl_svn139_2246

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_2247

><td class="source">			pass<br></td></tr
><tr
id=sl_svn139_2248

><td class="source">		else:<br></td></tr
><tr
id=sl_svn139_2249

><td class="source">			subkey_count, value_count, mod_time = win32api.RegQueryInfoKey(subkeyh)<br></td></tr
><tr
id=sl_svn139_2250

><td class="source">			<br></td></tr
><tr
id=sl_svn139_2251

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_2252

><td class="source">				path, type = win32api.RegQueryValueEx(subkeyh, &quot;PATH&quot;)<br></td></tr
><tr
id=sl_svn139_2253

><td class="source">				paths.append((subkey[0], path))<br></td></tr
><tr
id=sl_svn139_2254

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_2255

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_2256

><td class="source">	return paths<br></td></tr
><tr
id=sl_svn139_2257

><td class="source"><br></td></tr
><tr
id=sl_svn139_2258

><td class="source">def get_system_path():<br></td></tr
><tr
id=sl_svn139_2259

><td class="source">	# HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment<br></td></tr
><tr
id=sl_svn139_2260

><td class="source">	key_string = &#39;SYSTEM\CurrentControlSet\Control\Session Manager\Environment&#39;<br></td></tr
><tr
id=sl_svn139_2261

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2262

><td class="source">		keyh = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, key_string , 0, win32con.KEY_ENUMERATE_SUB_KEYS | win32con.KEY_QUERY_VALUE | win32con.KEY_READ)<br></td></tr
><tr
id=sl_svn139_2263

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_2264

><td class="source">		return None<br></td></tr
><tr
id=sl_svn139_2265

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2266

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2267

><td class="source">		path, type = win32api.RegQueryValueEx(keyh, &quot;PATH&quot;)<br></td></tr
><tr
id=sl_svn139_2268

><td class="source">		return path<br></td></tr
><tr
id=sl_svn139_2269

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_2270

><td class="source">		return None<br></td></tr
><tr
id=sl_svn139_2271

><td class="source">				<br></td></tr
><tr
id=sl_svn139_2272

><td class="source">#name=sys.argv[1]<br></td></tr
><tr
id=sl_svn139_2273

><td class="source">#if not os.path.exists(name):<br></td></tr
><tr
id=sl_svn139_2274

><td class="source">	#print name, &quot;does not exist!&quot;<br></td></tr
><tr
id=sl_svn139_2275

><td class="source">	#sys.exit()<br></td></tr
><tr
id=sl_svn139_2276

><td class="source"><br></td></tr
><tr
id=sl_svn139_2277

><td class="source"><br></td></tr
><tr
id=sl_svn139_2278

><td class="source">def check_user_paths():<br></td></tr
><tr
id=sl_svn139_2279

><td class="source">	for user_path in get_user_paths():<br></td></tr
><tr
id=sl_svn139_2280

><td class="source">		user_sid_s = user_path[0]<br></td></tr
><tr
id=sl_svn139_2281

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_2282

><td class="source">			user_sid  = win32security.ConvertStringSidToSid(user_sid_s)<br></td></tr
><tr
id=sl_svn139_2283

><td class="source">			principle, domain, type = win32security.LookupAccountSid(remote_server, user_sid)<br></td></tr
><tr
id=sl_svn139_2284

><td class="source">			user_fq = domain + &quot;\\&quot; + principle<br></td></tr
><tr
id=sl_svn139_2285

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_2286

><td class="source">			print &quot;WARNING: Can&#39;t convert sid %s to name.  Skipping.&quot; % user_sid_s<br></td></tr
><tr
id=sl_svn139_2287

><td class="source">			continue<br></td></tr
><tr
id=sl_svn139_2288

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2289

><td class="source">		path = user_path[1]<br></td></tr
><tr
id=sl_svn139_2290

><td class="source">		vprint(&quot;Checking path of %s&quot; % user_fq)<br></td></tr
><tr
id=sl_svn139_2291

><td class="source">		global tmp_trusted_principles_fq<br></td></tr
><tr
id=sl_svn139_2292

><td class="source">		tmp_trusted_principles_fq = (user_fq)<br></td></tr
><tr
id=sl_svn139_2293

><td class="source">		check_path(path, &quot;WPC015&quot;)<br></td></tr
><tr
id=sl_svn139_2294

><td class="source">		tmp_trusted_principles_fq = ()<br></td></tr
><tr
id=sl_svn139_2295

><td class="source"><br></td></tr
><tr
id=sl_svn139_2296

><td class="source">def check_current_path():<br></td></tr
><tr
id=sl_svn139_2297

><td class="source">	vprint(&quot;Checking current user&#39;s PATH&quot;)<br></td></tr
><tr
id=sl_svn139_2298

><td class="source">	global tmp_trusted_principles_fq<br></td></tr
><tr
id=sl_svn139_2299

><td class="source">	tmp_trusted_principles_fq = (os.environ[&#39;userdomain&#39;] + &quot;\\&quot; + os.environ[&#39;username&#39;])	<br></td></tr
><tr
id=sl_svn139_2300

><td class="source">	check_path(os.environ[&#39;path&#39;], &quot;WPC014&quot;)<br></td></tr
><tr
id=sl_svn139_2301

><td class="source">	tmp_trusted_principles_fq = ()<br></td></tr
><tr
id=sl_svn139_2302

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2303

><td class="source">def check_system_path():<br></td></tr
><tr
id=sl_svn139_2304

><td class="source">	vprint(&quot;Checking system PATH&quot;)<br></td></tr
><tr
id=sl_svn139_2305

><td class="source">	check_path(get_system_path(), &quot;WPC013&quot;)<br></td></tr
><tr
id=sl_svn139_2306

><td class="source"><br></td></tr
><tr
id=sl_svn139_2307

><td class="source">def check_paths():<br></td></tr
><tr
id=sl_svn139_2308

><td class="source">	check_system_path()<br></td></tr
><tr
id=sl_svn139_2309

><td class="source">	check_current_path()<br></td></tr
><tr
id=sl_svn139_2310

><td class="source">	check_user_paths()<br></td></tr
><tr
id=sl_svn139_2311

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2312

><td class="source"><br></td></tr
><tr
id=sl_svn139_2313

><td class="source">def check_drives():<br></td></tr
><tr
id=sl_svn139_2314

><td class="source">	for drive in win32api.GetLogicalDriveStrings().split(&quot;\x00&quot;):<br></td></tr
><tr
id=sl_svn139_2315

><td class="source">		sys.stdout.write(&quot;.&quot;)<br></td></tr
><tr
id=sl_svn139_2316

><td class="source">		type = win32file.GetDriveType(drive)<br></td></tr
><tr
id=sl_svn139_2317

><td class="source">		if type == win32con.DRIVE_FIXED:<br></td></tr
><tr
id=sl_svn139_2318

><td class="source">			fs = win32api.GetVolumeInformation(drive)[4]<br></td></tr
><tr
id=sl_svn139_2319

><td class="source">			if fs == &#39;NTFS&#39;:<br></td></tr
><tr
id=sl_svn139_2320

><td class="source">				warning = &quot;&quot;<br></td></tr
><tr
id=sl_svn139_2321

><td class="source">				weak_perms = check_weak_write_perms(drive, &#39;directory&#39;)<br></td></tr
><tr
id=sl_svn139_2322

><td class="source">				if weak_perms:<br></td></tr
><tr
id=sl_svn139_2323

><td class="source">					# print &quot;Weak permissions on drive root %s:&quot; % drive<br></td></tr
><tr
id=sl_svn139_2324

><td class="source">					# print_weak_perms(&#39;directory&#39;, weak_perms)<br></td></tr
><tr
id=sl_svn139_2325

><td class="source">					sys.stdout.write(&quot;.&quot;)<br></td></tr
><tr
id=sl_svn139_2326

><td class="source">					save_issue(&quot;WPC010&quot;, &quot;writable_drive_root&quot;, weak_perms) <br></td></tr
><tr
id=sl_svn139_2327

><td class="source">			elif fs == &#39;FAT&#39;:<br></td></tr
><tr
id=sl_svn139_2328

><td class="source">				save_issue_string(&quot;WPC011&quot;, &quot;fat_fs_drives&quot;, &quot;Fixed drive &quot; + drive + &quot;: has &quot; + fs + &quot; filesystem (FAT does not support file permissions)&quot; )<br></td></tr
><tr
id=sl_svn139_2329

><td class="source">				sys.stdout.write(&quot;!&quot;)<br></td></tr
><tr
id=sl_svn139_2330

><td class="source">			elif fs == &#39;FAT32&#39;:<br></td></tr
><tr
id=sl_svn139_2331

><td class="source">				save_issue_string(&quot;WPC011&quot;, &quot;fat_fs_drives&quot;, &quot;Fixed drive &quot; + drive + &quot;: has &quot; + fs + &quot; filesystem  (FAT32 does not support file permissions)&quot; )<br></td></tr
><tr
id=sl_svn139_2332

><td class="source">				sys.stdout.write(&quot;!&quot;)<br></td></tr
><tr
id=sl_svn139_2333

><td class="source">			else:<br></td></tr
><tr
id=sl_svn139_2334

><td class="source">				warning = &quot; (not NTFS - might be insecure)&quot;<br></td></tr
><tr
id=sl_svn139_2335

><td class="source">				save_issue_string(&quot;WPC011&quot;, &quot;fat_fs_drives&quot;, &quot;Fixed drive &quot; + drive + &quot;: has &quot; + fs + &quot; filesystem (Not NTFS - might not be secure)&quot; )<br></td></tr
><tr
id=sl_svn139_2336

><td class="source">				sys.stdout.write(&quot;!&quot;)<br></td></tr
><tr
id=sl_svn139_2337

><td class="source"><br></td></tr
><tr
id=sl_svn139_2338

><td class="source">				 <br></td></tr
><tr
id=sl_svn139_2339

><td class="source">			# print &quot;Fixed drive %s has %s filesystem%s&quot; % (drive, fs, warning)<br></td></tr
><tr
id=sl_svn139_2340

><td class="source">			<br></td></tr
><tr
id=sl_svn139_2341

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2342

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2343

><td class="source">def check_shares():<br></td></tr
><tr
id=sl_svn139_2344

><td class="source">	resume = 0;<br></td></tr
><tr
id=sl_svn139_2345

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2346

><td class="source">		(sharelist, total, resume) = win32net.NetShareEnum(None, 502, resume, 9999)<br></td></tr
><tr
id=sl_svn139_2347

><td class="source">		for share in sharelist:<br></td></tr
><tr
id=sl_svn139_2348

><td class="source">			sys.stdout.write(&quot;.&quot;)<br></td></tr
><tr
id=sl_svn139_2349

><td class="source">			sd = share[&#39;security_descriptor&#39;]<br></td></tr
><tr
id=sl_svn139_2350

><td class="source">			# print &quot;%s (%s) %s type=%s&quot; % (share[&#39;netname&#39;], share[&#39;path&#39;], share[&#39;remark&#39;], share[&#39;type&#39;])<br></td></tr
><tr
id=sl_svn139_2351

><td class="source">			if sd:<br></td></tr
><tr
id=sl_svn139_2352

><td class="source">				weak_perms = check_weak_write_perms_by_sd(&quot;Share \&quot;&quot; + share[&#39;netname&#39;] + &quot;\&quot; (&quot; + share[&#39;path&#39;] + &quot;) &quot;, &#39;share&#39;, sd)<br></td></tr
><tr
id=sl_svn139_2353

><td class="source">				if weak_perms:<br></td></tr
><tr
id=sl_svn139_2354

><td class="source">					save_issue(&quot;WPC017&quot;, &quot;non_admin_shares&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_2355

><td class="source">					sys.stdout.write(&quot;!&quot;)<br></td></tr
><tr
id=sl_svn139_2356

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_2357

><td class="source">		print &quot;[E] Can&#39;t check shares - not enough privs?&quot;<br></td></tr
><tr
id=sl_svn139_2358

><td class="source"><br></td></tr
><tr
id=sl_svn139_2359

><td class="source"># TODO not option to call this yet<br></td></tr
><tr
id=sl_svn139_2360

><td class="source">def audit_shares():	<br></td></tr
><tr
id=sl_svn139_2361

><td class="source">	print <br></td></tr
><tr
id=sl_svn139_2362

><td class="source">	print &quot;[+] Shares&quot;<br></td></tr
><tr
id=sl_svn139_2363

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2364

><td class="source"><br></td></tr
><tr
id=sl_svn139_2365

><td class="source">	resume = 0;<br></td></tr
><tr
id=sl_svn139_2366

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2367

><td class="source">		(sharelist, total, resume) = win32net.NetShareEnum(remote_server, 502, resume, 999999)<br></td></tr
><tr
id=sl_svn139_2368

><td class="source">		#print win32net.NetShareGetInfo(remote_server, ?, 0) # do we need this?<br></td></tr
><tr
id=sl_svn139_2369

><td class="source"><br></td></tr
><tr
id=sl_svn139_2370

><td class="source">		for share in sharelist:<br></td></tr
><tr
id=sl_svn139_2371

><td class="source">			# Determine type of share<br></td></tr
><tr
id=sl_svn139_2372

><td class="source">			types = []<br></td></tr
><tr
id=sl_svn139_2373

><td class="source">			if share[&#39;type&#39;] &amp; getattr(win32netcon, &quot;STYPE_SPECIAL&quot;):<br></td></tr
><tr
id=sl_svn139_2374

><td class="source">				# print &quot;Share type: &quot;<br></td></tr
><tr
id=sl_svn139_2375

><td class="source">				types.append(&quot;STYPE_SPECIAL&quot;)<br></td></tr
><tr
id=sl_svn139_2376

><td class="source">			share[&#39;type&#39;] = share[&#39;type&#39;] &amp; 3 # mask off &quot;special&quot;<br></td></tr
><tr
id=sl_svn139_2377

><td class="source">			#print share[&#39;type&#39;]<br></td></tr
><tr
id=sl_svn139_2378

><td class="source">			for stype in share_types:<br></td></tr
><tr
id=sl_svn139_2379

><td class="source">				if share[&#39;type&#39;] == getattr(win32netcon, stype):<br></td></tr
><tr
id=sl_svn139_2380

><td class="source">					types.append(stype)<br></td></tr
><tr
id=sl_svn139_2381

><td class="source">					#print &quot;Share type: &quot; + stype<br></td></tr
><tr
id=sl_svn139_2382

><td class="source">					break<br></td></tr
><tr
id=sl_svn139_2383

><td class="source">			print &quot;---------------&quot;<br></td></tr
><tr
id=sl_svn139_2384

><td class="source">			print &quot;Share:        &quot; + share[&#39;netname&#39;]<br></td></tr
><tr
id=sl_svn139_2385

><td class="source">			print &quot;Path:         &quot; + share[&#39;path&#39;]<br></td></tr
><tr
id=sl_svn139_2386

><td class="source">			print &quot;Remark:       &quot; + share[&#39;remark&#39;]<br></td></tr
><tr
id=sl_svn139_2387

><td class="source">			print &quot;Type(s):      &quot; + &quot;|&quot;.join(types)<br></td></tr
><tr
id=sl_svn139_2388

><td class="source">			print &quot;Reserved:     %s&quot; % share[&#39;reserved&#39;]<br></td></tr
><tr
id=sl_svn139_2389

><td class="source">			print &quot;Passwd:       %s&quot; % share[&#39;passwd&#39;]<br></td></tr
><tr
id=sl_svn139_2390

><td class="source">			print &quot;Current Uses: %s&quot; % share[&#39;current_uses&#39;]<br></td></tr
><tr
id=sl_svn139_2391

><td class="source">			print &quot;Max Uses:     %s&quot; % share[&#39;max_uses&#39;]<br></td></tr
><tr
id=sl_svn139_2392

><td class="source">			print &quot;Permissions:  %s&quot; % share[&#39;permissions&#39;]<br></td></tr
><tr
id=sl_svn139_2393

><td class="source">			print &quot;Sec. Desc.:   &quot; <br></td></tr
><tr
id=sl_svn139_2394

><td class="source">			dump_sd(share[&#39;netname&#39;], &#39;share&#39;, share[&#39;security_descriptor&#39;])<br></td></tr
><tr
id=sl_svn139_2395

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_2396

><td class="source">		print &quot;[E] Couldn&#39;t get share information&quot;<br></td></tr
><tr
id=sl_svn139_2397

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2398

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2399

><td class="source">	print &quot;[+] Server Info (NetServerGetInfo 102)&quot;<br></td></tr
><tr
id=sl_svn139_2400

><td class="source">	print <br></td></tr
><tr
id=sl_svn139_2401

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2402

><td class="source">def check_progfiles():<br></td></tr
><tr
id=sl_svn139_2403

><td class="source">	# %ProgramFiles%<br></td></tr
><tr
id=sl_svn139_2404

><td class="source">	# %ProgramFiles(x86)%<br></td></tr
><tr
id=sl_svn139_2405

><td class="source">	prog_dirs = []<br></td></tr
><tr
id=sl_svn139_2406

><td class="source">#	re_exe = re.compile(&#39;\.exe$|\.com$|\.bat$|\.dll$&#39;, re.IGNORECASE)<br></td></tr
><tr
id=sl_svn139_2407

><td class="source">	exts = (&#39;exe&#39;, &#39;com&#39;, &#39;bat&#39;, &#39;dll&#39;) # TODO pl, rb, py, php, inc, asp, aspx, ocx, vbs, more?<br></td></tr
><tr
id=sl_svn139_2408

><td class="source"><br></td></tr
><tr
id=sl_svn139_2409

><td class="source">	if os.getenv(&#39;ProgramFiles&#39;):<br></td></tr
><tr
id=sl_svn139_2410

><td class="source">		prog_dirs.append(os.environ[&#39;ProgramFiles&#39;])<br></td></tr
><tr
id=sl_svn139_2411

><td class="source"><br></td></tr
><tr
id=sl_svn139_2412

><td class="source">	if os.getenv(&#39;ProgramFiles(x86)&#39;):<br></td></tr
><tr
id=sl_svn139_2413

><td class="source">		prog_dirs.append(os.environ[&#39;ProgramFiles(x86)&#39;])<br></td></tr
><tr
id=sl_svn139_2414

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2415

><td class="source">	dot_count = 0<br></td></tr
><tr
id=sl_svn139_2416

><td class="source">	weak_flag = 0<br></td></tr
><tr
id=sl_svn139_2417

><td class="source">	for prog_dir in prog_dirs:<br></td></tr
><tr
id=sl_svn139_2418

><td class="source">		# print &quot;Looking for programs under %s...&quot; % prog_dir<br></td></tr
><tr
id=sl_svn139_2419

><td class="source">		for root, dirs, files in os.walk(prog_dir):<br></td></tr
><tr
id=sl_svn139_2420

><td class="source">			#print &quot;root=%s, dirs=%s, files=%s&quot; % (root, dirs, files)<br></td></tr
><tr
id=sl_svn139_2421

><td class="source">#			for file in files:<br></td></tr
><tr
id=sl_svn139_2422

><td class="source">#				m = re_exe.search(file)<br></td></tr
><tr
id=sl_svn139_2423

><td class="source">#				if m is None:<br></td></tr
><tr
id=sl_svn139_2424

><td class="source">#					continue<br></td></tr
><tr
id=sl_svn139_2425

><td class="source">#				#print &quot;Checking file %s&quot; % os.path.join(root, file)<br></td></tr
><tr
id=sl_svn139_2426

><td class="source">#				weak_perms = check_weak_write_perms(os.path.join(root, file), &#39;file&#39;)<br></td></tr
><tr
id=sl_svn139_2427

><td class="source">#				if weak_perms:<br></td></tr
><tr
id=sl_svn139_2428

><td class="source">#					print_weak_perms(&quot;File&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_2429

><td class="source">			for file in dirs:<br></td></tr
><tr
id=sl_svn139_2430

><td class="source">				#print &quot;Checking dir %s&quot; % os.path.join(root, file)<br></td></tr
><tr
id=sl_svn139_2431

><td class="source">				weak_perms = check_weak_write_perms(os.path.join(root, file), &#39;file&#39;)<br></td></tr
><tr
id=sl_svn139_2432

><td class="source">				if weak_perms:<br></td></tr
><tr
id=sl_svn139_2433

><td class="source">					#print_weak_perms(&quot;Directory&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_2434

><td class="source">					save_issue(&quot;WPC001&quot;, &quot;writable_dirs&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_2435

><td class="source">					weak_flag = 1<br></td></tr
><tr
id=sl_svn139_2436

><td class="source">				dir = file<br></td></tr
><tr
id=sl_svn139_2437

><td class="source">				for ext in exts:<br></td></tr
><tr
id=sl_svn139_2438

><td class="source">					for f in glob.glob(root + &quot;\\&quot; + dir + &#39;\*.&#39; + ext):<br></td></tr
><tr
id=sl_svn139_2439

><td class="source">						#print &quot;Processing &quot; + f<br></td></tr
><tr
id=sl_svn139_2440

><td class="source">						weak_perms = check_weak_write_perms(f, &#39;file&#39;)<br></td></tr
><tr
id=sl_svn139_2441

><td class="source">						if weak_perms:<br></td></tr
><tr
id=sl_svn139_2442

><td class="source">							print_weak_perms(&quot;File&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_2443

><td class="source">							save_issue(&quot;WPC001&quot;, &quot;writable_progs&quot;, weak_perms)<br></td></tr
><tr
id=sl_svn139_2444

><td class="source">							weak_flag = 1<br></td></tr
><tr
id=sl_svn139_2445

><td class="source">				dot_count = dot_count + 1;<br></td></tr
><tr
id=sl_svn139_2446

><td class="source">				# Don&#39;t print out all the dots.  There are too many!<br></td></tr
><tr
id=sl_svn139_2447

><td class="source">				if dot_count &gt; 10:<br></td></tr
><tr
id=sl_svn139_2448

><td class="source">					if weak_flag == 1:<br></td></tr
><tr
id=sl_svn139_2449

><td class="source">						sys.stdout.write(&quot;!&quot;)<br></td></tr
><tr
id=sl_svn139_2450

><td class="source">					else:<br></td></tr
><tr
id=sl_svn139_2451

><td class="source">						sys.stdout.write(&quot;.&quot;)						<br></td></tr
><tr
id=sl_svn139_2452

><td class="source">					dot_count = 0;<br></td></tr
><tr
id=sl_svn139_2453

><td class="source">					weak_flag = 0;<br></td></tr
><tr
id=sl_svn139_2454

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2455

><td class="source"><br></td></tr
><tr
id=sl_svn139_2456

><td class="source">def check_patches():<br></td></tr
><tr
id=sl_svn139_2457

><td class="source"># TODO: This is more difficult than I&#39;d hoped.  You can&#39;t just search for the KB number: XP will appear to be vulnerable to dcom.  Need to search for KB number or SP2 in this case.<br></td></tr
><tr
id=sl_svn139_2458

><td class="source">#	from subprocess import Popen, PIPE<br></td></tr
><tr
id=sl_svn139_2459

><td class="source">	patchlist = Popen([&quot;systeminfo&quot;], stdout=PIPE).communicate()[0]<br></td></tr
><tr
id=sl_svn139_2460

><td class="source">#	for kb_no in kb_nos:<br></td></tr
><tr
id=sl_svn139_2461

><td class="source">#		print &quot;Searching for &quot; + kb_no<br></td></tr
><tr
id=sl_svn139_2462

><td class="source">#		if re.search(kb_no, patchlist):<br></td></tr
><tr
id=sl_svn139_2463

><td class="source">#			print &quot;found&quot;<br></td></tr
><tr
id=sl_svn139_2464

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2465

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2466

><td class="source">def print_section(title):<br></td></tr
><tr
id=sl_svn139_2467

><td class="source">	if (verbose != 0):<br></td></tr
><tr
id=sl_svn139_2468

><td class="source">		print &quot;=================================&quot;<br></td></tr
><tr
id=sl_svn139_2469

><td class="source">		print title<br></td></tr
><tr
id=sl_svn139_2470

><td class="source">		print &quot;=================================&quot;<br></td></tr
><tr
id=sl_svn139_2471

><td class="source">		print<br></td></tr
><tr
id=sl_svn139_2472

><td class="source">	else:<br></td></tr
><tr
id=sl_svn139_2473

><td class="source">		sys.stdout.write(title + &quot;: &quot;)<br></td></tr
><tr
id=sl_svn139_2474

><td class="source"><br></td></tr
><tr
id=sl_svn139_2475

><td class="source"># http://www.daniweb.com/code/snippet216539.html<br></td></tr
><tr
id=sl_svn139_2476

><td class="source">def int2bin(n):<br></td></tr
><tr
id=sl_svn139_2477

><td class="source">	bStr = &#39;&#39;<br></td></tr
><tr
id=sl_svn139_2478

><td class="source">	if n &lt; 0: n = n + 2^32<br></td></tr
><tr
id=sl_svn139_2479

><td class="source">	if n == 0: return &#39;0&#39;<br></td></tr
><tr
id=sl_svn139_2480

><td class="source">	while n &gt; 0:<br></td></tr
><tr
id=sl_svn139_2481

><td class="source">		bStr = str(n % 2) + bStr<br></td></tr
><tr
id=sl_svn139_2482

><td class="source">		n = n &gt;&gt; 1<br></td></tr
><tr
id=sl_svn139_2483

><td class="source">	return bStr<br></td></tr
><tr
id=sl_svn139_2484

><td class="source"><br></td></tr
><tr
id=sl_svn139_2485

><td class="source">def impersonate(username, password, domain):<br></td></tr
><tr
id=sl_svn139_2486

><td class="source">	if username:<br></td></tr
><tr
id=sl_svn139_2487

><td class="source">		print &quot;Using alternative credentials:&quot;<br></td></tr
><tr
id=sl_svn139_2488

><td class="source">		print &quot;Username: &quot; + str(username)<br></td></tr
><tr
id=sl_svn139_2489

><td class="source">		print &quot;Password: &quot; + str(password)<br></td></tr
><tr
id=sl_svn139_2490

><td class="source">		print &quot;Domain:   &quot; + str(domain)<br></td></tr
><tr
id=sl_svn139_2491

><td class="source">		handle = win32security.LogonUser( username, domain, password, win32security.LOGON32_LOGON_NEW_CREDENTIALS, win32security.LOGON32_PROVIDER_WINNT50 )<br></td></tr
><tr
id=sl_svn139_2492

><td class="source">		win32security.ImpersonateLoggedOnUser( handle )<br></td></tr
><tr
id=sl_svn139_2493

><td class="source">	else:<br></td></tr
><tr
id=sl_svn139_2494

><td class="source">		print &quot;Running as current user.  No logon creds supplied (-u, -d, -p).&quot;<br></td></tr
><tr
id=sl_svn139_2495

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2496

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2497

><td class="source">def audit_passpol():<br></td></tr
><tr
id=sl_svn139_2498

><td class="source">	print <br></td></tr
><tr
id=sl_svn139_2499

><td class="source">	print &quot;[+] NetUserModalsGet 0,1,2,3&quot;<br></td></tr
><tr
id=sl_svn139_2500

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2501

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2502

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2503

><td class="source">		data = win32net.NetUserModalsGet(remote_server, 0)<br></td></tr
><tr
id=sl_svn139_2504

><td class="source">		for key in data.keys():<br></td></tr
><tr
id=sl_svn139_2505

><td class="source">			print &quot;%s: %s&quot; % (key, data[key])<br></td></tr
><tr
id=sl_svn139_2506

><td class="source">		data = win32net.NetUserModalsGet(remote_server, 1)<br></td></tr
><tr
id=sl_svn139_2507

><td class="source">		for key in data.keys():<br></td></tr
><tr
id=sl_svn139_2508

><td class="source">			print &quot;%s: %s&quot; % (key, data[key])<br></td></tr
><tr
id=sl_svn139_2509

><td class="source">		data = win32net.NetUserModalsGet(remote_server, 2)<br></td></tr
><tr
id=sl_svn139_2510

><td class="source">		for key in data.keys():<br></td></tr
><tr
id=sl_svn139_2511

><td class="source">			if key == &#39;domain_id&#39;:<br></td></tr
><tr
id=sl_svn139_2512

><td class="source">				print &quot;%s: %s&quot; % (key, win32security.ConvertSidToStringSid(data[key]))<br></td></tr
><tr
id=sl_svn139_2513

><td class="source">			elif key == &#39;lockout_threshold&#39; and data[key] == &#39;0&#39;:<br></td></tr
><tr
id=sl_svn139_2514

><td class="source">				print &quot;%s: %s (accounts aren&#39;t locked out)&quot; % (key, data[key])<br></td></tr
><tr
id=sl_svn139_2515

><td class="source">			else:<br></td></tr
><tr
id=sl_svn139_2516

><td class="source">				print &quot;%s: %s&quot; % (key, data[key])<br></td></tr
><tr
id=sl_svn139_2517

><td class="source">		data = win32net.NetUserModalsGet(remote_server, 3)<br></td></tr
><tr
id=sl_svn139_2518

><td class="source">		for key in data.keys():<br></td></tr
><tr
id=sl_svn139_2519

><td class="source">			if key == &#39;lockout_threshold&#39; and data[key] == 0:<br></td></tr
><tr
id=sl_svn139_2520

><td class="source">				print &quot;%s: %s (accounts aren&#39;t locked out)&quot; % (key, data[key])<br></td></tr
><tr
id=sl_svn139_2521

><td class="source">			else:<br></td></tr
><tr
id=sl_svn139_2522

><td class="source">				print &quot;%s: %s&quot; % (key, data[key])<br></td></tr
><tr
id=sl_svn139_2523

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_2524

><td class="source">		print &quot;[E] Couldn&#39;t get NetUserModals data&quot;<br></td></tr
><tr
id=sl_svn139_2525

><td class="source"><br></td></tr
><tr
id=sl_svn139_2526

><td class="source"># Recursive function to find group members (and the member of any groups in those groups...)<br></td></tr
><tr
id=sl_svn139_2527

><td class="source">def get_group_members(server, group, depth):<br></td></tr
><tr
id=sl_svn139_2528

><td class="source">		resume = 0<br></td></tr
><tr
id=sl_svn139_2529

><td class="source">		indent = &quot;\t&quot; * depth<br></td></tr
><tr
id=sl_svn139_2530

><td class="source">		members = []<br></td></tr
><tr
id=sl_svn139_2531

><td class="source">		while True:<br></td></tr
><tr
id=sl_svn139_2532

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_2533

><td class="source">				m, total, resume = win32net.NetLocalGroupGetMembers(server, group, 2, resume, 999999)<br></td></tr
><tr
id=sl_svn139_2534

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_2535

><td class="source">				break<br></td></tr
><tr
id=sl_svn139_2536

><td class="source">			for member in m:<br></td></tr
><tr
id=sl_svn139_2537

><td class="source">				if member[&#39;sidusage&#39;] == 4:<br></td></tr
><tr
id=sl_svn139_2538

><td class="source">					type = &quot;local group&quot;<br></td></tr
><tr
id=sl_svn139_2539

><td class="source">					g = member[&#39;domainandname&#39;].split(&quot;\\&quot;)<br></td></tr
><tr
id=sl_svn139_2540

><td class="source">					print indent + member[&#39;domainandname&#39;] + &quot; (&quot; + str(type) + &quot;)&quot;<br></td></tr
><tr
id=sl_svn139_2541

><td class="source">					get_group_members(server, g[1], depth + 1)<br></td></tr
><tr
id=sl_svn139_2542

><td class="source">				elif member[&#39;sidusage&#39;] == 2:<br></td></tr
><tr
id=sl_svn139_2543

><td class="source">					type = &quot;domain group&quot;<br></td></tr
><tr
id=sl_svn139_2544

><td class="source">					print indent + member[&#39;domainandname&#39;] + &quot; (&quot; + str(type) + &quot;)&quot;<br></td></tr
><tr
id=sl_svn139_2545

><td class="source">				elif member[&#39;sidusage&#39;] == 1:<br></td></tr
><tr
id=sl_svn139_2546

><td class="source">					type = &quot;user&quot;<br></td></tr
><tr
id=sl_svn139_2547

><td class="source">					print indent + member[&#39;domainandname&#39;] + &quot; (&quot; + str(type) + &quot;)&quot;<br></td></tr
><tr
id=sl_svn139_2548

><td class="source">				else: <br></td></tr
><tr
id=sl_svn139_2549

><td class="source">					type = &quot;type &quot; + str(member[&#39;sidusage&#39;])<br></td></tr
><tr
id=sl_svn139_2550

><td class="source">					print indent + member[&#39;domainandname&#39;] + &quot; (&quot; + str(type) + &quot;)&quot;<br></td></tr
><tr
id=sl_svn139_2551

><td class="source">			if resume == 0:<br></td></tr
><tr
id=sl_svn139_2552

><td class="source">				break<br></td></tr
><tr
id=sl_svn139_2553

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2554

><td class="source">def audit_admin_users():<br></td></tr
><tr
id=sl_svn139_2555

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2556

><td class="source">	for group in (&quot;administrators&quot;, &quot;domain admins&quot;, &quot;enterprise admins&quot;):<br></td></tr
><tr
id=sl_svn139_2557

><td class="source">		print &quot;\n[+] Members of &quot; + group + &quot;:&quot;<br></td></tr
><tr
id=sl_svn139_2558

><td class="source">		get_group_members(remote_server, group, 0)<br></td></tr
><tr
id=sl_svn139_2559

><td class="source">	print <br></td></tr
><tr
id=sl_svn139_2560

><td class="source"><br></td></tr
><tr
id=sl_svn139_2561

><td class="source"># It might be interesting to look up who has powerful privs, but LsaEnumerateAccountsWithUserRight doesn&#39;t seem to work as a low priv user<br></td></tr
><tr
id=sl_svn139_2562

><td class="source"># SE_ASSIGNPRIMARYTOKEN_NAME TEXT(&quot;SeAssignPrimaryTokenPrivilege&quot;) Required to assign the primary token of a process. User Right: Replace a process-level token.<br></td></tr
><tr
id=sl_svn139_2563

><td class="source"># SE_BACKUP_NAME TEXT(&quot;SeBackupPrivilege&quot;) Required to perform backup operations. This privilege causes the system to grant all read access control to any file, regardless of the access control list (ACL) specified for the file. Any access request other than read is still evaluated with the ACL. This privilege is required by the RegSaveKey and RegSaveKeyExfunctions. The following access rights are granted if this privilege is held: READ_CONTROL ACCESS_SYSTEM_SECURITY FILE_GENERIC_READ FILE_TRAVERSE User Right: Back up files and directories.<br></td></tr
><tr
id=sl_svn139_2564

><td class="source"># SE_CREATE_PAGEFILE_NAME TEXT(&quot;SeCreatePagefilePrivilege&quot;) Required to create a paging file. User Right: Create a pagefile.<br></td></tr
><tr
id=sl_svn139_2565

><td class="source"># SE_CREATE_TOKEN_NAME TEXT(&quot;SeCreateTokenPrivilege&quot;) Required to create a primary token. User Right: Create a token object.<br></td></tr
><tr
id=sl_svn139_2566

><td class="source"># SE_DEBUG_NAME TEXT(&quot;SeDebugPrivilege&quot;) Required to debug and adjust the memory of a process owned by another account. User Right: Debug programs.<br></td></tr
><tr
id=sl_svn139_2567

><td class="source"># SE_ENABLE_DELEGATION_NAME TEXT(&quot;SeEnableDelegationPrivilege&quot;) Required to mark user and computer accounts as trusted for delegation. User Right: Enable computer and user accounts to be trusted for delegation.<br></td></tr
><tr
id=sl_svn139_2568

><td class="source"># SE_LOAD_DRIVER_NAME TEXT(&quot;SeLoadDriverPrivilege&quot;) Required to load or unload a device driver. User Right: Load and unload device drivers.<br></td></tr
><tr
id=sl_svn139_2569

><td class="source"># SE_MACHINE_ACCOUNT_NAME TEXT(&quot;SeMachineAccountPrivilege&quot;) Required to create a computer account. User Right: Add workstations to domain.<br></td></tr
><tr
id=sl_svn139_2570

><td class="source"># SE_MANAGE_VOLUME_NAME TEXT(&quot;SeManageVolumePrivilege&quot;) Required to enable volume management privileges. User Right: Manage the files on a volume.<br></td></tr
><tr
id=sl_svn139_2571

><td class="source"># SE_RELABEL_NAME TEXT(&quot;SeRelabelPrivilege&quot;) Required to modify the mandatory integrity level of an object. User Right: Modify an object label.<br></td></tr
><tr
id=sl_svn139_2572

><td class="source"># SE_RESTORE_NAME TEXT(&quot;SeRestorePrivilege&quot;) Required to perform restore operations. This privilege causes the system to grant all write access control to any file, regardless of the ACL specified for the file. Any access request other than write is still evaluated with the ACL. Additionally, this privilege enables you to set any valid user or group SID as the owner of a file. This privilege is required by the RegLoadKey function. The following access rights are granted if this privilege is held: WRITE_DAC WRITE_OWNER ACCESS_SYSTEM_SECURITY FILE_GENERIC_WRITE FILE_ADD_FILE FILE_ADD_SUBDIRECTORY DELETE User Right: Restore files and directories.<br></td></tr
><tr
id=sl_svn139_2573

><td class="source"># SE_SHUTDOWN_NAME TEXT(&quot;SeShutdownPrivilege&quot;) Required to shut down a local system. User Right: Shut down the system.<br></td></tr
><tr
id=sl_svn139_2574

><td class="source"># SE_SYNC_AGENT_NAME TEXT(&quot;SeSyncAgentPrivilege&quot;) Required for a domain controller to use the LDAP directory synchronization services. This privilege enables the holder to read all objects and properties in the directory, regardless of the protection on the objects and properties. By default, it is assigned to the Administrator and LocalSystem accounts on domain controllers. User Right: Synchronize directory service data.<br></td></tr
><tr
id=sl_svn139_2575

><td class="source"># SE_TAKE_OWNERSHIP_NAME TEXT(&quot;SeTakeOwnershipPrivilege&quot;) Required to take ownership of an object without being granted discretionary access. This privilege allows the owner value to be set only to those values that the holder may legitimately assign as the owner of an object. User Right: Take ownership of files or other objects.<br></td></tr
><tr
id=sl_svn139_2576

><td class="source"># SE_TCB_NAME TEXT(&quot;SeTcbPrivilege&quot;) This privilege identifies its holder as part of the trusted computer base. Some trusted protected subsystems are granted this privilege. User Right: Act as part of the operating system.<br></td></tr
><tr
id=sl_svn139_2577

><td class="source"># SE_TRUSTED_CREDMAN_ACCESS_NAME TEXT(&quot;SeTrustedCredManAccessPrivilege&quot;) Required to access Credential Manager as a trusted caller. User Right: Access Credential Manager as a trusted caller.<br></td></tr
><tr
id=sl_svn139_2578

><td class="source"><br></td></tr
><tr
id=sl_svn139_2579

><td class="source"># Need: SE_ENABLE_DELEGATION_NAME, SE_MANAGE_VOLUME_NAME, SE_RELABEL_NAME, SE_SYNC_AGENT_NAME, SE_TRUSTED_CREDMAN_ACCESS_NAME<br></td></tr
><tr
id=sl_svn139_2580

><td class="source">#	ph = win32security.LsaOpenPolicy(remote_server, win32security.POLICY_VIEW_LOCAL_INFORMATION | win32security.POLICY_LOOKUP_NAMES)<br></td></tr
><tr
id=sl_svn139_2581

><td class="source">#	for priv in (SE_ASSIGNPRIMARYTOKEN_NAME, SE_BACKUP_NAME, SE_CREATE_PAGEFILE_NAME, SE_CREATE_TOKEN_NAME, SE_DEBUG_NAME, SE_LOAD_DRIVER_NAME, SE_MACHINE_ACCOUNT_NAME, SE_RESTORE_NAME, SE_SHUTDOWN_NAME, SE_TAKE_OWNERSHIP_NAME, SE_TCB_NAME):<br></td></tr
><tr
id=sl_svn139_2582

><td class="source">#		print &quot;Looking up who has &quot; + priv + &quot;priv&quot;<br></td></tr
><tr
id=sl_svn139_2583

><td class="source">#		try:<br></td></tr
><tr
id=sl_svn139_2584

><td class="source">#			sids = win32security.LsaEnumerateAccountsWithUserRight(ph, priv)<br></td></tr
><tr
id=sl_svn139_2585

><td class="source">#			print sids<br></td></tr
><tr
id=sl_svn139_2586

><td class="source">#		except:<br></td></tr
><tr
id=sl_svn139_2587

><td class="source">#			print &quot;[E] Lookup failed&quot;<br></td></tr
><tr
id=sl_svn139_2588

><td class="source"><br></td></tr
><tr
id=sl_svn139_2589

><td class="source">def audit_logged_in():<br></td></tr
><tr
id=sl_svn139_2590

><td class="source">	resume = 0<br></td></tr
><tr
id=sl_svn139_2591

><td class="source">	print &quot;\n[+] Logged in users:&quot;<br></td></tr
><tr
id=sl_svn139_2592

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2593

><td class="source">		while True:<br></td></tr
><tr
id=sl_svn139_2594

><td class="source">			users, total, resume = win32net.NetWkstaUserEnum(remote_server, 1 , resume , 999999 )<br></td></tr
><tr
id=sl_svn139_2595

><td class="source">			for user in users:<br></td></tr
><tr
id=sl_svn139_2596

><td class="source">				print &quot;User logged in: Logon Server=\&quot;%s\&quot; Logon Domain=\&quot;%s\&quot; Username=\&quot;%s\&quot;&quot; % (user[&#39;logon_server&#39;], user[&#39;logon_domain&#39;], user[&#39;username&#39;])<br></td></tr
><tr
id=sl_svn139_2597

><td class="source">			if resume == 0:<br></td></tr
><tr
id=sl_svn139_2598

><td class="source">				break<br></td></tr
><tr
id=sl_svn139_2599

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_2600

><td class="source">		print &quot;[E] Failed&quot;<br></td></tr
><tr
id=sl_svn139_2601

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2602

><td class="source">def audit_host_info():<br></td></tr
><tr
id=sl_svn139_2603

><td class="source">	print &quot;\n&quot;<br></td></tr
><tr
id=sl_svn139_2604

><td class="source">	if remote_server:<br></td></tr
><tr
id=sl_svn139_2605

><td class="source">		print &quot;Querying remote server: &quot; + remote_server<br></td></tr
><tr
id=sl_svn139_2606

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2607

><td class="source">	# Only works on local host<br></td></tr
><tr
id=sl_svn139_2608

><td class="source">	#win32net.NetGetJoinInformation()<br></td></tr
><tr
id=sl_svn139_2609

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2610

><td class="source">	# This looks interesting, but doesn&#39;t seem to work.  Maybe unsupported legacy api.<br></td></tr
><tr
id=sl_svn139_2611

><td class="source">	#pywintypes.error: (50, &#39;NetUseEnum&#39;, &#39;The request is not supported.&#39;)<br></td></tr
><tr
id=sl_svn139_2612

><td class="source">	#print<br></td></tr
><tr
id=sl_svn139_2613

><td class="source">	#print &quot;[+] Getting Net Use info&quot;<br></td></tr
><tr
id=sl_svn139_2614

><td class="source">	#print<br></td></tr
><tr
id=sl_svn139_2615

><td class="source"><br></td></tr
><tr
id=sl_svn139_2616

><td class="source">	#resume = 0<br></td></tr
><tr
id=sl_svn139_2617

><td class="source">	#use, total, resume = win32net.NetUseEnum(remote_server, 2, resume , 999999 )	<br></td></tr
><tr
id=sl_svn139_2618

><td class="source">	#print use<br></td></tr
><tr
id=sl_svn139_2619

><td class="source"><br></td></tr
><tr
id=sl_svn139_2620

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2621

><td class="source">	print &quot;[+] Workstation Info (NetWkstaGetInfo 102)&quot;<br></td></tr
><tr
id=sl_svn139_2622

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2623

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2624

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2625

><td class="source">		#print win32net.NetWkstaGetInfo(remote_server, 100)<br></td></tr
><tr
id=sl_svn139_2626

><td class="source">		#print win32net.NetWkstaGetInfo(remote_server, 101)<br></td></tr
><tr
id=sl_svn139_2627

><td class="source">		serverinfo = win32net.NetWkstaGetInfo(remote_server, 102)<br></td></tr
><tr
id=sl_svn139_2628

><td class="source">		print &quot;Computer Name: %s&quot; % serverinfo[&#39;computername&#39;]<br></td></tr
><tr
id=sl_svn139_2629

><td class="source">		print &quot;Langroup: %s&quot; % serverinfo[&#39;langroup&#39;]<br></td></tr
><tr
id=sl_svn139_2630

><td class="source">		print &quot;OS: %s.%s&quot; % (serverinfo[&#39;ver_major&#39;], serverinfo[&#39;ver_minor&#39;])<br></td></tr
><tr
id=sl_svn139_2631

><td class="source">		print &quot;Logged On Users: %s&quot; % serverinfo[&#39;logged_on_users&#39;]<br></td></tr
><tr
id=sl_svn139_2632

><td class="source">		print &quot;Lanroot: %s&quot; % serverinfo[&#39;lanroot&#39;]<br></td></tr
><tr
id=sl_svn139_2633

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2634

><td class="source">		if serverinfo[&#39;platform_id&#39;] &amp; win32netcon.PLATFORM_ID_NT:<br></td></tr
><tr
id=sl_svn139_2635

><td class="source">			print &quot;Platform: PLATFORM_ID_NT (means NT family, not NT4)&quot;<br></td></tr
><tr
id=sl_svn139_2636

><td class="source">		if serverinfo[&#39;platform_id&#39;] == win32netcon.PLATFORM_ID_OS2:<br></td></tr
><tr
id=sl_svn139_2637

><td class="source">			print &quot;Platform: PLATFORM_ID_OS2&quot;<br></td></tr
><tr
id=sl_svn139_2638

><td class="source">		if serverinfo[&#39;platform_id&#39;] == win32netcon.PLATFORM_ID_DOS:<br></td></tr
><tr
id=sl_svn139_2639

><td class="source">			print &quot;Platform: PLATFORM_ID_DOS&quot;<br></td></tr
><tr
id=sl_svn139_2640

><td class="source">		if serverinfo[&#39;platform_id&#39;] == win32netcon.PLATFORM_ID_OSF:<br></td></tr
><tr
id=sl_svn139_2641

><td class="source">			print &quot;Platform: PLATFORM_ID_OSF&quot;<br></td></tr
><tr
id=sl_svn139_2642

><td class="source">		if serverinfo[&#39;platform_id&#39;] == win32netcon.PLATFORM_ID_VMS:<br></td></tr
><tr
id=sl_svn139_2643

><td class="source">			print &quot;Platform: PLATFORM_ID_VMS&quot;<br></td></tr
><tr
id=sl_svn139_2644

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_2645

><td class="source">		print &quot;[E] Couldn&#39;t get Workstation Info&quot;<br></td></tr
><tr
id=sl_svn139_2646

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2647

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2648

><td class="source">	print &quot;[+] Server Info (NetServerGetInfo 102)&quot;<br></td></tr
><tr
id=sl_svn139_2649

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2650

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2651

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2652

><td class="source">		#print &quot;NetServerGetInfo 100&quot; + str(win32net.NetServerGetInfo(remote_server, 100))<br></td></tr
><tr
id=sl_svn139_2653

><td class="source">		#print &quot;NetServerGetInfo 101&quot; + str(win32net.NetServerGetInfo(remote_server, 101))<br></td></tr
><tr
id=sl_svn139_2654

><td class="source">		serverinfo = win32net.NetServerGetInfo(remote_server, 102)<br></td></tr
><tr
id=sl_svn139_2655

><td class="source">		print &quot;Name: %s&quot; % serverinfo[&#39;name&#39;]<br></td></tr
><tr
id=sl_svn139_2656

><td class="source">		print &quot;Comment: %s&quot; % serverinfo[&#39;comment&#39;]<br></td></tr
><tr
id=sl_svn139_2657

><td class="source">		print &quot;OS: %s.%s&quot; % (serverinfo[&#39;version_major&#39;], serverinfo[&#39;version_minor&#39;])<br></td></tr
><tr
id=sl_svn139_2658

><td class="source">		print &quot;Userpath: %s&quot; % serverinfo[&#39;userpath&#39;]<br></td></tr
><tr
id=sl_svn139_2659

><td class="source">		print &quot;Hidden: %s&quot; % serverinfo[&#39;hidden&#39;]<br></td></tr
><tr
id=sl_svn139_2660

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2661

><td class="source">		if serverinfo[&#39;platform_id&#39;] &amp; win32netcon.PLATFORM_ID_NT:<br></td></tr
><tr
id=sl_svn139_2662

><td class="source">			print &quot;Platform: PLATFORM_ID_NT (means NT family, not NT4)&quot;<br></td></tr
><tr
id=sl_svn139_2663

><td class="source">		if serverinfo[&#39;platform_id&#39;] == win32netcon.PLATFORM_ID_OS2:<br></td></tr
><tr
id=sl_svn139_2664

><td class="source">			print &quot;Platform: PLATFORM_ID_OS2&quot;<br></td></tr
><tr
id=sl_svn139_2665

><td class="source">		if serverinfo[&#39;platform_id&#39;] == win32netcon.PLATFORM_ID_DOS:<br></td></tr
><tr
id=sl_svn139_2666

><td class="source">			print &quot;Platform: PLATFORM_ID_DOS&quot;<br></td></tr
><tr
id=sl_svn139_2667

><td class="source">		if serverinfo[&#39;platform_id&#39;] == win32netcon.PLATFORM_ID_OSF:<br></td></tr
><tr
id=sl_svn139_2668

><td class="source">			print &quot;Platform: PLATFORM_ID_OSF&quot;<br></td></tr
><tr
id=sl_svn139_2669

><td class="source">		if serverinfo[&#39;platform_id&#39;] == win32netcon.PLATFORM_ID_VMS:<br></td></tr
><tr
id=sl_svn139_2670

><td class="source">			print &quot;Platform: PLATFORM_ID_VMS&quot;<br></td></tr
><tr
id=sl_svn139_2671

><td class="source">		for sv_type in sv_types:<br></td></tr
><tr
id=sl_svn139_2672

><td class="source">			if serverinfo[&#39;type&#39;] &amp; getattr(win32netcon, sv_type):<br></td></tr
><tr
id=sl_svn139_2673

><td class="source">				print &quot;Type: &quot; + sv_type<br></td></tr
><tr
id=sl_svn139_2674

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_2675

><td class="source">		print &quot;[E] Couldn&#39;t get Server Info&quot;<br></td></tr
><tr
id=sl_svn139_2676

><td class="source"><br></td></tr
><tr
id=sl_svn139_2677

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2678

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2679

><td class="source">	print &quot;[+] LsaQueryInformationPolicy&quot;<br></td></tr
><tr
id=sl_svn139_2680

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2681

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2682

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2683

><td class="source">		ph = win32security.LsaOpenPolicy(remote_server, win32security.POLICY_VIEW_LOCAL_INFORMATION | win32security.POLICY_LOOKUP_NAMES)<br></td></tr
><tr
id=sl_svn139_2684

><td class="source">		print &quot;PolicyDnsDomainInformation:&quot;<br></td></tr
><tr
id=sl_svn139_2685

><td class="source">		print win32security.LsaQueryInformationPolicy(ph, win32security.PolicyDnsDomainInformation)<br></td></tr
><tr
id=sl_svn139_2686

><td class="source">		print &quot;PolicyDnsDomainInformation:&quot;<br></td></tr
><tr
id=sl_svn139_2687

><td class="source">		print win32security.LsaQueryInformationPolicy(ph, win32security.PolicyPrimaryDomainInformation)<br></td></tr
><tr
id=sl_svn139_2688

><td class="source">		print &quot;PolicyPrimaryDomainInformation:&quot;<br></td></tr
><tr
id=sl_svn139_2689

><td class="source">		print win32security.LsaQueryInformationPolicy(ph, win32security.PolicyAccountDomainInformation)<br></td></tr
><tr
id=sl_svn139_2690

><td class="source">		print &quot;PolicyLsaServerRoleInformation:&quot;<br></td></tr
><tr
id=sl_svn139_2691

><td class="source">		print win32security.LsaQueryInformationPolicy(ph, win32security.PolicyLsaServerRoleInformation)<br></td></tr
><tr
id=sl_svn139_2692

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_2693

><td class="source">		print &quot;[E] Couldn&#39;t LsaOpenPolicy&quot;<br></td></tr
><tr
id=sl_svn139_2694

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2695

><td class="source">	# DsBindWithCred isn&#39;t available from python!<br></td></tr
><tr
id=sl_svn139_2696

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2697

><td class="source">	# IADsComputer looks useful, but also isn&#39;t implemented:<br></td></tr
><tr
id=sl_svn139_2698

><td class="source">	# http://msdn.microsoft.com/en-us/library/aa705980%28v=VS.85%29.aspx<br></td></tr
><tr
id=sl_svn139_2699

><td class="source"><br></td></tr
><tr
id=sl_svn139_2700

><td class="source">	# The following always seems to fail:<br></td></tr
><tr
id=sl_svn139_2701

><td class="source">	# need a dc hostname as remote_server<br></td></tr
><tr
id=sl_svn139_2702

><td class="source">	# and    domain<br></td></tr
><tr
id=sl_svn139_2703

><td class="source">	#try:<br></td></tr
><tr
id=sl_svn139_2704

><td class="source">	#	hds = win32security.DsBind(remote_server, remote_domain)<br></td></tr
><tr
id=sl_svn139_2705

><td class="source">	#	print &quot;hds: &quot; + hds<br></td></tr
><tr
id=sl_svn139_2706

><td class="source">	#	print &quot;DsListDomainsInSite: &quot;+ str(win32security.DsListDomainsInSite(hds))<br></td></tr
><tr
id=sl_svn139_2707

><td class="source">	#except:<br></td></tr
><tr
id=sl_svn139_2708

><td class="source">	#	pass<br></td></tr
><tr
id=sl_svn139_2709

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2710

><td class="source">	# domain can be null.  i think domainguid can be null.  sitename null.  flags = 0.<br></td></tr
><tr
id=sl_svn139_2711

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2712

><td class="source">	# lists roles recognised by the server (fsmo roles?)<br></td></tr
><tr
id=sl_svn139_2713

><td class="source">	# win32security.DsListRoles(hds)<br></td></tr
><tr
id=sl_svn139_2714

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2715

><td class="source">	# list misc info for a server<br></td></tr
><tr
id=sl_svn139_2716

><td class="source">	# win32security.DsListInfoForServer(hds, server)<br></td></tr
><tr
id=sl_svn139_2717

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2718

><td class="source">	# but how to get a list of sites?<br></td></tr
><tr
id=sl_svn139_2719

><td class="source">	# win32security.DsListServersInSite(hds, site )<br></td></tr
><tr
id=sl_svn139_2720

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2721

><td class="source">	# win32security.DsCrackNames(hds, flags , formatOffered , formatDesired , names )<br></td></tr
><tr
id=sl_svn139_2722

><td class="source">	# ...For example, user objects can be identified by SAM account names (Domain\UserName), user principal name (UserName@Domain.com), or distinguished name.<br></td></tr
><tr
id=sl_svn139_2723

><td class="source"><br></td></tr
><tr
id=sl_svn139_2724

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2725

><td class="source">	print &quot;[+] Getting domain controller info&quot;<br></td></tr
><tr
id=sl_svn139_2726

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2727

><td class="source">	<br></td></tr
><tr
id=sl_svn139_2728

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2729

><td class="source">		domain = None # TODO: could call of each domain if we had a list<br></td></tr
><tr
id=sl_svn139_2730

><td class="source">		print &quot;PDC: &quot; + win32net.NetGetDCName(remote_server, domain)<br></td></tr
><tr
id=sl_svn139_2731

><td class="source">		# Try to list some domain controllers for the remote host<br></td></tr
><tr
id=sl_svn139_2732

><td class="source">		# There are better ways of doing this, but they don&#39;t seem to be available via python!<br></td></tr
><tr
id=sl_svn139_2733

><td class="source">		dc_seen = {}<br></td></tr
><tr
id=sl_svn139_2734

><td class="source">		for filter in (0, 0x00004000, 0x00000080, 0x00001000, 0x00000400, 0x00000040, 0x00000010):<br></td></tr
><tr
id=sl_svn139_2735

><td class="source">			dc_info = win32security.DsGetDcName(remote_server, None, None, None, filter)<br></td></tr
><tr
id=sl_svn139_2736

><td class="source">			if not dc_info[&#39;DomainControllerAddress&#39;] in dc_seen:<br></td></tr
><tr
id=sl_svn139_2737

><td class="source">				print &quot;\n[+] Found DC\n&quot;<br></td></tr
><tr
id=sl_svn139_2738

><td class="source">				for k in dc_info:<br></td></tr
><tr
id=sl_svn139_2739

><td class="source">					print k + &quot;: &quot; + str(dc_info[k])<br></td></tr
><tr
id=sl_svn139_2740

><td class="source">			dc_seen[dc_info[&#39;DomainControllerAddress&#39;]] = 1<br></td></tr
><tr
id=sl_svn139_2741

><td class="source">		print &quot;\nWARNING: Above is not necessarily a complete list of DCs\n&quot;<br></td></tr
><tr
id=sl_svn139_2742

><td class="source">		#print &quot;Domain controller: &quot; + str(win32security.DsGetDcName(remote_server, None, None, None, 0)) # any dc<br></td></tr
><tr
id=sl_svn139_2743

><td class="source">		#print &quot;Domain controller: &quot; + str(win32security.DsGetDcName(remote_server, None, None, None, 0x00004000)) # not the system we connect to<br></td></tr
><tr
id=sl_svn139_2744

><td class="source">		#print &quot;Domain controller: &quot; + str(win32security.DsGetDcName(remote_server, None, None, None, 0x00000080)) # pdc<br></td></tr
><tr
id=sl_svn139_2745

><td class="source">		#print &quot;Domain controller: &quot; + str(win32security.DsGetDcName(remote_server, None, None, None, 0x00001000)) # writeable<br></td></tr
><tr
id=sl_svn139_2746

><td class="source">		#print &quot;Domain controller: &quot; + str(win32security.DsGetDcName(remote_server, None, None, None, 0x00000400)) # kerberos<br></td></tr
><tr
id=sl_svn139_2747

><td class="source">		#print &quot;Domain controller: &quot; + str(win32security.DsGetDcName(remote_server, None, None, None, 0x00000040)) # gc<br></td></tr
><tr
id=sl_svn139_2748

><td class="source">		#print &quot;Domain controller: &quot; + str(win32security.DsGetDcName(remote_server, None, None, None, 0x00000010)) # directory service<br></td></tr
><tr
id=sl_svn139_2749

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_2750

><td class="source">		print &quot;[E] Couldn&#39;t get DC info&quot;<br></td></tr
><tr
id=sl_svn139_2751

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2752

><td class="source">	# This function sounds very much like what lservers.exe does, but the server name must be None<br></td></tr
><tr
id=sl_svn139_2753

><td class="source">	# according to http://msdn.microsoft.com/en-us/library/aa370623%28VS.85%29.aspx.  No use to us.<br></td></tr
><tr
id=sl_svn139_2754

><td class="source">	# print win32net.NetServerEnum(remote_server, 100 or 101, win32netcon.SV_TYPE_ALL, &quot;SOMEDOMAIN.COM&quot;, 0, 999999)<br></td></tr
><tr
id=sl_svn139_2755

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2756

><td class="source">def audit_user_group():<br></td></tr
><tr
id=sl_svn139_2757

><td class="source">	try:<br></td></tr
><tr
id=sl_svn139_2758

><td class="source">		ph = win32security.LsaOpenPolicy(remote_server, win32security.POLICY_VIEW_LOCAL_INFORMATION | win32security.POLICY_LOOKUP_NAMES)<br></td></tr
><tr
id=sl_svn139_2759

><td class="source">	except:<br></td></tr
><tr
id=sl_svn139_2760

><td class="source">		pass		<br></td></tr
><tr
id=sl_svn139_2761

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2762

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2763

><td class="source">	print &quot;[+] Local Groups&quot;<br></td></tr
><tr
id=sl_svn139_2764

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2765

><td class="source">	resume = 0<br></td></tr
><tr
id=sl_svn139_2766

><td class="source">	groups = []<br></td></tr
><tr
id=sl_svn139_2767

><td class="source">	while True:<br></td></tr
><tr
id=sl_svn139_2768

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_2769

><td class="source">			g, total, resume = win32net.NetLocalGroupEnum(remote_server, 0, resume, 999999)<br></td></tr
><tr
id=sl_svn139_2770

><td class="source">			groups = groups + g<br></td></tr
><tr
id=sl_svn139_2771

><td class="source">			if resume == 0:<br></td></tr
><tr
id=sl_svn139_2772

><td class="source">				break<br></td></tr
><tr
id=sl_svn139_2773

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_2774

><td class="source">			print &quot;[E] NetLocalGroupEnum failed&quot;<br></td></tr
><tr
id=sl_svn139_2775

><td class="source">			break<br></td></tr
><tr
id=sl_svn139_2776

><td class="source">	for group in groups:<br></td></tr
><tr
id=sl_svn139_2777

><td class="source">		members = []<br></td></tr
><tr
id=sl_svn139_2778

><td class="source">		while True:<br></td></tr
><tr
id=sl_svn139_2779

><td class="source">			m, total, resume = win32net.NetLocalGroupGetMembers(remote_server, group[&#39;name&#39;], 1, resume, 999999)<br></td></tr
><tr
id=sl_svn139_2780

><td class="source">			for member in m:<br></td></tr
><tr
id=sl_svn139_2781

><td class="source">				members.append(member[&#39;name&#39;])<br></td></tr
><tr
id=sl_svn139_2782

><td class="source">			if resume == 0:<br></td></tr
><tr
id=sl_svn139_2783

><td class="source">				break<br></td></tr
><tr
id=sl_svn139_2784

><td class="source">		sid, s, i = win32security.LookupAccountName(remote_server, group[&#39;name&#39;])<br></td></tr
><tr
id=sl_svn139_2785

><td class="source">		sid_string = win32security.ConvertSidToStringSid(sid)<br></td></tr
><tr
id=sl_svn139_2786

><td class="source">		print &quot;Group %s has sid %s&quot; % (group[&#39;name&#39;], sid_string)<br></td></tr
><tr
id=sl_svn139_2787

><td class="source">		for m in members:<br></td></tr
><tr
id=sl_svn139_2788

><td class="source">			print &quot;Group %s has member: %s&quot; % (group[&#39;name&#39;], m)<br></td></tr
><tr
id=sl_svn139_2789

><td class="source">		if verbose:<br></td></tr
><tr
id=sl_svn139_2790

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_2791

><td class="source">				privs = win32security.LsaEnumerateAccountRights(ph, sid)<br></td></tr
><tr
id=sl_svn139_2792

><td class="source">				for priv in privs:<br></td></tr
><tr
id=sl_svn139_2793

><td class="source">					print &quot;Group %s has privilege: %s&quot; % (group[&#39;name&#39;], priv)<br></td></tr
><tr
id=sl_svn139_2794

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_2795

><td class="source">				print &quot;Group %s: privilege lookup failed &quot; % (group[&#39;name&#39;])<br></td></tr
><tr
id=sl_svn139_2796

><td class="source">		<br></td></tr
><tr
id=sl_svn139_2797

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2798

><td class="source">	print &quot;[+] Non-local Groups&quot;<br></td></tr
><tr
id=sl_svn139_2799

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2800

><td class="source">	resume = 0<br></td></tr
><tr
id=sl_svn139_2801

><td class="source">	groups = []<br></td></tr
><tr
id=sl_svn139_2802

><td class="source">	while True:<br></td></tr
><tr
id=sl_svn139_2803

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_2804

><td class="source">			g, total, resume = win32net.NetGroupEnum(remote_server, 0, resume, 999999)<br></td></tr
><tr
id=sl_svn139_2805

><td class="source">			groups = groups + g<br></td></tr
><tr
id=sl_svn139_2806

><td class="source">			if resume == 0:<br></td></tr
><tr
id=sl_svn139_2807

><td class="source">				break<br></td></tr
><tr
id=sl_svn139_2808

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_2809

><td class="source">			print &quot;[E] NetGroupEnum failed&quot;<br></td></tr
><tr
id=sl_svn139_2810

><td class="source">			break<br></td></tr
><tr
id=sl_svn139_2811

><td class="source">			<br></td></tr
><tr
id=sl_svn139_2812

><td class="source">	for group in groups:<br></td></tr
><tr
id=sl_svn139_2813

><td class="source">		members = []<br></td></tr
><tr
id=sl_svn139_2814

><td class="source">		while True:<br></td></tr
><tr
id=sl_svn139_2815

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_2816

><td class="source">				m, total, resume = win32net.NetGroupGetUsers(remote_server, group[&#39;name&#39;], 0, resume, 999999)<br></td></tr
><tr
id=sl_svn139_2817

><td class="source">				for member in m:<br></td></tr
><tr
id=sl_svn139_2818

><td class="source">					members.append(member[&#39;name&#39;])<br></td></tr
><tr
id=sl_svn139_2819

><td class="source">				if resume == 0:<br></td></tr
><tr
id=sl_svn139_2820

><td class="source">					break<br></td></tr
><tr
id=sl_svn139_2821

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_2822

><td class="source">				print &quot;[E] NetGroupEnum failed&quot;<br></td></tr
><tr
id=sl_svn139_2823

><td class="source">				break<br></td></tr
><tr
id=sl_svn139_2824

><td class="source">		sid, s, i = win32security.LookupAccountName(remote_server, group[&#39;name&#39;])<br></td></tr
><tr
id=sl_svn139_2825

><td class="source">		sid_string = win32security.ConvertSidToStringSid(sid)<br></td></tr
><tr
id=sl_svn139_2826

><td class="source">		print &quot;Group %s has sid %s&quot; % (group[&#39;name&#39;], sid_string)<br></td></tr
><tr
id=sl_svn139_2827

><td class="source">		for m in members:<br></td></tr
><tr
id=sl_svn139_2828

><td class="source">			print &quot;Group %s has member: %s&quot; % (group[&#39;name&#39;], m)<br></td></tr
><tr
id=sl_svn139_2829

><td class="source">		if verbose:<br></td></tr
><tr
id=sl_svn139_2830

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_2831

><td class="source">				privs = win32security.LsaEnumerateAccountRights(ph, sid)<br></td></tr
><tr
id=sl_svn139_2832

><td class="source">				for priv in privs:<br></td></tr
><tr
id=sl_svn139_2833

><td class="source">					print &quot;Group %s has privilege: %s&quot; % (group[&#39;name&#39;], priv)<br></td></tr
><tr
id=sl_svn139_2834

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_2835

><td class="source">				print &quot;Group %s has no privileges&quot; % (group[&#39;name&#39;])<br></td></tr
><tr
id=sl_svn139_2836

><td class="source">			<br></td></tr
><tr
id=sl_svn139_2837

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2838

><td class="source">	print &quot;[+] Users&quot;<br></td></tr
><tr
id=sl_svn139_2839

><td class="source">	print<br></td></tr
><tr
id=sl_svn139_2840

><td class="source">	resume = 0<br></td></tr
><tr
id=sl_svn139_2841

><td class="source">	users = []<br></td></tr
><tr
id=sl_svn139_2842

><td class="source">	if verbose:<br></td></tr
><tr
id=sl_svn139_2843

><td class="source">		level = 11<br></td></tr
><tr
id=sl_svn139_2844

><td class="source">	else:<br></td></tr
><tr
id=sl_svn139_2845

><td class="source">		level = 0<br></td></tr
><tr
id=sl_svn139_2846

><td class="source">	while True:<br></td></tr
><tr
id=sl_svn139_2847

><td class="source">		try:<br></td></tr
><tr
id=sl_svn139_2848

><td class="source">			# u, total, resume = win32net.NetUserEnum(remote_server, 11, 0, resume, 999999) # lots of user detail<br></td></tr
><tr
id=sl_svn139_2849

><td class="source">			# u, total, resume = win32net.NetUserEnum(remote_server, 0, 0, resume, 999999) # just the username<br></td></tr
><tr
id=sl_svn139_2850

><td class="source">			u, total, resume = win32net.NetUserEnum(remote_server, level, 0, resume, 999999)<br></td></tr
><tr
id=sl_svn139_2851

><td class="source">			for user in u:<br></td></tr
><tr
id=sl_svn139_2852

><td class="source">				if verbose:<br></td></tr
><tr
id=sl_svn139_2853

><td class="source">					for k in user:<br></td></tr
><tr
id=sl_svn139_2854

><td class="source">						if k != &#39;parms&#39;:<br></td></tr
><tr
id=sl_svn139_2855

><td class="source">							print k + &quot;\t: &quot; + str(user[k])<br></td></tr
><tr
id=sl_svn139_2856

><td class="source">					print <br></td></tr
><tr
id=sl_svn139_2857

><td class="source">				users.append(user[&#39;name&#39;])<br></td></tr
><tr
id=sl_svn139_2858

><td class="source">			if resume == 0:<br></td></tr
><tr
id=sl_svn139_2859

><td class="source">				break<br></td></tr
><tr
id=sl_svn139_2860

><td class="source">		except:<br></td></tr
><tr
id=sl_svn139_2861

><td class="source">			print &quot;[E] NetUserEnum failed&quot;<br></td></tr
><tr
id=sl_svn139_2862

><td class="source">			break<br></td></tr
><tr
id=sl_svn139_2863

><td class="source">			<br></td></tr
><tr
id=sl_svn139_2864

><td class="source">	for user in users:<br></td></tr
><tr
id=sl_svn139_2865

><td class="source">		gprivs = []<br></td></tr
><tr
id=sl_svn139_2866

><td class="source">		sid, s, i = win32security.LookupAccountName(remote_server, user)<br></td></tr
><tr
id=sl_svn139_2867

><td class="source">		sid_string = win32security.ConvertSidToStringSid(sid)<br></td></tr
><tr
id=sl_svn139_2868

><td class="source">		print &quot;User %s has sid %s&quot; % (user, sid_string)<br></td></tr
><tr
id=sl_svn139_2869

><td class="source">		groups = win32net.NetUserGetLocalGroups(remote_server, user, 0)<br></td></tr
><tr
id=sl_svn139_2870

><td class="source">		for group in groups:<br></td></tr
><tr
id=sl_svn139_2871

><td class="source">			gsid, s, i = win32security.LookupAccountName(remote_server, group)<br></td></tr
><tr
id=sl_svn139_2872

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_2873

><td class="source">				privs = win32security.LsaEnumerateAccountRights(ph, gsid)<br></td></tr
><tr
id=sl_svn139_2874

><td class="source">				gprivs = list(list(gprivs) + list(privs))<br></td></tr
><tr
id=sl_svn139_2875

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_2876

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_2877

><td class="source">			print &quot;User %s is in this local group: %s&quot; % (user, group)<br></td></tr
><tr
id=sl_svn139_2878

><td class="source">		group_list = win32net.NetUserGetGroups(remote_server, user)<br></td></tr
><tr
id=sl_svn139_2879

><td class="source">		groups = []<br></td></tr
><tr
id=sl_svn139_2880

><td class="source">		for g in group_list:<br></td></tr
><tr
id=sl_svn139_2881

><td class="source">			groups.append(g[0])<br></td></tr
><tr
id=sl_svn139_2882

><td class="source">		for group in groups:<br></td></tr
><tr
id=sl_svn139_2883

><td class="source">			print &quot;User %s is in this non-local group: %s&quot; % (user, group)<br></td></tr
><tr
id=sl_svn139_2884

><td class="source">		if verbose:<br></td></tr
><tr
id=sl_svn139_2885

><td class="source">			privs = []<br></td></tr
><tr
id=sl_svn139_2886

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_2887

><td class="source">				privs = win32security.LsaEnumerateAccountRights(ph, sid)<br></td></tr
><tr
id=sl_svn139_2888

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_2889

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_2890

><td class="source">			for priv in list(set(list(gprivs) + list(privs))):<br></td></tr
><tr
id=sl_svn139_2891

><td class="source">				print &quot;User %s has privilege %s&quot; % (user, priv)<br></td></tr
><tr
id=sl_svn139_2892

><td class="source"><br></td></tr
><tr
id=sl_svn139_2893

><td class="source">	if verbose:<br></td></tr
><tr
id=sl_svn139_2894

><td class="source">		print<br></td></tr
><tr
id=sl_svn139_2895

><td class="source">		print &quot;[+] Privileges&quot;<br></td></tr
><tr
id=sl_svn139_2896

><td class="source">		print<br></td></tr
><tr
id=sl_svn139_2897

><td class="source">				<br></td></tr
><tr
id=sl_svn139_2898

><td class="source">		for priv in windows_privileges:<br></td></tr
><tr
id=sl_svn139_2899

><td class="source">			try:<br></td></tr
><tr
id=sl_svn139_2900

><td class="source">				for s in win32security.LsaEnumerateAccountsWithUserRight(ph, priv):<br></td></tr
><tr
id=sl_svn139_2901

><td class="source">					priv_desc = &quot;NoDesc!&quot;<br></td></tr
><tr
id=sl_svn139_2902

><td class="source">					try:<br></td></tr
><tr
id=sl_svn139_2903

><td class="source">						priv_desc = win32security.LookupPrivilegeDisplayName(remote_server, priv)<br></td></tr
><tr
id=sl_svn139_2904

><td class="source">					except:<br></td></tr
><tr
id=sl_svn139_2905

><td class="source">						pass<br></td></tr
><tr
id=sl_svn139_2906

><td class="source">						<br></td></tr
><tr
id=sl_svn139_2907

><td class="source">					name, domain, type = win32security.LookupAccountSid(remote_server, s)<br></td></tr
><tr
id=sl_svn139_2908

><td class="source">					type_string = &quot;unknown_type&quot;<br></td></tr
><tr
id=sl_svn139_2909

><td class="source">					if type == 4:<br></td></tr
><tr
id=sl_svn139_2910

><td class="source">						type_string = &quot;group&quot;<br></td></tr
><tr
id=sl_svn139_2911

><td class="source">					if type == 5:<br></td></tr
><tr
id=sl_svn139_2912

><td class="source">						type_string = &quot;user&quot;<br></td></tr
><tr
id=sl_svn139_2913

><td class="source">					print &quot;Privilege %s (%s) is held by %s\%s (%s)&quot; % (priv, priv_desc, domain, name, type_string)<br></td></tr
><tr
id=sl_svn139_2914

><td class="source">					# print &quot;Privilege %s is held by %s\%s (%s)&quot; % (priv, domain, name, type_string)<br></td></tr
><tr
id=sl_svn139_2915

><td class="source">			except:<br></td></tr
><tr
id=sl_svn139_2916

><td class="source">				#print &quot;Skipping %s - doesn&#39;t exist for this platform&quot; % priv<br></td></tr
><tr
id=sl_svn139_2917

><td class="source">				pass<br></td></tr
><tr
id=sl_svn139_2918

><td class="source"><br></td></tr
><tr
id=sl_svn139_2919

><td class="source">print &quot;windows-privesc-check v%s (http://pentestmonkey.net/windows-privesc-check)\n&quot; % version<br></td></tr
><tr
id=sl_svn139_2920

><td class="source"><br></td></tr
><tr
id=sl_svn139_2921

><td class="source"># Process Command Line Options<br></td></tr
><tr
id=sl_svn139_2922

><td class="source">try:<br></td></tr
><tr
id=sl_svn139_2923

><td class="source">	opts, args = getopt.getopt(sys.argv[1:], &quot;artSDEPRHUOMAFILIehwiWvo:s:u:p:d:&quot;, [&quot;help&quot;, &quot;verbose&quot;, &quot;all_checks&quot;, &quot;registry_checks&quot;, &quot;path_checks&quot;, &quot;service_checks&quot;, &quot;services&quot;, &quot;drive_checks&quot;, &quot;eventlog_checks&quot;, &quot;progfiles_checks&quot;, &quot;passpol&quot;, &quot;process_checks&quot;, &quot;share_checks&quot;, &quot;user_groups&quot;, &quot;processes&quot;, &quot;ignore_trusted&quot;, &quot;owner_info&quot;, &quot;write_perms_only&quot;, &quot;domain&quot;, &quot;patch_checks&quot;, &quot;admin_users&quot;, &quot;host_info&quot;, &quot;logged_in&quot;, &quot;report_file=&quot;, &quot;username=&quot;, &quot;password=&quot;, &quot;domain=&quot;, &quot;server=&quot;])<br></td></tr
><tr
id=sl_svn139_2924

><td class="source">except getopt.GetoptError, err:<br></td></tr
><tr
id=sl_svn139_2925

><td class="source">	# print help information and exit:<br></td></tr
><tr
id=sl_svn139_2926

><td class="source">	print str(err) # will print something like &quot;option -a not recognized&quot;<br></td></tr
><tr
id=sl_svn139_2927

><td class="source">	usage()<br></td></tr
><tr
id=sl_svn139_2928

><td class="source">	sys.exit(2)<br></td></tr
><tr
id=sl_svn139_2929

><td class="source">output = None<br></td></tr
><tr
id=sl_svn139_2930

><td class="source">for o, a in opts:<br></td></tr
><tr
id=sl_svn139_2931

><td class="source">	if o in (&quot;-a&quot;, &quot;--all_checks&quot;):<br></td></tr
><tr
id=sl_svn139_2932

><td class="source">		all_checks = 1<br></td></tr
><tr
id=sl_svn139_2933

><td class="source">	elif o in (&quot;-r&quot;, &quot;--registry_checks&quot;):<br></td></tr
><tr
id=sl_svn139_2934

><td class="source">		registry_checks = 1<br></td></tr
><tr
id=sl_svn139_2935

><td class="source">	elif o in (&quot;-t&quot;, &quot;--path_checks&quot;):<br></td></tr
><tr
id=sl_svn139_2936

><td class="source">		path_checks = 1<br></td></tr
><tr
id=sl_svn139_2937

><td class="source">	elif o in (&quot;-S&quot;, &quot;--service_checks&quot;):<br></td></tr
><tr
id=sl_svn139_2938

><td class="source">		service_checks = 1<br></td></tr
><tr
id=sl_svn139_2939

><td class="source">	elif o in (&quot;-D&quot;, &quot;--drive_checks&quot;):<br></td></tr
><tr
id=sl_svn139_2940

><td class="source">		drive_checks = 1<br></td></tr
><tr
id=sl_svn139_2941

><td class="source">	elif o in (&quot;-E&quot;, &quot;--eventlog_checks&quot;):<br></td></tr
><tr
id=sl_svn139_2942

><td class="source">		eventlog_checks = 1<br></td></tr
><tr
id=sl_svn139_2943

><td class="source">	elif o in (&quot;-F&quot;, &quot;--progfiles_checks&quot;):<br></td></tr
><tr
id=sl_svn139_2944

><td class="source">		progfiles_checks = 1<br></td></tr
><tr
id=sl_svn139_2945

><td class="source">	elif o in (&quot;-R&quot;, &quot;--process_checks&quot;):<br></td></tr
><tr
id=sl_svn139_2946

><td class="source">		process_checks = 1<br></td></tr
><tr
id=sl_svn139_2947

><td class="source">	elif o in (&quot;-H&quot;, &quot;--share_checks&quot;):<br></td></tr
><tr
id=sl_svn139_2948

><td class="source">		share_checks = 1<br></td></tr
><tr
id=sl_svn139_2949

><td class="source">#	elif o in (&quot;-T&quot;, &quot;--patch_checks&quot;):<br></td></tr
><tr
id=sl_svn139_2950

><td class="source">#		patch_checks = 1<br></td></tr
><tr
id=sl_svn139_2951

><td class="source">	elif o in (&quot;-L&quot;, &quot;--logged_in_audit&quot;):<br></td></tr
><tr
id=sl_svn139_2952

><td class="source">		logged_in_audit = 1<br></td></tr
><tr
id=sl_svn139_2953

><td class="source">	elif o in (&quot;-U&quot;, &quot;--user_group_audit&quot;):<br></td></tr
><tr
id=sl_svn139_2954

><td class="source">		user_group_audit = 1<br></td></tr
><tr
id=sl_svn139_2955

><td class="source">	elif o in (&quot;-P&quot;, &quot;--passpol&quot;):<br></td></tr
><tr
id=sl_svn139_2956

><td class="source">		passpol_audit = 1<br></td></tr
><tr
id=sl_svn139_2957

><td class="source">	elif o in (&quot;-A&quot;, &quot;--admin_users_audit&quot;):<br></td></tr
><tr
id=sl_svn139_2958

><td class="source">		admin_users_audit = 1<br></td></tr
><tr
id=sl_svn139_2959

><td class="source">	elif o in (&quot;-O&quot;, &quot;--process_audit&quot;):<br></td></tr
><tr
id=sl_svn139_2960

><td class="source">		process_audit = 1<br></td></tr
><tr
id=sl_svn139_2961

><td class="source">	elif o in (&quot;-i&quot;, &quot;--host_info&quot;):<br></td></tr
><tr
id=sl_svn139_2962

><td class="source">		host_info_audit = 1<br></td></tr
><tr
id=sl_svn139_2963

><td class="source">	elif o in (&quot;-e&quot;, &quot;--services&quot;):<br></td></tr
><tr
id=sl_svn139_2964

><td class="source">		service_audit = 1<br></td></tr
><tr
id=sl_svn139_2965

><td class="source">	elif o in (&quot;-h&quot;, &quot;--help&quot;):<br></td></tr
><tr
id=sl_svn139_2966

><td class="source">		usage()<br></td></tr
><tr
id=sl_svn139_2967

><td class="source">		sys.exit()<br></td></tr
><tr
id=sl_svn139_2968

><td class="source">	elif o in (&quot;-w&quot;, &quot;--write_perms_only&quot;):<br></td></tr
><tr
id=sl_svn139_2969

><td class="source">		weak_perms_only = 1<br></td></tr
><tr
id=sl_svn139_2970

><td class="source">	elif o in (&quot;-I&quot;, &quot;--ignore_trusted&quot;):<br></td></tr
><tr
id=sl_svn139_2971

><td class="source">		ignore_trusted = 1<br></td></tr
><tr
id=sl_svn139_2972

><td class="source">	elif o in (&quot;-W&quot;, &quot;--owner_info&quot;):<br></td></tr
><tr
id=sl_svn139_2973

><td class="source">		owner_info  = 1<br></td></tr
><tr
id=sl_svn139_2974

><td class="source">	elif o in (&quot;-v&quot;, &quot;--verbose&quot;):<br></td></tr
><tr
id=sl_svn139_2975

><td class="source">		verbose = verbose + 1<br></td></tr
><tr
id=sl_svn139_2976

><td class="source">	elif o in (&quot;-o&quot;, &quot;--report_file&quot;):<br></td></tr
><tr
id=sl_svn139_2977

><td class="source">		report_file_name = a<br></td></tr
><tr
id=sl_svn139_2978

><td class="source">	elif o in (&quot;-s&quot;, &quot;--server&quot;):<br></td></tr
><tr
id=sl_svn139_2979

><td class="source">		remote_server = a<br></td></tr
><tr
id=sl_svn139_2980

><td class="source">		print &quot;Remote server selected: &quot; + a<br></td></tr
><tr
id=sl_svn139_2981

><td class="source">	elif o in (&quot;-u&quot;, &quot;--username&quot;):<br></td></tr
><tr
id=sl_svn139_2982

><td class="source">		remote_username = a<br></td></tr
><tr
id=sl_svn139_2983

><td class="source">	elif o in (&quot;-p&quot;, &quot;--password&quot;):<br></td></tr
><tr
id=sl_svn139_2984

><td class="source">		remote_password = a<br></td></tr
><tr
id=sl_svn139_2985

><td class="source">	elif o in (&quot;-d&quot;, &quot;--domain&quot;):<br></td></tr
><tr
id=sl_svn139_2986

><td class="source">		remote_domain = a<br></td></tr
><tr
id=sl_svn139_2987

><td class="source">	else:<br></td></tr
><tr
id=sl_svn139_2988

><td class="source">		assert False, &quot;unhandled option&quot;<br></td></tr
><tr
id=sl_svn139_2989

><td class="source"><br></td></tr
><tr
id=sl_svn139_2990

><td class="source">if all_checks:<br></td></tr
><tr
id=sl_svn139_2991

><td class="source">	registry_checks  = 1<br></td></tr
><tr
id=sl_svn139_2992

><td class="source">	path_checks      = 1<br></td></tr
><tr
id=sl_svn139_2993

><td class="source">	service_checks   = 1<br></td></tr
><tr
id=sl_svn139_2994

><td class="source">	service_audit    = 1<br></td></tr
><tr
id=sl_svn139_2995

><td class="source">	drive_checks     = 1<br></td></tr
><tr
id=sl_svn139_2996

><td class="source">	eventlog_checks  = 1<br></td></tr
><tr
id=sl_svn139_2997

><td class="source">	progfiles_checks = 1<br></td></tr
><tr
id=sl_svn139_2998

><td class="source">	process_checks   = 1<br></td></tr
><tr
id=sl_svn139_2999

><td class="source">	share_checks     = 1<br></td></tr
><tr
id=sl_svn139_3000

><td class="source">	user_group_audit = 1<br></td></tr
><tr
id=sl_svn139_3001

><td class="source">	passpol_audit    = 1<br></td></tr
><tr
id=sl_svn139_3002

><td class="source">	logged_in_audit  = 1<br></td></tr
><tr
id=sl_svn139_3003

><td class="source">	admin_users_audit= 1<br></td></tr
><tr
id=sl_svn139_3004

><td class="source">	host_info_audit  = 1<br></td></tr
><tr
id=sl_svn139_3005

><td class="source">	patch_checks     = 1<br></td></tr
><tr
id=sl_svn139_3006

><td class="source">	process_audit    = 1<br></td></tr
><tr
id=sl_svn139_3007

><td class="source"><br></td></tr
><tr
id=sl_svn139_3008

><td class="source"># Print usage message unless at least on type of check is selected<br></td></tr
><tr
id=sl_svn139_3009

><td class="source">if not (<br></td></tr
><tr
id=sl_svn139_3010

><td class="source">	registry_checks  or<br></td></tr
><tr
id=sl_svn139_3011

><td class="source">	path_checks      or<br></td></tr
><tr
id=sl_svn139_3012

><td class="source">	service_checks   or<br></td></tr
><tr
id=sl_svn139_3013

><td class="source">	service_audit    or<br></td></tr
><tr
id=sl_svn139_3014

><td class="source">	drive_checks     or<br></td></tr
><tr
id=sl_svn139_3015

><td class="source">	eventlog_checks  or<br></td></tr
><tr
id=sl_svn139_3016

><td class="source">	progfiles_checks or<br></td></tr
><tr
id=sl_svn139_3017

><td class="source">	process_checks   or<br></td></tr
><tr
id=sl_svn139_3018

><td class="source">    share_checks     or<br></td></tr
><tr
id=sl_svn139_3019

><td class="source">	logged_in_audit  or<br></td></tr
><tr
id=sl_svn139_3020

><td class="source">	user_group_audit or<br></td></tr
><tr
id=sl_svn139_3021

><td class="source">	passpol_audit    or<br></td></tr
><tr
id=sl_svn139_3022

><td class="source">	admin_users_audit or<br></td></tr
><tr
id=sl_svn139_3023

><td class="source">	host_info_audit  or<br></td></tr
><tr
id=sl_svn139_3024

><td class="source">	process_audit    or<br></td></tr
><tr
id=sl_svn139_3025

><td class="source">	patch_checks<br></td></tr
><tr
id=sl_svn139_3026

><td class="source">):<br></td></tr
><tr
id=sl_svn139_3027

><td class="source">	usage()<br></td></tr
><tr
id=sl_svn139_3028

><td class="source"><br></td></tr
><tr
id=sl_svn139_3029

><td class="source">if report_file_name == None:<br></td></tr
><tr
id=sl_svn139_3030

><td class="source">	report_file_name = &quot;privesc-report-&quot; + socket.gethostname() + &quot;.html&quot;<br></td></tr
><tr
id=sl_svn139_3031

><td class="source"><br></td></tr
><tr
id=sl_svn139_3032

><td class="source"># Better open the report file now in case there&#39;s a permissions problem<br></td></tr
><tr
id=sl_svn139_3033

><td class="source">REPORT = open(report_file_name,&quot;w&quot;)<br></td></tr
><tr
id=sl_svn139_3034

><td class="source"><br></td></tr
><tr
id=sl_svn139_3035

><td class="source"># Print out scan parameters<br></td></tr
><tr
id=sl_svn139_3036

><td class="source">print &quot;Audit parameters:&quot;<br></td></tr
><tr
id=sl_svn139_3037

><td class="source">print &quot;Registry Checks: ....... &quot; + str(registry_checks)<br></td></tr
><tr
id=sl_svn139_3038

><td class="source">print &quot;PATH Checks: ........... &quot; + str(path_checks)<br></td></tr
><tr
id=sl_svn139_3039

><td class="source">print &quot;Service Checks: ........ &quot; + str(service_checks)<br></td></tr
><tr
id=sl_svn139_3040

><td class="source">print &quot;Eventlog Checks: ....... &quot; + str(drive_checks)<br></td></tr
><tr
id=sl_svn139_3041

><td class="source">print &quot;Program Files Checks: .. &quot; + str(eventlog_checks)<br></td></tr
><tr
id=sl_svn139_3042

><td class="source">print &quot;Process Checks: ........ &quot; + str(progfiles_checks)<br></td></tr
><tr
id=sl_svn139_3043

><td class="source">print &quot;Patch Checks: ...........&quot; + str(patch_checks)<br></td></tr
><tr
id=sl_svn139_3044

><td class="source">print &quot;User/Group Audit: ...... &quot; + str(user_group_audit)<br></td></tr
><tr
id=sl_svn139_3045

><td class="source">print &quot;Password Policy Audit .. &quot; + str(passpol_audit)<br></td></tr
><tr
id=sl_svn139_3046

><td class="source">print &quot;Logged-in User Audit ... &quot; + str(logged_in_audit)<br></td></tr
><tr
id=sl_svn139_3047

><td class="source">print &quot;Admin Users Audit: ..... &quot; + str(admin_users_audit)<br></td></tr
><tr
id=sl_svn139_3048

><td class="source">print &quot;Host Info Audit: ....... &quot; + str(host_info_audit)<br></td></tr
><tr
id=sl_svn139_3049

><td class="source">print &quot;Process Audit: ......... &quot; + str(process_audit)<br></td></tr
><tr
id=sl_svn139_3050

><td class="source">print &quot;Service Audit .......... &quot; + str(service_audit)<br></td></tr
><tr
id=sl_svn139_3051

><td class="source">print &quot;Ignore Trusted ......... &quot; + str(ignore_trusted)<br></td></tr
><tr
id=sl_svn139_3052

><td class="source">print &quot;Owner Info ............. &quot; + str(owner_info)<br></td></tr
><tr
id=sl_svn139_3053

><td class="source">print &quot;Weak Perms Only ........ &quot; + str(weak_perms_only)<br></td></tr
><tr
id=sl_svn139_3054

><td class="source">print &quot;Verbosity .............. &quot; + str(verbose)<br></td></tr
><tr
id=sl_svn139_3055

><td class="source">print &quot;Output File: ........... &quot; + report_file_name<br></td></tr
><tr
id=sl_svn139_3056

><td class="source">print<br></td></tr
><tr
id=sl_svn139_3057

><td class="source"><br></td></tr
><tr
id=sl_svn139_3058

><td class="source">impersonate(remote_username, remote_password, remote_domain)<br></td></tr
><tr
id=sl_svn139_3059

><td class="source"><br></td></tr
><tr
id=sl_svn139_3060

><td class="source"># Load win32security<br></td></tr
><tr
id=sl_svn139_3061

><td class="source">#<br></td></tr
><tr
id=sl_svn139_3062

><td class="source"># Try to open file and ingore the result.  This gets win32security loaded and working.<br></td></tr
><tr
id=sl_svn139_3063

><td class="source"># We can then turn off WOW64 and call repeatedly.  If we turn off WOW64 first, <br></td></tr
><tr
id=sl_svn139_3064

><td class="source"># win32security will fail to work properly.<br></td></tr
><tr
id=sl_svn139_3065

><td class="source"><br></td></tr
><tr
id=sl_svn139_3066

><td class="source">try:<br></td></tr
><tr
id=sl_svn139_3067

><td class="source">	sd = win32security.GetNamedSecurityInfo (<br></td></tr
><tr
id=sl_svn139_3068

><td class="source">		&quot;.&quot;,<br></td></tr
><tr
id=sl_svn139_3069

><td class="source">		win32security.SE_FILE_OBJECT,<br></td></tr
><tr
id=sl_svn139_3070

><td class="source">		win32security.OWNER_SECURITY_INFORMATION | win32security.DACL_SECURITY_INFORMATION<br></td></tr
><tr
id=sl_svn139_3071

><td class="source">	)<br></td></tr
><tr
id=sl_svn139_3072

><td class="source">except:<br></td></tr
><tr
id=sl_svn139_3073

><td class="source">	# nothing<br></td></tr
><tr
id=sl_svn139_3074

><td class="source">	pass<br></td></tr
><tr
id=sl_svn139_3075

><td class="source"><br></td></tr
><tr
id=sl_svn139_3076

><td class="source"># Load win32net<br></td></tr
><tr
id=sl_svn139_3077

><td class="source">#<br></td></tr
><tr
id=sl_svn139_3078

><td class="source"># NetLocalGroupEnum fails with like under Windows 7 64-bit, but not XP 32-bit:<br></td></tr
><tr
id=sl_svn139_3079

><td class="source"># pywintypes.error: (127, &#39;NetLocalGroupEnum&#39;, &#39;The specified procedure could not be found.&#39;)<br></td></tr
><tr
id=sl_svn139_3080

><td class="source">dummy = win32net.NetLocalGroupEnum(None, 0, 0, 1000)<br></td></tr
><tr
id=sl_svn139_3081

><td class="source"><br></td></tr
><tr
id=sl_svn139_3082

><td class="source"># Disable WOW64 - we WANT to see 32-bit areas of the filesystem<br></td></tr
><tr
id=sl_svn139_3083

><td class="source">#<br></td></tr
><tr
id=sl_svn139_3084

><td class="source"># Need to wrap in a try because the following call will error on 32-bit windows<br></td></tr
><tr
id=sl_svn139_3085

><td class="source">try:<br></td></tr
><tr
id=sl_svn139_3086

><td class="source">	k32.Wow64DisableWow64FsRedirection( ctypes.byref(wow64) )<br></td></tr
><tr
id=sl_svn139_3087

><td class="source">except:<br></td></tr
><tr
id=sl_svn139_3088

><td class="source">	on64bitwindows = 0<br></td></tr
><tr
id=sl_svn139_3089

><td class="source"># WOW64 is now disabled, so we can read file permissions without Windows redirecting us from system32 to syswow64<br></td></tr
><tr
id=sl_svn139_3090

><td class="source"><br></td></tr
><tr
id=sl_svn139_3091

><td class="source"># Run checks<br></td></tr
><tr
id=sl_svn139_3092

><td class="source"><br></td></tr
><tr
id=sl_svn139_3093

><td class="source">if registry_checks:<br></td></tr
><tr
id=sl_svn139_3094

><td class="source">	print_section(&quot;Registry Checks&quot;)<br></td></tr
><tr
id=sl_svn139_3095

><td class="source">	check_registry()<br></td></tr
><tr
id=sl_svn139_3096

><td class="source"><br></td></tr
><tr
id=sl_svn139_3097

><td class="source">if path_checks:<br></td></tr
><tr
id=sl_svn139_3098

><td class="source">	print_section(&quot;PATH Checks&quot;)<br></td></tr
><tr
id=sl_svn139_3099

><td class="source">	check_paths()<br></td></tr
><tr
id=sl_svn139_3100

><td class="source"><br></td></tr
><tr
id=sl_svn139_3101

><td class="source">if service_checks:<br></td></tr
><tr
id=sl_svn139_3102

><td class="source">	print_section(&quot;Service Checks&quot;)<br></td></tr
><tr
id=sl_svn139_3103

><td class="source">	check_services()<br></td></tr
><tr
id=sl_svn139_3104

><td class="source"><br></td></tr
><tr
id=sl_svn139_3105

><td class="source">if service_audit:<br></td></tr
><tr
id=sl_svn139_3106

><td class="source">	print_section(&quot;Service Audit&quot;)<br></td></tr
><tr
id=sl_svn139_3107

><td class="source">	audit_services()<br></td></tr
><tr
id=sl_svn139_3108

><td class="source"><br></td></tr
><tr
id=sl_svn139_3109

><td class="source">if drive_checks:<br></td></tr
><tr
id=sl_svn139_3110

><td class="source">	print_section(&quot;Drive Checks&quot;)<br></td></tr
><tr
id=sl_svn139_3111

><td class="source">	check_drives()<br></td></tr
><tr
id=sl_svn139_3112

><td class="source"><br></td></tr
><tr
id=sl_svn139_3113

><td class="source">if eventlog_checks:<br></td></tr
><tr
id=sl_svn139_3114

><td class="source">	print_section(&quot;Event Log Checks&quot;)<br></td></tr
><tr
id=sl_svn139_3115

><td class="source">	check_event_logs()<br></td></tr
><tr
id=sl_svn139_3116

><td class="source"><br></td></tr
><tr
id=sl_svn139_3117

><td class="source">if progfiles_checks:<br></td></tr
><tr
id=sl_svn139_3118

><td class="source">	print_section(&quot;Program Files Checks&quot;)<br></td></tr
><tr
id=sl_svn139_3119

><td class="source">	check_progfiles()<br></td></tr
><tr
id=sl_svn139_3120

><td class="source"><br></td></tr
><tr
id=sl_svn139_3121

><td class="source">if process_checks:<br></td></tr
><tr
id=sl_svn139_3122

><td class="source">	print_section(&quot;Process Checks&quot;)<br></td></tr
><tr
id=sl_svn139_3123

><td class="source">	check_processes()<br></td></tr
><tr
id=sl_svn139_3124

><td class="source"><br></td></tr
><tr
id=sl_svn139_3125

><td class="source">if share_checks:<br></td></tr
><tr
id=sl_svn139_3126

><td class="source">	print_section(&quot;Share Checks&quot;)<br></td></tr
><tr
id=sl_svn139_3127

><td class="source">	check_shares()<br></td></tr
><tr
id=sl_svn139_3128

><td class="source"><br></td></tr
><tr
id=sl_svn139_3129

><td class="source">if logged_in_audit:<br></td></tr
><tr
id=sl_svn139_3130

><td class="source">	print_section(&quot;Logged-in User Audit&quot;)<br></td></tr
><tr
id=sl_svn139_3131

><td class="source">	audit_logged_in()<br></td></tr
><tr
id=sl_svn139_3132

><td class="source">	<br></td></tr
><tr
id=sl_svn139_3133

><td class="source">if user_group_audit:<br></td></tr
><tr
id=sl_svn139_3134

><td class="source">	print_section(&quot;User/Group Audit&quot;)<br></td></tr
><tr
id=sl_svn139_3135

><td class="source">	audit_user_group()<br></td></tr
><tr
id=sl_svn139_3136

><td class="source">	<br></td></tr
><tr
id=sl_svn139_3137

><td class="source">if passpol_audit:<br></td></tr
><tr
id=sl_svn139_3138

><td class="source">	print_section(&quot;Password Policy&quot;)<br></td></tr
><tr
id=sl_svn139_3139

><td class="source">	audit_passpol()<br></td></tr
><tr
id=sl_svn139_3140

><td class="source"><br></td></tr
><tr
id=sl_svn139_3141

><td class="source">if admin_users_audit:<br></td></tr
><tr
id=sl_svn139_3142

><td class="source">	print_section(&quot;Admin Users Audit&quot;)<br></td></tr
><tr
id=sl_svn139_3143

><td class="source">	audit_admin_users()<br></td></tr
><tr
id=sl_svn139_3144

><td class="source">	<br></td></tr
><tr
id=sl_svn139_3145

><td class="source">if host_info_audit:<br></td></tr
><tr
id=sl_svn139_3146

><td class="source">	print_section(&quot;Host Info Audit&quot;)<br></td></tr
><tr
id=sl_svn139_3147

><td class="source">	audit_host_info()<br></td></tr
><tr
id=sl_svn139_3148

><td class="source">	<br></td></tr
><tr
id=sl_svn139_3149

><td class="source">if process_audit:<br></td></tr
><tr
id=sl_svn139_3150

><td class="source">	print_section(&quot;Process Audit&quot;)<br></td></tr
><tr
id=sl_svn139_3151

><td class="source">	audit_processes()<br></td></tr
><tr
id=sl_svn139_3152

><td class="source"><br></td></tr
><tr
id=sl_svn139_3153

><td class="source">if patch_checks:<br></td></tr
><tr
id=sl_svn139_3154

><td class="source">	print_section(&quot;Patch Checks&quot;)<br></td></tr
><tr
id=sl_svn139_3155

><td class="source">	check_patches()<br></td></tr
><tr
id=sl_svn139_3156

><td class="source"><br></td></tr
><tr
id=sl_svn139_3157

><td class="source">	# task_name=&#39;test_addtask.job&#39;<br></td></tr
><tr
id=sl_svn139_3158

><td class="source"># ts=pythoncom.CoCreateInstance(taskscheduler.CLSID_CTaskScheduler,None,pythoncom.CLSCTX_INPROC_SERVER,taskscheduler.IID_ITaskScheduler)<br></td></tr
><tr
id=sl_svn139_3159

><td class="source"># tasks=ts.Enum()<br></td></tr
><tr
id=sl_svn139_3160

><td class="source"># for task in tasks:<br></td></tr
><tr
id=sl_svn139_3161

><td class="source">    # print task<br></td></tr
><tr
id=sl_svn139_3162

><td class="source"># print issues<br></td></tr
><tr
id=sl_svn139_3163

><td class="source"><br></td></tr
><tr
id=sl_svn139_3164

><td class="source"># Generate report<br></td></tr
><tr
id=sl_svn139_3165

><td class="source"><br></td></tr
><tr
id=sl_svn139_3166

><td class="source">audit_data = {}<br></td></tr
><tr
id=sl_svn139_3167

><td class="source"><br></td></tr
><tr
id=sl_svn139_3168

><td class="source">audit_data[&#39;hostname&#39;] = socket.gethostname()<br></td></tr
><tr
id=sl_svn139_3169

><td class="source">ver_list = win32api.GetVersionEx(1)<br></td></tr
><tr
id=sl_svn139_3170

><td class="source">os_ver = str(ver_list[0]) + &quot;.&quot; + str(ver_list[1])<br></td></tr
><tr
id=sl_svn139_3171

><td class="source"># version numbers from http://msdn.microsoft.com/en-us/library/ms724832(VS.85).aspx<br></td></tr
><tr
id=sl_svn139_3172

><td class="source">if os_ver == &quot;4.0&quot;:<br></td></tr
><tr
id=sl_svn139_3173

><td class="source">	os_str = &quot;Windows NT&quot;<br></td></tr
><tr
id=sl_svn139_3174

><td class="source">if os_ver == &quot;5.0&quot;:<br></td></tr
><tr
id=sl_svn139_3175

><td class="source">	os_str = &quot;Windows 2000&quot;<br></td></tr
><tr
id=sl_svn139_3176

><td class="source">if os_ver == &quot;5.1&quot;:<br></td></tr
><tr
id=sl_svn139_3177

><td class="source">	os_str = &quot;Windows XP&quot;<br></td></tr
><tr
id=sl_svn139_3178

><td class="source">if os_ver == &quot;5.2&quot;:<br></td></tr
><tr
id=sl_svn139_3179

><td class="source">	os_str = &quot;Windows 2003&quot;<br></td></tr
><tr
id=sl_svn139_3180

><td class="source">if os_ver == &quot;6.0&quot;:<br></td></tr
><tr
id=sl_svn139_3181

><td class="source">	os_str = &quot;Windows Vista&quot;<br></td></tr
><tr
id=sl_svn139_3182

><td class="source">if os_ver == &quot;6.0&quot;:<br></td></tr
><tr
id=sl_svn139_3183

><td class="source">	os_str = &quot;Windows 2008&quot;<br></td></tr
><tr
id=sl_svn139_3184

><td class="source">if os_ver == &quot;6.1&quot;:<br></td></tr
><tr
id=sl_svn139_3185

><td class="source">	os_str = &quot;Windows 2008 R2&quot;<br></td></tr
><tr
id=sl_svn139_3186

><td class="source">if os_ver == &quot;6.1&quot;:<br></td></tr
><tr
id=sl_svn139_3187

><td class="source">	os_str = &quot;Windows 7&quot;<br></td></tr
><tr
id=sl_svn139_3188

><td class="source">	<br></td></tr
><tr
id=sl_svn139_3189

><td class="source">audit_data[&#39;os_name&#39;] = os_str<br></td></tr
><tr
id=sl_svn139_3190

><td class="source"># print ver_list<br></td></tr
><tr
id=sl_svn139_3191

><td class="source"># audit_data[&#39;os_version&#39;] = str(ver_list[0]) + &quot;.&quot; + str(ver_list[1]) + &quot;.&quot; + str(ver_list[2]) + &quot; SP&quot; + str(ver_list[5])+ &quot;.&quot; + str(ver_list[6]) <br></td></tr
><tr
id=sl_svn139_3192

><td class="source">audit_data[&#39;os_version&#39;] = str(ver_list[0]) + &quot;.&quot; + str(ver_list[1]) + &quot;.&quot; + str(ver_list[2]) + &quot; SP&quot; + str(ver_list[5])<br></td></tr
><tr
id=sl_svn139_3193

><td class="source"># http://msdn.microsoft.com/en-us/library/ms724429(VS.85).aspx<br></td></tr
><tr
id=sl_svn139_3194

><td class="source">audit_data[&#39;ips&#39;] = local_ips<br></td></tr
><tr
id=sl_svn139_3195

><td class="source">audit_data[&#39;domwkg&#39;] = win32api.GetDomainName()<br></td></tr
><tr
id=sl_svn139_3196

><td class="source">audit_data[&#39;version&#39;] = version<br></td></tr
><tr
id=sl_svn139_3197

><td class="source">audit_data[&#39;datetime&#39;] = datetime.datetime.now().strftime(&quot;%Y-%m-%d %H:%M&quot;)<br></td></tr
><tr
id=sl_svn139_3198

><td class="source">audit_data[&#39;audit_user&#39;] = os.environ[&#39;USERDOMAIN&#39;] + &quot;\\&quot; + os.environ[&#39;USERNAME&#39;]<br></td></tr
><tr
id=sl_svn139_3199

><td class="source">audit_data[&#39;trusted_users&#39;] = trusted_principles_fq<br></td></tr
><tr
id=sl_svn139_3200

><td class="source">audit_data[&#39;trusted_groups&#39;] = trusted_principles<br></td></tr
><tr
id=sl_svn139_3201

><td class="source">audit_data[&#39;dangerous_privs&#39;] = &#39;somedangerous_privs&#39;<br></td></tr
><tr
id=sl_svn139_3202

><td class="source"><br></td></tr
><tr
id=sl_svn139_3203

><td class="source">REPORT.write(format_issues(&quot;html&quot;, issue_template, issues))<br></td></tr
><tr
id=sl_svn139_3204

><td class="source">REPORT.close<br></td></tr
><tr
id=sl_svn139_3205

><td class="source">print<br></td></tr
><tr
id=sl_svn139_3206

><td class="source">print<br></td></tr
><tr
id=sl_svn139_3207

><td class="source">print &quot;Report saved to &quot; + report_file_name<br></td></tr
><tr
id=sl_svn139_3208

><td class="source">print<br></td></tr
></table></pre>
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
</td>
</tr></table>

 
<script type="text/javascript">
 var lineNumUnderMouse = -1;
 
 function gutterOver(num) {
 gutterOut();
 var newTR = document.getElementById('gr_svn139_' + num);
 if (newTR) {
 newTR.className = 'undermouse';
 }
 lineNumUnderMouse = num;
 }
 function gutterOut() {
 if (lineNumUnderMouse != -1) {
 var oldTR = document.getElementById(
 'gr_svn139_' + lineNumUnderMouse);
 if (oldTR) {
 oldTR.className = '';
 }
 lineNumUnderMouse = -1;
 }
 }
 var numsGenState = {table_base_id: 'nums_table_'};
 var srcGenState = {table_base_id: 'src_table_'};
 var alignerRunning = false;
 var startOver = false;
 function setLineNumberHeights() {
 if (alignerRunning) {
 startOver = true;
 return;
 }
 numsGenState.chunk_id = 0;
 numsGenState.table = document.getElementById('nums_table_0');
 numsGenState.row_num = 0;
 if (!numsGenState.table) {
 return; // Silently exit if no file is present.
 }
 srcGenState.chunk_id = 0;
 srcGenState.table = document.getElementById('src_table_0');
 srcGenState.row_num = 0;
 alignerRunning = true;
 continueToSetLineNumberHeights();
 }
 function rowGenerator(genState) {
 if (genState.row_num < genState.table.rows.length) {
 var currentRow = genState.table.rows[genState.row_num];
 genState.row_num++;
 return currentRow;
 }
 var newTable = document.getElementById(
 genState.table_base_id + (genState.chunk_id + 1));
 if (newTable) {
 genState.chunk_id++;
 genState.row_num = 0;
 genState.table = newTable;
 return genState.table.rows[0];
 }
 return null;
 }
 var MAX_ROWS_PER_PASS = 1000;
 function continueToSetLineNumberHeights() {
 var rowsInThisPass = 0;
 var numRow = 1;
 var srcRow = 1;
 while (numRow && srcRow && rowsInThisPass < MAX_ROWS_PER_PASS) {
 numRow = rowGenerator(numsGenState);
 srcRow = rowGenerator(srcGenState);
 rowsInThisPass++;
 if (numRow && srcRow) {
 if (numRow.offsetHeight != srcRow.offsetHeight) {
 numRow.firstChild.style.height = srcRow.offsetHeight + 'px';
 }
 }
 }
 if (rowsInThisPass >= MAX_ROWS_PER_PASS) {
 setTimeout(continueToSetLineNumberHeights, 10);
 } else {
 alignerRunning = false;
 if (startOver) {
 startOver = false;
 setTimeout(setLineNumberHeights, 500);
 }
 }
 }
 function initLineNumberHeights() {
 // Do 2 complete passes, because there can be races
 // between this code and prettify.
 startOver = true;
 setTimeout(setLineNumberHeights, 250);
 window.onresize = setLineNumberHeights;
 }
 initLineNumberHeights();
</script>

 
 
 <div id="log">
 <div style="text-align:right">
 <a class="ifCollapse" href="#" onclick="_toggleMeta(this); return false">Show details</a>
 <a class="ifExpand" href="#" onclick="_toggleMeta(this); return false">Hide details</a>
 </div>
 <div class="ifExpand">
 
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="changelog">
 <p>Change log</p>
 <div>
 <a href="/p/windows-privesc-check/source/detail?spec=svn139&amp;r=24">r24</a>
 by pentestmonkey
 on Feb 22, 2011
 &nbsp; <a href="/p/windows-privesc-check/source/diff?spec=svn139&r=24&amp;format=side&amp;path=/trunk/windows-privesc-check.py&amp;old_path=/trunk/windows-privesc-check.py&amp;old=23">Diff</a>
 </div>
 <pre>Bug fix: -i now works as a non-priv user
</pre>
 </div>
 
 
 
 
 
 
 <script type="text/javascript">
 var detail_url = '/p/windows-privesc-check/source/detail?r=24&spec=svn139';
 var publish_url = '/p/windows-privesc-check/source/detail?r=24&spec=svn139#publish';
 // describe the paths of this revision in javascript.
 var changed_paths = [];
 var changed_urls = [];
 
 changed_paths.push('/trunk/windows-privesc-check.py');
 changed_urls.push('/p/windows-privesc-check/source/browse/trunk/windows-privesc-check.py?r\x3d24\x26spec\x3dsvn139');
 
 var selected_path = '/trunk/windows-privesc-check.py';
 
 
 function getCurrentPageIndex() {
 for (var i = 0; i < changed_paths.length; i++) {
 if (selected_path == changed_paths[i]) {
 return i;
 }
 }
 }
 function getNextPage() {
 var i = getCurrentPageIndex();
 if (i < changed_paths.length - 1) {
 return changed_urls[i + 1];
 }
 return null;
 }
 function getPreviousPage() {
 var i = getCurrentPageIndex();
 if (i > 0) {
 return changed_urls[i - 1];
 }
 return null;
 }
 function gotoNextPage() {
 var page = getNextPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoPreviousPage() {
 var page = getPreviousPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoDetailPage() {
 window.location = detail_url;
 }
 function gotoPublishPage() {
 window.location = publish_url;
 }
</script>

 
 <style type="text/css">
 #review_nav {
 border-top: 3px solid white;
 padding-top: 6px;
 margin-top: 1em;
 }
 #review_nav td {
 vertical-align: middle;
 }
 #review_nav select {
 margin: .5em 0;
 }
 </style>
 <div id="review_nav">
 <table><tr><td>Go to:&nbsp;</td><td>
 <select name="files_in_rev" onchange="window.location=this.value">
 
 <option value="/p/windows-privesc-check/source/browse/trunk/windows-privesc-check.py?r=24&amp;spec=svn139"
 selected="selected"
 >/trunk/windows-privesc-check.py</option>
 
 </select>
 </td></tr></table>
 
 
 



 <div style="white-space:nowrap">
 Project members,
 <a href="https://www.google.com/accounts/ServiceLogin?service=code&amp;ltmpl=phosting&amp;continue=http%3A%2F%2Fcode.google.com%2Fp%2Fwindows-privesc-check%2Fsource%2Fbrowse%2Ftrunk%2Fwindows-privesc-check.py&amp;followup=http%3A%2F%2Fcode.google.com%2Fp%2Fwindows-privesc-check%2Fsource%2Fbrowse%2Ftrunk%2Fwindows-privesc-check.py"
 >sign in</a> to write a code review</div>


 
 </div>
 
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="older_bubble">
 <p>Older revisions</p>
 
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="http://www.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="http://www.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/windows-privesc-check/source/detail?spec=svn139&r=23">r23</a>
 by pentestmonkey
 on Feb 21, 2011
 &nbsp; <a href="/p/windows-privesc-check/source/diff?spec=svn139&r=23&amp;format=side&amp;path=/trunk/windows-privesc-check.py&amp;old_path=/trunk/windows-privesc-check.py&amp;old=22">Diff</a>
 <br>
 <pre class="ifOpened">Renamed -P option (prog files) to -F
Renamed -m (domain info) to -i (host
info)
Renamed -i (ignore trusted) to -I
Added -P option to retreieve password
...</pre>
 </div>
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="http://www.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="http://www.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/windows-privesc-check/source/detail?spec=svn139&r=22">r22</a>
 by pentestmonkey
 on Feb 19, 2011
 &nbsp; <a href="/p/windows-privesc-check/source/diff?spec=svn139&r=22&amp;format=side&amp;path=/trunk/windows-privesc-check.py&amp;old_path=/trunk/windows-privesc-check.py&amp;old=21">Diff</a>
 <br>
 <pre class="ifOpened">-m lists some domain controllers.
-U -v lists detailed user account into
(pass age, num of logons, etc.)
-U no longer lists user/group
privileges (use -U -v if you want
...</pre>
 </div>
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="http://www.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="http://www.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/windows-privesc-check/source/detail?spec=svn139&r=21">r21</a>
 by pentestmonkey
 on Feb 19, 2011
 &nbsp; <a href="/p/windows-privesc-check/source/diff?spec=svn139&r=21&amp;format=side&amp;path=/trunk/windows-privesc-check.py&amp;old_path=/trunk/windows-privesc-check.py&amp;old=20">Diff</a>
 <br>
 <pre class="ifOpened">Activated -m option for getting domain
info like password policy
-A (which lists admin users) now lists
members of sub groups recursively
Improved formatting for -L option
...</pre>
 </div>
 
 
 <a href="/p/windows-privesc-check/source/list?path=/trunk/windows-privesc-check.py&start=24">All revisions of this file</a>
 </div>
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="fileinfo_bubble">
 <p>File info</p>
 
 <div>Size: 136275 bytes,
 3208 lines</div>
 
 <div><a href="//windows-privesc-check.googlecode.com/svn/trunk/windows-privesc-check.py">View raw file</a></div>
 </div>
 
 <div id="props">
 <p>File properties</p>
 <dl>
 
 <dt>svn:executable</dt>
 <dd>*</dd>
 
 <dt>svn:keywords</dt>
 <dd>LastChangedRevision</dd>
 
 </dl>
 </div>
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 </div>
 </div>


</div>

</div>
</div>


<script src="http://www.gstatic.com/codesite/ph/10868592318973270098/js/source_file_scripts.js"></script>

 <script type="text/javascript" src="http://www.gstatic.com/codesite/ph/10868592318973270098/js/kibbles.js"></script>
 <script type="text/javascript">
 var lastStop = null;
 var initialized = false;
 
 function updateCursor(next, prev) {
 if (prev && prev.element) {
 prev.element.className = 'cursor_stop cursor_hidden';
 }
 if (next && next.element) {
 next.element.className = 'cursor_stop cursor';
 lastStop = next.index;
 }
 }
 
 function pubRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftDestroyed(data) {
 updateCursorForCell(data.cellId, 'nocursor');
 if (initialized) {
 reloadCursors();
 }
 }
 function reloadCursors() {
 kibbles.skipper.reset();
 loadCursors();
 if (lastStop != null) {
 kibbles.skipper.setCurrentStop(lastStop);
 }
 }
 // possibly the simplest way to insert any newly added comments
 // is to update the class of the corresponding cursor row,
 // then refresh the entire list of rows.
 function updateCursorForCell(cellId, className) {
 var cell = document.getElementById(cellId);
 // we have to go two rows back to find the cursor location
 var row = getPreviousElement(cell.parentNode);
 row.className = className;
 }
 // returns the previous element, ignores text nodes.
 function getPreviousElement(e) {
 var element = e.previousSibling;
 if (element.nodeType == 3) {
 element = element.previousSibling;
 }
 if (element && element.tagName) {
 return element;
 }
 }
 function loadCursors() {
 // register our elements with skipper
 var elements = CR_getElements('*', 'cursor_stop');
 var len = elements.length;
 for (var i = 0; i < len; i++) {
 var element = elements[i]; 
 element.className = 'cursor_stop cursor_hidden';
 kibbles.skipper.append(element);
 }
 }
 function toggleComments() {
 CR_toggleCommentDisplay();
 reloadCursors();
 }
 function keysOnLoadHandler() {
 // setup skipper
 kibbles.skipper.addStopListener(
 kibbles.skipper.LISTENER_TYPE.PRE, updateCursor);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_top', 50);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_bottom', 100);
 // Register our keys
 kibbles.skipper.addFwdKey("n");
 kibbles.skipper.addRevKey("p");
 kibbles.keys.addKeyPressListener(
 'u', function() { window.location = detail_url; });
 kibbles.keys.addKeyPressListener(
 'r', function() { window.location = detail_url + '#publish'; });
 
 kibbles.keys.addKeyPressListener('j', gotoNextPage);
 kibbles.keys.addKeyPressListener('k', gotoPreviousPage);
 
 
 }
 </script>
<script src="http://www.gstatic.com/codesite/ph/10868592318973270098/js/code_review_scripts.js"></script>
<script type="text/javascript">
 function showPublishInstructions() {
 var element = document.getElementById('review_instr');
 if (element) {
 element.className = 'opened';
 }
 }
 var codereviews;
 function revsOnLoadHandler() {
 // register our source container with the commenting code
 var paths = {'svn139': '/trunk/windows-privesc-check.py'}
 codereviews = CR_controller.setup(
 {"loggedInUserEmail": null, "relativeBaseUrl": "", "assetHostPath": "http://www.gstatic.com/codesite/ph", "domainName": null, "profileUrl": null, "assetVersionPath": "http://www.gstatic.com/codesite/ph/10868592318973270098", "projectHomeUrl": "/p/windows-privesc-check", "token": null, "projectName": "windows-privesc-check"}, '', 'svn139', paths,
 CR_BrowseIntegrationFactory);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, showPublishInstructions);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_PUB_PLATE, pubRevealed);
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, draftRevealed);
 codereviews.registerActivityListener(CR_ActivityType.DISCARD_DRAFT_COMMENT, draftDestroyed);
 
 
 
 
 
 
 
 var initialized = true;
 reloadCursors();
 }
 window.onload = function() {keysOnLoadHandler(); revsOnLoadHandler();};

</script>
<script type="text/javascript" src="http://www.gstatic.com/codesite/ph/10868592318973270098/js/dit_scripts.js"></script>

 
 
 
 <script type="text/javascript" src="http://www.gstatic.com/codesite/ph/10868592318973270098/js/ph_core.js"></script>
 
 
 
 
</div> 

<div id="footer" dir="ltr">
 <div class="text">
 <a href="/projecthosting/terms.html">Terms</a> -
 <a href="http://www.google.com/privacy.html">Privacy</a> -
 <a href="/p/support/">Project Hosting Help</a>
 </div>
</div>
 <div class="hostedBy" style="margin-top: -20px;">
 <span style="vertical-align: top;">Powered by <a href="http://code.google.com/projecthosting/">Google Project Hosting</a></span>
 </div>

 
 


 
 </body>
</html>

