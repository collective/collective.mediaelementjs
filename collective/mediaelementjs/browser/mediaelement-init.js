/*jslint browser: true*/
/*global $, jQuery, define*/

/* global require */

if(window.jQuery){
  define('jquery', function(){
    return window.jQuery;
  });
}

require([
  'jquery',
  'mediaelementjs',
  ], function($, m) {
  'use strict';

  $(document).ready(function(){

    $('video,audio').mediaelementplayer();

  });
});
