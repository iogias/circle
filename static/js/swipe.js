var swiper = new Swiper(".mySwiper", {
  autoplay: {
    delay: 5000,
  },
  slidesPerView: 1,
  spaceBetween: 40,
  breakpoints: {
    // when window width is <= 320px
    320: {
      slidesPerView: 1,
      spaceBetweenSlides: 20,
    },
    // when window width is <= 480px
    480: {
      slidesPerView: 1,
      spaceBetweenSlides: 20,
    },
    // when window width is <= 640px
    640: {
      slidesPerView: 2,
      spaceBetweenSlides: 40,
    },
  },
})

var swiper_prod = new Swiper(".productSwiper", {
  slidesPerView: 4,
  spaceBetween: 40,
  breakpoints: {
    // when window width is <= 320px
    320: {
      slidesPerView: 4,
      spaceBetweenSlides: 40,
    },
    // when window width is <= 480px
    480: {
      slidesPerView: 4,
      spaceBetweenSlides: 40,
    },
    // when window width is <= 640px
    640: {
      slidesPerView: 8,
      spaceBetweenSlides: 20,
    },
  },
})
