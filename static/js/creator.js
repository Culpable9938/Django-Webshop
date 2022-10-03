
var clicked=0
$(".trigger").click(function()
{
    if(clicked == 0)
    {
        $("#menu ul").css({"max-height":"200px"})
        clicked = 1;
    }
    else
    {
        $("#menu ul").css({"max-height":"0px"})
        clicked = 0;
    }
})

$(".article_color").click(function(){
    id = $(this).index()

    articleid = $(this).parent().parent().index()

    $(".creator-rigs-container article").eq(articleid).children(".article_color_variation").css({"display":"none"})
    $(".creator-rigs-container article").eq(articleid).children(".article_color_variation").eq(id).css({"display":"block"})
    $(".creator-rigs-container article").eq(articleid).children(".article_color_container").children(".article_color").css({"border-color":"transparent"})
    $(".creator-rigs-container article").eq(articleid).children(".article_color_container").children(".article_color").eq(id).css({"border-color":"#a5b0d6 "})
});

$(".creator-rigs-container article").click(function(){

    $(this).css({"border-color":"#a5b0d6"})

});

/* menu */

$().ready(function(){
    id = $(".active-menu").index() 
    left = id * 25


    $(".creator-menus-indicator").css({"display":"block","left":left  + "%", "transition":"all 0.4s"})
});

/* beads */

$(".creator-menus li").hover(function(){
    id = $(this).index()
    left = id * 25

    $(".creator-menus-indicator").css({"left":left  + "%"})
}, function(){
    id = $(".active-menu").index() 
    left = id * 25


    $(".creator-menus-indicator").css({"left":left  + "%"})
});

$(".article_image").click(function(){
    $(".article_image").css({"border":"1px solid #d3d3d3"})
    $(this).css({"border":"1px solid #a5b0d6"})
   image = $(this).attr("src")
   $(".article_image_active").attr({"src": image})
})

$(".creator-select-bead").click(function(){

    $(".bead_charm-selector-container").css({"display":"block"});
    $(".bead_charm-selector-content").css({"display":"block"});

})

$(".selector_beads_charms-container article").click(function(){

    beadid = $(this).attr("value");
    beadimage = $(this).children(".article_color_variation").children("img").attr("src")
    beadname = $(this).children("h2").text()
    beadprice = $(this).children("h4").text()


    var div = document.createElement('div')
    div.className = "list-group mb-4 mt-3"
    div.innerHTML = '<div class="list-group-item d-flex align-items-center justify-content-between" data-id="2"><input type="hidden" ><ul><li><img src="' + beadimage + '"></img></li><li><h2>' + beadname + '</h2><h3>' + beadprice + '€</h3></li><li></li></ul></div>'

    document.getElementById("sortablelist").appendChild(div)

    $(".bead_charm-selector-container").css({"display":"none"});
    $(".bead_charm-selector-content").css({"display":"none"});
});

$(".selector_close").click(function(){

    $(".bead_charm-selector-container").css({"display":"none"});
    $(".bead_charm-selector-content").css({"display":"none"});

})


new Sortable(sortablelist, {
    animation: 350,
    ghostClass: 'sortable-ghost',
    removeOnSpill:true,
  });

$(".list-group").on('click', '.list-group-item' ,function(){

    $("div").removeClass("active-tag")
    $(this).addClass("active-tag")


    activeimage = $(this).children("ul").children("li").children("img").attr("src")
    $(".article_image_active").attr({"src":activeimage})

    activename = $(this).children("ul").children("li").children("h2").text()
    $(".article_image").css({"display":"none"})
    $(".article_image[name='" + activename + "']").css({"display":"block"})

});
