window.onload = choosePic;

var myPix = new Array("2B67.png","3G34.png","4B6K.png","5R8Z.png","6JJ4.png","8UDC.png","E3Y3.png","HSZ6.png","LDZ5.png","Y5VA.png");

function choosePic() {
     var randomNum = Math.floor(Math.random() * myPix.length);
     document.getElementById("myPicture").src = (r"C:\Users\SATVIKA\Desktop\integratemodel\generated_captcha_images\\").concat(myPix[randomNum]);
}