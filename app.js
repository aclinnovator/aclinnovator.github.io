$(window).scroll(function(){
	console.log("Window loaded");
		if ($(this).scrollTop() > $("header").height() + 300) {
			$('#building').slideUp(700);
		} else {
			$('#building').slideDown(700);

		}
});

$(window).resize(function(){
	console.log("Resized");
	$('header').height($(window).height());
	$('header').width($(window).width());
	$('header').height($(window).height());
	$('header').width($(window).width());

});

$(document).ready(function(){
	console.log("Document loaded");

	$('#building').slideDown(300);
	$('header').height($(window).height());
	$('header').width($(window).width());

	$('.pillar').click(function(){
		console.log("Pillar Clicked");
	});
});

var aclinnovator = new Gh3.User("aclinnovator");

aclinnovator.fetch(function(err, resultUser){
		if (err){
			throw "Outch...";
		} else {
			console.log(JSON.stringify(resultUser));
		}
});
