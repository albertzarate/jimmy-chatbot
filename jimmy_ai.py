#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itty import *
import json
import pprint
import requests
from bs4 import BeautifulSoup
from six.moves import urllib
import os.path
import sys
import spark
import urllib2


try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '880bca9aacd145dfb6f8c4c7d7a690cf'


html_home = '''<html class="lato-font-loaded" lang="en"><head>
  <meta charset="utf-8">
  <title>User Dashboard</title>
  <!--[if lte IE 9]> <meta http-equiv=refresh content="0; URL=/ie-9-is-not-supported.html" /> <![endif]-->
  <link rel="shortcut icon" type="image/x-icon" href="https://du11hjcvx0uqb.cloudfront.net/dist/images/favicon-e10d657a73.ico">
  <link rel="apple-touch-icon" href="https://du11hjcvx0uqb.cloudfront.net/dist/images/apple-touch-icon-585e5d997d.png">
        <link rel="alternate" type="application/atom+xml" title="User Atom Feed (All Courses)" href="/feeds/users/user_XfaZxicTyEMKJhXYOIQ4vPgZPOlNZn96q9G1sWoR.atom">

  <link rel="stylesheet" media="all" href="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/9aa105797e3845a39d5ae6e392e0bfde/variables-b59440e479f072e9f8e5fa783f2fcc29.css">
  <link rel="stylesheet" media="all" href="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/9aa105797e3845a39d5ae6e392e0bfde/new_styles_normal_contrast/bundles/common-4a3f5c7fe9.css">
  <script type="text/javascript" async="" src="https://ssl.google-analytics.com/ga.js"></script><script>
//<![CDATA[

!function(){
  var o,s,v;
  if (!(window.Promise && Object.assign && Object.values && [].find && [].includes && (o={},s=Symbol(),v={},o[s]=v,o[s]===v) && (function f(){}).bind().name==='bound f')) {
    s = 's', document.write('<'+s+'cr'+'ipt src="https://du11hjcvx0uqb.cloudfront.net/dist/ie11-polyfill-9524c2cc43.js"></'+s+'c'+'ript>');
  }
}();
      
//]]>
</script>
  <script src="https://du11hjcvx0uqb.cloudfront.net/dist/lato-fontfaceobserver-11a14bc0b6.js" async="async"></script>
  
  <meta name="apple-itunes-app" content="app-id=480883488">
<link rel="manifest" href="/web-app-manifest/manifest.json">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0055a2">
  <link rel="stylesheet" media="all" href="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/9aa105797e3845a39d5ae6e392e0bfde/new_styles_normal_contrast/bundles/dashboard-cd500e509c.css">
<link rel="stylesheet" media="all" href="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/9aa105797e3845a39d5ae6e392e0bfde/new_styles_normal_contrast/bundles/dashboard_card-1a30fe34e2.css">
  
  
  <script>
    function _earlyClick(e){
      var c = e.target
      while (c && c.ownerDocument) {
        if (c.getAttribute('href') == '#' || c.getAttribute('data-method')) {
          e.preventDefault()
          (_earlyClick.clicks = _earlyClick.clicks || []).push(c)
          break
        }
        c = c.parentNode
      }
    }
    document.addEventListener('click', _earlyClick)
  </script>
  <script src="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/9aa105797e3845a39d5ae6e392e0bfde/variables-b59440e479f072e9f8e5fa783f2fcc29.js" defer="defer"></script>
  <script src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/vendor.bundle-6f9e92f33d.js" defer="defer"></script>
<script src="https://du11hjcvx0uqb.cloudfront.net/dist/timezone/America/Los_Angeles-78b0e93740.js" defer="defer"></script>
<script src="https://du11hjcvx0uqb.cloudfront.net/dist/timezone/en_US-80a0ce259b.js" defer="defer"></script>
<script src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/appBootstrap.bundle-4fa23c5d57.js" defer="defer"></script>
<script src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/common.bundle-485efd46dc.js" defer="defer"></script>
<script src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/dashboard.bundle-6a3c5ca7be.js" defer="defer"></script>
<script src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/dashboard_card.bundle-62d7e48663.js" defer="defer"></script>
<style type="text/css"></style><style type="text/css" data-glamor=""></style><style type="text/css" data-glamor=""></style><style type="text/css" data-glamor=""></style></head>

<body class="with-right-side  primary-nav-expanded context-user_4150924 webkit chrome no-touch">

<noscript>
  &lt;div role="alert" class="ic-flash-static ic-flash-error"&gt;
    &lt;div class="ic-flash__icon" aria-hidden="true"&gt;
      &lt;i class="icon-warning"&gt;&lt;/i&gt;
    &lt;/div&gt;
    &lt;h1&gt;You need to have JavaScript enabled in order to access this site.&lt;/h1&gt;
  &lt;/div&gt;
</noscript>





<ul id="flash_message_holder"></ul>
<div id="flash_screenreader_holder" role="alert" aria-live="assertive" aria-relevant="additions" class="screenreader-only" aria-atomic="false"></div>

<div id="application" class="ic-app">
  
  <header id="header" class="ic-app-header no-print ">
    <a href="#content" id="skip_navigation_link">Skip To Content</a>
      <div role="region" class="ic-app-header__main-navigation" aria-label="Main Navigation">
        <div class="ic-app-header__logomark-container">
          <a href="https://sjsu.instructure.com/" class="ic-app-header__logomark">
            <span class="screenreader-only">Dashboard</span>
          </a>
        </div>
        <ul id="menu" class="ic-app-header__menu-list">
            <li class="menu-item ic-app-header__menu-list-item ">
              <a id="global_nav_profile_link" href="/profile" class="ic-app-header__menu-list-link">
                <div class="menu-item-icon-container" aria-hidden="true">
                  <div class="ic-avatar ">
                    <img src="https://sjsu.instructure.com/images/thumbnails/46057225/IAkpjG0Ww0SRvImY9le89tGaBRIaOmjpMfdNqn2V" alt="Priyank Varshney">
                  </div>
                </div>
                <div class="menu-item__text">
                  Account
                </div>
              </a>
            </li>
          <li class="ic-app-header__menu-list-item  ic-app-header__menu-list-item--active">
            <a id="global_nav_dashboard_link" href="https://sjsu.instructure.com/" class="ic-app-header__menu-list-link">
              <div class="menu-item-icon-container" aria-hidden="true">
                  <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--dashboard" version="1.1" x="0" y="0" viewBox="0 0 280 200" enable-background="new 0 0 280 200" xml:space="preserve"><path d="M273.09,180.75H197.47V164.47h62.62A122.16,122.16,0,1,0,17.85,142a124,124,0,0,0,2,22.51H90.18v16.29H6.89l-1.5-6.22A138.51,138.51,0,0,1,1.57,142C1.57,65.64,63.67,3.53,140,3.53S278.43,65.64,278.43,142a137.67,137.67,0,0,1-3.84,32.57ZM66.49,87.63,50.24,71.38,61.75,59.86,78,76.12Zm147,0L202,76.12l16.25-16.25,11.51,11.51ZM131.85,53.82v-23h16.29v23Zm15.63,142.3a31.71,31.71,0,0,1-28-16.81c-6.4-12.08-15.73-72.29-17.54-84.25a8.15,8.15,0,0,1,13.58-7.2c8.88,8.21,53.48,49.72,59.88,61.81a31.61,31.61,0,0,1-27.9,46.45ZM121.81,116.2c4.17,24.56,9.23,50.21,12,55.49A15.35,15.35,0,1,0,161,157.3C158.18,152,139.79,133.44,121.81,116.2Z"></path></svg>

              </div>
              <div class="menu-item__text">Dashboard</div>
            </a>
          </li>
          <li class="menu-item ic-app-header__menu-list-item ">
            <a id="global_nav_courses_link" href="/courses" class="ic-app-header__menu-list-link">
              <div class="menu-item-icon-container" aria-hidden="true">
                <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--courses" version="1.1" x="0" y="0" viewBox="0 0 280 259" enable-background="new 0 0 280 259" xml:space="preserve"><path d="M73.31,198c-11.93,0-22.22,8-24,18.73a26.67,26.67,0,0,0-.3,3.63v.3a22,22,0,0,0,5.44,14.65,22.47,22.47,0,0,0,17.22,8H200V228.19h-134V213.08H200V198Zm21-105.74h90.64V62H94.3ZM79.19,107.34V46.92H200v60.42Zm7.55,30.21V122.45H192.49v15.11ZM71.65,16.71A22.72,22.72,0,0,0,49,39.36V190.88a41.12,41.12,0,0,1,24.32-8h157V16.71ZM33.88,39.36A37.78,37.78,0,0,1,71.65,1.6H245.36V198H215.15v45.32h22.66V258.4H71.65a37.85,37.85,0,0,1-37.76-37.76Z"></path></svg>

              </div>
              <div class="menu-item__text">
                Courses
              </div>
            </a>
          </li>
            <li class="menu-item ic-app-header__menu-list-item ">
              <a id="global_nav_groups_link" href="/groups" class="ic-app-header__menu-list-link">
                <div class="menu-item-icon-container" aria-hidden="true">
                  <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--groups" viewBox="0 0 200 135"><path d="M134.5 129.4c0-1.1 0-19.8-6.2-31.1-4.5-8.5-16.4-12.4-35-19.2-1.7-.6-3.4-1.1-5.1-1.7v-8.5c5.6-5.1 8.5-12.4 8.5-20.3V29.4C96.6 13 83.6 0 67.2 0S37.9 13 37.9 29.4v19.2c0 7.3 3.4 14.7 8.5 20.3v8.5c-1.7.6-3.4 1.1-5.1 1.7-18.6 6.2-30.5 10.7-35 19.2C0 109.6 0 128.8 0 129.4c0 3.4 2.3 5.6 5.6 5.6h123.7c3.5 0 5.7-2.3 5.2-5.6zm-123.2-5.7c.6-5.6 1.7-14.7 3.4-19.8C17 98.8 30 94.3 43.5 89.8c2.8-1.1 5.6-2.3 9-3.4 2.3-.6 4-2.8 4-5.1V66.7c0-1.7-.6-3.4-1.7-4.5-4-3.4-6.2-8.5-6.2-13.6V29.4c0-10.2 7.9-18.1 18.1-18.1s18.1 7.9 18.1 18.1v19.2c0 5.1-2.3 10.2-6.2 13.6-1.1 1.1-1.7 2.8-1.7 4.5v14.7c0 2.3 1.7 4.5 4 5.1 2.8 1.1 6.2 2.3 9 3.4 13.6 5.1 26.6 9.6 28.8 14.1 2.8 5.1 4 13.6 4.5 19.8H11.3zM196 79.1c-2.8-6.2-11.3-9.6-22.6-13.6l-1.7-.6v-3.4c4.5-4 6.8-9.6 6.8-15.8V35c0-12.4-9.6-22-22-22s-22 10.2-22 22v10.7c0 6.2 2.3 11.9 6.8 15.8V65l-1.7.6c-7.3 2.8-13 4.5-16.9 7.3-1.7 1.1-2.3 2.8-2.3 5.1.6 1.7 1.7 3.4 3.4 4.5 7.9 4 12.4 7.3 14.1 10.7 2.3 4.5 4 10.2 5.1 18.1.6 2.3 2.8 4.5 5.6 4.5h45.8c3.4 0 5.6-2.8 5.6-5.1 0-3.9 0-24.3-4-31.6zm-42.9 25.4c-1.1-6.8-2.8-12.4-5.1-16.9-1.7-4-5.1-6.8-9.6-10.2 1.7-1.1 3.4-1.7 5.1-2.3l5.6-2.3c1.7-.6 3.4-2.8 3.4-5.1v-9.6c0-1.7-.6-3.4-2.3-4.5-2.8-1.7-4.5-5.1-4.5-8.5V34.5c0-6.2 4.5-10.7 10.7-10.7s10.7 5.1 10.7 10.7v10.7c0 3.4-1.7 6.2-4.5 8.5-1.1 1.1-2.3 2.8-2.3 4.5v10.2c0 2.3 1.1 4.5 3.4 5.1l5.6 2.3c6.8 2.3 15.3 5.6 16.4 7.9 1.7 2.8 2.8 12.4 2.8 20.9h-35.4z"></path></svg>

                </div>
                <div class="menu-item__text">
                  Groups
                </div>
              </a>
            </li>
          <li class="menu-item ic-app-header__menu-list-item ">
            <a id="global_nav_calendar_link" href="/calendar" class="ic-app-header__menu-list-link">
              <div class="menu-item-icon-container" aria-hidden="true">
                <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--calendar" version="1.1" x="0" y="0" viewBox="0 0 280 280" enable-background="new 0 0 280 280" xml:space="preserve"><path d="M197.07,213.38h16.31V197.07H197.07Zm-16.31,16.31V180.76h48.92v48.92Zm-48.92-16.31h16.31V197.07H131.85Zm-16.31,16.31V180.76h48.92v48.92ZM66.62,213.38H82.93V197.07H66.62ZM50.32,229.68V180.76H99.24v48.92Zm146.75-81.53h16.31V131.85H197.07Zm-16.31,16.31V115.54h48.92v48.92Zm-48.92-16.31h16.31V131.85H131.85Zm-16.31,16.31V115.54h48.92v48.92ZM66.62,148.15H82.93V131.85H66.62ZM50.32,164.46V115.54H99.24v48.92ZM34,262.29H246V82.93H34ZM246,66.62V42.16A8.17,8.17,0,0,0,237.84,34H213.38v8.15a8.15,8.15,0,1,1-16.31,0V34H82.93v8.15a8.15,8.15,0,0,1-16.31,0V34H42.16A8.17,8.17,0,0,0,34,42.16V66.62Zm-8.15-48.92a24.49,24.49,0,0,1,24.46,24.46V278.6H17.71V42.16A24.49,24.49,0,0,1,42.16,17.71H66.62V9.55a8.15,8.15,0,0,1,16.31,0v8.15H197.07V9.55a8.15,8.15,0,1,1,16.31,0v8.15Z"></path></svg>

              </div>
              <div class="menu-item__text">
                Calendar
              </div>
            </a>
          </li>
          <li class="menu-item ic-app-header__menu-list-item ">
            <a id="global_nav_conversations_link" href="/conversations" class="ic-app-header__menu-list-link">
              <div class="menu-item-icon-container" aria-hidden="true">
                <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--inbox" version="1.1" x="0" y="0" viewBox="0 0 280 280" enable-background="new 0 0 280 280" xml:space="preserve"><path d="M91.72,120.75h96.56V104.65H91.72Zm0,48.28h80.47V152.94H91.72Zm0-96.56h80.47V56.37H91.72Zm160.94,34.88H228.52V10.78h-177v96.56H27.34A24.17,24.17,0,0,0,3.2,131.48V244.14a24.17,24.17,0,0,0,24.14,24.14H252.66a24.17,24.17,0,0,0,24.14-24.14V131.48A24.17,24.17,0,0,0,252.66,107.34Zm0,16.09a8.06,8.06,0,0,1,8,8v51.77l-32.19,19.31V123.44ZM67.58,203.91v-177H212.42v177ZM27.34,123.44H51.48v79.13L19.29,183.26V131.48A8.06,8.06,0,0,1,27.34,123.44ZM252.66,252.19H27.34a8.06,8.06,0,0,1-8-8V202l30,18H230.75l30-18v42.12A8.06,8.06,0,0,1,252.66,252.19Z"></path></svg>

                <span class="menu-item__badge" style="display: none">0</span>
              </div>
              <div class="menu-item__text">
                Inbox
              </div>
            </a>
          </li>
            

      <li id="context_external_tool_22511_menu_item" class="menu-item ic-app-header__menu-list-item">
        <a class="ic-app-header__menu-list-link" href="/accounts/89550/external_tools/22511?launch_type=global_navigation">
            <svg version="1.1" class="ic-icon-svg ic-icon-svg--lti menu-item__icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 64 64">
              <path d="M9.4 32c0-7.8 6.5-14.3 14.4-14.3h11.7v-9.4h-11.8c-13.1 0-23.7 10.6-23.7 23.7s10.7 23.7 23.7 23.7h11.7v-9.4h-11.7c-7.9 0-14.3-6.5-14.3-14.3z m54.6 0l-19.1-17v11.3h-20.2c-3.1 0-5.6 2.5-5.6 5.6s2.5 5.6 5.6 5.7h20.2v11.2l19.1-16.8z"></path>
            </svg>
          <div class="menu-item__text">
            Commons
          </div>
        </a>
      </li>

          <li class="ic-app-header__menu-list-item">
           <a id="global_nav_help_link" class="ic-app-header__menu-list-link" data-track-category="help system" data-track-label="help button" href="http://help.instructure.com/">
              <div class="menu-item-icon-container" role="presentation">
                <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg menu-item__icon svg-icon-help" version="1.1" x="0" y="0" viewBox="0 0 200 200" enable-background="new 0 0 200 200" xml:space="preserve" fill="currentColor"><path d="M100,127.88A11.15,11.15,0,1,0,111.16,139,11.16,11.16,0,0,0,100,127.88Zm8.82-88.08a33.19,33.19,0,0,1,23.5,23.5,33.54,33.54,0,0,1-24,41.23,3.4,3.4,0,0,0-2.74,3.15v9.06H94.42v-9.06a14.57,14.57,0,0,1,11.13-14,22.43,22.43,0,0,0,13.66-10.27,22.73,22.73,0,0,0,2.31-17.37A21.92,21.92,0,0,0,106,50.59a22.67,22.67,0,0,0-19.68,3.88,22.18,22.18,0,0,0-8.65,17.64H66.54a33.25,33.25,0,0,1,13-26.47A33.72,33.72,0,0,1,108.82,39.8ZM100,5.2A94.8,94.8,0,1,0,194.8,100,94.91,94.91,0,0,0,100,5.2m0,178.45A83.65,83.65,0,1,1,183.65,100,83.73,83.73,0,0,1,100,183.65" transform="translate(-5.2 -5.2)"></path></svg>

              </div>
              <div class="menu-item__text">
                Help
              </div>
</a>          </li>
        <li class="menu-item ic-app-header__menu-list-item "><a id="global_nav_library_link" target="_blank" href="https://library.sjsu.edu" class="ic-app-header__menu-list-link"><div class="menu-item-icon-container" aria-hidden="true"><svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="45px" height="30px" x="0px" y="0px" viewBox="179.2 189.3 389.4 358.5" enable-background="new 179.2 189.3 389.4 358.5" xml:space="preserve"><path fill="#FFFFFF" d="M247.4,189.3c81.6,19.2,118.7,81.2,118.7,81.2v277.2c-41.7-59.9-118.7-84.3-118.7-84.3V461C247.4,461,247.5,189,247.4,189.3z"></path><path fill="#FFFFFF" d="M260.1,530.2c0,0-34.6-17.5-80.8-10.3V247.6h11.4v258.8C190.6,506.2,240.4,505.7,260.1,530.2z"></path><path fill="#FFFFFF" d="M306.8,521.3L306.8,521.3c-18-25.7-75-45.7-75-45.7V219.9l-23.6-9.2V489c0,0,24.3,3,36.4,6.4C286.5,507.2,306.8,521.3,306.8,521.3z"></path><path fill="#FFFFFF" d="M500.5,189.3c-81,25.2-118.7,81.2-118.7,81.2v277.2c41.7-59.9,118.7-84.3,118.7-84.3S500.5,190,500.5,189.3z"></path><path fill="#FFFFFF" d="M487.9,530.2c0,0,34.6-17.5,80.8-10.3V247.6h-11.4v258.8C557.3,506.2,507.6,505.7,487.9,530.2z"></path><path fill="#FFFFFF" d="M441.1,521.3L441.1,521.3c18-25.7,75-45.7,75-45.7V219.9l23.6-9.2V489c0,0-24.3,3-36.4,6.4C461.4,507.2,441.1,521.3,441.1,521.3z"></path></svg></div><div class="menu-item__text">Library</div></a></li></ul>
      </div>
      <div class="ic-app-header__secondary-navigation">
        <ul class="ic-app-header__menu-list">
          <li class="menu-item ic-app-header__menu-list-item">
            <button id="primaryNavToggle" class="ic-app-header__menu-list-link ic-app-header__menu-list-link--nav-toggle" aria-label="
                Minimize global navigation" title="
                Minimize global navigation">
              <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--navtoggle" version="1.1" x="0" y="0" width="40" height="32" viewBox="0 0 40 32" xml:space="preserve">
  <path d="M39.5,30.28V2.48H37.18v27.8Zm-4.93-13.9L22.17,4,20.53,5.61l9.61,9.61H.5v2.31H30.14l-9.61,9.61,1.64,1.64Z"></path>
</svg>

            </button>
          </li>
        </ul>
      </div>
    <div id="global_nav_tray_container"><noscript data-reactid=".2"></noscript></div>
  </header>


  <div id="instructure_ajax_error_box">
    <div style="text-align: right; background-color: #fff;"><a href="#" class="close_instructure_ajax_error_box_link">Close</a></div>
    <iframe id="instructure_ajax_error_result" src="about:blank" style="border: 0;" title="Error"></iframe>
  </div>

  

  <div id="wrapper" class="ic-Layout-wrapper">
    <div id="main" class="ic-Layout-columns">
        <div class="ic-Layout-watermark"></div>
      <div id="not_right_side" class="ic-app-main-content">
        <div id="content-wrapper" class="ic-Layout-contentWrapper">
            
          <div id="content" class="ic-Layout-contentMain" role="main">
            




<div id="dashboard" class="ic-dashboard-app">
  
  

<div class="ic-notification ic-notification--admin-created ic-notification--info account_notification">
  <div class="ic-notification__icon" role="presentation">
    <i class="icon-info"></i>
    <span class="screenreader-only">
      information
    </span>
  </div>

<div class="notification_account_content">
  <div class="ic-notification__content">
    <div class="ic-notification__message">
      <h4 class="ic-notification__title">
        Software and Workshops
      </h4>
      
    </div>
    <div class="ic-notification__actions">
      <a href="#" class="Button Button--icon-action" data-url="/dashboard/account_notifications/1621" data-remove=".ic-notification" title="close" role="button">
        <i class="icon-x"></i>
        <span class="screenreader-only">close</span>
      </a>
    </div>
  </div>
  <span class="notification_account_content_text">
    This is a message for <b>San Jose State University</b>
  </span>
</div>

</div>

<div class="ic-notification ic-notification--admin-created ic-notification--info account_notification">
  <div class="ic-notification__icon" role="presentation">
    <i class="icon-question"></i>
    <span class="screenreader-only">
      question
    </span>
  </div>

<div class="notification_account_content">
  <div class="ic-notification__content">
    <div class="ic-notification__message">
      <h4 class="ic-notification__title">
        Support
      </h4>
      <span class="notification_message">
      <p>Support is available for you as you use Canvas. You can find detailed tutorials discussing the different components of Canvas within the&nbsp;<a class="external" href="https://community.canvaslms.com/community/answers/guides/" target="_blank" rel="noreferrer"><span>Canvas Guides</span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a>&nbsp;and&nbsp;<a class="external" href="http://www.sjsu.edu/ecampus/teaching-tools/canvas/index.html" target="_blank" rel="noreferrer"><span>eCampus Canvas Website</span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a>.</p>
<p><span>For issues that you encounter in Canvas, please click on the word&nbsp;<strong>Help</strong>&nbsp;on the lower left corner of the screen. Then select,&nbsp;<strong>Report a Problem</strong>. Enter the necessary information and click&nbsp;<strong>Submit</strong>. You will receive a response back promptly from support personnel.</span></p>
<p><span><strong>Canvas Quick Tip</strong></span></p>
<p><a id="" title="" href="https://community.canvaslms.com/docs/DOC-10570-4212710327" target="_blank" class="external" rel="noreferrer"><span>Customize Canvas Course List:</span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a><a id="" class="" title="" href="https://guides.instructure.com/m/4152/l/48284-how-do-i-customize-my-course-list" target=""></a><span>&nbsp;</span><span>When you are enrolled in more than one Canvas course, you can customize the active courses you want to show in your Course list. Courses you want to show in the Courses drop-down menu are called favorite courses. You can favorite any published course that appears in the My Courses section on the course list page.&nbsp;</span><span></span><span>Course favorites also display in the&nbsp;<a href="https://community.canvaslms.com/docs/DOC-10587-4212710330" target="_blank" class="external" rel="noreferrer"><span>Dashboard</span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a>.</span></p>
<p><span>Download the Canvas App&nbsp;on Android and iOS devices.</span></p>
      </span>
    </div>
    <div class="ic-notification__actions">
      <a href="#" class="Button Button--icon-action" data-url="/dashboard/account_notifications/1620" data-remove=".ic-notification" title="close" role="button">
        <i class="icon-x"></i>
        <span class="screenreader-only">close</span>
      </a>
    </div>
  </div>
  <span class="notification_account_content_text">
    This is a message for <b>San Jose State University</b>
  </span>
</div>

</div>









  <div id="dashboard_header_container" class="ic-Dashboard-header"><div class="ic-Dashboard-header__layout" data-reactid=".0"><h1 class="ic-Dashboard-header__title" data-reactid=".0.0">Dashboard</h1><div class="ic-Dashboard-header__actions" data-reactid=".0.1"><div id="DashboardOptionsMenu_Container" data-reactid=".0.1.1"><span data-reactid=".0.1.1.0"><button role="button" tabindex="0" aria-haspopup="true" id="PopoverMenu__HkslmlS6pb" type="button" class="_1OIPJSt _3wIB8NA _3xK6Gsf" style="margin:0px;" data-reactid=".0.1.1.0.0"><span class="_2rc5olV" data-reactid=".0.1.1.0.0.0"><span class="_1GLewti" data-reactid=".0.1.1.0.0.0.0">Dashboard Options</span><svg name="IconSettings2Line" viewBox="0 0 1920 1920" style="fill:currentColor;width:1em;height:1em;" width="1em" height="1em" aria-hidden="true" role="presentation" data-reactid=".0.1.1.0.0.0.1"><g role="presentation" data-reactid=".0.1.1.0.0.0.1.2"><svg version="1.1" viewBox="0 0 1920 1920" data-reactid=".0.1.1.0.0.0.1.2.0"><path d="M1739.34 1293.414l-105.827 180.818-240.225-80.188-24.509 22.25c-69.91 63.586-150.211 109.666-238.644 136.771l-32.076 9.94-49.468 244.065H835.584l-49.468-244.179-32.076-9.939c-88.432-27.105-168.734-73.185-238.644-136.771l-24.508-22.25-240.226 80.189-105.826-180.82 189.74-164.442-7.453-32.978c-10.39-45.742-15.586-91.483-15.586-135.869 0-44.386 5.195-90.127 15.586-135.868l7.454-32.979-189.741-164.442 105.826-180.819 240.226 80.075 24.508-22.25c69.91-63.585 150.212-109.665 238.644-136.884l32.076-9.826 49.468-244.066h213.007l49.468 244.18 32.076 9.825c88.433 27.219 168.734 73.186 238.644 136.885l24.509 22.25 240.225-80.189 105.826 180.819-189.74 164.442 7.453 32.98c10.39 45.74 15.586 91.481 15.586 135.867 0 44.386-5.195 90.127-15.586 135.869l-7.454 32.978 189.741 164.556zm-53.76-333.403c0-41.788-3.84-84.48-11.634-127.284l210.184-182.062-199.454-340.856-265.186 88.433c-66.974-55.567-143.322-99.388-223.85-128.414L1140.977.01H743.198l-54.663 269.704c-81.431 29.139-156.424 72.282-223.963 128.414L199.5 309.809.045 650.665l210.07 182.062c-7.68 42.804-11.52 85.496-11.52 127.284 0 41.789 3.84 84.48 11.52 127.172L.046 1269.357 199.5 1610.214l265.186-88.546c66.974 55.68 143.323 99.388 223.85 128.527l54.663 269.816h397.779l54.663-269.703c81.318-29.252 156.424-72.283 223.85-128.527l265.186 88.546 199.454-340.857-210.184-182.174c7.793-42.805 11.633-85.496 11.633-127.285zM942.075 564.706C724.1 564.706 546.782 742.024 546.782 960c0 217.976 177.318 395.294 395.294 395.294 217.977 0 395.294-177.318 395.294-395.294 0-217.976-177.317-395.294-395.294-395.294m0 677.647c-155.633 0-282.353-126.72-282.353-282.353s126.72-282.353 282.353-282.353S1224.43 804.367 1224.43 960s-126.72 282.353-282.353 282.353" stroke="none" stroke-width="1" data-reactid=".0.1.1.0.0.0.1.2.0.0"></path></svg></g></svg></span></button><noscript data-reactid=".0.1.1.0.1"></noscript></span></div></div></div></div>
  <div id="dashboard-activity" class="ic-Dashboard-Activity" style="display: none">
    
<h2 class="recent-activity-header">
    Recent Activity
</h2>

<ul class="recent_activity unstyled_list">
    <li class="stream-category stream-announcement" data-category="Announcement">
      <div class="stream_header">
        <div class="image-block">
          <div class="image-block-image">
            <i class="icon-announcement"></i>
          </div>
          <div class="image-block-content">
            <div class="title">
              <b class="count">27</b> Announcements
            </div>
              <strong class="unread-count">
                <span class="accessibly-hidden">26 <span>unread items</span>
                </span>
              </strong>
            <div class="links">
              <a href="/courses/1238553/announcements" aria-label="Visit Course Announcements for FA17: CMPE-110 Sec 04 - Electronics">FA17: CMPE-110 Sec 04 - Electronics</a>, <a href="/courses/1240227/announcements" aria-label="Visit Course Announcements for FA17: CMPE-131 Sec 05 - Software Engr I">FA17: CMPE-131 Sec 05 - Software Engr I</a>, and <a href="/courses/1239787/announcements" aria-label="Visit Course Announcements for FA17: ISE-130 Sec 01 - Engr Statistics">FA17: ISE-130 Sec 01 - Engr Statistics</a>
            </div>
          </div>
        </div>
        <div class="header-right-side">
          <a href="#" class="toggle-details" aria-controls="details_container">
  <span aria-hidden="true">Show More <i class="icon-mini-arrow-down"></i></span>

<span class="screenreader-only">Expand 27 announcements</span></a>
        </div>
      </div>

      <div class="details_container">
        <table id="announcement-details" class="stream-details">
          <caption class="accessibly-hidden">Announcement Details</caption>
          <thead class="accessibly-hidden">
            <tr>
              <th scope="col">Unread</th>
              <th scope="col">Message</th>
              <th scope="col">Date</th>
              <th></th>
            </tr>
          </thead>
          
<tbody><tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3323407" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      2N3904 Load line characteristics
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 23 at  7:08pm" data-tooltip="top">Oct 23 at  7:08pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/148115597" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3322692" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      LAB 4 - BJT transistor datasheet
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 22 at  7:07pm" data-tooltip="top">Oct 22 at  7:07pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/148020082" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3322590" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      LAB 4
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 22 at  2:38pm" data-tooltip="top">Oct 22 at  2:38pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/148009707" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1240227/announcements/3322108" class="content_summary">
      <span class="fake-link">FA17: CMPE-131 Sec 05 - Software Engr I</span>
      <strong></strong>
      prototype deom 10/24 and 10/26
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 21 at  3:09pm" data-tooltip="top">Oct 21 at  3:09pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147963963" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1240227/announcements/3320324" class="content_summary">
      <span class="fake-link">FA17: CMPE-131 Sec 05 - Software Engr I</span>
      <strong></strong>
      slide--design and implementation
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 17 at  7:13pm" data-tooltip="top">Oct 17 at  7:13pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147766471" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1239787/announcements/3318605" class="content_summary">
      <span class="fake-link">FA17: ISE-130 Sec 01 - Engr Statistics</span>
      <strong></strong>
      MINITAB Express for MAC, ENGR 390 Lab
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 14 at  8:35pm" data-tooltip="top">Oct 14 at  8:35pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147548585" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1240227/announcements/3318001" class="content_summary">
      <span class="fake-link">FA17: CMPE-131 Sec 05 - Software Engr I</span>
      <strong></strong>
      GitHub Assignment Information
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 13 at  7pm" data-tooltip="top">Oct 13 at  7pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147520230" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3317205" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      Practice problems discussed in the lab
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 12 at 11:26pm" data-tooltip="top">Oct 12 at 11:26pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147390744" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3317783" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      curve for first two quizzes
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 12 at  8:12pm" data-tooltip="top">Oct 12 at  8:12pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147459636" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1240227/announcements/3316901" class="content_summary">
      <span class="fake-link">FA17: CMPE-131 Sec 05 - Software Engr I</span>
      <strong></strong>
      GitHub and Software Testing workshop on 10/12 &amp; Slide
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 11 at  9:30pm" data-tooltip="top">Oct 11 at  9:30pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147390738" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1240227/announcements/3316892" class="content_summary">
      <span class="fake-link">FA17: CMPE-131 Sec 05 - Software Engr I</span>
      <strong></strong>
      slide--testing 
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 11 at  6pm" data-tooltip="top">Oct 11 at  6pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147381900" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1239787/announcements/3315563" class="content_summary">
      <span class="fake-link">FA17: ISE-130 Sec 01 - Engr Statistics</span>
      <strong></strong>
      Problem 4-127 part (f)
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 9 at  6:21pm" data-tooltip="top">Oct 9 at  6:21pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147223998" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3312603" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      Idea for labs next week
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 4 at 10:25am" data-tooltip="top">Oct 4 at 10:25am</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146911755" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3312168" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      Lab submission should be OK now
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 3 at  5:57pm" data-tooltip="top">Oct 3 at  5:57pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146871203" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3312127" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      Submitting Lap Reports in Canvas
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 3 at  4:45pm" data-tooltip="top">Oct 3 at  4:45pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146863940" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3311684" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      Midterm will be on 10/16
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 3 at  7:44am" data-tooltip="top">Oct 3 at  7:44am</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146833791" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1240227/announcements/3311668" class="content_summary">
      <span class="fake-link">FA17: CMPE-131 Sec 05 - Software Engr I</span>
      <strong></strong>
      slide--architecture
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 3 at  5:58am" data-tooltip="top">Oct 3 at  5:58am</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146832392" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3311656" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      Regarding Lab Reports
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 3 at  4:18am" data-tooltip="top">Oct 3 at  4:18am</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146832153" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3310322" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      Lab 2
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 2 at 12:59am" data-tooltip="top">Oct 2 at 12:59am</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146721497" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3310321" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      Room Change for Makeup Quiz
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 30 at  6:16pm" data-tooltip="top">Sep 30 at  6:16pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146721418" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1240227/announcements/3309664" class="content_summary">
      <span class="fake-link">FA17: CMPE-131 Sec 05 - Software Engr I</span>
      <strong></strong>
      slide--midterm review
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 29 at  5:45am" data-tooltip="top">Sep 29 at  5:45am</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146669097" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3309630" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      Makeup Quiz 2
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 28 at 11:31pm" data-tooltip="top">Sep 28 at 11:31pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146666665" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1240227/announcements/3309008" class="content_summary">
      <span class="fake-link">FA17: CMPE-131 Sec 05 - Software Engr I</span>
      <strong></strong>
      prototype demo on 10/24 and 10/26
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 28 at  6:38am" data-tooltip="top">Sep 28 at  6:38am</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146622154" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1238553/announcements/3308541" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 04 - Electronics</span>
      <strong></strong>
      The Laplace of Vout
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 27 at 12:26pm" data-tooltip="top">Sep 27 at 12:26pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146586550" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1239787/announcements/3308464" class="content_summary">
      <span class="fake-link">FA17: ISE-130 Sec 01 - Engr Statistics</span>
      <strong></strong>
      Late Homework Submission Policy
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 27 at 10:36am" data-tooltip="top">Sep 27 at 10:36am</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146577850" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1240227/announcements/3307824" class="content_summary">
      <span class="fake-link">FA17: CMPE-131 Sec 05 - Software Engr I</span>
      <strong></strong>
      Midterm Exam
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 26 at 12:27pm" data-tooltip="top">Sep 26 at 12:27pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146533516" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
      <div class="unread"><span class="accessibly-hidden">Unread</span></div>
  </td>
  <td>
    <a href="/courses/1240227/announcements/3305466" class="content_summary">
      <span class="fake-link">FA17: CMPE-131 Sec 05 - Software Engr I</span>
      <strong></strong>
      GitHub Assignment Posted
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 26 at 12:17pm" data-tooltip="top">Sep 26 at 12:17pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146342263" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

        </tbody></table>
      </div>
    </li>
    <li class="stream-category stream-conversation" data-category="Conversation">
      <div class="stream_header">
        <div class="image-block">
          <div class="image-block-image">
            <i class="icon-message"></i>
          </div>
          <div class="image-block-content">
            <div class="title">
              <b class="count">1</b> Conversation Message
            </div>
            <div class="links">
              Stephanie Wemusa
            </div>
          </div>
        </div>
        <div class="header-right-side">
          <a href="#" class="toggle-details" aria-controls="details_container">
  <span aria-hidden="true">Show More <i class="icon-mini-arrow-down"></i></span>

<span class="screenreader-only">Expand 1 conversation message</span></a>
        </div>
      </div>

      <div class="details_container">
        <table id="conversation-details" class="stream-details">
          <caption class="accessibly-hidden">Conversation Details</caption>
          <thead class="accessibly-hidden">
            <tr>
              <th scope="col">Unread</th>
              <th scope="col">Message</th>
              <th scope="col">Date</th>
              <th></th>
            </tr>
          </thead>
          
<tbody><tr>
  <td>
  </td>
  <td>
    <a href="/conversations/8777867" class="content_summary">
      <span class="fake-link">Stephanie Wemusa</span>
      <strong></strong>
      Hello Everyone,

This week you will have your Green Talk due on Friday @ 11:59, remote assignment, I will send you the link and prompt on Thursday, 9/26 by 6pm.

Next week 10/3, you will have two assignments due:

Group presentation pitch, 10 minu...
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 26 at  6:12pm" data-tooltip="top">Sep 26 at  6:12pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146552391" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

        </tbody></table>
      </div>
    </li>
    <li class="stream-category stream-assignment" data-category="Assignment">
      <div class="stream_header">
        <div class="image-block">
          <div class="image-block-image">
            <i class="icon-assignment"></i>
          </div>
          <div class="image-block-content">
            <div class="title">
              <b class="count">20</b> Assignment Notifications
            </div>
            <div class="links">
              <a href="/courses/1245234/assignments" aria-label="Visit Course Assignments for FA17: ENGR-100W Sec 43 - Engr Reports">FA17: ENGR-100W Sec 43 - Engr Reports</a>, <a href="/courses/1243231/assignments" aria-label="Visit Course Assignments for FA17: CMPE-124 Sec 07 - Digital Design I">FA17: CMPE-124 Sec 07 - Digital Design I</a>, <a href="/courses/1238555/assignments" aria-label="Visit Course Assignments for FA17: CMPE-110 Sec 06 - Electronics">FA17: CMPE-110 Sec 06 - Electronics</a>, <a href="/courses/1239787/assignments" aria-label="Visit Course Assignments for FA17: ISE-130 Sec 01 - Engr Statistics">FA17: ISE-130 Sec 01 - Engr Statistics</a>, and 1 more...
            </div>
          </div>
        </div>
        <div class="header-right-side">
          <a href="#" class="toggle-details" aria-controls="details_container">
  <span aria-hidden="true">Show More <i class="icon-mini-arrow-down"></i></span>

<span class="screenreader-only">Expand 20 assignment notifications</span></a>
        </div>
      </div>

      <div class="details_container">
        <table id="assignment-details" class="stream-details">
          <caption class="accessibly-hidden">Assignment Details</caption>
          <thead class="accessibly-hidden">
            <tr>
              <th scope="col">Unread</th>
              <th scope="col">Message</th>
              <th scope="col">Date</th>
              <th></th>
            </tr>
          </thead>
          
<tbody><tr>
  <td>
  </td>
  <td>
    <a href="/courses/1245234/assignments/4558229" class="content_summary">
      <span class="fake-link">FA17: ENGR-100W Sec 43 - Engr Reports</span>
      <strong></strong>
      Assignment Created - Green Talk Assignment #6, FA17: ENGR-100W Sec 43 - Engr Reports
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 19 at  6pm" data-tooltip="top">Oct 19 at  6pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147907981" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1243231/assignments/4558179" class="content_summary">
      <span class="fake-link">FA17: CMPE-124 Sec 07 - Digital Design I</span>
      <strong></strong>
      Assignment Created - Lab 6 Part 1 Physical, FA17: CMPE-124 Sec 07 - Digital Design I
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 19 at  4:58pm" data-tooltip="top">Oct 19 at  4:58pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147905088" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1243231/assignments/4558178" class="content_summary">
      <span class="fake-link">FA17: CMPE-124 Sec 07 - Digital Design I</span>
      <strong></strong>
      Assignment Created - Lab 6 Part 1 Logic Works, FA17: CMPE-124 Sec 07 - Digital Design I
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 19 at  4:56pm" data-tooltip="top">Oct 19 at  4:56pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147905046" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1238555/assignments/4556610" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 06 - Electronics</span>
      <strong></strong>
      Assignment Created - Lab 3, FA17: CMPE-110 Sec 06 - Electronics
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 16 at  8:29pm" data-tooltip="top">Oct 16 at  8:29pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147689473" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1243231/assignments/4555825" class="content_summary">
      <span class="fake-link">FA17: CMPE-124 Sec 07 - Digital Design I</span>
      <strong></strong>
      Assignment Created - Quiz 2, FA17: CMPE-124 Sec 07 - Digital Design I
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 15 at  2:54pm" data-tooltip="top">Oct 15 at  2:54pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147568867" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1245234/assignments/4555137" class="content_summary">
      <span class="fake-link">FA17: ENGR-100W Sec 43 - Engr Reports</span>
      <strong></strong>
      Assignment Created - Green Talk Assignment #5 Energy, William Dunckel, Energy, Environment, and Engineering, FA17: ENGR-100W Sec 43 - Engr Reports
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 13 at  4:42pm" data-tooltip="top">Oct 13 at  4:42pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147515485" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1239787/assignments/4482052" class="content_summary">
      <span class="fake-link">FA17: ISE-130 Sec 01 - Engr Statistics</span>
      <strong></strong>
      Assignment Created - Homework 6, FA17: ISE-130 Sec 01 - Engr Statistics
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 12 at 10:58am" data-tooltip="top">Oct 12 at 10:58am</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147422524" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1238555/assignments/4550135" class="content_summary">
      <span class="fake-link">FA17: CMPE-110 Sec 06 - Electronics</span>
      <strong></strong>
      Assignment Changed: Lab 2, FA17: CMPE-110 Sec 06 - Electronics
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 11 at  7:01pm" data-tooltip="top">Oct 11 at  7:01pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147384420" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1245234/assignments/4554126" class="content_summary">
      <span class="fake-link">FA17: ENGR-100W Sec 43 - Engr Reports</span>
      <strong></strong>
      Assignment Created - Analysis of a Professional Journal, FA17: ENGR-100W Sec 43 - Engr Reports
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 10 at  5:54pm" data-tooltip="top">Oct 10 at  5:54pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147303643" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1245234/assignments/4551946" class="content_summary">
      <span class="fake-link">FA17: ENGR-100W Sec 43 - Engr Reports</span>
      <strong></strong>
      Assignment Created - Green Talk Assignment #4, FA17: ENGR-100W Sec 43 - Engr Reports
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 5 at  3:35pm" data-tooltip="top">Oct 5 at  3:35pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/147013306" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1239787/assignments/4482051" class="content_summary">
      <span class="fake-link">FA17: ISE-130 Sec 01 - Engr Statistics</span>
      <strong></strong>
      Assignment Created - Homework 5, FA17: ISE-130 Sec 01 - Engr Statistics
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 4 at  6:37pm" data-tooltip="top">Oct 4 at  6:37pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146952431" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1240227/assignments/4483943" class="content_summary">
      <span class="fake-link">FA17: CMPE-131 Sec 05 - Software Engr I</span>
      <strong></strong>
      Assignment Created - final, FA17: CMPE-131 Sec 05 - Software Engr I
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 1 at  7:22pm" data-tooltip="top">Oct 1 at  7:22pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146747133" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1240227/assignments/4483942" class="content_summary">
      <span class="fake-link">FA17: CMPE-131 Sec 05 - Software Engr I</span>
      <strong></strong>
      Assignment Created - midterm, FA17: CMPE-131 Sec 05 - Software Engr I
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Oct 1 at  7:22pm" data-tooltip="top">Oct 1 at  7:22pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146747095" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1245234/assignments/4548892" class="content_summary">
      <span class="fake-link">FA17: ENGR-100W Sec 43 - Engr Reports</span>
      <strong></strong>
      Assignment Created - Green Talk #3, FA17: ENGR-100W Sec 43 - Engr Reports
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 29 at  3:40pm" data-tooltip="top">Sep 29 at  3:40pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146687241" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1243231/assignments/4548592" class="content_summary">
      <span class="fake-link">FA17: CMPE-124 Sec 07 - Digital Design I</span>
      <strong></strong>
      Assignment Created - Exam Prep, FA17: CMPE-124 Sec 07 - Digital Design I
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 28 at  4:51pm" data-tooltip="top">Sep 28 at  4:51pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146654857" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1243231/assignments/4548590" class="content_summary">
      <span class="fake-link">FA17: CMPE-124 Sec 07 - Digital Design I</span>
      <strong></strong>
      Assignment Created - Lab 4 Report, FA17: CMPE-124 Sec 07 - Digital Design I
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 28 at  4:48pm" data-tooltip="top">Sep 28 at  4:48pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146654736" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1243231/assignments/4548588" class="content_summary">
      <span class="fake-link">FA17: CMPE-124 Sec 07 - Digital Design I</span>
      <strong></strong>
      Assignment Created - Lab 4 Physical Circuit 2 Demo, FA17: CMPE-124 Sec 07 - Digital Design I
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 28 at  4:46pm" data-tooltip="top">Sep 28 at  4:46pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146654170" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1243231/assignments/4548587" class="content_summary">
      <span class="fake-link">FA17: CMPE-124 Sec 07 - Digital Design I</span>
      <strong></strong>
      Assignment Created - Lab 4 Logicworks Circuit 2 Demo, FA17: CMPE-124 Sec 07 - Digital Design I
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 28 at  4:45pm" data-tooltip="top">Sep 28 at  4:45pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146654090" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1243231/assignments/4548586" class="content_summary">
      <span class="fake-link">FA17: CMPE-124 Sec 07 - Digital Design I</span>
      <strong></strong>
      Assignment Created - Lab 4 Physical Circuit 1 Demo, FA17: CMPE-124 Sec 07 - Digital Design I
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 28 at  4:45pm" data-tooltip="top">Sep 28 at  4:45pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146654044" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

<tr>
  <td>
  </td>
  <td>
    <a href="/courses/1243231/assignments/4548585" class="content_summary">
      <span class="fake-link">FA17: CMPE-124 Sec 07 - Digital Design I</span>
      <strong></strong>
      Assignment Created - Lab 4 Logicworks Circuit 1 Demo, FA17: CMPE-124 Sec 07 - Digital Design I
    </a>
  </td>
  <td class="date" tabindex="0">
    <span data-html-tooltip-title="Sep 28 at  4:43pm" data-tooltip="top">Sep 28 at  4:43pm</span>
  </td>
  <td class="remove">
    <a class="close ignore-item" href="#" data-url="https://sjsu.instructure.com/dashboard/ignore_stream_item/146653978" data-remove="tr" title="Ignore" aria-label="Ignore" role="button">×</a>
  </td>
</tr>

        </tbody></table>
      </div>
    </li>
</ul>


  </div>

  


<div id="DashboardCard_Container" style="display: block"><div class="ic-DashboardCard__box" data-reactid=".1"><div class="ic-DashboardCard" style="opacity:1;" aria-label="FA17: CMPE-110 Sec 04 - Electronics" data-reactid=".1.$1238553"><div class="ic-DashboardCard__header" data-reactid=".1.$1238553.0"><span class="screenreader-only" data-reactid=".1.$1238553.0.0">Course card color region for FA17: CMPE-110 Sec 04 - Electronics</span><div class="ic-DashboardCard__header_hero" style="background-color:#008400;" aria-hidden="true" data-reactid=".1.$1238553.0.1"></div><a href="/courses/1238553" class="ic-DashboardCard__link" data-reactid=".1.$1238553.0.2"><div class="ic-DashboardCard__header_content" data-reactid=".1.$1238553.0.2.0"><h2 class="ic-DashboardCard__header-title ellipsis" title="FA17: CMPE-110 Sec 04 - Electronics" data-reactid=".1.$1238553.0.2.0.0"><span style="color:#008400;" data-reactid=".1.$1238553.0.2.0.0.0">FA17: CMPE-110 Sec 04 - Electronics</span></h2><div class="ic-DashboardCard__header-subtitle ellipsis" title="FA17: CMPE-110 Sec 04 - Electronics" data-reactid=".1.$1238553.0.2.0.1">FA17: CMPE-110 Sec 04 - Electronics</div><div class="ic-DashboardCard__header-term ellipsis" title="Fall 2017" data-reactid=".1.$1238553.0.2.0.2">Fall 2017</div></div></a><div data-reactid=".1.$1238553.0.4"><div class="ic-DashboardCard__header-button-bg" style="background-color:#008400;opacity:0;" data-reactid=".1.$1238553.0.4.0"></div><button aria-controls="DashboardColorPicker-course_1238553" class="Button Button--icon-action-rev ic-DashboardCard__header-button" data-reactid=".1.$1238553.0.4.1" aria-expanded="false"><i class="icon-more" aria-hidden="true" data-reactid=".1.$1238553.0.4.1.0"></i><span class="screenreader-only" data-reactid=".1.$1238553.0.4.1.1">Choose a color or course nickname for FA17: CMPE-110 Sec 04 - Electronics</span></button></div></div><nav class="ic-DashboardCard__action-container" aria-label="Actions for FA17: CMPE-110 Sec 04 - Electronics" data-reactid=".1.$1238553.1"><a href="/courses/1238553/announcements" class="ic-DashboardCard__action announcements" title="Announcements - FA17: CMPE-110 Sec 04 - Electronics" data-reactid=".1.$1238553.1.$/courses/1238553/announcements"><span class="screenreader-only" data-reactid=".1.$1238553.1.$/courses/1238553/announcements.0">Announcements - FA17: CMPE-110 Sec 04 - Electronics</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1238553.1.$/courses/1238553/announcements.1"><i class="icon-announcement" data-reactid=".1.$1238553.1.$/courses/1238553/announcements.1.0"></i><span class="ic-DashboardCard__action-badge" data-reactid=".1.$1238553.1.$/courses/1238553/announcements.1.1"><span class="unread_count" data-reactid=".1.$1238553.1.$/courses/1238553/announcements.1.1.0">14</span><span class="screenreader-only" data-reactid=".1.$1238553.1.$/courses/1238553/announcements.1.1.1">Unread</span></span></div></a><a href="/courses/1238553/discussion_topics" class="ic-DashboardCard__action discussions" title="Discussions - FA17: CMPE-110 Sec 04 - Electronics" data-reactid=".1.$1238553.1.$/courses/1238553/discussion_topics"><span class="screenreader-only" data-reactid=".1.$1238553.1.$/courses/1238553/discussion_topics.0">Discussions - FA17: CMPE-110 Sec 04 - Electronics</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1238553.1.$/courses/1238553/discussion_topics.1"><i class="icon-discussion" data-reactid=".1.$1238553.1.$/courses/1238553/discussion_topics.1.0"></i></div></a><a href="/courses/1238553/files" class="ic-DashboardCard__action files" title="Files - FA17: CMPE-110 Sec 04 - Electronics" data-reactid=".1.$1238553.1.$/courses/1238553/files"><span class="screenreader-only" data-reactid=".1.$1238553.1.$/courses/1238553/files.0">Files - FA17: CMPE-110 Sec 04 - Electronics</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1238553.1.$/courses/1238553/files.1"><i class="icon-folder" data-reactid=".1.$1238553.1.$/courses/1238553/files.1.0"></i></div></a></nav><div id="DashboardColorPicker-course_1238553" class="ic-DashboardCardColorPicker horizontal" style="display:none;" data-reactid=".1.$1238553.2"><div class="ColorPicker__Container with-animation with-arrow with-border with-box-shadow" data-reactid=".1.$1238553.2.0"><div class="ic-Form-control" data-reactid=".1.$1238553.2.0.1"><label for="NicknameInput" class="ic-Label" data-reactid=".1.$1238553.2.0.1.0">Nickname:</label><input id="NicknameInput" type="text" class="ic-Input" maxlength="59" placeholder="FA17: CMPE-110 Sec 04 - Electronics" value="" data-reactid=".1.$1238553.2.0.1.1"></div><div class="ColorPicker__ColorContainer" role="radiogroup" aria-label="Select a predefined color." data-reactid=".1.$1238553.2.0.2"><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#EF4437;border-color:#EF4437;" title="Red (#EF4437)" data-reactid=".1.$1238553.2.0.2.$#EF4437"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#EF4437.1">Red (#EF4437)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#E71F63;border-color:#E71F63;" title="Pink (#E71F63)" data-reactid=".1.$1238553.2.0.2.$#E71F63"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#E71F63.1">Pink (#E71F63)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8F3E97;border-color:#8F3E97;" title="Purple (#8F3E97)" data-reactid=".1.$1238553.2.0.2.$#8F3E97"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#8F3E97.1">Purple (#8F3E97)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#65499D;border-color:#65499D;" title="Deep Purple (#65499D)" data-reactid=".1.$1238553.2.0.2.$#65499D"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#65499D.1">Deep Purple (#65499D)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#4554A4;border-color:#4554A4;" title="Indigo (#4554A4)" data-reactid=".1.$1238553.2.0.2.$#4554A4"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#4554A4.1">Indigo (#4554A4)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#2083C5;border-color:#2083C5;" title="Blue (#2083C5)" data-reactid=".1.$1238553.2.0.2.$#2083C5"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#2083C5.1">Blue (#2083C5)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#35A4DC;border-color:#35A4DC;" title="Light Blue (#35A4DC)" data-reactid=".1.$1238553.2.0.2.$#35A4DC"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#35A4DC.1">Light Blue (#35A4DC)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#09BCD3;border-color:#09BCD3;" title="Cyan (#09BCD3)" data-reactid=".1.$1238553.2.0.2.$#09BCD3"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#09BCD3.1">Cyan (#09BCD3)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#009688;border-color:#009688;" title="Teal (#009688)" data-reactid=".1.$1238553.2.0.2.$#009688"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#009688.1">Teal (#009688)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#43A047;border-color:#43A047;" title="Green (#43A047)" data-reactid=".1.$1238553.2.0.2.$#43A047"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#43A047.1">Green (#43A047)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8BC34A;border-color:#8BC34A;" title="Light Green (#8BC34A)" data-reactid=".1.$1238553.2.0.2.$#8BC34A"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#8BC34A.1">Light Green (#8BC34A)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#FDC010;border-color:#FDC010;" title="Yellow (#FDC010)" data-reactid=".1.$1238553.2.0.2.$#FDC010"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#FDC010.1">Yellow (#FDC010)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F8971C;border-color:#F8971C;" title="Orange (#F8971C)" data-reactid=".1.$1238553.2.0.2.$#F8971C"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#F8971C.1">Orange (#F8971C)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F0592B;border-color:#F0592B;" title="Deep Orange (#F0592B)" data-reactid=".1.$1238553.2.0.2.$#F0592B"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#F0592B.1">Deep Orange (#F0592B)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F06291;border-color:#F06291;" title="Light Pink (#F06291)" data-reactid=".1.$1238553.2.0.2.$#F06291"><span class="screenreader-only" data-reactid=".1.$1238553.2.0.2.$#F06291.1">Light Pink (#F06291)</span></button></div><div class="ColorPicker__CustomInputContainer ic-Input-group" data-reactid=".1.$1238553.2.0.3"><div class="ic-Input-group__add-on ColorPicker__ColorPreview" title="#008400" style="color:#008400;border-color:#d6d6d6;background-color:#008400;" role="presentation" aria-hidden="true" tabindex="-1" data-reactid=".1.$1238553.2.0.3.0"></div><label class="screenreader-only" for="ColorPickerCustomInput-course_1238553" data-reactid=".1.$1238553.2.0.3.1">Enter a hexcode here to use a custom color.</label><input class="ic-Input ColorPicker__CustomInput" id="ColorPickerCustomInput-course_1238553" value="#008400" type="text" maxlength="7" minlength="4" data-reactid=".1.$1238553.2.0.3.2"></div><div class="ColorPicker__Actions" data-reactid=".1.$1238553.2.0.4"><button class="Button" data-reactid=".1.$1238553.2.0.4.0">Cancel</button><span data-reactid=".1.$1238553.2.0.4.1">&nbsp;</span><button class="Button Button--primary" data-reactid=".1.$1238553.2.0.4.2">Apply</button></div></div></div></div><div class="ic-DashboardCard" style="opacity:1;" aria-label="FA17: CMPE-110 Sec 06 - Electronics" data-reactid=".1.$1238555"><div class="ic-DashboardCard__header" data-reactid=".1.$1238555.0"><span class="screenreader-only" data-reactid=".1.$1238555.0.0">Course card color region for FA17: CMPE-110 Sec 06 - Electronics</span><div class="ic-DashboardCard__header_hero" style="background-color:#9F7217;" aria-hidden="true" data-reactid=".1.$1238555.0.1"></div><a href="/courses/1238555" class="ic-DashboardCard__link" data-reactid=".1.$1238555.0.2"><div class="ic-DashboardCard__header_content" data-reactid=".1.$1238555.0.2.0"><h2 class="ic-DashboardCard__header-title ellipsis" title="FA17: CMPE-110 Sec 06 - Electronics" data-reactid=".1.$1238555.0.2.0.0"><span style="color:#9F7217;" data-reactid=".1.$1238555.0.2.0.0.0">FA17: CMPE-110 Sec 06 - Electronics</span></h2><div class="ic-DashboardCard__header-subtitle ellipsis" title="FA17: CMPE-110 Sec 06 - Electronics" data-reactid=".1.$1238555.0.2.0.1">FA17: CMPE-110 Sec 06 - Electronics</div><div class="ic-DashboardCard__header-term ellipsis" title="Fall 2017" data-reactid=".1.$1238555.0.2.0.2">Fall 2017</div></div></a><div data-reactid=".1.$1238555.0.4"><div class="ic-DashboardCard__header-button-bg" style="background-color:#9F7217;opacity:0;" data-reactid=".1.$1238555.0.4.0"></div><button aria-controls="DashboardColorPicker-course_1238555" class="Button Button--icon-action-rev ic-DashboardCard__header-button" data-reactid=".1.$1238555.0.4.1" aria-expanded="false"><i class="icon-more" aria-hidden="true" data-reactid=".1.$1238555.0.4.1.0"></i><span class="screenreader-only" data-reactid=".1.$1238555.0.4.1.1">Choose a color or course nickname for FA17: CMPE-110 Sec 06 - Electronics</span></button></div></div><nav class="ic-DashboardCard__action-container" aria-label="Actions for FA17: CMPE-110 Sec 06 - Electronics" data-reactid=".1.$1238555.1"><a href="/courses/1238555/announcements" class="ic-DashboardCard__action announcements" title="Announcements - FA17: CMPE-110 Sec 06 - Electronics" data-reactid=".1.$1238555.1.$/courses/1238555/announcements"><span class="screenreader-only" data-reactid=".1.$1238555.1.$/courses/1238555/announcements.0">Announcements - FA17: CMPE-110 Sec 06 - Electronics</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1238555.1.$/courses/1238555/announcements.1"><i class="icon-announcement" data-reactid=".1.$1238555.1.$/courses/1238555/announcements.1.0"></i></div></a><a href="/courses/1238555/assignments" class="ic-DashboardCard__action assignments" title="Assignments - FA17: CMPE-110 Sec 06 - Electronics" data-reactid=".1.$1238555.1.$/courses/1238555/assignments"><span class="screenreader-only" data-reactid=".1.$1238555.1.$/courses/1238555/assignments.0">Assignments - FA17: CMPE-110 Sec 06 - Electronics</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1238555.1.$/courses/1238555/assignments.1"><i class="icon-assignment" data-reactid=".1.$1238555.1.$/courses/1238555/assignments.1.0"></i></div></a><a href="/courses/1238555/discussion_topics" class="ic-DashboardCard__action discussions" title="Discussions - FA17: CMPE-110 Sec 06 - Electronics" data-reactid=".1.$1238555.1.$/courses/1238555/discussion_topics"><span class="screenreader-only" data-reactid=".1.$1238555.1.$/courses/1238555/discussion_topics.0">Discussions - FA17: CMPE-110 Sec 06 - Electronics</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1238555.1.$/courses/1238555/discussion_topics.1"><i class="icon-discussion" data-reactid=".1.$1238555.1.$/courses/1238555/discussion_topics.1.0"></i></div></a></nav><div id="DashboardColorPicker-course_1238555" class="ic-DashboardCardColorPicker horizontal" style="display:none;" data-reactid=".1.$1238555.2"><div class="ColorPicker__Container with-animation with-arrow with-border with-box-shadow" data-reactid=".1.$1238555.2.0"><div class="ic-Form-control" data-reactid=".1.$1238555.2.0.1"><label for="NicknameInput" class="ic-Label" data-reactid=".1.$1238555.2.0.1.0">Nickname:</label><input id="NicknameInput" type="text" class="ic-Input" maxlength="59" placeholder="FA17: CMPE-110 Sec 06 - Electronics" value="" data-reactid=".1.$1238555.2.0.1.1"></div><div class="ColorPicker__ColorContainer" role="radiogroup" aria-label="Select a predefined color." data-reactid=".1.$1238555.2.0.2"><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#EF4437;border-color:#EF4437;" title="Red (#EF4437)" data-reactid=".1.$1238555.2.0.2.$#EF4437"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#EF4437.1">Red (#EF4437)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#E71F63;border-color:#E71F63;" title="Pink (#E71F63)" data-reactid=".1.$1238555.2.0.2.$#E71F63"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#E71F63.1">Pink (#E71F63)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8F3E97;border-color:#8F3E97;" title="Purple (#8F3E97)" data-reactid=".1.$1238555.2.0.2.$#8F3E97"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#8F3E97.1">Purple (#8F3E97)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#65499D;border-color:#65499D;" title="Deep Purple (#65499D)" data-reactid=".1.$1238555.2.0.2.$#65499D"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#65499D.1">Deep Purple (#65499D)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#4554A4;border-color:#4554A4;" title="Indigo (#4554A4)" data-reactid=".1.$1238555.2.0.2.$#4554A4"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#4554A4.1">Indigo (#4554A4)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#2083C5;border-color:#2083C5;" title="Blue (#2083C5)" data-reactid=".1.$1238555.2.0.2.$#2083C5"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#2083C5.1">Blue (#2083C5)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#35A4DC;border-color:#35A4DC;" title="Light Blue (#35A4DC)" data-reactid=".1.$1238555.2.0.2.$#35A4DC"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#35A4DC.1">Light Blue (#35A4DC)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#09BCD3;border-color:#09BCD3;" title="Cyan (#09BCD3)" data-reactid=".1.$1238555.2.0.2.$#09BCD3"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#09BCD3.1">Cyan (#09BCD3)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#009688;border-color:#009688;" title="Teal (#009688)" data-reactid=".1.$1238555.2.0.2.$#009688"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#009688.1">Teal (#009688)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#43A047;border-color:#43A047;" title="Green (#43A047)" data-reactid=".1.$1238555.2.0.2.$#43A047"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#43A047.1">Green (#43A047)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8BC34A;border-color:#8BC34A;" title="Light Green (#8BC34A)" data-reactid=".1.$1238555.2.0.2.$#8BC34A"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#8BC34A.1">Light Green (#8BC34A)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#FDC010;border-color:#FDC010;" title="Yellow (#FDC010)" data-reactid=".1.$1238555.2.0.2.$#FDC010"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#FDC010.1">Yellow (#FDC010)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F8971C;border-color:#F8971C;" title="Orange (#F8971C)" data-reactid=".1.$1238555.2.0.2.$#F8971C"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#F8971C.1">Orange (#F8971C)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F0592B;border-color:#F0592B;" title="Deep Orange (#F0592B)" data-reactid=".1.$1238555.2.0.2.$#F0592B"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#F0592B.1">Deep Orange (#F0592B)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F06291;border-color:#F06291;" title="Light Pink (#F06291)" data-reactid=".1.$1238555.2.0.2.$#F06291"><span class="screenreader-only" data-reactid=".1.$1238555.2.0.2.$#F06291.1">Light Pink (#F06291)</span></button></div><div class="ColorPicker__CustomInputContainer ic-Input-group" data-reactid=".1.$1238555.2.0.3"><div class="ic-Input-group__add-on ColorPicker__ColorPreview" title="#9F7217" style="color:#9F7217;border-color:#d6d6d6;background-color:#9F7217;" role="presentation" aria-hidden="true" tabindex="-1" data-reactid=".1.$1238555.2.0.3.0"></div><label class="screenreader-only" for="ColorPickerCustomInput-course_1238555" data-reactid=".1.$1238555.2.0.3.1">Enter a hexcode here to use a custom color.</label><input class="ic-Input ColorPicker__CustomInput" id="ColorPickerCustomInput-course_1238555" value="#9F7217" type="text" maxlength="7" minlength="4" data-reactid=".1.$1238555.2.0.3.2"></div><div class="ColorPicker__Actions" data-reactid=".1.$1238555.2.0.4"><button class="Button" data-reactid=".1.$1238555.2.0.4.0">Cancel</button><span data-reactid=".1.$1238555.2.0.4.1">&nbsp;</span><button class="Button Button--primary" data-reactid=".1.$1238555.2.0.4.2">Apply</button></div></div></div></div><div class="ic-DashboardCard" style="opacity:1;" aria-label="FA17: CMPE-124 Sec 05 - Digital Design I" data-reactid=".1.$1241624"><div class="ic-DashboardCard__header" data-reactid=".1.$1241624.0"><span class="screenreader-only" data-reactid=".1.$1241624.0.0">Course card color region for FA17: CMPE-124 Sec 05 - Digital Design I</span><div class="ic-DashboardCard__header_hero" style="background-color:#E1185C;" aria-hidden="true" data-reactid=".1.$1241624.0.1"></div><a href="/courses/1241624" class="ic-DashboardCard__link" data-reactid=".1.$1241624.0.2"><div class="ic-DashboardCard__header_content" data-reactid=".1.$1241624.0.2.0"><h2 class="ic-DashboardCard__header-title ellipsis" title="FA17: CMPE-124 Sec 05 - Digital Design I" data-reactid=".1.$1241624.0.2.0.0"><span style="color:#E1185C;" data-reactid=".1.$1241624.0.2.0.0.0">FA17: CMPE-124 Sec 05 - Digital Design I</span></h2><div class="ic-DashboardCard__header-subtitle ellipsis" title="FA17: CMPE-124 Sec 05 - Digital Design I" data-reactid=".1.$1241624.0.2.0.1">FA17: CMPE-124 Sec 05 - Digital Design I</div><div class="ic-DashboardCard__header-term ellipsis" title="Fall 2017" data-reactid=".1.$1241624.0.2.0.2">Fall 2017</div></div></a><div data-reactid=".1.$1241624.0.4"><div class="ic-DashboardCard__header-button-bg" style="background-color:#E1185C;opacity:0;" data-reactid=".1.$1241624.0.4.0"></div><button aria-controls="DashboardColorPicker-course_1241624" class="Button Button--icon-action-rev ic-DashboardCard__header-button" data-reactid=".1.$1241624.0.4.1" aria-expanded="false"><i class="icon-more" aria-hidden="true" data-reactid=".1.$1241624.0.4.1.0"></i><span class="screenreader-only" data-reactid=".1.$1241624.0.4.1.1">Choose a color or course nickname for FA17: CMPE-124 Sec 05 - Digital Design I</span></button></div></div><nav class="ic-DashboardCard__action-container" aria-label="Actions for FA17: CMPE-124 Sec 05 - Digital Design I" data-reactid=".1.$1241624.1"><a href="/courses/1241624/discussion_topics" class="ic-DashboardCard__action discussions" title="Discussions - FA17: CMPE-124 Sec 05 - Digital Design I" data-reactid=".1.$1241624.1.$/courses/1241624/discussion_topics"><span class="screenreader-only" data-reactid=".1.$1241624.1.$/courses/1241624/discussion_topics.0">Discussions - FA17: CMPE-124 Sec 05 - Digital Design I</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1241624.1.$/courses/1241624/discussion_topics.1"><i class="icon-discussion" data-reactid=".1.$1241624.1.$/courses/1241624/discussion_topics.1.0"></i></div></a><a href="/courses/1241624/files" class="ic-DashboardCard__action files" title="Files - FA17: CMPE-124 Sec 05 - Digital Design I" data-reactid=".1.$1241624.1.$/courses/1241624/files"><span class="screenreader-only" data-reactid=".1.$1241624.1.$/courses/1241624/files.0">Files - FA17: CMPE-124 Sec 05 - Digital Design I</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1241624.1.$/courses/1241624/files.1"><i class="icon-folder" data-reactid=".1.$1241624.1.$/courses/1241624/files.1.0"></i></div></a></nav><div id="DashboardColorPicker-course_1241624" class="ic-DashboardCardColorPicker horizontal" style="display:none;" data-reactid=".1.$1241624.2"><div class="ColorPicker__Container with-animation with-arrow with-border with-box-shadow" data-reactid=".1.$1241624.2.0"><div class="ic-Form-control" data-reactid=".1.$1241624.2.0.1"><label for="NicknameInput" class="ic-Label" data-reactid=".1.$1241624.2.0.1.0">Nickname:</label><input id="NicknameInput" type="text" class="ic-Input" maxlength="59" placeholder="FA17: CMPE-124 Sec 05 - Digital Design I" value="" data-reactid=".1.$1241624.2.0.1.1"></div><div class="ColorPicker__ColorContainer" role="radiogroup" aria-label="Select a predefined color." data-reactid=".1.$1241624.2.0.2"><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#EF4437;border-color:#EF4437;" title="Red (#EF4437)" data-reactid=".1.$1241624.2.0.2.$#EF4437"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#EF4437.1">Red (#EF4437)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#E71F63;border-color:#E71F63;" title="Pink (#E71F63)" data-reactid=".1.$1241624.2.0.2.$#E71F63"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#E71F63.1">Pink (#E71F63)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8F3E97;border-color:#8F3E97;" title="Purple (#8F3E97)" data-reactid=".1.$1241624.2.0.2.$#8F3E97"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#8F3E97.1">Purple (#8F3E97)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#65499D;border-color:#65499D;" title="Deep Purple (#65499D)" data-reactid=".1.$1241624.2.0.2.$#65499D"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#65499D.1">Deep Purple (#65499D)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#4554A4;border-color:#4554A4;" title="Indigo (#4554A4)" data-reactid=".1.$1241624.2.0.2.$#4554A4"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#4554A4.1">Indigo (#4554A4)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#2083C5;border-color:#2083C5;" title="Blue (#2083C5)" data-reactid=".1.$1241624.2.0.2.$#2083C5"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#2083C5.1">Blue (#2083C5)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#35A4DC;border-color:#35A4DC;" title="Light Blue (#35A4DC)" data-reactid=".1.$1241624.2.0.2.$#35A4DC"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#35A4DC.1">Light Blue (#35A4DC)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#09BCD3;border-color:#09BCD3;" title="Cyan (#09BCD3)" data-reactid=".1.$1241624.2.0.2.$#09BCD3"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#09BCD3.1">Cyan (#09BCD3)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#009688;border-color:#009688;" title="Teal (#009688)" data-reactid=".1.$1241624.2.0.2.$#009688"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#009688.1">Teal (#009688)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#43A047;border-color:#43A047;" title="Green (#43A047)" data-reactid=".1.$1241624.2.0.2.$#43A047"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#43A047.1">Green (#43A047)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8BC34A;border-color:#8BC34A;" title="Light Green (#8BC34A)" data-reactid=".1.$1241624.2.0.2.$#8BC34A"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#8BC34A.1">Light Green (#8BC34A)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#FDC010;border-color:#FDC010;" title="Yellow (#FDC010)" data-reactid=".1.$1241624.2.0.2.$#FDC010"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#FDC010.1">Yellow (#FDC010)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F8971C;border-color:#F8971C;" title="Orange (#F8971C)" data-reactid=".1.$1241624.2.0.2.$#F8971C"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#F8971C.1">Orange (#F8971C)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F0592B;border-color:#F0592B;" title="Deep Orange (#F0592B)" data-reactid=".1.$1241624.2.0.2.$#F0592B"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#F0592B.1">Deep Orange (#F0592B)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F06291;border-color:#F06291;" title="Light Pink (#F06291)" data-reactid=".1.$1241624.2.0.2.$#F06291"><span class="screenreader-only" data-reactid=".1.$1241624.2.0.2.$#F06291.1">Light Pink (#F06291)</span></button></div><div class="ColorPicker__CustomInputContainer ic-Input-group" data-reactid=".1.$1241624.2.0.3"><div class="ic-Input-group__add-on ColorPicker__ColorPreview" title="#E1185C" style="color:#E1185C;border-color:#d6d6d6;background-color:#E1185C;" role="presentation" aria-hidden="true" tabindex="-1" data-reactid=".1.$1241624.2.0.3.0"></div><label class="screenreader-only" for="ColorPickerCustomInput-course_1241624" data-reactid=".1.$1241624.2.0.3.1">Enter a hexcode here to use a custom color.</label><input class="ic-Input ColorPicker__CustomInput" id="ColorPickerCustomInput-course_1241624" value="#E1185C" type="text" maxlength="7" minlength="4" data-reactid=".1.$1241624.2.0.3.2"></div><div class="ColorPicker__Actions" data-reactid=".1.$1241624.2.0.4"><button class="Button" data-reactid=".1.$1241624.2.0.4.0">Cancel</button><span data-reactid=".1.$1241624.2.0.4.1">&nbsp;</span><button class="Button Button--primary" data-reactid=".1.$1241624.2.0.4.2">Apply</button></div></div></div></div><div class="ic-DashboardCard" style="opacity:1;" aria-label="FA17: CMPE-124 Sec 07 - Digital Design I" data-reactid=".1.$1243231"><div class="ic-DashboardCard__header" data-reactid=".1.$1243231.0"><span class="screenreader-only" data-reactid=".1.$1243231.0.0">Course card color region for FA17: CMPE-124 Sec 07 - Digital Design I</span><div class="ic-DashboardCard__header_hero" style="background-color:#008400;" aria-hidden="true" data-reactid=".1.$1243231.0.1"></div><a href="/courses/1243231" class="ic-DashboardCard__link" data-reactid=".1.$1243231.0.2"><div class="ic-DashboardCard__header_content" data-reactid=".1.$1243231.0.2.0"><h2 class="ic-DashboardCard__header-title ellipsis" title="FA17: CMPE-124 Sec 07 - Digital Design I" data-reactid=".1.$1243231.0.2.0.0"><span style="color:#008400;" data-reactid=".1.$1243231.0.2.0.0.0">FA17: CMPE-124 Sec 07 - Digital Design I</span></h2><div class="ic-DashboardCard__header-subtitle ellipsis" title="FA17: CMPE-124 Sec 07 - Digital Design I" data-reactid=".1.$1243231.0.2.0.1">FA17: CMPE-124 Sec 07 - Digital Design I</div><div class="ic-DashboardCard__header-term ellipsis" title="Fall 2017" data-reactid=".1.$1243231.0.2.0.2">Fall 2017</div></div></a><div data-reactid=".1.$1243231.0.4"><div class="ic-DashboardCard__header-button-bg" style="background-color:#008400;opacity:0;" data-reactid=".1.$1243231.0.4.0"></div><button aria-controls="DashboardColorPicker-course_1243231" class="Button Button--icon-action-rev ic-DashboardCard__header-button" data-reactid=".1.$1243231.0.4.1" aria-expanded="false"><i class="icon-more" aria-hidden="true" data-reactid=".1.$1243231.0.4.1.0"></i><span class="screenreader-only" data-reactid=".1.$1243231.0.4.1.1">Choose a color or course nickname for FA17: CMPE-124 Sec 07 - Digital Design I</span></button></div></div><nav class="ic-DashboardCard__action-container" aria-label="Actions for FA17: CMPE-124 Sec 07 - Digital Design I" data-reactid=".1.$1243231.1"><a href="/courses/1243231/announcements" class="ic-DashboardCard__action announcements" title="Announcements - FA17: CMPE-124 Sec 07 - Digital Design I" data-reactid=".1.$1243231.1.$/courses/1243231/announcements"><span class="screenreader-only" data-reactid=".1.$1243231.1.$/courses/1243231/announcements.0">Announcements - FA17: CMPE-124 Sec 07 - Digital Design I</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1243231.1.$/courses/1243231/announcements.1"><i class="icon-announcement" data-reactid=".1.$1243231.1.$/courses/1243231/announcements.1.0"></i></div></a><a href="/courses/1243231/assignments" class="ic-DashboardCard__action assignments" title="Assignments - FA17: CMPE-124 Sec 07 - Digital Design I" data-reactid=".1.$1243231.1.$/courses/1243231/assignments"><span class="screenreader-only" data-reactid=".1.$1243231.1.$/courses/1243231/assignments.0">Assignments - FA17: CMPE-124 Sec 07 - Digital Design I</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1243231.1.$/courses/1243231/assignments.1"><i class="icon-assignment" data-reactid=".1.$1243231.1.$/courses/1243231/assignments.1.0"></i></div></a><a href="/courses/1243231/files" class="ic-DashboardCard__action files" title="Files - FA17: CMPE-124 Sec 07 - Digital Design I" data-reactid=".1.$1243231.1.$/courses/1243231/files"><span class="screenreader-only" data-reactid=".1.$1243231.1.$/courses/1243231/files.0">Files - FA17: CMPE-124 Sec 07 - Digital Design I</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1243231.1.$/courses/1243231/files.1"><i class="icon-folder" data-reactid=".1.$1243231.1.$/courses/1243231/files.1.0"></i></div></a></nav><div id="DashboardColorPicker-course_1243231" class="ic-DashboardCardColorPicker horizontal" style="display:none;" data-reactid=".1.$1243231.2"><div class="ColorPicker__Container with-animation with-arrow with-border with-box-shadow" data-reactid=".1.$1243231.2.0"><div class="ic-Form-control" data-reactid=".1.$1243231.2.0.1"><label for="NicknameInput" class="ic-Label" data-reactid=".1.$1243231.2.0.1.0">Nickname:</label><input id="NicknameInput" type="text" class="ic-Input" maxlength="59" placeholder="FA17: CMPE-124 Sec 07 - Digital Design I" value="" data-reactid=".1.$1243231.2.0.1.1"></div><div class="ColorPicker__ColorContainer" role="radiogroup" aria-label="Select a predefined color." data-reactid=".1.$1243231.2.0.2"><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#EF4437;border-color:#EF4437;" title="Red (#EF4437)" data-reactid=".1.$1243231.2.0.2.$#EF4437"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#EF4437.1">Red (#EF4437)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#E71F63;border-color:#E71F63;" title="Pink (#E71F63)" data-reactid=".1.$1243231.2.0.2.$#E71F63"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#E71F63.1">Pink (#E71F63)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8F3E97;border-color:#8F3E97;" title="Purple (#8F3E97)" data-reactid=".1.$1243231.2.0.2.$#8F3E97"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#8F3E97.1">Purple (#8F3E97)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#65499D;border-color:#65499D;" title="Deep Purple (#65499D)" data-reactid=".1.$1243231.2.0.2.$#65499D"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#65499D.1">Deep Purple (#65499D)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#4554A4;border-color:#4554A4;" title="Indigo (#4554A4)" data-reactid=".1.$1243231.2.0.2.$#4554A4"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#4554A4.1">Indigo (#4554A4)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#2083C5;border-color:#2083C5;" title="Blue (#2083C5)" data-reactid=".1.$1243231.2.0.2.$#2083C5"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#2083C5.1">Blue (#2083C5)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#35A4DC;border-color:#35A4DC;" title="Light Blue (#35A4DC)" data-reactid=".1.$1243231.2.0.2.$#35A4DC"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#35A4DC.1">Light Blue (#35A4DC)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#09BCD3;border-color:#09BCD3;" title="Cyan (#09BCD3)" data-reactid=".1.$1243231.2.0.2.$#09BCD3"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#09BCD3.1">Cyan (#09BCD3)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#009688;border-color:#009688;" title="Teal (#009688)" data-reactid=".1.$1243231.2.0.2.$#009688"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#009688.1">Teal (#009688)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#43A047;border-color:#43A047;" title="Green (#43A047)" data-reactid=".1.$1243231.2.0.2.$#43A047"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#43A047.1">Green (#43A047)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8BC34A;border-color:#8BC34A;" title="Light Green (#8BC34A)" data-reactid=".1.$1243231.2.0.2.$#8BC34A"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#8BC34A.1">Light Green (#8BC34A)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#FDC010;border-color:#FDC010;" title="Yellow (#FDC010)" data-reactid=".1.$1243231.2.0.2.$#FDC010"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#FDC010.1">Yellow (#FDC010)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F8971C;border-color:#F8971C;" title="Orange (#F8971C)" data-reactid=".1.$1243231.2.0.2.$#F8971C"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#F8971C.1">Orange (#F8971C)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F0592B;border-color:#F0592B;" title="Deep Orange (#F0592B)" data-reactid=".1.$1243231.2.0.2.$#F0592B"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#F0592B.1">Deep Orange (#F0592B)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F06291;border-color:#F06291;" title="Light Pink (#F06291)" data-reactid=".1.$1243231.2.0.2.$#F06291"><span class="screenreader-only" data-reactid=".1.$1243231.2.0.2.$#F06291.1">Light Pink (#F06291)</span></button></div><div class="ColorPicker__CustomInputContainer ic-Input-group" data-reactid=".1.$1243231.2.0.3"><div class="ic-Input-group__add-on ColorPicker__ColorPreview" title="#008400" style="color:#008400;border-color:#d6d6d6;background-color:#008400;" role="presentation" aria-hidden="true" tabindex="-1" data-reactid=".1.$1243231.2.0.3.0"></div><label class="screenreader-only" for="ColorPickerCustomInput-course_1243231" data-reactid=".1.$1243231.2.0.3.1">Enter a hexcode here to use a custom color.</label><input class="ic-Input ColorPicker__CustomInput" id="ColorPickerCustomInput-course_1243231" value="#008400" type="text" maxlength="7" minlength="4" data-reactid=".1.$1243231.2.0.3.2"></div><div class="ColorPicker__Actions" data-reactid=".1.$1243231.2.0.4"><button class="Button" data-reactid=".1.$1243231.2.0.4.0">Cancel</button><span data-reactid=".1.$1243231.2.0.4.1">&nbsp;</span><button class="Button Button--primary" data-reactid=".1.$1243231.2.0.4.2">Apply</button></div></div></div></div><div class="ic-DashboardCard" style="opacity:1;" aria-label="FA17: CMPE-131 Sec 05 - Software Engr I" data-reactid=".1.$1240227"><div class="ic-DashboardCard__header" data-reactid=".1.$1240227.0"><span class="screenreader-only" data-reactid=".1.$1240227.0.0">Course card color region for FA17: CMPE-131 Sec 05 - Software Engr I</span><div class="ic-DashboardCard__header_hero" style="background-color:#324A4D;" aria-hidden="true" data-reactid=".1.$1240227.0.1"></div><a href="/courses/1240227" class="ic-DashboardCard__link" data-reactid=".1.$1240227.0.2"><div class="ic-DashboardCard__header_content" data-reactid=".1.$1240227.0.2.0"><h2 class="ic-DashboardCard__header-title ellipsis" title="FA17: CMPE-131 Sec 05 - Software Engr I" data-reactid=".1.$1240227.0.2.0.0"><span style="color:#324A4D;" data-reactid=".1.$1240227.0.2.0.0.0">FA17: CMPE-131 Sec 05 - Software Engr I</span></h2><div class="ic-DashboardCard__header-subtitle ellipsis" title="FA17: CMPE-131 Sec 05 - Software Engr I" data-reactid=".1.$1240227.0.2.0.1">FA17: CMPE-131 Sec 05 - Software Engr I</div><div class="ic-DashboardCard__header-term ellipsis" title="Fall 2017" data-reactid=".1.$1240227.0.2.0.2">Fall 2017</div></div></a><div data-reactid=".1.$1240227.0.4"><div class="ic-DashboardCard__header-button-bg" style="background-color:#324A4D;opacity:0;" data-reactid=".1.$1240227.0.4.0"></div><button aria-controls="DashboardColorPicker-course_1240227" class="Button Button--icon-action-rev ic-DashboardCard__header-button" data-reactid=".1.$1240227.0.4.1" aria-expanded="false"><i class="icon-more" aria-hidden="true" data-reactid=".1.$1240227.0.4.1.0"></i><span class="screenreader-only" data-reactid=".1.$1240227.0.4.1.1">Choose a color or course nickname for FA17: CMPE-131 Sec 05 - Software Engr I</span></button></div></div><nav class="ic-DashboardCard__action-container" aria-label="Actions for FA17: CMPE-131 Sec 05 - Software Engr I" data-reactid=".1.$1240227.1"><a href="/courses/1240227/announcements" class="ic-DashboardCard__action announcements" title="Announcements - FA17: CMPE-131 Sec 05 - Software Engr I" data-reactid=".1.$1240227.1.$/courses/1240227/announcements"><span class="screenreader-only" data-reactid=".1.$1240227.1.$/courses/1240227/announcements.0">Announcements - FA17: CMPE-131 Sec 05 - Software Engr I</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1240227.1.$/courses/1240227/announcements.1"><i class="icon-announcement" data-reactid=".1.$1240227.1.$/courses/1240227/announcements.1.0"></i><span class="ic-DashboardCard__action-badge" data-reactid=".1.$1240227.1.$/courses/1240227/announcements.1.1"><span class="unread_count" data-reactid=".1.$1240227.1.$/courses/1240227/announcements.1.1.0">10</span><span class="screenreader-only" data-reactid=".1.$1240227.1.$/courses/1240227/announcements.1.1.1">Unread</span></span></div></a><a href="/courses/1240227/assignments" class="ic-DashboardCard__action assignments" title="Assignments - FA17: CMPE-131 Sec 05 - Software Engr I" data-reactid=".1.$1240227.1.$/courses/1240227/assignments"><span class="screenreader-only" data-reactid=".1.$1240227.1.$/courses/1240227/assignments.0">Assignments - FA17: CMPE-131 Sec 05 - Software Engr I</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1240227.1.$/courses/1240227/assignments.1"><i class="icon-assignment" data-reactid=".1.$1240227.1.$/courses/1240227/assignments.1.0"></i></div></a><a href="/courses/1240227/discussion_topics" class="ic-DashboardCard__action discussions" title="Discussions - FA17: CMPE-131 Sec 05 - Software Engr I" data-reactid=".1.$1240227.1.$/courses/1240227/discussion_topics"><span class="screenreader-only" data-reactid=".1.$1240227.1.$/courses/1240227/discussion_topics.0">Discussions - FA17: CMPE-131 Sec 05 - Software Engr I</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1240227.1.$/courses/1240227/discussion_topics.1"><i class="icon-discussion" data-reactid=".1.$1240227.1.$/courses/1240227/discussion_topics.1.0"></i></div></a><a href="/courses/1240227/files" class="ic-DashboardCard__action files" title="Files - FA17: CMPE-131 Sec 05 - Software Engr I" data-reactid=".1.$1240227.1.$/courses/1240227/files"><span class="screenreader-only" data-reactid=".1.$1240227.1.$/courses/1240227/files.0">Files - FA17: CMPE-131 Sec 05 - Software Engr I</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1240227.1.$/courses/1240227/files.1"><i class="icon-folder" data-reactid=".1.$1240227.1.$/courses/1240227/files.1.0"></i></div></a></nav><div id="DashboardColorPicker-course_1240227" class="ic-DashboardCardColorPicker horizontal" style="display:none;" data-reactid=".1.$1240227.2"><div class="ColorPicker__Container with-animation with-arrow with-border with-box-shadow" data-reactid=".1.$1240227.2.0"><div class="ic-Form-control" data-reactid=".1.$1240227.2.0.1"><label for="NicknameInput" class="ic-Label" data-reactid=".1.$1240227.2.0.1.0">Nickname:</label><input id="NicknameInput" type="text" class="ic-Input" maxlength="59" placeholder="FA17: CMPE-131 Sec 05 - Software Engr I" value="" data-reactid=".1.$1240227.2.0.1.1"></div><div class="ColorPicker__ColorContainer" role="radiogroup" aria-label="Select a predefined color." data-reactid=".1.$1240227.2.0.2"><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#EF4437;border-color:#EF4437;" title="Red (#EF4437)" data-reactid=".1.$1240227.2.0.2.$#EF4437"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#EF4437.1">Red (#EF4437)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#E71F63;border-color:#E71F63;" title="Pink (#E71F63)" data-reactid=".1.$1240227.2.0.2.$#E71F63"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#E71F63.1">Pink (#E71F63)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8F3E97;border-color:#8F3E97;" title="Purple (#8F3E97)" data-reactid=".1.$1240227.2.0.2.$#8F3E97"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#8F3E97.1">Purple (#8F3E97)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#65499D;border-color:#65499D;" title="Deep Purple (#65499D)" data-reactid=".1.$1240227.2.0.2.$#65499D"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#65499D.1">Deep Purple (#65499D)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#4554A4;border-color:#4554A4;" title="Indigo (#4554A4)" data-reactid=".1.$1240227.2.0.2.$#4554A4"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#4554A4.1">Indigo (#4554A4)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#2083C5;border-color:#2083C5;" title="Blue (#2083C5)" data-reactid=".1.$1240227.2.0.2.$#2083C5"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#2083C5.1">Blue (#2083C5)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#35A4DC;border-color:#35A4DC;" title="Light Blue (#35A4DC)" data-reactid=".1.$1240227.2.0.2.$#35A4DC"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#35A4DC.1">Light Blue (#35A4DC)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#09BCD3;border-color:#09BCD3;" title="Cyan (#09BCD3)" data-reactid=".1.$1240227.2.0.2.$#09BCD3"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#09BCD3.1">Cyan (#09BCD3)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#009688;border-color:#009688;" title="Teal (#009688)" data-reactid=".1.$1240227.2.0.2.$#009688"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#009688.1">Teal (#009688)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#43A047;border-color:#43A047;" title="Green (#43A047)" data-reactid=".1.$1240227.2.0.2.$#43A047"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#43A047.1">Green (#43A047)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8BC34A;border-color:#8BC34A;" title="Light Green (#8BC34A)" data-reactid=".1.$1240227.2.0.2.$#8BC34A"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#8BC34A.1">Light Green (#8BC34A)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#FDC010;border-color:#FDC010;" title="Yellow (#FDC010)" data-reactid=".1.$1240227.2.0.2.$#FDC010"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#FDC010.1">Yellow (#FDC010)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F8971C;border-color:#F8971C;" title="Orange (#F8971C)" data-reactid=".1.$1240227.2.0.2.$#F8971C"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#F8971C.1">Orange (#F8971C)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F0592B;border-color:#F0592B;" title="Deep Orange (#F0592B)" data-reactid=".1.$1240227.2.0.2.$#F0592B"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#F0592B.1">Deep Orange (#F0592B)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F06291;border-color:#F06291;" title="Light Pink (#F06291)" data-reactid=".1.$1240227.2.0.2.$#F06291"><span class="screenreader-only" data-reactid=".1.$1240227.2.0.2.$#F06291.1">Light Pink (#F06291)</span></button></div><div class="ColorPicker__CustomInputContainer ic-Input-group" data-reactid=".1.$1240227.2.0.3"><div class="ic-Input-group__add-on ColorPicker__ColorPreview" title="#324A4D" style="color:#324A4D;border-color:#d6d6d6;background-color:#324A4D;" role="presentation" aria-hidden="true" tabindex="-1" data-reactid=".1.$1240227.2.0.3.0"></div><label class="screenreader-only" for="ColorPickerCustomInput-course_1240227" data-reactid=".1.$1240227.2.0.3.1">Enter a hexcode here to use a custom color.</label><input class="ic-Input ColorPicker__CustomInput" id="ColorPickerCustomInput-course_1240227" value="#324A4D" type="text" maxlength="7" minlength="4" data-reactid=".1.$1240227.2.0.3.2"></div><div class="ColorPicker__Actions" data-reactid=".1.$1240227.2.0.4"><button class="Button" data-reactid=".1.$1240227.2.0.4.0">Cancel</button><span data-reactid=".1.$1240227.2.0.4.1">&nbsp;</span><button class="Button Button--primary" data-reactid=".1.$1240227.2.0.4.2">Apply</button></div></div></div></div><div class="ic-DashboardCard" style="opacity:1;" aria-label="FA17: ENGR-100W Sec 43 - Engr Reports" data-reactid=".1.$1245234"><div class="ic-DashboardCard__header" data-reactid=".1.$1245234.0"><span class="screenreader-only" data-reactid=".1.$1245234.0.0">Course card color region for FA17: ENGR-100W Sec 43 - Engr Reports</span><div class="ic-DashboardCard__header_hero" style="background-color:#626E7B;" aria-hidden="true" data-reactid=".1.$1245234.0.1"></div><a href="/courses/1245234" class="ic-DashboardCard__link" data-reactid=".1.$1245234.0.2"><div class="ic-DashboardCard__header_content" data-reactid=".1.$1245234.0.2.0"><h2 class="ic-DashboardCard__header-title ellipsis" title="FA17: ENGR-100W Sec 43 - Engr Reports" data-reactid=".1.$1245234.0.2.0.0"><span style="color:#626E7B;" data-reactid=".1.$1245234.0.2.0.0.0">FA17: ENGR-100W Sec 43 - Engr Reports</span></h2><div class="ic-DashboardCard__header-subtitle ellipsis" title="FA17: ENGR-100W Sec 43 - Engr Reports" data-reactid=".1.$1245234.0.2.0.1">FA17: ENGR-100W Sec 43 - Engr Reports</div><div class="ic-DashboardCard__header-term ellipsis" title="Fall 2017" data-reactid=".1.$1245234.0.2.0.2">Fall 2017</div></div></a><div data-reactid=".1.$1245234.0.4"><div class="ic-DashboardCard__header-button-bg" style="background-color:#626E7B;opacity:0;" data-reactid=".1.$1245234.0.4.0"></div><button aria-controls="DashboardColorPicker-course_1245234" class="Button Button--icon-action-rev ic-DashboardCard__header-button" data-reactid=".1.$1245234.0.4.1" aria-expanded="false"><i class="icon-more" aria-hidden="true" data-reactid=".1.$1245234.0.4.1.0"></i><span class="screenreader-only" data-reactid=".1.$1245234.0.4.1.1">Choose a color or course nickname for FA17: ENGR-100W Sec 43 - Engr Reports</span></button></div></div><nav class="ic-DashboardCard__action-container" aria-label="Actions for FA17: ENGR-100W Sec 43 - Engr Reports" data-reactid=".1.$1245234.1"><a href="/courses/1245234/assignments" class="ic-DashboardCard__action assignments" title="Assignments - FA17: ENGR-100W Sec 43 - Engr Reports" data-reactid=".1.$1245234.1.$/courses/1245234/assignments"><span class="screenreader-only" data-reactid=".1.$1245234.1.$/courses/1245234/assignments.0">Assignments - FA17: ENGR-100W Sec 43 - Engr Reports</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1245234.1.$/courses/1245234/assignments.1"><i class="icon-assignment" data-reactid=".1.$1245234.1.$/courses/1245234/assignments.1.0"></i></div></a><a href="/courses/1245234/discussion_topics" class="ic-DashboardCard__action discussions" title="Discussions - FA17: ENGR-100W Sec 43 - Engr Reports" data-reactid=".1.$1245234.1.$/courses/1245234/discussion_topics"><span class="screenreader-only" data-reactid=".1.$1245234.1.$/courses/1245234/discussion_topics.0">Discussions - FA17: ENGR-100W Sec 43 - Engr Reports</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1245234.1.$/courses/1245234/discussion_topics.1"><i class="icon-discussion" data-reactid=".1.$1245234.1.$/courses/1245234/discussion_topics.1.0"></i></div></a><a href="/courses/1245234/files" class="ic-DashboardCard__action files" title="Files - FA17: ENGR-100W Sec 43 - Engr Reports" data-reactid=".1.$1245234.1.$/courses/1245234/files"><span class="screenreader-only" data-reactid=".1.$1245234.1.$/courses/1245234/files.0">Files - FA17: ENGR-100W Sec 43 - Engr Reports</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1245234.1.$/courses/1245234/files.1"><i class="icon-folder" data-reactid=".1.$1245234.1.$/courses/1245234/files.1.0"></i></div></a></nav><div id="DashboardColorPicker-course_1245234" class="ic-DashboardCardColorPicker horizontal" style="display:none;" data-reactid=".1.$1245234.2"><div class="ColorPicker__Container with-animation with-arrow with-border with-box-shadow" data-reactid=".1.$1245234.2.0"><div class="ic-Form-control" data-reactid=".1.$1245234.2.0.1"><label for="NicknameInput" class="ic-Label" data-reactid=".1.$1245234.2.0.1.0">Nickname:</label><input id="NicknameInput" type="text" class="ic-Input" maxlength="59" placeholder="FA17: ENGR-100W Sec 43 - Engr Reports" value="" data-reactid=".1.$1245234.2.0.1.1"></div><div class="ColorPicker__ColorContainer" role="radiogroup" aria-label="Select a predefined color." data-reactid=".1.$1245234.2.0.2"><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#EF4437;border-color:#EF4437;" title="Red (#EF4437)" data-reactid=".1.$1245234.2.0.2.$#EF4437"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#EF4437.1">Red (#EF4437)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#E71F63;border-color:#E71F63;" title="Pink (#E71F63)" data-reactid=".1.$1245234.2.0.2.$#E71F63"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#E71F63.1">Pink (#E71F63)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8F3E97;border-color:#8F3E97;" title="Purple (#8F3E97)" data-reactid=".1.$1245234.2.0.2.$#8F3E97"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#8F3E97.1">Purple (#8F3E97)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#65499D;border-color:#65499D;" title="Deep Purple (#65499D)" data-reactid=".1.$1245234.2.0.2.$#65499D"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#65499D.1">Deep Purple (#65499D)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#4554A4;border-color:#4554A4;" title="Indigo (#4554A4)" data-reactid=".1.$1245234.2.0.2.$#4554A4"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#4554A4.1">Indigo (#4554A4)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#2083C5;border-color:#2083C5;" title="Blue (#2083C5)" data-reactid=".1.$1245234.2.0.2.$#2083C5"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#2083C5.1">Blue (#2083C5)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#35A4DC;border-color:#35A4DC;" title="Light Blue (#35A4DC)" data-reactid=".1.$1245234.2.0.2.$#35A4DC"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#35A4DC.1">Light Blue (#35A4DC)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#09BCD3;border-color:#09BCD3;" title="Cyan (#09BCD3)" data-reactid=".1.$1245234.2.0.2.$#09BCD3"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#09BCD3.1">Cyan (#09BCD3)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#009688;border-color:#009688;" title="Teal (#009688)" data-reactid=".1.$1245234.2.0.2.$#009688"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#009688.1">Teal (#009688)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#43A047;border-color:#43A047;" title="Green (#43A047)" data-reactid=".1.$1245234.2.0.2.$#43A047"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#43A047.1">Green (#43A047)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8BC34A;border-color:#8BC34A;" title="Light Green (#8BC34A)" data-reactid=".1.$1245234.2.0.2.$#8BC34A"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#8BC34A.1">Light Green (#8BC34A)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#FDC010;border-color:#FDC010;" title="Yellow (#FDC010)" data-reactid=".1.$1245234.2.0.2.$#FDC010"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#FDC010.1">Yellow (#FDC010)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F8971C;border-color:#F8971C;" title="Orange (#F8971C)" data-reactid=".1.$1245234.2.0.2.$#F8971C"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#F8971C.1">Orange (#F8971C)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F0592B;border-color:#F0592B;" title="Deep Orange (#F0592B)" data-reactid=".1.$1245234.2.0.2.$#F0592B"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#F0592B.1">Deep Orange (#F0592B)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F06291;border-color:#F06291;" title="Light Pink (#F06291)" data-reactid=".1.$1245234.2.0.2.$#F06291"><span class="screenreader-only" data-reactid=".1.$1245234.2.0.2.$#F06291.1">Light Pink (#F06291)</span></button></div><div class="ColorPicker__CustomInputContainer ic-Input-group" data-reactid=".1.$1245234.2.0.3"><div class="ic-Input-group__add-on ColorPicker__ColorPreview" title="#626E7B" style="color:#626E7B;border-color:#d6d6d6;background-color:#626E7B;" role="presentation" aria-hidden="true" tabindex="-1" data-reactid=".1.$1245234.2.0.3.0"></div><label class="screenreader-only" for="ColorPickerCustomInput-course_1245234" data-reactid=".1.$1245234.2.0.3.1">Enter a hexcode here to use a custom color.</label><input class="ic-Input ColorPicker__CustomInput" id="ColorPickerCustomInput-course_1245234" value="#626E7B" type="text" maxlength="7" minlength="4" data-reactid=".1.$1245234.2.0.3.2"></div><div class="ColorPicker__Actions" data-reactid=".1.$1245234.2.0.4"><button class="Button" data-reactid=".1.$1245234.2.0.4.0">Cancel</button><span data-reactid=".1.$1245234.2.0.4.1">&nbsp;</span><button class="Button Button--primary" data-reactid=".1.$1245234.2.0.4.2">Apply</button></div></div></div></div><div class="ic-DashboardCard" style="opacity:1;" aria-label="FA17: ISE-130 Sec 01 - Engr Statistics" data-reactid=".1.$1239787"><div class="ic-DashboardCard__header" data-reactid=".1.$1239787.0"><span class="screenreader-only" data-reactid=".1.$1239787.0.0">Course card color region for FA17: ISE-130 Sec 01 - Engr Statistics</span><div class="ic-DashboardCard__header_hero" style="background-color:#91349B;" aria-hidden="true" data-reactid=".1.$1239787.0.1"></div><a href="/courses/1239787" class="ic-DashboardCard__link" data-reactid=".1.$1239787.0.2"><div class="ic-DashboardCard__header_content" data-reactid=".1.$1239787.0.2.0"><h2 class="ic-DashboardCard__header-title ellipsis" title="FA17: ISE-130 Sec 01 - Engr Statistics" data-reactid=".1.$1239787.0.2.0.0"><span style="color:#91349B;" data-reactid=".1.$1239787.0.2.0.0.0">FA17: ISE-130 Sec 01 - Engr Statistics</span></h2><div class="ic-DashboardCard__header-subtitle ellipsis" title="FA17: ISE-130 Sec 01 - Engr Statistics" data-reactid=".1.$1239787.0.2.0.1">FA17: ISE-130 Sec 01 - Engr Statistics</div><div class="ic-DashboardCard__header-term ellipsis" title="Fall 2017" data-reactid=".1.$1239787.0.2.0.2">Fall 2017</div></div></a><div data-reactid=".1.$1239787.0.4"><div class="ic-DashboardCard__header-button-bg" style="background-color:#91349B;opacity:0;" data-reactid=".1.$1239787.0.4.0"></div><button aria-controls="DashboardColorPicker-course_1239787" class="Button Button--icon-action-rev ic-DashboardCard__header-button" data-reactid=".1.$1239787.0.4.1" aria-expanded="false"><i class="icon-more" aria-hidden="true" data-reactid=".1.$1239787.0.4.1.0"></i><span class="screenreader-only" data-reactid=".1.$1239787.0.4.1.1">Choose a color or course nickname for FA17: ISE-130 Sec 01 - Engr Statistics</span></button></div></div><nav class="ic-DashboardCard__action-container" aria-label="Actions for FA17: ISE-130 Sec 01 - Engr Statistics" data-reactid=".1.$1239787.1"><a href="/courses/1239787/announcements" class="ic-DashboardCard__action announcements" title="Announcements - FA17: ISE-130 Sec 01 - Engr Statistics" data-reactid=".1.$1239787.1.$/courses/1239787/announcements"><span class="screenreader-only" data-reactid=".1.$1239787.1.$/courses/1239787/announcements.0">Announcements - FA17: ISE-130 Sec 01 - Engr Statistics</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1239787.1.$/courses/1239787/announcements.1"><i class="icon-announcement" data-reactid=".1.$1239787.1.$/courses/1239787/announcements.1.0"></i><span class="ic-DashboardCard__action-badge" data-reactid=".1.$1239787.1.$/courses/1239787/announcements.1.1"><span class="unread_count" data-reactid=".1.$1239787.1.$/courses/1239787/announcements.1.1.0">2</span><span class="screenreader-only" data-reactid=".1.$1239787.1.$/courses/1239787/announcements.1.1.1">Unread</span></span></div></a><a href="/courses/1239787/assignments" class="ic-DashboardCard__action assignments" title="Assignments - FA17: ISE-130 Sec 01 - Engr Statistics" data-reactid=".1.$1239787.1.$/courses/1239787/assignments"><span class="screenreader-only" data-reactid=".1.$1239787.1.$/courses/1239787/assignments.0">Assignments - FA17: ISE-130 Sec 01 - Engr Statistics</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1239787.1.$/courses/1239787/assignments.1"><i class="icon-assignment" data-reactid=".1.$1239787.1.$/courses/1239787/assignments.1.0"></i></div></a><a href="/courses/1239787/discussion_topics" class="ic-DashboardCard__action discussions" title="Discussions - FA17: ISE-130 Sec 01 - Engr Statistics" data-reactid=".1.$1239787.1.$/courses/1239787/discussion_topics"><span class="screenreader-only" data-reactid=".1.$1239787.1.$/courses/1239787/discussion_topics.0">Discussions - FA17: ISE-130 Sec 01 - Engr Statistics</span><div class="ic-DashboardCard__action-layout" data-reactid=".1.$1239787.1.$/courses/1239787/discussion_topics.1"><i class="icon-discussion" data-reactid=".1.$1239787.1.$/courses/1239787/discussion_topics.1.0"></i></div></a></nav><div id="DashboardColorPicker-course_1239787" class="ic-DashboardCardColorPicker horizontal" style="display:none;" data-reactid=".1.$1239787.2"><div class="ColorPicker__Container with-animation with-arrow with-border with-box-shadow" data-reactid=".1.$1239787.2.0"><div class="ic-Form-control" data-reactid=".1.$1239787.2.0.1"><label for="NicknameInput" class="ic-Label" data-reactid=".1.$1239787.2.0.1.0">Nickname:</label><input id="NicknameInput" type="text" class="ic-Input" maxlength="59" placeholder="FA17: ISE-130 Sec 01 - Engr Statistics" value="" data-reactid=".1.$1239787.2.0.1.1"></div><div class="ColorPicker__ColorContainer" role="radiogroup" aria-label="Select a predefined color." data-reactid=".1.$1239787.2.0.2"><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#EF4437;border-color:#EF4437;" title="Red (#EF4437)" data-reactid=".1.$1239787.2.0.2.$#EF4437"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#EF4437.1">Red (#EF4437)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#E71F63;border-color:#E71F63;" title="Pink (#E71F63)" data-reactid=".1.$1239787.2.0.2.$#E71F63"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#E71F63.1">Pink (#E71F63)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8F3E97;border-color:#8F3E97;" title="Purple (#8F3E97)" data-reactid=".1.$1239787.2.0.2.$#8F3E97"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#8F3E97.1">Purple (#8F3E97)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#65499D;border-color:#65499D;" title="Deep Purple (#65499D)" data-reactid=".1.$1239787.2.0.2.$#65499D"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#65499D.1">Deep Purple (#65499D)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#4554A4;border-color:#4554A4;" title="Indigo (#4554A4)" data-reactid=".1.$1239787.2.0.2.$#4554A4"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#4554A4.1">Indigo (#4554A4)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#2083C5;border-color:#2083C5;" title="Blue (#2083C5)" data-reactid=".1.$1239787.2.0.2.$#2083C5"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#2083C5.1">Blue (#2083C5)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#35A4DC;border-color:#35A4DC;" title="Light Blue (#35A4DC)" data-reactid=".1.$1239787.2.0.2.$#35A4DC"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#35A4DC.1">Light Blue (#35A4DC)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#09BCD3;border-color:#09BCD3;" title="Cyan (#09BCD3)" data-reactid=".1.$1239787.2.0.2.$#09BCD3"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#09BCD3.1">Cyan (#09BCD3)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#009688;border-color:#009688;" title="Teal (#009688)" data-reactid=".1.$1239787.2.0.2.$#009688"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#009688.1">Teal (#009688)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#43A047;border-color:#43A047;" title="Green (#43A047)" data-reactid=".1.$1239787.2.0.2.$#43A047"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#43A047.1">Green (#43A047)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#8BC34A;border-color:#8BC34A;" title="Light Green (#8BC34A)" data-reactid=".1.$1239787.2.0.2.$#8BC34A"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#8BC34A.1">Light Green (#8BC34A)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#FDC010;border-color:#FDC010;" title="Yellow (#FDC010)" data-reactid=".1.$1239787.2.0.2.$#FDC010"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#FDC010.1">Yellow (#FDC010)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F8971C;border-color:#F8971C;" title="Orange (#F8971C)" data-reactid=".1.$1239787.2.0.2.$#F8971C"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#F8971C.1">Orange (#F8971C)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F0592B;border-color:#F0592B;" title="Deep Orange (#F0592B)" data-reactid=".1.$1239787.2.0.2.$#F0592B"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#F0592B.1">Deep Orange (#F0592B)</span></button><button class="ColorPicker__ColorBlock" role="radio" aria-checked="false" style="background-color:#F06291;border-color:#F06291;" title="Light Pink (#F06291)" data-reactid=".1.$1239787.2.0.2.$#F06291"><span class="screenreader-only" data-reactid=".1.$1239787.2.0.2.$#F06291.1">Light Pink (#F06291)</span></button></div><div class="ColorPicker__CustomInputContainer ic-Input-group" data-reactid=".1.$1239787.2.0.3"><div class="ic-Input-group__add-on ColorPicker__ColorPreview" title="#91349B" style="color:#91349B;border-color:#d6d6d6;background-color:#91349B;" role="presentation" aria-hidden="true" tabindex="-1" data-reactid=".1.$1239787.2.0.3.0"></div><label class="screenreader-only" for="ColorPickerCustomInput-course_1239787" data-reactid=".1.$1239787.2.0.3.1">Enter a hexcode here to use a custom color.</label><input class="ic-Input ColorPicker__CustomInput" id="ColorPickerCustomInput-course_1239787" value="#91349B" type="text" maxlength="7" minlength="4" data-reactid=".1.$1239787.2.0.3.2"></div><div class="ColorPicker__Actions" data-reactid=".1.$1239787.2.0.4"><button class="Button" data-reactid=".1.$1239787.2.0.4.0">Cancel</button><span data-reactid=".1.$1239787.2.0.4.1">&nbsp;</span><button class="Button Button--primary" data-reactid=".1.$1239787.2.0.4.2">Apply</button></div></div></div></div></div></div>

</div>

          </div>
        </div>
        <div id="right-side-wrapper" class="ic-app-main-content__secondary">
          <aside id="right-side" role="complementary" style="opacity: 1; display: block;">
  

  <h2 class="todo-list-header" tabindex="-1">To Do</h2>
  <ul class="right-side-list to-do-list">
      <li class="todo" style="">
        <a class="item" href="/courses/1238555/assignments/4556610#submit" data-track-category="dashboard" data-track-label="todo needs submitting">
          <i class="icon-assignment" aria-label="Assignment"></i>
          <div class="todo-details">
            <b class="todo-details__title">Turn in Lab 3</b>
              <p class="todo-details__context">
                FA17: CMPE-110 Sec 06 - Electronics
              </p>
            <p>
                10 points
                •
              Oct 25 at 11:59pm
            </p>
          </div>
        </a>
        
<button type="button" class="Button Button--icon-action disable_item_link disable-todo-item-link" title="Ignore this assignment" href="#" data-api-href="https://sjsu.instructure.com/api/v1/users/self/todo/assignment_4556610/submitting?permanent=1" data-flash-message="">
  <i class="icon-x"></i>
  <span class="screenreader-only">Ignore Lab 3</span>
</button>

      </li>
  </ul>


<div class="events_list coming_up">
  <h2><a class="event-list-view-calendar icon-calendar-day standalone-icon" href="https://sjsu.instructure.com/calendar">View Calendar</a> Coming Up</h2>
  <ul class="right-side-list events">
      
<li style="" class="event">


  <a data-track-category="dashboard" data-track-label="recent event" href="/courses/1238555/assignments/4556610">
    <i class="icon-assignment" aria-label="Assignment"></i>
    <div class="event-details">
      <b class="event-details__title">Lab 3</b>
        <p>FA17: CMPE-110 Sec 06 - Electronics</p>
      <p>
            10 points
            •
          Oct 25 at 11:59pm
      </p>
    </div>
  </a>


</li>

  </ul>
</div>


<div class="events_list recent_feedback">
  <h2> Recent Feedback</h2>
  <ul class="right-side-list events">
      
<li style="" class="event">


  <a data-track-category="dashboard" data-track-label="recent feedback" class="recent_feedback_icon" href="/courses/1243231/assignments/4558178/submissions/4150924">
    <i class="icon-check"></i>
    <div class="event-details">
      <b class="event-details__title recent_feedback_title">
        Lab 6 Part 1 Logic Works
      </b>
        <p class="event-details__context">
          FA17: CMPE-124 Sec 07 - Digital Design I
        </p>
        <p><strong>4 out of 4</strong></p>
    </div>
    <div class="clear"></div>
  </a>
  <div class="clear"></div>


</li>

      
<li style="" class="event">


  <a data-track-category="dashboard" data-track-label="recent feedback" class="recent_feedback_icon" href="/courses/1243231/assignments/4555825/submissions/4150924">
    <i class="icon-check"></i>
    <div class="event-details">
      <b class="event-details__title recent_feedback_title">
        Quiz 2
      </b>
        <p class="event-details__context">
          FA17: CMPE-124 Sec 07 - Digital Design I
        </p>
        <p><strong>29 out of 25</strong></p>
    </div>
    <div class="clear"></div>
  </a>
  <div class="clear"></div>


</li>

      
<li style="" class="event">


  <a data-track-category="dashboard" data-track-label="recent feedback" class="recent_feedback_icon" href="/courses/1238555/assignments/4550132/submissions/4150924">
    <i class="icon-check"></i>
    <div class="event-details">
      <b class="event-details__title recent_feedback_title">
        Lab 1
      </b>
        <p class="event-details__context">
          FA17: CMPE-110 Sec 06 - Electronics
        </p>
        <p><strong>9 out of 10</strong></p>
    </div>
    <div class="clear"></div>
  </a>
  <div class="clear"></div>


</li>

      
<li style="display: none;" class="event">


  <a data-track-category="dashboard" data-track-label="recent feedback" class="recent_feedback_icon" href="/courses/1243231/assignments/4548592/submissions/4150924">
    <i class="icon-check"></i>
    <div class="event-details">
      <b class="event-details__title recent_feedback_title">
        Exam Prep
      </b>
        <p class="event-details__context">
          FA17: CMPE-124 Sec 07 - Digital Design I
        </p>
        <p><strong>30 out of 30</strong></p>
    </div>
    <div class="clear"></div>
  </a>
  <div class="clear"></div>


</li>

      
<li style="display: none;" class="event">


  <a data-track-category="dashboard" data-track-label="recent feedback" class="recent_feedback_icon" href="/courses/1243231/assignments/4548588/submissions/4150924">
    <i class="icon-check"></i>
    <div class="event-details">
      <b class="event-details__title recent_feedback_title">
        Lab 4 Physical Circuit 2 Demo
      </b>
        <p class="event-details__context">
          FA17: CMPE-124 Sec 07 - Digital Design I
        </p>
        <p><strong>4 out of 4</strong></p>
    </div>
    <div class="clear"></div>
  </a>
  <div class="clear"></div>


</li>

      
<li style="display: none;" class="event">


  <a data-track-category="dashboard" data-track-label="recent feedback" class="recent_feedback_icon" href="/courses/1243231/assignments/4548587/submissions/4150924">
    <i class="icon-check"></i>
    <div class="event-details">
      <b class="event-details__title recent_feedback_title">
        Lab 4 Logicworks Circuit 2 Demo
      </b>
        <p class="event-details__context">
          FA17: CMPE-124 Sec 07 - Digital Design I
        </p>
        <p><strong>4 out of 4</strong></p>
    </div>
    <div class="clear"></div>
  </a>
  <div class="clear"></div>


</li>

      
<li style="display: none;" class="event">


  <a data-track-category="dashboard" data-track-label="recent feedback" class="recent_feedback_icon" href="/courses/1243231/assignments/4548586/submissions/4150924">
    <i class="icon-check"></i>
    <div class="event-details">
      <b class="event-details__title recent_feedback_title">
        Lab 4 Physical Circuit 1 Demo
      </b>
        <p class="event-details__context">
          FA17: CMPE-124 Sec 07 - Digital Design I
        </p>
        <p><strong>4 out of 4</strong></p>
    </div>
    <div class="clear"></div>
  </a>
  <div class="clear"></div>


</li>

      
<li style="display: none;" class="event">


  <a data-track-category="dashboard" data-track-label="recent feedback" class="recent_feedback_icon" href="/courses/1243231/assignments/4548585/submissions/4150924">
    <i class="icon-check"></i>
    <div class="event-details">
      <b class="event-details__title recent_feedback_title">
        Lab 4 Logicworks Circuit 1 Demo
      </b>
        <p class="event-details__context">
          FA17: CMPE-124 Sec 07 - Digital Design I
        </p>
        <p><strong>4 out of 4</strong></p>
    </div>
    <div class="clear"></div>
  </a>
  <div class="clear"></div>


</li>

      
<li style="display: none;" class="event">


  <a data-track-category="dashboard" data-track-label="recent feedback" class="recent_feedback_icon" href="/courses/1243231/assignments/4545746/submissions/4150924">
    <i class="icon-check"></i>
    <div class="event-details">
      <b class="event-details__title recent_feedback_title">
        Lab 1 Report
      </b>
        <p class="event-details__context">
          FA17: CMPE-124 Sec 07 - Digital Design I
        </p>
        <p><strong>18 out of 20</strong></p>
    </div>
    <div class="clear"></div>
  </a>
  <div class="clear"></div>


</li>

      
<li style="display: none;" class="event">


  <a data-track-category="dashboard" data-track-label="recent feedback" class="recent_feedback_icon" href="/courses/1240227/assignments/4483934/submissions/4150924">
    <i class="icon-check"></i>
    <div class="event-details">
      <b class="event-details__title recent_feedback_title">
        SDD
      </b>
        <p class="event-details__context">
          FA17: CMPE-131 Sec 05 - Software Engr I
        </p>
        <p><strong>4.75 out of 5</strong></p>
    </div>
    <div class="clear"></div>
  </a>
  <div class="clear"></div>


</li>

    <li>
      <a href="#" class="more_link">
            7 more in the past two weeks
        …</a>
    </li>
  </ul>
</div>

<div>

  <a href="/grades" class="Button button-sidebar-wide">
  View Grades
  </a>
</div>
</aside>
        </div>
      </div>
    </div>
      
<footer role="contentinfo" id="footer" class="ic-app-footer">
  <a href="http://www.instructure.com" class="footer-logo ic-app-footer__logo-link">
    <span class="screenreader-only">
      By Instructure
    </span>
  </a>
  <div id="footer-links" class="ic-app-footer__links">
    <a href="https://sjsu.instructure.com/privacy_policy">Privacy policy</a>
<a href="https://sjsu.instructure.com/terms_of_use">Terms of service</a>
<a href="http://facebook.com/instructure">Facebook</a>
<a href="http://twitter.com/instructure">Twitter</a>

  </div>
</footer>

  </div>



    <div style="display:none;"><!-- Everything inside of this should always stay hidden -->
        <div id="page_view_id">f97ce94c-b414-4ff7-8db0-de7a44098276</div>
    </div>
    
<div id="cant_record_dialog" style="display: none;">
  <div>
    In order to create video or audio recordings your computer needs to be 
    webcam-enabled.  If you don't have a webcam on your computer, you can still
    record audio-only messages by first installing the Google Video Chat
    plugin.
  </div>
  <div style="text-align: center; font-size: 1.5em; margin: 10px;">
    <a href="http://www.google.com/chat/video" target="_blank" class="btn">Install the Video Plugin</a>
  </div>
  <div class="links" style="text-align: right; font-size: 0.8em; display: none;">
    <a href="#" class="cant_record_link">Don't have a webcam?</a>
  </div>
</div>
  <div id="aria_alerts" class="hide-text affix" role="alert" aria-live="assertive"></div>
  <div id="StudentTray__Container"></div>
  <script>
  INST = {"environment":"production","kalturaSettings":{"domain":"nv.instructuremedia.com","resource_domain":"nv.instructuremedia.com","rtmp_domain":"fms-prod.instructuremedia.com","partner_id":"9","subpartner_id":"0","player_ui_conf":"0","kcw_ui_conf":"0","upload_ui_conf":"0","max_file_size_bytes":534773760,"do_analytics":false,"hide_rte_button":false,"js_uploader":true},"googleAnalyticsAccount":"UA-9138420-1","disableScribdPreviews":true,"logPageViews":true,"maxVisibleEditorButtons":3,"editorButtons":[]};
  ENV = {"ASSET_HOST":"https://du11hjcvx0uqb.cloudfront.net","active_brand_config":"9aa105797e3845a39d5ae6e392e0bfde","active_brand_config_json_url":"https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/9aa105797e3845a39d5ae6e392e0bfde/variables-b59440e479f072e9f8e5fa783f2fcc29.json","url_to_what_gets_loaded_inside_the_tinymce_editor_css":["https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/9aa105797e3845a39d5ae6e392e0bfde/variables-b59440e479f072e9f8e5fa783f2fcc29.css","https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/9aa105797e3845a39d5ae6e392e0bfde/new_styles_normal_contrast/bundles/what_gets_loaded_inside_the_tinymce_editor-4e58055365.css"],"current_user_id":"4150924","current_user":{"id":"4150924","display_name":"Priyank Varshney","avatar_image_url":"https://sjsu.instructure.com/images/thumbnails/46057225/IAkpjG0Ww0SRvImY9le89tGaBRIaOmjpMfdNqn2V","html_url":"https://sjsu.instructure.com/about/4150924"},"current_user_roles":["user","student","teacher"],"current_user_disabled_inbox":false,"files_domain":"cluster12-files.instructure.com","DOMAIN_ROOT_ACCOUNT_ID":120000000089550,"k12":false,"help_link_name":"Help","help_link_icon":"help","use_high_contrast":false,"SETTINGS":{"open_registration":false,"eportfolios_enabled":true,"collapse_global_nav":false,"show_feedback_link":true,"enable_profiles":true},"page_view_update_url":"/page_views/f97ce94c-b414-4ff7-8db0-de7a44098276?page_view_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpIjoiZjk3Y2U5NGMtYjQxNC00ZmY3LThkYjAtZGU3YTQ0MDk4Mjc2IiwidSI6MTIwMDAwMDA0MTUwOTI0LCJjIjoiMjAxNy0xMC0yNFQyMjozNTowMC45N1oifQ.TbBXHXMeD9ddvF7STzn1mlWzh8WaZ5E7iZlbhTgT3Js","context_asset_string":null,"TIMEZONE":"America/Los_Angeles","GRAPHQL_ENABLED":false,"LOCALE":"en","BIGEASY_LOCALE":"en_US","FULLCALENDAR_LOCALE":"en","MOMENT_LOCALE":"en","INCOMPLETE_REGISTRATION":null,"USER_EMAIL":"pvarshney123@gmail.com","DASHBOARD_SIDEBAR_URL":"https://sjsu.instructure.com/dashboard-sidebar","PREFERENCES":{"recent_activity_dashboard":false,"hide_dashcard_color_overlays":null,"custom_colors":{"course_1162924":"#009688","course_1160268":"#09BCD3","course_1164014":"#8F3E97","course_1161092":"#F0592B","course_1184605":"#43A047","course_1183948":"#09BCD3","group_203414":"#F8971C","course_1212081":"#E71F63","course_1212764":"#177B63","course_1209263":"#4D3D4D","course_1208638":"#008400","course_1227414":"#008400","course_1233077":"#177B63","course_1228375":"#D41E00","course_1228918":"#008400","course_1230351":"#3C4F36","course_1230042":"#254284","course_1234696":"#4D3D4D","course_1240227":"#324A4D","course_1241624":"#E1185C","course_1238553":"#008400","course_1239787":"#91349B","course_1245234":"#626E7B","course_1243231":"#008400","course_1238555":"#9F7217"},"show_planner":false},"STUDENT_PLANNER_ENABLED":false,"STUDENT_PLANNER_COURSES":false,"DASHBOARD_COURSES":[{"longName":"FA17: CMPE-110 Sec 04 - Electronics - FA17: CMPE-110 Sec 04 - Electronics","shortName":"FA17: CMPE-110 Sec 04 - Electronics","originalName":"FA17: CMPE-110 Sec 04 - Electronics","courseCode":"FA17: CMPE-110 Sec 04 - Electronics","assetString":"course_1238553","href":"/courses/1238553","term":"Fall 2017","subtitle":"enrolled as: Student","id":"1238553","image":null,"imagesEnabled":false,"rights":{"can_manage":false},"position":null,"links":[{"css_class":"announcements","icon":"icon-announcement","hidden":null,"path":"/courses/1238553/announcements","label":"Announcements"},{"css_class":"discussions","icon":"icon-discussion","hidden":null,"path":"/courses/1238553/discussion_topics","label":"Discussions"},{"css_class":"files","icon":"icon-folder","hidden":null,"path":"/courses/1238553/files","label":"Files"}]},{"longName":"FA17: CMPE-110 Sec 06 - Electronics - FA17: CMPE-110 Sec 06 - Electronics","shortName":"FA17: CMPE-110 Sec 06 - Electronics","originalName":"FA17: CMPE-110 Sec 06 - Electronics","courseCode":"FA17: CMPE-110 Sec 06 - Electronics","assetString":"course_1238555","href":"/courses/1238555","term":"Fall 2017","subtitle":"enrolled as: Student","id":"1238555","image":null,"imagesEnabled":false,"rights":{"can_manage":false},"position":null,"links":[{"css_class":"announcements","icon":"icon-announcement","hidden":null,"path":"/courses/1238555/announcements","label":"Announcements"},{"css_class":"assignments","icon":"icon-assignment","hidden":null,"path":"/courses/1238555/assignments","label":"Assignments"},{"css_class":"discussions","icon":"icon-discussion","hidden":null,"path":"/courses/1238555/discussion_topics","label":"Discussions"}]},{"longName":"FA17: CMPE-124 Sec 05 - Digital Design I - FA17: CMPE-124 Sec 05 - Digital Design I","shortName":"FA17: CMPE-124 Sec 05 - Digital Design I","originalName":"FA17: CMPE-124 Sec 05 - Digital Design I","courseCode":"FA17: CMPE-124 Sec 05 - Digital Design I","assetString":"course_1241624","href":"/courses/1241624","term":"Fall 2017","subtitle":"enrolled as: Student","id":"1241624","image":null,"imagesEnabled":false,"rights":{"can_manage":false},"position":null,"links":[{"css_class":"discussions","icon":"icon-discussion","hidden":null,"path":"/courses/1241624/discussion_topics","label":"Discussions"},{"css_class":"files","icon":"icon-folder","hidden":null,"path":"/courses/1241624/files","label":"Files"}]},{"longName":"FA17: CMPE-124 Sec 07 - Digital Design I - FA17: CMPE-124 Sec 07 - Digital Design I","shortName":"FA17: CMPE-124 Sec 07 - Digital Design I","originalName":"FA17: CMPE-124 Sec 07 - Digital Design I","courseCode":"FA17: CMPE-124 Sec 07 - Digital Design I","assetString":"course_1243231","href":"/courses/1243231","term":"Fall 2017","subtitle":"enrolled as: Student","id":"1243231","image":null,"imagesEnabled":false,"rights":{"can_manage":false},"position":null,"links":[{"css_class":"announcements","icon":"icon-announcement","hidden":null,"path":"/courses/1243231/announcements","label":"Announcements"},{"css_class":"assignments","icon":"icon-assignment","hidden":null,"path":"/courses/1243231/assignments","label":"Assignments"},{"css_class":"files","icon":"icon-folder","hidden":null,"path":"/courses/1243231/files","label":"Files"}]},{"longName":"FA17: CMPE-131 Sec 05 - Software Engr I - FA17: CMPE-131 Sec 05 - Software Engr I","shortName":"FA17: CMPE-131 Sec 05 - Software Engr I","originalName":"FA17: CMPE-131 Sec 05 - Software Engr I","courseCode":"FA17: CMPE-131 Sec 05 - Software Engr I","assetString":"course_1240227","href":"/courses/1240227","term":"Fall 2017","subtitle":"enrolled as: Student","id":"1240227","image":null,"imagesEnabled":false,"rights":{"can_manage":false},"position":null,"links":[{"css_class":"announcements","icon":"icon-announcement","hidden":null,"path":"/courses/1240227/announcements","label":"Announcements"},{"css_class":"assignments","icon":"icon-assignment","hidden":null,"path":"/courses/1240227/assignments","label":"Assignments"},{"css_class":"discussions","icon":"icon-discussion","hidden":null,"path":"/courses/1240227/discussion_topics","label":"Discussions"},{"css_class":"files","icon":"icon-folder","hidden":null,"path":"/courses/1240227/files","label":"Files"}]},{"longName":"FA17: ENGR-100W Sec 43 - Engr Reports - FA17: ENGR-100W Sec 43 - Engr Reports","shortName":"FA17: ENGR-100W Sec 43 - Engr Reports","originalName":"FA17: ENGR-100W Sec 43 - Engr Reports","courseCode":"FA17: ENGR-100W Sec 43 - Engr Reports","assetString":"course_1245234","href":"/courses/1245234","term":"Fall 2017","subtitle":"enrolled as: Student","id":"1245234","image":null,"imagesEnabled":false,"rights":{"can_manage":false},"position":null,"links":[{"css_class":"assignments","icon":"icon-assignment","hidden":null,"path":"/courses/1245234/assignments","label":"Assignments"},{"css_class":"discussions","icon":"icon-discussion","hidden":null,"path":"/courses/1245234/discussion_topics","label":"Discussions"},{"css_class":"files","icon":"icon-folder","hidden":null,"path":"/courses/1245234/files","label":"Files"}]},{"longName":"FA17: ISE-130 Sec 01 - Engr Statistics - FA17: ISE-130 Sec 01 - Engr Statistics","shortName":"FA17: ISE-130 Sec 01 - Engr Statistics","originalName":"FA17: ISE-130 Sec 01 - Engr Statistics","courseCode":"FA17: ISE-130 Sec 01 - Engr Statistics","assetString":"course_1239787","href":"/courses/1239787","term":"Fall 2017","subtitle":"enrolled as: Student","id":"1239787","image":null,"imagesEnabled":false,"rights":{"can_manage":false},"position":null,"links":[{"css_class":"announcements","icon":"icon-announcement","hidden":null,"path":"/courses/1239787/announcements","label":"Announcements"},{"css_class":"assignments","icon":"icon-assignment","hidden":null,"path":"/courses/1239787/assignments","label":"Assignments"},{"css_class":"discussions","icon":"icon-discussion","hidden":null,"path":"/courses/1239787/discussion_topics","label":"Discussions"}]}],"DASHBOARD_REORDERING_ENABLED":false,"notices":[]};
</script>

<script src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/navigation_header.bundle-615775f5bd.js" defer="defer"></script>
<script src="https://instructure-uploads.s3.amazonaws.com/account_120000000089550/attachments/44214137/libraryIcon-2.js?AWSAccessKeyId=AKIAJFNFXH2V2O7RPCAA&amp;Expires=1937956047&amp;Signature=j8vGlo0gjUs%2FR48d7LpO2Hzcmmk%3D&amp;response-cache-control=Cache-Control%3Amax-age%3D473364000.0%2C%20public&amp;response-expires=473364000.0" defer="defer"></script>

</div> <!-- #application -->


<div class="ReactTrayPortal"><div data-reactid=".3"></div></div></body></html>'''

# api info website for Canvas https://canvas.instructure.com/courses/785215
# api documentation for Canvas https://canvas.instructure.com/doc/api/index.html
# general format for requesting url: https://canvas.instructure.com/api/v1/ + path
# example: https://canvas.instructure.com/api/v1/courses?include[]=total_scores  for the request for user's grades

def Authorization():
    	global access_token

def login(): 
	return True

def post_message_data(data):
	messages_url = 'https://api.ciscospark.com/v1/messages'
	sendSparkPOST(messages_url, data)

def sendSparkPOST(url, data):
	"""
	This method is used for:
	    -posting a message to the Spark room to confirm that a command was received and processed
	"""

	# need to make sure that data is no longer than the spark POST limit
	# of 7439 characters (before encryption).

	if data:
	    if data.get("markdown") and len(data.get("markdown")) > 7400:
	        data["markdown"] = ( data.get("markdown")[:7400] + "...[truncated]" )

	    if data.get("text") and len(data.get("text")) > 7400:
	        data["text"] = ( data.get("text")[:7400] + "...[truncated]" )

	request = urllib2.Request(url, json.dumps(data),
	                        headers={"Accept" : "application/json",
	                                 "Content-Type":"application/json"})
	request.add_header("Authorization", "Bearer "+ "ZDhiZjdlZjUtYmRlNy00OGEzLWE1YWMtNjdiNTUyMTgzZmViMTZhYTQzZWEtZTky")
	contents = urllib2.urlopen(request).read()
	return contents

def get_announcement():
	url = 'https://canvas.instructure.com/api/v1//api/v1/announcements'

	params = {
		'context_codes':'',
		'start_date':'',
		'end_date':'',
		'active_only':''}

	r = requests.get(url, params,headers = {"Authorization":access_token} )
	data = json.loads(r.text)
	title = data['title'], message = data['message']
	output = 'reply message'

def get_classes():

	print("IN GET CLASS FUNCTION")
	course_ids = []
	classes = []
	url = 'https://sjsu.instructure.com/'

	content = urllib.request.urlopen(url).read()
	soup=BeautifulSoup(html_home,'html.parser')
	tag=soup.body.find(class_="ic-NavMenu-list-item__link")
	print(tag.string)
	for string in tag.string:
	    print(string)
	    msg = "Classes: "
	    msg+= string
	    post_message_data( { "roomId": roomid, "markdown": msg } )

	
	classes_data = {'classes':classes, 'course id': course_ids}

	


	#return classes_data
	return tag


def get_grades():

    classes_data = get_classes() # gets a dict of class data from get_classes()
    ids = classes_data['course id'] # the ids of the classes as a list
    courses = classes_data['classes'] # the class names in a list
    class_and_grade={} # an empty dict for class:grade pairs
    
    for i, cid in enumerate(ids):
        grade_url = 'https://sjsu.instructure.com/courses/%s/grades' % ids[i]
        content = urllib.request.urlopen(grade_url).read()
        soup=BeautifulSoup(content,'html.parser')
        tag=soup.body.find(class_="student_assignment final_grade")
        grade=""
        for string in tag.stripped_strings:
            grade+=(repr(string))
        grade=grade[9]+grade[10]+'%' #orig str is 'total:__%', this returns __%
        class_and_grade[courses[i]]=grade #adds a class:grade pair

	msg = class_and_grade
	post_message_data( { "roomId": roomid, "markdown": msg } )


    return class_and_grade # returns a dict of class:grade pairs

@post('/')
def index(request):
	r = json.loads(request.body)
	if not r:
	    return "True"

	pprint.pprint(r)

	roomid = r['originalRequest']['data']['data']['roomId']
	print roomid

	action = r['result']['action']

	if action == 'get_grades':
		get_grades()

	if action == 'get_classes':
		get_classes()

	if action == 'get_announcement':
		get_announcement()

	return True


if __name__ == "__main__":

	run_itty(server='wsgiref', host='0.0.0.0', port=8080)
