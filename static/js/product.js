$(".nav ul li").click(function()
{
    id = $(this).index()

    $(".nav ul li").removeClass("active")
    $(".nav ul li").eq(id).addClass("active")

    $(".tab-content").removeClass("active")
    $(".tab-content").eq(id).addClass("active")
});