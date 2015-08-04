function loadImage() {
    var canvas = $("#canvas");
    canvas.width = 105;
    canvas.height = 130;
    var context = canvas.getContext('2d');
    var image = new Image();
    image.src = "disguise.cgi?Hacker="+$("#hacker").val()+".bmp&Mustache="+$("#mustache").val()+".bmp&Shades="+$("#shades").val()+".bmp";
    $("#spinner").show();
    var i = setInterval(draw,20,$("#spinner"),context);

    setTimeout(function(){clearInterval(i);context.drawImage(image,0,0);},wait);
    wait -= 200;
}
