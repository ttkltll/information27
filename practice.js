function generateImageCode() {
    // 浏览器要发起图片验证码请求/image_code?imageCodeId=xxxxx
    imageCodeId = generateUUID()
    // 生成 url
    var url = "/image_code?imageCodeId=" + imageCodeId
    // 给指定img标签设置src,设置了地址之后，img标签就会去向这个地址发起请求，请求图片
    $(".get_pic_code").attr("src", url)
}


function generateImageCode(){

}


function generateImageCode() {
    //浏览器要发起图片验证码请请/
    imageCodeId = generateUUID()
    var url = "/image_code?imageCodeld=" + imageCodeId
    $(".get_pic_code").attr("src",url)

}


