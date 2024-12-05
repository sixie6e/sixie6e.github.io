var $parent = $("#main"),
	$aside = $("#aside"),
	$asideTarget = $aside.find(".aside--details"),
	$asideClose = $aside.find(".close"),
	$tilesParent = $(".tiles"),
	$tiles = $tilesParent.find("a"),
	slideClass = "show-detail";
	$tiles.on("click", function(e){
		e.preventDefault();
		e.stopPropagation();
		if(!$("html").hasClass(slideClass)){
			$tiles.removeClass("active");
			$(this).addClass("active");
			$(this).attr("aria-expanded","true");
			loadTileData($(this));
			}else{
				killAside();
				$(this).attr("aria-expanded","false");
				}
			});
			
		$asideClose.on("click", function(e){
			e.preventDefault();
			killAside();
		});
		
		function loadTileData(target){
			var $this = $(target),
			itemHtml = $this.find(".details").html();
			$asideTarget.html(itemHtml);
			showAside();
		}
		
		function showAside(){
			if(!$("html").hasClass(slideClass)){
				$("html").toggleClass(slideClass);
				$aside.attr("aria-hidden","false");
				focusCloseButton();
			}
		}
		
		window.addEventListener("keyup", function(e){
			var code = (e.keyCode ? e.keyCode : e.which);
			if(code === 27){
				killAside();
			}
		}, false);
		
		function killAside(){
			if($("html").hasClass(slideClass)){
				$("html").removeClass(slideClass);
				sendFocusBack();
				$aside.attr("aria-hidden","true");
				$tiles.attr("aria-expanded","false");
			}
		}
		
		function focusCloseButton(){
			$asideClose.focus();
		}
		
		function sendFocusBack(){
			$(".active").focus();
		}
		
		$parent.on("click",function(e){
			if($("html").hasClass(slideClass)){
				killAside();
			}
		});
