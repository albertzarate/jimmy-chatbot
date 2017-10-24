#!/usr/bin/env python
from itty import *
import json
import pprint
import jimmy
import requests
from bs4 import BeautifulSoup
import urllib.request


# api info website for Canvas https://canvas.instructure.com/courses/785215
# api documentation for Canvas https://canvas.instructure.com/doc/api/index.html
# general format for requesting url: https://canvas.instructure.com/api/v1/ + path
# example: https://canvas.instructure.com/api/v1/courses?include[]=total_scores  for the request for user's grades

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


def Authorization():
    	global access_token

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

	course_ids = []
	classes = []

	classes_data = {'classes':classes, 'course id': course_ids}


	return classes_data



def get_grades():

	classes_data = get_classes() # gets a dict of class data from get_classes()

	ids = classes_data['course id'] # the ids of the classes as a list

    courses = classes_data['classes'] # the class names in a list

    class_and_grade={} # an empty dict for class:grade pairs

	content="""
    <html class="lato-font-loaded" lang="en"><head>
  <meta charset="utf-8">
  <title>Grades for Albert Zarate: FA17: CMPE-130 Sec 02 - Adv Alg Des</title>
  <!--[if lte IE 9]> <meta http-equiv=refresh content="0; URL=/ie-9-is-not-supported.html" /> <![endif]-->
  <link rel="shortcut icon" type="image/x-icon" href="https://du11hjcvx0uqb.cloudfront.net/dist/images/favicon-e10d657a73.ico">
  <link rel="apple-touch-icon" href="https://du11hjcvx0uqb.cloudfront.net/dist/images/apple-touch-icon-585e5d997d.png">

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
</script><style type="text/css">
:root #content > #right > .dose > .dosesingle,
:root #content > #center > .dose > .dosesingle,
:root #header + #content > #left > #rlblock_left
{ display: none !important; }</style>
  <script src="https://du11hjcvx0uqb.cloudfront.net/dist/lato-fontfaceobserver-11a14bc0b6.js" async="async"></script>

  <meta name="apple-itunes-app" content="app-id=480883488">
<link rel="manifest" href="/web-app-manifest/manifest.json">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0055a2">
  <link rel="stylesheet" media="all" href="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/9aa105797e3845a39d5ae6e392e0bfde/new_styles_normal_contrast/bundles/grade_summary-030eb4696b.css">


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
<script src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/grade_summary.bundle-3b38e53a17.js" defer="defer"></script>
<script src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/rubric_assessment.bundle-e607d1341e.js" defer="defer"></script>
<script src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/legacy/gradebooks_grade_summary.bundle-d4e55b5251.js" defer="defer"></script>
<style type="text/css"></style><script type="text/javascript" charset="utf-8" async="" src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/14.chunk-ad84753a36.js"></script><link rel="stylesheet" href="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/9aa105797e3845a39d5ae6e392e0bfde/new_styles_normal_contrast/jst/outcomes/outcomePopover-d830f91dc6.css" data-loaded-by-brandablecss="true"></head>

<body class="with-left-side course-menu-expanded with-right-side grades primary-nav-expanded context-course_1244662 webkit chrome touch vsc-initialized">

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
            <li class="menu-item ic-app-header__menu-list-item">
              <a id="global_nav_profile_link" href="/profile" class="ic-app-header__menu-list-link">
                <div class="menu-item-icon-container" aria-hidden="true">
                  <div class="ic-avatar ">
                    <img src="https://sjsu.instructure.com/images/thumbnails/46797560/MQWOSey0GuwJiMpva6T5BGufmMSkivRXTw1rwTro" alt="Albert Zarate">
                  </div>
                </div>
                <div class="menu-item__text">
                  Account
                </div>
              </a>
            </li>
          <li class="ic-app-header__menu-list-item ">
            <a id="global_nav_dashboard_link" href="https://sjsu.instructure.com/" class="ic-app-header__menu-list-link">
              <div class="menu-item-icon-container" aria-hidden="true">
                  <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--dashboard" version="1.1" x="0" y="0" viewBox="0 0 280 200" enable-background="new 0 0 280 200" xml:space="preserve"><path d="M273.09,180.75H197.47V164.47h62.62A122.16,122.16,0,1,0,17.85,142a124,124,0,0,0,2,22.51H90.18v16.29H6.89l-1.5-6.22A138.51,138.51,0,0,1,1.57,142C1.57,65.64,63.67,3.53,140,3.53S278.43,65.64,278.43,142a137.67,137.67,0,0,1-3.84,32.57ZM66.49,87.63,50.24,71.38,61.75,59.86,78,76.12Zm147,0L202,76.12l16.25-16.25,11.51,11.51ZM131.85,53.82v-23h16.29v23Zm15.63,142.3a31.71,31.71,0,0,1-28-16.81c-6.4-12.08-15.73-72.29-17.54-84.25a8.15,8.15,0,0,1,13.58-7.2c8.88,8.21,53.48,49.72,59.88,61.81a31.61,31.61,0,0,1-27.9,46.45ZM121.81,116.2c4.17,24.56,9.23,50.21,12,55.49A15.35,15.35,0,1,0,161,157.3C158.18,152,139.79,133.44,121.81,116.2Z"></path></svg>

              </div>
              <div class="menu-item__text">Dashboard</div>
            </a>
          </li>
          <li class="menu-item ic-app-header__menu-list-item ic-app-header__menu-list-item--active">
            <a id="global_nav_courses_link" href="/courses" class="ic-app-header__menu-list-link">
              <div class="menu-item-icon-container" aria-hidden="true">
                <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--courses" version="1.1" x="0" y="0" viewBox="0 0 280 259" enable-background="new 0 0 280 259" xml:space="preserve"><path d="M73.31,198c-11.93,0-22.22,8-24,18.73a26.67,26.67,0,0,0-.3,3.63v.3a22,22,0,0,0,5.44,14.65,22.47,22.47,0,0,0,17.22,8H200V228.19h-134V213.08H200V198Zm21-105.74h90.64V62H94.3ZM79.19,107.34V46.92H200v60.42Zm7.55,30.21V122.45H192.49v15.11ZM71.65,16.71A22.72,22.72,0,0,0,49,39.36V190.88a41.12,41.12,0,0,1,24.32-8h157V16.71ZM33.88,39.36A37.78,37.78,0,0,1,71.65,1.6H245.36V198H215.15v45.32h22.66V258.4H71.65a37.85,37.85,0,0,1-37.76-37.76Z"></path></svg>

              </div>
              <div class="menu-item__text">
                Courses
              </div>
            </a>
          </li>
            <li class="menu-item ic-app-header__menu-list-item">
              <a id="global_nav_groups_link" href="/groups" class="ic-app-header__menu-list-link">
                <div class="menu-item-icon-container" aria-hidden="true">
                  <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--groups" viewBox="0 0 200 135"><path d="M134.5 129.4c0-1.1 0-19.8-6.2-31.1-4.5-8.5-16.4-12.4-35-19.2-1.7-.6-3.4-1.1-5.1-1.7v-8.5c5.6-5.1 8.5-12.4 8.5-20.3V29.4C96.6 13 83.6 0 67.2 0S37.9 13 37.9 29.4v19.2c0 7.3 3.4 14.7 8.5 20.3v8.5c-1.7.6-3.4 1.1-5.1 1.7-18.6 6.2-30.5 10.7-35 19.2C0 109.6 0 128.8 0 129.4c0 3.4 2.3 5.6 5.6 5.6h123.7c3.5 0 5.7-2.3 5.2-5.6zm-123.2-5.7c.6-5.6 1.7-14.7 3.4-19.8C17 98.8 30 94.3 43.5 89.8c2.8-1.1 5.6-2.3 9-3.4 2.3-.6 4-2.8 4-5.1V66.7c0-1.7-.6-3.4-1.7-4.5-4-3.4-6.2-8.5-6.2-13.6V29.4c0-10.2 7.9-18.1 18.1-18.1s18.1 7.9 18.1 18.1v19.2c0 5.1-2.3 10.2-6.2 13.6-1.1 1.1-1.7 2.8-1.7 4.5v14.7c0 2.3 1.7 4.5 4 5.1 2.8 1.1 6.2 2.3 9 3.4 13.6 5.1 26.6 9.6 28.8 14.1 2.8 5.1 4 13.6 4.5 19.8H11.3zM196 79.1c-2.8-6.2-11.3-9.6-22.6-13.6l-1.7-.6v-3.4c4.5-4 6.8-9.6 6.8-15.8V35c0-12.4-9.6-22-22-22s-22 10.2-22 22v10.7c0 6.2 2.3 11.9 6.8 15.8V65l-1.7.6c-7.3 2.8-13 4.5-16.9 7.3-1.7 1.1-2.3 2.8-2.3 5.1.6 1.7 1.7 3.4 3.4 4.5 7.9 4 12.4 7.3 14.1 10.7 2.3 4.5 4 10.2 5.1 18.1.6 2.3 2.8 4.5 5.6 4.5h45.8c3.4 0 5.6-2.8 5.6-5.1 0-3.9 0-24.3-4-31.6zm-42.9 25.4c-1.1-6.8-2.8-12.4-5.1-16.9-1.7-4-5.1-6.8-9.6-10.2 1.7-1.1 3.4-1.7 5.1-2.3l5.6-2.3c1.7-.6 3.4-2.8 3.4-5.1v-9.6c0-1.7-.6-3.4-2.3-4.5-2.8-1.7-4.5-5.1-4.5-8.5V34.5c0-6.2 4.5-10.7 10.7-10.7s10.7 5.1 10.7 10.7v10.7c0 3.4-1.7 6.2-4.5 8.5-1.1 1.1-2.3 2.8-2.3 4.5v10.2c0 2.3 1.1 4.5 3.4 5.1l5.6 2.3c6.8 2.3 15.3 5.6 16.4 7.9 1.7 2.8 2.8 12.4 2.8 20.9h-35.4z"></path></svg>

                </div>
                <div class="menu-item__text">
                  Groups
                </div>
              </a>
            </li>
          <li class="menu-item ic-app-header__menu-list-item">
            <a id="global_nav_calendar_link" href="/calendar" class="ic-app-header__menu-list-link">
              <div class="menu-item-icon-container" aria-hidden="true">
                <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--calendar" version="1.1" x="0" y="0" viewBox="0 0 280 280" enable-background="new 0 0 280 280" xml:space="preserve"><path d="M197.07,213.38h16.31V197.07H197.07Zm-16.31,16.31V180.76h48.92v48.92Zm-48.92-16.31h16.31V197.07H131.85Zm-16.31,16.31V180.76h48.92v48.92ZM66.62,213.38H82.93V197.07H66.62ZM50.32,229.68V180.76H99.24v48.92Zm146.75-81.53h16.31V131.85H197.07Zm-16.31,16.31V115.54h48.92v48.92Zm-48.92-16.31h16.31V131.85H131.85Zm-16.31,16.31V115.54h48.92v48.92ZM66.62,148.15H82.93V131.85H66.62ZM50.32,164.46V115.54H99.24v48.92ZM34,262.29H246V82.93H34ZM246,66.62V42.16A8.17,8.17,0,0,0,237.84,34H213.38v8.15a8.15,8.15,0,1,1-16.31,0V34H82.93v8.15a8.15,8.15,0,0,1-16.31,0V34H42.16A8.17,8.17,0,0,0,34,42.16V66.62Zm-8.15-48.92a24.49,24.49,0,0,1,24.46,24.46V278.6H17.71V42.16A24.49,24.49,0,0,1,42.16,17.71H66.62V9.55a8.15,8.15,0,0,1,16.31,0v8.15H197.07V9.55a8.15,8.15,0,1,1,16.31,0v8.15Z"></path></svg>

              </div>
              <div class="menu-item__text">
                Calendar
              </div>
            </a>
          </li>
          <li class="menu-item ic-app-header__menu-list-item">
            <a id="global_nav_conversations_link" href="/conversations" class="ic-app-header__menu-list-link">
              <div class="menu-item-icon-container" aria-hidden="true">
                <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--inbox" version="1.1" x="0" y="0" viewBox="0 0 280 280" enable-background="new 0 0 280 280" xml:space="preserve"><path d="M91.72,120.75h96.56V104.65H91.72Zm0,48.28h80.47V152.94H91.72Zm0-96.56h80.47V56.37H91.72Zm160.94,34.88H228.52V10.78h-177v96.56H27.34A24.17,24.17,0,0,0,3.2,131.48V244.14a24.17,24.17,0,0,0,24.14,24.14H252.66a24.17,24.17,0,0,0,24.14-24.14V131.48A24.17,24.17,0,0,0,252.66,107.34Zm0,16.09a8.06,8.06,0,0,1,8,8v51.77l-32.19,19.31V123.44ZM67.58,203.91v-177H212.42v177ZM27.34,123.44H51.48v79.13L19.29,183.26V131.48A8.06,8.06,0,0,1,27.34,123.44ZM252.66,252.19H27.34a8.06,8.06,0,0,1-8-8V202l30,18H230.75l30-18v42.12A8.06,8.06,0,0,1,252.66,252.19Z"></path></svg>

                <span class="menu-item__badge" style="">30</span>
              </div>
              <div class="menu-item__text">
                Inbox
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
        <li class="menu-item ic-app-header__menu-list-item"><a id="global_nav_library_link" target="_blank" href="https://library.sjsu.edu" class="ic-app-header__menu-list-link"><div class="menu-item-icon-container" aria-hidden="true"><svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="45px" height="30px" x="0px" y="0px" viewBox="179.2 189.3 389.4 358.5" enable-background="new 179.2 189.3 389.4 358.5" xml:space="preserve"><path fill="#FFFFFF" d="M247.4,189.3c81.6,19.2,118.7,81.2,118.7,81.2v277.2c-41.7-59.9-118.7-84.3-118.7-84.3V461C247.4,461,247.5,189,247.4,189.3z"></path><path fill="#FFFFFF" d="M260.1,530.2c0,0-34.6-17.5-80.8-10.3V247.6h11.4v258.8C190.6,506.2,240.4,505.7,260.1,530.2z"></path><path fill="#FFFFFF" d="M306.8,521.3L306.8,521.3c-18-25.7-75-45.7-75-45.7V219.9l-23.6-9.2V489c0,0,24.3,3,36.4,6.4C286.5,507.2,306.8,521.3,306.8,521.3z"></path><path fill="#FFFFFF" d="M500.5,189.3c-81,25.2-118.7,81.2-118.7,81.2v277.2c41.7-59.9,118.7-84.3,118.7-84.3S500.5,190,500.5,189.3z"></path><path fill="#FFFFFF" d="M487.9,530.2c0,0,34.6-17.5,80.8-10.3V247.6h-11.4v258.8C557.3,506.2,507.6,505.7,487.9,530.2z"></path><path fill="#FFFFFF" d="M441.1,521.3L441.1,521.3c18-25.7,75-45.7,75-45.7V219.9l23.6-9.2V489c0,0-24.3,3-36.4,6.4C461.4,507.2,441.1,521.3,441.1,521.3z"></path></svg></div><div class="menu-item__text">Library</div></a></li></ul>
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
    <div id="global_nav_tray_container"><noscript data-reactid=".0"></noscript></div>
  </header>


  <div id="instructure_ajax_error_box">
    <div style="text-align: right; background-color: #fff;"><a href="#" class="close_instructure_ajax_error_box_link">Close</a></div>
    <iframe id="instructure_ajax_error_result" src="about:blank" style="border: 0;" title="Error"></iframe>
  </div>



  <div id="wrapper" class="ic-Layout-wrapper">
      <div class="ic-app-nav-toggle-and-crumbs no-print">
          <button type="button" id="courseMenuToggle" class="Button Button--link ic-app-course-nav-toggle" aria-live="polite" aria-label="Hide Courses Navigation Menu" title="Hide Courses Navigation Menu">
            <i class="icon-hamburger" aria-hidden="true"></i>
          </button>
          <div class="ic-app-crumbs">
        <nav id="breadcrumbs" role="navigation" aria-label="breadcrumbs"><ul><li class="home"><a href="/"><span class="ellipsible">      <i class="icon-home" title="My Dashboard">
        <span class="screenreader-only">My Dashboard</span>
      </i>
</span></a></li><li><a href="/courses/1244662"><span class="ellipsible">FA17: CMPE-130 Sec 02 - Adv Alg Des</span></a></li><li><a href="/courses/1244662/grades"><span class="ellipsible">Grades</span></a></li><li><a href="/courses/1244662/grades/4152168"><span class="ellipsible">Albert Zarate</span></a></li></ul></nav>
        </div>
      </div>
    <div id="main" class="ic-Layout-columns">
        <div class="ic-Layout-watermark"></div>
        <div id="left-side" class="ic-app-course-menu list-view" style="display: block">
              <span id="section-tabs-header-subtitle" class="ellipsis">Fall 2017</span>
            <nav role="navigation" aria-label="Courses Navigation Menu"><ul id="section-tabs"><li class="section"><a href="/courses/1244662" title="Home" class="home" tabindex="0">Home</a></li><li class="section"><a href="/courses/1244662/announcements" title="Announcements" class="announcements" tabindex="0">Announcements</a></li><li class="section"><a href="/courses/1244662/assignments" title="Assignments" class="assignments" tabindex="0">Assignments</a></li><li class="section"><a href="/courses/1244662/discussion_topics" title="Discussions" class="discussions" tabindex="0">Discussions</a></li><li class="section"><a href="/courses/1244662/grades" title="Grades" class="grades active" tabindex="0">Grades</a></li><li class="section"><a href="/courses/1244662/users" title="People" class="people" tabindex="0">People</a></li><li class="section"><a href="/courses/1244662/files" title="Files" class="files" tabindex="0">Files</a></li><li class="section"><a href="/courses/1244662/assignments/syllabus" title="Syllabus" class="syllabus" tabindex="0">Syllabus</a></li><li class="section"><a href="/courses/1244662/quizzes" title="Quizzes" class="quizzes" tabindex="0">Quizzes</a></li><li class="section"><a href="/courses/1244662/modules" title="Modules" class="modules" tabindex="0">Modules</a></li><li class="section"><a href="/courses/1244662/conferences" title="Conferences" class="conferences" tabindex="0">Conferences</a></li><li class="section"><a href="/courses/1244662/collaborations" title="Collaborations" class="collaborations" tabindex="0">Collaborations</a></li><li class="section"><a href="/courses/1244662/external_tools/12165" title="Chat" class="context_external_tool_12165" tabindex="0">Chat</a></li><li class="section"><a href="/courses/1244662/external_tools/12285" title="Blackboard Collaborate" class="context_external_tool_12285" tabindex="0">Blackboard Collaborate</a></li><li class="section"><a href="/courses/1244662/external_tools/15990" title="Criterion" class="context_external_tool_15990" tabindex="0">Criterion</a></li><li class="section"><a href="/courses/1244662/external_tools/24799" title="Writer's Help" class="context_external_tool_24799" tabindex="0">Writer's Help</a></li><li class="section"><a href="/courses/1244662/external_tools/29705" title="+WebEx" class="context_external_tool_29705" tabindex="0">+WebEx</a></li><li class="section"><a href="/courses/1244662/external_tools/38568" title="Portfolium" class="context_external_tool_38568" tabindex="0">Portfolium</a></li></ul></nav>
        </div>
      <div id="not_right_side" class="ic-app-main-content">
        <div id="content-wrapper" class="ic-Layout-contentWrapper">


          <div id="content" class="ic-Layout-contentMain" role="main">


<h1 class="screenreader-only">Grades for Albert Zarate</h1>


<div id="print-grades-container" class="grid-row middle-xs between-xs">
  <div class="col-xs-6">
  </div>

  <div id="print-grades-button-container" class="col-md-6 col-lg-3">
    <a id="print-grades-button" class="btn print-grades icon-printer" href="javascript:window.print()">
      Print grades
    </a>
  </div>
</div>

<h2>
Grades for    Albert Zarate
</h2>

<div class="dropdowns">
    <div id="course-selector-dropdown" style="margin-left: 10px; float: left;" class="course_selector">
    <label for="course_url">For the course</label>
    <select id="course_url">
        <option value="/courses/1209263/grades">FA16: MATH-123 Sec 01 - Diff Eq and Linear Alg</option>
        <option value="/courses/1238553/grades">FA17: CMPE-110 Sec 04 - Electronics</option>
        <option value="/courses/1238555/grades">FA17: CMPE-110 Sec 06 - Electronics</option>
        <option value="/courses/1240227/grades">FA17: CMPE-131 Sec 05 - Software Engr I</option>
        <option value="/courses/1241624/grades">FA17: CMPE-124 Sec 05 - Digital Design I</option>
        <option value="/courses/1243231/grades">FA17: CMPE-124 Sec 07 - Digital Design I</option>
        <option value="/courses/1244662/grades" selected="">FA17: CMPE-130 Sec 02 - Adv Alg Des</option>
        <option value="/courses/1245234/grades">FA17: ENGR-100W Sec 43 - Engr Reports</option>
    </select>
    </div>

  <div class="assignment_order" style="margin-right:10px;float:right;">
    <form style="margin-bottom: 0;" action="/courses/1244662/save_assignment_order" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="2tjdLKnyMBTxOIR9+vbO0ZD7Ef3K46YJZw6+WllHvC+blqxPmr9fZbJN10S2hI25+MlXpaXankU2fvUSFQrOdg==">
      <label for="assignment_order">Arrange by</label>
      <select name="assignment_order" id="assignment_order"><option value="assignment_group">Assignment Group</option>
<option selected="selected" value="due_at">Due Date</option>
<option value="module">Module</option>
<option value="title">Title</option></select>
</form>  </div>
</div>


<div id="assignments">
  <span id="aria-announcer" class="hide-text affix" aria-live="polite" aria-relevant="additions"></span>
<table style="width: 100%;" id="grades_summary" class="editable">
    <caption class="screenreader-only">You can view your grades based on What-If scores so that you know how grades will be affected by upcoming or resubmitted assignments. You can test scores for an assignment that already includes a score, or an assignment that has yet to be graded.</caption>
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Due</th>


      <th scope="col" class="assignment_score">Score</th>
      <th scope="col" class="possible">Out of</th>
      <th scope="col"><span class="screenreader-only">Details</span></th>
    </tr>
  </thead>
  <tbody><tr class="student_assignment assignment_graded editable" data-muted="false" id="submission_4535420">

      <th class="title" scope="row">
          <a href="/courses/1244662/assignments/4535420/submissions/4152168">In-class-sept-5</a>
          <div class="context">Quizzes and In-class assignments</div>

      </th><td class="due">
          Sep 5 by 11:59pm
      </td>


      <td class="assignment_score" title="Click to test a different score">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade" tabindex="0">
              <span class="tooltip_wrap right" aria-hidden="true">
                  <span class="tooltip_text score_teaser">
                      Click to test a different score
                  </span>
              </span>
                <span class="screenreader-only" role="link">
                  Click to test a different score
                </span>
                10
            </span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">
              10.0
            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">
              10
            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">
              10
            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              graded
            <span class="assignment_group_id">1760781</span>
            <span class="assignment_id">4535420</span>
            <span class="group_weight"></span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">
        10
      </td>
      <td class="details">
        <a href="#" class="toggle_final_grade_info tooltip" aria-label="This assignment does not count toward the final grade." aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">Grade Info</span>
          </span>
          <i class="icon-warning standalone-icon"></i>
        </a>
        <a href="#" class="toggle_comments_link tooltip" aria-label="Read comments" aria-describedby="comment_count_for_assignment_4535420" aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text" id="comment_count_for_assignment_4535420">
              0 comments
            </span>
          </span>
          <i class="icon-discussion standalone-icon"></i>
        </a>
        <a href="#" class="toggle_score_details_link tooltip" aria-label="See scoring details" aria-expanded="false" aria-controls="grade_info_4535420">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See scoring details</span>
          </span>
          <i class="icon-check-plus standalone-icon"></i>
        </a>
        <a href="#" class="toggle_rubric_assessments_link tooltip" aria-label="See rubric results" aria-expanded="false" aria-controls="rubric_4535420" tabindex="0" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See rubric results</span>
          </span>
          <i class="icon-rubric"></i>
        </a>
      </td>
    </tr>
    <tr id="final_grade_info_4535420" class="comments assignment_graded" style="display: none;">
    </tr>
    <tr id="grade_info_4535420" class="comments grade_details assignment_graded" style="display: none;">
        <td colspan="6" style="padding-bottom: 20px;">
            <table id="score_details_4535420" class="score_details_table">
              <thead>
                <tr>
                  <th colspan="5">
                    Score Details
                  </th>
                  <th>
                    <a href="#" data-aria="grade_info_4535420" aria-label="Close score details" class="screenreader-toggle pull-right">Close</a>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                    <td>
                      Mean:
                      8.6
                    </td>
                    <td>
                      High:
                      10
                    </td>
                    <td>
                      Low:
                      0
                    </td>
                    <td colspan="3">
                      <div style="cursor: pointer; float: right; height: 30px; margin-left: 20px; width: 160px; position: relative; margin-right: 30px;" aria-hidden="true" title="Mean 8.6, High 10.0, Low 0.0">
                        <div class="grade-summary-graph-component" style="height: 10px; margin: 5px 0px; border-width: 2px; border-right-width: 0;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="width: 0px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 150px; width: 0px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 0px; width: 129px; height: 20px; border-width: 2px; border-top-left-radius: 3px; border-bottom-left-radius: 3px; border-right-width: 0; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 129px; width: 21px; height: 20px; border-width: 2px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 153px; height: 10px; margin: 5px 0px; border-width: 2px; border-left-width: 0;">&nbsp;</div>
                          <div class="grade-summary-graph-component" style="top: 5px; height: 10px; width: 10px; left: 145px; border: 2px solid #248; background: #abd; border-radius: 3px;" title="Your Score:
                            10.0 out of 10">&nbsp;
                          </div>
                      </div>
                    </td>
                </tr>
              </tbody>
            </table>
        </td></tr>
    <tr id="comments_thread_4535420" class="comments comments_thread assignment_graded" style="display: none;">
      <td colspan="6">
      </td>
    </tr>
    <tr id="rubric_4535420" class="rubric_assessments assignment_graded" style="display: none;">
    </tr>
  <tr class="student_assignment assignment_graded editable" data-muted="false" id="submission_4518429">

      <th class="title" scope="row">
          <a href="/courses/1244662/assignments/4518429/submissions/4152168">Academic integrity upload</a>
          <div class="context">Quizzes and In-class assignments</div>

      </th><td class="due">
          Sep 14 by 11:59pm
      </td>


      <td class="assignment_score" title="Click to test a different score">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade" tabindex="0">
              <span class="tooltip_wrap right" aria-hidden="true">
                  <span class="tooltip_text score_teaser">
                      Click to test a different score
                  </span>
              </span>
                <span class="screenreader-only" role="link">
                  Click to test a different score
                </span>
                10
            </span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">
              10.0
            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">
              10
            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">
              10
            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              graded
            <span class="assignment_group_id">1760781</span>
            <span class="assignment_id">4518429</span>
            <span class="group_weight"></span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">
        10
      </td>
      <td class="details">
        <a href="#" class="toggle_final_grade_info tooltip" aria-label="This assignment does not count toward the final grade." aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">Grade Info</span>
          </span>
          <i class="icon-warning standalone-icon"></i>
        </a>
        <a href="#" class="toggle_comments_link tooltip" aria-label="Read comments" aria-describedby="comment_count_for_assignment_4518429" aria-expanded="false" aria-controls="comments_thread_4518429">
          <span class="tooltip_wrap right">
            <span class="tooltip_text" id="comment_count_for_assignment_4518429">
              2 comments
            </span>
          </span>
          <i class="icon-discussion standalone-icon"></i>
        </a>
        <a href="#" class="toggle_score_details_link tooltip" aria-label="See scoring details" aria-expanded="false" aria-controls="grade_info_4518429">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See scoring details</span>
          </span>
          <i class="icon-check-plus standalone-icon"></i>
        </a>
        <a href="#" class="toggle_rubric_assessments_link tooltip" aria-label="See rubric results" aria-expanded="false" aria-controls="rubric_4518429" tabindex="0" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See rubric results</span>
          </span>
          <i class="icon-rubric"></i>
        </a>
      </td>
    </tr>
    <tr id="final_grade_info_4518429" class="comments assignment_graded" style="display: none;">
    </tr>
    <tr id="grade_info_4518429" class="comments grade_details assignment_graded" style="display: none;">
        <td colspan="6" style="padding-bottom: 20px;">
            <table id="score_details_4518429" class="score_details_table">
              <thead>
                <tr>
                  <th colspan="5">
                    Score Details
                  </th>
                  <th>
                    <a href="#" data-aria="grade_info_4518429" aria-label="Close score details" class="screenreader-toggle pull-right">Close</a>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                    <td>
                      Mean:
                      9.7
                    </td>
                    <td>
                      High:
                      10
                    </td>
                    <td>
                      Low:
                      0
                    </td>
                    <td colspan="3">
                      <div style="cursor: pointer; float: right; height: 30px; margin-left: 20px; width: 160px; position: relative; margin-right: 30px;" aria-hidden="true" title="Mean 9.7, High 10.0, Low 0.0">
                        <div class="grade-summary-graph-component" style="height: 10px; margin: 5px 0px; border-width: 2px; border-right-width: 0;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="width: 0px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 150px; width: 0px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 0px; width: 146px; height: 20px; border-width: 2px; border-top-left-radius: 3px; border-bottom-left-radius: 3px; border-right-width: 0; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 146px; width: 5px; height: 20px; border-width: 2px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 153px; height: 10px; margin: 5px 0px; border-width: 2px; border-left-width: 0;">&nbsp;</div>
                          <div class="grade-summary-graph-component" style="top: 5px; height: 10px; width: 10px; left: 145px; border: 2px solid #248; background: #abd; border-radius: 3px;" title="Your Score:
                            10.0 out of 10">&nbsp;
                          </div>
                      </div>
                    </td>
                </tr>
              </tbody>
            </table>
        </td></tr>
    <tr id="comments_thread_4518429" class="comments comments_thread assignment_graded" style="display: none;">
      <td colspan="6">
            <table class="score_details_table">
              <thead>
                <tr>
                  <th>Comments</th>
                  <th>
                    <a href="#" data-aria="comments_thread_4518429" aria-label="Close comments" class="screenreader-toggle pull-right">Close</a>
                  </th>
                </tr>
              </thead>
              <tbody>
                  <tr>
                    <td>
                      <span style="white-space: pre-wrap;">Please sign and submit the document again.</span>
                    <div style="text-align: right; font-size: 0.8em; margin-right: 10px; clear: both;">
                    </div>
                  </td>
                  <td>
                    Harsh Mehta,
                    Sep 26 at  6:25pm
                  </td>
                  </tr><tr>
                    <td>
                      <span style="white-space: pre-wrap;">Sorry for the mistake, here is the updated signed file.</span>
                    <div style="text-align: right; font-size: 0.8em; margin-right: 10px; clear: both;">
                    </div>
                  </td>
                  <td>
                    Albert Zarate,
                    Oct 3 at 10:03am
                  </td>
              </tr>
            </tbody>
          </table>
      </td>
    </tr>
    <tr id="rubric_4518429" class="rubric_assessments assignment_graded" style="display: none;">
    </tr>
  <tr class="student_assignment assignment_graded editable" data-muted="false" id="submission_4543421">

      <th class="title" scope="row">
          <a href="/courses/1244662/assignments/4543421/submissions/4152168">Reading quiz: Quicksort</a>
          <div class="context">Quizzes and In-class assignments</div>

      </th><td class="due">
          Sep 21 by  9am
      </td>


      <td class="assignment_score" title="Click to test a different score">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade" tabindex="0">
              <span class="tooltip_wrap right" aria-hidden="true">
                  <span class="tooltip_text score_teaser">
                      Click to test a different score
                  </span>
              </span>
                <span class="screenreader-only" role="link">
                  Click to test a different score
                </span>
                10
            </span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">
              10.0
            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">
              10
            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">
              10
            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              graded
            <span class="assignment_group_id">1760781</span>
            <span class="assignment_id">4543421</span>
            <span class="group_weight"></span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">
        10
      </td>
      <td class="details">
        <a href="#" class="toggle_final_grade_info tooltip" aria-label="This assignment does not count toward the final grade." aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">Grade Info</span>
          </span>
          <i class="icon-warning standalone-icon"></i>
        </a>
        <a href="#" class="toggle_comments_link tooltip" aria-label="Read comments" aria-describedby="comment_count_for_assignment_4543421" aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text" id="comment_count_for_assignment_4543421">
              0 comments
            </span>
          </span>
          <i class="icon-discussion standalone-icon"></i>
        </a>
        <a href="#" class="toggle_score_details_link tooltip" aria-label="See scoring details" aria-expanded="false" aria-controls="grade_info_4543421">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See scoring details</span>
          </span>
          <i class="icon-check-plus standalone-icon"></i>
        </a>
        <a href="#" class="toggle_rubric_assessments_link tooltip" aria-label="See rubric results" aria-expanded="false" aria-controls="rubric_4543421" tabindex="0" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See rubric results</span>
          </span>
          <i class="icon-rubric"></i>
        </a>
      </td>
    </tr>
    <tr id="final_grade_info_4543421" class="comments assignment_graded" style="display: none;">
    </tr>
    <tr id="grade_info_4543421" class="comments grade_details assignment_graded" style="display: none;">
        <td colspan="6" style="padding-bottom: 20px;">
            <table id="score_details_4543421" class="score_details_table">
              <thead>
                <tr>
                  <th colspan="5">
                    Score Details
                  </th>
                  <th>
                    <a href="#" data-aria="grade_info_4543421" aria-label="Close score details" class="screenreader-toggle pull-right">Close</a>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                    <td>
                      Mean:
                      9.9
                    </td>
                    <td>
                      High:
                      10
                    </td>
                    <td>
                      Low:
                      8
                    </td>
                    <td colspan="3">
                      <div style="cursor: pointer; float: right; height: 30px; margin-left: 20px; width: 160px; position: relative; margin-right: 30px;" aria-hidden="true" title="Mean 9.9, High 10.0, Low 8.0">
                        <div class="grade-summary-graph-component" style="height: 10px; margin: 5px 0px; border-width: 2px; border-right-width: 0;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="width: 120px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 150px; width: 0px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 120px; width: 29px; height: 20px; border-width: 2px; border-top-left-radius: 3px; border-bottom-left-radius: 3px; border-right-width: 0; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 149px; width: 1px; height: 20px; border-width: 2px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 153px; height: 10px; margin: 5px 0px; border-width: 2px; border-left-width: 0;">&nbsp;</div>
                          <div class="grade-summary-graph-component" style="top: 5px; height: 10px; width: 10px; left: 145px; border: 2px solid #248; background: #abd; border-radius: 3px;" title="Your Score:
                            10.0 out of 10">&nbsp;
                          </div>
                      </div>
                    </td>
                </tr>
              </tbody>
            </table>
        </td></tr>
    <tr id="comments_thread_4543421" class="comments comments_thread assignment_graded" style="display: none;">
      <td colspan="6">
      </td>
    </tr>
    <tr id="rubric_4543421" class="rubric_assessments assignment_graded" style="display: none;">
    </tr>
  <tr class="student_assignment assignment_graded editable" data-muted="false" id="submission_4541310">

      <th class="title" scope="row">
          <a href="/courses/1244662/assignments/4541310/submissions/4152168">Homework1</a>
          <div class="context">Homeworks</div>

      </th><td class="due">
          Sep 22 by 11:59pm
      </td>


      <td class="assignment_score" title="Click to test a different score">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade" tabindex="0">
              <span class="tooltip_wrap right" aria-hidden="true">
                  <span class="tooltip_text score_teaser">
                      Click to test a different score
                  </span>
              </span>
                <span class="screenreader-only" role="link">
                  Click to test a different score
                </span>
                100
            </span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">
              100.0
            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">
              100
            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">
              100
            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              graded
            <span class="assignment_group_id">1760780</span>
            <span class="assignment_id">4541310</span>
            <span class="group_weight"></span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">
        100
      </td>
      <td class="details">
        <a href="#" class="toggle_final_grade_info tooltip" aria-label="This assignment does not count toward the final grade." aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">Grade Info</span>
          </span>
          <i class="icon-warning standalone-icon"></i>
        </a>
        <a href="#" class="toggle_comments_link tooltip" aria-label="Read comments" aria-describedby="comment_count_for_assignment_4541310" aria-expanded="false" aria-controls="comments_thread_4541310">
          <span class="tooltip_wrap right">
            <span class="tooltip_text" id="comment_count_for_assignment_4541310">
              1 comment
            </span>
          </span>
          <i class="icon-discussion standalone-icon"></i>
        </a>
        <a href="#" class="toggle_score_details_link tooltip" aria-label="See scoring details" aria-expanded="false" aria-controls="grade_info_4541310">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See scoring details</span>
          </span>
          <i class="icon-check-plus standalone-icon"></i>
        </a>
        <a href="#" class="toggle_rubric_assessments_link tooltip" aria-label="See rubric results" aria-expanded="false" aria-controls="rubric_4541310" tabindex="0" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See rubric results</span>
          </span>
          <i class="icon-rubric"></i>
        </a>
            <a class="tooltip" title="Similarity score -- more information" href="/courses/1244662/assignments/4541310/submissions/4152168/turnitin/attachment_47990255" style="" target="_blank">
              <img alt="See Turnitin results" src="https://du11hjcvx0uqb.cloudfront.net/dist/images/turnitin_warning_score-7650b2ca85.png">
              <span class="tooltip_wrap right">
                <span class="tooltip_text">See Turnitin results</span>
              </span>
            </a>
      </td>
    </tr>
    <tr id="final_grade_info_4541310" class="comments assignment_graded" style="display: none;">
    </tr>
    <tr id="grade_info_4541310" class="comments grade_details assignment_graded" style="display: none;">
        <td colspan="6" style="padding-bottom: 20px;">
            <table id="score_details_4541310" class="score_details_table">
              <thead>
                <tr>
                  <th colspan="5">
                    Score Details
                  </th>
                  <th>
                    <a href="#" data-aria="grade_info_4541310" aria-label="Close score details" class="screenreader-toggle pull-right">Close</a>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                    <td>
                      Mean:
                      66
                    </td>
                    <td>
                      High:
                      100
                    </td>
                    <td>
                      Low:
                      0
                    </td>
                    <td colspan="3">
                      <div style="cursor: pointer; float: right; height: 30px; margin-left: 20px; width: 160px; position: relative; margin-right: 30px;" aria-hidden="true" title="Mean 66.0, High 100.0, Low 0.0">
                        <div class="grade-summary-graph-component" style="height: 10px; margin: 5px 0px; border-width: 2px; border-right-width: 0;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="width: 0px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 150px; width: 0px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 0px; width: 99px; height: 20px; border-width: 2px; border-top-left-radius: 3px; border-bottom-left-radius: 3px; border-right-width: 0; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 99px; width: 51px; height: 20px; border-width: 2px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 153px; height: 10px; margin: 5px 0px; border-width: 2px; border-left-width: 0;">&nbsp;</div>
                          <div class="grade-summary-graph-component" style="top: 5px; height: 10px; width: 10px; left: 145px; border: 2px solid #248; background: #abd; border-radius: 3px;" title="Your Score:
                            100.0 out of 100">&nbsp;
                          </div>
                      </div>
                    </td>
                </tr>
              </tbody>
            </table>
        </td></tr>
    <tr id="comments_thread_4541310" class="comments comments_thread assignment_graded" style="display: none;">
      <td colspan="6">
            <table class="score_details_table">
              <thead>
                <tr>
                  <th>Comments</th>
                  <th>
                    <a href="#" data-aria="comments_thread_4541310" aria-label="Close comments" class="screenreader-toggle pull-right">Close</a>
                  </th>
                </tr>
              </thead>
              <tbody>
                  <tr>
                    <td>
                      <span style="white-space: pre-wrap;">P1: 40
P2: 10
P3: 10
P4: 30
P5: 10</span>
                    <div style="text-align: right; font-size: 0.8em; margin-right: 10px; clear: both;">
                    </div>
                  </td>
                  <td>
                    Harsh Mehta,
                    Oct 7 at 10:18pm
                  </td>
              </tr>
            </tbody>
          </table>
      </td>
    </tr>
    <tr id="rubric_4541310" class="rubric_assessments assignment_graded" style="display: none;">
    </tr>
  <tr class="student_assignment assignment_graded editable" data-muted="false" id="submission_4547478">

      <th class="title" scope="row">
          <a href="/courses/1244662/assignments/4547478/submissions/4152168">In-class-assignment-sept-26</a>
          <div class="context">Quizzes and In-class assignments</div>

      </th><td class="due">
          Sep 26 by 10:15am
      </td>


      <td class="assignment_score" title="Click to test a different score">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade" tabindex="0">
              <span class="tooltip_wrap right" aria-hidden="true">
                  <span class="tooltip_text score_teaser">
                      Click to test a different score
                  </span>
              </span>
                <span class="screenreader-only" role="link">
                  Click to test a different score
                </span>
                10
            </span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">
              10.0
            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">
              10
            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">
              10
            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              graded
            <span class="assignment_group_id">1760781</span>
            <span class="assignment_id">4547478</span>
            <span class="group_weight"></span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">
        10
      </td>
      <td class="details">
        <a href="#" class="toggle_final_grade_info tooltip" aria-label="This assignment does not count toward the final grade." aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">Grade Info</span>
          </span>
          <i class="icon-warning standalone-icon"></i>
        </a>
        <a href="#" class="toggle_comments_link tooltip" aria-label="Read comments" aria-describedby="comment_count_for_assignment_4547478" aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text" id="comment_count_for_assignment_4547478">
              0 comments
            </span>
          </span>
          <i class="icon-discussion standalone-icon"></i>
        </a>
        <a href="#" class="toggle_score_details_link tooltip" aria-label="See scoring details" aria-expanded="false" aria-controls="grade_info_4547478">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See scoring details</span>
          </span>
          <i class="icon-check-plus standalone-icon"></i>
        </a>
        <a href="#" class="toggle_rubric_assessments_link tooltip" aria-label="See rubric results" aria-expanded="false" aria-controls="rubric_4547478" tabindex="0" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See rubric results</span>
          </span>
          <i class="icon-rubric"></i>
        </a>
      </td>
    </tr>
    <tr id="final_grade_info_4547478" class="comments assignment_graded" style="display: none;">
    </tr>
    <tr id="grade_info_4547478" class="comments grade_details assignment_graded" style="display: none;">
        <td colspan="6" style="padding-bottom: 20px;">
            <table id="score_details_4547478" class="score_details_table">
              <thead>
                <tr>
                  <th colspan="5">
                    Score Details
                  </th>
                  <th>
                    <a href="#" data-aria="grade_info_4547478" aria-label="Close score details" class="screenreader-toggle pull-right">Close</a>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                    <td>
                      Mean:
                      8.7
                    </td>
                    <td>
                      High:
                      10
                    </td>
                    <td>
                      Low:
                      0
                    </td>
                    <td colspan="3">
                      <div style="cursor: pointer; float: right; height: 30px; margin-left: 20px; width: 160px; position: relative; margin-right: 30px;" aria-hidden="true" title="Mean 8.7, High 10.0, Low 0.0">
                        <div class="grade-summary-graph-component" style="height: 10px; margin: 5px 0px; border-width: 2px; border-right-width: 0;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="width: 0px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 150px; width: 0px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 0px; width: 130px; height: 20px; border-width: 2px; border-top-left-radius: 3px; border-bottom-left-radius: 3px; border-right-width: 0; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 130px; width: 20px; height: 20px; border-width: 2px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 153px; height: 10px; margin: 5px 0px; border-width: 2px; border-left-width: 0;">&nbsp;</div>
                          <div class="grade-summary-graph-component" style="top: 5px; height: 10px; width: 10px; left: 145px; border: 2px solid #248; background: #abd; border-radius: 3px;" title="Your Score:
                            10.0 out of 10">&nbsp;
                          </div>
                      </div>
                    </td>
                </tr>
              </tbody>
            </table>
        </td></tr>
    <tr id="comments_thread_4547478" class="comments comments_thread assignment_graded" style="display: none;">
      <td colspan="6">
      </td>
    </tr>
    <tr id="rubric_4547478" class="rubric_assessments assignment_graded" style="display: none;">
    </tr>
  <tr class="student_assignment assignment_graded editable" data-muted="false" id="submission_4541773">

      <th class="title" scope="row">
          <a href="/courses/1244662/assignments/4541773/submissions/4152168">Project abstract</a>
          <div class="context">Course Project</div>

      </th><td class="due">
          Sep 29 by 11:59pm
      </td>


      <td class="assignment_score" title="Click to test a different score">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade" tabindex="0">
              <span class="tooltip_wrap right" aria-hidden="true">
                  <span class="tooltip_text score_teaser">
                      Click to test a different score
                  </span>
              </span>
                <span class="screenreader-only" role="link">
                  Click to test a different score
                </span>
                10
            </span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">
              10.0
            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">
              10
            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">
              10
            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              graded
            <span class="assignment_group_id">1760782</span>
            <span class="assignment_id">4541773</span>
            <span class="group_weight"></span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">
        10
      </td>
      <td class="details">
        <a href="#" class="toggle_final_grade_info tooltip" aria-label="This assignment does not count toward the final grade." aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">Grade Info</span>
          </span>
          <i class="icon-warning standalone-icon"></i>
        </a>
        <a href="#" class="toggle_comments_link tooltip" aria-label="Read comments" aria-describedby="comment_count_for_assignment_4541773" aria-expanded="false" aria-controls="comments_thread_4541773">
          <span class="tooltip_wrap right">
            <span class="tooltip_text" id="comment_count_for_assignment_4541773">
              2 comments
            </span>
          </span>
          <i class="icon-discussion standalone-icon"></i>
        </a>
        <a href="#" class="toggle_score_details_link tooltip" aria-label="See scoring details" aria-expanded="false" aria-controls="grade_info_4541773">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See scoring details</span>
          </span>
          <i class="icon-check-plus standalone-icon"></i>
        </a>
        <a href="#" class="toggle_rubric_assessments_link tooltip" aria-label="See rubric results" aria-expanded="false" aria-controls="rubric_4541773" tabindex="0" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See rubric results</span>
          </span>
          <i class="icon-rubric"></i>
        </a>
      </td>
    </tr>
    <tr id="final_grade_info_4541773" class="comments assignment_graded" style="display: none;">
    </tr>
    <tr id="grade_info_4541773" class="comments grade_details assignment_graded" style="display: none;">
        <td colspan="6" style="padding-bottom: 20px;">
            <table id="score_details_4541773" class="score_details_table">
              <thead>
                <tr>
                  <th colspan="5">
                    Score Details
                  </th>
                  <th>
                    <a href="#" data-aria="grade_info_4541773" aria-label="Close score details" class="screenreader-toggle pull-right">Close</a>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                    <td>
                      Mean:
                      10
                    </td>
                    <td>
                      High:
                      10
                    </td>
                    <td>
                      Low:
                      10
                    </td>
                    <td colspan="3">
                      <div style="cursor: pointer; float: right; height: 30px; margin-left: 20px; width: 160px; position: relative; margin-right: 30px;" aria-hidden="true" title="Mean 10.0, High 10.0, Low 10.0">
                        <div class="grade-summary-graph-component" style="height: 10px; margin: 5px 0px; border-width: 2px; border-right-width: 0;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="width: 150px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 150px; width: 0px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 150px; width: 0px; height: 20px; border-width: 2px; border-top-left-radius: 3px; border-bottom-left-radius: 3px; border-right-width: 0; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 150px; width: 0px; height: 20px; border-width: 2px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 153px; height: 10px; margin: 5px 0px; border-width: 2px; border-left-width: 0;">&nbsp;</div>
                          <div class="grade-summary-graph-component" style="top: 5px; height: 10px; width: 10px; left: 145px; border: 2px solid #248; background: #abd; border-radius: 3px;" title="Your Score:
                            10.0 out of 10">&nbsp;
                          </div>
                      </div>
                    </td>
                </tr>
              </tbody>
            </table>
        </td></tr>
    <tr id="comments_thread_4541773" class="comments comments_thread assignment_graded" style="display: none;">
      <td colspan="6">
            <table class="score_details_table">
              <thead>
                <tr>
                  <th>Comments</th>
                  <th>
                    <a href="#" data-aria="comments_thread_4541773" aria-label="Close comments" class="screenreader-toggle pull-right">Close</a>
                  </th>
                </tr>
              </thead>
              <tbody>
                  <tr>
                    <td>
                      <span style="white-space: pre-wrap;">Building a social-network mobile app may be more work than you anticipate. Don't build-in too many features. Focus on the algorithm part.
From the abstract it is not clear how each algorithm will be used. In the project report you will have to be very specific about the inputs/outputs of your algorithm and its analysis.</span>
                    <div style="text-align: right; font-size: 0.8em; margin-right: 10px; clear: both;">
                    </div>
                  </td>
                  <td>
                    Gheorghi Guzun,
                    Oct 3 at  7:37pm
                  </td>
                  </tr><tr>
                    <td>
                      <span style="white-space: pre-wrap;">This being a social network it would be better to use graphs for mapping your users</span>
                    <div style="text-align: right; font-size: 0.8em; margin-right: 10px; clear: both;">
                    </div>
                  </td>
                  <td>
                    Gheorghi Guzun,
                    Oct 5 at  4:26pm
                  </td>
              </tr>
            </tbody>
          </table>
      </td>
    </tr>
    <tr id="rubric_4541773" class="rubric_assessments assignment_graded" style="display: none;">
    </tr>
  <tr class="student_assignment assignment_graded editable" data-muted="false" id="submission_4551802">

      <th class="title" scope="row">
          <a href="/courses/1244662/assignments/4551802/submissions/4152168">Oct-5-inClass-Quiz</a>
          <div class="context">Quizzes and In-class assignments</div>

      </th><td class="due">
          Oct 5 by 10:15am
      </td>


      <td class="assignment_score" title="Click to test a different score">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade" tabindex="0">
              <span class="tooltip_wrap right" aria-hidden="true">
                  <span class="tooltip_text score_teaser">
                      Click to test a different score
                  </span>
              </span>
                <span class="screenreader-only" role="link">
                  Click to test a different score
                </span>
                7
            </span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">
              7.0
            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">
              7
            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">
              7
            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              graded
            <span class="assignment_group_id">1760781</span>
            <span class="assignment_id">4551802</span>
            <span class="group_weight"></span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">
        10
      </td>
      <td class="details">
        <a href="#" class="toggle_final_grade_info tooltip" aria-label="This assignment does not count toward the final grade." aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">Grade Info</span>
          </span>
          <i class="icon-warning standalone-icon"></i>
        </a>
        <a href="#" class="toggle_comments_link tooltip" aria-label="Read comments" aria-describedby="comment_count_for_assignment_4551802" aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text" id="comment_count_for_assignment_4551802">
              0 comments
            </span>
          </span>
          <i class="icon-discussion standalone-icon"></i>
        </a>
        <a href="#" class="toggle_score_details_link tooltip" aria-label="See scoring details" aria-expanded="false" aria-controls="grade_info_4551802">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See scoring details</span>
          </span>
          <i class="icon-check-plus standalone-icon"></i>
        </a>
        <a href="#" class="toggle_rubric_assessments_link tooltip" aria-label="See rubric results" aria-expanded="false" aria-controls="rubric_4551802" tabindex="0" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See rubric results</span>
          </span>
          <i class="icon-rubric"></i>
        </a>
      </td>
    </tr>
    <tr id="final_grade_info_4551802" class="comments assignment_graded" style="display: none;">
    </tr>
    <tr id="grade_info_4551802" class="comments grade_details assignment_graded" style="display: none;">
        <td colspan="6" style="padding-bottom: 20px;">
            <table id="score_details_4551802" class="score_details_table">
              <thead>
                <tr>
                  <th colspan="5">
                    Score Details
                  </th>
                  <th>
                    <a href="#" data-aria="grade_info_4551802" aria-label="Close score details" class="screenreader-toggle pull-right">Close</a>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                    <td>
                      Mean:
                      4.5
                    </td>
                    <td>
                      High:
                      9
                    </td>
                    <td>
                      Low:
                      0
                    </td>
                    <td colspan="3">
                      <div style="cursor: pointer; float: right; height: 30px; margin-left: 20px; width: 160px; position: relative; margin-right: 30px;" aria-hidden="true" title="Mean 4.5, High 9.0, Low 0.0">
                        <div class="grade-summary-graph-component" style="height: 10px; margin: 5px 0px; border-width: 2px; border-right-width: 0;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="width: 0px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 135px; width: 15px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 0px; width: 68px; height: 20px; border-width: 2px; border-top-left-radius: 3px; border-bottom-left-radius: 3px; border-right-width: 0; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 68px; width: 68px; height: 20px; border-width: 2px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 150px; height: 10px; margin: 5px 0px; border-width: 2px; border-left-width: 0;">&nbsp;</div>
                          <div class="grade-summary-graph-component" style="top: 5px; height: 10px; width: 10px; left: 100px; border: 2px solid #248; background: #abd; border-radius: 3px;" title="Your Score:
                            7.0 out of 10">&nbsp;
                          </div>
                      </div>
                    </td>
                </tr>
              </tbody>
            </table>
        </td></tr>
    <tr id="comments_thread_4551802" class="comments comments_thread assignment_graded" style="display: none;">
      <td colspan="6">
      </td>
    </tr>
    <tr id="rubric_4551802" class="rubric_assessments assignment_graded" style="display: none;">
    </tr>
  <tr class="student_assignment assignment_graded editable" data-muted="false" id="submission_4551280">

      <th class="title" scope="row">
          <a href="/courses/1244662/assignments/4551280/submissions/4152168">Reading Quiz: Data Structure and Hashing</a>
          <div class="context">Quizzes and In-class assignments</div>

      </th><td class="due">
          Oct 6 by 11:59pm
      </td>


      <td class="assignment_score" title="Click to test a different score">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade" tabindex="0">
              <span class="tooltip_wrap right" aria-hidden="true">
                  <span class="tooltip_text score_teaser">
                      Click to test a different score
                  </span>
              </span>
                <span class="screenreader-only" role="link">
                  Click to test a different score
                </span>
                10
            </span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">
              10.0
            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">
              10
            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">
              10
            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              graded
            <span class="assignment_group_id">1760781</span>
            <span class="assignment_id">4551280</span>
            <span class="group_weight"></span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">
        10
      </td>
      <td class="details">
        <a href="#" class="toggle_final_grade_info tooltip" aria-label="This assignment does not count toward the final grade." aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">Grade Info</span>
          </span>
          <i class="icon-warning standalone-icon"></i>
        </a>
        <a href="#" class="toggle_comments_link tooltip" aria-label="Read comments" aria-describedby="comment_count_for_assignment_4551280" aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text" id="comment_count_for_assignment_4551280">
              0 comments
            </span>
          </span>
          <i class="icon-discussion standalone-icon"></i>
        </a>
        <a href="#" class="toggle_score_details_link tooltip" aria-label="See scoring details" aria-expanded="false" aria-controls="grade_info_4551280">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See scoring details</span>
          </span>
          <i class="icon-check-plus standalone-icon"></i>
        </a>
        <a href="#" class="toggle_rubric_assessments_link tooltip" aria-label="See rubric results" aria-expanded="false" aria-controls="rubric_4551280" tabindex="0" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See rubric results</span>
          </span>
          <i class="icon-rubric"></i>
        </a>
      </td>
    </tr>
    <tr id="final_grade_info_4551280" class="comments assignment_graded" style="display: none;">
    </tr>
    <tr id="grade_info_4551280" class="comments grade_details assignment_graded" style="display: none;">
        <td colspan="6" style="padding-bottom: 20px;">
            <table id="score_details_4551280" class="score_details_table">
              <thead>
                <tr>
                  <th colspan="5">
                    Score Details
                  </th>
                  <th>
                    <a href="#" data-aria="grade_info_4551280" aria-label="Close score details" class="screenreader-toggle pull-right">Close</a>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                    <td>
                      Mean:
                      9.4
                    </td>
                    <td>
                      High:
                      10
                    </td>
                    <td>
                      Low:
                      4
                    </td>
                    <td colspan="3">
                      <div style="cursor: pointer; float: right; height: 30px; margin-left: 20px; width: 160px; position: relative; margin-right: 30px;" aria-hidden="true" title="Mean 9.4, High 10.0, Low 4.0">
                        <div class="grade-summary-graph-component" style="height: 10px; margin: 5px 0px; border-width: 2px; border-right-width: 0;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="width: 60px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 150px; width: 0px; height: 0px; margin-top: 10px; border-bottom-width: 2px;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 60px; width: 81px; height: 20px; border-width: 2px; border-top-left-radius: 3px; border-bottom-left-radius: 3px; border-right-width: 0; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 141px; width: 9px; height: 20px; border-width: 2px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; background: #fff;">&nbsp;</div>
                        <div class="grade-summary-graph-component" style="left: 153px; height: 10px; margin: 5px 0px; border-width: 2px; border-left-width: 0;">&nbsp;</div>
                          <div class="grade-summary-graph-component" style="top: 5px; height: 10px; width: 10px; left: 145px; border: 2px solid #248; background: #abd; border-radius: 3px;" title="Your Score:
                            10.0 out of 10">&nbsp;
                          </div>
                      </div>
                    </td>
                </tr>
              </tbody>
            </table>
        </td></tr>
    <tr id="comments_thread_4551280" class="comments comments_thread assignment_graded" style="display: none;">
      <td colspan="6">
      </td>
    </tr>
    <tr id="rubric_4551280" class="rubric_assessments assignment_graded" style="display: none;">
    </tr>
  <tr class="student_assignment editable" data-muted="true" id="submission_4550558">

      <th class="title" scope="row">
          <a href="/courses/1244662/assignments/4550558/submissions/4152168">Homework 2</a>
          <div class="context">Homeworks</div>

      </th><td class="due">
          Oct 13 by 11:59pm
      </td>


      <td class="assignment_score" title="Click to test a different score">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade" tabindex="0">
              <span class="tooltip_wrap right" aria-hidden="true">
                  <span class="tooltip_text score_teaser">
                      Instructor is working on grades
                  </span>
              </span>
                <i class="icon-muted" title="Muted"></i>
            </span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">

            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">

            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">

            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              submitted
            <span class="assignment_group_id">1760780</span>
            <span class="assignment_id">4550558</span>
            <span class="group_weight"></span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">
        100
      </td>
      <td class="details">
        <a href="#" class="toggle_final_grade_info tooltip" aria-label="This assignment does not count toward the final grade." aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">Grade Info</span>
          </span>
          <i class="icon-warning standalone-icon"></i>
        </a>
        <a href="#" class="toggle_comments_link tooltip" aria-label="Read comments" aria-describedby="comment_count_for_assignment_4550558" aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text" id="comment_count_for_assignment_4550558">
              1 comment
            </span>
          </span>
          <i class="icon-discussion standalone-icon"></i>
        </a>
        <a href="#" class="toggle_score_details_link tooltip" aria-label="See scoring details" aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See scoring details</span>
          </span>
          <i class="icon-check-plus standalone-icon"></i>
        </a>
        <a href="#" class="toggle_rubric_assessments_link tooltip" aria-label="See rubric results" aria-expanded="false" aria-controls="rubric_4550558" tabindex="0" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See rubric results</span>
          </span>
          <i class="icon-rubric"></i>
        </a>
      </td>
    </tr>
    <tr id="final_grade_info_4550558" class="comments " style="display: none;">
    </tr>
    <tr id="grade_info_4550558" class="comments grade_details " style="display: none;">
        <td colspan="6" style="padding-bottom: 20px;">
        </td></tr>
    <tr id="comments_thread_4550558" class="comments comments_thread " style="display: none;">
      <td colspan="6">
            <table class="score_details_table">
              <thead>
                <tr>
                  <th>Comments</th>
                  <th>
                    <a href="#" data-aria="comments_thread_4550558" aria-label="Close comments" class="screenreader-toggle pull-right">Close</a>
                  </th>
                </tr>
              </thead>
              <tbody>
                  <tr>
                    <td>
                      <span style="white-space: pre-wrap;">To run problem2.cpp
1) Make sure to have a c++ IDE
2) Open problem2.cpp
3) Press build and run
4) A menu will pop up. Type in choice numbers to insert, delete, search, display, or exit</span>
                    <div style="text-align: right; font-size: 0.8em; margin-right: 10px; clear: both;">
                    </div>
                  </td>
                  <td>
                    Albert Zarate,
                    Oct 13 at  9:30pm
                  </td>
              </tr>
            </tbody>
          </table>
      </td>
    </tr>
    <tr id="rubric_4550558" class="rubric_assessments " style="display: none;">
    </tr>
  <tr class="student_assignment editable" data-muted="false" id="submission_4555589">

      <th class="title" scope="row">
          <a href="/courses/1244662/assignments/4555589/submissions/4152168">Homework 3</a>
          <div class="context">Homeworks</div>

      </th><td class="due">
          Oct 24 by 11:59pm
      </td>


      <td class="assignment_score" title="Click to test a different score">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade" tabindex="0">
              <span class="tooltip_wrap right" aria-hidden="true">
                  <span class="tooltip_text score_teaser">
                      Click to test a different score
                  </span>
              </span>
                <span class="screenreader-only" role="link">
                  Click to test a different score
                </span>
                -
            </span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">

            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">

            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">

            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              unsubmitted
            <span class="assignment_group_id">1760780</span>
            <span class="assignment_id">4555589</span>
            <span class="group_weight"></span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">
        100
      </td>
      <td class="details">
        <a href="#" class="toggle_final_grade_info tooltip" aria-label="This assignment does not count toward the final grade." aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">Grade Info</span>
          </span>
          <i class="icon-warning standalone-icon"></i>
        </a>
        <a href="#" class="toggle_comments_link tooltip" aria-label="Read comments" aria-describedby="comment_count_for_assignment_4555589" aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text" id="comment_count_for_assignment_4555589">
              0 comments
            </span>
          </span>
          <i class="icon-discussion standalone-icon"></i>
        </a>
        <a href="#" class="toggle_score_details_link tooltip" aria-label="See scoring details" aria-hidden="true" role="presentation" tabindex="-1" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See scoring details</span>
          </span>
          <i class="icon-check-plus standalone-icon"></i>
        </a>
        <a href="#" class="toggle_rubric_assessments_link tooltip" aria-label="See rubric results" aria-expanded="false" aria-controls="rubric_4555589" tabindex="0" style="visibility: hidden;">
          <span class="tooltip_wrap right">
            <span class="tooltip_text">See rubric results</span>
          </span>
          <i class="icon-rubric"></i>
        </a>
      </td>
    </tr>
    <tr id="final_grade_info_4555589" class="comments " style="display: none;">
    </tr>
    <tr id="grade_info_4555589" class="comments grade_details " style="display: none;">

    </tr>
    <tr id="rubric_4555589" class="rubric_assessments " style="display: none;">
    </tr>
  <tr class="student_assignment hard_coded group_total" data-muted="" id="submission_group-1760780">

      <th class="title" scope="row">
          Homeworks

      </th><td class="due">
      </td>


      <td class="assignment_score" title="">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade">100%</span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">

            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">

            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">

            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              none
            <span class="assignment_group_id">1760780</span>
            <span class="assignment_id">group-1760780</span>
            <span class="group_weight">20.0</span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">100.00 / 100.00</td>
      <td class="details">
      </td>
    </tr>
    <tr id="final_grade_info_group-1760780" class="comments " style="display: none;">
    </tr>
    <tr id="grade_info_group-1760780" class="comments grade_details " style="display: none;">

    </tr>
    <tr id="rubric_group-1760780" class="rubric_assessments " style="display: none;">
    </tr>
  <tr class="student_assignment hard_coded group_total" data-muted="" id="submission_group-1760781">

      <th class="title" scope="row">
          Quizzes and In-class assignments

      </th><td class="due">
      </td>


      <td class="assignment_score" title="">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade">95%</span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">

            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">

            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">

            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              none
            <span class="assignment_group_id">1760781</span>
            <span class="assignment_id">group-1760781</span>
            <span class="group_weight">10.0</span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">57.00 / 60.00</td>
      <td class="details">
      </td>
    </tr>
    <tr id="final_grade_info_group-1760781" class="comments " style="display: none;">
    </tr>
    <tr id="grade_info_group-1760781" class="comments grade_details " style="display: none;">

    </tr>
    <tr id="rubric_group-1760781" class="rubric_assessments " style="display: none;">
    </tr>
  <tr class="student_assignment hard_coded group_total" data-muted="" id="submission_group-1760782">

      <th class="title" scope="row">
          Course Project

      </th><td class="due">
      </td>


      <td class="assignment_score" title="">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade">100%</span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">

            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">

            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">

            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              none
            <span class="assignment_group_id">1760782</span>
            <span class="assignment_id">group-1760782</span>
            <span class="group_weight">20.0</span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">10.00 / 10.00</td>
      <td class="details">
      </td>
    </tr>
    <tr id="final_grade_info_group-1760782" class="comments " style="display: none;">
    </tr>
    <tr id="grade_info_group-1760782" class="comments grade_details " style="display: none;">

    </tr>
    <tr id="rubric_group-1760782" class="rubric_assessments " style="display: none;">
    </tr>
  <tr class="student_assignment hard_coded group_total" data-muted="" id="submission_group-1760783">

      <th class="title" scope="row">
          Midterm

      </th><td class="due">
      </td>


      <td class="assignment_score" title="">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade">N/A</span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">

            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">

            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">

            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              none
            <span class="assignment_group_id">1760783</span>
            <span class="assignment_id">group-1760783</span>
            <span class="group_weight">20.0</span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">0.00 / 0.00</td>
      <td class="details">
      </td>
    </tr>
    <tr id="final_grade_info_group-1760783" class="comments " style="display: none;">
    </tr>
    <tr id="grade_info_group-1760783" class="comments grade_details " style="display: none;">

    </tr>
    <tr id="rubric_group-1760783" class="rubric_assessments " style="display: none;">
    </tr>
  <tr class="student_assignment hard_coded group_total" data-muted="" id="submission_group-1754307">

      <th class="title" scope="row">
          Final Exam

      </th><td class="due">
      </td>


      <td class="assignment_score" title="">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade">N/A</span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">

            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">

            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">

            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              none
            <span class="assignment_group_id">1754307</span>
            <span class="assignment_id">group-1754307</span>
            <span class="group_weight">30.0</span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">0.00 / 0.00</td>
      <td class="details">
      </td>
    </tr>
    <tr id="final_grade_info_group-1754307" class="comments " style="display: none;">
    </tr>
    <tr id="grade_info_group-1754307" class="comments grade_details " style="display: none;">

    </tr>
    <tr id="rubric_group-1754307" class="rubric_assessments " style="display: none;">
    </tr>
  <tr class="student_assignment hard_coded final_grade" data-muted="" id="submission_final-grade">

      <th class="title" scope="row">
          Total

      </th><td class="due">

      </td>


      <td class="assignment_score" title="">
        <div style="position: relative; height: 100%;" class="score_holder">
          <span class="tooltip">
            <span class="grade">99%</span>
          </span>
          <div style="display: none;">
            <!-- Store the original points so we don't need to parse and guess at locale -->
            <span class="original_points">

            </span>
            <!-- Store the original score so that we can retrieve it after any "What-If" calculations -->
            <span class="original_score">

            </span>
            <!-- Store the current score so that it can persist between multiple "What-If" calculations -->
            <span class="what_if_score">

            </span>
            <!-- Load any previously saved "What-If" scores -->
            <span class="student_entered_score">

            </span>
            <span class="submission_status">
              none
            <span class="assignment_group_id"></span>
            <span class="assignment_id">final-grade</span>
            <span class="group_weight"></span>
            <span class="rules"></span>
          </span></div>
        </div>
      </td>
      <td class="possible points_possible" aria-label="">99.00 / 100.00</td>
      <td class="details">
      </td>
    </tr>
    <tr id="final_grade_info_final-grade" class="comments " style="display: none;">
    </tr>
    <tr id="grade_info_final-grade" class="comments grade_details " style="display: none;">

    </tr>
    <tr id="rubric_final-grade" class="rubric_assessments " style="display: none;">
    </tr>
</tbody></table>
</div>
  <small><i class="icon-muted" role="presentation"></i>Your instructor is working on grades. While your instructor is working on grades, grade and comment information is unavailable.</small>
<div id="total_groups_weight" style="display: none;">100.0</div>

<div id="rubric_long_description_dialog" style="display: none;">
  <div class="description" style="border-bottom: 1px solid #ccc; padding: 5px 0; font-size: 1.2em; font-weight: bold; margin-bottom: 5px;">
  </div>
  <div class="editing">
    <textarea class="long_description" aria-label="Long Description" name="long_description" style="width: 370px;"></textarea>
    <div class="button-container">
      <button type="button" class="btn btn button-secondary cancel_button">Cancel</button>
      <button type="button" class="btn save_button">Update Description</button>
    </div>
  </div>
  <div class="displaying">
    <div class="long_description">
    </div>
  </div>
</div>
<div id="rubric_criterion_comments_dialog" style="display: none;">
  <div class="criterion_description" style="border-bottom: 1px solid #ccc; padding: 5px 0; font-size: 1.2em; font-weight: bold; margin-bottom: 5px;" tabindex="-1"></div>
  <div class="editing">
    <label for="criterion_comments_textarea">
      Additional Comments:
    </label>
    <textarea id="criterion_comments_textarea" class="criterion_comments" name="criterion_comments" style="width: 370px;"></textarea>
    <div class="button-container">
      <button type="button" class="btn btn button-secondary cancel_button">Cancel</button>
      <button type="button" class="btn save_button">Update Comments</button>
    </div>
  </div>
  <div class="displaying">
    Additional Comments:
    <div class="criterion_comments" style="margin-top: 10px;">
    </div>
  </div>
</div>

<input type="text" style="width: 40px; display: none;" id="grade_entry" title="Enter a score to test">
<a href="#" id="revert_score_template" class="revert_score_link" title="Revert to original score"><i class="icon-reply-2"></i></a>
<a href="/courses/1244662/assignments/%7B%7B%20assignment_id%20%7D%7D/submissions/4152168" class="update_submission_url" style="display: none;">&nbsp;</a>

          </div>
        </div>
        <div id="right-side-wrapper" class="ic-app-main-content__secondary">
          <aside id="right-side" role="complementary">
              <div id="student-grades-right-content">
      <div class="student_assignment final_grade" style="font-size: 1.2em;">
        Total: <span class="grade">99%</span>
      </div>
        <div id="student-grades-whatif" class="show_guess_grades student-grades-revert-guess-button">
          <button type="button" class="btn button-sidebar-wide show_guess_grades_link"> <i class="icon-check-plus"></i> Show Saved "What-If" Scores</button>
        </div>
        <div id="student-grades-revert" class="revert_all_scores student-grades-revert-guess-button" style="display: none;">
          *NOTE*: This is NOT your official score.<br>
          <button href="#" id="revert-all-to-actual-score" class="btn revert_all_scores_link"><i class="icon-reply-2"></i> Revert to Actual Score</button>
        </div>
    <div id="student-grades-show-all" class="show_all_details">
      <button type="button" class="Button" id="show_all_details_button">Show All Details</button>
    </div>
    <div id="assignments-not-weighted">

<div role="complementary" aria-label="Assignment Weights">
  <h2>Assignments are weighted by group:</h2>

  <table class="summary">
    <thead>
    <tr>
      <th scope="col">Group</th>
      <th scope="col">Weight</th>
    </tr>
    </thead>
    <tbody>
        <tr>
          <th scope="row">Homeworks</th>
          <td>20%</td>
        </tr>
        <tr>
          <th scope="row">Quizzes and In-class assignments</th>
          <td>10%</td>
        </tr>
        <tr>
          <th scope="row">Course Project</th>
          <td>20%</td>
        </tr>
        <tr>
          <th scope="row">Midterm</th>
          <td>20%</td>
        </tr>
        <tr>
          <th scope="row">Final Exam</th>
          <td>30%</td>
        </tr>
      <tr style="font-weight: bold;">
        <th scope="row">Total</th>
        <td>100%</td>
      </tr>
    </tbody>
  </table>
</div>

        <div id="only_consider_graded_assignments_wrapper" class="ic-Form-control ic-Form-control--checkbox">
          <input type="checkbox" id="only_consider_graded_assignments" checked="true">
          <label class="ic-Label" for="only_consider_graded_assignments">Calculate based only on graded assignments</label>
        </div>
    </div>
      <div id="whatif-score-description">
        You can view your grades based on What-If scores so that you know how grades will be affected by upcoming or resubmitted assignments. You can test scores for an assignment that already includes a score, or an assignment that has yet to be graded.
      </div>
  </div>

          </aside>
        </div>
      </div>
    </div>
  </div>



    <div style="display:none;"><!-- Everything inside of this should always stay hidden -->
        <div id="page_view_id">bdbb98c5-a5aa-445d-8b3b-97211e18e664</div>
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
  INST = {"environment":"production","allowMediaComments":true,"kalturaSettings":{"domain":"nv.instructuremedia.com","resource_domain":"nv.instructuremedia.com","rtmp_domain":"fms-prod.instructuremedia.com","partner_id":"9","subpartner_id":"0","player_ui_conf":"0","kcw_ui_conf":"0","upload_ui_conf":"0","max_file_size_bytes":534773760,"do_analytics":false,"hide_rte_button":false,"js_uploader":true},"googleAnalyticsAccount":"UA-9138420-1","disableScribdPreviews":true,"logPageViews":true,"maxVisibleEditorButtons":3,"editorButtons":[{"name":"Google Drive","id":34141,"url":"https://google-drive-lti-iad-prod.instructure.com/lti/rce-content-selection","icon_url":"https://google-drive-lti-iad-prod.instructure.com/assets/google_drive_icon-146a263de4b09116263668157f317cbdb540eebdd626571c8741152fc6dc0c8b.png","canvas_icon_class":null,"width":700,"height":600}]};
  ENV = {"ASSET_HOST":"https://du11hjcvx0uqb.cloudfront.net","active_brand_config":"9aa105797e3845a39d5ae6e392e0bfde","active_brand_config_json_url":"https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/9aa105797e3845a39d5ae6e392e0bfde/variables-b59440e479f072e9f8e5fa783f2fcc29.json","url_to_what_gets_loaded_inside_the_tinymce_editor_css":["https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/9aa105797e3845a39d5ae6e392e0bfde/variables-b59440e479f072e9f8e5fa783f2fcc29.css","https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/9aa105797e3845a39d5ae6e392e0bfde/new_styles_normal_contrast/bundles/what_gets_loaded_inside_the_tinymce_editor-4e58055365.css"],"current_user_id":"4152168","current_user":{"id":"4152168","display_name":"Albert Zarate","avatar_image_url":"https://sjsu.instructure.com/images/thumbnails/46797560/MQWOSey0GuwJiMpva6T5BGufmMSkivRXTw1rwTro","html_url":"https://sjsu.instructure.com/about/4152168"},"current_user_roles":["user","student"],"current_user_disabled_inbox":false,"files_domain":"cluster12-files.instructure.com","DOMAIN_ROOT_ACCOUNT_ID":120000000089550,"k12":false,"help_link_name":"Help","help_link_icon":"help","use_high_contrast":false,"SETTINGS":{"open_registration":false,"eportfolios_enabled":true,"collapse_global_nav":false,"show_feedback_link":true,"enable_profiles":true},"page_view_update_url":"/page_views/bdbb98c5-a5aa-445d-8b3b-97211e18e664?page_view_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpIjoiYmRiYjk4YzUtYTVhYS00NDVkLThiM2ItOTcyMTFlMThlNjY0IiwidSI6MTIwMDAwMDA0MTUyMTY4LCJjIjoiMjAxNy0xMC0yNFQyMjozOToyOS43MVoifQ.5M0RGWXQBgqw-_6en48BuJvAKV-rzAbosQzz7WBEumc","context_asset_string":"course_1244662","ping_url":"https://sjsu.instructure.com/api/v1/courses/1244662/ping","TIMEZONE":"America/Los_Angeles","CONTEXT_TIMEZONE":"America/Los_Angeles","GRAPHQL_ENABLED":false,"LOCALE":"en","BIGEASY_LOCALE":"en_US","FULLCALENDAR_LOCALE":"en","MOMENT_LOCALE":"en","submissions":[{"assignment_id":"4555589","score":null,"excused":false,"workflow_state":"unsubmitted"},{"assignment_id":"4541773","score":10.0,"excused":false,"workflow_state":"graded"},{"assignment_id":"4541310","score":100.0,"excused":false,"workflow_state":"graded"},{"assignment_id":"4551802","score":7.0,"excused":false,"workflow_state":"graded"},{"assignment_id":"4551280","score":10.0,"excused":false,"workflow_state":"graded"},{"assignment_id":"4518429","score":10.0,"excused":false,"workflow_state":"graded"},{"assignment_id":"4547478","score":10.0,"excused":false,"workflow_state":"graded"},{"assignment_id":"4543421","score":10.0,"excused":false,"workflow_state":"graded"},{"assignment_id":"4535420","score":10.0,"excused":false,"workflow_state":"graded"}],"assignment_groups":[{"id":"1760780","rules":{},"group_weight":20.0,"assignments":[{"id":"4541310","submission_types":["online_upload"],"points_possible":100.0,"due_at":"2017-09-23T06:59:00Z","omit_from_final_grade":false,"muted":false},{"id":"4550558","submission_types":["online_upload"],"points_possible":100.0,"due_at":"2017-10-14T06:59:00Z","omit_from_final_grade":false,"muted":true},{"id":"4555589","submission_types":["online_upload"],"points_possible":100.0,"due_at":"2017-10-25T06:59:59Z","omit_from_final_grade":false,"muted":false}]},{"id":"1760781","rules":{},"group_weight":10.0,"assignments":[{"id":"4518429","submission_types":["online_upload"],"points_possible":10.0,"due_at":"2017-09-15T06:59:00Z","omit_from_final_grade":false,"muted":false},{"id":"4547478","submission_types":["on_paper"],"points_possible":10.0,"due_at":"2017-09-26T17:15:00Z","omit_from_final_grade":false,"muted":false},{"id":"4535420","submission_types":["online_upload"],"points_possible":10.0,"due_at":"2017-09-06T06:59:00Z","omit_from_final_grade":false,"muted":false},{"id":"4551802","submission_types":["none"],"points_possible":10.0,"due_at":"2017-10-05T17:15:00Z","omit_from_final_grade":false,"muted":false},{"id":"4551280","submission_types":["online_quiz"],"points_possible":10.0,"due_at":"2017-10-07T06:59:00Z","omit_from_final_grade":false,"muted":false},{"id":"4543421","submission_types":["online_quiz"],"points_possible":10.0,"due_at":"2017-09-21T16:00:00Z","omit_from_final_grade":false,"muted":false}]},{"id":"1760782","rules":{},"group_weight":20.0,"assignments":[{"id":"4541773","submission_types":["online_upload"],"points_possible":10.0,"due_at":"2017-09-30T06:59:00Z","omit_from_final_grade":false,"muted":false}]},{"id":"1760783","rules":{},"group_weight":20.0,"assignments":[]},{"id":"1754307","rules":{},"group_weight":30.0,"assignments":[]}],"group_weighting_scheme":"percent","show_total_grade_as_points":false,"grading_scheme":[["A",0.9399999999999999],["A-",0.9],["B+",0.87],["B",0.84],["B-",0.8],["C+",0.77],["C",0.74],["C-",0.7],["D+",0.67],["D",0.64],["D-",0.61],["F",0.0]],"grading_period_set":null,"grading_period":null,"grading_periods":null,"effective_due_dates":null,"exclude_total":false,"student_outcome_gradebook_enabled":false,"student_id":"4152168","badge_counts":{"submissions":0},"notices":[]};
</script>

<script src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/navigation_header.bundle-615775f5bd.js" defer="defer"></script>
<script src="https://instructure-uploads.s3.amazonaws.com/account_120000000089550/attachments/44214137/libraryIcon-2.js?AWSAccessKeyId=AKIAJFNFXH2V2O7RPCAA&amp;Expires=1937956047&amp;Signature=j8vGlo0gjUs%2FR48d7LpO2Hzcmmk%3D&amp;response-cache-control=Cache-Control%3Amax-age%3D473364000.0%2C%20public&amp;response-expires=473364000.0" defer="defer"></script>

</div> <!-- #application -->


<div class="ReactTrayPortal"><div data-reactid=".1"></div></div></body></html>
    """
    soup=BeautifulSoup(content,'html.parser')
    tag=soup.body.find(class_="student_assignment final_grade")
    grade=""
    for string in tag.stripped_strings
        grade+=(repr(string))
    grade=grade[9]+grade[10]+'%' #orig str is 'total:__%', this returns __%
    class_and_grade[courses[i]]=grade #adds a class:grade pair

    msg = "Grade for CMPE 130"
    msg += grade
    post_message_data( { "roomId": roomid, "markdown": msg } )

    return class_and_grade # returns a dict of class:grade pairs


@post('/')
def index(request):
	r = json.loads(request.body)
	if not r:
	    return "True"

	pprint.pprint(r)

    roomid = r['originalRequest']['data']['data']['roomId']

	action = r['result']['action']

	if action == 'get_grades':
		get_grades()

	if action == 'classes':
		get_classes()

	if action == 'get_announcement':
		get_announcement()

    return True


if __name__ == "__main__":

	run_itty(server='wsgiref', host='0.0.0.0', port=8080)
