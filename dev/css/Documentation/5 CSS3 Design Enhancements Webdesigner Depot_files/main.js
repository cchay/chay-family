var isWddIpadDevice = false;
jQuery(document).ready(function(){
  
  jQuery('pre').each(function(i, e) {hljs.highlightBlock(e)});
  
  isWddIpadDevice = navigator.userAgent.match(/iPad/i);

  initIpad();
  
  initFooterAnimation();
  initPopularSwitcher();
  initAds();
  initScrolling();
 
  initSearchForm();
  
  if(!!document.createElement('canvas').getContext)
    initCanvas();
 
  
  generateNoise(0.1, '.sidebar-banner-container', 140);
  generateNoise(0.1, '.sidebar-grey-container', 140);
  
  
  
  initQuotes();
  initMciPosts();
  
  //initParalax();
  
  initFooterSections();
  initPopularListSwitcher();
  
  initFooterForm();
  initMainMenuSelect();
  
  
  initFloatWddBar();
  
  if(getWddInternetExplorerVersion() == 10){
    is_ie_10 = true;
    jQuery('head').append('<link rel="stylesheet" href="http://www.webdesignerdepot.com/wp-content/themes/wdd_new/css/ie.css" type="text/css" />');
  }
  
  initRollLinks();
  initLoadMoreMobile();
  initMobileLogic();
  
  initSocialStubs()
  initMdPopup();
  checkPoll();
  
  if (navigator.userAgent.indexOf("Firefox")!=-1)
    initFixingFF();
    
  
  initSafariFixes();  
  
  
});

function openSuPopup(url){
  window.open('http://www.stumbleupon.com/badge/?url=' + url, 'StumbleUpon', 'target=_blank,width=434,height=360, left=0, top=100 ');
}

var wddFacebookJsLoaded = false;
function initSocialStubs(){
  jQuery('.fb-stub').mouseenter(function(){
    
    var link = jQuery(this);
    var fbLink = jQuery('<fb:like href="'+ link.attr('href') +'"  send="false" layout="button_count" width="70" show_faces="true" font=""></fb:like>');
    link.replaceWith(fbLink);
    var parent = fbLink.parent()[0];
    if(wddFacebookJsLoaded)
      FB.XFBML.parse(parent);


    if(!wddFacebookJsLoaded)
      initFacebookJs();
    
  });
}

function initFacebookJs(){
  var d = document;
  var s = 'script';
  var id = 'facebook-jssdk';
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=527303500614036";
  fjs.parentNode.insertBefore(js, fjs);
  wddFacebookJsLoaded = true;
  
}

function isWddSafari(){
  return navigator.userAgent.indexOf("Safari") > -1;
}

function isWddChrome(){
  return navigator.userAgent.indexOf("Chrome") > -1;
}

function initSafariFixes(){
  if(!isWddSafari() || isWddChrome() )
    return;
    
  var style = jQuery('<style>#header-menu-wrap { overflow:auto; }</style>')
  jQuery('html > head').append(style);
}


function checkContactForm(jform){
  var form = jQuery(jform);
  
  var error = '';
  var name = form.find('[name=your-name]').val();
  if(!name)
    error += "Please enter your name\n";
    
  var email = form.find('[name=your-email]').val();
  if(!validateEmailForWdd(email))
    error += "Please enter a valid email address\n";
    
  var subject = form.find('[name=your-subject]').val();
  if(!subject)
    error += "Please enter the subject\n";
    
  var msg = form.find('[name=your-message]').val();
  if(!msg)
    error += "Please enter a message";
    
  var codeA = parseInt ( form.find('[name=codeA]').val() );
  var codeB = parseInt ( form.find('[name=codeB]').val() );
  var code =  parseInt (form.find('[name=code]').val() );
  if(codeA + codeB != code)
    error += "\nYou did not answer the captcha question correctly";
    
  if(error){
    alert(error);
    return false;
  }
  
  jQuery('.ajax-loader').css('visibility', 'visible');
  var formData = form.serialize();
  jQuery.ajax({url: form.attr('action'), type: "POST", data: formData,
    success: function(data){
      alert(data);
      jQuery('.ajax-loader').css('visibility', 'hidden');
      form.find('[name=your-name]').val('');
      form.find('[name=your-email]').val('');
      form.find('[name=your-subject]').val('');
      form.find('[name=your-message]').val('');
      
      form.find('[name=code]').val('');
    }
  
  });
  
  
  return false; 
}


function initMobileLogic(){
  
  if( jQuery('.wdd-mobile-body').length < 1)
    return;


  var mstr1 = '@webdesign';
  var mailtoStr = 'mai' + 'lto:info'+ mstr1  +'erdepot.com';
  jQuery('.m-contact-link').each(function(i,e){
    var link = jQuery(e);
    link.attr('href', mailtoStr);
  });

  jQuery('.m-contact-option').each(function(i,e){
    var option = jQuery(e);
    option.val(mailtoStr);
  });

}

function initFixingFF(){
  jQuery('.mci-bottom').css({ 'position': 'relative', 'margin-top' : '-10px' });
  jQuery('.main-column-item-wrap').css('padding', '0px');
  setTimeout(fixFFMcBottom, 50);
}

function fixFFMcBottom(){
jQuery('.mci-bottom').each(function(i,e){
    var item = jQuery(e);
    var itemHeight = item.outerHeight();
    var wrap = item.closest('.main-column-item-wrap');
    var postArea = jQuery(item.parent().find('.mci-post-area')[0]);
    var postAreaBottom = postArea.offset().top + postArea.outerHeight();
    var wrapBottom = wrap.offset().top + wrap.outerHeight();
    var itemBottom = item.offset().top +  itemHeight;
    
    /*var delta = itemBottom - postAreaBottom;
    item.css('margin-top', -40 + delta);
    itemBottom = item.offset().top +  itemHeight;
    */
    var deltaR = wrapBottom - itemBottom;
    if(deltaR > 1)
      item.css('top', (deltaR - 1) + 'px' );
    
  });
}


var mobilePreloaderInterval;
var mobilePreloaderBlock;

var mobileLoadedPosts;
var mobileAddPostsInterval;

/* PARALAX */
(function($){
	$.fn.plaxmove = function(options) {

		this.defaults = {
			ratioH: 0.2,
			ratioV: 0.2,
			invertH: false,
			invertV: false,
			reversed: false
		}

		var settings = $.extend({},this.defaults,options),
			layer = $(this),
			center = {
				//x: $('html').width()/2-layer.width()/2,
				//y: $('html').height()/2-layer.height()/2
        x: $(window).width()/2-layer.width()/2
				//y: $(window).height()/2-layer.height()/2
			},
			y0 = layer.offset().top,
			//x0 = layer.offset().left;
      x0 = layer.position().left;

		if(settings.reversed) {

			if(settings.invertH)
				var eqH = function(e) {
					return x0-(e.pageY - center.y)*settings.ratioH
				}

			else 
				var eqH = function(e) {
					return x0+(e.pageY - center.y)*settings.ratioH
          
				}

			if(settings.invertV)
				var eqW = function(e) {
					return y0-(e.pageX - center.x)*settings.ratioV
				}
			else
				var eqW = function(e) {
					return y0+(e.pageX - center.x)*settings.ratioV
				}

		}

		else {

			if(settings.invertH)
				var eqH = function(e) {
					return x0-(e.pageX * 0.5 - center.x)*settings.ratioH
          
				}

			else 
				var eqH = function(e) {
          
					return x0+(e.pageX * 0.5 - center.x)*settings.ratioH
          
				}

			if(settings.invertV)
				var eqW = function(e) {
					return y0-(e.pageY - center.y)*settings.ratioV
				}
			else
				var eqW = function(e) {
					return y0+(e.pageY - center.y)*settings.ratioV
				}		

		}

		$('html').bind('mousemove', function(e) {

        if(e.pageY <= 306){
          if(wddParallaxDisabled)
        	  return;
            
				  x = eqH(e);
          $(layer).css({left:x})
          
        }

		})

	};
})(jQuery);

function initLoadMoreMobile(){
  var mobilePage = 1;
  var loadMobileBtn = jQuery('#load-more-mobile');
  var leftColumn = jQuery('.mobile-left-column');
  var rightColumn = jQuery('.mobile-right-column');
  mobilePreloaderBlock = jQuery('#mobile-preloader');
  var mobilePreloaderLabel = jQuery('#lmb-label');
  
  
  var url = loadMobileBtn.attr('data-url');
  loadMobileBtn.click(function(){
    startMobilePreloader();
    
    mobilePreloaderLabel.css('visibility','hidden');
    
    jQuery.getJSON( url, {page: mobilePage }, function(data){
        mobilePage++;
        mobileLoadedPosts = data;
        
        if( !mobileLoadedPosts || mobileLoadedPosts.length < 1 ){
           jQuery('#mobile-lmb-block').hide();
           return;
        }
       
        addMobileLoadedPost();
        mobileAddPostsInterval = setInterval(addMobileLoadedPost, 50);
        
        stopMobilePreloader();
        
        mobilePreloaderLabel.css('visibility','visible');
    });
    
    return false;
  });
}

function addMobileLoadedPost(){
  
  
  var leftColumn = jQuery('.mobile-left-column');
  var rightColumn = jQuery('.mobile-right-column');
    
  var item = mobileLoadedPosts.shift();
  
  var postHtml = wdd_base64_decode(item['postHtml']);
  if(rightColumn.outerHeight() < leftColumn.outerHeight() )
     rightColumn.append(postHtml);
  else
     leftColumn.append(postHtml);
     
  if( mobileLoadedPosts.length <= 0 ){
    clearInterval(mobileAddPostsInterval);
    return;
  }  
  
}



function startMobilePreloader(){
  mobilePreloaderBlock.show();
  mobilePreloaderInterval = setInterval(animateMobilePreloader, 150);
}

function stopMobilePreloader(){
  mobilePreloaderBlock.hide();
  clearInterval(mobilePreloaderInterval);
}

function animateMobilePreloader(){
  var preloaderStepsCount = 3;
  var activeStep = jQuery('#mobile-preloader .active')
  var index = activeStep.index('#mobile-preloader span');
  index++;
  if(index >= preloaderStepsCount)
    index = 0;
  var newItem = jQuery('#mobile-preloader span').eq(index);
        
  jQuery('#mobile-preloader span').removeClass('active');
  jQuery(newItem).addClass('active');
}

function wddIsPad(){
  return navigator.userAgent.match(/iPad/i);
}

function initIpad(){
  
  if(wddIsPad() ) { 
     jQuery("div.menu-item").each(function(i,e){
       var menuItem = jQuery(e);
       var mobileRef = jQuery('<a>').addClass('mi-mobile-a').attr('href','javascript:;');
       menuItem.append(mobileRef);
       
    });
  
    
  }
}

function hideIpadSubmenu(){
  jQuery('.submenu-item').hide(); 
}

function initRollLinks(){
  if( typeof is_ie_lte9 !== 'undefined' || typeof is_ie_10 !== 'undefined' )
    return;
    
  jQuery('.entry-content a, .page-entry-content a, .ftb-text a, .author-bio-text a, .entry p a').each(function(i,e){
     var link = jQuery(e);
     if(  !link.html().match(/<img/gi) ){
       link.addClass('roll-link');
       link.html('<span data-title="'+ link.text() +'">' + link.html() + '</span>');
     }
  });
}

function getWddInternetExplorerVersion(){
// Returns the version of Internet Explorer or a -1
// (indicating the use of another browser).
  var rv = -1; // Default value assumes failure. 
  var ua = navigator.userAgent;

  // If user agent string contains "MSIE x.y", assume
  // Internet Explorer and use "x.y" to determine the
  // version.
 
  var re  = new RegExp("MSIE ([0-9]{1,}[\.0-9]{0,})");
  if (re.exec(ua) != null) 
    rv = parseFloat( RegExp.$1 );
  return rv;
}


function initFloatWddBar(){
  
  var plusLnk = jQuery('.plus-floatbar-lnk');
  
  if(wddIsPad() ){
    plusLnk.hide();
    return;
  }

  var leftSidebar = jQuery('#left-sidebar');
    
  jQuery('.left-sidebar-close-lnk').click(function(){
    closeLeftSidebar();
    return false;
  });
  
  
  var leftSidebarScroller = jQuery('#left-sidebar-scroller');
  var initiated = false;
  
  var floatBarVisible = WDD_Popup_Get_Cookie( 'floatBarVisible');
  if(floatBarVisible > 0){
    leftSidebar.css('display', 'block'); 
    jQuery('.plus-floatbar-lnk .psl-plus').hide();
    jQuery('.plus-floatbar-lnk .psl-min').show();
    initFloatBar();
    initiated = true;
  }
  
  
  
  plusLnk.click(function(){
  
      
    if(leftSidebar.css('display') == 'none' ){
    
      leftSidebar.css('display', 'block');
      
    
      jQuery('.plus-floatbar-lnk .psl-plus').hide();
      jQuery('.plus-floatbar-lnk .psl-min').show();
      
      WDD_Popup_Set_Cookie( 'floatBarVisible', 1 , 365, '/' );
      if(!initiated){
        initFloatBar();
        initiated = true;
      }
      
    }
    else{
    
      
      closeLeftSidebar();
    }
     
    
    return false;
  });
 
}




function initFloatBar(){
  var leftSidebar = jQuery('#left-sidebar');
  var leftSidebarScroller = jQuery('#left-sidebar-scroller');
  var leftSidebarTop = 0;
  
        var left = 0;
        var top = 0;
        
        
        
        var floatBarLeft = WDD_Popup_Get_Cookie( 'floatBarLeft');
        var floatBarTop = WDD_Popup_Get_Cookie( 'floatBarTop');
        if(floatBarLeft && floatBarTop){
          left = floatBarLeft; 
          if(floatBarTop >= jQuery(window).height() )
            top = jQuery(window).height() * 0.5 - leftSidebar.height() * 0.5;
          else
            top = floatBarTop;
          
        }
        else{
          left = jQuery(window).width() * 0.5 - leftSidebar.width() * 0.5;
          
        }
        
         
        
        
        
        var cssData = {  'left': (left + 'px'), 'top' : (top + 'px') };
        
        var height = 310;
        var floatBarWidth = WDD_Popup_Get_Cookie( 'floatBarWidth');
        var floatBarHeight = WDD_Popup_Get_Cookie( 'floatBarHeight');
        
        
        var bottomPadding = 70;
        if( floatBarHeight > 0 ){
          height = parseInt(floatBarHeight);
          leftSidebarScroller.css('height', (height - bottomPadding) + 'px' );
        }
     
        cssData['height'] = height + 'px';
        
        if(floatBarWidth > 0){
          cssData['width'] = floatBarWidth + 'px';
          leftSidebarScroller.css('width', (parseInt(floatBarWidth) + 21) + 'px' ); 
        }
        
        leftSidebar.css( cssData );
        
        if(leftSidebar && leftSidebar.position())
          leftSidebarTop = leftSidebar.position().top;
        
        // refactor this ???
        try{
          //*
          leftSidebar.draggable({
            drag: function(event, ui){
              var top = getTopWddDrag(ui.helper);
              ui.helper.css('position', 'fixed');
              ui.helper.css('top', top+"px");
              leftSidebarTop = top;//ui.position.top;
              
            },
            
            stop: function(event, ui){
              var top = getTopWddDrag(ui.helper);
              ui.helper.css('position', 'fixed');
              ui.helper.css('top', top+"px"); 
              
              WDD_Popup_Set_Cookie( 'floatBarTop', top , 365, '/' );
              WDD_Popup_Set_Cookie( 'floatBarLeft', ui.position.left , 365, '/' );
              leftSidebarTop = top;//ui.position.top;
             
            }
          
          });
          
          leftSidebar.resizable({
            maxHeight: 450,
            minWidth:280,
            minHeight:150,
            resize: function( event, ui ){
              leftSidebar.css("top", leftSidebarTop + 'px' );
              leftSidebarScroller.css('width', (ui.size.width + 31) + 'px' );
              leftSidebarScroller.css('height', (ui.size.height - bottomPadding) + 'px' );
            }
            ,
            stop: function(event, ui){
              leftSidebar.css("top", leftSidebarTop + 'px' );
              leftSidebar.css('position', 'fixed');
              
              WDD_Popup_Set_Cookie( 'floatBarWidth', ui.size.width , 365, '/' );
              WDD_Popup_Set_Cookie( 'floatBarHeight', ui.size.height , 365, '/' );
              leftSidebar.css("top", leftSidebarTop + 'px' );
            }
          
          });
          //*/
        }
        catch(err){
        
        }
      
      
      // init float swithcer
      jQuery('#float-switcher a').click(function(){
        var ref = jQuery(this);
        var index = jQuery(ref).attr('section-index');//  index('#float-switcher a');
        var newItem = jQuery('#left-sidebar-scroller .left-sidebar-block').eq(index);
        
        jQuery('#float-switcher a').removeClass('active');
        jQuery('#left-sidebar-scroller .left-sidebar-block').hide();
        
        ref.addClass('active');
        newItem.show();
        
        return false;
        
    
      });  
      
      initFloatRelatedSection();
      
}

function getTopWddDrag(ele)
{
    var eTop = ele.offset().top;
    var wTop = $(window).scrollTop();
    var top = eTop - wTop;

    return top; 
}

var floatRelatedDic = {};
var floatRelatedIndex = 0;

function initFloatRelatedSection(){
  
  var relatedIdIndex = 0;
  
  var title = jQuery('.new-single-title');
 
  addFloatRelatedRef(title, title.html(), 'h1');
  
  jQuery('.entry-content h2, .entry-content h3').each(function(i,e){
    var header = jQuery(e);
   
    
    addFloatRelatedRef(header, header.html(),   header[0].tagName.toLowerCase());
    
    
  });
  
  var comments = jQuery('#comments_section');
  addFloatRelatedRef(comments,'Comments',   'h1');
  
}

function addFloatRelatedRef(scrollToTarget, title, fcrClass){
  var section = jQuery('#float-bar-current-section');
  floatRelatedIndex++;
  var currentDiv = jQuery('<div>').addClass('left-sidebar-entry');
  var currentRef = jQuery('<a>').addClass('fcr-' +fcrClass ).html(title );
  
  var newId = 'fcr-id-' + floatRelatedIndex;
  floatRelatedDic[newId] = scrollToTarget;
  currentRef.attr('id', newId);
  
  currentRef.click(relatedScrolling);
  currentDiv.append(currentRef);
  section.append(currentDiv);

}

function relatedScrolling(e){
    
    var ref =  jQuery(this);
    var id = ref.attr('id');
    var targetScroll = floatRelatedDic[id];
    
    if(targetScroll)
      jQuery.scrollTo(targetScroll, 200, {offset: {top: -55 } });
    
    return false;
}

function closeLeftSidebar(){
  WDD_Popup_Set_Cookie( 'floatBarVisible', 0 , 365, '/' );
  var leftSidebar = jQuery('#left-sidebar');
  var plusLnk = jQuery('.plus-floatbar-lnk');
  leftSidebar.css('display', 'none');
  
  jQuery('.plus-floatbar-lnk .psl-plus').show();
  jQuery('.plus-floatbar-lnk .psl-min').hide();
}


function initMainMenuSelect(){
  var menuSelect = jQuery('#main-menu-select');
  menuSelect.change(function(){
    var ref = menuSelect.val();
    if(ref)
      window.location = ref;
  });
}


var isWddMobileDevice = {
    Android: function() {
        return navigator.userAgent.match(/Android/i);
    },
    BlackBerry: function() {
        return navigator.userAgent.match(/BlackBerry/i);
    },
    iOS: function() {
        return navigator.userAgent.match(/iPhone|iPad|iPod/i);
    },
    Opera: function() {
        return navigator.userAgent.match(/Opera Mini/i);
    },
    Windows: function() {
        return navigator.userAgent.match(/IEMobile/i);
    },
    any: function() {
        return (isWddMobileDevice.Android() || isWddMobileDevice.BlackBerry() || isWddMobileDevice.iOS() || isWddMobileDevice.Opera() || isWddMobileDevice.Windows());
    }
};

function initMdPopup(){
  if( isWddMobileDevice.any() )
    return;
  
  
  
  var mdPopupPagesVisits = WDD_Popup_Get_Cookie('md_popup_page_visits');
  if(!mdPopupPagesVisits)
    mdPopupPagesVisits = 1;
  else
    mdPopupPagesVisits = 1 + parseInt(mdPopupPagesVisits);
  
  
  WDD_Popup_Set_Cookie('md_popup_page_visits', mdPopupPagesVisits, 0, '/' );
  
  if(mdPopupPagesVisits >= 10 && !WDD_Popup_Get_Cookie('md_popup_done') && !WDD_Popup_Get_Cookie('md_popup_week') ){
    jQuery('body').append('<a href="/wp-content/plugins/md-popup/iframe_n.html" class="md-popup-link" style="display:none"></a>');
    loadFancyBoxLibrary();
    //initMdPopupFancy();
    setTimeout('activateMdPopupFancy()', 2000);
    
  }
}

function loadFancyBoxLibrary(){
  var oHead = document.getElementsByTagName('HEAD').item(0);
  var oScript= document.createElement("script");
  oScript.type = "text/javascript";
  oScript.src="/wp-content/themes/wdd_new/fancybox/jquery.fancybox-1.3.4.pack.js";
  oHead.appendChild( oScript);
  
  var cssLink = document.createElement('link');
  cssLink.rel = 'stylesheet';
  cssLink.type = 'text/css';
  cssLink.href = '/wp-content/themes/wdd_new/fancybox/jquery.fancybox-1.3.4.css';
  oHead.appendChild( cssLink);

}

function activateMdPopupFancy(){

jQuery('.md-popup-link').fancybox({
       'width' : 920,
			 'height' : 425,
			 'autoScale' : false,
			 'transitionIn' : 'none',
			 'transitionOut' : 'none',
			 'type' : 'iframe',
			 'padding': 0,
			 'overlayColor': '#333',
       'centerOnScroll': true,
			 onClosed: function(){
        WDD_Popup_Set_Cookie('md_popup_week', 1, 7, '/' );	
       },
       onComplete: function(){
         jQuery.ajax({ type: 'POST', url: '/wp-content/plugins/md-popup/ajax/wp-api.php' , data: {'imp' : 1 } });
       }
  });
  
  jQuery('.md-popup-link').click();

}

function initFooterForm(){

   var subscribeField = jQuery('#footer-subscribe-email'); 
   subscribeField.focus(function(){
     if(subscribeField.hasClass('inactive')){
       subscribeField.removeClass('inactive')
       subscribeField.val('');
     }
   });
   
   jQuery('#footer-subscribe-form').submit(function(){
      var actionUrl = jQuery('#footer-subscribe-form').attr('action');
      var email = jQuery('#footer-subscribe-email').val();
      
      if(!validateEmailForWdd(email)){
        alert('Please enter a valid email address');
        return false;
      }
      
      var wdd_chk = jQuery('#wdd_newsletter_chk').is(':checked');
      var md_chk = jQuery('#md_newsletter_chk').is(':checked'); 
      
      if( !(md_chk || wdd_chk)){
        alert('Please select at least one newsletter');
        return false;
      }
      
      var formData = {'ref' : 'wddblog', 'email' : email.replace('+','%2b')};
      
      if(wdd_chk)
          formData['wdd_newsletter_chk'] = 1;
  
      if(md_chk)
        formData['md_newsletter_chk'] = 1;
    
      jQuery.ajax({
        url: actionUrl,
        data: formData,
        success: function(){
           jQuery('#footer-subscribe-email').val('');
           alert('Thank you! Please check your email for the confirmation link. ');
        }
      });
      
      return false;
   });
}

function validateEmailForWdd(email){ 
 var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/ 
 return email.match(re) 
}

function initAllCategoriesPage(){
  jQuery('.hc-child-lnk-wrap').mouseenter(function(){
    var lnk = jQuery(this);
    var categoryPosts = lnk.find('.hc-categories-posts');
    categoryPosts.css('left', (-categoryPosts.width() + lnk.width() ) * 0.5 );
    categoryPosts.stop();
    categoryPosts.delay(1000).queue(function (){categoryPosts.show(); });
    //fadeIn(1);//, function(){ /*categoryPosts.show();*/ console.log('eee') } );
  });
  
  jQuery('.hc-child-lnk-wrap').mouseleave(function(){
     var categoryPosts = jQuery(this).find('.hc-categories-posts');
     categoryPosts.stop();
     categoryPosts.hide();//delay(50).queue(function (){categoryPosts.hide(); });//hide();
  });
}

function initHomeThumbs(){
   jQuery('.mc-item-img-lnk').each(function(i,e){
      var lnk = jQuery(e);
      var img = jQuery(lnk.find('.mc-item-css-image')[0]);
      lnk.mousemove(function(e){
        
        var element = jQuery(e.currentTarget);
        var deltaWdith = img.innerWidth() - element.innerWidth(); 
        if(element.innerWidth() >= img.innerWidth() )
        
          return;
          
        var deltaX = Math.round(e.pageX - element.offset().left);
        
        //var distance = e.pageY - $(this).offset().top;
            // Get the percentage value with respect to the Mouse Y on the 'menu_holder'.
        var percentage = deltaX / element.innerWidth();
        
        percentage = 1 - percentage;
            // Calculate the new Y position of the 'slider'.
        //var targetY = -Math.round(($("#slider").height() - $(this).height()) * percentage);
            // With jQuery easing funtion from easing plugin.
        img.css('left', 'auto');
        img.animate({right: [ - Math.round(percentage * deltaWdith) + "px", "easeOutCirc"]}, { queue:false, duration:200 });
            
      
      }); 
   });
}





function initFooterSections(){
   if(isWddIpadDevice)
    jQuery('.footer-block').removeClass('ft-anim-block');
  
  
  jQuery('.footer-block-content').mouseenter(function(){
      
      var footerTitle = jQuery(this).find('.footer-title')
      
      if(isWddIpadDevice){
        footerTitle.css({ top: '-300px'});
      }
      else{
        footerTitle.stop().animate( { top: '-300px'},400, 'easeOutCirc');
      }
      
      
    
      
      var block = jQuery(this);
      
      var text = block.find('.ftb-text');
      var footerMenu = jQuery('#footer-menu');
      var footerMenuHeight = footerMenu.innerHeight();
      text.css('top', footerMenuHeight );
      text.css('visibility', 'visible');
      
      
      
      var textHeight = text.height();
      // vertical center
      var deltaTop = Math.round( (footerMenuHeight - textHeight) * 0.5 ) - 20;
      
      if(isWddIpadDevice){
       text.css({ top: deltaTop + 'px' });
       return;
      }
      
      text.stop().animate({ top: deltaTop + 'px' }, 400, 'easeOutCirc');
    
      
  });
  
  jQuery('.footer-block-content').mouseleave(function(){
    
      var footerTitle = jQuery(this).find('.footer-title');
      if(isWddIpadDevice){
        footerTitle.css({ top: '-58px'}); 
      }
      else
        footerTitle.stop().animate( { top: '-58px' }, 400, 'easeInCirc');
      
      var block = jQuery(this);
      var text = block.find('.ftb-text');
     
      var footerMenu = jQuery('#footer-menu');
      
      if(isWddIpadDevice){
       text.css({ top: footerMenu.innerHeight() + 'px', 'visibility': 'hidden' });
       return;
      }
      
      text.stop().animate({ top: footerMenu.innerHeight() + 'px' }, 400, 'easeInCirc', function(){
        text.css('visibility', 'hidden');
      }) ;
      
     
      
  });
}

wddParallaxDisabled = false;
function initParalax(){
  
  wddParallaxDisabled = WDD_Popup_Get_Cookie('parallaxEffectDisabled');

  jQuery('#anim-header div').bind("contextmenu",function(e){
    var texting = "Disable parallax effect?";
    if(wddParallaxDisabled)
      var texting = "Enable parallax effect?";

    var confirmation = confirm(texting);
    if(confirmation)
      wddParallaxDisabled = !wddParallaxDisabled;

    if(wddParallaxDisabled)
      WDD_Popup_Set_Cookie( 'parallaxEffectDisabled', 1  , 365, '/' );
    else
      WDD_Popup_Set_Cookie( 'parallaxEffectDisabled', 1  , -1, '/' );

    return false;
  }); 
  

  jQuery('#grey-spheres').plaxmove({ratioH:0.04,ratioV:0.01})
  jQuery('#color-spheres-2').plaxmove({ratioH:0.05,ratioV:0.02, invertH: true})
  jQuery('#color-spheres').plaxmove({ratioH:0.06,ratioV:0.03})
  jQuery('#small-stuff').plaxmove({ratioH:0.07,ratioV:0.04, invertH: true})
  jQuery('#tiny-stuff').plaxmove({ratioH:0.08,ratioV:0.04, invertH: false})
}

function initMciPosts(){
  jQuery('.mci-post-area').each(function(i,e){
    var postArea = jQuery(this);
    var excerpt = jQuery(postArea.find('.mc-item-excerpt')[0]);
    var postAreaOffset = postArea.offset();
    var excerptOffset = excerpt.offset();
    if(!excerptOffset)
      return;
      
      
      
    postAreaBottom = postAreaOffset.top + postArea.height();
    excerptHeight = excerpt.height();
    excerptBottom = excerptOffset.top + excerptHeight;
    deltaHeight = (excerptBottom - postAreaBottom);
    
    var bottomPadding = 90;
    
    if( navigator.userAgent.indexOf("Firefox") == -1 ){
      var colItemWrap = postArea.closest('.main-column-item-wrap');
      var mciBottom = jQuery(postArea.parent().find('.mci-bottom')[0]);
      var bottomDelta = mciBottom.offset().top -  postAreaBottom ;
      deltaHeight -= bottomDelta;
      //bottomPadding =  bottomPadding - bottomDelta;
      //colItemWrap.css('padding-bottom',  bottomPadding );
    }
    
    
    
    excerpt.height( excerptHeight - deltaHeight);
    //try {
    excerpt.ellipsis();
    //}
    //catch(e){
    //}
    
    excerpt.css('height', 'auto');
    postArea.addClass('mpa-handled');
    
    var sharedWidget = jQuery(postArea.find('.share-widget-wrap')[0]);
   
    
  });
}


function initQuotes(){
  var itemsCount = jQuery('#quotes-items .quote-item').length;
  
  var qItems = jQuery('#quotes-items');
  
  //jQuery('#sb-widget-title-label').click(function(){ qItems.click() });
  
  jQuery('#sb-widget-title-label,#quotes-authors,#quotes-items').click(function(){
    var activeQuote = jQuery('#quotes-items .active');
    var prevQuote = activeQuote;
    var index = jQuery(activeQuote).index('#quotes-items .quote-item');
    index++;
    if(index >= itemsCount)
      index = 0; 
    
    qItems.css('height', activeQuote.height() + 'px');
    
    activeQuote.removeClass('active');
    
    
    var newItem = jQuery('#quotes-items .quote-item').eq(index);
    
    var newItemHeight = newItem.height();
    
    
    newItem.addClass('active');
    
    jQuery('#quotes-authors .active').removeClass('active');
    var newAuthors = jQuery('#quotes-authors .quote-author').eq(index);
    newAuthors.addClass('active');
    
  
    
    newItem.data.scrollingInitiated = true;
    
    var animationType = Math.floor((Math.random()*3)+1);
    
    // always fading effect, for now
    
    qItems.animate({'height' : newItemHeight }, 500);
    
    animationType = 2;
    if(animationType == 1){
      prevQuote.slideUp(500);
      newItem.css('top', '125px');
    
      newItem.show();
      newItem.animate( {'top':'0px'}, 500);
    }
    else if(animationType == 2){
      
      newItem.hide();
      
      prevQuote.fadeOut(500, function(){ } );
      newItem.fadeIn(500);
    }
    else if(animationType == 3){
     
      newItem.show();
      newItem.css({'left' : '410px'});
      prevQuote.show();
      prevQuote.animate({'left' : '-410px'}, 500, function(){ prevQuote.css({ 'left' : 0, 'display': 'none' }) } );
      newItem.animate({'left' : '0'}, 500, function(){  } );
     
    }
    
  });
  
    
}



function initCanvas(){
  
  jQuery('.left-corner-canvas').each(function(i,e){
     var context = e.getContext("2d");
     drawLeftTriangle(context);
  });
  
  jQuery('.right-corner-canvas').each(function(i,e){
     var context = e.getContext("2d");
     drawRightTriangle(context);
  });
  
  jQuery('.comment-trian-canvas').each(function(i,e){
     var context = e.getContext("2d");
     drawCommentTriangle(context);
  });
  
  jQuery('.fbc-mark').each(function(i,e){
     var context = e.getContext("2d");
     drawCommentBlockTriangle(context);
  });
  
  

  
  jQuery('.switcher-trian').each(function(i,e){
     var context = e.getContext("2d");
     drawSwitcherTriangle(context);
  });
  
  
  jQuery('.side-corner-canvas').each(function(i,e){
     var context = e.getContext("2d");
     drawSideTriangle(context);
  });
  
  jQuery('.blockquote-canvas').each(function(i,e){
     var context = e.getContext("2d");
     drawBlockquoteTriangle(context);
  });
  
   jQuery('.submenu-triangle').each(function(i,e){
     var context = e.getContext("2d");
     drawSubmenuTriangle(context);
  });
  
  jQuery('.hcp-triangle').each(function(i,e){
     var context = e.getContext("2d");
     drawHcpTriangle(context);
  });
  
  jQuery('.quote-triangle').each(function(i,e){
     var context = e.getContext("2d");
     drawQuoteTriangle(context);
  });
  
}

function drawQuoteTriangle(context){
  context.beginPath();
  context.moveTo(0, 0);        // Top Corner
  context.lineTo(20, 20);         // Bottom Left
  context.lineTo(20,0); // Bottom Right
  context.fillStyle = "#ffffff";
  context.fill();
  context.closePath();
  
  
  context.beginPath();
  context.moveTo(0, 0);        // Top Corner
  context.lineTo(20, 20);         // Bottom Left
  context.lineTo(20,0); 
  context.strokeStyle = '#d5d5d5';
  context.lineWidth   = 1;
  context.stroke();
}

function drawHcpTriangle(context){
  context.beginPath();
  context.moveTo(10, 0);        // Top Corner
  context.lineTo(20,10); // Bottom Right
  context.lineTo(0, 10);         // Bottom Left
  context.closePath();
  
  context.strokeStyle = '#dadada'; 
  context.lineWidth   = 1.2;
  
  // Fill the path
  context.fillStyle = "#ffffff";
  context.stroke();
  context.fill();     
}

function drawSubmenuTriangle(context){
  context.beginPath();
  context.moveTo(10, 1);        // Top Corner
  context.lineTo(20,11); // Bottom Right
  context.lineTo(0, 11);         // Bottom Left
  context.closePath();
  
  


  // Fill the path
  context.fillStyle = "#2f2f2f";
  context.fill();
  
  context.beginPath();
  context.strokeStyle = '#b9b9b9';//'rgba(255, 255, 255, 0.5)'; 
  context.lineWidth   = 2;
  context.moveTo(10, 1);        // Top Corner
  context.lineTo(20,11); // Bottom Right
  context.moveTo(10, 1)
  context.lineTo(0, 11);         // Bottom Left
  context.closePath();
  context.stroke();
  
  context.beginPath();
  context.strokeStyle = '#797979';//'rgba(255, 255, 255, 0.5)'; 
  context.lineWidth   = 1;
  context.moveTo(10, 0);        // Top Corner
  context.lineTo(20,9); // Bottom Right
  context.moveTo(10, 0)
  context.lineTo(0, 9);         // Bottom Left
  context.closePath();
  context.stroke();
 
}

function drawCommentBlockTriangle(context){
  
  // Draw a path
  context.beginPath();
  context.moveTo(10, 10);        // Top Corner
  context.lineTo(20,20); // Bottom Right
  context.lineTo(0, 20);         // Bottom Left
  context.closePath();
  context.fillStyle = "#D0D0D0";
  context.fill();
}

function drawBlockquoteTriangle(context){
  
  // Draw a path
  context.beginPath();
  context.moveTo(0, 0);        // Top Corner
  context.lineTo(20,0); // Bottom Right
  context.lineTo(20, 15);         // Bottom Left
  context.closePath();
  

  // Fill the path
  context.fillStyle = "#DD4D42";
  //context.stroke();
  context.fill();
  
  
}


function drawSideTriangle(context){
  
  // Draw a path
  context.beginPath();
  context.moveTo(0, 0);        // Top Corner
  context.lineTo(8,8); // Bottom Right
  context.lineTo(0, 16);         // Bottom Left
  context.closePath();
  
  context.strokeStyle = '#d0d0d0'; // red
  context.lineWidth   = 1.3;

  // Fill the path
  context.fillStyle = "#ffffff";
  context.stroke();
  context.fill();
  
  
}

function drawSwitcherTriangle(context){
  context.beginPath();
  context.moveTo(0, 0);        // Top Corner
  context.lineTo(4,8); // Bottom Right
  context.lineTo(8, 0);         // Bottom Left
  context.closePath();
  
  context.strokeStyle = '#d9d9d9'; // red
  context.lineWidth   = 1.3;

  // Fill the path
  context.fillStyle = "#ffffff";
  context.stroke();
  context.fill();
}

function drawCommentTriangle(context){
  var width = 16;  // Triangle Width
  var height = 8; // Triangle Height
  

  
  // Draw a path
  context.beginPath();
  context.moveTo(0, 0);        // Top Corner
  context.lineTo(8,8); // Bottom Right
  context.lineTo(16, 0);         // Bottom Left
  context.closePath();
  
  context.strokeStyle = '#d0d0d0'; // red
  context.lineWidth   = 1.3;

  // Fill the path
  context.fillStyle = "#ffffff";
  context.stroke();
  context.fill();
  
  
}

function drawLeftTriangle(context){
  var width = 8;  // Triangle Width
  var height = 8; // Triangle Height
  

  // Draw a path
  context.beginPath();
  context.moveTo(8, 0);        // Top Corner
  context.lineTo(8,8); // Bottom Right
  context.lineTo(0, 0);         // Bottom Left
  context.closePath();

  // Fill the path
  context.fillStyle = "#646464";
  context.fill();
 
  
}

function drawTopRightTriangle(context){
  context.beginPath();
  context.moveTo(0, 0);        // Top Corner
  context.lineTo(0,8); // Bottom Right
  context.lineTo(8, 8);         // Bottom Left
  context.closePath();

  // Fill the path
  context.fillStyle = "#d8cc44";
  context.fill();
  
}

function drawRightTriangle(context){
  // Draw a path
  context.beginPath();
  context.moveTo(0, 0);        // Top Corner
  context.lineTo(8,0); // Bottom Right
  context.lineTo(0, 8);         // Bottom Left
  context.closePath();

  // Fill the path
  context.fillStyle = "#646464";//#d8cc44";
  context.fill();
  
}

var autocompleteStuff;
function initSearchForm(){
 
  jQuery('#footer-search').focus(function(){
     var input = jQuery(this);
     if(input.val() == 'Search...'){
        input.val(''); 
        input.removeClass('inactive');
     }
  });
  
  jQuery('#fastsearch').focus(function(){
     var box = jQuery(this);
     if(box.val() == 'Search...'){
        box.val(''); 
        box.removeClass('inactive');
     }
     
     if( jQuery(window).width() <= 683 )
       return;
     
     jQuery('#search-btn-link').hide();
     jQuery('#search-close-link').show();
      
     box.animate({width: '280px' }, function() {
       autocompleteStuff.fixPosition();
     });
     
     
     
  });
  
  jQuery('#fastsearch').focusout(function(){
    var box = jQuery(this);
    
    if(box.val() == ''){
      box.val('Search...'); 
      box.addClass('inactive');
      
      if( jQuery(window).width() <= 683 )
        return;
      jQuery('#search-btn-link').show();
      jQuery('#search-close-link').hide();
      box.animate({width: '170px'});
      
    }
     
  });
  
  jQuery('#fastsearch').keyup(function(){
    var input = jQuery(this);
    var closeBtn = input.parent().find('#search-close-link');
    if(input.val().length > 0 ){
        
        jQuery('#search-btn-link').hide();
        jQuery('#search-close-link').show();
     }
     else{
        jQuery('#search-btn-link').show();
        jQuery('#search-close-link').hide();
        
     }
        
  
    
  });
  
  jQuery('#search-btn-link').click(function(){
    if(jQuery(window).width() < 683) {
        var input = jQuery('#fastsearch');
        input.show();
        jQuery('#fastsearch-wrap').show();
    
        jQuery('#mobile-logo').hide();
        jQuery('#search-btn-link').hide();
        jQuery('#search-close-link').show();
        jQuery('#search-box .mobile-btn-bg').addClass('active');
      
    }
    
    return false;
  });
  
  jQuery('#search-close-link').click(function(){
    var btn = jQuery(this);
    var input = jQuery('#fastsearch');
    
    
    if(jQuery(window).width() < 683) {
        input.css('display', 'none');
        jQuery('#fastsearch-wrap').hide();
        //???jQuery('#main-menu-select').show();
        jQuery('#mobile-logo').show();
        jQuery('#search-btn-link').show();
        jQuery('#search-close-link').hide();
        input.val('Search...');
        input.addClass('inactive');
        jQuery('#search-box .mobile-btn-bg').removeClass('active');
      
    }
    else{
      jQuery('#search-btn-link').show();
      jQuery('#search-close-link').hide();
      input.val('');
      input.focus();
    }
    
    if(autocompleteStuff)
      autocompleteStuff.hide();
    
    
    return false;
  });
  
  var options;
  jQuery(function(){
     options = { 'serviceUrl' : '/wp-content/themes/wdd_new/ajax/predective_search.php',
                  minChars:3,
                  autoSubmit: true };
     autocompleteStuff = jQuery('#fastsearch').autocomplete(options);
  });
}



function initAds(){
  jQuery('#top-ads-block').load('/wp-content/themes/wdd2/ads-rotator-ajax.php');
}

function initPopularSwitcher(){
  jQuery('.popluar-switch-menu a').click(function(){
    var link = jQuery(this);
    var href = link.attr('href');
    var label = link.html();
    console.log(label);
    jQuery.ajax({
      url: href,
      success: function(data){
         jQuery('#popular-posts-container').html(data);
         jQuery('#popular-posts-label').html(label);
         console.log(label);
      }
    });
    
    return false;
  });
}

var closeTopBarLinkIsVisible = false;
function initScrolling(){
  jQuery('#top_link').click(function(){
    var lnk = jQuery(this);
    var id = lnk.attr('href');
    id = id.replace(/.*?#/g,"#");
    var el = jQuery(id);
    jQuery.scrollTo(el, 200);
    return false;
  });
  
  jQuery(window).scroll(function(e){
    var offsetY = jQuery(window).scrollTop(); //e.currentTarget.pageYOffset;
    if(offsetY >= 200 && !closeTopBarLinkIsVisible){
       closeTopBarLinkIsVisible = true;
       jQuery('#nav-bar-close-link').show();
       jQuery('#top_link').show();
    }
    else if(offsetY < 200 && closeTopBarLinkIsVisible ){
      closeTopBarLinkIsVisible = false;
      jQuery('#nav-bar-close-link').hide();
      jQuery('#top_link').hide();
    }
    
    
  });
  
  jQuery('#nav-bar-close-link').click(function(){
    jQuery('#header-menu-wrap').css({ 'position' : 'absolute'});
    if(autocompleteStuff)
      autocompleteStuff.hide();
    return false;
  } );
}


function initFooterAnimation(){
  var coordinatesHash;
  var activeElem;
  var fX, fY;
  var fw = jQuery('#header-content-wrap');
  var arrowVisible = false;
  var arrowPointerLeft; 
  
  var fbcPointer = jQuery('#fbc-mark-wrap');
  jQuery('.footer-block').mouseenter(function(){
     var ftBlock = jQuery(this);
     
     
     
     arrowPointerLeft = ftBlock.position().left + Math.round(ftBlock.width() * 0.5);
     
     if(isWddIpadDevice){
       fbcPointer.css('left', arrowPointerLeft);
       fbcPointer.css('bottom', 0);
       return;
     }
     
     if(arrowVisible){
       fbcPointer.css('bottom', 0);
       fbcPointer.stop().animate({left: arrowPointerLeft}, 600);
       
     }       
     else{
       //fbcPointer.animate({left: arrowPointerLeft}, 600);
       fbcPointer.css('left', arrowPointerLeft);
       fbcPointer.stop().animate({bottom: '0px'}, 600);
       arrowVisible = true;
     }
  });
  
  jQuery('#footer-menu').mouseleave(function(){
    if(isWddIpadDevice){
       //fbcPointer.css('left', arrowPointerLeft);
       fbcPointer.css('bottom', '-10px');
       return;
    }
    fbcPointer.stop().animate({bottom: '-10px'}, 600, function() { arrowVisible = false } );//.animate({left: arrowPointerLeft}, 600); ;
  });
  
  jQuery('#footer-menu').mouseenter(function(){
    //fbcPointer.stop().animate({bottom: '0px'}, 600, function(){ arrowVisible = true } );//.animate({left: arrowPointerLeft}, 600);;
  });
  
  fw.mouseenter(function(e){
    coordinatesHash = new Array();
    fX = e.pageX - fw.offset().left;
    fY = e.pageY - fw.offset().top;
    
    jQuery('#header-content-wrap .alpha-rect').each(function(i,e){
          var rect = jQuery(e);
          var rectPos = rect.position();
          coordinatesHash.push({elem: rect, opacity: parseFloat(rect.css('opacity')), dir:  (Math.random() > 0.5 ? -1 : 1 )  , tlx: rectPos.left, tly: rectPos.top , rbx: rectPos.left + 30, rby : rectPos.top + 30 });
    });
            
  });
  
  
  
  fw.mousemove(function(e){
     var mouseX = e.pageX - fw.offset().left;
     var mouseY = e.pageY - fw.offset().top;
     
     var vX = mouseX - fX;
     var vY = mouseY - fY;
     fX = mouseX;
     fY = mouseY;
     
     var deltaDir = 1;
     if( (vX >=0 && vY >= 0 ) )
      deltdaDir = 1;
     if(vX <=0 && vY <= 0)
      deltdaDir = -1;
    
     
     for (var key in coordinatesHash) {
       var elem = coordinatesHash [key];
       
       
       
       elem.opacity += elem.dir * deltdaDir * 0.01;
      
       
       if(elem.opacity > 1){
        elem.opacity = 1;
        elem.dir = -elem.dir;
       }
       
       if(elem.opacity < 0.8){
        elem.opacity = 0.8;
        elem.dir = -elem.dir;
       }
       
       elem.elem.css('opacity', elem.opacity);
     
    }
    

     
  });
  
 
}

function mouseWithinRect(mouseX, mouseY, elem){
  return mouseX >= elem.tlx && mouseY >= elem.tly && mouseX <= elem.rbx && mouseY <= elem.rby;
}

function generateNoise(opacity, selector, delta) {
   

   var canvas = document.createElement("canvas");
   var ctx;
   
   
   if(typeof G_vmlCanvasManager  != 'undefined' ){
     canvas = G_vmlCanvasManager.initElement(canvas);
   }
   
   if (typeof canvas.toDataURL === 'undefined')
     return;
   
   ctx = canvas.getContext('2d');
   
   var x, y,
   number,
   opacity = opacity || .2;
   
   

   canvas.width = 45;
   canvas.height = 45;

   for ( x = 0; x < canvas.width; x++ ) {
      for ( y = 0; y < canvas.height; y++ ) {
         number = Math.floor( Math.random() * 60 + delta );

         ctx.fillStyle = "rgba(" + number + "," + number + "," + number + "," + opacity + ")";
         ctx.fillRect(x, y, 1, 1);
      }
   }

   
   jQuery(selector).css('background-image', "url(" + canvas.toDataURL("image/png") + ")" );
}


function initPopularListSwitcher(){
  jQuery('.side-menu-switcher a').click(function(){
    var link = jQuery(this);
    var href = link.attr('title');
    jQuery('.side-menu-switcher a').removeClass('active');
    jQuery(link).addClass('active');
  
    jQuery('.side-popular-list').css('display', 'none');
    console.log(href);
    jQuery(href).css('display','block');
    
    return false;
  });
}



function WDD_Popup_Get_Cookie( check_name ) {
	// first we'll split this cookie up into name/value pairs
	// note: document.cookie only returns name=value, not the other components
	var a_all_cookies = document.cookie.split( ';' );
	var a_temp_cookie = '';
	var cookie_name = '';
	var cookie_value = '';
	var b_cookie_found = false; // set boolean t/f default f

	for ( i = 0; i < a_all_cookies.length; i++ )
	{
		// now we'll split apart each name=value pair
		a_temp_cookie = a_all_cookies[i].split( '=' );


		// and trim left/right whitespace while we're at it
		cookie_name = a_temp_cookie[0].replace(/^\s+|\s+$/g, '');

		// if the extracted name matches passed check_name
		if ( cookie_name == check_name )
		{
			b_cookie_found = true;
			// we need to handle case where cookie has no value but exists (no = sign, that is):
			if ( a_temp_cookie.length > 1 )
			{
				cookie_value = unescape( a_temp_cookie[1].replace(/^\s+|\s+$/g, '') );
			}
			// note that in cases where cookie is initialized but no value, null is returned
			return cookie_value;
			break;
		}
		a_temp_cookie = null;
		cookie_name = '';
	}
	if ( !b_cookie_found )
	{
		return null;
	}
}


function WDD_Popup_Set_Cookie( name, value, expires, path, domain, secure ){
// set time, it's in milliseconds
var today = new Date();
today.setTime( today.getTime() );

/*
if the expires variable is set, make the correct
expires time, the current script below will set
it for x number of days, to make it for hours,
delete * 24, for minutes, delete * 60 * 24
*/
if ( expires )
{
expires = expires * 1000 * 60 * 60 * 24;
}
var expires_date = new Date( today.getTime() + (expires) );

document.cookie = name + "=" +escape( value ) +
( ( expires ) ? ";expires=" + expires_date.toGMTString() : "" ) +
( ( path ) ? ";path=" + path : "" ) +
( ( domain ) ? ";domain=" + domain : "" ) +
( ( secure ) ? ";secure" : "" );
}

/**
 * jQuery.ScrollTo - Easy element scrolling using jQuery.
 * Copyright (c) 2007-2009 Ariel Flesler - aflesler(at)gmail(dot)com | http://flesler.blogspot.com
 * Dual licensed under MIT and GPL.
 * Date: 5/25/2009
 * @author Ariel Flesler
 * @version 1.4.2
 *
 * http://flesler.blogspot.com/2007/10/jqueryscrollto.html
 */
;(function(d){var k=d.scrollTo=function(a,i,e){d(window).scrollTo(a,i,e)};k.defaults={axis:'xy',duration:parseFloat(d.fn.jquery)>=1.3?0:1};k.window=function(a){return d(window)._scrollable()};d.fn._scrollable=function(){return this.map(function(){var a=this,i=!a.nodeName||d.inArray(a.nodeName.toLowerCase(),['iframe','#document','html','body'])!=-1;if(!i)return a;var e=(a.contentWindow||a).document||a.ownerDocument||a;return d.browser.safari||e.compatMode=='BackCompat'?e.body:e.documentElement})};d.fn.scrollTo=function(n,j,b){if(typeof j=='object'){b=j;j=0}if(typeof b=='function')b={onAfter:b};if(n=='max')n=9e9;b=d.extend({},k.defaults,b);j=j||b.speed||b.duration;b.queue=b.queue&&b.axis.length>1;if(b.queue)j/=2;b.offset=p(b.offset);b.over=p(b.over);return this._scrollable().each(function(){var q=this,r=d(q),f=n,s,g={},u=r.is('html,body');switch(typeof f){case'number':case'string':if(/^([+-]=)?\d+(\.\d+)?(px|%)?$/.test(f)){f=p(f);break}f=d(f,this);case'object':if(f.is||f.style)s=(f=d(f)).offset()}d.each(b.axis.split(''),function(a,i){var e=i=='x'?'Left':'Top',h=e.toLowerCase(),c='scroll'+e,l=q[c],m=k.max(q,i);if(s){g[c]=s[h]+(u?0:l-r.offset()[h]);if(b.margin){g[c]-=parseInt(f.css('margin'+e))||0;g[c]-=parseInt(f.css('border'+e+'Width'))||0}g[c]+=b.offset[h]||0;if(b.over[h])g[c]+=f[i=='x'?'width':'height']()*b.over[h]}else{var o=f[h];g[c]=o.slice&&o.slice(-1)=='%'?parseFloat(o)/100*m:o}if(/^\d+$/.test(g[c]))g[c]=g[c]<=0?0:Math.min(g[c],m);if(!a&&b.queue){if(l!=g[c])t(b.onAfterFirst);delete g[c]}});t(b.onAfter);function t(a){r.animate(g,j,b.easing,a&&function(){a.call(this,n,b)})}}).end()};k.max=function(a,i){var e=i=='x'?'Width':'Height',h='scroll'+e;if(!d(a).is('html,body'))return a[h]-d(a)[e.toLowerCase()]();var c='client'+e,l=a.ownerDocument.documentElement,m=a.ownerDocument.body;return Math.max(l[h],m[h])-Math.min(l[c],m[c])};function p(a){return typeof a=='object'?a:{top:a,left:a}}})(jQuery);


/*!

    Copyright (c) 2011 Peter van der Spek
    Autoellipsis
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
    
 */(function(a){function m(){if(!d){d=!0;for(var c in b)a(c).each(function(){var d,e;d=a(this),e=d.data("jqae"),(e.containerWidth!=d.width()||e.containerHeight!=d.height())&&f(d,b[c])});d=!1}}function l(a){b[a]&&(delete b[a],b.length||c&&(window.clearInterval(c),c=undefined))}function k(a,d){b[a]=d,c||(c=window.setInterval(function(){m()},200))}function j(){return this.nodeType===3}function i(b){if(b.contents().length){var c=b.contents(),d=c.eq(c.length-1);
 if(d.filter(j).length){var e=d.get(0).nodeValue;e=a.trim(e);if(e==""){d.remove();return!0}return!1}while(i(d));if(d.contents().length)return!1;d.remove();return!0}return!1}function h(a){if(a.contents().length){var b=a.contents(),c=b.eq(b.length-1);return c.filter(j).length?c:h(c)}a.append("");var b=a.contents();return b.eq(b.length-1)}function g(b){var c=h(b);
 if(c.length){var d=c.get(0).nodeValue,e=d.lastIndexOf(" ");e>-1?(d=a.trim(d.substring(0,e)),c.get(0).nodeValue=d):c.get(0).nodeValue="";return!0}return!1}
 function f(b,c){var d=b.data("jqae");d||(d={});var e=d.wrapperElement;e||(e=b.wrapInner("<div/>").find(">div"),e.css({margin:0,padding:0,border:0}));var f=e.data("jqae");f||(f={});var j=f.originalContent;j?e=f.originalContent.clone(!0).data("jqae",{originalContent:j}).replaceAll(e):e.data("jqae",{originalContent:e.clone(!0)}),b.data("jqae",{wrapperElement:e,containerWidth:b.width(),containerHeight:b.height()});var k=b.height(),l=(parseInt(b.css("padding-top"),10)||0)+(parseInt(b.css("border-top-width"),10)||0)-(e.offset().top-b.offset().top),m=!1,n=e;c.selector&&(n=a(e.find(c.selector).get().reverse())),n.each(function(){var b=a(this),d=b.text(),f=!1;if(e.innerHeight()-b.innerHeight()>k+l)b.remove();else{i(b);
 if(b.contents().length){m&&(h(b).get(0).nodeValue+=c.ellipsis,m=!1);while(e.innerHeight()>k+l){f=g(b);if(!f){m=!0,b.remove();break}i(b);
 if(b.contents().length){
 //if(h(b).get(0))
   h(b).get(0).nodeValue+=c.ellipsis;
  }
 else{m=!0,b.remove();break}}c.setTitle=="onEllipsis"&&f||c.setTitle=="always"?b.attr("title",d):c.setTitle!="never"&&b.removeAttr("title")}}})}var b={},c,d=!1,e={ellipsis:"...",setTitle:"never",live:!1};a.fn.ellipsis=function(b,c){var d,g;d=a(this),typeof b!="string"&&(c=b,b=undefined),g=a.extend({},e,c),g.selector=b,d.each(function(){var b=a(this);f(b,g)}),g.live?k(d.selector,g):l(d.selector);return this}})(jQuery)
 
 
/*
 * jQuery Easing v1.3 - http://gsgd.co.uk/sandbox/jquery/easing/
 *
 * Uses the built in easing capabilities added In jQuery 1.1
 * to offer multiple easing options
 *
 * TERMS OF USE - jQuery Easing
 * 
 * Open source under the BSD License. 
 * 
 * Copyright © 2008 George McGinley Smith
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without modification, 
 * are permitted provided that the following conditions are met:
 * 
 * Redistributions of source code must retain the above copyright notice, this list of 
 * conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice, this list 
 * of conditions and the following disclaimer in the documentation and/or other materials 
 * provided with the distribution.
 * 
 * Neither the name of the author nor the names of contributors may be used to endorse 
 * or promote products derived from this software without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 *  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
 *  GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED 
 * AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 *  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
 * OF THE POSSIBILITY OF SUCH DAMAGE. 
 *
*/

// t: current time, b: begInnIng value, c: change In value, d: duration
jQuery.easing['jswing'] = jQuery.easing['swing'];

jQuery.extend( jQuery.easing,
{
	def: 'easeOutQuad',
	swing: function (x, t, b, c, d) {
		//alert(jQuery.easing.default);
		return jQuery.easing[jQuery.easing.def](x, t, b, c, d);
	},
	easeInQuad: function (x, t, b, c, d) {
		return c*(t/=d)*t + b;
	},
	easeOutQuad: function (x, t, b, c, d) {
		return -c *(t/=d)*(t-2) + b;
	},
	easeInOutQuad: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return c/2*t*t + b;
		return -c/2 * ((--t)*(t-2) - 1) + b;
	},
	easeInCubic: function (x, t, b, c, d) {
		return c*(t/=d)*t*t + b;
	},
	easeOutCubic: function (x, t, b, c, d) {
		return c*((t=t/d-1)*t*t + 1) + b;
	},
	easeInOutCubic: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return c/2*t*t*t + b;
		return c/2*((t-=2)*t*t + 2) + b;
	},
	easeInQuart: function (x, t, b, c, d) {
		return c*(t/=d)*t*t*t + b;
	},
	easeOutQuart: function (x, t, b, c, d) {
		return -c * ((t=t/d-1)*t*t*t - 1) + b;
	},
	easeInOutQuart: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return c/2*t*t*t*t + b;
		return -c/2 * ((t-=2)*t*t*t - 2) + b;
	},
	easeInQuint: function (x, t, b, c, d) {
		return c*(t/=d)*t*t*t*t + b;
	},
	easeOutQuint: function (x, t, b, c, d) {
		return c*((t=t/d-1)*t*t*t*t + 1) + b;
	},
	easeInOutQuint: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return c/2*t*t*t*t*t + b;
		return c/2*((t-=2)*t*t*t*t + 2) + b;
	},
	easeInSine: function (x, t, b, c, d) {
		return -c * Math.cos(t/d * (Math.PI/2)) + c + b;
	},
	easeOutSine: function (x, t, b, c, d) {
		return c * Math.sin(t/d * (Math.PI/2)) + b;
	},
	easeInOutSine: function (x, t, b, c, d) {
		return -c/2 * (Math.cos(Math.PI*t/d) - 1) + b;
	},
	easeInExpo: function (x, t, b, c, d) {
		return (t==0) ? b : c * Math.pow(2, 10 * (t/d - 1)) + b;
	},
	easeOutExpo: function (x, t, b, c, d) {
		return (t==d) ? b+c : c * (-Math.pow(2, -10 * t/d) + 1) + b;
	},
	easeInOutExpo: function (x, t, b, c, d) {
		if (t==0) return b;
		if (t==d) return b+c;
		if ((t/=d/2) < 1) return c/2 * Math.pow(2, 10 * (t - 1)) + b;
		return c/2 * (-Math.pow(2, -10 * --t) + 2) + b;
	},
	easeInCirc: function (x, t, b, c, d) {
		return -c * (Math.sqrt(1 - (t/=d)*t) - 1) + b;
	},
	easeOutCirc: function (x, t, b, c, d) {
		return c * Math.sqrt(1 - (t=t/d-1)*t) + b;
	},
	easeInOutCirc: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return -c/2 * (Math.sqrt(1 - t*t) - 1) + b;
		return c/2 * (Math.sqrt(1 - (t-=2)*t) + 1) + b;
	},
	easeInElastic: function (x, t, b, c, d) {
		var s=1.70158;var p=0;var a=c;
		if (t==0) return b;  if ((t/=d)==1) return b+c;  if (!p) p=d*.3;
		if (a < Math.abs(c)) { a=c; var s=p/4; }
		else var s = p/(2*Math.PI) * Math.asin (c/a);
		return -(a*Math.pow(2,10*(t-=1)) * Math.sin( (t*d-s)*(2*Math.PI)/p )) + b;
	},
	easeOutElastic: function (x, t, b, c, d) {
		var s=1.70158;var p=0;var a=c;
		if (t==0) return b;  if ((t/=d)==1) return b+c;  if (!p) p=d*.3;
		if (a < Math.abs(c)) { a=c; var s=p/4; }
		else var s = p/(2*Math.PI) * Math.asin (c/a);
		return a*Math.pow(2,-10*t) * Math.sin( (t*d-s)*(2*Math.PI)/p ) + c + b;
	},
	easeInOutElastic: function (x, t, b, c, d) {
		var s=1.70158;var p=0;var a=c;
		if (t==0) return b;  if ((t/=d/2)==2) return b+c;  if (!p) p=d*(.3*1.5);
		if (a < Math.abs(c)) { a=c; var s=p/4; }
		else var s = p/(2*Math.PI) * Math.asin (c/a);
		if (t < 1) return -.5*(a*Math.pow(2,10*(t-=1)) * Math.sin( (t*d-s)*(2*Math.PI)/p )) + b;
		return a*Math.pow(2,-10*(t-=1)) * Math.sin( (t*d-s)*(2*Math.PI)/p )*.5 + c + b;
	},
	easeInBack: function (x, t, b, c, d, s) {
		if (s == undefined) s = 1.70158;
		return c*(t/=d)*t*((s+1)*t - s) + b;
	},
	easeOutBack: function (x, t, b, c, d, s) {
		if (s == undefined) s = 1.70158;
		return c*((t=t/d-1)*t*((s+1)*t + s) + 1) + b;
	},
	easeInOutBack: function (x, t, b, c, d, s) {
		if (s == undefined) s = 1.70158; 
		if ((t/=d/2) < 1) return c/2*(t*t*(((s*=(1.525))+1)*t - s)) + b;
		return c/2*((t-=2)*t*(((s*=(1.525))+1)*t + s) + 2) + b;
	},
	easeInBounce: function (x, t, b, c, d) {
		return c - jQuery.easing.easeOutBounce (x, d-t, 0, c, d) + b;
	},
	easeOutBounce: function (x, t, b, c, d) {
		if ((t/=d) < (1/2.75)) {
			return c*(7.5625*t*t) + b;
		} else if (t < (2/2.75)) {
			return c*(7.5625*(t-=(1.5/2.75))*t + .75) + b;
		} else if (t < (2.5/2.75)) {
			return c*(7.5625*(t-=(2.25/2.75))*t + .9375) + b;
		} else {
			return c*(7.5625*(t-=(2.625/2.75))*t + .984375) + b;
		}
	},
	easeInOutBounce: function (x, t, b, c, d) {
		if (t < d/2) return jQuery.easing.easeInBounce (x, t*2, 0, c, d) * .5 + b;
		return jQuery.easing.easeOutBounce (x, t*2-d, 0, c, d) * .5 + c*.5 + b;
	}
});






function wdd_base64_decode (data) {
    // http://kevin.vanzonneveld.net
    // +   original by: Tyler Akins (http://rumkin.com)
    // +   improved by: Thunder.m
    // +      input by: Aman Gupta
    // +   improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
    // +   bugfixed by: Onno Marsman
    // +   bugfixed by: Pellentesque Malesuada
    // +   improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
    // +      input by: Brett Zamir (http://brett-zamir.me)
    // +   bugfixed by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
    // -    depends on: utf8_decode
    // *     example 1: base64_decode('S2V2aW4gdmFuIFpvbm5ldmVsZA==');
    // *     returns 1: 'Kevin van Zonneveld'
    // mozilla has this native
    // - but breaks in 2.0.0.12!
    //if (typeof this.window['btoa'] == 'function') {
    //    return btoa(data);
    //}
    var b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    var o1, o2, o3, h1, h2, h3, h4, bits, i = 0,
        ac = 0,
        dec = "",
        tmp_arr = [];

    if (!data) {
        return data;
    }

    data += '';

    do { // unpack four hexets into three octets using index points in b64
        h1 = b64.indexOf(data.charAt(i++));
        h2 = b64.indexOf(data.charAt(i++));
        h3 = b64.indexOf(data.charAt(i++));
        h4 = b64.indexOf(data.charAt(i++));

        bits = h1 << 18 | h2 << 12 | h3 << 6 | h4;

        o1 = bits >> 16 & 0xff;
        o2 = bits >> 8 & 0xff;
        o3 = bits & 0xff;

        if (h3 == 64) {
            tmp_arr[ac++] = String.fromCharCode(o1);
        } else if (h4 == 64) {
            tmp_arr[ac++] = String.fromCharCode(o1, o2);
        } else {
            tmp_arr[ac++] = String.fromCharCode(o1, o2, o3);
        }
    } while (i < data.length);

    dec = tmp_arr.join('');
    dec = wdd_utf8_decode(dec);

    return dec;
}

function wdd_utf8_decode (str_data) {
    // http://kevin.vanzonneveld.net
    // +   original by: Webtoolkit.info (http://www.webtoolkit.info/)
    // +      input by: Aman Gupta
    // +   improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
    // +   improved by: Norman "zEh" Fuchs
    // +   bugfixed by: hitwork
    // +   bugfixed by: Onno Marsman
    // +      input by: Brett Zamir (http://brett-zamir.me)
    // +   bugfixed by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
    // *     example 1: utf8_decode('Kevin van Zonneveld');
    // *     returns 1: 'Kevin van Zonneveld'
    var tmp_arr = [],
        i = 0,
        ac = 0,
        c1 = 0,
        c2 = 0,
        c3 = 0;

    str_data += '';

    while (i < str_data.length) {
        c1 = str_data.charCodeAt(i);
        if (c1 < 128) {
            tmp_arr[ac++] = String.fromCharCode(c1);
            i++;
        } else if (c1 > 191 && c1 < 224) {
            c2 = str_data.charCodeAt(i + 1);
            tmp_arr[ac++] = String.fromCharCode(((c1 & 31) << 6) | (c2 & 63));
            i += 2;
        } else {
            c2 = str_data.charCodeAt(i + 1);
            c3 = str_data.charCodeAt(i + 2);
            tmp_arr[ac++] = String.fromCharCode(((c1 & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
            i += 3;
        }
    }

    return tmp_arr.join('');
}


// POLL LOGIC
function checkPoll(){
  
  var pollId = jQuery('.widget-poll input[name=poll_id]').val();
  var cookieName =  'cwppoll' + pollId;
  if(pollId > 0 && WDD_Popup_Get_Cookie( cookieName) ){

     var form = jQuery('.widget-poll .show-form' + pollId);
     form.css('display', 'none');

     var results = jQuery('.widget-poll .poll-show-results');
     results.css('display', 'block');

  }
}

function vote_poll(pollid, answertype, maxnoanswers){
    
    if(answertype == 'multiple')
    {
        var answersCheckedCount = jQuery("#poll"+ pollid +" input[type=checkbox]:checked").length;
        if(answersCheckedCount < 1){
          alert('Click on the different options to vote and view results');
          return false;
        }
        
        data = jQuery('#poll'+pollid).serialize();
        var n=data.match(/option/g);
        if(parseInt(n.length) <= parseInt(maxnoanswers))
            {
                jQuery('#show-form'+pollid).fadeOut(500);
                jQuery('#show-results'+pollid).css('display', 'none');
                jQuery.post(ajaxurl, data,  
                    function(response){
                        jQuery('#poll'+pollid).html(response);
                        jQuery('#pollsc'+pollid).html(response);
                    }
                );
            }
        else jAlert("Sorry! Maximum no of answers allowed is " + maxnoanswers, "Error message");
    }
    if(answertype == 'one')
    {
        var answersCheckedCount = jQuery("#poll"+ pollid +" input[type=radio]:checked").length;
        if(answersCheckedCount < 1){
          alert('Click on the different options to vote and view results');
          return false;
        }
        
        data = jQuery('#poll'+pollid).serialize();
        jQuery('#show-form'+pollid).fadeOut(500);
        jQuery('#show-results'+pollid).css('display', 'none');
        jQuery.post(ajaxurl, data,  
            function(response){
                jQuery('#poll'+pollid).html(response);
                jQuery('#pollsc'+pollid).html(response);
            }
        ); 
    }
}


function vote_poll_sc(pollid, answertype, maxnoanswers){
  
    if(answertype == 'multiple')
    {
        data = jQuery('#pollsc'+pollid).serialize();
        var n=data.match(/option/g);
        if(parseInt(n.length) <= parseInt(maxnoanswers))
            {
                jQuery('#show-form'+pollid).fadeOut(500);
                jQuery('#show-results'+pollid).css('display', 'none');
                jQuery.post(ajaxurl, data,  
                    function(response){
                        jQuery('#poll'+pollid).html(response);
                        jQuery('#pollsc'+pollid).html(response);
                    }
                );
            }
        else jAlert("Sorry! Maximum no of answers allowed is " + maxnoanswers, "Error message");
    }
    if(answertype == 'one')
    {
        data = jQuery('#pollsc'+pollid).serialize();
        jQuery('#show-form'+pollid).fadeOut(500);
        jQuery('#show-results'+pollid).css('display', 'none');
        jQuery.post(ajaxurl, data,  
            function(response){
                jQuery('#poll'+pollid).html(response);
                jQuery('#pollsc'+pollid).html(response);
            }
        ); 
    }    
}

/* AUTOCOMPLETE */
(function($){function fnFormatResult(a,b,c){var d="("+c.replace(reEscape,"\\$1")+")";return a.replace(new RegExp(d,"gi"),"<strong>$1</strong>")}function Autocomplete(a,b){this.el=$(a);this.el.attr("autocomplete","off");this.suggestions=[];this.data=[];this.badQueries=[];this.selectedIndex=-1;this.currentValue=this.el.val();this.intervalId=0;this.cachedResponse=[];this.onChangeInterval=null;this.onChange=null;this.ignoreValueChange=false;this.serviceUrl=b.serviceUrl;this.isLocal=false;this.options={autoSubmit:false,minChars:1,maxHeight:300,deferRequestBy:0,width:0,highlight:true,params:{},fnFormatResult:fnFormatResult,delimiter:null,zIndex:9999};this.initialize();this.setOptions(b);this.el.data("autocomplete",this)}var reEscape=new RegExp("(\\"+["/",".","*","+","?","|","(",")","[","]","{","}","\\"].join("|\\")+")","g");$.fn.autocomplete=function(a,b){var c;if(typeof a=="string"){c=this.data("autocomplete");if(typeof c[a]=="function"){c[a](b)}}else{c=new Autocomplete(this.get(0)||$("<input />"),a)}return c};Autocomplete.prototype={killerFn:null,initialize:function(){var a,b,c;a=this;b=Math.floor(Math.random()*1048576).toString(16);c="Autocomplete_"+b;this.killerFn=function(b){if($(b.target).parents(".autocomplete").size()===0){a.killSuggestions();a.disableKillerFn()}};if(!this.options.width){this.options.width=this.el.width()}this.mainContainerId="AutocompleteContainter_"+b;$('<div id="'+this.mainContainerId+'" style="position:absolute;z-index:9999;"><div class="autocomplete-w1"><div class="autocomplete" id="'+c+'" style="display:none; width:300px;"></div></div></div>').appendTo("body");this.container=$("#"+c);this.fixPosition();if(window.opera){this.el.keypress(function(b){a.onKeyPress(b)})}else{this.el.keydown(function(b){a.onKeyPress(b)})}this.el.keyup(function(b){a.onKeyUp(b)});this.el.blur(function(){a.enableKillerFn()});this.el.focus(function(){a.fixPosition()});this.el.change(function(){a.onValueChanged()})},extendOptions:function(a){$.extend(this.options,a)},setOptions:function(a){var b=this.options;this.extendOptions(a);if(b.lookup||b.isLocal){this.isLocal=true;if($.isArray(b.lookup)){b.lookup={suggestions:b.lookup,data:[]}}}$("#"+this.mainContainerId).css({zIndex:b.zIndex});this.container.css({maxHeight:b.maxHeight+"px",width:b.width})},clearCache:function(){this.cachedResponse=[];this.badQueries=[]},disable:function(){this.disabled=true},enable:function(){this.disabled=false},fixPosition:function(){var a=this.el.offset();$("#"+this.mainContainerId).css({top:a.top+this.el.innerHeight()+"px",left:a.left+"px"})},enableKillerFn:function(){var a=this;$(document).bind("click",a.killerFn)},disableKillerFn:function(){var a=this;$(document).unbind("click",a.killerFn)},killSuggestions:function(){var a=this;this.stopKillSuggestions();this.intervalId=window.setInterval(function(){a.hide();a.stopKillSuggestions()},300)},stopKillSuggestions:function(){window.clearInterval(this.intervalId)},onValueChanged:function(){this.change(this.selectedIndex)},onKeyPress:function(a){if(this.disabled||!this.enabled){return}switch(a.keyCode){case 27:this.el.val(this.currentValue);this.hide();break;case 9:case 13:if(this.selectedIndex===-1){this.hide();return}this.select(this.selectedIndex);if(a.keyCode===9){return}break;case 38:this.moveUp();break;case 40:this.moveDown();break;default:return}a.stopImmediatePropagation();a.preventDefault()},onKeyUp:function(a){if(this.disabled){return}switch(a.keyCode){case 38:case 40:return}clearInterval(this.onChangeInterval);if(this.currentValue!==this.el.val()){if(this.options.deferRequestBy>0){var b=this;this.onChangeInterval=setInterval(function(){b.onValueChange()},this.options.deferRequestBy)}else{this.onValueChange()}}},onValueChange:function(){clearInterval(this.onChangeInterval);this.currentValue=this.el.val();var a=this.getQuery(this.currentValue);this.selectedIndex=-1;if(this.ignoreValueChange){this.ignoreValueChange=false;return}if(a===""||a.length<this.options.minChars){this.hide()}else{this.getSuggestions(a)}},getQuery:function(a){var b,c;b=this.options.delimiter;if(!b){return $.trim(a)}c=a.split(b);return $.trim(c[c.length-1])},getSuggestionsLocal:function(a){var b,c,d,e,f;c=this.options.lookup;d=c.suggestions.length;b={suggestions:[],data:[]};a=a.toLowerCase();for(f=0;f<d;f++){e=c.suggestions[f];if(e.toLowerCase().indexOf(a)===0){b.suggestions.push(e);b.data.push(c.data[f])}}return b},getSuggestions:function(a){var b,c;b=this.isLocal?this.getSuggestionsLocal(a):this.cachedResponse[a];if(b&&$.isArray(b.suggestions)){this.suggestions=b.suggestions;this.data=b.data;this.suggest()}else if(!this.isBadQuery(a)){c=this;c.options.params.query=a;$.get(this.serviceUrl,c.options.params,function(a){c.processResponse(a)},"text")}},isBadQuery:function(a){var b=this.badQueries.length;while(b--){if(a.indexOf(this.badQueries[b])===0){return true}}return false},hide:function(){this.enabled=false;this.selectedIndex=-1;this.container.hide()},suggest:function(){if(this.suggestions.length===0){this.hide();return}var a,b,c,d,e,f,g,h,i;a=this;b=this.suggestions.length;d=this.options.fnFormatResult;e=this.getQuery(this.currentValue);h=function(b){return function(){a.activate(b)}};i=function(b){return function(){a.select(b)}};this.container.hide().empty();for(f=0;f<b;f++){g=this.suggestions[f];c=$((a.selectedIndex===f?'<div class="selected"':"<div")+' title="'+g+'">'+d(g,this.data[f],e)+"</div>");c.mouseover(h(f));c.click(i(f));this.container.append(c)}this.enabled=true;this.container.show()},processResponse:function(text){var response;try{response=eval("("+text+")")}catch(err){return}if(!$.isArray(response.data)){response.data=[]}if(!this.options.noCache){this.cachedResponse[response.query]=response;if(response.suggestions.length===0){this.badQueries.push(response.query)}}if(response.query===this.getQuery(this.currentValue)){this.suggestions=response.suggestions;this.data=response.data;this.suggest()}},activate:function(a){var b,c;b=this.container.children();if(this.selectedIndex!==-1&&b.length>this.selectedIndex){$(b.get(this.selectedIndex)).removeClass()}this.selectedIndex=a;if(this.selectedIndex!==-1&&b.length>this.selectedIndex){c=b.get(this.selectedIndex);$(c).addClass("selected")}return c},deactivate:function(a,b){a.className="";if(this.selectedIndex===b){this.selectedIndex=-1}},select:function(a){var b,c;b=this.suggestions[a];if(b){this.el.val(b);if(this.options.autoSubmit){c=this.el.parents("form");if(c.length>0){c.get(0).submit()}}this.ignoreValueChange=true;this.hide();this.onSelect(a)}},change:function(a){var b,c,d;d=this;b=this.suggestions[a];if(b){var e,f;e=d.suggestions[a];f=d.data[a];d.el.val(d.getValue(e))}else{e="";f=-1}c=d.options.onChange;if($.isFunction(c)){c(e,f,d.el)}},moveUp:function(){if(this.selectedIndex===-1){return}if(this.selectedIndex===0){this.container.children().get(0).className="";this.selectedIndex=-1;this.el.val(this.currentValue);return}this.adjustScroll(this.selectedIndex-1)},moveDown:function(){if(this.selectedIndex===this.suggestions.length-1){return}this.adjustScroll(this.selectedIndex+1)},adjustScroll:function(a){var b,c,d,e;b=this.activate(a);c=b.offsetTop;d=this.container.scrollTop();e=d+this.options.maxHeight-25;if(c<d){this.container.scrollTop(c)}else if(c>e){this.container.scrollTop(c-this.options.maxHeight+25)}this.el.val(this.getValue(this.suggestions[a]))},onSelect:function(a){var b,c,d,e;b=this;c=b.options.onSelect;d=b.suggestions[a];e=b.data[a];b.el.val(b.getValue(d));if($.isFunction(c)){c(d,e,b.el)}},getValue:function(a){var b,c,d,e;e=this;b=e.options.delimiter;if(!b){return a}c=e.currentValue;d=c.split(b);if(d.length===1){return a}return c.substr(0,c.length-d[d.length-1].length)+a}}})(jQuery)


/* HIGHLIGHTING */

var hljs=new function(){function m(p){return p.replace(/&/gm,"&amp;").replace(/</gm,"&lt;")}function c(r){for(var p=0;p<r.childNodes.length;p++){var q=r.childNodes[p];if(q.nodeName=="CODE"){return q}if(!(q.nodeType==3&&q.nodeValue.match(/\s+/))){break}}}var b=(typeof navigator!=="undefined"&&/MSIE [678]/.test(navigator.userAgent));function i(t,s){var p="";for(var r=0;r<t.childNodes.length;r++){if(t.childNodes[r].nodeType==3){var q=t.childNodes[r].nodeValue;if(s){q=q.replace(/\n/g,"")}p+=q}else{if(t.childNodes[r].nodeName=="BR"){p+="\n"}else{p+=i(t.childNodes[r])}}}if(b){p=p.replace(/\r/g,"\n")}return p}function a(s){var r=s.className.split(/\s+/);r=r.concat(s.parentNode.className.split(/\s+/));for(var q=0;q<r.length;q++){var p=r[q].replace(/^language-/,"");if(f[p]||p=="no-highlight"){return p}}}function d(r){var p=[];(function q(t,u){for(var s=0;s<t.childNodes.length;s++){if(t.childNodes[s].nodeType==3){u+=t.childNodes[s].nodeValue.length}else{if(t.childNodes[s].nodeName=="BR"){u+=1}else{if(t.childNodes[s].nodeType==1){p.push({event:"start",offset:u,node:t.childNodes[s]});u=q(t.childNodes[s],u);p.push({event:"stop",offset:u,node:t.childNodes[s]})}}}}return u})(r,0);return p}function k(y,w,x){var q=0;var z="";var s=[];function u(){if(y.length&&w.length){if(y[0].offset!=w[0].offset){return(y[0].offset<w[0].offset)?y:w}else{return w[0].event=="start"?y:w}}else{return y.length?y:w}}function t(D){var A="<"+D.nodeName.toLowerCase();for(var B=0;B<D.attributes.length;B++){var C=D.attributes[B];A+=" "+C.nodeName.toLowerCase();if(C.value!==undefined&&C.value!==false&&C.value!==null){A+='="'+m(C.value)+'"'}}return A+">"}while(y.length||w.length){var v=u().splice(0,1)[0];z+=m(x.substr(q,v.offset-q));q=v.offset;if(v.event=="start"){z+=t(v.node);s.push(v.node)}else{if(v.event=="stop"){var p,r=s.length;do{r--;p=s[r];z+=("</"+p.nodeName.toLowerCase()+">")}while(p!=v.node);s.splice(r,1);while(r<s.length){z+=t(s[r]);r++}}}}return z+m(x.substr(q))}function g(r){function p(t,s){return RegExp(t,"m"+(r.cI?"i":"")+(s?"g":""))}function q(z,x){if(z.compiled){return}z.compiled=true;var u=[];if(z.k){var s={};function A(E,D){var B=D.split(" ");for(var t=0;t<B.length;t++){var C=B[t].split("|");s[C[0]]=[E,C[1]?Number(C[1]):1];u.push(C[0])}}z.lR=p(z.l||hljs.IR,true);if(typeof z.k=="string"){A("keyword",z.k)}else{for(var y in z.k){if(!z.k.hasOwnProperty(y)){continue}A(y,z.k[y])}}z.k=s}if(x){if(z.bWK){z.b="\\b("+u.join("|")+")\\s"}z.bR=p(z.b?z.b:"\\B|\\b");if(!z.e&&!z.eW){z.e="\\B|\\b"}if(z.e){z.eR=p(z.e)}z.tE=z.e||"";if(z.eW&&x.tE){z.tE+=(z.e?"|":"")+x.tE}}if(z.i){z.iR=p(z.i)}if(z.r===undefined){z.r=1}if(!z.c){z.c=[]}for(var w=0;w<z.c.length;w++){if(z.c[w]=="self"){z.c[w]=z}q(z.c[w],z)}if(z.starts){q(z.starts,x)}var v=[];for(var w=0;w<z.c.length;w++){v.push(z.c[w].b)}if(z.tE){v.push(z.tE)}if(z.i){v.push(z.i)}z.t=v.length?p(v.join("|"),true):null}q(r)}function e(D,E){function s(r,N){for(var M=0;M<N.c.length;M++){var L=N.c[M].bR.exec(r);if(L&&L.index==0){return N.c[M]}}}function v(L,r){if(p[L].e&&p[L].eR.test(r)){return 1}if(p[L].eW){var M=v(L-1,r);return M?M+1:0}return 0}function w(r,L){return L.i&&L.iR.test(r)}function q(L,r){var M=p[p.length-1];if(M.t){M.t.lastIndex=r;return M.t.exec(L)}}function A(N,r){var L=F.cI?r[0].toLowerCase():r[0];var M=N.k[L];if(M&&M instanceof Array){return M}return false}function G(L,P){L=m(L);if(!P.k){return L}var r="";var O=0;P.lR.lastIndex=0;var M=P.lR.exec(L);while(M){r+=L.substr(O,M.index-O);var N=A(P,M);if(N){y+=N[1];r+='<span class="'+N[0]+'">'+M[0]+"</span>"}else{r+=M[0]}O=P.lR.lastIndex;M=P.lR.exec(L)}return r+L.substr(O)}function B(L,M){var r;if(M.sL==""){r=h(L)}else{r=e(M.sL,L)}if(M.r>0){y+=r.keyword_count;C+=r.r}return'<span class="'+r.language+'">'+r.value+"</span>"}function K(r,L){if(L.sL&&f[L.sL]||L.sL==""){return B(r,L)}else{return G(r,L)}}function J(M,r){var L=M.cN?'<span class="'+M.cN+'">':"";if(M.rB){z+=L;M.buffer=""}else{if(M.eB){z+=m(r)+L;M.buffer=""}else{z+=L;M.buffer=r}}p.push(M);C+=M.r}function H(N,M){var Q=p[p.length-1];if(M===undefined){z+=K(Q.buffer+N,Q);return}var P=s(M,Q);if(P){z+=K(Q.buffer+N,Q);J(P,M);return P.rB}var L=v(p.length-1,M);if(L){var O=Q.cN?"</span>":"";if(Q.rE){z+=K(Q.buffer+N,Q)+O}else{if(Q.eE){z+=K(Q.buffer+N,Q)+O+m(M)}else{z+=K(Q.buffer+N+M,Q)+O}}while(L>1){O=p[p.length-2].cN?"</span>":"";z+=O;L--;p.length--}var r=p[p.length-1];p.length--;p[p.length-1].buffer="";if(r.starts){J(r.starts,"")}return Q.rE}if(w(M,Q)){throw"Illegal"}}var F=f[D];g(F);var p=[F];F.buffer="";var C=0;var y=0;var z="";try{var x,u=0;while(true){x=q(E,u);if(!x){break}var t=H(E.substr(u,x.index-u),x[0]);u=x.index+(t?0:x[0].length)}H(E.substr(u),undefined);return{r:C,keyword_count:y,value:z,language:D}}catch(I){if(I=="Illegal"){return{r:0,keyword_count:0,value:m(E)}}else{throw I}}}function h(t){var p={keyword_count:0,r:0,value:m(t)};var r=p;for(var q in f){if(!f.hasOwnProperty(q)){continue}var s=e(q,t);s.language=q;if(s.keyword_count+s.r>r.keyword_count+r.r){r=s}if(s.keyword_count+s.r>p.keyword_count+p.r){r=p;p=s}}if(r.language){p.second_best=r}return p}function j(r,q,p){if(q){r=r.replace(/^((<[^>]+>|\t)+)/gm,function(t,w,v,u){return w.replace(/\t/g,q)})}if(p){r=r.replace(/\n/g,"<br>")}return r}function n(t,w,r){var x=i(t,r);var v=a(t);var y,s;if(v=="no-highlight"){return}if(v){y=e(v,x)}else{y=h(x);v=y.language}var q=d(t);if(q.length){s=document.createElement("pre");s.innerHTML=y.value;y.value=k(q,d(s),x)}y.value=j(y.value,w,r);var u=t.className;if(!u.match("(\\s|^)(language-)?"+v+"(\\s|$)")){u=u?(u+" "+v):v}if(b&&t.tagName=="CODE"&&t.parentNode.tagName=="PRE"){s=t.parentNode;var p=document.createElement("div");p.innerHTML="<pre><code>"+y.value+"</code></pre>";t=p.firstChild.firstChild;p.firstChild.cN=s.cN;s.parentNode.replaceChild(p.firstChild,s)}else{t.innerHTML=y.value}t.className=u;t.result={language:v,kw:y.keyword_count,re:y.r};if(y.second_best){t.second_best={language:y.second_best.language,kw:y.second_best.keyword_count,re:y.second_best.r}}}function o(){if(o.called){return}o.called=true;var r=document.getElementsByTagName("pre");for(var p=0;p<r.length;p++){var q=c(r[p]);if(q){n(q,hljs.tabReplace)}}}function l(){if(window.addEventListener){window.addEventListener("DOMContentLoaded",o,false);window.addEventListener("load",o,false)}else{if(window.attachEvent){window.attachEvent("onload",o)}else{window.onload=o}}}var f={};this.LANGUAGES=f;this.highlight=e;this.highlightAuto=h;this.fixMarkup=j;this.highlightBlock=n;this.initHighlighting=o;this.initHighlightingOnLoad=l;this.IR="[a-zA-Z][a-zA-Z0-9_]*";this.UIR="[a-zA-Z_][a-zA-Z0-9_]*";this.NR="\\b\\d+(\\.\\d+)?";this.CNR="(\\b0[xX][a-fA-F0-9]+|(\\b\\d+(\\.\\d*)?|\\.\\d+)([eE][-+]?\\d+)?)";this.BNR="\\b(0b[01]+)";this.RSR="!|!=|!==|%|%=|&|&&|&=|\\*|\\*=|\\+|\\+=|,|\\.|-|-=|/|/=|:|;|<|<<|<<=|<=|=|==|===|>|>=|>>|>>=|>>>|>>>=|\\?|\\[|\\{|\\(|\\^|\\^=|\\||\\|=|\\|\\||~";this.BE={b:"\\\\[\\s\\S]",r:0};this.ASM={cN:"string",b:"'",e:"'",i:"\\n",c:[this.BE],r:0};this.QSM={cN:"string",b:'"',e:'"',i:"\\n",c:[this.BE],r:0};this.CLCM={cN:"comment",b:"//",e:"$"};this.CBLCLM={cN:"comment",b:"/\\*",e:"\\*/"};this.HCM={cN:"comment",b:"#",e:"$"};this.NM={cN:"number",b:this.NR,r:0};this.CNM={cN:"number",b:this.CNR,r:0};this.BNM={cN:"number",b:this.BNR,r:0};this.inherit=function(r,s){var p={};for(var q in r){p[q]=r[q]}if(s){for(var q in s){p[q]=s[q]}}return p}}();hljs.LANGUAGES.bash=function(a){var f="true false";var c={cN:"variable",b:"\\$[a-zA-Z0-9_]+\\b"};var b={cN:"variable",b:"\\${([^}]|\\\\})+}"};var g={cN:"string",b:'"',e:'"',i:"\\n",c:[a.BE,c,b],r:0};var d={cN:"string",b:"'",e:"'",c:[{b:"''"}],r:0};var e={cN:"test_condition",b:"",e:"",c:[g,d,c,b],k:{literal:f},r:0};return{k:{keyword:"if then else fi for break continue while in do done echo exit return set declare",literal:f},c:[{cN:"shebang",b:"(#!\\/bin\\/bash)|(#!\\/bin\\/sh)",r:10},c,b,a.HCM,g,d,a.inherit(e,{b:"\\[ ",e:" \\]",r:0}),a.inherit(e,{b:"\\[\\[ ",e:" \\]\\]"})]}}(hljs);hljs.LANGUAGES.diff=function(a){return{cI:true,c:[{cN:"chunk",b:"^\\@\\@ +\\-\\d+,\\d+ +\\+\\d+,\\d+ +\\@\\@$",r:10},{cN:"chunk",b:"^\\*\\*\\* +\\d+,\\d+ +\\*\\*\\*\\*$",r:10},{cN:"chunk",b:"^\\-\\-\\- +\\d+,\\d+ +\\-\\-\\-\\-$",r:10},{cN:"header",b:"Index: ",e:"$"},{cN:"header",b:"=====",e:"=====$"},{cN:"header",b:"^\\-\\-\\-",e:"$"},{cN:"header",b:"^\\*{3} ",e:"$"},{cN:"header",b:"^\\+\\+\\+",e:"$"},{cN:"header",b:"\\*{5}",e:"\\*{5}$"},{cN:"addition",b:"^\\+",e:"$"},{cN:"deletion",b:"^\\-",e:"$"},{cN:"change",b:"^\\!",e:"$"}]}}(hljs);hljs.LANGUAGES.javascript=function(a){return{k:{keyword:"in if for while finally var new function do return void else break catch instanceof with throw case default try this switch continue typeof delete let yield const",literal:"true false null undefined NaN Infinity"},c:[a.ASM,a.QSM,a.CLCM,a.CBLCLM,a.CNM,{b:"("+a.RSR+"|\\b(case|return|throw)\\b)\\s*",k:"return throw case",c:[a.CLCM,a.CBLCLM,{cN:"regexp",b:"/",e:"/[gim]*",c:[{b:"\\\\/"}]}],r:0},{cN:"function",bWK:true,e:"{",k:"function",c:[{cN:"title",b:"[A-Za-z$_][0-9A-Za-z$_]*"},{cN:"params",b:"\\(",e:"\\)",c:[a.CLCM,a.CBLCLM],i:"[\"'\\(]"}],i:"\\[|%"}]}}(hljs);hljs.LANGUAGES.css=function(a){var b={cN:"function",b:a.IR+"\\(",e:"\\)",c:[a.NM,a.ASM,a.QSM]};return{cI:true,i:"[=/|']",c:[a.CBLCLM,{cN:"id",b:"\\#[A-Za-z0-9_-]+"},{cN:"class",b:"\\.[A-Za-z0-9_-]+",r:0},{cN:"attr_selector",b:"\\[",e:"\\]",i:"$"},{cN:"pseudo",b:":(:)?[a-zA-Z0-9\\_\\-\\+\\(\\)\\\"\\']+"},{cN:"at_rule",b:"@(font-face|page)",l:"[a-z-]+",k:"font-face page"},{cN:"at_rule",b:"@",e:"[{;]",eE:true,k:"import page media charset",c:[b,a.ASM,a.QSM,a.NM]},{cN:"tag",b:a.IR,r:0},{cN:"rules",b:"{",e:"}",i:"[^\\s]",r:0,c:[a.CBLCLM,{cN:"rule",b:"[^\\s]",rB:true,e:";",eW:true,c:[{cN:"attribute",b:"[A-Z\\_\\.\\-]+",e:":",eE:true,i:"[^\\s]",starts:{cN:"value",eW:true,eE:true,c:[b,a.NM,a.QSM,a.ASM,a.CBLCLM,{cN:"hexcolor",b:"\\#[0-9A-F]+"},{cN:"important",b:"!important"}]}}]}]}]}}(hljs);hljs.LANGUAGES.xml=function(a){var c="[A-Za-z0-9\\._:-]+";var b={eW:true,c:[{cN:"attribute",b:c,r:0},{b:'="',rB:true,e:'"',c:[{cN:"value",b:'"',eW:true}]},{b:"='",rB:true,e:"'",c:[{cN:"value",b:"'",eW:true}]},{b:"=",c:[{cN:"value",b:"[^\\s/>]+"}]}]};return{cI:true,c:[{cN:"pi",b:"<\\?",e:"\\?>",r:10},{cN:"doctype",b:"<!DOCTYPE",e:">",r:10,c:[{b:"\\[",e:"\\]"}]},{cN:"comment",b:"<!--",e:"-->",r:10},{cN:"cdata",b:"<\\!\\[CDATA\\[",e:"\\]\\]>",r:10},{cN:"tag",b:"<style(?=\\s|>|$)",e:">",k:{title:"style"},c:[b],starts:{e:"</style>",rE:true,sL:"css"}},{cN:"tag",b:"<script(?=\\s|>|$)",e:">",k:{title:"script"},c:[b],starts:{e:"<\/script>",rE:true,sL:"javascript"}},{b:"<%",e:"%>",sL:"vbscript"},{cN:"tag",b:"</?",e:"/?>",c:[{cN:"title",b:"[^ />]+"},b]}]}}(hljs);hljs.LANGUAGES.http=function(a){return{i:"\\S",c:[{cN:"status",b:"^HTTP/[0-9\\.]+",e:"$",c:[{cN:"number",b:"\\b\\d{3}\\b"}]},{cN:"request",b:"^[A-Z]+ (.*?) HTTP/[0-9\\.]+$",rB:true,e:"$",c:[{cN:"string",b:" ",e:" ",eB:true,eE:true}]},{cN:"attribute",b:"^\\w",e:": ",eE:true,i:"\\n|\\s|=",starts:{cN:"string",e:"$"}},{b:"\\n\\n",starts:{sL:"",eW:true}}]}}(hljs);hljs.LANGUAGES.php=function(a){var e={cN:"variable",b:"\\$+[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*"};var b=[a.inherit(a.ASM,{i:null}),a.inherit(a.QSM,{i:null}),{cN:"string",b:'b"',e:'"',c:[a.BE]},{cN:"string",b:"b'",e:"'",c:[a.BE]}];var c=[a.CNM,a.BNM];var d={cN:"title",b:a.UIR};return{cI:true,k:"and include_once list abstract global private echo interface as static endswitch array null if endwhile or const for endforeach self var while isset public protected exit foreach throw elseif include __FILE__ empty require_once do xor return implements parent clone use __CLASS__ __LINE__ else break print eval new catch __METHOD__ case exception php_user_filter default die require __FUNCTION__ enddeclare final try this switch continue endfor endif declare unset true false namespace trait goto instanceof insteadof __DIR__ __NAMESPACE__ __halt_compiler",c:[a.CLCM,a.HCM,{cN:"comment",b:"/\\*",e:"\\*/",c:[{cN:"phpdoc",b:"\\s@[A-Za-z]+"}]},{cN:"comment",eB:true,b:"__halt_compiler.+?;",eW:true},{cN:"string",b:"<<<['\"]?\\w+['\"]?$",e:"^\\w+;",c:[a.BE]},{cN:"preprocessor",b:"<\\?php",r:10},{cN:"preprocessor",b:"\\?>"},e,{cN:"function",bWK:true,e:"{",k:"function",i:"\\$|\\[|%",c:[d,{cN:"params",b:"\\(",e:"\\)",c:["self",e,a.CBLCLM].concat(b).concat(c)}]},{cN:"class",bWK:true,e:"{",k:"class",i:"[:\\(\\$]",c:[{bWK:true,eW:true,k:"extends",c:[d]},d]},{b:"=>"}].concat(b).concat(c)}}(hljs);hljs.LANGUAGES.sql=function(a){return{cI:true,i:"[^\\s]",c:[{cN:"operator",b:"(begin|start|commit|rollback|savepoint|lock|alter|create|drop|rename|call|delete|do|handler|insert|load|replace|select|truncate|update|set|show|pragma|grant)\\b",e:";",eW:true,k:{keyword:"all partial global month current_timestamp using go revoke smallint indicator end-exec disconnect zone with character assertion to add current_user usage input local alter match collate real then rollback get read timestamp session_user not integer bit unique day minute desc insert execute like ilike|2 level decimal drop continue isolation found where constraints domain right national some module transaction relative second connect escape close system_user for deferred section cast current sqlstate allocate intersect deallocate numeric public preserve full goto initially asc no key output collation group by union session both last language constraint column of space foreign deferrable prior connection unknown action commit view or first into float year primary cascaded except restrict set references names table outer open select size are rows from prepare distinct leading create only next inner authorization schema corresponding option declare precision immediate else timezone_minute external varying translation true case exception join hour default double scroll value cursor descriptor values dec fetch procedure delete and false int is describe char as at in varchar null trailing any absolute current_time end grant privileges when cross check write current_date pad begin temporary exec time update catalog user sql date on identity timezone_hour natural whenever interval work order cascade diagnostics nchar having left call do handler load replace truncate start lock show pragma",aggregate:"count sum min max avg"},c:[{cN:"string",b:"'",e:"'",c:[a.BE,{b:"''"}],r:0},{cN:"string",b:'"',e:'"',c:[a.BE,{b:'""'}],r:0},{cN:"string",b:"`",e:"`",c:[a.BE]},a.CNM]},a.CBLCLM,{cN:"comment",b:"--",e:"$"}]}}(hljs);hljs.LANGUAGES.json=function(a){var e={literal:"true false null"};var d=[a.QSM,a.CNM];var c={cN:"value",e:",",eW:true,eE:true,c:d,k:e};var b={b:"{",e:"}",c:[{cN:"attribute",b:'\\s*"',e:'"\\s*:\\s*',eB:true,eE:true,c:[a.BE],i:"\\n",starts:c}],i:"\\S"};var f={b:"\\[",e:"\\]",c:[a.inherit(c,{cN:null})],i:"\\S"};d.splice(d.length,0,b,f);return{c:d,k:e,i:"\\S"}}(hljs);


/* AC RUN ACTIVE CONTENT */
AC_FL_RunContent = 0;
//v1.7
// Flash Player Version Detection
// Detect Client Browser type
// Copyright 2005-2007 Adobe Systems Incorporated.  All rights reserved.
var isIE  = (navigator.appVersion.indexOf("MSIE") != -1) ? true : false;
var isWin = (navigator.appVersion.toLowerCase().indexOf("win") != -1) ? true : false;
var isOpera = (navigator.userAgent.indexOf("Opera") != -1) ? true : false;

function ControlVersion()
{
	var version;
	var axo;
	var e;

	// NOTE : new ActiveXObject(strFoo) throws an exception if strFoo isn't in the registry

	try {
		// version will be set for 7.X or greater players
		axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash.7");
		version = axo.GetVariable("$version");
	} catch (e) {
	}

	if (!version)
	{
		try {
			// version will be set for 6.X players only
			axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash.6");
			
			// installed player is some revision of 6.0
			// GetVariable("$version") crashes for versions 6.0.22 through 6.0.29,
			// so we have to be careful. 
			
			// default to the first public version
			version = "WIN 6,0,21,0";

			// throws if AllowScripAccess does not exist (introduced in 6.0r47)		
			axo.AllowScriptAccess = "always";

			// safe to call for 6.0r47 or greater
			version = axo.GetVariable("$version");

		} catch (e) {
		}
	}

	if (!version)
	{
		try {
			// version will be set for 4.X or 5.X player
			axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash.3");
			version = axo.GetVariable("$version");
		} catch (e) {
		}
	}

	if (!version)
	{
		try {
			// version will be set for 3.X player
			axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash.3");
			version = "WIN 3,0,18,0";
		} catch (e) {
		}
	}

	if (!version)
	{
		try {
			// version will be set for 2.X player
			axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash");
			version = "WIN 2,0,0,11";
		} catch (e) {
			version = -1;
		}
	}
	
	return version;
}

// JavaScript helper required to detect Flash Player PlugIn version information
function GetSwfVer(){
	// NS/Opera version >= 3 check for Flash plugin in plugin array
	var flashVer = -1;
	
	if (navigator.plugins != null && navigator.plugins.length > 0) {
		if (navigator.plugins["Shockwave Flash 2.0"] || navigator.plugins["Shockwave Flash"]) {
			var swVer2 = navigator.plugins["Shockwave Flash 2.0"] ? " 2.0" : "";
			var flashDescription = navigator.plugins["Shockwave Flash" + swVer2].description;
			var descArray = flashDescription.split(" ");
			var tempArrayMajor = descArray[2].split(".");			
			var versionMajor = tempArrayMajor[0];
			var versionMinor = tempArrayMajor[1];
			var versionRevision = descArray[3];
			if (versionRevision == "") {
				versionRevision = descArray[4];
			}
			if (versionRevision[0] == "d") {
				versionRevision = versionRevision.substring(1);
			} else if (versionRevision[0] == "r") {
				versionRevision = versionRevision.substring(1);
				if (versionRevision.indexOf("d") > 0) {
					versionRevision = versionRevision.substring(0, versionRevision.indexOf("d"));
				}
			}
			var flashVer = versionMajor + "." + versionMinor + "." + versionRevision;
		}
	}
	// MSN/WebTV 2.6 supports Flash 4
	else if (navigator.userAgent.toLowerCase().indexOf("webtv/2.6") != -1) flashVer = 4;
	// WebTV 2.5 supports Flash 3
	else if (navigator.userAgent.toLowerCase().indexOf("webtv/2.5") != -1) flashVer = 3;
	// older WebTV supports Flash 2
	else if (navigator.userAgent.toLowerCase().indexOf("webtv") != -1) flashVer = 2;
	else if ( isIE && isWin && !isOpera ) {
		flashVer = ControlVersion();
	}	
	return flashVer;
}

// When called with reqMajorVer, reqMinorVer, reqRevision returns true if that version or greater is available
function DetectFlashVer(reqMajorVer, reqMinorVer, reqRevision)
{
	versionStr = GetSwfVer();
	if (versionStr == -1 ) {
		return false;
	} else if (versionStr != 0) {
		if(isIE && isWin && !isOpera) {
			// Given "WIN 2,0,0,11"
			tempArray         = versionStr.split(" "); 	// ["WIN", "2,0,0,11"]
			tempString        = tempArray[1];			// "2,0,0,11"
			versionArray      = tempString.split(",");	// ['2', '0', '0', '11']
		} else {
			versionArray      = versionStr.split(".");
		}
		var versionMajor      = versionArray[0];
		var versionMinor      = versionArray[1];
		var versionRevision   = versionArray[2];

        	// is the major.revision >= requested major.revision AND the minor version >= requested minor
		if (versionMajor > parseFloat(reqMajorVer)) {
			return true;
		} else if (versionMajor == parseFloat(reqMajorVer)) {
			if (versionMinor > parseFloat(reqMinorVer))
				return true;
			else if (versionMinor == parseFloat(reqMinorVer)) {
				if (versionRevision >= parseFloat(reqRevision))
					return true;
			}
		}
		return false;
	}
}

function AC_AddExtension(src, ext)
{
  if (src.indexOf('?') != -1)
    return src.replace(/\?/, ext+'?'); 
  else
    return src + ext;
}

function AC_Generateobj(objAttrs, params, embedAttrs) 
{ 
  var str = '';
  if (isIE && isWin && !isOpera)
  {
    str += '<object ';
    for (var i in objAttrs)
    {
      str += i + '="' + objAttrs[i] + '" ';
    }
    str += '>';
    for (var i in params)
    {
      str += '<param name="' + i + '" value="' + params[i] + '" /> ';
    }
    str += '</object>';
  }
  else
  {
    str += '<embed ';
    for (var i in embedAttrs)
    {
      str += i + '="' + embedAttrs[i] + '" ';
    }
    str += '> </embed>';
  }

  document.write(str);
}

function AC_FL_RunContent(){
  var ret = 
    AC_GetArgs
    (  arguments, ".swf", "movie", "clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
     , "application/x-shockwave-flash"
    );
  AC_Generateobj(ret.objAttrs, ret.params, ret.embedAttrs);
}

function AC_SW_RunContent(){
  var ret = 
    AC_GetArgs
    (  arguments, ".dcr", "src", "clsid:166B1BCA-3F9C-11CF-8075-444553540000"
     , null
    );
  AC_Generateobj(ret.objAttrs, ret.params, ret.embedAttrs);
}

function AC_GetArgs(args, ext, srcParamName, classid, mimeType){
  var ret = new Object();
  ret.embedAttrs = new Object();
  ret.params = new Object();
  ret.objAttrs = new Object();
  for (var i=0; i < args.length; i=i+2){
    var currArg = args[i].toLowerCase();    

    switch (currArg){	
      case "classid":
        break;
      case "pluginspage":
        ret.embedAttrs[args[i]] = args[i+1];
        break;
      case "src":
      case "movie":	
        args[i+1] = AC_AddExtension(args[i+1], ext);
        ret.embedAttrs["src"] = args[i+1];
        ret.params[srcParamName] = args[i+1];
        break;
      case "onafterupdate":
      case "onbeforeupdate":
      case "onblur":
      case "oncellchange":
      case "onclick":
      case "ondblclick":
      case "ondrag":
      case "ondragend":
      case "ondragenter":
      case "ondragleave":
      case "ondragover":
      case "ondrop":
      case "onfinish":
      case "onfocus":
      case "onhelp":
      case "onmousedown":
      case "onmouseup":
      case "onmouseover":
      case "onmousemove":
      case "onmouseout":
      case "onkeypress":
      case "onkeydown":
      case "onkeyup":
      case "onload":
      case "onlosecapture":
      case "onpropertychange":
      case "onreadystatechange":
      case "onrowsdelete":
      case "onrowenter":
      case "onrowexit":
      case "onrowsinserted":
      case "onstart":
      case "onscroll":
      case "onbeforeeditfocus":
      case "onactivate":
      case "onbeforedeactivate":
      case "ondeactivate":
      case "type":
      case "codebase":
      case "id":
        ret.objAttrs[args[i]] = args[i+1];
        break;
      case "width":
      case "height":
      case "align":
      case "vspace": 
      case "hspace":
      case "class":
      case "title":
      case "accesskey":
      case "name":
      case "tabindex":
        ret.embedAttrs[args[i]] = ret.objAttrs[args[i]] = args[i+1];
        break;
      default:
        ret.embedAttrs[args[i]] = ret.params[args[i]] = args[i+1];
    }
  }
  ret.objAttrs["classid"] = classid;
  if (mimeType) ret.embedAttrs["type"] = mimeType;
  return ret;
}

/*
 * jQuery UI Touch Punch 0.2.2
 *
 * Copyright 2011, Dave Furfero
 * Dual licensed under the MIT or GPL Version 2 licenses.
 *
 * Depends:
 *  jquery.ui.widget.js
 *  jquery.ui.mouse.js
 */
(function(b){b.support.touch="ontouchend" in document;if(!b.support.touch){return;}var c=b.ui.mouse.prototype,e=c._mouseInit,a;function d(g,h){if(g.originalEvent.touches.length>1){return;}g.preventDefault();var i=g.originalEvent.changedTouches[0],f=document.createEvent("MouseEvents");f.initMouseEvent(h,true,true,window,1,i.screenX,i.screenY,i.clientX,i.clientY,false,false,false,false,0,null);g.target.dispatchEvent(f);}c._touchStart=function(g){var f=this;if(a||!f._mouseCapture(g.originalEvent.changedTouches[0])){return;}a=true;f._touchMoved=false;d(g,"mouseover");d(g,"mousemove");d(g,"mousedown");};c._touchMove=function(f){if(!a){return;}this._touchMoved=true;d(f,"mousemove");};c._touchEnd=function(f){if(!a){return;}d(f,"mouseup");d(f,"mouseout");if(!this._touchMoved){d(f,"click");}a=false;};c._mouseInit=function(){var f=this;f.element.bind("touchstart",b.proxy(f,"_touchStart")).bind("touchmove",b.proxy(f,"_touchMove")).bind("touchend",b.proxy(f,"_touchEnd"));e.call(f);};})(jQuery);