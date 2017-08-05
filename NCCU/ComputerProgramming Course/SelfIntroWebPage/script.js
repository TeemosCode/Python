//jquery
var main = function() {
  
	
  $('.arrow-next').click(function() {
    var currentSlide = $('.active-slide');
    var nextSlide = currentSlide.next();
    var currentDot = $('.active-dot');
    var nextDot = currentDot.next();

    if(nextDot.length === 0) {
      nextSlide = $('.slides').first();
      nextDot = $('.dot').first();
    }
    
    currentSlide.fadeOut(600).removeClass('active-slide');
    nextSlide.fadeIn(300).addClass('active-slide');
    currentDot.removeClass('active-dot');
    nextDot.addClass('active-dot');
  });


  $('.arrow-prev').click(function() {
    var currentSlide = $('.active-slide');
    var prevSlide = currentSlide.prev();
    var currentDot = $('.active-dot');
    var prevDot = currentDot.prev();

    if(prevDot.length === 0) {
      prevSlide = $('.slides').last();
      prevDot = $('.dot').last();
    }
    
    currentSlide.fadeOut(300).removeClass('active-slide');
    prevSlide.fadeIn(300).addClass('active-slide');
    currentDot.removeClass('active-dot');
    prevDot.addClass('active-dot');
  });

}

$(document).ready(main);