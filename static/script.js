let li_items = document.querySelectorAll(".side-nav-bar ul li");
let wrapper = document.querySelector(".nav-bar-wrapper");
// alert("hello world");

li_items.forEach((li_item) => {
    li_item.addEventListener("mouseenter", () => {

        li_item.closest('.nav-bar-wrapper').classList.remove("hover-collapse");

    })
})

li_items.forEach((li_item) => {
    li_item.addEventListener("mouseleave", () => {

        li_item.closest(".nav-bar-wrapper").classList.add("hover-collapse");

    })
})


